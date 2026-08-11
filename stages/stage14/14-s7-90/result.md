# Stage14-s7-90 — shared squarefree/square-part dilation to primitive coprime ratio normal form

## Status

`COMPLETE_SHARED_SQUAREFREE_AND_COMMON_SQUAREPART_TO_PRIMITIVE_RATIO_NORMAL_FORM`

Consumes merged `Stage14-s7-89`, merged mainline `Stage14-4fg`, merged `Stage14-Work-brX30`, and batch-start main

```text
d519dcccee5bedb4844dbcee5cb4b5171600c0bf.
```

Only merged results are theorem sources.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Entering normalized s packet

Merged s7-89 fixes positive coefficients `alpha,beta,d0` and writes every accepted heavy-ray point as

```text
n=J1*a1*b1,
|Xr|=alpha*J1*a1^2,
|Yr|=beta *J1*b1^2,
h=d0*n,
```

with `J1` squarefree and every inherited physical range, primitive, gcd, orientation, root-origin, allocation, canonical, and reverse-completion mask retained.

Merged 4fg / Work-brX30 identify the equivalent single reciprocal divisor coordinate

```text
L_s=J1*a1^2,
|Xr|=alpha*L_s,
|Yr|=beta*n^2/L_s.
```

This coordinate identification is already merged and is not counted here as a new saving or a separate support variable.

## 2. Peel the common gcd of the two square-part variables

Define exactly

```text
g:=gcd(a1,b1),
a1=g*u,
b1=g*v,
gcd(u,v)=1.
```

Now put

```text
E:=J1*g^2.
```

Because `J1` is squarefree,

```text
sqf(E)=J1,
g=sqrt(E/sqf(E)).
```

Hence the map

```text
(J1,a1,b1)
<->
(E,u,v)
```

is exact and bijective subject to

```text
gcd(u,v)=1,
E>=1,
sqf(E)=J1,
```

with all inherited coefficient/gcd masks transported through `J1=sqf(E)`.

The three main identities become

```text
boxed:
n=E*u*v,
|Xr|=alpha*E*u^2,
|Yr|=beta *E*v^2.
```

Thus the old pair

```text
shared squarefree dilation J1
+
common square part g^2
```

is a single common dilation coordinate `E`. The projective root direction is carried only by the primitive coprime ratio `(u:v)`.

```text
COMMON_SQUAREPART_GCD_PEELED=true
COMMON_DILATION_E=J1_times_g_squared
SQF_E_EQUALS_J1=true
PRIMITIVE_RATIO_GCD_U_V=1
PEELED_TRIPLE_TO_E_U_V_BIJECTION=true
```

## 3. No fresh multiplicity is introduced

For fixed normalized radial value `n`, every accepted tuple satisfies

```text
E*u*v=n,
gcd(u,v)=1.
```

Ignoring all further filters gives at most divisor-many possibilities:

```text
# {(E,u,v): Euv=n} <= d_3(n)=B^o(1).
```

This is the same charged fixed-`n` fiber already present in s7-88/89 and Work-brX30. It is not a second divisor charge.

```text
FIXED_N_E_U_V_FIBER=Bo1
FIXED_N_DIVISOR_FIBER_RECHARGED=false
```

## 4. Physical interpretation

The common dilation `E` changes the magnitude of both root factors simultaneously:

```text
(|Xr|,|Yr|)
 = E*(alpha*u^2, beta*v^2).
```

The root projective ratio is independent of `E`:

```text
|Xr|/|Yr|
 = (alpha/beta)*(u/v)^2.
```

Thus the physical root-window problem has only two deterministic pieces:

```text
common magnitude: E,
primitive projective ratio: u/v.
```

This is a sharper coordinate normal form, but the minimal receiver is not yet declared changed: the actual physical windows have not yet been eliminated against `n=Euv`.

## 5. H decision

No new `sH` is opened. The next internal step is exact: eliminate `E` using `n=Euv` and rewrite both root windows directly as a primitive ratio selector at fixed normalized radial `n`.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_90_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_90=COMPLETE_SHARED_SQUAREFREE_AND_COMMON_SQUAREPART_TO_PRIMITIVE_RATIO_NORMAL_FORM
COMMON_SQUAREPART_GCD_PEELED=true
COMMON_DILATION_E=J1_times_g_squared
SQF_E_EQUALS_J1=true
PRIMITIVE_RATIO_GCD_U_V=1
PEELED_TRIPLE_TO_E_U_V_BIJECTION=true
FIXED_N_E_U_V_FIBER=Bo1
FIXED_N_DIVISOR_FIBER_RECHARGED=false
RECEIVER_MATERIALLY_CHANGED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_90_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-91
```
