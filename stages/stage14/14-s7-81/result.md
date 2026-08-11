# Stage14-s7-81 — heavy-ray radial-support capacity and primitive-ray height gap

## Status

`COMPLETE_HEAVY_RAY_RADIAL_SUPPORT_CAPACITY_AND_PRIMITIVE_RAY_HEIGHT_GAP`

Consumes merged `Stage14-s7-78..80`, merged mainline `Stage14-4eq..4eu`, merged `Stage14-Work-boX27`, and latest main at batch start

```text
58ebe4a8312c74a7d909138c49472e1e4b0825e9.
```

The updated batch contract on this main integrates a newly exposed `sH` as a work unit, but no new `sH` is exposed in this stage.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Consume the fixed-h closure

Fix one polynomial common-core modulus `C` and one heavy primitive reciprocal ray. After the frozen sign/unit label there is one primitive pair

```text
(x,y),
gcd(x,y)=1,
N0=x^2+y^2=C*m0,
```

and every raw opposite-reciprocal vector on the ray is

```text
(X,Y)=h(x,y),
h>=1.
```

Merged `4eq` proves the missing reverse statement left open by s7-80:

```text
fixed (C,x,y,h)
  -> full canonical physical background fiber = B^o(1).
```

Hence a `B^o(1)` set of exact radial values cannot carry polynomial heavy-ray mass. This is also the heavy-ray specialization of merged Work-boX27's subpolynomial-fiber support-relocation lemma.

```text
MERGED_4EQ_FIXED_H_CLOSURE_CONSUMED=true
MERGED_WORK_BOX27_SUPPORT_RELOCATION_CONSUMED=true
HEAVY_RAY_RADIAL_CONCENTRATION_BRANCH_CLOSED=true
```

## 2. Freeze one raw reciprocal archimedean cell

Freeze a charged-once dyadic/range cell

```text
|X| ~ R,
|Y| ~ S
```

with all original sign, angular, chart, endpoint and allocation masks retained. Since

```text
X=h*x,
Y=h*y,
```

an admissible integer `h` lies in the intersection of two constant-factor intervals

```text
h ~ R/|x|,
h ~ S/|y|.
```

Therefore the total number of possible exact radial values in this cell satisfies

```text
# {h compatible with the raw cell}
  << 1 + min(R/|x|, S/|y|).
```

Define the radial capacity

```text
H_cap := 1 + min(R/|x|, S/|y|).
```

This bound uses only the exact radial identity and the frozen physical range cell. It does not assume equidistribution or independence.

```text
HEAVY_RAY_RADIAL_CAPACITY_DEFINED=true
RADIAL_CAPACITY_UPPER_BOUND=min_R_over_x_S_over_y_plus_1
```

## 3. Heavy-ray saturation forces polynomial radial capacity

Let `M_ray` be the charged-once heavy-ray incidence mass in the frozen cell. For each exact `h`, merged 4eq gives only `B^o(1)` physical backgrounds, so

```text
M_ray <= H_cap * B^o(1).
```

Consequently, if this heavy-ray cell carries polynomial mass

```text
M_ray=B^(mu+o(1)),
mu>0,
```

then necessarily

```text
H_cap >= B^(mu-o(1)).
```

Thus square-root-scale survival on a heavy ray cannot come from reverse multiplicity at fixed radius. It requires genuinely polynomial radial room inside the physical reciprocal box.

```text
HEAVY_RAY_POLYNOMIAL_MASS_FORCES_POLYNOMIAL_RADIAL_CAPACITY=true
FIXED_H_REVERSE_MULTIPLICITY_CANNOT_SUPPORT_POLYNOMIAL_MASS=true
```

## 4. Primitive-ray height gap

Because

```text
H_cap <= 1 + R/|x|,
H_cap <= 1 + S/|y|,
```

a polynomial-capacity cell with `H_cap=B^(sigma+o(1))`, `sigma>0`, forces

```text
|x| <= R * B^(-sigma+o(1)),
|y| <= S * B^(-sigma+o(1)).
```

Hence

```text
N0=x^2+y^2
   <= (R^2+S^2) B^(-2*sigma+o(1)),
```

and since `N0=C*m0`,

```text
C*m0
  <= (R^2+S^2) B^(-2*sigma+o(1)).
```

Polynomial radial mobility therefore forces the primitive reciprocal ray to sit polynomially inside the raw reciprocal scale. This is a genuine range consequence, not yet a counting saving for the whole family.

```text
POLYNOMIAL_RADIAL_CAPACITY_FORCES_PRIMITIVE_RAY_HEIGHT_GAP=true
HEAVY_RAY_PRIMITIVE_NORM_GAP_EXPONENT=2*sigma
```

## 5. Receiver and next

The heavy-ray receiver remains the same radial-support problem, now with an exact capacity/height constraint. The next stage should insert the radial identity into the exact second reciprocal difference-of-squares equation and expose how the moving square `h^2` enters the physical factor packet.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_81_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_81=COMPLETE_HEAVY_RAY_RADIAL_SUPPORT_CAPACITY_AND_PRIMITIVE_RAY_HEIGHT_GAP
MERGED_4EQ_FIXED_H_CLOSURE_CONSUMED=true
HEAVY_RAY_RADIAL_CONCENTRATION_BRANCH_CLOSED=true
HEAVY_RAY_RADIAL_CAPACITY_DEFINED=true
HEAVY_RAY_POLYNOMIAL_MASS_FORCES_POLYNOMIAL_RADIAL_CAPACITY=true
POLYNOMIAL_RADIAL_CAPACITY_FORCES_PRIMITIVE_RAY_HEIGHT_GAP=true
RECEIVER_MATERIALLY_CHANGED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_81_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-82
```
