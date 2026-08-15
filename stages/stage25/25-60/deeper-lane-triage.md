# Stage25-60 — deeper-lane triage after the audited quarter-power breakthrough

STATUS=COMPLETE_FOR_CHECKPOINT60
GOAL=TEST_WHETHER_CURRENT_LIVE_LANES_CERTIFY_EXPONENT_ABOVE_1/4

The entering audited theorem is

\[
B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

Checkpoint60 deliberately reopens every live checkpoint50 lane before causal closeout.

## R502 — Meskhishvili third parametrization

The third one-parameter NPC parametrization has the same maximal homogeneous degree eight as r501. A reduced rational parameter has two integer height coordinates, so the same direct rational-height mechanism has scale `T^2` parameters at `T^8` raw height and therefore exponent `1/4`.

This can provide an independent same-exponent family after its own exact primitive/mask audit, but a finite union of degree-eight one-parameter families does not raise the polynomial exponent.

```text
R502_STATUS=LIVE_SAME_EXPONENT_FALLBACK
R502_EXPONENT_ABOVE_QUARTER_FROM_DEGREE_COUNT=false
```

## R503 — Yoshida varying elliptic fibers

Primary source: Takumi Yoshida, *The relationship between face cuboids and elliptic curves*, arXiv:2407.09825, current manuscript dated 2026-03-22.

The paper supplies a `32:1` map from non-torsion points on the family

\[
E_{1,s}: y^2=x(x-(2s)^2)(x+(s^2-1)^2)
\]

to rational face-cuboid similarity classes and proves infinitely many rational `s` with positive rank. This is a genuine higher-dimensional structural receiver.

However, the paper does not provide the uniform bounded-height counting theorem required here: we would need a lower bound for the number of pairs `(s,P)` whose resulting exact Stage19 primitive height is `<=B`, uniformly while the elliptic fiber varies. The fixed-fiber construction from multiples of one non-torsion point has quadratic canonical height and exponential coordinate height, so by itself it returns only logarithmic-type counting rather than a polynomial exponent competitive with r501.

```text
R503_STATUS=OPEN_HIGH_VALUE
R503_32_TO_1_STRUCTURE=FOUND
R503_UNIFORM_VARYING_FIBER_HEIGHT_COUNT=NOT_PROVED
R503_EXPONENT_ABOVE_QUARTER=NOT_CERTIFIED
```

## R504 — symmetric-k quartic aggregation

Stage24 introduced

\[
e=2kpq,\quad x=k^2p^2-q^2,\quad y=k^2q^2-p^2,
\]
with space receiver

\[
p^4+q^4=(k^4+1)Z^2.
\]

Writing `t=q/p`, the genus-one fiber is

\[
C_k:\quad t^4+1=(k^4+1)z^2.
\]

There is a rational section `(t,z)=(k,1)`. Under

\[
X=-4t^2/z^2,\qquad Y=4t(t^4-1)/z^3,
\]
this maps to

\[
E_k:Y^2=X^3-4(k^4+1)^2X,
\]
\[
P(k)=(-4k^2,4k(k^4-1)).
\]

The specialization `k=2` is the audited infinite-order Stage24 point `(-16,120)`. Therefore the generic section `P(k)` is non-torsion over `Q(k)`; otherwise every good specialization, including `k=2`, would be torsion.

The third multiple yields an explicit nondegenerate rational section:

\[
t_3=
\frac{k(k^8-6k^4-3)}{3k^8+6k^4-1},
\]

\[
z_3=
\frac{k^{16}+28k^{12}+6k^8+28k^4+1}
{(3k^8+6k^4-1)^2},
\]
which satisfies `t_3^4+1=(k^4+1)z_3^2` identically.

This proves that the symmetric-k surface has a genuine non-torsion moving section, not just the isolated `k=2` fiber. Quantitatively, however, inserting this section into the cuboid formulas produces much higher rational-height degree than r501 (the direct integer-k representative has raw space degree 20). No primitive-height compression or two-dimensional uniform count is proved that beats the audited `1/4` exponent.

```text
R504_STATUS=STRUCTURAL_PROGRESS_NO_LOWER_UPGRADE
R504_GENERIC_NONTORSION_SECTION_PROVED=true
R504_EXPLICIT_3P_SECTION_PROVED=true
R504_EXPONENT_ABOVE_QUARTER=NOT_PROVED
```

## R505/R506 — common-core and common-leg receivers

Both remain population-compatible receivers, but neither currently closes an injective primitive polynomial-height family with a dimension/degree ratio exceeding `2/8`.

```text
R505_STATUS=OPEN_NO_QUANTITATIVE_CLOSURE
R506_STATUS=OPEN_NO_QUANTITATIVE_CLOSURE
```

## Search conclusion

The r501 family is now proved to have exact internal growth `Theta(B^(1/4))`, so its own gcd cannot hide a stronger exponent. R502 is same-degree. R503 is the highest-value open route but lacks a uniform varying-fiber height count. R504 gains a new generic non-torsion section but its available explicit section has worse height degree. R505/R506 have no closed count.

Thus checkpoint60 finds **new structure but no certified global exponent above `1/4`**.

```text
HIGHER_THAN_ONE_QUARTER_SEARCH=EXECUTED
HIGHER_THAN_ONE_QUARTER_LOWER_PROVED=false
MATCHING_HALF_POWER_LOWER_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
BEST_OPEN_LANE=R503_YOSHIDA_UNIFORM_VARYING_FIBER_HEIGHT
SECOND_OPEN_LANE=R504_SYMMETRIC_K_UNIFORM_AGGREGATION
SEARCH_STOP_REASON=current remaining upgrades require a genuinely new uniform height/count theorem, not another algebraic substitution inside the audited r501 family
```
