# Proved reoptimized thick-sieve cookbook

```yaml
ID: TB-RECIPE-cookbook-thick-reoptimized-15-16
TYPE: RECIPE
STATUS: CURRENT
TITLE: Proved 4bx thick-packet reoptimization plus one-cell thin receiver yielding 15/16
SCOPE: BOTH
SOURCE_STAGE: Stage14-4bx
SOURCE_PR: 422
SOURCE_MERGE_SHA: 6774b9b6fb662cb14cc221c0b56bb74c077a3659
SOURCE_FILES:
  - stages/stage14/14-4bx/result.md
  - stages/stage14/14-s7-08/result.md
  - stages/stage14/14-4bw/result.md
```

## INPUT

The proved product-square packet inequality together with the proved shared-`xi` one-cell thin receiver.

## OUTPUT

The reusable thick-packet theorem

```text
N_packet << M*H^(-4/5) B^o(1)
```

and the historical exhaustive `15/16` whole-family checkpoint obtained before the two-cell theorem was closed.

## VARIABLE DICTIONARY

```text
THICK_PACKET_RELATIVE_SAVING=H^(-4/5)
lambda=15/32
nu=13/32
tau=5/64
historical whole-family exponent=15/16
```

## USED BY

- The current 13/14 two-cell architecture as its thick-side input.
- Future attempts to improve the four-square-part receiver.

## DO NOT USE FOR

- Do not call `15/16` current after merged s7-10/4by.
- Do not infer that the packet theorem itself was superseded; only its old global recombination was.

## PROVENANCE NOTES

Merged 4bx proves the `H^(-4/5)` packet estimate. Merged s7-10/4by later retain that estimate and improve only the thin receiver/global recombination to `13/14`.