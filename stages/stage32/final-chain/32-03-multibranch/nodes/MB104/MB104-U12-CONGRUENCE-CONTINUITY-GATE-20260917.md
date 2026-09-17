# Stage32 MB104 — U12 congruence-continuity gate — 2026-09-17

Status: **LEVEL-2 COMMON DESCENT REJECTED / DEEPER DYADIC LEVEL HOLD / P167 PREMATURE / NO CREDIT**

## Scope and correction check

This note continues from `MB104-U3-U4-U12-PORTFOLIO-GATE-20260917.md`.
It first checks that U12 is using the correct curve.  The original product
factor is the genus-five modular curve `X=X(8)`, but Stoll--Testa supply the
free order-four quotient

```text
C2=X/G0+ : y^2=2(x^5-x),
```

which is the genus-two Bolza curve.  The dangerous lift has two etale maps
`B->C2` of degree `56l`, and the exact two-fibre packet gives the pullback
equality of two specified odd theta characteristics.  Thus the Bolza/six-spin
reduction is internally consistent; it is not a substitution of `C2` for
`X(8)`.

## Why one finite-valued spin test is not automatically fixed-level

For a commensurator element `g`, write

```text
Lambda_g = Gamma intersect g^(-1) Gamma g.
```

The cross-leg spin difference is a sign character on `Lambda_g`.  Although
its values lie in `F2`, the subgroup `Lambda_g` changes with `g`.  Therefore
finite codomain alone does not imply that the predicate factors through one
fixed congruence quotient of `Gamma`.

A sufficient all-`l` adapter would require the two retained spin splittings,
including their affine offsets, to extend compatibly to one fixed open
subgroup of the dyadic/metaplectic completion.  Neither the Arsenal nor the
retained Bolza source proves this congruence continuity.

## Exact level-two obstruction

Let

```text
V = H^1(Gamma,F2) = J(C2)[2],                 dim V=4,
N = P Q_B^1(2),
W = Hom(Gamma/N,F2),                          dim W=2.
```

The principal level subgroup `N` is normalized by the Bolza level symmetry,
so, after source-locking the retained marking, the injection `W->V` is
`S4`-equivariant.  The exact six-Weierstrass replay gives

```text
V - {0} = orbit_3 disjoint_union orbit_12.
```

There is a unique `S4`-stable two-plane: its three nonzero elements are the
opposite-edge/Richelot orbit.  The retained difference

```text
delta=[w0-w1]
```

is an adjacent-edge class in the twelve-element orbit.  Hence

```text
delta notin W.
```

Consequently the two retained spin splittings cannot both descend from one
common level-two metaplectic extension: the difference of two such descended
splittings would lie in `W`.

This proves only the scoped rejection

```text
U12_COMMON_LEVEL2_SPIN_DESCENT=REJECT.
```

It does not prove that `delta` remains outside every deeper level.  For
principal dyadic levels `N_k`, the images

```text
W_k = image(Hom(Gamma/N_k,F2) -> V)
```

may grow from dimension two to dimension four.  Nor does failure of common
splitting descent exclude an accidental finite factorization of the boolean
cross-leg predicate without a necessity lemma.

## The decisive shallow all-level test

Before constructing a single large split-prime correspondence, compute

```text
W_infinity = image(Hom_cont(closure_dyadic(Gamma),F2) -> V)
```

from the Frattini quotients of the dyadic division-unit filtration until the
image stabilizes.

- If `dim W_infinity=2`, then `delta` is outside every dyadic congruence level;
  common fixed-level spin descent is excluded for all `k`.
- If `dim W_infinity=4`, deeper level can see the adjacent class and U12
  remains live, subject to the affine metaplectic conjugation law.
- If the image or its marking cannot be source-locked, stop rather than infer
  it from abstract dimensions.

This is the next all-`l` gate.  It is preferable to an isolated `p=167` test.

## What is and is not materialized at `p=167`

The finite reduction can be made explicit.  Since

```text
sqrt(2) = 13 or 154 mod 167,
(167)=(13+sqrt(2))(13-sqrt(2)),
```

one retained matrix realization has

```text
rho(alpha) = [[84,41],[1,84]],
rho(beta)  = [[86,118],[64,82]]   for sqrt(2)=13,
rho(beta)  = [[84,31],[136,84]]   for sqrt(2)=154.
```

These matrices give the `PSL2(F167)` reduction, the Borel inverse image, and
the index-168 first leg.  They do not determine the second leg.  Missing are:

1. a global quaternion/Hecke-ideal representative of reduced norm
   `13+sqrt(2)` or `13-sqrt(2)`, giving conjugation for the second embedding;
2. a marked bridge from the Stoll--Testa points `w0,w1` to the six spin lifts
   in the Katz surface-group presentation.

Thus the isolated finite computation is partially materializable but not
currently executable.  Even after those inputs are supplied it closes only
one double coset and its symmetry orbit unless the all-level factorization is
proved.

## U3 comparison

The only new singular-divisor extension candidate found in the parallel
shallow search accepts an effective singular divisor but requires the map to
be defined on that divisor scheme, not merely on its normalization.  The
current product-cover map has not been shown constant on every normalization
fibre.  Proving that descent reopens the parked conductor/pair-gluing problem.
Moreover the available degree-`56l` pencil fails the candidate theorem's
numerical threshold (`D_l^2=336l^2` versus a lower bound asymptotic to
`1568l^2` already at irregularity two).  Hence this does not replace U12.

## Updated frontier

```text
U12_COMMON_LEVEL2_SPIN_DESCENT=REJECT
U12_FIXED_DYADIC_LEVEL_ALL_K=HOLD
U12_P167_FINITE_REDUCTION_MATERIALIZED=true
U12_P167_SECOND_LEG_MATERIALIZED=false
U12_P167_MARKED_SPIN_BRIDGE_MATERIALIZED=false
U3_SINGULAR_DIVISOR_EXTENSION=BLOCKED_DESCENT_AND_NUMERICS
```

Next leaf:

```text
U12-DYADIC-FRATTINI:
  compute and mark W_infinity; stop U12 if its dimension remains two.
```

## Firewalls

```text
MB104_complete=false
all_l_exclusion_proved=false
finite_degree_window_proved=false
receiver_credit=false
effectivity_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
