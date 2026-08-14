# Stage21-50 — lower-side mechanism and constructive-survivor diagnostic

EVIDENCE_LEVEL=PROVED
CHECKPOINT=50
STATUS=PROVED_CANDIDATE_PENDING_FRESH_AUDIT

## 1. Purpose

Checkpoint30 proves the exact conditional survival asymptotic

\[
N_1(B)/M_1(B)\sim (\kappa\pi/18)(\log B)^2/B.
\]

Checkpoint40 records that the two logarithms have not been uniquely factorized into audited local mechanisms. Checkpoint50 attacks the same question from below: can a known explicit survivor family explain the full transition scale?

## 2. Recovered constructive lower interface

The audited Stage17 final bundle records the AR-039 explicit Stage17 subfamily

\[
\boxed{N_1(B)\ge \frac{\sqrt2}{120\pi^2}B^{1/2}-O(B^{1/4}\log B)}.
\]

This family lies in the exact Stage17 population: primitive, canonical, exactly one integral face, integral space diagonal, common cutoff `R=d<=B`. Hence it is a legitimate constructive lower-side witness for Stage21.

No stronger explicit-family lower bound with the same population/cutoff was recovered in the Stage21-50 repository search. The full asymptotic lower side remains supplied by the Stage13/17 counting theorem, not by a known parametrized family.

## 3. Conditional lower bound from the explicit family

Using the Stage21-10/E-1e denominator

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B,
\]

the AR-039 family alone implies, for sufficiently large `B`, a constructive contribution on the scale

\[
\frac{N_{1,\mathrm{AR039}}(B)}{M_1(B)}\gg \frac{B^{1/2}}{B^2\log B}
=\boxed{B^{-3/2}(\log B)^{-1}}.
\]

More precisely, division of the displayed leading terms gives the benchmark coefficient

\[
\frac{\sqrt2/(120\pi^2)}{3/(4\pi^2)}=\frac{\sqrt2}{90},
\]

so the recorded AR-039 lower formula corresponds formally to

\[
N_{1,\mathrm{AR039}}(B)/M_1(B)\ge
(\sqrt2/90+o(1))B^{-3/2}(\log B)^{-1}
\]

when `N_{1,AR039}` denotes the certified constructed subset count behind that lower bound.

## 4. The explicit family cannot explain the full enhancement

The true conditional survival scale is

\[
B^{-1}(\log B)^2,
\]

whereas the recovered explicit family contributes only

\[
B^{-3/2}(\log B)^{-1}.
\]

Their scale ratio is

\[
\frac{B^{-3/2}(\log B)^{-1}}{B^{-1}(\log B)^2}
=B^{-1/2}(\log B)^{-3}\to0.
\]

Therefore

\[
\boxed{N_{1,\mathrm{AR039}}(B)=o(N_1(B))}.
\]

This is a useful negative mechanism result: the known explicit constructive survivor family is asymptotically negligible inside the full Stage17 population and cannot be the source of the `(log B)^2` conditional enhancement.

Equivalently, the main Stage21 phenomenon is genuinely a bulk counting effect in the Stage13/17 arithmetic population, not an artifact of the currently known low-dimensional explicit family.

## 5. Lower-bound ledger

There are two logically different lower statements and they must not be conflated:

1. **Full theorem lower side:** because `N1/M1 ~ C (log B)^2/B` with `C=kappa*pi/18>0`,
   \[
   N_1(B)/M_1(B)\gg (\log B)^2/B.
   \]
   This is sharp and comes from the full asymptotic theorem.
2. **Constructive-family lower side:** AR-039 gives only
   \[
   N_{1,\mathrm{AR039}}(B)/M_1(B)\gg B^{-3/2}(\log B)^{-1}.
   \]
   This is explicit but far below the true scale.

Thus an explicit-family explanation of the full enhancement remains open.

## 6. Mechanism status after the lower-side attack

```text
FULL_LOWER_SCALE=(log B)^2/B
FULL_LOWER_SCALE_SHARP=true
FULL_LOWER_SOURCE=Stage13/17 asymptotic counting theorem + E-1e denominator
EXPLICIT_FAMILY=AR-039
EXPLICIT_FAMILY_NUMERATOR_SCALE=B^1/2
EXPLICIT_FAMILY_CONDITIONAL_SCALE=B^-3/2*(log B)^-1
EXPLICIT_FAMILY_IS_NEGLIGIBLE_IN_N1=true
EXPLICIT_FAMILY_EXPLAINS_LOG_SQUARED_ENHANCEMENT=false
BULK_ARITHMETIC_EFFECT_REQUIRED=true
OPEN_GATE=LOG_SQUARED_ENHANCEMENT_BULK_MECHANISM_UNRESOLVED
```

Checkpoint50 therefore narrows the open gate: searching only for another presentation of AR-039 is not enough. A successful mechanism theorem must account for a positive proportion at the `B(log B)^3` numerator scale, or otherwise derive the two extra logarithms in the bulk counting architecture.

## 7. Boundary

No new parametrization, local-factor product, or density decomposition is asserted here. The AR-039 formula is reused exactly as frozen in the audited Stage17 bundle. Finite data are not promoted. The exact leading transition theorem from checkpoint30 is unchanged.

```text
UPSTREAM_PREMISE_CHECK=PASS
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
FINITE_DATA_USED_AS_PROOF=false
DOUBLE_CHARGE_CHECK=PASS
NEW_RESEARCH_RESULT=known explicit survivor family is asymptotically negligible and cannot explain the bulk enhancement
NEXT_CHECKPOINT=60
NEXT_EXPECTED_COMMAND=Stage21-audit
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
CODEX_REQUIRED=false
```
