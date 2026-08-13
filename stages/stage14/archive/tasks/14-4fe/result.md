# Stage14-4fe — radial denominator peel and bare factorization no-go

## Status

`COMPLETE_RADIAL_DENOMINATOR_PEEL_AND_BARE_FACTORIZATION_NO_GO`

Consumes merged `Stage14-4fd`, merged `Stage14-s7-86`, merged `Stage14-Work-bqX29`, and latest merged main at batch start

```text
c5c84d2727caad0afdc08dec69f6696716f21b38.
```

Only merged results are theorem sources.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Entering heavy-ray packet

Merged 4fd fixes one surviving heavy primitive reciprocal ray and one agreement packet with

```text
M_C=B^(mu+o(1)),
0<mu<=rho(phi):=1/4-phi<=1/24,
B^(mu-o(1)) <= |H_*| <= B^(rho(phi)+o(1)).
```

Merged s7-86, on the identical fixed ray/agreement packet, writes the exact root/radial identity

```text
d0*J*a*b = c0*h,                                  (1)
```

where

```text
gcd(c0,d0)=1,
J squarefree,
gcd(J,K_Z)=1,
a,b>=1,
```

and `(c0,d0,K_Z)` are frozen with the packet.

## 2. Exact denominator divisibility

From (1) and `gcd(c0,d0)=1`, every physically accepted radial scale satisfies

```text
d0 | h.                                            (2)
```

Write

```text
d0=B^(delta+o(1)),
delta>=0.
```

Because all accepted radial scales lie below the merged 4fd capacity

```text
h <= B^(rho(phi)+o(1)),
```

(2) gives the exact elementary support bound

```text
|H_*| <= B^(rho(phi)-delta+o(1)).                  (3)
```

Combining (3) with the heavy-ray lower bound from 4fd yields the necessary survivor inequality

```text
boxed:
delta <= rho(phi)-mu.                              (4)
```

Thus a polynomial denominator can be charged, but only against the unused radial-capacity slack. In particular a near-capacity heavy ray with `mu=rho(phi)-o(1)` forces

```text
d0=B^o(1).
```

```text
RADIAL_DENOMINATOR_DIVIDES_EVERY_ACCEPTED_H=true
RADIAL_DENOMINATOR_SUPPORT_DEFICIT_EXPONENT=delta
SURVIVING_HEAVY_RAY_DENOMINATOR_EXPONENT_MAX=rho_minus_mu
NEAR_CAPACITY_HEAVY_RAY_FORCES_D0=Bo1
```

## 3. Bare squareclass/factorization algebra has no further sparsity

The denominator divisibility is the complete support restriction coming from equation (1) before the remaining physical root-factor windows are imposed.

Indeed, put

```text
h=d0*n.
```

Then (1) is equivalent to

```text
J*a*b=c0*n.                                        (5)
```

For every integer `n>=1`, the tuple

```text
J=1,
a=1,
b=c0*n
```

satisfies (5), with `J` squarefree and `gcd(J,K_Z)=1` automatically. Therefore the bare root squareclass/factorization equation accepts every normalized radial integer `n`; any further thinning must come from the transported physical size, chamber, origin, coprimality, or canonical-completion masks.

This is a rigorous no-go for extracting another independent fixed-power loss from the equality `d0*J*a*b=c0*h` itself.

```text
BARE_RADIAL_FACTORIZATION_SUPPORT_EXACTLY_MULTIPLES_OF_D0=true
BARE_NORMALIZED_RADIAL_EQUATION_ACCEPTS_EVERY_N=true
FRESH_SQUARECLASS_FACTORIZATION_POWER_SAVING_AVAILABLE=false
PHYSICAL_FACTOR_WINDOWS_ARE_NOW_ESSENTIAL=true
```

## 4. Receiver and H decision

This stage does not yet change the minimal heavy receiver: it peels the only unconditional arithmetic modulus inside the radial factorization and proves that the remaining algebraic equality is support-dense.

No new H is opened. The next internal step is to normalize by `d0` and transfer the heavy mass requirement to the physical acceptance set on the normalized radial coordinate.

```text
RECEIVER_MATERIALLY_CHANGED=false
NEW_MAIN_H_NEEDED=false
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
NEXT=Stage14-4ff
```
