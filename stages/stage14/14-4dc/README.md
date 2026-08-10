# Stage14-4dc

Stage14-4dc consumes merged `Stage14-4db` and the newly merged `Stage14-s7-44` square-root determinant no-go on latest main.

The entering theorem is already

```text
V(B) << B^(1/2+o(1)).
```

The possible equality band has been reduced to

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
H=K=B^o(1),
C=J=C_Cayley at fixed-power scale.
```

Merged s7-44 writes the obstruction as a Cartesian product of two primitive root lines over the same full core `C`:

```text
(a_0 U/(b_0 V))^2 == -1 (mod C/B^o(1)),
(A_z/B_z)^2       == +1 (mod C/B^o(1)).
```

Stage14-4dc sharpens the coefficient space before the requested average theorem.

Put

```text
a=c_x^+,
b=c_x^-,
g=gcd(a,b),
a=g*a_0,
b=g*b_0,

P=a_0*U,
Q=b_0*V.
```

Merged s7-27 gives

```text
oddpart(a*b)=oddpart(u_res),
```

and merged s7-42 gives on the theta-quarter square-root band

```text
u_res exponent = A(phi):=1/2-2phi,
first residual <-> single reduced column
with B^o(1) fibers in both directions.
```

Since

```text
U*V=B^(2phi+o(1)),
a_0*b_0<=B^(A(phi)+o(1)),
```

we have

```text
P*Q<=B^(1/2+o(1)).
```

The s7-29 Gaussian congruence becomes coefficient-free:

```text
C_0 | P^2+Q^2,
C_0=C/B^o(1).
```

After the endpoint-small gcd peel already present in s7-29/s7-44, `(P,Q)` is primitive up to `B^o(1)`.  For fixed `C_0` and Gaussian root orientation, determinant spacing therefore gives

```text
#(P,Q) <= B^(1/2-chi+o(1)).
```

Conversely a fixed product pair `(P,Q)` has only divisor-many splittings

```text
P=a_0 U,
Q=b_0 V,
```

so this single product-pair count already includes both the first residual support and the primitive `(U,V)` support.  Merged s7-42 then makes the endpoint column a physical compatibility filter with only `B^o(1)` fiber after the split is fixed.

Thus the s7-44 dual-root-line ledger is compressed to

```text
C choice:                    chi,
Gaussian product root line:  1/2-chi,
physical endpoint completion: 0,
----------------------------------
total:                       1/2.
```

No exponent improvement follows from the reparameterization, but the minimal analytic receiver is smaller.

There is also an exact resultant no-go.  On every odd prime `p|C_0`, write

```text
P/Q == rho,
rho^2 == -1,
A_z/B_z == sigma,
sigma^2 == 1.
```

Since

```text
Res(t^2+1,t^2-1)=4,
```

we have for odd `C_0`

```text
gcd(C_0,P*B_z-Q*A_z)=1,
gcd(C_0,P*B_z+Q*A_z)=1.
```

So the obvious rational cross determinant is not a second multiple of `C`; it is a unit on the full good core.  Gaussian cross norms divisible by `C` are algebraic consequences of the two already charged root equations and cannot be used as a fresh spacing modulus.

The refined receiver is

```text
SquareRootThetaQuarterGloballyOddPrimitiveFullCoreGaussianProductRootLinePhysicalCompletionEnergy
```

and a strict sub-square-root theorem now requires a genuine average estimate

```text
sum_C I_C^phys << B^(1/2-delta+o(1))
```

for some fixed `delta>0`, uniformly over `5/24<=phi<=1/4`.

Accordingly Stage14-4dc promotes the merged s7-44 H gate to the mainline and narrows its target to

```text
SquareRootThetaQuarterGloballyOddPrimitiveFullCoreGaussianProductRootLinePhysicalCompletionEnergyPowerSaving.
```

No fixed-U t/tH result is cross-promoted.

Next: `Stage14-4dd_after_H`.
