# Stage14-s7-84 — merged agreement-pair compression localizes s7-83 mobility to the root side

## Status

`COMPLETE_MERGED_4FA_AGREEMENT_COMPRESSION_LOCALIZES_S83_MOBILITY_TO_ROOT_SIDE`

Consumes merged `Stage14-s7-83`, merged mainline `Stage14-4ey..4fa`, merged `Stage14-Work-bpX28`, and batch-start main

```text
95e98cbd6626bc8f50a1397be881d04722b271ff.
```

Only merged results are theorem sources.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Entering s receiver

Merged s7-83 starts from one fixed heavy primitive reciprocal ray and one factor label

```text
F_* in {|Xr|,|Yr|,|U|,|V|}
```

with polynomial value support.  It then splits that support into moving squarefree kernel versus fixed-kernel square-part mobility.

That result predated the merged mainline compression `4ey..4fa`.  We now consume the stronger merged theorem rather than reprove its root-line argument.

## 2. Merged 4fa removes polynomial agreement-pair freedom

Merged 4ey reconstructs the squarefree agreement product

```text
D=U*V
```

from the fixed ray kernel and the root product squareclass.  Merged 4ez then produces the large fixed-ray overlap

```text
G=gcd(UV,K),
G|K,
G>=B^(1/3-o(1)).
```

Because `G|K` with fixed `K`, exact `G` has only divisor-many `B^o(1)` possibilities.  Merged 4fa further freezes the coprime allocation

```text
G=G_U*G_V
```

at `B^o(1)` cost and proves, conditionally on the already-charged common-core root line,

```text
# {(U,V) | fixed C,K,G,G_U,G_V,coefficient/root label}=B^o(1).
```

The dictionaries of admissible `G`, allocations and frozen finite/root labels are themselves only `B^o(1)`.  Therefore on one fixed heavy-ray packet the total agreement-pair value support satisfies

```text
|S_U|+|S_V|=B^o(1).
```

This is a use of merged 4fa in its proved direction.  The common-core root-line density is not charged again.

```text
MERGED_4FA_CONSUMED=true
AGREEMENT_PAIR_TOTAL_VALUE_SUPPORT=Bo1
AGREEMENT_SIDE_POLYNOMIAL_FACTOR_MOBILITY_REMOVED=true
COMMON_CORE_ROOT_LINE_RECHARGED=false
```

## 3. Polynomial factor mobility must be root-side

Merged s7-82 gives, after choosing one charged factor packet per radial value,

```text
#H_phys
 <= |S_Xr| |S_Yr| |S_U| |S_V|.
```

A saturating heavy ray has polynomially many accepted radial values on the branch under discussion.  Since `|S_U||S_V|=B^o(1)` after merged 4fa, necessarily

```text
|S_Xr| |S_Yr| >= B^(mu-o(1))
```

for the radial-support exponent `mu>0`.  Hence at least one root label

```text
F_root in {|Xr|,|Yr|}
```

has polynomial value support.

Because only `B^o(1)` agreement pairs survive, one exact `(U,V)` may also be frozen on a polynomial radial-support subpacket without changing its fixed-power exponent.

```text
POLYNOMIAL_FACTOR_MOBILITY_MUST_BE_ROOT_SIDE=true
ONE_EXACT_AGREEMENT_PAIR_CAN_BE_FROZEN_AT_BO1_COST=true
ROOT_FACTOR_SUPPORT_EXPONENT_AT_LEAST=mu/2
```

## 4. Exact root-product equation after freezing the agreement pair

Let

```text
D0:=x^2-y^2>0
```

be the fixed primitive-ray difference.  Merged 4ex/4fa gives the exact second reciprocal identity

```text
h^2 D0
 = 4*epsilon_x*Xr*Yr*U*V.
```

Freeze the finite sign convention and one surviving `(U,V)`.  Then

```text
Xr*Yr = r0*h^2,
r0:=D0/(4*epsilon_x*U*V)
```

as an exact equality in positive rational numbers; every physical point makes the left side integral.  Thus the two root factors are not independent polynomial coordinates: their product lies on one fixed rational squareclass times `h^2`.

```text
FIXED_AGREEMENT_ROOT_PRODUCT_EQUATION=true
ROOT_PRODUCT_RATIONAL_SQUARECLASS_FIXED=true
```

## 5. Receiver and H decision

This stage consumes the newly merged agreement compression and removes the now-impossible `U/V` mover alternatives from s7-83.  It does not yet choose between the two root-side kernel/square-part mechanisms, so the minimal two-branch s receiver is retained with the factor label restricted to `Xr` or `Yr`.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_84_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

The next stage should exploit the fixed squareclass of `Xr*Yr` to determine how two moving root kernels can vary.

## Boundary

```text
STAGE14_S7_84=COMPLETE_MERGED_4FA_AGREEMENT_COMPRESSION_LOCALIZES_S83_MOBILITY_TO_ROOT_SIDE
MERGED_4FA_CONSUMED=true
AGREEMENT_PAIR_TOTAL_VALUE_SUPPORT=Bo1
AGREEMENT_SIDE_POLYNOMIAL_FACTOR_MOBILITY_REMOVED=true
POLYNOMIAL_FACTOR_MOBILITY_MUST_BE_ROOT_SIDE=true
ONE_EXACT_AGREEMENT_PAIR_CAN_BE_FROZEN_AT_BO1_COST=true
FIXED_AGREEMENT_ROOT_PRODUCT_EQUATION=true
COMMON_CORE_ROOT_LINE_RECHARGED=false
RECEIVER_MATERIALLY_CHANGED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_84_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-85
```
