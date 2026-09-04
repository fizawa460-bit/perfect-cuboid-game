# Stage32 post-1534 b3 cusp-orbit ambient-equivariance obstruction

Scope: fixed recovered V6 class `g1-d186`, retained `O=210`, `q'=4`, `Q=602`. This leaf follows the hostile-audited #1534 reduction

`[T,b3]=0  =>  Q(T) != 602`

but it does **not** prove or refute the actual Jacobian commutator `[T,b3]`. It closes only the most direct ambient/cusp-profile realization of the missing `b3` equivariance.

## Source-locked inputs

The marked-gauge asset source-locks the principal Bolza/G12 matrix

```
b3 = [[-1,-1],[1,0]]
```

over `Z[r]`, `r^2=-2`, to Sergio Cecotti, arXiv:2509.24605v1, Appendix B, equations (B.1)-(B.6). Exact multiplication gives `b3^3=I` and `b3!=I`, hence order 3 on the principally polarized Jacobian.

The hostile-audited transvection asset

`post1505-o210-q602-weierstrass-parity-transvection-refinement.json`

is now a direct source lock of this leaf. Its retained boundary-label/Weierstrass adapter gives

```
33 -> 6
36 -> 1
37 -> 5
40 -> 3
41 -> 4
44 -> 2
```

so the six retained second-factor boundary curves

```
33, 36, 37, 40, 41, 44
```

map bijectively onto the six Weierstrass ids `{1,2,3,4,5,6}`. The diagnostic and certifier assert both the six exact pairs above and the bijectivity. This is the semantic anchor that identifies these six retained boundary labels as one representative for each Bolza Weierstrass cusp.

The recovered V6 witness gives the exact all-140 Picard pairing vector. On those six source-locked second-factor Weierstrass representatives the numerical profile is

```
11, 22, 16, 11, 28, 22.
```

The retained H-deck adapter is

```
id = 1
u  = g7*g9
v  = g7*g8
uv = g8*g9.
```

Using the retained 140-class Stoll action, all four H-deck translates of the V6 numerical class have **the same** six-entry second-factor profile above.

## Why an ambient b3 action forces two 3-cycles on the six cusps

The Bolza curve is genus 2 and hyperelliptic. Any curve automorphism descends through the hyperelliptic quotient to an automorphism of `P^1` preserving the six branch/Weierstrass points. The kernel of this descent is the hyperelliptic involution, of order 2.

For an ambient realization inducing the order-3 principal action `b3`, the induced action on the hyperelliptic base is nontrivial of order 3 (the possible central sign/hyperelliptic factor does not change the induced action on `P^1`). A nonidentity order-3 Möbius transformation has at most two fixed points. On an invariant set of six branch points every orbit has size 1 or 3, so the number of fixed branch points is congruent to 6 modulo 3. The only value at most 2 is zero. Therefore the six branch points split as exactly two 3-cycles.

This leaf does not need an absolute labeling of those two 3-cycles. It exhausts every permutation of the six source-locked Weierstrass representatives having cycle type `(3,3)`.

## Exact finite obstruction

There are exactly 40 permutations of six labels with cycle type `(3,3)`. For each of the four H-deck translates, the diagnostic tests all 40 against invariance of the six-entry Picard pairing profile.

Result:

```
H member   second-factor profile       preserving (3,3) permutations
id         11,22,16,11,28,22           0
u          11,22,16,11,28,22           0
v          11,22,16,11,28,22           0
uv         11,22,16,11,28,22           0
```

Thus there is no order-3 permutation of the required branch-cycle type that can preserve this retained ambient cusp profile, even after allowing the full H-deck orbit of the V6 class.

Equivalently, the following **specific** mechanism is ruled out:

```
DIRECT_AMBIENT_B3_CUSP_PROFILE_EQUIVARIANCE_FOR_V6_H_ORBIT
```

where `b3` is realized by an ambient/retained-Picard symmetry that permutes the six second-factor boundary curves through their source-locked Bolza Weierstrass ids and carries the V6 class into its H-deck orbit.

## Firewall

This is a bounded negative result only. In particular it does **not** prove any of the following:

- `[T,b3] != 0` for the hypothetical actual correspondence;
- nonexistence of an intrinsic automorphism of a hypothetical carrier `Y` that does not extend to the retained ambient Picard action;
- nonexistence of an exact divisor/correspondence identity proving `[T,b3]=0` by another route;
- `Q(T) != 602` unconditionally;
- exclusion of `O=210`;
- authorization of `O>=212` work;
- effectivity, FULL178, receiver, route, theorem, endpoint, or perfect-cuboid credit.

The Stage32 controller is unchanged. `O210/Q602` remain OPEN and `O212+` remains blocked.

Re-entry after this leaf requires genuinely new information outside this ambient cusp-profile mechanism, for example an intrinsic carrier automorphism with an exact action on `f1,f2`, or an exact divisor/correspondence commutator identity.