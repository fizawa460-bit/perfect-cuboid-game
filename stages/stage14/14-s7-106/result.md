# Stage14-s7-106 — provenance audit of the fixed-product E-local mask

## Status

`COMPLETE_FIXED_PRODUCT_E_LOCAL_PROVENANCE_AUDIT_AND_SINGLE_COMPLETION_BOOLEAN_REDUCTION`

Consumes batch-local `Stage14-s7-105`, merged `Stage14-s7-93/104`, merged `Stage14-4fk/4fr`, and merged `Stage14-Work-bwX35`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Reopen exactly what was proved E-local

Merged s7-93 gives the exact pullback

```text
w_ratio(n,u,v,E)
 = 1_{gcd(sqf(E),K_Z)=1}
   * w_res(n,u,v,E),
```

and explicitly places every remaining fixed-coefficient allocation, primitive/orientation, root-origin, parity/two-primary, canonical and reverse-completion condition inside `w_res`.

Merged 4fk later introduces the notation `m_E(E)` only for predicates whose E-only dependence has already been proved, and specifically retains the same squarefree-kernel coprimality.  It forbids moving any other mask into `m_E` without merged provenance.

No merged source through s7-104 names or proves a second independent E-only physical predicate on the fixed-product branch.

```text
NAMED_PROVED_E_ONLY_MASK_COUNT=1
NAMED_PROVED_E_ONLY_MASK=gcd_sqf_E_KZ_equals_1
UNNAMED_RESIDUAL_E_ONLY_PREDICATE_MAY_BE_CHARGED=false
```

## 2. The s7-104 residual E-local symbol is bookkeeping, not an additional arithmetic mechanism

Merged s7-104 conservatively wrote

```text
m_E(E)=m_K(E)*m_E^res(E)
```

with

```text
m_K(E)=1_{gcd(sqf(E),K_Z)=1}.
```

The symbol `m_E^res` did not come with a named predicate or a proof that any remaining physical condition is a function of E alone.  Therefore it cannot be assigned an independent support exponent or an independent density loss.

On the fixed primitive-product cell `(m0,u0,v0)`, define instead the exact single residual physical Boolean

```text
C_fix^*(E)
 := w_res(E*m0,u0,v0,E).
```

Then the physical selector is exactly

```text
A_fix(E)
 = 1_{E in I_E}
   * 1_{gcd(sqf(E),K_Z)=1}
   * C_fix^*(E).
```

This is only a provenance-correct regrouping of the same conjunction.  It does not assert that the remaining conditions are independent of E; on the contrary, all their E-dependence remains inside `C_fix^*`.

```text
S7_104_RESIDUAL_E_LOCAL_SYMBOL_RECLASSIFIED_AS_UNPROVEN_FACTOR=true
FIXED_PRODUCT_SINGLE_RESIDUAL_PHYSICAL_BOOLEAN_DEFINED=true
FIXED_PRODUCT_PHYSICAL_SELECTOR_CHANGED=false
FIXED_PRODUCT_MASK_INDEPENDENCE_ASSUMED=false
```

## 3. Fixed-power ledger after the known E-only mask is discharged

Merged s7-104 already proves that on a polynomial-length E interval

```text
1_{gcd(sqf(E),K_Z)=1}
```

has zero fixed-power deficit, using the subset `gcd(E,rad(K_Z))=1` and the standard `phi(Q)/Q=B^(-o(1))` bound for polynomial `Q`.

Hence any fixed-power loss on the fixed-product scalar realization is carried entirely by the support of

```text
C_fix^*(E)=1
```

inside the already-charged scalar interval, not by a separately chargeable unnamed E-local factor.

Write

```text
#I_E = B^(lambda_E+o(1)),
#{E in I_E : A_fix(E)=1}=B^(tau_fix+o(1)).
```

Heavy survival requires `tau_fix>=mu`.  The only live Stage14-specific mechanism on this realization is therefore one-dimensional physical-completion support.

```text
FIXED_PRODUCT_KNOWN_E_LOCAL_FIXED_POWER_DEFICIT=0
FIXED_PRODUCT_INDEPENDENT_RESIDUAL_E_LOCAL_DEFICIT_DEFINED=false
FIXED_PRODUCT_ONE_DIMENSIONAL_PHYSICAL_COMPLETION_SUPPORT_RETAINS=true
```

## 4. Receiver/H decision

This stage removes an unsupported decomposition from the ledger but does not change the accepted set and does not yet alter the other live branches.  The next step tests whether the polynomial `(E,m)` unitary branch also admits a legal ordinary-divisor absolute upper envelope without freezing E.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_106_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_106=COMPLETE_FIXED_PRODUCT_E_LOCAL_PROVENANCE_AUDIT_AND_SINGLE_COMPLETION_BOOLEAN_REDUCTION
NAMED_PROVED_E_ONLY_MASK_COUNT=1
S7_104_RESIDUAL_E_LOCAL_SYMBOL_RECLASSIFIED_AS_UNPROVEN_FACTOR=true
FIXED_PRODUCT_SINGLE_RESIDUAL_PHYSICAL_BOOLEAN_DEFINED=true
FIXED_PRODUCT_ONE_DIMENSIONAL_PHYSICAL_COMPLETION_SUPPORT_RETAINS=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_106_NEW_AUXILIARY_H_NEEDED=false
RECEIVER_MATERIALLY_CHANGED=false
NEXT=Stage14-s7-107
```