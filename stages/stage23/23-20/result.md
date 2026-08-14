# Stage23-20 — finite baseline plus concrete Stage17-slice attack

Status: **REPAIRED_SUBMISSION_PENDING_FRESH_AUDIT**

Checkpoint20 finite census is unchanged and not reopened. The repair scope is only the missing concrete candidate-family generation and test ledger.

The inherited matched finite checkpoint remains

\[
N_1(2000)=1434,\qquad N_2(2000)=5,
\]
so
\[
N_2(2000)/N_1(2000)=5/1434.
\]
This is diagnostic only.

## New attack direction

Instead of repeating the Stage14/15 two-face-first route, start from Stage17's already solved Pythagorean chain

\[
x^2+y^2=p^2,\qquad p^2+z^2=d^2,
\]

and ask whether a second face square can be cut into that space-diagonal-integral family.

Use the audited AR-039 Stage17 family

\[
x=m^2-n^2,\ y=2mn,\ p=m^2+n^2,\ z=(p^2-1)/2,\ d=(p^2+1)/2.
\]

A concrete one-parameter subfamily is obtained by fixing `n=1` and taking `m=t=2 mod 14`.

All source-side requirements are already live:

```text
POSITIVITY=PASS
STRICT_ORDERING=PASS_AFTER_AR039_CANONICAL_SORT
SPACE_DIAGONAL=PASS_IDENTICALLY
PRIMITIVITY=PASS_BY_AR039_CONTRACT
SOURCE_EXACTLY_ONE=PASS_BY_AR039_CONTRACT
INFINITE_SOURCE_FAMILY=PASS
HEIGHT_GROWTH=PASS, d~t^4/2
```

The two possible new face conditions reduce to

\[
(2q)^2=(t^4+2t^2-4t+2)(t^4+2t^2+4t+2)
\]

and

\[
Q^2=(t^2+4)(t^2-2t+2)(t^2+2t+2).
\]

These are degree-8 and degree-6 hyperelliptic square-value models, generically genus 3 and genus 2 respectively after smooth projective completion.

An exact integer scan over the certified congruence slice

```text
n=1
m=t=2 mod 14
2 <= t < 200000
```

found

```text
XZ_FACE_HITS=0
YZ_FACE_HITS=0
```

so no Stage19 member was produced on this tested one-parameter slice. This is finite evidence only and is not used as a nonexistence theorem.

The complete derivation and test ledger are recorded in `stages/stage23/23-20/new-view-attack.md`.

## Checkpoint repair verdict

The prior audit failure was that no concrete nontrivial candidate family had actually been generated and pushed through the Stage19 gates. That defect is repaired: AR-039 with `n=1`, `m=t=2 mod 14` is an explicit infinite primitive Stage17 candidate family, and positivity, ordering, space diagonal, primitivity, source mask, infinity, height growth, and both possible second-face equations are tested in order.

It does **not** produce an infinite Stage19 family, positive-power lower bound, or matching half-power family. The new information is that this natural Stage17 slice leads to higher-genus square-value problems rather than an obvious rational parametrization.

```text
EVIDENCE_LEVEL=COMPUTED+PROVED_ALGEBRAIC_REDUCTION
CHECKPOINT=20
FINITE_CENSUS_REOPEN_REQUIRED=false
UPSTREAM_THEOREM_REOPEN_REQUIRED=false
REPAIR_SCOPE=CONCRETE_CANDIDATE_FAMILY_GENERATION_AND_TEST_LEDGER_ONLY
AGGRESSIVE_SEARCH_POLICY=REQUIRED
CANDIDATE_FAMILY_GENERATION_REQUIRED=true
CANDIDATE_FAMILY_GENERATION_STATUS=PASS_MATERIALIZED
CANDIDATE_FAMILY=AR039_N1_SLICE
CANDIDATE_FAMILY_PATH=stages/stage23/23-20/new-view-attack.md
OLD_STAGE14_15_PRIMARY_ROUTE_REUSED=false
NEW_VIEW=STAGE17_FAMILY_SLICING
INFINITE_STAGE19_FAMILY_FOUND=false
POSITIVE_POWER_LOWER_BOUND_FOUND=false
MATCHING_HALF_POWER_FAMILY_FOUND=false
TRUE_EXPONENT_IDENTIFIED=false
FINITE_DATA_USED_AS_PROOF=false
AUDIT_REQUIRED=true
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT_AFTER_PASS=30
MERGE_ALLOWED=false
CODEX_REQUIRED=false
```
