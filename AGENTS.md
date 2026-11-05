# Repository instructions

## Scope
This repository contains the creative-gif-prompts skill by Sun Xiang: English instructions, 31 prompt recipes, and a dependency-free GIF inspector. Keep all maintained content in English. Never include credentials, session logs, or local account configuration.

## Boundaries
Describe capabilities from the actual available tool schema. A requested GIF is not evidence of GIF output, and a source title is not evidence of a model version. Preserve the author's original English recipe text unless a requested revision requires changes. No independent paid API, installation, conversion, or publishing is implied by invoking this skill.

## Validation
Run `python3 -m unittest discover -s tests -v` and the host skill validator when available. Confirm recipe IDs 01 through 31 are present exactly once and Markdown links resolve locally. Report the difference between structural checks and live image generation.

## Collaboration and commits
Read HANDOFF.md and inspect Git status/log before writing. Record task ownership, baseline, and scope there. Use one writer at a time. Preserve unrelated work. Update HANDOFF.md with actual changes, validation, outstanding work, and service/data state at completion. Stage named task files only and commit each independent deliverable. Push only when the user authorizes publication.

## Handoff entry point
[HANDOFF.md](HANDOFF.md) is the single state record. CLAUDE.md imports this file and the handoff.
