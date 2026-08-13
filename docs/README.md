# Documentation index

The `docs/` root contains only current entry points and reusable interfaces.
Completed stage-specific research and operational history lives with its stage.

## Current project entry points

- `00_CURRENT_RESEARCH_STATUS.md` — current research status and active Stage15 review handoff
- `face-ratio-geometry-research.md` — geometric research overview
- `cycle-exploration-safety-protocol.md` — current cycle safety protocol
- `self-contained-review-standard.md` — project-wide definition and template for final self-contained mathematical review artifacts

## Review construction standard

`self-contained-review-standard.md` is authoritative for every future artifact labeled
`SELF_CONTAINED_WITH_STATED_EXTERNAL_THEOREMS`.

The top-level `review/` directory remains reserved for active rendered review artifacts.
Do not put policy/template documents there. A stage controller, manifest, build script, or
audit contract that creates a self-contained review should reference the standard explicitly.

## Stage14 reusable interfaces

- `stage14-arsenal.md` — authoritative weapon registry
- `stage14-arsenal-index.md` — obstruction/search index
- `stage14-arsenal-stage15-map.md` — Stage15 reuse map
- `stage14-toolbox/` — reusable cards, formulas, warnings, and receiver matrices

## Closed Stage15-6 operational provenance

- `stages/stage15/15-6-final.md` — canonical Stage15-6 closeout and Stage15-7 handoff
- `stage15-6-chat-operations.md` — closed ChatGPT-first operating contract
- `stage15-6-cycle-roadmap.md` — closed Stage15-6 cycle roadmap
- `stages/stage15/15-6-controller.json` — closed Stage15-6 controller state

These files remain available for provenance and audit. They are not invitations
to open another Stage15-6 internal route after the audited closure.

## Historical material

- `stages/stage14/archive/docs/q-research/` — completed Q literature and route research
- `stages/stage14/archive/docs/operations/` — retired Stage14 batch contracts and roadmaps
- `stages/stage14/archive/review/` — historical rendered reviews and manifests

Stage12, Stage13, and Stage14 each expose their final document and manifest from
their own stage directory. Historical files should not be moved back into the
root merely to preserve an old citation; update the citation to the archive path.
