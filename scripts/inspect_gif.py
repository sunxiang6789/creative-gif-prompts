#!/usr/bin/env python3
"""Inspect container structure without decoding pixels or changing the file."""
import argparse
import json
from pathlib import Path


def inspect(data):
    result = {'format': 'unknown', 'frames': 0, 'delays_ms': [],
              'loop_count': None, 'complete': False, 'animated_gif': False}
    if data.startswith(b'\x89PNG\r\n\x1a\n'):
        result['format'] = 'PNG'
        return result
    if data.startswith(b'\xff\xd8\xff'):
        result['format'] = 'JPEG'
        return result
    if data[:6] not in (b'GIF87a', b'GIF89a'):
        return result
    result['format'] = data[:6].decode()
    pos = 6

    def take(n):
        nonlocal pos
        if pos + n > len(data):
            raise ValueError('Truncated GIF')
        value = data[pos:pos + n]
        pos += n
        return value

    def subblocks():
        out = []
        while True:
            n = take(1)[0]
            if n == 0:
                return out
            out.append(take(n))

    delay = 0
    try:
        screen = take(7)
        if screen[4] & 128:
            take(3 * (2 ** ((screen[4] & 7) + 1)))
        while True:
            marker = take(1)[0]
            if marker == 0x3b:
                result['complete'] = True
                break
            if marker == 0x2c:
                descriptor = take(9)
                if descriptor[8] & 128:
                    take(3 * (2 ** ((descriptor[8] & 7) + 1)))
                take(1)  # LZW minimum code size; pixel data are not decoded.
                subblocks()
                result['frames'] += 1
                result['delays_ms'].append(delay)
                delay = 0
            elif marker == 0x21:
                label = take(1)[0]
                if label == 0xf9:
                    if take(1) != b'\x04':
                        raise ValueError('Invalid graphics control extension')
                    control = take(4)
                    delay = int.from_bytes(control[1:3], 'little') * 10
                    if take(1) != b'\x00':
                        raise ValueError('Invalid graphics control terminator')
                elif label == 0xff:
                    app = take(take(1)[0])
                    blocks = subblocks()
                    if app in (b'NETSCAPE2.0', b'ANIMEXTS1.0'):
                        for block in blocks:
                            if len(block) == 3 and block[0] == 1:
                                result['loop_count'] = int.from_bytes(block[1:3], 'little')
                elif label == 0x01:
                    take(take(1)[0])
                    subblocks()
                    delay = 0  # A plain-text graphic consumes the pending control.
                else:
                    subblocks()
            else:
                raise ValueError('Unexpected GIF block marker')
    except (ValueError, IndexError) as error:
        result['error'] = str(error)
    result['animated_gif'] = result['complete'] and result['frames'] > 1
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', type=Path)
    args = parser.parse_args()
    try:
        result = inspect(args.file.read_bytes())
    except OSError as error:
        print(json.dumps({'error': str(error)}))
        return 1
    print(json.dumps(result, indent=2))
    return 0 if result['animated_gif'] else 2


if __name__ == '__main__':
    raise SystemExit(main())
