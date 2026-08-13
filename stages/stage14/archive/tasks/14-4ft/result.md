# Stage14-4ft — fixed-E bare shadow splits into primitive endpoint completion support or two-sided unitary shadow

## Status

`COMPLETE_FIXED_E_BARE_SHADOW_TO_ENDPOINT_COMPLETION_OR_TWO_SIDED_UNITARY_SPLIT`

Consumes only merged theorem sources from batch-start main

```text
923b4b92bdfa90d7fa626e9ec512ea2cfb06c00e
```

namely merged `Stage14-4fs`, merged `Stage14-s7-101`, and merged `Stage14-Work-bvX34`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Enter the fixed-E nested-support receiver

Freeze one exact surviving complementary dilation `E=E0`.  Merged 4fs gives

```text
A_E0(m) <= B_E0(m),
B_E0(m)=1{exists u||m with u in U_E0(m)},
```

where `A_E0` additionally retains the canonical/root-origin/reverse/post-column completion Boolean.  On an exponent cell write

```text
S_bare=B^(sigma+o(1)),
S_phys=B^(tau+o(1)),
delta_c=sigma-tau>=0,
tau=sigma-delta_c>=mu
```

for a surviving heavy packet.

## 2. Consume the merged primitive-factor split

Write `m=u*v`, `gcd(u,v)=1` and localize

```text
u=B^(a+o(1)),
v=B^(b+o(1)).
```

Merged s7-101 proves the exhaustive alternatives

```text
Endpoint: min(a,b)=0;
Two-sided: a>0 and b>0.
```

The two branches refine the same fixed-E heavy packet and are not multiplicable.

```text
FIXED_E_PRIMITIVE_SCALE_SPLIT_CONSUMED=true
GLOBAL_S_SAME_HEAVY_PACKET_RETAINED=true
GLOBAL_S_COUNTS_MULTIPLICABLE=false
```

## 3. Endpoint branch: the unitary witness choice disappears

Suppose `u=B^o(1)`; the `v`-small case is symmetric.  Freeze the exact small value

```text
u=r0
```

at `B^o(1)` cost.  Then

```text
v=s,
m=r0*s,
gcd(r0,s)=1,
```

and the candidate unitary partition is determined by the single moving integer `s`.  There is no remaining polynomial multiplicity or existential choice of a unitary divisor at fixed `s`.

Define the exact transported bare endpoint support

```text
B_end(s)=1{gcd(r0,s)=1 and the frozen endpoint candidate lies in the retained physical size/ratio window}
```

and the completion Boolean `C_end(s)` from merged s7-101.  Then

```text
A_end(s)=B_end(s)*C_end(s).
```

Thus on the endpoint branch the Stage14-specific thinning problem is no longer a divisor-existence problem.  It is a one-dimensional conditional physical-completion support problem on the already transported endpoint outer set.

No geometry-only saving is claimed: merged s7-101 explicitly retains this branch.

```text
FIXED_E_ENDPOINT_UNITARY_WITNESS_CHOICE_EXHAUSTED=true
FIXED_E_ENDPOINT_DIVISOR_EXISTENCE_RECEIVER_RETAINS=false
FIXED_E_ENDPOINT_ONE_DIMENSIONAL_PHYSICAL_COMPLETION_SUPPORT=true
FIXED_E_ENDPOINT_GEOMETRY_FIXED_POWER_SAVING_PROVED=false
```

## 4. Two-sided branch: the genuine unitary shadow remains

If `a>0` and `b>0`, neither primitive factor can be frozen at exponent-zero cost.  Define

```text
B_2s(m)=1{exists u||m,
          u in U_E0(m),
          u and m/u both on the frozen positive exponent cells},
```

and let `A_2s(m)` impose the retained canonical/reverse completion predicate on one such witness.  Then

```text
A_2s(m)<=B_2s(m).
```

The inner witness fiber remains only `B^o(1)`, but the existence of a two-sided polynomial unitary partition is a genuine arithmetic event.

```text
FIXED_E_TWO_SIDED_UNITARY_SHADOW_RETAINS=true
FIXED_E_TWO_SIDED_PHYSICAL_COMPLETION_RETAINS=true
FIXED_E_INNER_MULTIPLICITY_RECHARGED=false
```

## 5. Receiver and H decision

This stage refines the fixed-E part of the 4fs budget, but does not yet replace the whole heavy receiver because the two-sided unitary shadow still needs an ambient comparison and the endpoint completion Boolean remains unopened.

```text
CURRENT_FIXED_E_HEAVY_RECEIVER=FixedComplementaryDilationPrimitiveEndpointOneDimensionalConditionalPhysicalCompletionSupport_OR_FixedComplementaryDilationTwoSidedPolynomialShortUnitaryShadowVersusConditionalPhysicalCompletionDeficit
RECEIVER_MATERIALLY_CHANGED=false
NEW_HEAVY_MAIN_H_NEEDED=false
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
NEXT=Stage14-4fu
```

## Boundary

```text
STAGE14_4FT=COMPLETE_FIXED_E_BARE_SHADOW_TO_ENDPOINT_COMPLETION_OR_TWO_SIDED_UNITARY_SPLIT
FIXED_E_ENDPOINT_UNITARY_WITNESS_CHOICE_EXHAUSTED=true
FIXED_E_ENDPOINT_ONE_DIMENSIONAL_PHYSICAL_COMPLETION_SUPPORT=true
FIXED_E_TWO_SIDED_UNITARY_SHADOW_RETAINS=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_HEAVY_MAIN_H_NEEDED=false
RECEIVER_MATERIALLY_CHANGED=false
NEXT=Stage14-4fu
```