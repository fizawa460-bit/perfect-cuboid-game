# Current reoptimized thick-sieve cookbook

```yaml
ID: TB-RECIPE-cookbook-thick-reoptimized-15-16
TYPE: RECIPE
STATUS: CURRENT
TITLE: Current 4bx thick-packet reoptimization plus one-cell thin receiver yielding 15/16
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

The current unconditional whole-family theorem

```text
V(B) << B^(15/16+o(1)).
```

obtained by the optimized auxiliary prime scale `L=H^(4/5)` and exhaustive reoptimization.

## VARIABLE DICTIONARY

```text
THICK_PACKET_RELATIVE_SAVING=H^(-4/5)
lambda=15/32
nu=13/32
tau=5/64
current exponent=15/16
sqrt gap=7/16
```

## USED BY

- Current main/s exponent comparisons.
- Any future attempt to improve the thick-packet or one-cell-thin architecture.
- Updating conditional two-cell targets after a proved thick-side improvement.

## DO NOT USE FOR

- Do not claim the s7-09 mixed Fourier theorem is proved; 4bx explicitly does not use it.
- Do not treat `13/14` as current; it remains conditional on the missing two-cell theorem.

## PROVENANCE NOTES

Merged 4bx uses only previously merged one-cell inputs and proves the unconditional `15/16` bound.