# Stage35-EX Goal4AU source lock — three-direction marked Kummer gcd allocation

Scope: continue the single marked-Kummer route sharpened by Goal4AT. Audited Stage35-EX authority remains V74 / Goal4AK. Goal4AU is a provisional exact prime-allocation/cross-face coupling leaf stacked on exact-green Goal4AT. It does not promote Goal4AT or any later stacked leaf to hostile-audited authority and does not prove E1, Stage35, or any Perfect Cuboid theorem.

## Parent and source dictionary

For a positive primitive endpoint write

```text
A = x*y*a,
B = x*z*b,
C = y*z*c,
```

with

```text
x=gcd(A,B), y=gcd(A,C), z=gcd(B,C),
gcd(x,y)=gcd(x,z)=gcd(y,z)=1,
gcd(a,b)=gcd(a,c)=gcd(b,c)=1.
```

The three reduced primitive Pythagorean faces are

```text
r_AB^2 = (y*a)^2 + (z*b)^2,   D_AB=x*r_AB,
r_AC^2 = (x*a)^2 + (z*c)^2,   D_AC=y*r_AC,
r_BC^2 = (x*b)^2 + (y*c)^2,   D_BC=z*r_BC.
```

Each reduced leg pair has opposite parity, so all three `r_AB,r_AC,r_BC` are odd.

Goal4AT applied in the `A`-direction gives

```text
G_A = gcd(D_AB*D_AC-B*C, D_AB*D_AC+B*C),
d_A = [(2*B*C)/G_A].
```

Because the endpoint equations are symmetric, the same exact theorem may be applied to the two relabelings:

```text
G_B = gcd(D_AB*D_BC-A*C, D_AB*D_BC+A*C),
d_B = [(2*A*C)/G_B],

G_C = gcd(D_AC*D_BC-A*B, D_AC*D_BC+A*B),
d_C = [(2*A*B)/G_C].
```

These are three source-marked Kummer squareclasses on three relabeled Goal4L receivers. They are not asserted to be points on one elliptic curve.

## Strip the pair-gcd factors

Define

```text
H_A = gcd(r_AB*r_AC-z^2*b*c, r_AB*r_AC+z^2*b*c),
H_B = gcd(r_AB*r_BC-y^2*a*c, r_AB*r_BC+y^2*a*c),
H_C = gcd(r_AC*r_BC-x^2*a*b, r_AC*r_BC+x^2*a*b).
```

Then exactly

```text
G_A=x*y*H_A,
G_B=x*z*H_B,
G_C=y*z*H_C.                                      (AU-1)
```

The three inner complementary products are squares:

```text
(r_AB*r_AC-z^2*b*c)*(r_AB*r_AC+z^2*b*c) = (a*W)^2,
(r_AB*r_BC-y^2*a*c)*(r_AB*r_BC+y^2*a*c) = (b*W)^2,
(r_AC*r_BC-x^2*a*b)*(r_AC*r_BC+x^2*a*b) = (c*W)^2. (AU-2)
```

## Odd-prime allocation

Put

```text
h_a = gcd(a,r_BC),
h_b = gcd(b,r_AC),
h_c = gcd(c,r_AB).
```

All three are odd because the reduced hypotenuses are odd.

For `H_A`, let `ell` be odd.

- If `ell|z`, primitivity of both reduced `AB` and `AC` leg pairs makes `r_AB` and `r_AC` `ell`-adic units, so `ell` does not divide `H_A`.
- Since `H_A | 2*z^2*b*c`, every odd prime of `H_A` therefore divides `b*c`.
- If `ell|b`, then `r_AB` is an `ell`-adic unit, `ell` does not divide `z*c`, and
  `v_ell(H_A)=min(v_ell(b),v_ell(r_AC))`.
- If `ell|c`, symmetrically
  `v_ell(H_A)=min(v_ell(c),v_ell(r_AB))`.

Because `gcd(b,c)=1`, these channels are disjoint. Hence the complete odd part is

```text
(H_A)_odd = h_b*h_c.
```

Cyclically,

```text
(H_B)_odd = h_a*h_c,
(H_C)_odd = h_a*h_b.                                (AU-3)
```

This is an exact prime-allocation theorem, not a fixed-prime-support theorem: `h_a,h_b,h_c` remain live source-dependent reservoirs.

## Exact 2-adic factors

Since every reduced hypotenuse is odd, write

```text
epsilon_A = 2 if z*b*c is odd, else 1,
epsilon_B = 2 if y*a*c is odd, else 1,
epsilon_C = 2 if x*a*b is odd, else 1.
```

Indeed, in `gcd(R-T,R+T)` with `R` odd, the gcd is odd when `T` is even and has exact 2-adic valuation one when `T` is odd.

Therefore

```text
H_A = epsilon_A*h_b*h_c,
H_B = epsilon_B*h_a*h_c,
H_C = epsilon_C*h_a*h_b.                            (AU-4)
```

The retained endpoint parity dictionary implies **exactly one** of
`epsilon_A,epsilon_B,epsilon_C` equals `2`.

- If `A` is odd, then `x,y,a` are odd, `z` is even, and `b,c` have opposite parity. Thus `epsilon_A=1` and exactly one of `epsilon_B,epsilon_C` is `2`.
- If `B` is odd, then `x,z,b` are odd, `y` is even, and `a,c` have opposite parity. Thus `epsilon_B=1` and exactly one of `epsilon_A,epsilon_C` is `2`.
- If `C` is odd, then `y,z,c` are odd, `x` is even, and `a,b` have opposite parity. Thus `epsilon_C=1` and exactly one of `epsilon_A,epsilon_B` is `2`.

Hence

```text
epsilon_A*epsilon_B*epsilon_C = 2.                  (AU-5)
```

Define the positive integer Goal4AT representatives

```text
K_A = (2*B*C)/G_A,
K_B = (2*A*C)/G_B,
K_C = (2*A*B)/G_C,
```

and stripped source integers

```text
a0=a/h_a, b0=b/h_b, c0=c/h_c,
k_A=2/epsilon_A, k_B=2/epsilon_B, k_C=2/epsilon_C.
```

Here every `k_i` is exactly `1` or `2`. Using `(AU-1)` and `(AU-4)` gives the **literal integer factorizations**

```text
K_A = z^2*k_A*b0*c0,
K_B = y^2*k_B*a0*c0,
K_C = x^2*k_C*a0*b0.                                (AU-6)
```

Since exactly one `epsilon_i` is `2`, exactly two `k_i` equal `2` and one equals `1`, so

```text
k_A*k_B*k_C=4
```

and therefore

```text
K_A*K_B*K_C = (2*x*y*z*a0*b0*c0)^2.                (AU-7)
```

Thus the cross-face relation is not merely an abstract squareclass product: the three canonical positive Goal4AT representatives have an explicit source-derived square product.

## Three-reservoir marked Kummer graph

Define source quotient squareclasses

```text
alpha = [a/h_a],
beta  = [b/h_b],
gamma = [c/h_c],
```

and

```text
kappa_A = [2/epsilon_A],
kappa_B = [2/epsilon_B],
kappa_C = [2/epsilon_C].
```

Using Goal4AT and `(AU-1)`--`(AU-4)`,

```text
d_A = kappa_A*beta*gamma,
d_B = kappa_B*alpha*gamma,
d_C = kappa_C*alpha*beta.                            (AU-KUMMER)
```

Thus the three marked classes are a complete three-reservoir squareclass graph. The linear part has matrix

```text
0 1 1
1 0 1
1 1 0
```

over `F_2`, of rank two with diagonal kernel `(1,1,1)`. Goal4AU therefore does not recover the three live source reservoirs individually.

Because exactly one `epsilon_i` is `2`, exactly two `kappa_i` equal `[2]` and one equals `[1]`. Consequently

```text
d_A*d_B*d_C = 1 in Q*/Q*^2.                         (AU-CROSS)
```

Equivalently, any two of the source-marked Kummer classes determine the third.

A direct check is also

```text
[G_A*G_B*G_C]=[2],
[(2BC/G_A)*(2AC/G_B)*(2AB/G_C)]=1.
```

## Relation to Goal4J

Goal4J found only the separate congruent-number twist shadow

```text
[N_AB]*[N_AC]*[N_BC]=[2]
```

and explicitly had no source-locked shared covering, inter-twist isogeny, Cassels-pairing identity, or common Selmer complex.

Goal4AU is not a retroactive repair of Goal4J and does not claim such a common cover. It adds a different exact datum: the **specific source-marked residual Kummer classes** on the three relabeled Goal4L receivers satisfy `(AU-CROSS)` after the exact gcd/hypotenuse stripping above.

The abstract rank-two matrix is still noninjective, so `(AU-CROSS)` alone gives no branch exclusion and does not force any `d_i=1`. For example, three nontrivial squareclasses can satisfy a product-one relation.

## Route verdict

```text
GOAL4AU_THREE_DIRECTION_GCD_ALLOCATION=true
GOAL4AU_THREE_RESERVOIR_KUMMER_GRAPH=true
GOAL4AU_CROSS_FACE_MARKED_KUMMER_PRODUCT_ONE=true
GOAL4AU_NEW_BRANCH_PRUNING=false
GOAL4AU_COMMON_2COVER_CONSTRUCTED=false
GOAL4AU_CASSELS_PAIRING_IDENTITY=false

D_I_TRIVIAL_FOR_ANY_DIRECTION_PROVED=false
FIXED_FINITE_GLOBAL_SQUARECLASS_FAMILY_PROVED=false
TWO_DIVISIBILITY_PROVED=false
INFINITE_DESCENT_PROVED=false
```

The exact next leaf is

```text
35EX-35_GOAL4AV_CROSS_FACE_MARKED_KUMMER_COMMON_COVER_PREFLIGHT
```

with the bounded question:

```text
does d_A*d_B*d_C=1 lift from a squareclass identity to a source-derived
common 2-cover / fiber-product / Cassels-pairing constraint that excludes
the physical marked triple, or is the rank-two relation only another
non-pruning shadow?
```

If no source-derived common cover or pairing identity is constructed, freeze this coupling as non-pruning rather than treating product-one as an obstruction.

## Credit firewall

Certified provisionally only:

- the exact factorizations `(AU-1)` and `(AU-2)`;
- the complete odd allocation `(AU-3)`;
- the exact 2-adic factors `(AU-4)` and one-even-factor theorem `(AU-5)`;
- the literal representative factorization `(AU-6)` and exact square product `(AU-7)`;
- the three-reservoir marked Kummer graph `(AU-KUMMER)`;
- the cross-face source-marked identity `d_A*d_B*d_C=1`.

Not certified:

- triviality or nontriviality of any global `d_i`;
- a fixed finite global squareclass family;
- a common 2-cover, common Selmer complex, or Cassels-pairing obstruction;
- 2-divisibility or infinite descent;
- any new Brauer-Manin obstruction;
- E1, R29-PESCH-E1, Stage35, endpoint, or Perfect Cuboid existence/nonexistence closure.
