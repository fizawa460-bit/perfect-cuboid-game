# Stage14-t122 — finite Gaussian symmetry covers every nonboundary primitive sign orbit

## Status

`COMPLETE_FINITE_GAUSSIAN_SYMMETRY_CANONICAL_CHAMBER_COVERAGE`

Consumes Stage14-t121 on the same batch branch together with merged t89/t91 primitive-cover facts.

For a fixed generic orientation let

```text
W=W_sigma=a*gamma_E*gamma_G(epsilon)=p-i*sigma*q.
```

Stage14-t121 re-exposes the finite unit/conjugation normalization orbit.  The Gaussian units and conjugation generate the usual finite dihedral action on the coordinate pair `(p,q)`:

```text
(p,q), (q,p), (-p,q), (p,-q), ...
```

up to the already fixed `sigma` convention.  The canonical unit/sign convention is a choice of one representative from this finite orbit.  Away from the tie walls, one and only one orbit representative lies in the frozen strict canonical chamber (equivalently any fixed D4 fundamental chamber such as `p>q>0`; changing the named chamber only relabels the finite normalization states).

Hence the only possible failure of finite-orbit sign/canonical coverage occurs on the D4 boundary

```text
p*q*(p^2-q^2)=0.
```

Merged t91 makes the primitive-cover condition automatic on the orientation cube, so every live `W` here satisfies

```text
gcd(p,q)=1.
```

Therefore the boundary is arithmetically tiny:

- if `p*q=0`, primitivity forces the nonzero coordinate to have absolute value `1`, so `N(W)=1`;
- if `p^2=q^2`, primitivity forces `|p|=|q|=1`, so `N(W)=2`.

But

```text
N(W)=N(a)N(gamma_E)N(gamma_G)=k0*m*g.
```

Consequently

```text
D4 boundary
=>
k0*m*g in {1,2}.
```

For every generic scalar norm satisfying

```text
k0*m*g>2,
```

every primitive orientation orbit is nonboundary, and the finite normalization orbit contains a sign/canonical accepted representative.  In particular

```text
k0*m*g>2
=>
g in G_phys(m,e_loc).
```

This is a pointwise chamber-coverage lemma.  It has not yet been pushed through the weighted t120 receiver in this stage, so the batch does not declare the receiver change until the charged-once weighted consequence is recorded next.

No asymptotic prime-distribution theorem is used.

```text
FINITE_GAUSSIAN_NORMALIZATION_ORBIT_IS_D4=true
NONBOUNDARY_D4_ORBIT_HAS_CANONICAL_SIGN_REPRESENTATIVE=true
SIGN_CANONICAL_FAILURE_IMPLIES_D4_BOUNDARY=true
PRIMITIVE_D4_BOUNDARY_NORM_SET={1,2}
D4_BOUNDARY_IMPLIES_K0_M_G_IN_1_OR_2=true
GENERIC_SIGN_SUPPORT_POINTWISE_FULL_FOR_K0_M_G_GT_2=true
RECEIVER_MATERIALLY_CHANGED=false
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
PREFERRED_RECEIVER=SharedUGenericSplitPrimeNormFiniteGaussianSignCanonicalSupportOrSelectedProjectiveClassNearTotalDepletion
NEXT_INTERNAL_TARGET=WeightedGenericNormSupportBoundaryDischarge
NEXT=Stage14-t123
```
