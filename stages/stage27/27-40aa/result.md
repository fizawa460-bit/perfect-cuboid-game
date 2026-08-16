# Stage27-40aa — MAIN-CRT2 fixed-moment and support attack

```text
TASK_ID=Stage27-40aa
OWNER_STAGE=Stage27
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_ONLY
ROUTE_PRIORITY=1
ROUTE_LABEL=MAIN_CRT2
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
ADVANCE_TO_CHECKPOINT50=false
```

## Authorization

Stage27-r401a hostile intermediate audit passed and PR #1026 merged. Its accepted continuation order puts `R401-NEXT-MAIN-CRT2` first. This route remains inside checkpoint40 and does not authorize checkpoint50.

The target population remains the primitive canonical exactly-two-face integral-space population under the same Euclidean cutoff `R<=B`.

## Fixed-moment exponent-equivalence

For one principal primitive rectangle and fixed supported core label, let `N_rec(u,v)` be the number of accepted reciprocal witnesses and `T_rec={(u,v):N_rec(u,v)>0}`. The frozen Stage14 interface gives uniformly `N_rec(u,v)<=B^{o(1)}`.

For every fixed integer `r>=1`, put

\[
S_r=\sum_{(u,v)}N_{\rm rec}(u,v)^r.
\]

On support `N_rec>=1`, hence

\[
\boxed{\#T_{\rm rec}\le S_r\le B^{o(1)}\#T_{\rm rec}}.
\]

Thus every fixed witness moment has the same fixed-power exponent as support. Replacing the first moment by a second or higher fixed moment cannot by itself manufacture a polynomial saving.

```text
FIXED_WITNESS_MOMENT_EXPONENT_EQUIVALENCE_PROVED=true
SECOND_MOMENT_ALONE_CAN_CREATE_FIXED_POWER_SUPPORT_DEFICIT=false
FIXED_HIGHER_MOMENT_ALONE_CAN_CREATE_FIXED_POWER_SUPPORT_DEFICIT=false
```

## Remaining MAIN gate

The exponent-changing quantity is the critical-wall support mass for simultaneous nested two-level CRT solvability. The unresolved system retains

\[
t_p,t_q\mid m^\circ,\qquad f\mid t_pt_q,
\]

and the two reversible quadratic root congruences

\[
G_-f^2\equiv-G_+t_pt_q\pmod{2U},\qquad
G_-f^2\equiv G_+t_pt_q\pmod{2V},
\]

with primitive `(u,v)`, principal-cell geometry, and all frozen filters retained. No independence is assumed.

A genuine MAIN crossing must prove a fixed-power support deficit on the balanced wall, uniformly per retained cell or with a same-measure chargeable exceptional set. Any fixed-moment theorem is useful only insofar as it proves that support deficit.

## Outcome

No strict global sub-square-root theorem is obtained in aa. The strongest global upper remains

\[
\boxed{N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}}.
\]

But aa closes fixed witness-moment reweighting as an exponent source and narrows MAIN to support mass itself. After fresh audit, the next independent ranked route is `27-40ab = T-AVG-ADAPTER`, unless audit exposes a genuine unused MAIN support theorem.

```text
CURRENT_GLOBAL_MU=1/2
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
MAIN_CRT2_ATTACK_EXECUTED=true
MAIN_FIXED_MOMENT_REWEIGHTING_ROUTE_CLOSED=true
MAIN_SUPPORT_DEFICIT_GATE_OPEN=true
MAIN_SUPPORT_DEFICIT_PROVED=false
FINITE_DATA_USED_AS_PROOF=false
INDEPENDENCE_PRODUCT_CLAIMED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=40
NEXT_DERIVED_ROUTE=27-40ab
MERGE_ALLOWED=false
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
NEXT_EXPECTED_COMMAND=Stage27-audit
```
