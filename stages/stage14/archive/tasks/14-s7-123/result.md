# Stage14-s7-123 — normalize the first square-class reverse factor pair by coprime squarefree allocation

## Status

`COMPLETE_FIRST_REVERSE_LAYER_COPRIME_SQUAREFREE_ALLOCATION_NORMAL_FORM`

Consumes merged `Stage14-s7-119..122` and merged `Stage14-Work-cbX40` at batch-start main

```text
a9b864841a6c42e6f42d3e23ad583162aaf0653c
```

The aligned fixed-E two-sided branch remains parked at its existing main external gate. This stage concerns only the three active nonaligned s realizations.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Exact first reverse equation

For one exact precompletion candidate `chi`, merged s7-119 gives

```text
M=M0*z^2,
W2(z)=C*z^2,
F2^-*F2^+=C*z^2,
```

where `C=4*P0*epsilon_x*U*V` is frozen on the packet and the positive factor pair `(F2^-,F2^+)` is subject to the inherited parity, order, endpoint and reconstruction filters.

Write

```text
g := gcd(F2^-,F2^+),
F2^- = g*r,
F2^+ = g*s,
gcd(r,s)=1.
```

Then

```text
g^2*r*s = C*z^2.
```

Let

```text
K := sqf(C),
C = K*c^2
```

with `K` squarefree and `c>=1` integral. Taking squarefree kernels gives

```text
sqf(r*s)=K.
```

Because `gcd(r,s)=1`, there are unique coprime squarefree integers `A,B` and positive integers `x,y` such that

```text
A*B=K,
gcd(A,B)=1,
r=A*x^2,
s=B*y^2.
```

Substitution into the product identity gives the exact positive relation

```text
(g*x*y)^2 = c^2*z^2,
```

hence

```text
g*x*y = c*z.
```

Thus every first-layer reverse factor pair is represented exactly as

```text
F2^- = g*A*x^2,
F2^+ = g*B*y^2,
A*B=K,
gcd(A,B)=1,
g*x*y=c*z,
```

with the original parity/order/reconstruction conditions retained as filters.

## 2. Converse

Conversely, any positive tuple `(A,B,g,x,y)` satisfying

```text
A*B=K,
A,B squarefree,
gcd(A,B)=1,
g*x*y=c*z
```

produces

```text
F2^- = g*A*x^2,
F2^+ = g*B*y^2
```

and therefore

```text
F2^-*F2^+ = g^2*K*x^2*y^2 = K*c^2*z^2 = C*z^2.
```

So this is an exact bijective normalization once the ordered squarefree allocation `(A,B)` is included. No density statement is used.

```text
S_FIRST_REVERSE_SQUARECLASS_ALLOCATION_NORMAL_FORM_PROVED=true
S_FIRST_REVERSE_EXACT_RELATION=g_times_x_times_y_eq_c_times_z
S_FIRST_REVERSE_CONVERSE_PROVED=true
```

## 3. Allocation multiplicity

The ordered squarefree allocations satisfy `A*B=K`, so their number is

```text
2^omega(K) <= tau(K) = B^o(1)
```

for the frozen polynomial-height coefficient `K`.

This is only a label multiplicity. It may be frozen on a principal exponent cell at `B^o(1)` cost, but it is not an outer-density saving and it does not imply that any allocation survives the inherited physical filters.

```text
S_FIRST_REVERSE_ALLOCATION_COUNT=Bo1
S_FIRST_REVERSE_ALLOCATION_DENSITY_SAVING_RECHARGED=false
```

## 4. Branch measures remain unchanged

The scalar host `z` is still

```text
endpoint: z=t,
fixed-product: z=E,
polynomial pair: z=n=E*m.
```

The exact factor-pair algebra is common, but the charged outer measures remain respectively scalar `t`, scalar `E`, and pair `(E,m)`. The normalization therefore does not prove a cross-branch support adapter.

```text
S_FIRST_REVERSE_ALGEBRA_COMMON=true
S_FIRST_REVERSE_OUTER_MEASURE_COMMON=false
S_FIRST_REVERSE_SUPPORT_CROSS_PROMOTABLE=false
```

## 5. Receiver

The receiver is refined but not yet materially changed: the bare square-class support in each active nonaligned branch can now be opened through a `B^o(1)` family of exact multiplicative hosts

```text
g*x*y=c*z
```

followed by the inherited `cp,dq -> (c,p),(d,q)` reconstruction, the second reverse factor pair, and the residual post-mask.

The next stage freezes one allocation and transports all first-layer physical congruence/order conditions onto this multiplicative host.

```text
RECEIVER_MATERIALLY_CHANGED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-124
```

## Boundary

```text
STAGE14_S7_123=COMPLETE_FIRST_REVERSE_LAYER_COPRIME_SQUAREFREE_ALLOCATION_NORMAL_FORM
S_FIRST_REVERSE_SQUARECLASS_ALLOCATION_NORMAL_FORM_PROVED=true
S_FIRST_REVERSE_EXACT_RELATION=g_times_x_times_y_eq_c_times_z
S_FIRST_REVERSE_ALLOCATION_COUNT=Bo1
S_FIRST_REVERSE_ALLOCATION_DENSITY_SAVING_RECHARGED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-124
```
