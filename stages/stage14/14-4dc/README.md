# Stage14-4dc

Stage14-4dc consumes merged `4db`, `s7-44`, `s7-42`, `s7-29`, and the X13 square-root theorem on latest main.

The current theorem is

```text
V(B) << B^(1/2+o(1)).
```

Possible equality packets satisfy

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
H=K=B^o(1),
C=J=C_Cayley at fixed-power scale.
```

Merged s7-44 reduces the obstruction to two primitive full-core root lines.  Stage14-4dc reparameterizes the first residual and Gaussian agreement pair by

```text
a=g*a0,
b=g*b0,
P=a0*U,
Q=b0*V.
```

Using `oddpart(ab)=oddpart(u_res)`, `u_res<=B^(1/2-2phi+o(1))`, and `UV=B^(2phi+o(1))`,

```text
P*Q<=B^(1/2+o(1)).
```

The s7-29 common-core equation becomes coefficient-free:

```text
C0 | P^2+Q^2,
C0=C/B^o(1).
```

After the endpoint-small gcd peel, `(P,Q)` is primitive and the determinant lemma gives

```text
#(P,Q)<=B^(1/2-chi+o(1)).
```

A fixed `(P,Q)` has only divisor-many splittings `P=a0U`, `Q=b0V`.  Merged s7-42 then gives only `B^o(1)` compatible single columns, and X13 gives only `B^o(1)` post-column reciprocal completions.  Thus the full square-root ledger is equivalently

```text
C:                     chi,
Gaussian product line: 1/2-chi,
physical completion:   0,
total:                 1/2.
```

The obvious cross-resultant shortcut is impossible.  The endpoint column has slope root `sigma^2=1`, while the Gaussian product line has `rho^2=-1`.  Since

```text
Res(t^2+1,t^2-1)=4,
```

on the odd full good core

```text
gcd(C0,P*B_z-Q*A_z)=1,
gcd(C0,P*B_z+Q*A_z)=1.
```

So neither rational cross determinant gives a fresh copy of `C`.  Quadratic Gaussian cross norms divisible by `C` are formal consequences of the two already charged root equations and cannot be used as a second determinant modulus.

No strict sub-square-root exponent is proved.  The minimal receiver becomes

```text
SquareRootThetaQuarterGloballyOddPrimitiveFullCoreGaussianProductRootLinePhysicalCompletionEnergy
```

and the merged s7-44 H gate is promoted to the mainline with the refined target

```text
SquareRootThetaQuarterGloballyOddPrimitiveFullCoreGaussianProductRootLinePhysicalCompletionEnergyPowerSaving.
```

Required output:

```text
sum_C I_C^phys << B^(1/2-delta+o(1))
```

for some fixed `delta>0`, uniformly over `5/24<=phi<=1/4`, retaining all physical masks and without reusing `C` as a second spacing modulus.

Fixed-U `t/tH` results are not cross-promoted.

Next: `Stage14-4dd_after_H`.
