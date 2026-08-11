# Stage14-tH28 immutable target — canonical-LPF primitive norm-form projected physical support

Source snapshot: Stage14-t108 on branch `agent/stage14-t-batch-t106-108-q-support-decomposition` at the commit containing this file. This target is immutable once published; later t stages must not rewrite it.

Audit object:

```text
CanonicalLPFPrimitiveSumOfTwoSquaresProjectedPhysicalSupportSieveOrDispersion
```

Determine whether existing literature supplies a uniform fixed-power saving for the projected support of tuples satisfying

```text
Q=ell*(u^2+v^2),
gcd(u,v)=1,
ell=LPF(Q),
v_ell(Q)=1,
all odd p|Q => p==1 mod 4,
ell^2>4B,
ell^2>2*h*k0*Q,
h*k0*Q<=2B,
```

with fixed-U packet data and all surviving physical linear/congruence/orientation masks retained. The fixed norm-`k0` Gaussian factor converts cover coordinates to fixed integral linear forms in `(u,v)`; short-cover archimedean bounds are automatic from the strong gap and must not be charged again.

Required output:

```text
DIRECT_THEOREM_APPLICABLE=true|false
UNIFORM_FIXED_POWER_SAVING_PROVED=true|false
MASK_TRANSFER_COST=...
FIRST_NONABSORBABLE_MASK_OR_HYPOTHESIS=...
FULL_FIXED_U_UNIFORMITY=true|false
WHOLE_FAMILY_CROSS_PROMOTION_PROVED=false unless separately established
```

If no direct theorem applies, identify the closest theorem family and the exact missing adapter. Do not weaken the largest-prime condition, primitivity, strong gap, or physical mask family to claim applicability.
