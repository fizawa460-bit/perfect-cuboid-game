# Stage35-EX Goal4BQ source lock — y=0 boundary escape and exact 2-primary conductor depth

Scope: continue the Goal4BP-selected boundary-escape route. This leaf isolates an explicit increasing finite visible-character packet at the 2-adic place and computes exactly how deeply the source-marked local point must approach the fixed rational boundary anchor `y=0` in order to reproduce the anchor evaluations.

This is a local/adelic theorem. It does **not** assert that a rational endpoint realizes these local packets.

## 1. Fixed rational boundary anchor and 2-adic slice

Use the Goal4BB / 35EX-22 rational anchor

```text
P*:
x0=272/225,
y=0,
p0=353/225,
q=1,
z=x0,
w=p0.
```

It satisfies the affine surface equations

```text
p^2=1+x^2,
q^2=1+y^2,
z^2=x^2+y^2,
w^2=1+x^2+y^2,
```

and lies outside the selected open `U_PC` only because `y=0`.

At `2`, fix

```text
x=x0,
p=p0
```

and take a nonzero `y in Q_2` with

```text
m=v2(y)>=6.                                           (BQ-m)
```

Choose the square-root branches reducing to the anchor:

```text
q^2=1+y^2,          q near 1,
z^2=x0^2+y^2,       z near x0,
w^2=p0^2+y^2,       w near p0.                       (BQ-slice)
```

These roots exist for `m>=6`: `v2(x0)=4`, so `v2(y/x0)>=2` and `1+(y/x0)^2 == 1 mod 16`; similarly `1+y^2` and `1+(y/p0)^2` are 2-adic unit squares in the indicated branches.

## 2. Exact depth of the visible unit q+y

From

```text
(q-1)(q+1)=y^2
```

and the chosen branch `q near 1`, one has `v2(q+1)=1`. Therefore

```text
v2(q-1)=2*m-1.                                       (BQ-qminus1)
```

Since `m>=6`, the two summands in

```text
(q+y)-1=(q-1)+y
```

have unequal valuations `2*m-1` and `m`. Hence exactly

```text
v2((q+y)-1)=m.                                       (BQ-visible-depth)
```

This equality, not merely an inequality, is the boundary-depth invariant used below.

## 3. Increasing finite global character packets

For every `n>=6`, let

```text
X_n = Hom((Z/2^n Z)^*, Q/Z),                         (BQ-Xn)
```

viewed as the finite family of global Dirichlet/Artin characters of 2-power conductor dividing `2^n`. Pair each character with the Goal4AQ visible unit

```text
u_2=q+y
```

to obtain the finite Brauer packet

```text
F_n={ beta(chi,q+y) : chi in X_n }.                  (BQ-Fn)
```

At the anchor `q+y=1`, every local 2-adic evaluation is trivial.

Characters of the finite group `(Z/2^n Z)^*` separate its points, so the intersection of all their kernels is the identity class. Therefore for a 2-adic unit `u`,

```text
chi(u)=1 for every chi in X_n
iff u == 1 mod 2^n.                                  (BQ-separation)
```

Combining `(BQ-visible-depth)` and `(BQ-separation)` gives the exact equivalence on the fixed source slice:

```text
all F_n evaluations at 2 match the anchor
iff v2(q+y-1)>=n
iff m=v2(y)>=n.                                      (BQ-depth-theorem)
```

Thus the minimal boundary depth is exactly

```text
D(n)=n   for n>=6.                                   (BQ-Dn)
```

The bound is sharp: taking any `m=n` gives a valid local slice and meets, but does not exceed, the required congruence depth.

## 4. Conditional rational-height consequence

If a nonzero rational number `y=a/b` is in lowest terms and

```text
v2(y)>=n,
```

then `b` is odd and `2^n | a`. Consequently the naive rational height satisfies

```text
H(y)=max(|a|,|b|) >= 2^n.                            (BQ-height)
```

Hence any **rational realization of this fixed-x packet** would have exponentially growing coordinate height as the character conductor grows.

But no retained Stage35-EX theorem produces such a rational realization. Goal4BB supplies adelic points, not rational points; Goal4AQ says the full infinite character layer is endpoint-equivalent, not that each finite packet has a rational point. Strong approximation or a rational approximation theorem on `U_PC` with this fixed local slice is not available and would itself be a major new theorem.

Therefore `(BQ-height)` cannot be charged against Goal4M or any endpoint counting bound.

## 5. Compactness firewall

The calculation proves an explicit escape to the removed divisor `y=0` for this chosen finite character filtration. It does not justify a compactness argument on `U_PC(A_Q)`:

- the open condition removes `y=0`;
- the sequence with `v2(y)->infinity` converges to the removed boundary point in the ambient affine/projective local space;
- finite-intersection nonemptiness inside a noncompact punctured neighborhood does not imply a point in the full intersection.

Thus the finite/full Brauer gap from Goal4BB/AQ is concretely compatible with boundary escape.

## 6. Verdict

Certified provisionally:

```text
FIXED_Y_ZERO_BOUNDARY_ANCHOR=true;
FIXED_X_2ADIC_SLICE_EXISTS_FOR_V2_Y_GE_6=true;
V2_Q_PLUS_Y_MINUS_1_EQUALS_V2_Y=true;
FINITE_2PRIMARY_VISIBLE_CHARACTER_PACKET_EXPLICIT=true;
CHARACTER_PACKET_ANCHOR_MATCH_IFF_V2_Y_GE_N=true;
BOUNDARY_DEPTH_D_N_EQUALS_N=true;
RATIONAL_REALIZATION_HEIGHT_LOWER_BOUND_2POW_N=true;
RATIONAL_REALIZATION_PROVED=false;
GLOBAL_ENDPOINT_HEIGHT_ADAPTER_OBTAINED=false;
COMPACTNESS_CLOSURE_CLAIMED=false;
BRANCH_PRUNING=false.
```

The selected route therefore yields a real source-fixed escape invariant but does not convert finite adelic nonobstruction into a global contradiction.

## 7. Next leaf

Return to the distinct Goal4BP backup rather than iterating witness-depth refinements:

```text
35EX-35_GOAL4BR_DERIVED_FOURTH_SQUARE_DEFECT_SQUARECLASS_PREFLIGHT
```

Question: analyze the source-fixed derived fourth-square defect

```text
Q_D=(x*a*b)^2+(y*a*c)^2+(z*b*c)^2
```

using the exact completion identity and primitive parity/gcd dictionary. First determine its squarefree support and whether S34-W01 can actually be triggered; do not assume a finite squareclass family.

No merge. No hostile-audit credit. MAIN-STATE remains V74 / Goal4AK.
