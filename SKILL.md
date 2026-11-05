---
name: creative-gif-prompts
description: Plan and generate expressive looping GIFs from photos, pets, doodles, artwork, original chibi characters, or old photographs using 31 English prompt recipes. Use for animated reaction stickers, character loops, and reference-image GIF requests; verify actual animated output.
---

# Creative GIF Prompts

Author: Sun Xiang (GitHub: sunxiang6789).

## Choose a recipe

Read only the relevant category:

| Category | Recipes | Reference |
|---|---|---|
| 1990s anime reactions from portraits | 01-06 | [Anime reactions](references/anime-reactions.md) |
| Recognizable pets with exaggerated actions | 07-12 | [Pet comedy](references/pet-comedy.md) |
| Rough drawings coming alive | 13-18 | [Doodle animation](references/doodle-animation.md) |
| Classic paintings and cinematic imagery | 19-22 | [Art and cinema](references/art-and-cinema.md) |
| Personal chibi characters and animated stickers | 23-28 | [Chibi characters](references/chibi-characters.md) |
| Restored, colorized old photographs | 29-31 | [Old photographs](references/old-photographs.md) |

Choose the closest action to the user's request; adapt the action while retaining identity and style constraints. If the user has already supplied an image or a clear action, proceed without asking them to choose a numbered recipe.

## Prepare and generate

- Use clear, unobstructed reference images for people, pets, artwork, original characters, and old photographs. Doodles can start from text alone. Inspect local reference images before editing when the tool requires it.
- Preserve faces, fur markings, clothing, proportions, composition, and the chosen visual medium. Realistic pets remain realistic; deliberately crude doodles remain crude. For old photographs, preserve apparent age and identity; restored colors are plausible reconstructions, not verified historical colors.
- Prefer one independent effect per call. Describe the starting action, its escalation, and a natural return to the starting pose. Keep the camera and background stable.
- Do not impose frame counts or frame rates by default. Preserve explicit user timing requirements and use supported animation settings when available.
- Use the tool or platform selected by the user. For Codex CLI requests, actually invoke the terminal CLI; a tool call in a desktop chat is a different invocation path. Use built-in generation when available, and inspect its current schema for native GIF options rather than inventing arguments or assuming every version supports them.
- If no native GIF control is exposed, explain the uncertainty. A user-requested prompt-only experiment may still call generation with a GIF requirement in the prompt; do not claim it will work. Do not silently change providers, use a separately billed API, install software, or synthesize/convert frames as a substitute for native generation. Those are separate approaches requiring the user's scope to include them.
- A pure green background is optional for later chroma keying, not a substitute for an alpha channel. For transparency requests, use supported transparency controls and verify the resulting alpha separately.

## Verify the artifact

Inspect the original returned file, not its extension or thumbnail. If local bytes are available, run:

```sh
python3 scripts/inspect_gif.py /absolute/path/to/result
```

The script reports the byte-level format, GIF frame count, frame delays, loop metadata, and structural completeness. A successful check requires a structurally complete GIF with multiple image frames. It does not judge smoothness or prove visually distinct frames; preview the animation as well. PNG/APNG output, single-frame GIFs, sprite sheets, and pose collages do not satisfy a request for an animated GIF.

Report the actual format, frame count, saved path, and whether generation was native or converted. If the output is static, say so plainly. Do not rename PNG files to GIF or infer model versions from source titles, C2PA specification versions, speed, or visual quality. Stop after the requested test; do not repeat paid or quota-consuming calls indefinitely.

## Improve a supported animation

For a visible seam, flicker, or identity drift, use this refinement with the user's existing scope:

> Improve the seamless loop by making the final movement flow naturally back into the starting pose. Avoid visible jumps, flickering, and character distortion.

For later chroma keying, optionally append:

> Use a solid pure green chroma-key background, keeping the background completely uniform throughout the animation for easy keying.

## Attribution and scope

These recipes are Sun Xiang's original collection, packaged at the author's request. See [source and authorship](references/source-and-authorship.md). The collection supplies creative directions; output support depends on the chosen tool and account. This package does not certify a particular GPT Image model version or bundle the source document's example media.
