# Stage14-4fr — polynomial complementary dilation: outer physical support to bare shadows and conditional completion ledgers

## Status

`COMPLETE_POLYNOMIAL_E_PHYSICAL_SUPPORT_TO_BARE_SHADOWS_AND_COMPLETION_LEDGERS`

Consumes batch-local `Stage14-4fq`, merged `Stage14-4fo/4fp`, merged `Stage14-s7-98`, and merged `Stage14-Work-buX33`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Polynomial-E outer-pair receiver

On the branch

```text
E=B^(epsilon+o(1)), epsilon>0,
n=E*m,
```

merged 4fo/4fp defines

```text
A_poly(E,m)=1
```

iff there exists

```text
u || m,
u in U_phys(E,m),
```

with the exact physical Boolean

```text
k(E,m,u)=m_E(E)*m_cpl(E*m,u,m/u,E)=1.
```

A surviving heavy packet requires

```text
S_phys,poly
 := #{(E,m):A_poly(E,m)=1}
 >= B^(mu-o(1)).
```

## 2. Bare polynomial-E shadow

Retain the complementary-dilation local mask `m_E(E)` and the exact transported unitary-divisor interval, but remove only the canonical/reverse completion Boolean. Define

```text
B_poly(E,m)
 := m_E(E)
    * 1{exists u || m with u in U_phys(E,m)}.
```

Then pointwise

```text
A_poly(E,m) <= B_poly(E,m).
```

Let

```text
S_bare,poly:=sum_{E,m} B_poly(E,m).
```

Survival implies

```text
S_bare,poly >= B^(mu-o(1)).
```

The local `E` mask is retained because it is part of the charged physical outer family.  Only the unresolved canonical/reverse completion requirement has been relaxed.

```text
POLYNOMIAL_E_BARE_SHADOW_DEFINED=true
POLYNOMIAL_E_LOCAL_MASK_RETAINED_IN_BARE_SHADOW=true
POLYNOMIAL_E_PHYSICAL_SUPPORT_SUBSET_BARE_SHADOW=true
```

## 3. Consume the merged s7-98 primitive-product scale split

Merged s7-98 is a same-packet refinement and is consumed without recharging it.

### Branch P0: `m=B^o(1)`

The exact primitive product and one unitary orientation may be frozen at `B^o(1)` cost:

```text
m=m0,
u=u0 || m0.
```

The bare support is then one-dimensional in the polynomial coordinate `E`:

```text
B_P0(E)
 := m_E(E)
    * 1{u0 in U_phys(E,m0)}.
```

The physical support further requires

```text
c_P0(E)
 := m_cpl(E*m0,u0,m0/u0,E)=1.
```

Hence

```text
A_P0(E)=B_P0(E)*c_P0(E).
```

This is an exact conjunction, not an independence factorization.

### Branch P+: `m=B^(kappa+o(1))`, `kappa>0`

Both `E` and `m` remain polynomial.  The bare outer-pair selector is exactly

```text
B_P+(E,m)=B_poly(E,m),
```

and the physical selector is `A_poly(E,m)`.

```text
POLYNOMIAL_E_SUBPOLYNOMIAL_M_OUTER_COORDINATE=E
POLYNOMIAL_E_POLYNOMIAL_M_OUTER_COORDINATE=(E,m)
S7_98_SCALE_SPLIT_RECHARGED=false
```

## 4. Conditional completion exponent ledgers

For P0 write

```text
# {E:B_P0(E)=1}=B^(sigma_0+o(1)),
# {E:A_P0(E)=1}=B^(tau_0+o(1)),
delta_0:=sigma_0-tau_0>=0.
```

For P+ write

```text
# {(E,m):B_P+(E,m)=1}=B^(sigma_++o(1)),
# {(E,m):A_poly(E,m)=1}=B^(tau_++o(1)),
delta_+:=sigma_+-tau_+>=0.
```

A surviving branch satisfies respectively

```text
sigma_0-delta_0=tau_0>=mu
```

or

```text
sigma_+-delta_+=tau_+>=mu.
```

Thus, exactly as in 4fq, the obstruction splits into

```text
bare-shadow support exponent
versus
conditional canonical/reverse completion deficit exponent.
```

No exponent-zero conditional density is forced unless the corresponding bare-shadow exponent is first shown to be `mu+o(1)`.

```text
POLYNOMIAL_E_P0_SURVIVAL_BUDGET=sigma_0_minus_delta_0_ge_mu
POLYNOMIAL_E_PPLUS_SURVIVAL_BUDGET=sigma_plus_minus_delta_plus_ge_mu
POLYNOMIAL_E_EXPONENT_ZERO_COMPLETION_DENSITY_FORCED=false
```

## 5. H decision

The same two-level arithmetic budget now exists on every complementary-dilation branch.  The next stage can freeze the minimal heavy receiver globally and state exactly which part q14/Ford can test and which part remains a Stage14-specific physical-completion problem.

```text
RECEIVER_MATERIALLY_CHANGED=false
NEW_HEAVY_MAIN_H_NEEDED=false
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
NEXT=Stage14-4fs
```

## Boundary

```text
STAGE14_4FR=COMPLETE_POLYNOMIAL_E_PHYSICAL_SUPPORT_TO_BARE_SHADOWS_AND_COMPLETION_LEDGERS
POLYNOMIAL_E_BARE_SHADOW_DEFINED=true
POLYNOMIAL_E_LOCAL_MASK_RETAINED_IN_BARE_SHADOW=true
POLYNOMIAL_E_SUBPOLYNOMIAL_M_OUTER_COORDINATE=E
POLYNOMIAL_E_POLYNOMIAL_M_OUTER_COORDINATE=(E,m)
POLYNOMIAL_E_P0_SURVIVAL_BUDGET=sigma_0_minus_delta_0_ge_mu
POLYNOMIAL_E_PPLUS_SURVIVAL_BUDGET=sigma_plus_minus_delta_plus_ge_mu
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_HEAVY_MAIN_H_NEEDED=false
RECEIVER_MATERIALLY_CHANGED=false
NEXT=Stage14-4fs
```
