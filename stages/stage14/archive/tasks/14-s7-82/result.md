# Stage14-s7-82 — polynomial fixed-kernel support forces polynomial mobility in one physical factor

## Status

`COMPLETE_FIXED_KERNEL_RADIAL_SUPPORT_TO_ONE_FACTOR_POLYNOMIAL_OUTER_MOBILITY`

Consumes batch-local `Stage14-s7-81`, merged `Stage14-4ev..4ex`, merged `Stage14-Work-boX27`, and the charged-once fixed-h reverse-fiber boundary.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Choose one charged-once factor packet per accepted radial value

On the fixed heavy primitive ray, merged `4ex` gives an injective map

```text
h -> T=K*(t0*h)^2.
```

For each accepted exact `h`, choose one charged-once complete physical factor packet

```text
(F1,F2,F3,F4)
 = (|Xr|,|Yr|,|U|,|V|)
```

satisfying

```text
4*F1*F2*F3*F4=T.
```

This choice is legitimate because the physical fiber over one exact `h` or `T` is only `B^o(1)`. Selecting one representative cannot create a power saving or enlarge the support.

Let

```text
S_j := {Fj(h) : h in H_phys}
```

be the value support of the `j`-th factor in the chosen representatives.

```text
ONE_CHARGED_FACTOR_PACKET_SELECTED_PER_H=true
REPRESENTATIVE_SELECTION_POWER_COST=Bo1
```

## 2. Product-support inequality

Distinct accepted `h` give distinct exact products `T`. Every chosen product is determined by one quadruple from

```text
S_1 x S_2 x S_3 x S_4.
```

Therefore

```text
#H_phys
 <= # {T}
 <= |S_1| |S_2| |S_3| |S_4|.
```

The first inequality is equality on the fixed ray by injectivity, but the weaker displayed form is enough.

If the heavy-ray branch has polynomial radial support

```text
#H_phys >= B^(mu-o(1)),
mu>0,
```

then necessarily

```text
max_j |S_j| >= B^(mu/4-o(1)).
```

Thus at least one of the four physical factors has genuinely polynomial outer value mobility.

```text
POLYNOMIAL_RADIAL_SUPPORT_FORCES_POLYNOMIAL_FACTOR_VALUE_SUPPORT=true
POLYNOMIAL_FACTOR_SUPPORT_EXPONENT_AT_LEAST=mu/4
```

## 3. Freeze which factor moves

There are only four factor labels. Freeze one index

```text
j_* in {1,2,3,4}
```

with maximal support. This costs only `O(1)`.

Call the corresponding moving factor

```text
F_* in { |Xr|, |Yr|, |U|, |V| }.
```

Its value support satisfies a fixed positive power lower bound on every polynomially saturating radial packet.

This does not mean the other three factors are fixed or subpolynomial. It means only that one polynomial outer coordinate can be selected without loss of exponent.

```text
ONE_POLYNOMIAL_FACTOR_MOVER_CAN_BE_FROZEN_AT_O1_COST=true
OTHER_THREE_FACTORS_FIXED_ASSUMED=false
```

## 4. Squareclass relation seen by the mover

Let

```text
kappa_* := sqf(F_*).
```

The exact s7-81 relation gives

```text
kappa_*
 = K * product_{j!=j_*} sqf(F_j)
```

inside the squareclass group `Q_{>0}^*/(Q_{>0}^*)^2`.

Thus the mover squareclass is selected by the joint squareclasses of the other physical factors and the fixed primitive-ray kernel `K`. No standalone density statement for `kappa_*` is legal without retaining that correlation.

```text
MOVER_SQUARECLASS_SELECTED_BY_OTHER_FACTORS_AND_FIXED_K=true
MOVER_SQUARECLASS_INDEPENDENCE_ASSUMED=false
```

## 5. Receiver and next

The fixed-kernel square-value receiver has now been opened to a factor-level polynomial outer coordinate, but the mover factor may vary either mainly through its squarefree kernel or mainly through its square part. The next stage should split those two possibilities quantitatively.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_82_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_82=COMPLETE_FIXED_KERNEL_RADIAL_SUPPORT_TO_ONE_FACTOR_POLYNOMIAL_OUTER_MOBILITY
POLYNOMIAL_RADIAL_SUPPORT_FORCES_POLYNOMIAL_FACTOR_VALUE_SUPPORT=true
ONE_POLYNOMIAL_FACTOR_MOVER_CAN_BE_FROZEN_AT_O1_COST=true
MOVER_SQUARECLASS_SELECTED_BY_OTHER_FACTORS_AND_FIXED_K=true
RECEIVER_MATERIALLY_CHANGED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_82_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-83
```
