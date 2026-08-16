# Stage25-reentry-70 — propagation synthesis and Stage26 handoff

TASK_ID=Stage25-um-r007a
PHASE=70
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PARENT_PHASE=Stage25-u20-r006a
PARENT_PR=1011
PARENT_MERGE_COMMIT=119afa00919f67bea8e3ba5515c0f9663aa9f2e2

## 1. Campaign completion check

The bounded Stage25-reentry pass has executed phases `10,20,30,40,50,60` in roadmap order. Their fresh audits are PASS and their PRs are merged. The theorem-changing derived routes opened during the campaign are exactly

- `Stage25-um-r008a` — directional quarter-power backflow;
- `Stage25-um-r009a` — exact common-`A3` mask backflow;
- `Stage25-um-r010a` — exact common-`M3` raw-pair / directional Stage22 backflow;
- `Stage25-um-r011a` — geometric Manin-invariant log2/log4 mechanism.

All four derived routes are hostile-audited PASS and merged. No additional internal child route was opened by phase60.

Phase70 synchronizes the receiver files that still carried historical `PENDING` labels; it does not reprove their mathematics.

## 2. Strongest synchronized interfaces

### Euler one-face source

\[
M_1(B)\sim\frac{3}{4\pi^2}B^2\log B.
\]

### One face plus integral space diagonal

\[
N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3,
\qquad
\frac{N_1}{M_1}\sim\frac{\kappa\pi}{18}\frac{(\log B)^2}{B}.
\]

The Stage21 fine mechanism is closed at the geometric Manin-invariant level:

\[
M_1:(a,b)=(2,2)\to N_1:(1,4).
\]

### Exactly two faces, no space condition

\[
M_2(B)\sim C_{M_2}B(\log B)^5,
\qquad C_{M_2}>0,
\]

with directional chambers

\[
M_{2,j}(B)\sim C_jB(\log B)^5,
\qquad C_{M_2}=C_a+C_b+C_c.
\]

The Stage22 transition is

\[
\frac{M_2}{M_1}\sim\frac{4\pi^2C_{M_2}}3\frac{(\log B)^4}{B},
\]

and the log-four fine mechanism is closed at the geometric Manin-invariant level:

\[
M_1:(2,2)\to M_2:(1,6),
\qquad 6-2=(4-2)+(6-4)=2+2.
\]

No four-independent-factor or common-Dirichlet-pole-slot theorem is claimed.

### Exactly two faces with integral space diagonal

\[
\boxed{B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}},
\]

and for every canonical shared edge `j=a,b,c`,

\[
\boxed{N_{2,j}(B)\gg_j B^{1/4}}.
\]

The exact mask identities are

\[
N_{2,a}=A_{ab,ac}-A_3,\quad
N_{2,b}=A_{ab,bc}-A_3,\quad
N_{2,c}=A_{ac,bc}-A_3.
\]

The true `N2` exponent remains open.

### Three faces, no space condition — Euler bricks

The frozen Stage20 envelope remains

\[
\boxed{B^{1/6}\ll M_3(B)\ll_\eta B(\log B)^{5-\eta}}
\qquad(\eta<1/46).
\]

The exact raw-pair incidence receiver is

\[
P_j=M_{2,j}+M_3,
\qquad
P=M_2+3M_3.
\]

Define the literal same-measure third-face completion rates

\[
\Theta_j=\frac{M_3}{P_j},
\qquad
\Theta=\frac{3M_3}{P}.
\]

Audited phase60 gives

\[
\boxed{B^{-5/6}(\log B)^{-5}\ll_j\Theta_j
\ll_{j,\eta}(\log B)^{-\eta}},
\]

and the analogous global corridor, hence `Theta_j,Theta -> 0`. It also gives

\[
\boxed{\Theta_j/\Theta_k\to C_k/C_j}
\]

without an asymptotic formula for `M3`.

## 3. Stage26-ready receiver

The Stage26 entry package is now exact on population, cutoff, multiplicity and measure:

1. split `4A1` quartic-del-Pezzo shared-edge raw two-face host;
2. degree-two K3 third-face cover;
3. exact raw-incidence multiplicity adapter `P_j=M2,j+M3`, `P=M2+3M3`;
4. literal completion observables `Theta_j,Theta`;
5. S20-W01 explicit thin-cover upper;
6. S20-W02 primitive Saunderson lower;
7. S20-W03 local blocker law and sieve dimension two;
8. S25-W05 raw-pair completion adapter;
9. S25-W06 geometric transition ledger, with a firewall forbidding fake extension of the Manin subtraction across the K3 cover.

The primary Stage26 mathematical target is therefore not to rebuild the host but to sharpen the third-face completion law: improve the `M3`/`Theta` corridor, identify the true exponent if possible, and test whether a matching same-measure theorem can be proved.

## 4. Residual gates and routing

The following are not unresolved Stage25-reentry internal routes and therefore do not block handoff:

- true `M3` exponent / matching lower or stronger upper — Stage26 primary target;
- true `N2` exponent / matching half-power behavior — later Stage27/28 receiver;
- Stage14/15 Q05 moving-genus-one global uniformity — external/future theorem gate;
- Q06 physical-diagonal Kummer support count — external/future theorem gate;
- Q11 effective growing-modulus overlap sieve — external/future theorem gate;
- R504 exceptional Prym/isogeny locus — external theorem gate;
- common Dirichlet pole-slot / independent factorization refinement of the log ladder — optional analytic refinement, not needed for Stage26 entry.

The P3 Stage14/15 clusters remain exhausted internally and are not reopened.

## 5. Phase70 gate candidate

After this synchronization:

```text
STAGE25_MAIN_CLOSED=true
PHASE10_AUDITED_MERGED=true
PHASE20_AUDITED_MERGED=true
PHASE30_AUDITED_MERGED=true
PHASE40_AUDITED_MERGED=true
PHASE50_AUDITED_MERGED=true
PHASE60_AUDITED_MERGED=true
DERIVED_R008A_AUDITED_MERGED=true
DERIVED_R009A_AUDITED_MERGED=true
DERIVED_R010A_AUDITED_MERGED=true
DERIVED_R011A_AUDITED_MERGED=true
DERIVED_ROUTE_QUEUE_HAS_UNRESOLVED_INTERNAL_ROUTE=false
STAGE20_STAGE26_READY_INTERFACE=true
BACKFLOW_SYNCHRONIZED_CANDIDATE=true
ALL_REENTRY_PHASES_AUDITED=false
STAGE26_ALLOWED=false
```

`ALL_REENTRY_PHASES_AUDITED` remains false until this phase70 package itself receives a fresh hostile audit. Stage26 is therefore still blocked in this submission.

```text
THEOREM_INTERFACE_VALID=true
REENTRY_RESEARCH_COMPLETE_CANDIDATE=true
STRONGER_RESULT_PROVED=false
NEW_REUSABLE_WEAPON_PROVED=false
ARSENAL_PROMOTIONS=S25-W05,S25-W06
FINITE_DATA_PROMOTED_TO_THEOREM=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
HUMAN_DECISION_REQUIRED=false
STAGE26_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage25-reentry-audit
```
