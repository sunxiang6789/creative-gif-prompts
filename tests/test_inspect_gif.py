"""Container fixtures check frame, timing, and failure behavior."""
import base64
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('inspect_gif', Path(__file__).parents[1] / 'scripts/inspect_gif.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# A complete 1x1 GIF with a two-color global table and one image block.
SINGLE = base64.b64decode('R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw==')
HEADER = SINGLE[:19]
FRAME = SINGLE[19:-1]
CONTROL = b'\x21\xf9\x04\x00\x0f\x00\x00\x00'
LOOP = b'\x21\xff\x0bNETSCAPE2.0\x03\x01\x00\x00\x00'


class InspectGifTests(unittest.TestCase):
    def test_static_gif_is_not_animation(self):
        result = module.inspect(SINGLE)
        self.assertTrue(result['complete'])
        self.assertEqual(result['frames'], 1)
        self.assertFalse(result['animated_gif'])

    def test_multiframe_timing_and_loop(self):
        result = module.inspect(HEADER + LOOP + CONTROL + FRAME + CONTROL + FRAME + b';')
        self.assertTrue(result['animated_gif'])
        self.assertEqual(result['frames'], 2)
        self.assertEqual(result['delays_ms'], [150, 150])
        self.assertEqual(result['loop_count'], 0)

    def test_missing_trailer_does_not_pass(self):
        result = module.inspect(HEADER + FRAME + FRAME)
        self.assertEqual(result['frames'], 2)
        self.assertFalse(result['animated_gif'])
        self.assertIn('error', result)

    def test_static_png_is_not_gif(self):
        result = module.inspect(b'\x89PNG\r\n\x1a\n')
        self.assertEqual(result['format'], 'PNG')
        self.assertFalse(result['animated_gif'])

    def test_truncated_extension_does_not_pass(self):
        self.assertFalse(module.inspect(HEADER + b'\x21\xf9\x04')['animated_gif'])


if __name__ == '__main__':
    unittest.main()
