# Stage14-t109 — factor the fixed-cofactor ray physical mask

## Status

`COMPLETE_PRIMITIVE_COFACTOR_RAY_PHYSICAL_MASK_FACTORIZATION`

Consumes merged Stage14-t108, merged Stage14-tH28, and the exact selector opening from merged Stage14-t90.  The tH28 negative verdict is theorem-source input; no positive sieve saving is imported.

Fix one live fixed-U packet

```text
(U,epsilon,k,h,kappa,beta,eta),
k0=eta*k,
```

one allowed norm-`k0` Gaussian factor `a`, one exceptional/unit/orientation label, and one primitive cofactor

```text
gamma=u+i*v,
n=N(gamma)=u^2+v^2,
gcd(u,v)=1.
```

Vary only the dominant split prime `ell` and its canonical Gaussian factor `pi_ell`, with

```text
Q=ell*n,
ell > 2*h*k0*n,
ell > 2*sqrt(B),
h*k0*ell*n<=2B.
```

Merged tH28 proves that under this strong gap the conditions `ell=LPF(Q)` and `v_ell(Q)=1` are automatic, so they are not charged again.

Merged t90 opens the exact physical selector as

```text
P_prim(a,gamma)
P_tag(U,kappa,beta;a,gamma)
P_cell(U;a,gamma)
P_proj(d;a,gamma,pi_ell)
P_sign(U;a,gamma).
```

For fixed `(a,gamma)` the primitive, denominator-tag, four-cell/angular and sign/positivity factors are independent of `ell`.  The only nonautomatic moving prime-side mask is the endpoint projective condition

```text
[gamma]*[a]*[pi_ell]=1 in
G(d)=(Z[i]/dZ[i])^x/(Z/dZ)^x,
```

with merged `d=B^o(1)` and `gcd(d,ell*k0*n)=1`.

Define the ell-independent core

```text
C_U(a,gamma)
 := P_prim P_tag P_cell P_sign in {0,1}
```

and, when `C_U(a,gamma)=1`, the selected projective target

```text
c_U(a,gamma):=([gamma][a])^(-1) in G(d).
```

Then along the fixed primitive cofactor ray the full physical predicate factors exactly as

```text
P_phys(a,gamma;ell)
 = C_U(a,gamma)
   * 1_{[pi_ell]=c_U(a,gamma)}.
```

Thus a dead ray is detected entirely by `C_U=0`; on a live core ray, the persistent-ray question is exactly prime occupancy of one packet-selected projective class in the physical interval

```text
I_B(n)=
(max(2*sqrt(B),2*h*k0*n), 2B/(h*k0*n)].
```

No lower bound and no fixed-power saving is asserted.

```text
TH28_NEGATIVE_VERDICT_CONSUMED=true
T109_MAY_CONSUME_TH28_FIXED_POWER_SAVING=false
RAY_FIXED_GAMMA_PRIME_DEPENDENCE_ONLY_PROJECTIVE_SELECTOR=true
RAY_PHYSICAL_PREDICATE_FACTORS_EXACTLY=true
RAY_ELL_INDEPENDENT_PHYSICAL_CORE_DEFINED=true
RAY_ENDPOINT_TARGET_CLASS_EXACT=true
CANONICAL_LPF_RECHARGE_FORBIDDEN=true
PERSISTENT_RAY_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
PREFERRED_RECEIVER=SharedUPrimitiveCofactorRayProjectiveGaussianPrimeClassOccupancy
NEXT=Stage14-t110
```
