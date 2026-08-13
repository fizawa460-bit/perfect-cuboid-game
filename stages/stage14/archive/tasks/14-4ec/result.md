# Stage14-4ec — opposite reciprocal Gaussian norm selector

## Status

`COMPLETE_OPPOSITE_RECIPROCAL_TO_PRIMITIVE_GAUSSIAN_NORM_DIVISIBILITY`

Consumes batch-local `Stage14-4eb`, merged `Stage14-s7-69/70` from publication recheck, merged `Stage14-s7-46`, `Stage14-s7-42`, `Stage14-X13`, and merged `Stage14-4ea`. The batch-start theorem boundary remains `e601b1e4224e718eafa67018f964ca40ee607377`; newly merged s7-69/70 are consumed as theorem sources only after their merge to main.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. First reciprocal layer is gone

Stage14-4eb independently proves the same selector elimination now merged as s7-69: after canonical allocation reconstruction,

```text
(D+A)^2-(D-A)^2=4DA
```

is the first reciprocal equation itself, so it is not a live density condition.

Merged X13/s7-42 also make final post-column reverse reconstruction a `B^o(1)` fiber once the opposite reciprocal data are fixed.

Therefore the only live arithmetic condition inside the reciprocal conditional factor is the opposite/second reciprocal common-core root equation.

## 2. Exact Gaussian norm divisibility

Merged s7-46 writes

```text
Q_xi+P_xi = c p,
Q_xi-P_xi = d q,
```

and retains

```text
C | p^2 c^2 + q^2 d^2.
```

Set

```text
X=p c,
Y=q d.
```

The live reciprocal selector is exactly

```text
C | X^2+Y^2.
```

The canonical allocation witness fixes `(p,q)` up to divisor-many `B^o(1)` ambiguity, and merged s7-42 gives only `B^o(1)` opposite quotient candidates `(c,d)` after the outer data are fixed.

```text
SECOND_RECIPROCAL_SELECTOR_IS_GAUSSIAN_NORM_DIVISIBILITY=true
SECOND_RECIPROCAL_CANDIDATE_MULTIPLICITY_PER_ALLOCATION=Bo1
```

## 3. Primitive root packet

Write

```text
h=gcd(X,Y),
X=hX0,
Y=hY0,
gcd(X0,Y0)=1.
```

The fixed-power common-core/common-vector overlap has already been power-saved away on every possible square-root saturation sequence. After the charged `B^o(1)` overlap peel the live selector is

```text
C0 | X0^2+Y0^2,
gcd(C0,X0Y0)=1,
```

with `C0` differing from the physical common core only by subpolynomial support.

```text
PRIMITIVE_SECOND_RECIPROCAL_ROOT_PACKET_DEFINED=true
SECOND_RECIPROCAL_COMMON_GCD_PEEL=Bo1
```

## 4. Local splitting is not a fresh saving

Primewise, for every odd `ell|C0`,

```text
(X0 Y0^(-1))^2 == -1 (mod ell).
```

Thus the primes of `C0` are Gaussian split and the primitive ratio selects a root orientation. These are already-frozen Gaussian support/orientation data in the Stage14 packet and may not be charged again as an independent `1/ell` density loss.

```text
SECOND_RECIPROCAL_PRIME_SUPPORT_GAUSSIAN_SPLIT=true
LOCAL_GAUSSIAN_SPLITTING_RECHARGE_ALLOWED=false
FRESH_LOCAL_CONGRUENCE_POWER_SAVING_PROVED=false
```

Unlike the first reciprocal equation, no identity forces the divisibility `C0 | X0^2+Y0^2` for every canonical allocation witness. Finite candidate multiplicity therefore does not eliminate this Boolean selector.

## 5. Updated density receiver

Define `A_root=1` on a canonical allocation-bearing primitive slope iff at least one charged-once candidate `(C0,X0,Y0)` satisfies the primitive Gaussian norm divisibility above. Then, at the exponent scale,

```text
mu_G = mu_can * mu_root,
```

where `mu_root` is the conditional density of `A_root=1` and the post-root completion is only a `B^o(1)` reconstruction fiber.

```text
RECIPROCAL_CONDITIONAL_DENSITY_REDUCED_TO_ROOT_SELECTOR=true
CANONICAL_ALLOCATION_GAUSSIAN_ROOT_DENSITY_CHAIN_EXACT=true
RECIPROCAL_ROOT_FIXED_POWER_DEFICIT_PROVED=false
```

## Boundary

```text
STAGE14_4EC=COMPLETE_OPPOSITE_RECIPROCAL_TO_PRIMITIVE_GAUSSIAN_NORM_DIVISIBILITY
SECOND_RECIPROCAL_SELECTOR_IS_GAUSSIAN_NORM_DIVISIBILITY=true
PRIMITIVE_SECOND_RECIPROCAL_ROOT_PACKET_DEFINED=true
SECOND_RECIPROCAL_CANDIDATE_MULTIPLICITY_PER_ALLOCATION=Bo1
LOCAL_GAUSSIAN_SPLITTING_RECHARGE_ALLOWED=false
RECIPROCAL_CONDITIONAL_DENSITY_REDUCED_TO_ROOT_SELECTOR=true
CANONICAL_ALLOCATION_GAUSSIAN_ROOT_DENSITY_CHAIN_EXACT=true
RECIPROCAL_ROOT_FIXED_POWER_DEFICIT_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=false
NEXT=Stage14-4ed
```
