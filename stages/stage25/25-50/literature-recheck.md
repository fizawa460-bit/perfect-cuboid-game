# Stage25-50 literature recheck

ROLE=PRIMARY_SOURCE_PROVENANCE_AND_DEEPER_LANE_TRIAGE
STATUS=COMPLETE_FOR_R501;OPEN_FOR_HIGHER_EXPONENT_LANES

## Meskhishvili 2015 — direct formula provenance

Mamuka Meskhishvili, *Parametric Solutions for a Nearly-Perfect Cuboid*, arXiv:1502.02375.

The paper treats the case where one face diagonal is the only potentially irrational length and gives three one-parameter rational parametrizations. Its first parametrization is exactly the dehomogenized source of Stage25-r501:

\[
a=16t^2(t^4-9),
\]
\[
b=(t^4-10t^2+9)(t^4+2t^2+9),
\]
\[
c=4t(t^2+3)(t^4-10t^2+9),
\]
\[
d_{ac}=4t(t^2+3)(t^4-2t^2+9),
\]
\[
d_{bc}=(t^4-1)(t^4-81),
\]
\[
d_s=t^8+46t^4+81.
\]

The paper also writes the remaining-face square condition explicitly as the condition that `a^2+b^2` be square.

Stage25 does not import any counting claim from the paper. It homogenizes with `t=m/n`, proves a fixed physical cone, primitive reduction, bounded similarity multiplicity, a genus-seven exceptional curve, and the `B^(1/4)` count independently.

The third parametrization also has maximal homogeneous degree eight and is retained as a fallback same-exponent lane. The second has maximal degree twelve and is lower priority for exponent improvement.

## Yoshida 2024 / revision 2026 — elliptic-surface direction

Takumi Yoshida, *The relationship between face cuboids and elliptic curves*, arXiv:2407.09825, revision dated 2026-03-22.

The paper defines rational face cuboids as cuboids with rational edges, two rational face diagonals and rational space diagonal. It constructs a finite-to-one map from rational elliptic-curve data to similarity classes of rational face cuboids and proves infinitely many such classes. It also proves infinitely many rational parameters `s` for which the associated elliptic curve has positive Mordell-Weil rank.

This is structurally relevant to a possible Stage25-r503 higher-dimensional count. However the current checkpoint does not yet have a uniform theorem controlling rational-point height while `s` varies, so Yoshida is not used to claim an exponent above `1/4`.

## Novelty boundary

```text
RATIONAL_NPC_PARAMETRIZATION_NOVEL=false
RATIONAL_FACE_CUBOID_INFINITUDE_NOVEL=false
STAGE25_REPO_NATIVE_NEW_CLAIM=exact_primitive_canonical_height_count_candidate_N2>>B^(1/4)
PRIMARY_LITERATURE_USED_AS_BLACK_BOX_COUNT=false
EXACT_STAGE19_ADAPTER_PROVED_SEPARATELY=true
```

## Deeper-search handoff

```text
R502_MESKHISHVILI_THIRD_FAMILY=OPEN_FALLBACK_SAME_EXPONENT
R503_YOSHIDA_UNIFORM_HEIGHT_OVER_VARYING_FIBERS=OPEN_HIGH_VALUE
R504_SYMMETRIC_K_QUARTIC_AGGREGATION=OPEN_HIGH_VALUE
HIGHER_THAN_ONE_QUARTER_LOWER=NOT_PROVED
MATCHING_HALF_POWER_LOWER=NOT_PROVED
```
