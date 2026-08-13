# Stage14-s7-71 — primitive Gaussian root-density boundary and external theorem gate

## Status

`COMPLETE_PRIMITIVE_GAUSSIAN_ROOT_DENSITY_BOUNDARY_AND_SH71_GATE`

Consumes batch-local `Stage14-s7-69/70`, merged `Stage14-s7-68`, merged `Stage14-Work-blX24`, merged `Stage14-s7-42/46/60`, and latest merged main at batch start.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Entering explicit selector

Stage14-s7-70 reduces the reciprocal conditional factor to the Boolean event that at least one finite-fiber opposite-reciprocal candidate satisfies

```text
C0 | X0^2+Y0^2,
gcd(X0,Y0)=1,
gcd(C0,X0Y0)=1,
```

on the canonical balanced integer/Gaussian allocation background. Every local prime of `C0` is already an eligible Gaussian split prime, and its root orientation is already part of the frozen physical Gaussian data.

The question is whether this explicit condition can still be reduced internally by spacing, divisor switching, or a new elementary modulus.

## 2. No new modulus can be charged from the same root condition

The congruence itself is equivalent primewise to

```text
X0 == i_C Y0 (mod C0)
```

for one root `i_C^2==-1 (mod C0)` assembled from the frozen local Gaussian orientations, up to `B^o(1)` unit/2-primary decorations.

Thus the only modulus visible in the second reciprocal selector is `C0` itself. There is no second coprime growing modulus produced by the canonical allocation substitution. Reusing the same `C0` root line once to define the Gaussian orientation and again as an independent spacing gain would double charge the same arithmetic condition.

```text
SECOND_RECIPROCAL_ROOT_LINE_MODULUS_IS_C0=true
INDEPENDENT_SECOND_GROWING_MODULUS_PRODUCED=false
ROOT_LINE_DOUBLE_CHARGE_ALLOWED=false
```

## 3. Divisor switching is only a reparametrization

The candidate variables have finite-fiber decompositions

```text
X0=p*c / h,
Y0=q*d / h,
```

with `(p,q)` drawn from the canonical k-agreement allocation and `(c,d)` from the opposite signed quotient candidate set. Switching between `(p,q,c,d)` and `(X0,Y0)` changes multiplicity only by divisor-many `B^o(1)` factors already charged by merged s7-46/s7-42.

Therefore a divisor switch does not expose a new polynomial coordinate or a new independent density factor.

```text
SECOND_RECIPROCAL_DIVISOR_SWITCH_FIBER=Bo1
FRESH_DIVISOR_SWITCH_POWER_SAVING_PROVED=false
```

## 4. Pointwise root counting is insufficient

For a fixed modulus `C0` and a fixed root orientation, the primitive congruence line can have full exponent relative to a positive-width box when the box dimensions dominate `C0`; conversely when `C0` is large it gives spacing already represented by the existing common-core/root-line ledger. Neither regime yields a new uniform fixed-power deficit without averaging the physical candidate distribution against `C0`.

The canonical background also couples `C0`, `(p,q)`, `(c,d)`, and the primitive slope through the original complementary-square and allocation equations. Treating those quantities as independent random variables is not legal.

```text
POINTWISE_ROOT_LINE_COUNT_UNIFORMLY_CLOSES_RECEIVER=false
INDEPENDENCE_OF_C0_AND_RECIPROCAL_CANDIDATES_ASSUMED=false
```

## 5. Exact theorem-ready density target

Let `Omega_can(B)` be the canonical allocation-bearing primitive-slope family from s7-68. For each `omega in Omega_can(B)`, let `R(omega)` be its charged-once `B^o(1)` set of primitive opposite-reciprocal candidates `(C0,X0,Y0)` after all frozen endpoint, 2-primary, root-orientation, chart, range, and allocation masks are retained.

Define

```text
A_root(omega)=1
```

iff there exists `(C0,X0,Y0) in R(omega)` such that

```text
C0 | X0^2+Y0^2.
```

The needed theorem is a uniform fixed-power density estimate

```text
# {omega in Omega_can(B): A_root(omega)=1}
 << |Omega_can(B)| * B^(-delta+o(1))
```

for some fixed `delta>0`, or an equivalent incidence/dispersion bound strong enough to imply it, under all physical masks and the actual quantifier order.

No merged theorem supplies this estimate.

```text
PRIMITIVE_GAUSSIAN_ROOT_CONDITIONAL_DENSITY_THEOREM_PROVED=false
FIXED_POWER_RECIPROCAL_ROOT_DENSITY_DEFICIT_PROVED=false
```

## 6. Why an external H is now necessary

The internal elementary reductions are exhausted:

```text
first reciprocal equation: reconstructed identity;
post-column completion: B^o(1) finite fiber;
second reciprocal local splitting: already-frozen Gaussian support;
second reciprocal root modulus: no independent second modulus;
divisor switch: B^o(1) reparametrization.
```

What remains is genuinely an averaged density/dispersion problem for a Gaussian root congruence whose modulus and candidate vectors are correlated through canonical physical allocation. This is now theorem-shaped and cannot be advanced responsibly by another internal algebraic rewrite.

Therefore open an auxiliary theorem audit:

```text
Stage14-sH71
```

Target:

```text
CanonicalAllocationConditionalPrimitiveGaussianRootDensity
```

Required theorem contract:

```text
background:
  primitive slopes of height B^(1/4+o(1));
  fixed subpolynomial mover prime/root/chart;
  canonical balanced integer/Gaussian allocation witness;

candidate fiber:
  B^o(1) primitive triples (C0,X0,Y0) per slope;
  gcd(X0,Y0)=1;
  gcd(C0,X0Y0)=1;
  local primes of C0 Gaussian split with frozen root orientation;

selector:
  C0 | X0^2+Y0^2;

must retain:
  all dyadic/range/angular masks,
  squarefree/coprime allocation masks,
  actual C0-candidate correlation,
  charged-once quantifier order;

wanted:
  uniform fixed delta>0 density saving,
  or a rigorous no-go/counterexample showing full exponent is possible.
```

Candidate theorem classes to audit include Gaussian/Kloosterman dispersion, large sieve for roots of `-1`, bilinear congruence incidence, and divisor-correlated norm-form sieve, but none may be cross-promoted without an exact adapter.

```text
S7_71_NEW_AUXILIARY_H_NEEDED=true
S7_71_AUXILIARY_H_TARGET=CanonicalAllocationConditionalPrimitiveGaussianRootDensity
S_ROUTE_BLOCKED_WAITING_FOR_H=true
```

## 7. Material receiver boundary

The outer global decomposition remains

```text
mu_G=mu_can*mu_recip,
```

but `mu_recip` is no longer opaque: it has become one explicit theorem-ready Gaussian root density. That is a material receiver change and simultaneously an external-lemma gate.

```text
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_S_RECEIVER=PrimitiveCoprimeBinaryFormsCanonicalBalancedIntegerGaussianAllocationDensity_x_ConditionalPrimitiveGaussianRootDensity
```

The canonical theorem remains `1/2`; no strict sub-square-root saving is claimed.

## Boundary

```text
STAGE14_S7_71=COMPLETE_PRIMITIVE_GAUSSIAN_ROOT_DENSITY_BOUNDARY_AND_SH71_GATE
SECOND_RECIPROCAL_ROOT_LINE_MODULUS_IS_C0=true
INDEPENDENT_SECOND_GROWING_MODULUS_PRODUCED=false
FRESH_DIVISOR_SWITCH_POWER_SAVING_PROVED=false
PRIMITIVE_GAUSSIAN_ROOT_CONDITIONAL_DENSITY_THEOREM_PROVED=false
FIXED_POWER_RECIPROCAL_ROOT_DENSITY_DEFICIT_PROVED=false
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_71_NEW_AUXILIARY_H_NEEDED=true
S7_71_AUXILIARY_H_TARGET=CanonicalAllocationConditionalPrimitiveGaussianRootDensity
S_ROUTE_BLOCKED_WAITING_FOR_H=true
NEXT=Stage14-sH71
```
