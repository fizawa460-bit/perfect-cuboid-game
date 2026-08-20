# Stage27-20-r302aq — all gcd strata recombine to the exact quadratic-root projector

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302ap
SOURCE_STAGE=Stage20

R302ap gives, for `Q=q/d`,

```text
R_{d,C}(f)=c_Q(f^2-C)/q.
```

Summing over all divisors `d|q`, equivalently all `Q|q`, uses the exact Ramanujan identity

```text
sum_{Q|q} c_Q(n)
 = q * 1_{q|n}.
```

Hence

```text
sum_{d|q} R_{d,C}(f)
 = 1_{f^2=C (mod q)}.
```

Thus the entire additive-frequency/Gauss apparatus, after exact recombination, is simply the original quadratic-root projector on the residue coordinate `f`.

Let

```text
Root_q(C) = {f mod q : f^2=C (mod q)},
P_C(f)=1_{f in Root_q(C)}.
```

For the original physical residue coefficient `W(f)`, the local arithmetic contribution is exactly

```text
S_C(W)=sum_{f mod q} W(f) P_C(f).
```

With the existing transform convention

```text
W_hat(b)=sum_f W(f)e_q(-bf),
c_b=W_hat(b)/q,
```

Fourier inversion gives the equivalent coefficient-space identity

```text
S_C(W)
 = sum_{b mod q} c_b K_C(b),
K_C(b)=sum_{f in Root_q(C)} e_q(bf).
```

and Parseval gives

```text
sum_{b mod q}|K_C(b)|^2
 = q * #Root_q(C).
```

These are exact finite identities. No Kloosterman, Kuznetsov, large-sieve, or equidistribution estimate has been used.

The benefit is conceptual and operational: the canonical coefficient-specific problem is now visible directly in residue space. Any genuine saving must say that the actual physical coefficient `W` has little mass on the exact root set, or that packets with dangerous root concentration carry little `H_phys^MAIN` mass. Oscillatory transforms may still prove such statements, but they are tools rather than the theorem target itself.

```text
STAGE27_20_R302AQ_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
ALL_GCD_STRATA_RECOMBINE_TO_ROOT_PROJECTOR=true
ROOT_SET_FOURIER_KERNEL_IDENTITY_PROVED=true
ROOT_KERNEL_PARSEVAL_IDENTITY_PROVED=true
ORIGINAL_PHYSICAL_RESIDUE_COEFFICIENT_RESTORED=true
KLOOSTERMAN_THEOREM_CANONICAL_TARGET=false
NEW_FIXED_POWER_SAVING_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
CURRENT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302ar
NEXT_BATCH=Stage27-20-r302-main-batch
```