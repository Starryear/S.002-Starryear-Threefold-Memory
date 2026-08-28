---
name: starryear-threefold-memory
description: "Transform one user-supplied photograph into a vertical three-panel memory artwork: a large fragmented visual-memory collage above, unchanged photographic evidence in the middle, and a source-specific spatial signal map below. Use for Threefold Memory, What I Saw / What Happened / What Stayed, 三段式记忆, or photo-to-memory triptychs. The method adapts every route, node, fragment, pictogram, palette, and rhythm to the supplied photograph; it must not hard-code a place, object, route, or decorative constellation."
metadata:
  version: "2.2.1"
---

# Starryear Threefold Memory

Turn one locked photograph into three equal horizontal panels stacked vertically:

1. `TOP — WHAT I SAW`: fragmented visual memory. The photograph is recomposed as large, irregular geometric fragments, overlapping paper planes, sharp cut shapes, translucent layers, displaced silhouettes, worn pigment, and selective metallic or printed texture. The main subject remains large and compositionally dominant, but unstable.
2. `MIDDLE — WHAT HAPPENED`: photographic evidence. The original photograph remains unchanged except for deterministic proportional fitting.
3. `BOTTOM — WHAT STAYED`: spatial signal map. The photograph's paths, directions, color regions, object relationships, and intervals become a loose hybrid of metro diagram, constellation chart, and restrained circuit traces with generous empty space.

The final order is `PERCEPTION -> PHOTOGRAPH -> AFTERIMAGE`. Generate the top and bottom separately and assemble them deterministically around the locked photo.

## Core correction

This version rejects two failure modes:

- `TOP TOO LITERAL`: a filter, enlarged photograph, generic abstract painting, or tiny symbolic subject. The main subject must remain large and recognizable through its defining proportions, direction, rhythm, or silhouette, while being fractured and recombined.
- `BOTTOM TOO GENERIC`: a stock city map, regular constellation, motherboard, or technical schematic. Every route, node, icon, gap, and density change must be caused by a visible spatial relationship in the photograph.
- `TEMPLATE LEAK`: never name or preselect a pagoda, tree, flower, animal, landmark, city, fixed route, fixed node shape, fixed constellation, or fixed palette. The photograph is the only content source; bundled examples are method references only.

The intended transformation is:

```text
TOP:    SOURCE SIGNALS -> LARGE PAPER/GEOMETRIC FRAGMENTS + DISPLACED SILHOUETTES -> UNSTABLE VISUAL MEMORY
MIDDLE: SOURCE PHOTOGRAPH -> PROPORTIONAL FIT ONLY
BOTTOM: SOURCE SPATIAL RELATIONSHIPS -> ROUTES / NODES / COLOR FIELDS -> SPATIAL SIGNAL MAP
```

Read the complete [Version 2 master prompt](versions/v2/MASTER-PROMPT.md) and [visual grammar](versions/v2/references/painterly-cubist-afterimage-grammar.md) before generating. The master prompt is the production contract; the grammar reference resolves conflicts with legacy examples.

## Non-negotiable output contract

- Use exactly one user-supplied photograph as the sole content source for one artwork.
- Default final size: `1920 x 3240 px`, composed of three equal `1920 x 1080` panels.
- Join panels edge-to-edge with no gap, frame, divider, label, title, caption, logo, signature, watermark, or mockup.
- Preserve the middle photograph as evidence. Do not redraw, relight, recolor, denoise, retouch, remove, or add content.
- Generate the top and bottom as separate horizontal images. Never generate the full triptych in one image-model call.
- Assemble with [versions/v2/scripts/compose_triptych.py](versions/v2/scripts/compose_triptych.py) or equivalent deterministic compositing.
- Every major top or bottom element must point to a visible source fact or a documented transformation of a source relationship.

## Visual relationship between panels

The three layers must feel related but not interchangeable:

- The top shares the source's subject, palette, light, mass, and emotional pressure.
- The middle preserves the event.
- The bottom shares the source's positions, counts, intervals, directions, gaps, groupings, and material echoes.

The top should be recognizable only through fragments, never as a realistic animal, person, or scene. The bottom must retain a felt and auditable connection to the source even after the literal scene dissolves.

## Stage 1 — Lock and inspect the photograph

Before interpretation:

1. Enumerate and visually inspect every supplied image candidate.
2. Lock one exact source path or asset identifier.
3. Record pixel size, orientation, color mode, optional checksum, intended crop, and focus point.
4. Inventory literal evidence separately from emotion:
   - subject and finite count;
   - position, scale, gesture, gaze, silhouette, and spacing;
   - foreground, middle ground, background, and occlusion;
   - structural carrier: grid, horizon, vertical rhythm, curve, diagonal, frame, or branching growth;
   - largest masses and largest pauses;
   - palette roles and brightest opening;
   - distinctive source-specific details.
5. Do not invent symbols, species, architecture, weather, narrative, or cultural meaning.

For file-based work, keep a small audit trail:

```text
work/<job-id>/
|-- PIPELINE_STATE.md
|-- SOURCE_MANIFEST.json
|-- EVIDENCE_ANALYSIS.md
|-- LAYER_BRIEF.md
|-- photo-panel.png
|-- top-panel.png
|-- bottom-panel.png
|-- QA_REPORT.md
`-- retry/
```

## Stage 2 — Write three distinct propositions

Write one sentence for each layer:

```text
WHAT I SAW: the subject/light/material tension that struck first.
WHAT HAPPENED: a strictly literal description of the photographed event.
WHAT STAYED: the count, interval, path, gaze, gap, repetition, or pressure that remained.
```

If the top and bottom propositions could be swapped, rewrite them.

## Stage 3 — Plan the top: fragmented visual memory

The top has two cooperating systems. Neither may disappear.

### A. Fragmented field

The field carries source-derived sensation and material memory:

- use large irregular geometric fragments, overlapping paper planes, sharp cut shapes, translucent layers, displaced silhouettes, worn pigment, printed-paper texture, and occasional metallic or dry-brush passages;
- derive fragment direction, scale, overlap, light opening, and material from the photograph's own paths and spatial hierarchy;
- preserve the source's brightest opening and largest pauses as quiet paper/sky regions;
- let fragments collide, interrupt, stretch, and dissolve around the subject while keeping a controlled composition;
- use clean-cut, worn/broken-print, and translucent/soft edge behaviors. Do not turn the image into a blur, generic watercolor wash, grunge texture, or stock collage.

The smear must feel hand-made and directional. Reject generic blur, fog overlays, uniform watercolor wash, grunge, or dirty vintage texture.

### B. Large subject reconstruction

The subject is not a complete illustration. Deconstruct it into angular planes and selectively shifted viewpoints:

- preserve the main subject's approximate scale, position, defining proportions, direction, finite count, and structural rhythm; it must remain large and compositionally dominant;
- break it into large and medium irregular planes, partial silhouettes, repeated structural bands, and displaced fragments with changes in angle, value, scale, or viewpoint;
- create shallow dimensionality through overlap, occlusion, translucent layers, paper-plane stacking, and cast-shape relationships—not photorealistic volume, CGI, or low-poly modeling;
- let source-derived secondary elements expand, collide, and dissolve around the subject; interrupt at least two major subject regions with surrounding fragments;
- keep the subject recognizable through 30–60% structural continuity, but remove literal surface detail and complete scene description;
- use a few factual lines or cut seams to hold the reconstruction together. Every major fragment must be explainable as a transformed source fact.

Cubism is a structural operation, not permission to add unrelated geometry, extra faces, duplicate animals, or arbitrary colors.

### Top balance rule

At thumbnail size the top should read first as a bold source-derived geometric collage with layered paper depth, second as a large fractured version of the photographed subject. If it reads as a filter, tiny icon, generic collage, vector mosaic, or complete literal illustration, it fails.

Recommended visual weight:

- `35–55%` source-derived geometric/color field and negative space;
- `30–50%` large subject fragments and displaced silhouette;
- `5–15%` thin structural drawing, scraped seams, or factual accent.

These ranges guide judgment; do not enforce them mechanically.

## Stage 4 — Plan the bottom: spatial signal map

The bottom begins by extracting the photograph's dominant subject, spatial paths, directional movement, color regions, object relationships, and empty space—not by selecting a reusable map template.

### Relationship anchor

Choose one dominant source relationship:

- two subjects and the interval between them;
- one gaze or movement across a frame;
- repeated verticals, roofs, stems, windows, or waves;
- a horizon and distance field;
- a path through foreground occlusion;
- a cluster and surrounding silence.

Never choose a fixed route, node system, constellation, pictogram set, or layout before inspecting the photograph. The structure must be regenerated from each image.

State it in one sentence. This relationship must remain perceptible in the finished bottom panel.

### Source echo requirement

Retain `2–5` recognizable but nonliteral source echoes. Examples:

- paired subjects -> paired partial silhouettes, masks, warm masses, or landmark nodes in their observed positions;
- animal gaze -> eye-colored nodes with directional arcs, plus ear or shoulder fragments;
- architecture -> broken roof/tier rhythm or facade fragments aligned to the source axis;
- flowers -> simplified cup/petal remnants attached to growth routes;
- water -> a broad current band carrying light residues;
- lattice or railing -> partial frame segments and measured intervals, not a complete schematic grid.

The echoes must preserve observed count and relative position, but should be reduced into a recognizable sequence of geometric symbols or pictograms rather than miniature realistic drawings. Their number and form must adapt to the photograph.

### Loose metro / constellation / circuit language

Organize the source echoes with:

- one primary metro-like route derived from the source carrier;
- one or two secondary routes that bend around or connect source echoes;
- varied star points, small nodes, short dotted chains, thin rings, pauses, transfers, and density gradients;
- occasional chip-like trace behavior—right-angle turns, stepped segments, terminal pads, paired traces, small stations, and branching buses—used as a secondary accent rather than the substrate;
- station-like circles or transfer points only at meaningful source positions;
- broad translucent fields or currents derived from source masses, light, shadow, or material;
- continuous movement through the frame rather than a uniform grid.

Lines may bend, stop, drift, cross, disconnect, and restart. Vary density, spacing, scale, and rhythm. Preserve generous empty space and avoid perfect symmetry. Use orbital dots, signal points, short chains, and simplified pictograms only where source relationships justify them.

The route system should combine a poetic metro map with a restrained chip-trace vocabulary. Alternate curved and rectilinear segments; use meaningful stops, transfers, intervals, and open channels. It must remain spatial and source-specific, not a stock PCB template.

### Electronics boundary

Electronic or chip-like details are a deliberate secondary organizing language, but must remain subordinate to source relationships:

- no full-field PCB grid;
- no motherboard composition;
- no processor blocks, pin arrays, solder-pad vocabulary, engineering labels, or technical symmetry;
- allow approximately `5–20%` chip-like traces, nodes, terminals, and stepped buses when they clarify the source's intervals, barriers, or paths;
- if removing all literal electronic motifs would destroy the picture, the design is too dependent on circuitry and must be rebuilt from the source relationship.

### Bottom balance rule

At thumbnail size the bottom should read first as a spacious source-specific spatial signal map, second as a flowing metro/constellation field, and only third—as a restrained circuit accent.

Recommended visual weight:

- `45–65%` recognizable source relationships, echoes, and source-derived fields;
- `25–45%` flowing routes, star points, nodes, rings, and dotted chains;
- `5–20%` chip-like/rectilinear trace detail, blended with routes rather than laid out as a full PCB.

## Stage 5 — Build an evidence ledger

Before generation, map at least four source facts through all layers:

```text
SOURCE FACT | TOP: SMEAR/CUBIST FORM | MIDDLE: PHOTO EVIDENCE | BOTTOM: ECHO/FLOW
```

For the bottom, also write `4–7` causal mappings:

```text
[visible source fact] -> [retained echo] -> [route/node/field behavior] -> [position]
```

Reject any important bottom mark that cannot complete: `This exists because the photograph contains ____.`

## Stage 6 — Prepare the middle panel

- Apply EXIF orientation correction only.
- Scale proportionally.
- Default to a restrained `cover` crop around the recorded focus point.
- Protect faces, heads, hands, animal ears, architectural crowns, and other identity anchors.
- Do not sharpen, blur, recolor, grade, relight, add grain, denoise, or retouch.
- Save and reuse this exact photo panel during assembly.

## Stage 7 — Generate the top and bottom separately

Use the locked photograph as the sole content reference. Bundled examples are method references only and must never contribute their subjects, palette, layout, or symbols.

### Top prompt scaffold

```text
Generate only the TOP panel of a Starryear Threefold Memory artwork.

OUTPUT: one borderless, text-free horizontal 16:9 image. No triptych, photograph, or mockup.
IMAGE 1: locked source photograph and sole content source. Do not embed it or apply a simple filter.

WHAT I SAW: [source-specific proposition]
SOURCE SIGNALS: [main subject, approximate scale/position, defining proportions, direction, count, spatial hierarchy, dominant paths, color regions, light opening, material, and 2–4 identity anchors]

FRAGMENTED VISUAL MEMORY:
Reconstruct the same photograph from its extracted signals using large irregular geometric fragments, overlapping paper planes, sharp cut shapes, translucent layers, worn pigment, printed-paper texture, displaced silhouettes, and occasional metallic texture. Keep the main subject large, recognizable, compositionally dominant, and in its approximate position. Preserve its defining proportions and structural rhythm while allowing unstable shifts in angle, value, scale, and viewpoint.

COMPOSITION:
Let secondary elements expand, collide, and dissolve around the subject. Use generous negative space derived from the photograph's brightest opening. Combine clean cuts, worn/broken print edges, and soft translucent overlaps. Keep 30–60% of the subject structure recognizable; remove literal surface detail and complete scene description. Every major fragment must be traceable to a visible source fact.

PALETTE/LIGHT: derive all colors from the source photograph; preserve its visual and material DNA.
AVOID: fixed subject assumptions, fixed location, generic abstract art, tiny subject icon, enlarged photograph, simple blur/filter, neat vector mosaic, stock collage, unrelated geometry, arbitrary symbols, text, watermark, border, sepia, grunge.
```

### Bottom prompt scaffold

```text
Generate only the BOTTOM panel of the same Starryear Threefold Memory artwork.

OUTPUT: one borderless, text-free horizontal 16:9 spatial signal map. No triptych, photograph, mockup, or stock PCB template.
IMAGE 1: same locked source photograph and sole content source. Do not recreate or filter it.

WHAT STAYED: [source-specific relationship or residual rhythm]
EXTRACTED SIGNALS: [subject, paths, directional movement, color regions, object relationships, count, approximate positions, gaps, and quiet areas]
SOURCE ECHOES TO RETAIN: [2–5 adaptive geometric echoes or pictograms; no fixed symbols]
CAUSAL MAPPINGS: [4–7 source fact -> echo -> route/node/field behavior -> position mappings]

COMPOSITION:
Translate the photograph into a loose hybrid of metro diagram, constellation chart, and restrained circuit map. Keep source relationships, echoes, color fields, and generous empty space as the main content. Use one primary route and one or two secondary paths only when the photograph supports them. Lines may bend, stop, drift, cross, disconnect, and restart; vary density, spacing, scale, and rhythm. Add scattered nodes, orbital dots, signal points, short chains, and simplified pictograms at meaningful source positions.

TRANSIT / CIRCUIT BALANCE:
Use only 5–20% chip-like accents—occasional stepped traces, right-angle turns, terminals, paired lines, station pads, or transfers. No full-field PCB, motherboard, processor blocks, pin-array repetition, engineering labels, neon cyberpunk, or perfect symmetry. This layer translates space into signals; it must not duplicate the top's fragmented collage.

SOURCE LINK TEST:
At thumbnail size the source's main subject, approximate position, dominant carrier, grouping, largest gap, density distribution, and at least two identity echoes must remain perceptible. If the map could fit an unrelated photograph, rebuild it.

PALETTE/LIGHT: derive color fields and line colors from the source photograph; preserve its visual DNA without importing a fixed palette.
AVOID: fixed routes, repeated decorative constellations, generic city maps, unrelated symbols, outer-space spectacle, miniature realistic scene, duplicate of top, text, watermark, border, sepia, grunge.
```

## Stage 8 — Inspect and retry

Inspect each generated panel before assembly. Use no more than three attempts per panel. Diagnose one or two failed gates per retry.

### Top hard gates

- large source-derived geometric fragments and layered paper depth are visibly dominant;
- the main subject remains large, compositionally dominant, and recognizable through proportions, direction, count, or structural rhythm;
- at least two identity anchors survive while the subject is visibly fractured and recombined;
- subject and context overlap rather than sit in separate layers;
- source palette, light, and material remain credible;
- no fixed-template subject, enlarged photograph, generic filter, stock collage, invented subject, text, or border.

### Bottom hard gates

- source relationship remains perceptible at thumbnail size;
- `2–5` adaptive geometric echoes or pictograms remain near their observed positions;
- one primary flow and optional secondary routes organize the field without a fixed layout;
- signal points, nodes, short chains, pauses, density variation, and generous empty space are present;
- route feeling comes from source-specific continuity, intervals, crossings, breaks, and restarts—not a copied subway diagram;
- chip language is sparse, source-bound, and subordinate to spatial signals;
- no generic city map, PCB, motherboard, corporate network, unrelated constellation, scene redraw, text, or border.

### Cross-layer gates

- at least four source facts survive across all three layers;
- top and bottom share palette and emotional temperature but use different organizing logic;
- top reads as fragmented visual memory, middle as photographic evidence, bottom as a spatial signal map;
- no reference subject or symbol leaks into the output.

If the third attempt still fails a hard gate, stop and report the unresolved failure instead of delivering a compromised result.

## Stage 9 — Assemble and validate

Use the compositor:

```bash
python3 versions/v2/scripts/compose_triptych.py \
  --top top-panel.png \
  --photo photo-panel.png \
  --bottom bottom-panel.png \
  --output outputs/threefold-001-subject.JPG
```

Then reopen the final file and verify:

- exact `1920 x 3240` RGB output unless the user requested another size;
- equal panel heights and correct order;
- unchanged middle photo;
- no seams, gaps, dividers, labels, signatures, or watermarks;
- top passes the smear/deconstruction thumbnail test and does not read as a realistic animal/scene;
- bottom passes the source-link test and reads as a source-specific metro/chip afterimage rather than a generic PCB.

## Bundled legacy examples

The images in `versions/v2/assets/examples/` are partial method references only:

- inspect them only for three-panel rhythm, source palette continuity, and deterministic photographic placement;
- use them only to understand three-panel rhythm, source continuity, paper texture, and the contrast between memory collage and signal map;
- never borrow their subjects, landmarks, palette, route geometry, node shapes, pictograms, layout, or symbols;
- every new photograph must generate a new subject decomposition and a new map structure from its own evidence.

## Delivery

Return only verified final artwork from the user-facing output folder. Briefly identify the locked source, any deliberate crop, and the generated-panel approach. Preserve Starryear attribution when packaging or presenting the method.
