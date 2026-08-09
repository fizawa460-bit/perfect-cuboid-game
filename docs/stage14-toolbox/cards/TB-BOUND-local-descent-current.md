# Current closed s5 local-descent bound

```yaml
ID: TB-BOUND-local-descent-current
TYPE: BOUND
STATUS: CURRENT
TITLE: Closed s5 local-descent saving 1/21 and physical exponent 41/42
SCOPE: BOTH
SOURCE_STAGE: Stage14-s5u
SOURCE_PR: 338
SOURCE_MERGE_SHA: 516ffb08155e0aa618b2539efb07802a389ca219
SOURCE_FILES:
  - stages/stage14/14-s5u/result.md
EXPONENT_SCALE: M and physical B
SAVING_EXACT: 1/21 on M-scale; 1/42 on B-scale
EXPONENT_EXACT: 41/42 on physical B-scale
CONVERSION: M<=sqrt(B)
```

## INPUT

- The closed Stage14-s5 local 2-descent / reciprocity-sieve system.
- Regular Euclid boxes, including the projective all-short refinement.
- Physical conversion `M<=sqrt(B)`.

## OUTPUT

```text
N_local(M) << M^(2-1/21+epsilon)
#Q_B^phys << B^(41/42+epsilon)
```

Exact scale conversion:

```text
(2-1/21)/2 = 41/42.
```

Thus the current proved whole-family physical saving inherited from the closed s5 local majorant is `1/42` relative to exponent `1`.

## VARIABLE DICTIONARY

- `M` = Euclid scale.
- `B` = physical cutoff.
- `N_local` = locally-soluble class count.

## USED BY

- Stage14 main/s post-local work.
- Current square-root-gap ledger.
- Any future comparison that asks for the strongest closed local input.

## DO NOT USE FOR

- Do not claim `B^(41/42)` is the expected final order or an asymptotic.
- Do not infer global solubility from local solubility.
- Do not replace it by the nearby `1/20` single-edge ceiling: that ceiling is not a proved whole-system `M` saving.
- Do not multiply later coordinate-density savings into this packet/base count unless a transfer theorem proves that quantifier step.

## PROVENANCE NOTES

This card supersedes the s5s `1/200` and s5t `1/41` cards on the same normalized local-count use case. Stage14-s5u explicitly closes the s5 method after this improvement.
