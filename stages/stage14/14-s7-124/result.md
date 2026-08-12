# Stage14-s7-124 — freeze one squarefree allocation and transport the first-layer physical filters

## Status

`COMPLETE_FIRST_REVERSE_ALLOCATION_FREEZE_AND_MULTIPLICATIVE_HOST_FILTER_TRANSPORT`

Consumes batch-local `Stage14-s7-123` and merged `Stage14-s7-119..122`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Notation and one frozen allocation

To avoid collision with the reconstructed reverse variable named `c`, write

```text
C = K*c_C^2,
K=sqf(C).
```

By s7-123 the first reverse factor pair is exactly

```text
F2^- = g*A*x^2,
F2^+ = g*B*y^2,
A*B=K,
gcd(A,B)=1,
g*x*y=c_C*z.
```

There are only `2^omega(K)=B^o(1)` ordered allocations `(A,B)`. On a principal exponent cell we may freeze one exact ordered allocation `(A_*,B_*)` at `B^o(1)` cost. This does not create a density saving.

```text
S_FIRST_REVERSE_ALLOCATION_FROZEN=true
S_FIRST_REVERSE_ALLOCATION_FREEZE_COST=Bo1
S_FIRST_REVERSE_ALLOCATION_FREEZE_USED_AS_SAVING=false
```

## 2. First-layer reconstructed coordinates

For the frozen allocation define

```text
F2^-(g,x,y)=g*A_*x^2,
F2^+(g,x,y)=g*B_*y^2,
cp=(F2^++F2^-)/2,
dq=(F2^+-F2^-)/2.
```

The first reverse layer is therefore completely determined by a positive triple `(g,x,y)` satisfying

```text
g*x*y=c_C*z.
```

All conditions that were already imposed before the ordered factorizations

```text
cp=c*p,
dq=d*q
```

are now deterministic predicates of `(z,g,x,y)` and the frozen packet data. These include:

```text
- integrality of cp,dq, equivalently the required parity of F2^- and F2^+;
- positivity/order and endpoint-side orientation;
- the inherited first-layer size cell;
- already-exposed gcd/divisibility labels that depend only on F2^-,F2^+,cp,dq and frozen data.
```

No downstream root/canonical/post-column acceptance is moved into this predicate.

Define

```text
R_mult(z;g,x,y) in {0,1}
```

as exactly this first-layer deterministic conjunction.

## 3. Multiplicative-host witness set

For one outer candidate with scalar host `z`, define

```text
Omega_mult(z)
 := {(g,x,y)>0:
       g*x*y=c_C*z,
       R_mult(z;g,x,y)=1}.
```

Then the full square-class reverse witness set `Omega_sq(chi)` of s7-119 is obtained from some member of `Omega_mult(z)` by subsequently choosing ordered factorizations

```text
cp=c*p,
dq=d*q,
```

then solving the second reverse factor-pair equation and finally imposing the residual extension mask.

Thus

```text
Omega_sq(chi) nonempty
=> Omega_mult(z) nonempty,
```

but the converse is not asserted.

```text
S_FIRST_REVERSE_MULTIPLICATIVE_HOST_SET_DEFINED=true
S_FULL_REVERSE_SUPPORT_IMPLIES_FIRST_MULTIPLICATIVE_SUPPORT=true
S_FIRST_MULTIPLICATIVE_SUPPORT_IMPLIES_FULL_REVERSE_SUPPORT=false
```

## 4. Fixed-z multiplicity

For fixed `z`, the equation `g*x*y=c_C*z` has at most

```text
d_3(c_C*z)=B^o(1)
```

positive triples throughout the polynomial-height packet. This is a witness-fiber bound only.

It does not prove that `Omega_mult(z)` is nonempty and cannot be recharged as an outer density saving.

```text
S_FIRST_MULTIPLICATIVE_FIXED_Z_FIBER=Bo1
S_FIRST_MULTIPLICATIVE_FIXED_Z_FIBER_RECHARGED=false
```

## 5. Charged measures

The same algebraic host is retained on all three active nonaligned realizations, but the charged measures remain:

```text
endpoint: outer scalar t, z=t;
fixed-product: outer scalar E, z=E;
polynomial-pair: outer pair (E,m), z=E*m only inside the reverse host.
```

Therefore even after allocation freezing, scalar and pair support theorems remain distinct.

```text
S_MULTIPLICATIVE_HOST_COMMON=true
S_MULTIPLICATIVE_CHARGED_MEASURE_COMMON=false
S_MULTIPLICATIVE_SUPPORT_CROSS_PROMOTABLE=false
```

## 6. Receiver / next

The first reverse layer is no longer an opaque factor-pair selector. It is a deterministic filtered triple-product host followed by the remaining second reverse layer and post-mask. The next stage introduces separate exponent deficits for these layers and freezes the sharpened theorem contracts.

```text
RECEIVER_MATERIALLY_CHANGED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-125
```

## Boundary

```text
STAGE14_S7_124=COMPLETE_FIRST_REVERSE_ALLOCATION_FREEZE_AND_MULTIPLICATIVE_HOST_FILTER_TRANSPORT
S_FIRST_REVERSE_ALLOCATION_FROZEN=true
S_FIRST_REVERSE_MULTIPLICATIVE_HOST_SET_DEFINED=true
S_FIRST_MULTIPLICATIVE_FIXED_Z_FIBER=Bo1
S_FIRST_MULTIPLICATIVE_FIXED_Z_FIBER_RECHARGED=false
S_MULTIPLICATIVE_CHARGED_MEASURE_COMMON=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-125
```
