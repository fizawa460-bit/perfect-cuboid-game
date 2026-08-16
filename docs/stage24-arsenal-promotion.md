# Stage24 arsenal promotion — exactly-two ambient to exactly-two + space

PROMOTION_ID=AR-STAGE24-TRANSITION-M2-N2
STATUS=AUDITED_PASS_CLOSED_WITH_STAGE25_LOWER_SUPERSESSION
SOURCE_STAGE=Stage24
SOURCE_CHECKPOINT=70

## Purpose

Portable interface for later Stage25/26/27/28 work and any future Stage19 lower-bound analysis. This promotion packages three Stage24-specific outputs that were not available at the historical Stage19 closeout:

1. the historical Stage24 two-sided Stage18 -> Stage19 population interface,
   whose lower side was later strengthened by Stage25;
2. the mixed-parity C17 infinite primitive construction;
3. the independent degree-two space-square thin-cover zero-density route.

## Exact population contract

```text
SOURCE=M2(B)
SOURCE_POPULATION=primitive canonical 0<a<b<c; gcd(a,b,c)=1; exactly two integral face diagonals; no space requirement
TARGET=N2(B)
TARGET_POPULATION=source population plus integral R=sqrt(a^2+b^2+c^2)
CUTOFF=R<=B
LITERAL_SUBSET_TRANSITION=true
POPULATION_ADAPTER_REQUIRED=false
CUTOFF_ADAPTER_REQUIRED=false
MULTIPLICITY_ADAPTER_REQUIRED=false
```

## Reusable transition theorem

The audited source/target stack gives

\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0,
\]

\[
B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

Therefore

\[
\boxed{
B^{-3/4}(\log B)^{-5}
\ll
N_2(B)/M_2(B)
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-5}
}
\]

and

\[
\boxed{N_2(B)/M_2(B)\to0,\qquad N_2(B)\to\infty.}
\]

Reuse label:

```text
TRANSITION_CLASS=THIN_BUT_INFINITE
TRUE_TARGET_EXPONENT_IDENTIFIED=false
```

Do not convert the half-power upper into an asymptotic or an intrinsic exponent claim.

## Reusable C17 lower family

For coprime positive parameters satisfying

\[
p^4+q^4=17Z^2,
\]

define

\[
e=4pq,
\qquad x=4p^2-q^2,
\qquad y=4q^2-p^2,
\qquad D=17Z.
\]

Then

\[
e^2+x^2=(4p^2+q^2)^2,
\]
\[
e^2+y^2=(4q^2+p^2)^2,
\]
\[
e^2+x^2+y^2=D^2.
\]

On the physical cone

\[
1<q/p<(1+\sqrt2)/2,
\]

the canonical ordering is

\[
(a,b,c)=(x,y,e).
\]

The genus-one curve `17z^2=t^4+1` has positive rank. The third-face-square sublocus is a connected genus-five curve and therefore has only finitely many rational points. Elliptic height growth and real-component density yield

\[
\boxed{N_2(B)\gg\sqrt{\log B}}.
\]

Directional consequence on this cone:

\[
\boxed{N_{2,c}(B)\gg\sqrt{\log B}}.
\]

The historical odd/odd specialization remains impossible modulo 16. The reusable lesson is that parity strata of the same ambient algebraic formula can have qualitatively different space-lift behavior. Its quantitative `sqrt(log B)` lower is superseded by S25-W01, but the construction remains a parked parity-stratum example.

## Reusable space-square thin-cover route

On the shared-edge double-Pythagorean surface

\[
u^2=e^2+x^2,
\qquad
v^2=e^2+y^2,
\]

adjoin

\[
w^2=e^2+x^2+y^2.
\]

On the affine dense chart `e=1`, with independent Pythagorean parameters

\[
x=2t/(1-t^2),
\qquad
y=2s/(1-s^2),
\]

the radicand is

\[
f=\frac{u^2s^4+(4-2u^2)s^2+u^2}{(1-s^2)^2}.
\]

Writing `z=s^2`, the numerator quadratic has discriminant

\[
-16x^2\ne0
\]

generically and nonzero constant term, so it has four simple roots as a polynomial in `s`. Hence `f` is not a square in the geometric function field. The normalization is therefore a geometrically integral generically degree-two cover, and its rational image is type-II thin.

Under the already-verified anticanonical toric thin-set theorem on the same Stage18 host,

\[
N_2(B)=o(B(\log B)^5),
\]
so

\[
N_2(B)/M_2(B)\to0.
\]

This route is qualitative only. Do not multiply its little-o saving with the Stage14 half-power upper or with the fixed-prime squareclass sieve.

## Interaction firewall

Later stages may compare this transition against Stage16S/21/22/23, but the following are mandatory:

- Stage16S ambient `B^-1` space cost is a comparator, not an independent factor to multiply;
- Stage21 `(log B)^2` enhancement belongs to the one-face host and does not automatically transfer to Stage24;
- Stage23 already contains space in its source and must not charge space twice;
- `N2/N1` and `M2/M1` are adjacent-stratum count ratios, not objectwise survival probabilities;
- the Stage25 cross-ratio sign is positive divergent, but it remains a matched
  population interaction invariant rather than an independent probability;
- C17 is a lower witness, not evidence for bulk density.

## Reuse conditions

Direct reuse requires exact population, canonicalization, primitivity, physical cutoff and multiplicity match. If a later stage changes from exactly-two to at-least-two, changes the height, or marks distinguished faces/incidences, an explicit adapter is required.

## Nonclaims

```text
POSITIVE_POWER_LOWER_BOUND_PROVED=true
CURRENT_POSITIVE_POWER_LOWER_BOUND=N2(B)>>B^(1/4)
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
STRICT_SUB_SQRT_WHOLE_FAMILY_UPPER_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_INTRINSIC_PROVED=false
HALF_POWER_CAUSAL_MECHANISM_IDENTIFIED=false
STAGE24_GLOBAL_INTERACTION_SIGN=POSITIVE_DIVERGENT_BY_STAGE25_BACKFLOW
SECOND_ORDER_INTERACTION_SIGN=POSITIVE_DIVERGENT_BY_STAGE25_BACKFLOW
SURVIVOR_RATIO_LEADING_CONSTANT_AVAILABLE=false
PERFECT_CUBOID_CONCLUSION=NONE
```

```text
ARSENAL_PROMOTION_REQUIRED=true
ARSENAL_PROMOTION_DECISION=YES
ARSENAL_PROMOTION_MATERIALIZED=true
REUSE_CLASS=DIRECT_ON_EXACT_STAGE24_CONTRACT_WITH_EXPLICIT_ADAPTER_REQUIRED_OTHERWISE
AUDIT_REQUIRED=false
C17_STATUS=PARKED_PARITY_EXAMPLE_SUPERSEDED_AS_GLOBAL_LOWER
SPACE_SQUARE_THIN_COVER_STATUS=PARKED_ALTERNATE_QUALITATIVE_PROOF
```
