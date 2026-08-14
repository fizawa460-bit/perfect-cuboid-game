# Stage24-50 — fresh Stage19 lower surgeon

CHECKPOINT=50
ROLE=FRESH_STAGE19_LOWER_SURGEON_FIRST
STATUS=BREAKTHROUGH_SUBMITTED_FOR_FRESH_AUDIT

## 1. Frozen target

The entering certified lower information was only the finite floor

\[
N_2(B)\ge3495\qquad(B\ge500,000,000).
\]

Checkpoint50 explicitly searches for:

1. `N2(B)->infinity`;
2. an infinite primitive Stage19 construction;
3. any asymptotic lower law, especially a positive power;
4. a direct space lift of the Stage18 explicit family.

Finite census growth is not used as proof.

## 2. Fresh candidate generation

### F50-S1 — mixed-parity lift of the Stage15-2 shared-edge family

Start from

\[
e=4pq,\quad x=4p^2-q^2,\quad y=4q^2-p^2,
\]

but remove the historical `p,q odd` restriction. The exact space condition becomes

\[
\boxed{p^4+q^4=17Z^2.}
\]

This is the genus-one quartic `C_17`. It maps nontrivially to

\[
E:Y^2=X^3-1156X,
\]

and the rational point `(t,z)=(2,1)` maps to `(-16,120)`, which has infinite order by the two-good-prime reduction certificate in `u19-r501a-quartic-family.md` and `quartic_family_audit.py`.

A physical rational point in the canonical cone is

\[
(p,q,Z)=(38,43,569),
\]
which yields

\[
(a,b,c,D)=(3927,5952,6536,9673).
\]

The third-face-square sublocus is a connected degree-four `V_4` cover of `P1` with genus five, hence has finitely many rational points by Faltings. Therefore infinitely many positive-rank quartic points in the physical cone survive the exactly-two mask.

Standard elliptic height plus real-circle equidistribution gives

\[
\boxed{N_2(B)\gg\sqrt{\log B}.}
\]

Verdict: `BREAKTHROUGH_PROVED_UNBOUNDEDNESS_AND_LOGARITHMIC_LOWER`.

### F50-S2 — general symmetric multiplier family

For an integer `k>=2`, the algebraic shared-edge family

\[
e=2kpq,\quad x=k^2p^2-q^2,\quad y=k^2q^2-p^2
\]

satisfies

\[
e^2+x^2+y^2=(k^4+1)(p^4+q^4).
\]

A natural space-lift receiver is therefore

\[
p^4+q^4=(k^4+1)Z^2.
\]

The point `(p,q,Z)=(1,k,1)` gives a rational base point on every such quartic. The `k=2` member is exactly F50-S1 and is proved positive-rank. No rank theorem uniform in `k` is claimed.

Verdict: `FAMILY_CLASS_IDENTIFIED_K2_CLOSED_OTHERS_OPEN`.

### F50-S3 — direct Stage19 squareclass-core slices

Stage19 has the exact condition

\[
A=kP^2,\qquad B=kQ^2
\]
for a common squarefree core `k`. The fresh lower surgeon tested the stronger construction idea of prescribing a fixed core and forcing both Gaussian norms into that core before physical reconstruction. This retains the correct target condition but produces moving genus-one/Pell-type slices already recognizable from Stage15-6; no new globally injective primitive family was closed here.

Verdict: `STRUCTURALLY_COMPATIBLE_NO_NEW_LOWER_THEOREM`.

### F50-S4 — shared-edge divisor pair plus space norm

The Stage18 common-leg factorization gives many exact-two ambient pairs through one shared edge. Adding the space norm produces a simultaneous square condition on the two completion legs. Reorganizing it as a fixed-edge divisor problem did not produce an independent infinite target family. Its successful low-dimensional specialization is again represented by F50-S1.

Verdict: `SUBSUMED_BY_QUARTIC_BREAKTHROUGH_FOR_CURRENT_CHECKPOINT`.

The policy requires four fresh candidates only when no breakthrough is found. Four are nevertheless recorded here to preserve the exploration ledger.

## 3. Stage18 explicit-family lift test

The canonical Stage15-2 ambient lower family chose coprime odd `p,q`, so the entire old subfamily is excluded from Stage19 by

\[
17(p^4+q^4)\equiv2\pmod{16}.
\]

That old congruence remains correct **for the odd/odd subfamily only**. The broader algebraic family was not exhausted by that parity specialization. Mixed-parity points on `C_17` revive the same formulas and satisfy the exact space condition.

Thus the old Stage23 revalidation verdict `R60-01 DEAD_CONFIRMED_GLOBAL_MOD16` is scope-correct for odd/odd parameters but is superseded as a statement about the broader formula family:

```text
OLD_ODD_ODD_SUBFAMILY_DEAD=true
BROADER_STAGE15_2_ALGEBRAIC_FORMULA_DEAD=false
MIXED_PARITY_VARIANT_REVIVED=true
```

This is the required direct Stage18-family space-lift test.

## 4. Lower-bound strength

The new theorem is

\[
N_2(B)\gg\sqrt{\log B}.
\]

Therefore

```text
STAGE19_UNBOUNDEDNESS_PROVED=true
INFINITE_PRIMITIVE_CONSTRUCTION_PROVED=true
POSITIVE_POWER_LOWER_BOUND_PROVED=false
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
```

The polynomial lower exponent is still zero. Checkpoint50 does not claim any `B^delta` lower bound.

## 5. Old-dead-branch policy

The controller requires reopening at least eight old branches **if checkpoint50 ends negative**. It does not end negative: F50-S1 supplies a positive theorem-level construction. Hence the eight-branch negative-result gate is not triggered.

One old branch, R60-01, is nevertheless reopened because it is directly superseded by the new mixed-parity mutation. The other Stage23-60 revalidation conclusions are not needed to prove the new lower theorem and are not rewritten.

## 6. Numerical reuse

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R03,24-14num-r201,24-14num-r202
NUM_POPULATION_MATCH=EXACT
NUM_EVIDENCE_LEVEL=EXACT_FINITE_ORACLE_PLUS_NEW_THEOREM_CONSTRUCTION
NUM_NEW_COMPUTATION_JUSTIFIED=TARGETED_CONSTRUCTION_REGRESSION_ONLY
```

The new computation checks two exact quartic witnesses, the elliptic reduction certificate, and the genus arithmetic. It does not rerun or extend the census.

## 7. Exit

```text
FRESH_STAGE19_LOWER_SURGEON_EXECUTED=true
FRESH_LOWER_CANDIDATES=4
BREAKTHROUGH_FOUND=true
STAGE18_EXPLICIT_FAMILY_SPACE_LIFT_TEST=PASS_MIXED_PARITY_VARIANT
STAGE19_UNBOUNDEDNESS_PROVED=true
INFINITE_PRIMITIVE_STAGE19_CONSTRUCTION_PROVED=true
NEW_LOWER_BOUND=N2(B)>>sqrt(log B)
POSITIVE_POWER_LOWER_BOUND_PROVED=false
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
OLD_DEAD_BRANCH_EIGHT_REVALIDATION_TRIGGERED=false
HISTORY_SUPERSESSION_BACKFLOW_REQUIRED_AFTER_AUDIT_PASS=true
AUDIT_REQUIRED=true
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=50
MERGE_ALLOWED=false
```
