# Stage14-4ef — single-side ledger no-go and correlated allocation-density gate

## Status

`COMPLETE_SINGLE_SIDE_ALLOCATION_LEDGER_NOGO_AND_CORRELATED_INTEGER_GAUSSIAN_DENSITY_GATE`

Consumes batch-local `Stage14-4ee`, merged `Stage14-4ea`, merged `Stage14-s7-47`, merged `Stage14-s7-65..68`, and the canonical theta-quarter scale `H=B^(1/4+o(1))`. The reciprocal-root branch remains delegated to sH71 and is not reused here.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Fixed-type allocation incidence

Stage14-4ee freezes one `B^o(1)` canonical allocation type and leaves live divisor values

```text
d_a | a,
d_b | b,
d_+ | a^2+b^2,
```

inside prescribed physical dyadic/balanced windows, with

```text
gcd(a,b)=1,
0<a<b,
a,b=B^(1/4+o(1)).
```

All cross-sign coprimality and Gaussian conjugate-orientation bookkeeping is already charged.

## 2. Minus-side divisor ledger is exponent-neutral

Let

```text
H=B^(1/4+o(1)),
d_a ~ D_a,
d_b ~ D_b,
D_a,D_b <= H*B^o(1).
```

Ignoring physical filters can only enlarge the count. There are at most `O(D_a D_b)` dyadic divisor-value choices. For fixed `(d_a,d_b)`, the number of pairs in an `H x H` box satisfying

```text
d_a|a,
d_b|b
```

is at most

```text
(H/D_a+1)(H/D_b+1).
```

Summing over the dyadic divisor values gives

```text
O(H^2 + H D_a + H D_b + D_a D_b)=H^2 B^o(1),
```

because the physical divisor windows have `D_a,D_b<=H B^o(1)`.

Thus choosing and imposing the two canonical minus divisors consumes exactly the same exponent as the ambient primitive pair family; no fixed-power deficit follows from the minus allocation alone.

```text
MINUS_CANONICAL_DIVISOR_LEDGER_EXPONENT_NEUTRAL=true
MINUS_ALLOCATION_ALONE_FIXED_POWER_SAVING=false
```

## 3. Plus Gaussian divisor/root-line ledger is also exponent-neutral

Let

```text
d_+ ~ D_+,
D_+<=H*B^o(1)
```

in the physical balanced plus-cell window. Since `d_+|a^2+b^2` and `gcd(a,b)=1`, every odd prime of `d_+` is `1 mod 4`; the number of roots of `-1 mod d_+` is `2^omega(d_+)=B^o(1)` on the squarefree physical support.

For fixed `d_+` and one root `i`, the congruence

```text
a == i b (mod d_+)
```

has at most

```text
O(H^2/D_+ + H)
```

pairs in an `H x H` box. Summing over `O(D_+)` dyadic moduli and `B^o(1)` root labels gives

```text
B^o(1) * (H^2 + D_+ H)
 = H^2 B^o(1)
```

because `D_+<=H B^o(1)`.

Therefore the plus balanced Gaussian divisor/root-line condition by itself also reproduces the ambient exponent `1/2`. This is the forward-ledger form of the merged statement that generic balanced split existence and already-charged Gaussian orientation do not yield a fresh saving.

```text
PLUS_GAUSSIAN_DIVISOR_ROOT_LEDGER_EXPONENT_NEUTRAL=true
PLUS_ALLOCATION_ALONE_FIXED_POWER_SAVING=false
ROOT_ORIENTATION_RECHARGE_ALLOWED=false
```

## 4. Only simultaneous integer/Gaussian divisor correlation remains

Write

```text
a=d_a a_1,
b=d_b b_1.
```

Because merged s7-65 gives

```text
gcd(a^2+b^2,ab)=1,
```

every plus divisor `d_+` is coprime to `d_a d_b a_1 b_1`. The simultaneous incidence therefore contains the exact primitive congruence

```text
d_+ | d_a^2 a_1^2 + d_b^2 b_1^2,
```

or equivalently, for the induced Gaussian root,

```text
d_a a_1 == i_{d_+} d_b b_1 (mod d_+),
i_{d_+}^2 == -1 (mod d_+).
```

The separate minus and plus ledgers each have full ambient exponent. Hence any strict saving for `mu_can` must use their **simultaneous correlation on the same primitive pair**, together with the retained balanced/squarefree/smooth-rough physical masks. Multiplying the two separate ledgers as if independent is illegal.

```text
SEPARATE_MINUS_PLUS_ALLOCATION_DENSITIES_INDEPENDENT=false
ONLY_SIMULTANEOUS_INTEGER_GAUSSIAN_DIVISOR_CORRELATION_CAN_SAVE=true
```

## 5. Theorem-ready allocation-density target

Define the target

```text
CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity
```

on one frozen allocation type by the existence of `(d_a,d_b,d_+)` satisfying

```text
d_a|a,
d_b|b,
d_+|a^2+b^2,
```

in their physical windows and support classes, with all original primitive/range/squarefree/coprime/smooth-rough masks retained.

A theorem closing this factor would prove for some fixed `delta>0`

```text
# {primitive (a,b) in the frozen background: A_can(a,b)=1}
 << H^2 * B^(-delta+o(1)).
```

Equivalently it may prove an incidence/dispersion estimate strong enough to give a fixed-power deficit for `mu_can`, or a rigorous no-go/counterexample showing that full exponent is compatible with the full physical masks.

No merged theorem supplies such an estimate, and the elementary one-side ledgers above exhaust the immediate spacing/divisor-count reductions.

```text
CANONICAL_INTEGER_GAUSSIAN_CORRELATION_DENSITY_THEOREM_PROVED=false
CANONICAL_ALLOCATION_FIXED_POWER_DEFICIT_PROVED=false
```

## 6. H decision after five-stage batch

The reciprocal factor has the already-frozen auxiliary target `Stage14-sH71`. The allocation factor has now independently reached a theorem-ready correlated binary-form divisor-density target.

Therefore after completing the requested five substantive stages, the mainline has no further honest elementary rewrite that would avoid a theorem audit on at least one of these two factors.

Freeze the new mainline auxiliary target as

```text
CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity
```

with contract:

```text
background: primitive coprime (a,b), height B^(1/4+o(1)), frozen root/chart/allocation type;
live divisors: d_a|a, d_b|b, d_+|a^2+b^2 in prescribed physical windows;
retain: squarefree/coprime, smooth/rough, dyadic/range/angular and charged-once masks;
wanted: uniform fixed delta>0 density saving or rigorous full-exponent no-go.
```

```text
MAINLINE_H_NEEDED=true
MAINLINE_H_TARGET=CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity
RECIPROCAL_SUBROUTE_H_NEEDED=true
RECIPROCAL_SUBROUTE_H_TARGET=CanonicalAllocationConditionalPrimitiveGaussianRootDensity
NEXT_H_NEEDED=true
```

## Boundary

```text
STAGE14_4EF=COMPLETE_SINGLE_SIDE_ALLOCATION_LEDGER_NOGO_AND_CORRELATED_INTEGER_GAUSSIAN_DENSITY_GATE
MINUS_CANONICAL_DIVISOR_LEDGER_EXPONENT_NEUTRAL=true
PLUS_GAUSSIAN_DIVISOR_ROOT_LEDGER_EXPONENT_NEUTRAL=true
MINUS_ALLOCATION_ALONE_FIXED_POWER_SAVING=false
PLUS_ALLOCATION_ALONE_FIXED_POWER_SAVING=false
SEPARATE_MINUS_PLUS_ALLOCATION_DENSITIES_INDEPENDENT=false
ONLY_SIMULTANEOUS_INTEGER_GAUSSIAN_DIVISOR_CORRELATION_CAN_SAVE=true
CANONICAL_INTEGER_GAUSSIAN_CORRELATION_DENSITY_THEOREM_PROVED=false
CANONICAL_ALLOCATION_FIXED_POWER_DEFICIT_PROVED=false
CURRENT_GLOBAL_RECEIVER=CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity_x_ConditionalPrimitiveGaussianRootDensity
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=true
MAINLINE_H_TARGET=CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity
RECIPROCAL_SUBROUTE_H_NEEDED=true
RECIPROCAL_SUBROUTE_H_TARGET=CanonicalAllocationConditionalPrimitiveGaussianRootDensity
NEXT_H_NEEDED=true
NEXT=auxiliary_theorem_audits
```
