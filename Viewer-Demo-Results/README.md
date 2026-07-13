# Viewer Demo Results — SWMM5 Benchmark 3D Viewer

Complete `.inp` + `.rpt` + `.out` sets for the 17 models embedded in the
[SWMM5 Benchmark 3D Viewer](https://swmm5-3d-viewer.netlify.app/): the 11
EXTRAN Manual benchmarks (OWA regression suite), EPA SWMM5 Example 1, and the
five larger real-network samples (user1–user5).

## Why this folder exists

The viewer (build v2026.06.28+) auto-fetches same-basename `.rpt`/`.out`
siblings when you load a `.inp` through its GitHub browser. Point the browser at:

- **Owner:** `SWMMBobSWMM6`  ·  **Repo:** `1729-SWMM5-Models-2030`  ·  **Branch:** `master`
- **Path:** `Viewer-Demo-Results`

…click any `.inp`, and its engine results attach automatically — max-HGL
ribbon, results coloring, and the animated `.out` timeline, no local files needed.

Note: the 12 benchmark models (exam1, extran1–10) also ship with results
*bundled inside the app itself* (build v2026.07.01+). This folder additionally
serves the five user samples, whose `.out` files (1.9–4.2 MB each) are too
large to embed, and provides an end-to-end verification path for the GitHub
sibling-fetch feature.

## Provenance

All results generated with **EPA SWMM 5.2.4** (via pyswmm 2.x), each model run
in an isolated engine process, from exactly the `.inp` text embedded in the
viewer — so element names match by construction. Verified by decoding every
`.out` through the viewer's own binary parser: 17/17 models, 100% node and
link name matches, Node Depth Summary tables present in every `.rpt`.

## Known quirk: extran8b hotstart

As distributed, `extran8a.inp` **saves** `extran8.hsf` while `extran8b.inp`
tries to **use** `extran8b.hsf` — a filename mismatch, so 8b cannot run
as-shipped (SWMM ERROR 331). The bundled `extran8b.rpt`/`.out` were generated
by running 8a first and pointing 8b at the saved `extran8.hsf`. That file is
included here (227 bytes) for anyone who wants to reproduce the run.

*Generated 2026-07-12 · SWMM5 Benchmark 3D Viewer project*
