# Stage35-EX Goal4AV source lock — cross-face marked Kummer common-cover preflight

Scope: consume exact-green Goal4AU and test the bounded question left there: whether the exact source-marked relation `d_A*d_B*d_C=1` produces a genuine common 2-cover / fiber-product / Cassels-pairing obstruction for the physical marked triple. Audited Stage35-EX authority remains V74 / Goal4AK. Goal4AV is provisional and grants no hostile-audit, E1, Stage35, endpoint, or Perfect Cuboid credit.

## Exact-green parent

Goal4AU is exact-head green at

```text
head = 2e9972a64cfa31d2116ea70a9728a64cb083b5e3
aggregate = 34292248229
verify-stage35-ex-current = 102282485273
```

Goal4AU gives positive integer representatives

```text
K_A = (2*B*C)/G_A = z^2*k_A*b0*c0,
K_B = (2*A*C)/G_B = y^2*k_B*a0*c0,
K_C = (2*A*B)/G_C = x^2*k_C*a0*b0,
```

with

```text
k_A*k_B*k_C = 4,
S = 2*x*y*z*a0*b0*c0,
K_A*K_B*K_C = S^2,                                  (AV-1)
[d_A]=[K_A], [d_B]=[K_B], [d_C]=[K_C],
d_A*d_B*d_C=1 in Q*/Q*^2.                           (AV-2)
```

The three marked points lie on three cyclically relabeled Goal4L curves; Goal4AU does not identify those elliptic curves or their Selmer groups.

## The common coefficient group that really exists

Goal4AS put each directional physical point on the marked Kummer line

```text
delta_i(P_i)=(d_i,d_i,1).
```

For a split rational-2-torsion curve, the ordered Kummer coordinates identify `H^1(Q,E_i[2])` with two copies of `Q*/Q*^2`. The marked diagonal line `(d,d,1)` is therefore a copy of

```text
H^1(Q,mu_2) = Q*/Q*^2.
```

For each direction choose only this source-marked coefficient extraction and write

```text
chi_A=[K_A], chi_B=[K_B], chi_C=[K_C] in H^1(Q,mu_2).
```

This uses the same **coefficient group** `mu_2`, but does not identify the three target modules `E_A[2],E_B[2],E_C[2]`, the three curves, or their local Selmer conditions.

Then `(AV-2)` is exactly

```text
chi_A + chi_B + chi_C = 0 in H^1(Q,mu_2).            (AV-3)
```

Thus the contracted product of the three quadratic coefficient torsors is trivial. This is the strongest common cohomological statement supplied by Goal4AU alone.

## Literal fiber-product package

Define the three quadratic coefficient torsors over `Spec(Q)`

```text
T_A: t_A^2=K_A,
T_B: t_B^2=K_B,
T_C: t_C^2=K_C.
```

Because all `K_i` are positive nonzero integers on the retained physical population, their coordinate functions are invertible in these finite etale algebras.

The full product has coordinate ring

```text
Q[t_A,t_B,t_C]/(t_A^2-K_A,t_B^2-K_B,t_C^2-K_C).
```

By `(AV-1)`,

```text
(t_A*t_B*t_C/S)^2=1.
```

Hence the product splits into two sign components. On the `+` component

```text
t_A*t_B*t_C=S,                                      (AV-4)
```

and `t_C=S/(t_A*t_B)`, so the component is exactly the rank-at-most-four biquadratic package

```text
T_AB: t_A^2=K_A, t_B^2=K_B,                         (AV-5)
```

with the third square root reconstructed by `(AV-4)`. The `-` component is the same package with the opposite sign.

Therefore Goal4AU **does** lift to an exact common coefficient-field statement:

```text
Q(sqrt(K_A),sqrt(K_B),sqrt(K_C))
  = Q(sqrt(K_A),sqrt(K_B)),
```

so its degree is at most four rather than eight. This is a genuine source-derived biquadratic coupling.

## Why this is not a common endpoint 2-cover obstruction

The crucial distinction is between

```text
(a) a coefficient torsor over Spec(Q),
(b) the multiplication-by-2 fiber over a rational point on an elliptic curve.
```

A rational physical marked point `P_i in E_i(Q)` is allowed to have nonzero Kummer class `delta_i(P_i)`. The fiber `[2]^{-1}(P_i)` has a rational point exactly when the full Kummer class is trivial; Goal4AS and Goal4AU never asserted this.

For the coefficient package `(AV-5)`, a rational point requires

```text
K_A in Q*2 and K_B in Q*2,
```

which then forces `K_C in Q*2` by `(AV-1)`. Equivalently,

```text
T_AB(Q) != empty  iff  d_A=d_B=d_C=1.               (AV-6)
```

But the endpoint hypotheses do not require `T_AB(Q) != empty`. They require only the original marked points `P_A,P_B,P_C`, which already exist by construction. Therefore replacing `(AV-3)` by the demand for a rational section of `(AV-5)` would add precisely the unproved conclusion that all residual Kummer classes vanish.

The non-pruning nature is formal: for arbitrary squareclasses `u,v in Q*/Q*^2`,

```text
(u,v,u*v)
```

satisfies product one. Thus `(AV-3)` leaves two independent `H^1(Q,mu_2)` parameters and does not force any coordinate to be trivial.

## Why no family-level common 2-cover has been constructed

The retained literal representatives `K_i` are arithmetic formulas involving

```text
h_a=gcd(a,r_BC), h_b=gcd(b,r_AC), h_c=gcd(c,r_AB)
```

and parity-selected `epsilon_i`. These are exact integer-point data, not rational functions supplied on the ambient algebraic endpoint family. Goal4AU therefore gives a pointwise arithmetic square product `(AV-1)`, not a source-locked function-field square identity defining one algebraic cover of the entire endpoint family.

One could instead start from the rational-function representatives before gcd stripping, but no exact identity in the retained source says that their product is a square in the endpoint function field. Goal4AV does not invent such an identity.

Accordingly:

```text
COMMON_COEFFICIENT_BIQUADRATIC_PACKAGE=true
COMMON_ENDPOINT_FAMILY_2COVER_CONSTRUCTED=false
PHYSICAL_ENDPOINT_REQUIRES_RATIONAL_SECTION_OF_T_AB=false
```

## Cassels-pairing boundary

A Cassels/Cassels-Tate pairing is attached to Selmer data for a fixed elliptic curve (or to two Selmer structures connected by an explicit transport theorem). Here the three Goal4L curves are cyclic relabelings with different parameters, and the retained source contains no inter-curve isogeny, no identification of the three local Kummer images, and no common Selmer complex.

The common coefficient identity `(AV-3)` therefore cannot be promoted to a Cassels-pairing identity. Any future revival of this route must first construct an explicit source-compatible transport

```text
E_A[2] <-> E_B[2] <-> E_C[2]
```

or a common covering complex together with its local conditions. Equality of the abstract coefficient group `mu_2` is not such a transport.

Hence

```text
COMMON_SELMER_COMPLEX_CONSTRUCTED=false
CASSELS_PAIRING_IDENTITY_CONSTRUCTED=false
CASSELS_PAIRING_OBSTRUCTION_OBTAINED=false
```

## Route verdict

Goal4AV sharpens Goal4AU in one positive and one negative direction:

1. positive: the three residual classes admit an exact source-derived biquadratic coefficient package of degree at most four;
2. negative: this package is only the contracted-product realization of the rank-two relation and imposes no rational-lift condition supplied by the endpoint.

Therefore the concrete `NEW_COMMON_SELMER_OR_CASSELS_COUPLING` route generated at Goal4AS is now classified, for this product-one mechanism, as

```text
BLOCKED_NONPRUNING_COEFFICIENT_TORSOR_SHADOW.
```

This does not prove that every conceivable future cross-curve Selmer/Cassels construction is impossible. It means the current exact datum `d_A*d_B*d_C=1` cannot be credited as one without a genuinely new transport object.

Certified provisional conclusions:

```text
GOAL4AV_COMMON_MU2_COEFFICIENT_COUPLING=true
GOAL4AV_BIQUADRATIC_DEGREE_AT_MOST_FOUR=true
GOAL4AV_THIRD_SQRT_RECONSTRUCTED_FROM_FIRST_TWO=true
GOAL4AV_COMMON_ENDPOINT_2COVER_CONSTRUCTED=false
GOAL4AV_COMMON_SELMER_COMPLEX_CONSTRUCTED=false
GOAL4AV_CASSELS_PAIRING_IDENTITY=false
GOAL4AV_NEW_BRANCH_PRUNING=false
GOAL4AV_ANY_D_I_TRIVIAL_FORCED=false
```

## Next exact leaf

With this concrete coupling frozen as non-pruning, switch to the next blind-audit candidate that already has an exact physical marked point and a quantitative receiver:

```text
35EX-35_GOAL4AW_MARKED_ELLIPTIC_HEIGHT_LOWER_VS_GOAL4M_UPPER_PREFLIGHT
```

Bounded question:

```text
on the exact physical Goal4L family, can a source-locked explicit lower bound
for the canonical height of the marked non-torsion point be compared against
the retained Goal4M O(log B) endpoint upper window with constants strong
enough to eliminate all sufficiently large physical endpoints?
```

If the available lower-bound constants or parameter-height adapters do not beat the Goal4M upper window, freeze that quantitative route rather than claiming eventual zero.

## Credit firewall

Not certified:

- `d_i=1` or `d_i!=1` for any global physical direction;
- rational points on the coefficient torsors `T_i` or `T_AB`;
- a family-level common 2-cover;
- a common Selmer complex or Cassels-pairing obstruction;
- 2-divisibility or infinite descent;
- a fixed finite global squareclass family;
- any new Brauer-Manin obstruction;
- E1, R29-PESCH-E1, Stage35, endpoint, or Perfect Cuboid existence/nonexistence closure.
