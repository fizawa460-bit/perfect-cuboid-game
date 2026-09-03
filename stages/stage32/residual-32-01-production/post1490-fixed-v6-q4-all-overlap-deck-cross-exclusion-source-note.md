# Stage32 post-1490 fixed-V6 q'=4 all-overlap deck-cross exclusion

Scope: exact recovered V6 class `g1-d186`, `d=186`, `e=266`, `z=(-15,62,-44,26,32)`. This note generalizes only the O-independent quotient/Picard portion of the hostile-audited O=210 argument. It does not reuse the O=210 first-projection etale specialization, the O=210 forced `210 x m1 + 28 x m2` histogram, or any O=210-only Hurwitz witness.

## Retained source-locked geometry

The post-1473 Beauville odd-branch source note fixes the normalized exceptional pullback

`D_E = sum_P m_P P`, `sum_P m_P = e = 266`, `O=#{P:m_P odd}`,

and the resolved Beauville double cover `Xtilde -> Btilde`. For every surviving overlap here `O>=210>0`, the normalized pullback `Y->N` is connected.

The post-1484 modular-factor boundary fixes the two maps `N->X(4)` to degrees `(105,81)` and excludes `q'=1,2` by integrality. Thus only `q'=4` remains.

The source-locked subgroup quotient square is independent of O:

- `B=P/G_diag`,
- `X=P/H_diag`,
- `C0=X(8)/H`,
- `Q=C0 x C0=P/(H x H)`,
- `X->Q` is finite etale of degree four with deck group `(H x H)/H_diag ~= V4`,
- `X` is the common degree-two pullback of `C0->X(4)` over either factor map.

Therefore, for any hypothetical integral carrier in the fixed class, the connected Beauville pullback `Y` maps to each `C0` with degrees `(105,81)`.

## Pair-map birationality is O-independent

Let `Gamma` be the image of the pair map

`Y -> Q=C0 x C0`.

The generic degree of this map is a stabilizer degree for the V4 cover `X->Q`, hence lies in `{1,2,4}`. It also divides both projection degrees 105 and 81, hence divides `gcd(105,81)=3`. Therefore the generic degree is one.

So for every surviving O in this fixed q'=4 class:

- `Y -> Gamma` is birational;
- `Gamma` is integral;
- `Gamma` has bidegree `(105,81)`.

No O=210 etale-projection hypothesis enters this argument.

## O-independent V4 translate-sum identity

Let `D` be the irreducible carrier-image curve on `X` whose normalization is `Y`. The exact Beauville pullback/strict-transform adapter used in the audited O=210 leaf depends only on the fixed V6 divisor class and the resolved quotient geometry, not on a choice of branch partition. It gives the same fixed class `D` for every hypothetical carrier in this V6 class.

On `Q=C0 x C0`, with `g(C0)=2`, a bidegree `(105,81)` curve has

`Gamma^2 = 2*105*81 = 17010`.

Because `q:X->Q` is finite etale V4 and `D->Gamma` is birational,

`q^*Gamma = D + uD + vD + uvD`.

Squaring and using deck symmetry gives

`4*Gamma^2 = 4*D^2 + 4*(D.uD + D.vD + D.uvD)`,

hence the exact required identity

`D.uD + D.vD + D.uvD = Gamma^2 - D^2`.

The exact fixed-class Beauville self adapter gives

`D^2 = 3874`.

Therefore every hypothetical q'=4 carrier in this fixed V6 class must satisfy

`D.uD + D.vD + D.uvD = 17010-3874 = 13136`.

This derivation is deliberately independent of `g(Y)`, `delta_D`, the O=210 first-projection etale condition, and the O=210 contact histogram.

## Exact Picard/deck side

The post-1490 equivariant Beauville deck-cross replay reconstructs the exact recovered V6 class from all 140 pairings, applies the source-locked modular/Stoll actions

`u=g7*g9`, `v=g7*g8`, `uv=g8*g9`,

and transports them through the explicit Beauville pullback/blowdown correction. Since these data are properties of the fixed divisor class, their values do not depend on O:

- `D.uD=3892`,
- `D.vD=4020`,
- `D.uvD=4020`,
- total `11932`.

Thus the fixed-class Picard/deck total differs from the O-independent quotient requirement by

`13136-11932 = 1204`.

Consequently no hypothetical q'=4 integral genus-one carrier in the exact recovered V6 class can exist for any overlap compatible with the retained fixed-class setup. Combined with the already audited modular-factor integrality exclusion of `q'=1,2`, this provisionally excludes all integral genus-one carriers in this exact V6 class, pending hostile audit of this generalization.

## Firewalls

- This is a fixed exact V6 class exclusion only; it does not close all Stage32 receiver rows or FULL178.
- The new step is the O-independent generalization of the quotient-square/deck-cross contradiction. It requires hostile audit before promotion.
- No arbitrary `Pic(B)` class is identified with `Pic(X)`; the explicit equivariant Beauville adapter remains mandatory.
- No effectivity, receiver, route, theorem, endpoint, perfect-cuboid existence, or perfect-cuboid nonexistence credit follows.
