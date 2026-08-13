# Stage14-s7-118 — all three active nonaligned realizations host the X13 column on one fixed square class

## Status

`COMPLETE_NONALIGNED_THREE_BRANCH_FIXED_SQUARECLASS_COLUMN_NORMALIZATION`

Consumes batch-local `Stage14-s7-117`, merged `Stage14-s7-100/101`, merged `Stage14-s7-111/112`, and merged `Stage14-X13`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

Throughout, distinguish the frozen X13 endpoint-small labels `r_ep,s_ep` from the scalar variable of the s realization.

## 1. Fixed-E primitive endpoint

Freeze

```text
E=E0,
u=r0,
v=t,
gcd(r0,t)=1,
```

with `r0=B^o(1)` already frozen. Merged s7-101 gives

```text
|Xr|=alpha*E0*r0^2=:A_end,
|Yr|=beta*E0*t^2=:B_end*t^2,
h=d0*E0*r0*t.
```

Hence the X13 column parameter satisfies exactly

```text
M=4*r_ep*s_ep*|Xr|*|Yr|*epsilon_x*epsilon_k
 =M_end,0*t^2,
```

where `M_end,0` is fixed on the packet.

## 2. Polynomial-E fixed primitive product

Freeze `(m0,u0,v0)` as in s7-100 and let `E` move. Then

```text
|Xr|=(alpha*u0^2)E,
|Yr|=(beta*v0^2)E,
h=(d0*m0)E,
```

so

```text
M=M_fix,0*E^2
```

for one fixed packet coefficient `M_fix,0`.

## 3. Polynomial-E polynomial-product fibered realization

Here

```text
n=E*u*v=E*m,
|Xr|=alpha*E*u^2,
|Yr|=beta*E*v^2.
```

Since `m=uv`,

```text
|Xr|*|Yr|=alpha*beta*(E*m)^2=alpha*beta*n^2,
```

and therefore

```text
M=M_pair,0*n^2.
```

The reverse-column square class depends only on `n=Em`. This does **not** collapse the charged outer pair `(E,m)` to `n`: the precompletion Boolean and branch labels may still depend on `E,u,v` separately. Merged Work-byX37 only permits the already-charged `B^o(1)` multiplication-fiber statement.

## 4. Common square-class hosting statement

For the three active realizations define the scalar

```text
z=t     on the fixed-E endpoint branch,
z=E     on the fixed-product branch,
z=n=Em  on the polynomial pair branch.
```

Then each branch has

```text
M=M0*z^2,
|Xr|*|Yr|=P0*z^2
```

with branch-dependent coefficients `M0,P0` frozen on the packet. The agreement pair `(U,V)` and all finite/two-primary decorations remain frozen as before.

Thus the generic extension Boolean of s7-112 is not a generic moving-column problem on these branches: it is reverse reconstruction along one fixed square class.

```text
S_ENDPOINT_X13_COLUMN_FIXED_SQUARECLASS=true
S_FIXED_PRODUCT_X13_COLUMN_FIXED_SQUARECLASS=true
S_POLYNOMIAL_PAIR_X13_COLUMN_FIXED_SQUARECLASS_IN_n=true
S_NONALIGNED_THREE_BRANCH_SQUARECLASS_HOSTING_PROVED=true
POLYNOMIAL_PAIR_OUTER_MEASURE_COLLAPSED_TO_n=false
```

## 5. H and receiver

This algebraic square-class normalization alone gives no support density and no existence theorem. The extension witness remains existential. The next stage opens the exact X13 factor-pair conditions on this square-class host before deciding whether any new theorem audit is justified.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_118_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-119
```

## Boundary

```text
STAGE14_S7_118=COMPLETE_NONALIGNED_THREE_BRANCH_FIXED_SQUARECLASS_COLUMN_NORMALIZATION
S_NONALIGNED_THREE_BRANCH_SQUARECLASS_HOSTING_PROVED=true
S_POLYNOMIAL_PAIR_X13_COLUMN_FIXED_SQUARECLASS_IN_n=true
POLYNOMIAL_PAIR_OUTER_MEASURE_COLLAPSED_TO_n=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-119
```
