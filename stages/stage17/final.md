# Stage17 final self-contained interface bundle — R01

```text
BUNDLE_ID=STAGE17-FINAL-SELF-CONTAINED-20260814-R01
STATUS=CANDIDATE_PENDING_FRESH_STAGE17_AUDIT
STANDARD=SELF_CONTAINED_REVIEW_STANDARD_V1
SOURCE_SNAPSHOT_BASE=ae6c43a569544ef1f5b5d531551e651dc09504c8
```

## Executive theorem

Let `N_1(B)` count primitive canonical cuboids with `0<a<b<c`, `gcd(a,b,c)=1`, exactly one integral face diagonal, integral space diagonal, and `R=sqrt(a^2+b^2+c^2)<=B`. Then

\[
\boxed{N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3},\qquad \frac{\kappa}{24\pi}>0.
\]

If `M_1(B)` is the same exactly-one-face population before integral space diagonal is imposed, then

\[
\boxed{M_1(B)\asymp B^2\log B},\qquad
\boxed{\frac{N_1(B)}{M_1(B)}\asymp\frac{(\log B)^2}{B}\to0}.
\]

If `H_{1,d}(B)` counts the same primitive canonical integral-space-diagonal population with at least one integral face, then

\[
\boxed{H_{1,d}(B)\sim N_1(B)},\qquad
\boxed{N_1(B)/H_{1,d}(B)\to1}.
\]

## Population and exact cutoff adapter

Write the positive integral space diagonal as `d`. Since

\[
d^2=a^2+b^2+c^2=R^2
\]

and `d,R>0`,

\[
\boxed{d=R},\qquad \boxed{d\le B\iff R\le B}.
\]

This is an identity, with no measure, multiplicity, or quantifier loss.

## Frozen Stage13 interface

Completed Stage13 counts positive quadruples `(a,b,c,d)` with

\[
a<b<c,\quad \gcd(a,b,c)=1,\quad a^2+b^2+c^2=d^2,\quad d\le B,
\]

and exactly one integral face. Its frozen theorem is

\[
N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3.
\]

It also proves, for its raw face-incidence overlaps,

\[
A_{ab,ac},A_{ab,bc},A_{ac,bc},A_3=o(B(\log B)^3).
\]

The Stage17 edge ordering, gcd condition, exactly-one predicate, and space equation are literal matches. The only differently written cutoff is identified exactly by `d=R` above.

```text
UPSTREAM_STAGE=Stage13
POPULATION_MATCH=true
CUTOFF_MATCH=true_after_d_equals_R
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
```

Therefore the Stage13 asymptotic transfers to Stage17 without loss.

## Frozen Stage16 interface and survival proof

Completed Stage16 counts the same primitive canonical exactly-one-face objects under `R<=B` before integral `R` is imposed and proves

\[
M_1(B)\asymp B^2\log B.
\]

Stage17 is the literal subset

\[
\mathcal B_{1,d}(B)=\mathcal B_1(B)\cap\{R\in\mathbf Z\}.
\]

Thus `N_1(B)<=M_1(B)` pointwise. Since the transferred Stage13 theorem gives

\[
N_1(B)\asymp B(\log B)^3,
\]

division by the Stage16 `Theta` law gives

\[
\boxed{N_1(B)/M_1(B)\asymp(\log B)^2/B\to0}.
\]

No ratio asymptotic `~ C(log B)^2/B` is claimed because Stage16 has no certified leading constant for `M_1(B)`.

## Exactly-one dominance after imposing the space diagonal

Let

\[
P(B)=A_{ab,ac}+A_{ab,bc}+A_{ac,bc}.
\]

Every object in `H_{1,d}(B)-N_1(B)` has at least two integral faces, hence contributes to at least one pair overlap. Therefore

\[
0\le H_{1,d}(B)-N_1(B)\le P(B).
\]

The frozen Stage13 overlap theorem gives `P(B)=o(B(log B)^3)`. Since `N_1(B)` has a positive main term of order `B(log B)^3`,

\[
H_{1,d}(B)=N_1(B)+o(B(\log B)^3),
\]

so

\[
\boxed{H_{1,d}(B)\sim N_1(B)},\qquad
\boxed{N_1(B)/H_{1,d}(B)\to1}.
\]

This does not assume perfect cuboids do not exist. Three-face objects lie inside the lower-order overlap correction.

## Structural cause

For the unique integral face write

\[
x^2+y^2=p^2
\]

and let `z` be the complementary edge. Then

\[
R^2=x^2+y^2+z^2=p^2+z^2.
\]

Hence Stage17's new requirement is exactly

\[
\boxed{p^2+z^2=d^2}.
\]

The Stage16-to-Stage17 change is therefore a second Pythagorean extension sharing the face diagonal `p`. Its audited net conditional survival scale is `Theta((log B)^2/B)`.

Canonical ordering, primitivity, exactly-one source multiplicity, the common cutoff, and `d=R` are not new thinning mechanisms. The logarithmic correction is a net count comparison, not a factorization into independent probabilities.

## Intrinsic-status boundary

The **absolute Stage17 population law** is settled at full asymptotic resolution:

```text
TRUE_ORDER_IDENTIFIED=true
POLYNOMIAL_EXPONENT=1
LOG_POWER=3
LEADING_CONSTANT_PROVED=true
LEADING_CONSTANT=kappa/(24*pi)
ABSOLUTE_INTRINSIC_STATUS=PROVED_ASYMPTOTIC
```

A different question remains open: whether the space-diagonal condition is intrinsically strong in the ambient cuboid population or becomes differently costly after one integral face has already been imposed. That requires Stage16S and belongs to Stage21.

```text
SPACE_DIAGONAL_COST_INTRINSICNESS=DEFER_TO_STAGE21_WITH_STAGE16S
INDEPENDENCE_CLAIM=false
CORRELATION_CLASSIFICATION=false
```

Stage16S is parallel and does not block Stage17 closure.

## Finite evidence and construction boundary

Stage17-20 froze the exact finite counts

```text
B:   50  100  200  400  800  1200  1600  2000
N1:   7   25   67  174  453   764  1077  1434
```

with CSV SHA-256 `2f066143090713c25eec2e8ecef7a31d5c5ec169dc008380577757b34674168a`; direct canonical brute force matched the optimized enumerator through `B=200`. These data are `COMPUTED` diagnostics only.

AR-039 supplies an explicit Stage17 subfamily with

\[
N_1(B)\ge\frac{\sqrt2}{120\pi^2}B^{1/2}-O(B^{1/4}\log B).
\]

It is a lower-order constructive survivor family, not the mechanism for the full asymptotic.

## Non-claims and stop rule

Stage17 does not prove a leading constant for `N_1/M_1`, an effective error term for the Stage13 asymptotic, an effective rate for `N_1/H_{1,d}->1`, independence of face and space integrality, the Stage16S comparison, or any perfect-cuboid existence/nonexistence theorem.

Further refinement requires a new Stage16 leading-constant theorem, a new effective Stage13 theorem, more Stage16S work, or the Stage21 interaction comparison. These are new inputs or off-stage work.

```text
POPULATION_DRIFT=false
CUTOFF_DRIFT=false
MULTIPLICITY_DRIFT=false
FINITE_DATA_PROMOTED_TO_THEOREM=false
DOUBLE_CHARGE_CHECK=PASS
SYNTHESIS_STOP_RULE_SATISFIED=YES
```

## Provenance and audit lock

Canonical Stage17 records are `stages/stage17/17-{10,20,30,40,50,60}/`, `stages/stage17/17-70/result.md`, and this bundle. Frozen upstream interfaces are `stages/stage13/final.md` and `stages/stage16/final.md`. Policy is fixed by `docs/stage16-28-population-roadmap.md`, `docs/stage16-28-stage70-policy.md`, and `docs/self-contained-review-standard.md`.

A fresh Stage17 auditor must verify the exact Stage13 target match, the exact Stage16 source match, `d=R`, the ratio derivation, the pair-overlap proof of `N_1/H_{1,d}->1`, and the Stage16S/Stage21 boundary.

```text
BUNDLE_ID=STAGE17-FINAL-SELF-CONTAINED-20260814-R01
STATUS=CANDIDATE_PENDING_FRESH_STAGE17_AUDIT
FROZEN_UPSTREAM_INTERFACES=Stage13,Stage16
INTERNAL_LOAD_BEARING_ADAPTERS_EMBEDDED=true
EXTERNAL_THEOREMS_DIRECTLY_INVOKED=NONE
FINITE_DATA_PROMOTED_TO_THEOREM=false
PRIMARY_THEOREM=N_1(B) ~ kappa/(24*pi) B(log B)^3
MATCHED_SURVIVAL=N_1(B)/M_1(B) ASYM (log B)^2/B -> 0
AT_LEAST_ONE_DOMINANCE=N_1(B)/H_{1,d}(B) -> 1
SPACE_DIAGONAL_COST_INTRINSICNESS=DEFER_TO_STAGE21_WITH_STAGE16S
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_REQUIRED=true
```
