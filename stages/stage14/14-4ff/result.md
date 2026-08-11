# Stage14-4ff — normalized radial support and heavy-mass transfer

## Status

`COMPLETE_NORMALIZED_RADIAL_SUPPORT_AND_HEAVY_MASS_TRANSFER`

Consumes Stage14-4fe on the same batch branch and merged `Stage14-4eq/4fd/s7-86`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Normalize the exact radial coordinate

Stage14-4fe proves every accepted radial scale has

```text
h=d0*n,
```

with fixed `d0`, and that the bare root factorization becomes

```text
J*a*b=c0*n.                                        (1)
```

Let

```text
d0=B^(delta+o(1)),
rho:=rho(phi)=1/4-phi,
0<mu<=rho,
delta<=rho-mu.
```

Define the normalized physical radial support

```text
N_*
 := {n>=1 : d0*n belongs to H_*}.
```

The map `n -> h=d0*n` is injective, hence exactly

```text
|N_*|=|H_*|.                                       (2)
```

Merged 4fd and 4fe therefore give

```text
boxed:
B^(mu-o(1)) <= |N_*| <= B^(rho-delta+o(1)).        (3)
```

The normalized ambient radial exponent is `rho-delta`; the heavy packet occupies it with exponent at least `mu`.

```text
NORMALIZED_RADIAL_COORDINATE_DEFINED=true
NORMALIZED_RADIAL_SUPPORT_CARDINALITY_EQUALS_H_SUPPORT=true
NORMALIZED_RADIAL_AMBIENT_EXPONENT=rho_minus_delta
NORMALIZED_RADIAL_REQUIRED_SUPPORT_EXPONENT=mu
```

## 2. Fixed normalized radial value has only subpolynomial fiber

For fixed `n`, equation (1) has at most divisor-many root-factor tuples:

```text
# {(J,a,b): J*a*b=c0*n}
 <= d_3(c0*n)
 = B^o(1)
```

on the polynomial Stage14 height range. Merged s7-86 gives the same statement with all squarefree/gcd restrictions retained, and merged 4eq gives `B^o(1)` full physical reverse multiplicity per exact `h`, hence per exact `n`.

Thus no hidden atomic weight can carry the heavy exponent above one normalized radial value:

```text
FIXED_N_ROOT_FACTOR_FIBER=Bo1
FIXED_N_FULL_PHYSICAL_REVERSE_FIBER=Bo1
```

Consequently the heavy mass requirement is genuinely a support requirement on distinct normalized integers `n`, not a weight-concentration statement.

## 3. The survivor density is now an explicit one-dimensional object

Let

```text
N_amb
 := {n>=1 : n <= B^(rho-delta+o(1))
               and the frozen parity/scale convention for h=d0*n holds}.
```

Finite parity/end-point labels cost only `B^o(1)`. Define

```text
A_rad(n)=1
```

iff at least one of the divisor-many tuples `(J,a,b)` with `Jab=c0*n` survives every transported physical root-factor window and the already-charged canonical reverse-completion masks.

Then

```text
N_*={n in N_amb : A_rad(n)=1}
```

up to the frozen `B^o(1)` decorations, and a surviving heavy ray requires

```text
# {n in N_amb : A_rad(n)=1}
 >= B^(mu-o(1)).                                  (4)
```

No independence or multiplicative structure of `A_rad` is asserted.

```text
HEAVY_MASS_RELOCATED_TO_NORMALIZED_RADIAL_ACCEPTANCE_SUPPORT=true
RADIAL_ACCEPTANCE_BOOLEAN_DEFINED=true
RADIAL_ACCEPTANCE_MULTIPLICATIVE=false
RADIAL_ACCEPTANCE_INDEPENDENCE_PROVED=false
```

## 4. Receiver and H decision

This stage still refines the same heavy radial branch. The next step must open `A_rad` by substituting the fixed squareclass normal form for the two root factors and identifying exactly which masks can thin the divisor tuples.

```text
RECEIVER_MATERIALLY_CHANGED=false
NEW_MAIN_H_NEEDED=false
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
NEXT=Stage14-4fg
```
