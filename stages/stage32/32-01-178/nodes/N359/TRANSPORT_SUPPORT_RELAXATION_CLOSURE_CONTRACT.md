# Stage32 32-01-178 N359 — optimistic transport/support relaxation closure

Status: `AUDIT_REQUIRED_NO_NEW_PRUNING_CREDIT`.

## Purpose

N356 supplied the balanced three-component optimistic transport mass cap. N357 supplied the exact separate omitted-support caps for those same three components. N358 found one genuine incompatibility between those two optimistic projections on the third component at total-mass saturation.

N359 asks the bounded question left by that chain:

> after N358, is there any further zero-loss pruning available from **only** the N356 transport capacities plus the N357 support model?

The answer retained here is **NO**. Within that exact optimistic model, N358 is the complete joint mass/support projection. This is a route-exhaustion result, not FULL178 completion and not a statement that the omitted geometry is realizable.

## Variables

Write `d=2h` and use the N356 stored-prefix group sums

```text
a = x2+x3+x7,
b = x1+x5+x9,
c = x0+x6+x8+x10,
M = a+b+c.
```

The balanced omitted-mass capacities of the three disjoint `2x2` transport components are

```text
R0 = 2h,
RA = 2h-a,
R3 = min(2h-b-c, 2h-2b).
```

Hence

```text
Rmax = R0+RA+R3 = Cmax-M
Cmax = min(3d, 3d+c-b),
```

exactly the hostile-audited N356 mass projection.

The hostile-audited N357 separate support maxima are

```text
S0 = min(16,d),
SA = min(13,d-a,d-2a+4,h+5),
S3 = min(9,d-b-c,d-2b,d-2c+1),
Srem = S0+SA+S3.
```

For exact omitted mass `R=e-M`, only `0<=R<=Rmax` is relevant after N356.

## Component 0 exact joint profile

At exact omitted mass `r`, component 0 has joint support maximum

```text
J0(r) = min(r,S0),  0<=r<=R0.
```

For `r<=S0`, take any `r` occupied unit slots from a maximum-support occupancy pattern; the row/column inequalities are downward closed.

At saturation `R0=2h`, choose the cell-mass matrix

```text
[t, h-t]
[h-t, t]
```

with `t=floor(h/2)`. Its support is

```text
2 min(4,t) + 2 min(4,h-t) = min(16,2h) = S0.
```

Keeping those occupied slots and increasing/decreasing positive cell masses gives every exact mass between `S0` and `R0`.

## Component A exact joint profile

Let `B=h-a`. Use aggregate omitted cell masses

```text
z : the one omitted slot in the stored-a cell,
x,y : the two cross cells,
w : the opposite cell.
```

They obey

```text
z+x <= B, z+y <= B,
x+w <= h, y+w <= h.
```

N357 already proves the maximum support is `SA`. For `r<=SA`, downward closure of a maximum-support unit occupancy gives support `r`.

At saturation `RA=2h-a`, equality forces

```text
x=y=B-z,  w=a+z,  0<=z<=B.
```

The exact saturated support is therefore

```text
1[z>0] + 2 min(4,B-z) + min(4,a+z).
```

The retained verifier checks for every `0<=h<=96` and every `0<=a<=h` that the maximum of this expression over integral `z` is exactly `SA`. Thus a saturated configuration exists with support `SA`; varying positive masses while keeping its occupied slots proves

```text
JA(r) = min(r,SA),  0<=r<=RA.
```

on the complete FULL178 degree range.

## Component 3 exact joint profile

Put

```text
B=h-b, C=h-c.
```

The aggregate omitted masses are

```text
z : the one omitted slot in the stored-b cell,
x,y : the two cross cells,
```

with

```text
z+x <= B, z+y <= B,
x <= C, y <= C.
```

The mass cap is `R3=min(B+C,2B)`.

If `B>C` (`b<c`), saturation is realized by

```text
z=B-C, x=y=C,
```

whose support is `1+2 min(4,C)`, exactly `S3`.

If `B<=C` (`b>=c`), saturation `R3=2B` forces

```text
z=0, x=y=B,
```

so saturated support is `2 min(4,B)`. This equals `S3` for `B<=4`, but for `B>=5` it is `8` while `S3=9`. One unit below saturation,

```text
z=1, x=y=B-1
```

has mass `2B-1` and support `9`.

Therefore

```text
J3(r) = min(r,S3)
```

everywhere except exactly

```text
b>=c, h-b>=5, r=R3,
```

where

```text
J3(R3)=min(R3,S3-1)=8.
```

This is precisely the N358 local saturation loss.

## Three-component convolution

Because the three components are disjoint, exact total omitted mass `R` is split as

```text
R=r0+rA+r3.
```

If `R<Srem`, distribute `R` unit-support masses among the component support capacities; since each `Si<=Ri`, support `R` is attainable.

If `Srem<=R<Rmax`, first realize all `Srem` support slots and distribute the excess mass into the residual mass capacities. In the only anomalous component-3 case, `R<Rmax` leaves at least one global mass unit of slack, so component 3 may be kept at `R3-1`, where support `S3=9` is still attainable.

At `R=Rmax`, every component is saturated. Thus the exact optimistic joint support maximum is

```text
J(R) = min(R,Srem)
```

except on

```text
b>=c, h-b>=5, R=Rmax,
```

where

```text
J(Rmax) = min(Rmax,Srem-1).
```

Now `R=e-M` and `R=Rmax` is equivalent, on this branch, to

```text
e=Cmax=3d+c-b.
```

So the exact joint necessary condition

```text
s + J(e-M) >= K
```

is identical to N357 away from the saturation face and identical to the hostile-audited N358 strengthening on that face.

## Consequence

Within the explicitly optimistic N356/N357 transport-support relaxation:

```text
N358 predicate = exact joint mass/support projection.
```

Therefore N359 has

```text
additional_rejected_exceptional_prefixes = 0
additional_rejected_terminals = 0
```

relative to the hostile-audited and MAIN-consumed N358 authority.

This closes only this relaxation route. Any further pruning must add information not present in the N356 mass capacities plus N357 support capacities, for example a new Picard/branch/effectivity/incidence constraint.

## Firewalls

```text
N358_MAIN_PRUNING_CREDIT=true
N359_MAIN_PRUNING_CREDIT=false
TRANSPORT_SUPPORT_RELAXATION_ROUTE_EXHAUSTION_AUDIT_REQUIRED=true
FULL178_COMPLETE=false
N350_PRODUCER_REGISTERED=false
PRODUCTION_COMPLETE=false
N104_RELEASE=false
RECEIVER_CREDIT=false
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
STAGE32_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
HEAVY_COMPUTE_AUTHORIZED=false
MERGE_AUTHORIZED=false
```
