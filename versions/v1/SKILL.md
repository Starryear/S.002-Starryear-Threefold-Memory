---
name: starryear-threefold-memory
description: Transform travel, landscape, architecture, botanical, animal, or quiet documentary photographs into Starryear-Threefold-Memory artworks with an expressive source-derived perception above, the original photograph in the middle, and a distinct cartographic afterimage below. Use for 三重记忆、旅行记忆三联画、照片上下抽象, What I Saw / What Happened / What Stayed, or three horizontal 16:9 panels stacked vertically.
---

# Starryear-Threefold-Memory

Create one vertical artwork from one locked source photograph. Separate the moment into:

1. `TOP — WHAT I SAW`: first-sight perception—subject identity, color, light, rhythm, and atmosphere.
2. `MIDDLE — WHAT HAPPENED`: the user's actual photograph.
3. `BOTTOM — WHAT STAYED`: spatial memory—routes, distances, intervals, traces, and afterimage.

This is neither a filter nor three versions of one picture. Read [references/threefold-method.md](references/threefold-method.md) before generation.

## Lock the evidence

Record the exact local path of the user's photograph. Use that same file for analysis, both generated panels, middle-panel composition, and verification. Never substitute a prior output, screenshot, reference, derivative, or neighboring file.

For a series, use an explicit manifest mapping `source -> top -> bottom -> final`; never guess pairings from filenames.

## Analyze and direct

Extract three to six decisive facts: minimum recognition cues, dominant masses, negative space, axes, flow, palette roles, light, repetition, grouping, overlap, depth, and emotional temperature. Every major generated mark must be explainable from one named source fact.

Generate the top and bottom separately using the complete scaffolds in [references/generation-prompt.md](references/generation-prompt.md). Do not ask an image model to generate the complete triptych.

Use [assets/examples](assets/examples) as visual demonstrations of the authored family. They show the intended difference between full-field expressive perception, the untouched original moment, and relational memory-atlas language. Treat them as style and structure evidence only: never reuse their subjects, compositions, or palettes unless the user supplies that exact photograph.

### Top: expressive perception

Use the `photo-abstract-editorial` principle of minimum necessary recognizability, but adapt it to the user's demonstrated full-field painterly language. Preserve two to four identity anchors for distinctive subjects. Permit source-derived paper, print, brushed, translucent, or collage-like material character inside the artwork; do not force a uniform ivory field. Activate the whole 16:9 field through large masses, directional structure, rhythm, and distributed supporting evidence.

The top may be more representational than the bottom, but must remain an authored abstraction rather than a realistic redraw, filter, miniature illustration, or isolated symbol.

### Bottom: relational memory atlas

Use the `travel-photo-abstraction` method: deconstruct, distill, and reconstruct relational identity. Translate direction, distance, count, repetition, gaps, occlusion, depth, and time into routes, nodes, tracks, intervals, grids, drifting fragments, compressed clusters, and color residues.

The bottom may retain simplified subject anchors when the examples justify them, but its organizing logic must be cartographic or relational, not scenic. It must not repeat the top layout.

Use a source-derived palette in both panels. One high-value accent may carry an observed focal fact, such as a red coat, golden leaf, eye, reflected light, or architectural trim. Never invent a fashionable accent.

## Composition contract

- Three equal horizontal `16:9` panels; default `1920 x 1080 px` each.
- Exact order: `PERCEPTION -> ORIGINAL -> MEMORY`.
- Default final output: RGB `1920 x 3240 px`.
- Join directly with no frames, gaps, dividers, labels, captions, logos, or watermarks.
- Fit the middle photograph proportionally with `cover` by default. Allow restrained cropping, protect the focal subject, never stretch or recolor, and never add bars.
- Use `contain` only when the user explicitly requires zero cropping and accepts visible padding.
- Assemble with `scripts/compose_triptych.py` and require `DELIVERY PASS`.

## Series workflow

Inspect all sources, then produce one representative complete sample. Obtain approval for recognition level, material density, difference between top and bottom, and crop before processing the rest. Do not batch-generate the entire set first.

For each source, choose its own visual grammar:

- architecture: axes, tier rhythm, openings, masonry grids, and shadow geometry;
- water/light: currents, sparkle fields, rail trajectories, and isolated human color;
- botanical subjects: stems, repeated growth, petal radiation, leaf intervals, and seasonal palette;
- animals/people: observed count, gaze or stance, occluding grid, scale, and spacing—never invent hidden anatomy;
- street moments: built grid, movement blur, doorway/frame, light path, and human pause.

Maintain one Starryear family through evidence fidelity, tactile material, source palette, and the perception/photo/memory sequence—not by reusing one template.

## Validation

Reject if the middle panel is altered, stretched, barred, or mismatched; the top is either photographic or generic; the bottom is a redraw or a duplicate of the top; a source-specific cue is lost; unsupported people, animals, buildings, symbols, colors, or text appear; or seams and dimensions fail.

Create a contact sheet for a completed series and visually check every source-to-output pairing. Return only completed triptychs.

Authored by Starryear.
