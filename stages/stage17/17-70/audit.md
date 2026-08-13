# Stage17-70 — fresh audit record

Status: **FAIL**

Audited submission: PR #912, head `b344e7012942b54e49c97469cfc0fd0eaef79db6`.

## Accepted mathematics

The checkpoint-70 mathematics is accepted as far as the Stage17 theorem and bounded deductions are concerned.

- The Stage13 target population matches Stage17 after the exact identity adapter `d=R`, so `N_1(B) ~ (kappa/(24*pi)) B(log B)^3` transfers without population or cutoff loss.
- The frozen Stage16 source law `M_1(B) asymp B^2 log B` gives `N_1(B)/M_1(B) asymp (log B)^2/B -> 0`; no leading ratio constant is claimed.
- If `H_{1,d}(B)` counts primitive canonical integral-space-diagonal cuboids with at least one integral face, then every object in `H_{1,d}(B)-N_1(B)` lies in at least one Stage13 pair overlap. Since the three pair overlaps are `o(B(log B)^3)`, the deduction `H_{1,d}(B) ~ N_1(B)` and `N_1(B)/H_{1,d}(B) -> 1` is valid.
- The structural Stage16-to-Stage17 predicate `p^2+z^2=d^2` after `x^2+y^2=p^2` is exact, and the bundle correctly defers intrinsic/independent/correlated/interaction-dependent classification of the space-diagonal cost to Stage21 with Stage16S.
- The required StageX-70 bounded-synthesis fields are present and the stop rule is satisfied.
- No perfect-cuboid existence or nonexistence conclusion is introduced.

## Failure: frozen Stage16 interface is not explicit enough for V1

`SELF_CONTAINED_REVIEW_STANDARD_V1` requires each frozen earlier-stage interface used load-bearingly by the final bundle to make the following items explicit:

```text
UPSTREAM_STAGE=
UPSTREAM_THEOREM=
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
```

`stages/stage17/final.md` gives an explicit Stage13 interface block and states the Stage16 theorem and source population in prose, but the Stage16 import does not explicitly certify the multiplicity, measure-adapter, and quantifier-adapter fields required by V1. Because the Stage16 denominator theorem is load-bearing for the Stage16-to-Stage17 survival law, the final bundle cannot yet be frozen as a V1 self-contained interface.

This is a bundle-contract repair, not a mathematical failure. No new theorem, computation, literature input, or human decision is needed.

Recommended minimum repair in `stages/stage17/final.md`:

```text
UPSTREAM_STAGE=Stage16
UPSTREAM_THEOREM=M_1(B) asymp B^2 log B for primitive canonical exactly-one-face cuboids under R<=B
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
ROLE=matched Stage16 source/denominator law
```

The repaired bundle should also expose the V1 closeout gates in its machine-readable lock, in particular `UPSTREAM_INTERFACES_EXACT=true`, while leaving `FRESH_HOSTILE_REVIEW=FAIL` or pending until the next Stage17-audit.

A secondary metadata inconsistency should be normalized in the same repair: the Stage17 controller labels checkpoint 10 merely `PROVED`, while the manifest/result correctly record the existing checkpoint-10 audit PASS.

## Verdict

```text
AUDIT_VERDICT=FAIL
AUDIT_PERSISTENCE_STATUS=PENDING_CONTROLLER_SYNC
ADVANCE_ALLOWED=false
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
NEXT_CHECKPOINT=70
NEXT_STAGE=
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
MERGE_ALLOWED=false
```
