# Creative GIF Prompts

By **Sun Xiang** ([sunxiang6789](https://github.com/sunxiang6789)).

An English agent skill with 31 creative looping-GIF recipes across anime reactions, pets, doodles, art and cinema, chibi characters, and old photographs. Includes a dependency-free inspector that distinguishes actual multi-frame GIF files from static images.

## Install

Copy this repository's skill files into a `creative-gif-prompts` directory under your agent's skills directory. For Codex, the usual user location is `~/.codex/skills/creative-gif-prompts/`. The directory must contain `SKILL.md` and its `references/`, `scripts/`, and `agents/` directories. Restart or refresh skill discovery if needed.

## Use

> Use $creative-gif-prompts with this kitten photo. Create a funny dancing loop and verify that the returned file is an animated GIF.

The skill selects a suitable recipe and uses the available image workflow. It does not guarantee native GIF support and never reports a static collage as an animation. If the user requests Codex CLI, it uses the actual terminal CLI.

Inspect a result:

```sh
python3 scripts/inspect_gif.py /path/to/result.gif
```

Exit status: 0 for a structurally complete multi-frame GIF; 2 for a non-GIF, static GIF, or malformed/incomplete GIF; 1 for file access errors. Frame parsing does not decode LZW pixels, establish visual differences, or evaluate animation quality.

## Development

```sh
python3 -m unittest discover -s tests -v
```

See [authorship and source](references/source-and-authorship.md) for credit and reuse terms. Example media are not included. No API keys or third-party Python packages are required for inspection.
