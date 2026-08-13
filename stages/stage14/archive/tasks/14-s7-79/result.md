# Stage14-s7-79 — heavy-ray factorization multiplicity is divisor-subpolynomial

## Status

`COMPLETE_HEAVY_RAY_RADIAL_SCALE_AND_DIVISOR_FACTORIZATION_SEPARATION`

Consumes batch-local `Stage14-s7-78`, merged `Stage14-s7-70/77`, and merged mainline `Stage14-4el..4ep`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Fixed heavy-ray data

Stage14-s7-78 freezes, up to O(1) sign/unit data,

```text
exact polynomial common core C,
primitive reciprocal vector (x,y), gcd(x,y)=1,
primitive norm N0=x^2+y^2,
complementary quotient m0=N0/C.
```

Every unprimitive opposite-reciprocal vector on the packet is

```text
(X,Y)=h(x,y)
```

for an integer radial scale `h>=1`, and the signed reciprocal factorization satisfies

```text
p*c=h*x,
q*d=h*y.
```

## 2. Freeze only the radial exponent, not an exact radial value

The Stage14 range dictionary allows the radial scale to be partitioned into `B^o(1)` exponent/dyadic cells

```text
h=B^(sigma+o(1)),
sigma>=0.
```

This is legal. It is not legal to freeze one exact `h` if polynomially many exact radial values may carry mass.

```text
HEAVY_RAY_RADIAL_EXPONENT_SIGMA_CAN_BE_FROZEN=true
EXACT_RADIAL_SCALE_H_CAN_BE_FROZEN_AT_BO1_COST=false
```

Thus a heavy-ray saturating packet may still be concentrated on `B^o(1)` exact `h` values or diffuse across polynomially many exact radial values inside one scale cell.

## 3. For fixed h, reciprocal factorization has only divisor-many choices

Fix one exact `h`. Since

```text
p*c=h*x,
q*d=h*y,
```

the number of positive factor pairs `(p,c)` is at most `tau(h|x|)` and the number of `(q,d)` pairs is at most `tau(h|y|)`. Signs, units, 2-primary labels and the already-frozen chart contribute only `B^o(1)`.

On every polynomial Stage14 height range,

```text
tau(n)=B^o(1).
```

Therefore

```text
# {(p,q,c,d) for fixed h,x,y}=B^o(1).
```

Retaining physical range/squarefree/coprime masks can only reduce this count.

```text
FIXED_H_RECIPROCAL_FACTORIZATION_MULTIPLICITY=Bo1
DIVISOR_FACTORIZATION_RECHARGE_ALLOWED=false
```

## 4. Heavy multiplicity cannot be explained by factorization entropy

Let `M_ray` be the charged-once incidence mass on the fixed heavy primitive ray inside one radial exponent cell. Decompose it over exact radial values and reciprocal factor tuples.

Because each exact `h` has only `B^o(1)` reciprocal factor tuples, any polynomial heavy-ray multiplicity must be carried by at least one of two mechanisms:

```text
A. polynomially many exact radial values h;

B. a B^o(1)-sized set of exact h/factor tuples whose upstream
   canonical physical background fibers themselves have polynomial mass.
```

The divisor decomposition itself is not a third polynomial source.

```text
HEAVY_RAY_POLYNOMIAL_MASS_NOT_FROM_DIVISOR_FACTORIZATION=true
```

## 5. Radial concentration versus radial diffusion

Define

```text
m(h):=number of charged physical incidences on the heavy primitive ray
      with exact radial scale h,
```

with the `B^o(1)` factorization multiplicity absorbed once.

Then exactly

```text
M_ray=sum_h m(h).
```

At exponent level there are two alternatives:

```text
Radial concentration:
  some B^o(1) exact h values carry M_ray*B^(-o(1)) mass;

Radial diffusion:
  no B^o(1) exact h set carries exponent-zero mass, so a polynomial
  family of exact radial scales is genuinely required.
```

This split is structural and assumes no probabilistic independence.

```text
HEAVY_RAY_RADIAL_CONCENTRATION_DIFFUSION_DICHOTOMY_DEFINED=true
```

## 6. Receiver and next

The heavy-ray receiver has been narrowed from arbitrary reverse multiplicity to a one-dimensional radial support plus possible upstream background multiplicity at fixed scaled reciprocal data. One more stage should use

```text
Q_xi+P_xi=h*x,
Q_xi-P_xi=h*y
```

to expose the exact radial signed-quotient line and identify what remains after fixing one radial value.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_79_NEW_AUXILIARY_H_NEEDED=false
```

## Boundary

```text
STAGE14_S7_79=COMPLETE_HEAVY_RAY_RADIAL_SCALE_AND_DIVISOR_FACTORIZATION_SEPARATION
HEAVY_RAY_RADIAL_EXPONENT_SIGMA_CAN_BE_FROZEN=true
FIXED_H_RECIPROCAL_FACTORIZATION_MULTIPLICITY=Bo1
DIVISOR_FACTORIZATION_RECHARGE_ALLOWED=false
HEAVY_RAY_POLYNOMIAL_MASS_NOT_FROM_DIVISOR_FACTORIZATION=true
HEAVY_RAY_RADIAL_CONCENTRATION_DIFFUSION_DICHOTOMY_DEFINED=true
RECEIVER_MATERIALLY_CHANGED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_79_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-80
```