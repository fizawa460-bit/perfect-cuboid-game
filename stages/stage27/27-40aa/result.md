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

## 1. Exact MAIN witness interface

Stage14-4gg/4gh freezes, for one principal primitive rectangle and one fixed `K_*`-supported core label,

\[
t_p\mid m^\circ,\qquad t_q\mid m^\circ,
\qquad N=t_pt_q,
\qquad f\mid N,
\]

with the two reversible quadratic root congruences

\[
G_-f^2\equiv-G_+N\pmod{2U},
\qquad
G_-f^2\equiv G_+N\pmod{2V}.
\]

Let `Omega_rec(u,v)` be the accepted reciprocal witness set and

\[
N_{\rm rec}(u,v)=\#\Omega_{\rm rec}(u,v).
\]

The merged Stage14 interface proves uniformly

\[
0\le N_{\rm rec}(u,v)\le B^{o(1)}.
\]

The reciprocal support is

\[
T_{\rm rec}=\{(u,v):N_{\rm rec}(u,v)>0\}.
\]

## 2. Fixed-moment exponent-equivalence lemma

For every fixed integer `r>=1`, define

\[
S_r=\sum_{(u,v)\in R_{\rm prim}}N_{\rm rec}(u,v)^r.
\]

On support, `N_rec>=1`; uniformly, `N_rec<=B^{o(1)}`. Hence for each fixed `r`,

\[
\boxed{
\#T_{\rm rec}\le S_r\le B^{o(1)}\#T_{\rm rec}.
}
\]

Indeed, if `N_rec<=B^{epsilon_B}` with `epsilon_B->0`, then
`N_rec^r<=B^{r epsilon_B}=B^{o(1)}` for fixed `r`.

Therefore

\[
\boxed{
S_r\text{ and }\#T_{\rm rec}\text{ have the same fixed-power exponent for every fixed }r.
}
\]

In particular, replacing the already-frozen first moment by the second moment or by any other fixed witness moment cannot, by itself, create a fixed `B^{-delta}` deficit in reciprocal support.

```text
FIXED_WITNESS_MOMENT_EXPONENT_EQUIVALENCE_PROVED=true
SECOND_MOMENT_ALONE_CAN_CREATE_FIXED_POWER_SUPPORT_DEFICIT=false
FIXED_HIGHER_MOMENT_ALONE_CAN_CREATE_FIXED_POWER_SUPPORT_DEFICIT=false
```

This is stronger bookkeeping than merely saying a second moment is unnecessary for first-moment-to-support transfer: it closes the whole class of fixed witness-moment reweightings as a source of a new polynomial exponent unless the arithmetic estimate controls support itself.

## 3. What MAIN-CRT2 must actually prove

The remaining high-value object is not witness multiplicity. It is the number of critical-wall base pairs for which at least one nested divisor allocation satisfies both quadratic CRT root conditions.

A genuine strict-sub-half input must therefore prove, uniformly on every retained principal critical-wall cell (or with a chargeable exceptional set in the same physical measure), a support deficit of the form

\[
\boxed{
\#\{(u,v)\in R_{\rm prim}^{\rm wall}:N_{\rm rec}(u,v)>0\}
\ll B^{\kappa-\delta+o(1)}
}
\]

for some fixed `delta>0`, relative to that cell's complete-host exponent `kappa`, with enough deficit after the already-frozen capacity/post-mask ledger to cross the global half-power wall.

Equivalent acceptable input: an upper bound for any one fixed moment `S_r` with the same fixed-power deficit. The new lemma shows that such a moment theorem is useful only because it proves a support deficit; changing `r` itself supplies no saving.

The exact unresolved arithmetic remains the simultaneous system

\[
t_p,t_q\mid m^\circ,\quad f\mid t_pt_q,
\]

\[
G_-f^2\equiv-G_+t_pt_q\pmod{2U},
\qquad
G_-f^2\equiv G_+t_pt_q\pmod{2V},
\]

with primitive `(u,v)`, fixed principal-cell geometry, and all frozen filters retained. No independence between the two congruences is assumed.

## 4. Outcome of aa

No strict global sub-square-root theorem is obtained in aa. The current strongest global upper remains

\[
\boxed{N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}}.
\]

But the first-ranked MAIN continuation is materially narrowed:

1. fixed second/higher witness moments are exponent-neutral;
2. divisor/core multiplicity sharpening is exponent-neutral at fixed-power scale;
3. the only MAIN quantity capable of changing the exponent is the critical-wall **support mass** of simultaneous two-level CRT solvability (or an exactly equivalent moment theorem that actually proves a support deficit).

Thus the next upper route, if aa is audited PASS, should move to the next independent high-probability species rather than repeat witness-moment algebra. Under the r401a ranking this is `27-40ab = T-AVG-ADAPTER`, unless fresh audit finds an unexploited support theorem inside MAIN.

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
