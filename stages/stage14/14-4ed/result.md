# Stage14-4ed — primitive Gaussian root-density gate and mainline branch switch

## Status

`COMPLETE_RECIPROCAL_ROOT_DENSITY_H_GATE_AND_MAINLINE_SWITCH_TO_CANONICAL_ALLOCATION`

Consumes batch-local `Stage14-4ec`, newly merged `Stage14-s7-71`, merged `Stage14-s7-68`, `Stage14-Work-blX24`, `Stage14-s7-42/46/60`, `Stage14-X13`, and merged `Stage14-4ea`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Reciprocal factor has reached its theorem gate

Stage14-4ec reduces the reciprocal conditional factor to the Boolean event that a canonical allocation-bearing primitive slope has at least one charged-once primitive candidate

```text
(C0,X0,Y0)
```

with

```text
C0 | X0^2+Y0^2,
gcd(X0,Y0)=1,
gcd(C0,X0Y0)=1.
```

This agrees with merged s7-71.

Primewise the selector is one root line

```text
X0 == i_C Y0 (mod C0),
i_C^2 == -1 (mod C0).
```

There is no independent second growing modulus; reusing `C0` after its Gaussian orientation has already been charged would double count the same condition. Divisor switching among `(p,q,c,d)` and `(X0,Y0)` is only `B^o(1)` reparametrization, and X13 makes the post-column layer a finite-fiber filter.

```text
SECOND_RECIPROCAL_ROOT_LINE_MODULUS_IS_C0=true
INDEPENDENT_SECOND_GROWING_MODULUS_PRODUCED=false
ROOT_LINE_DOUBLE_CHARGE_ALLOWED=false
SECOND_RECIPROCAL_DIVISOR_SWITCH_FIBER=Bo1
POST_COLUMN_REVERSE_COMPLETION_INDEPENDENT_POLYNOMIAL_SELECTOR=false
```

Pointwise root-line counting does not uniformly close the receiver because `C0` and the reciprocal candidate vector are correlated through the physical allocation packet.

```text
POINTWISE_ROOT_LINE_COUNT_UNIFORMLY_CLOSES_RECEIVER=false
PRIMITIVE_GAUSSIAN_ROOT_CONDITIONAL_DENSITY_THEOREM_PROVED=false
FIXED_POWER_RECIPROCAL_ROOT_DENSITY_DEFICIT_PROVED=false
```

Therefore the reciprocal sub-branch is now correctly delegated to

```text
Stage14-sH71
CanonicalAllocationConditionalPrimitiveGaussianRootDensity.
```

At publication recheck no merged sH71 theorem is available.

## 2. The whole mainline is not blocked

Merged 4ea has the exact two-factor chain

```text
mu_G = mu_can * mu_root,
```

where `mu_root` is the reciprocal root density above and `mu_can` is the canonical balanced integer/Gaussian allocation density.

A fixed-power deficit in **either** factor closes the range-stable arithmetic branch. Hence the fact that `mu_root` is waiting for sH71 does not force the mainline to stop: the legal alternative is to attack `mu_can` directly without using or assuming any sH71 conclusion.

```text
RECIPROCAL_SUBROUTE_H_NEEDED=true
RECIPROCAL_SUBROUTE_H_TARGET=CanonicalAllocationConditionalPrimitiveGaussianRootDensity
S_ROUTE_H_NEEDED=true
S_ROUTE_BLOCKED_WAITING_FOR_H=true
MAINLINE_BLOCKED_WAITING_FOR_H=false
MAINLINE_SWITCHES_TO_CANONICAL_ALLOCATION_DENSITY=true
MAINLINE_H_NEEDED=false
```

No theorem is cross-promoted from the unmerged Work-bmX25 or any unmerged H result.

## 3. Next mainline target

Stage14-4ee should work only on

```text
mu_can = density of primitive slopes carrying at least one canonical
         balanced integer/Gaussian allocation witness,
```

using the exact primitive binary forms

```text
F_-(a,b)=oddpart(ab),
F_+(a,b)=oddpart(a^2+b^2),
gcd(F_-,F_+)=1.
```

All reciprocal-root information is now frozen as a parallel H target and must not be reused as an allocation saving.

## Boundary

```text
STAGE14_4ED=COMPLETE_RECIPROCAL_ROOT_DENSITY_H_GATE_AND_MAINLINE_SWITCH_TO_CANONICAL_ALLOCATION
SECOND_RECIPROCAL_ROOT_LINE_MODULUS_IS_C0=true
INDEPENDENT_SECOND_GROWING_MODULUS_PRODUCED=false
PRIMITIVE_GAUSSIAN_ROOT_CONDITIONAL_DENSITY_THEOREM_PROVED=false
FIXED_POWER_RECIPROCAL_ROOT_DENSITY_DEFICIT_PROVED=false
RECIPROCAL_SUBROUTE_H_NEEDED=true
RECIPROCAL_SUBROUTE_H_TARGET=CanonicalAllocationConditionalPrimitiveGaussianRootDensity
S_ROUTE_H_NEEDED=true
MAINLINE_BLOCKED_WAITING_FOR_H=false
MAINLINE_SWITCHES_TO_CANONICAL_ALLOCATION_DENSITY=true
MAINLINE_H_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=false
NEXT=Stage14-4ee
```
