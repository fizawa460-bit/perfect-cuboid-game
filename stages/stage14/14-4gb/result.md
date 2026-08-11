# Stage14-4gb — fixed-E two-sided principal rectangle reduces to conditional physical completion only

## Status

`COMPLETE_FIXED_E_TWO_SIDED_BARE_ARITHMETIC_EXHAUSTION_TO_COMPLETION_ONLY_RECEIVER`

Consumes batch-local `Stage14-4fz/4ga`, merged `Stage14-4fy`, merged `Stage14-s7-105..107`, and merged `Stage14-Work-bxX36`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Correct principal rectangular baseline

On one fixed `E=E0` two-sided principal rectangle write

```text
#D=B^(kappa_D+o(1)),
#V=B^(kappa_V+o(1)),
kappa:=kappa_D+kappa_V>=mu-o(1).
```

Batch-local 4fz proves

```text
#P(D,V)=B^(kappa+o(1)),
```

and batch-local 4ga proves for the actual unitary/coprime bare support

```text
P_prim(D,V)
 ={uv:u in D,v in V,gcd(u,v)=1},
#P_prim(D,V)=B^(kappa+o(1)).                       (1)
```

Thus neither multiplication collisions nor the primitive/unitary restriction creates a positive fixed-power loss from rectangular pair capacity.

```text
FIXED_E_TWO_SIDED_BARE_SUPPORT_EXPONENT=kappa
MULTIPLICATION_COMPRESSION_FIXED_POWER_DEFICIT=0
UNITARY_COPRIME_FIXED_POWER_DEFICIT=0
```

## 2. Define the completion-only accepted support

For `m in P_prim(D,V)`, define

```text
C_phys(m)=1
```

iff at least one primitive representation

```text
m=u*v,
u in D,
v in V,
gcd(u,v)=1
```

satisfies every retained Stage14 physical condition not already forced by the fixed rectangular packet, including

```text
canonical/root-origin/allocation masks,
reverse/post-column completion,
parity/two-primary decorations,
and the frozen physical chart/orientation conditions still attached to the candidate.
```

The number of primitive representations of one `m` is at most `tau(m)=B^o(1)`, so this existential definition introduces no hidden polynomial witness multiplicity.

The physical outer support is exactly

```text
S_phys
 := #{m in P_prim(D,V): C_phys(m)=1}
 = B^(tau_phys+o(1)).                               (2)
```

Define the conditional completion deficit exponent

```text
delta_comp:=kappa-tau_phys>=0.                     (3)
```

Then a surviving heavy fixed-E two-sided cell requires exactly

```text
kappa-delta_comp=tau_phys>=mu.                     (4)
```

```text
FIXED_E_TWO_SIDED_COMPLETION_BOOLEAN_DEFINED=true
FIXED_PRODUCT_PRIMITIVE_WITNESS_FIBER=Bo1
FIXED_E_TWO_SIDED_COMPLETION_DEFICIT_EXPONENT=delta_comp
FIXED_E_TWO_SIDED_SURVIVAL_BUDGET=kappa_minus_delta_comp_ge_mu
```

## 3. Threshold consequences

Equation (4) gives two useful exact regimes.

### Near-threshold rectangular capacity

If

```text
kappa=mu+o(1),
```

then survival forces

```text
delta_comp=o(1).
```

So the conditional physical completion must have exponent-zero deficit on that cell.

### Super-threshold rectangular capacity

If

```text
kappa>=mu+eta
```

for fixed `eta>0`, a positive completion deficit can coexist with survival, but only up to

```text
delta_comp<=kappa-mu.
```

Therefore a future completion theorem must be compared with the **actual capacity headroom `kappa-mu`**, not merely prove some positive saving.

```text
NEAR_THRESHOLD_SURVIVAL_FORCES_COMPLETION_DEFICIT_ZERO_AT_FIXED_POWER=true
SUPERTHRESHOLD_COMPLETION_SAVING_MUST_EXCEED_CAPACITY_HEADROOM=true
```

## 4. Material receiver change

Merged 4fy still had two possible fixed-E two-sided mechanisms:

```text
distinct-product capacity loss
OR
conditional physical lift loss.
```

Batch-local 4fz and 4ga exhaust both bare arithmetic components at fixed-power level. The fixed-E two-sided receiver is now solely

```text
FixedComplementaryDilationTwoSidedPrincipalRectangularConditionalCanonicalReversePhysicalCompletionDeficit
WithCapacityHeadroomKappaMinusMu.
```

The fixed-E primitive endpoint remains its separate one-dimensional completion receiver. The polynomial-E fixed-product and polynomial outer-pair branches remain separate and are not modified here. The existing non-heavy mainline H gates also remain pending.

```text
CURRENT_FIXED_E_TWO_SIDED_RECEIVER=FixedComplementaryDilationTwoSidedPrincipalRectangularConditionalCanonicalReversePhysicalCompletionDeficitWithCapacityHeadroomKappaMinusMu
RECEIVER_MATERIALLY_CHANGED=true
```

## 5. H decision

No new heavy main H is opened yet. The residual object is finally a pure physical-completion receiver, but the Boolean `C_phys(m)` still bundles several Stage14-specific canonical/root-origin/reverse predicates. A clean-room theorem target should be frozen only after the next internal stage opens this Boolean and identifies its minimal arithmetic species.

This agrees with the Work-bxX36 policy: deterministic ambient-capacity and bare arithmetic restrictions are exhausted before spending correlation machinery.

```text
NEW_HEAVY_MAIN_H_NEEDED=false
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
EXISTING_NONHEAVY_MAIN_H_GATES_PENDING=true
WHOLE_MAINLINE_BLOCKED_BY_H=false
NEXT=Stage14-4gc
```

## Boundary

```text
STAGE14_4GB=COMPLETE_FIXED_E_TWO_SIDED_BARE_ARITHMETIC_EXHAUSTION_TO_COMPLETION_ONLY_RECEIVER
FIXED_E_TWO_SIDED_BARE_SUPPORT_EXPONENT=kappa
MULTIPLICATION_COMPRESSION_FIXED_POWER_DEFICIT=0
UNITARY_COPRIME_FIXED_POWER_DEFICIT=0
FIXED_E_TWO_SIDED_SURVIVAL_BUDGET=kappa_minus_delta_comp_ge_mu
CURRENT_FIXED_E_TWO_SIDED_RECEIVER=FixedComplementaryDilationTwoSidedPrincipalRectangularConditionalCanonicalReversePhysicalCompletionDeficitWithCapacityHeadroomKappaMinusMu
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_HEAVY_MAIN_H_NEEDED=false
NEXT=Stage14-4gc
```
