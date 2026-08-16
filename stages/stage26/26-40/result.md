# Stage26-40 — upper-bound ledger and third-face mechanism boundary

EVIDENCE_LEVEL=PROVED_DERIVED_THEOREM_CANDIDATE
CHECKPOINT=40
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
DEPENDS_ON=Stage26-30,Stage20,Stage25-reentry-60

## 1. Accepted checkpoint30 input

Work throughout with the frozen primitive/canonical no-space Euclidean cutoff `R<=B`. Let

\[
r(B)=\frac{M_3(B)}{M_2(B)},\qquad
\Phi(B)=\frac{M_3(B)}{M_2(B)+M_3(B)},\qquad
\Theta(B)=\frac{3M_3(B)}{M_2(B)+3M_3(B)}.
\]

Checkpoint30 is hostile-audited PASS and merged as PR #1016 / `e5e884e37f62db78a31f09d8927be230f07b0f2f`. It proves `r->0`, `Phi->0`, `Theta->0`, the exact odds bridge, and the two-sided corridor inherited from Stage18/20.

## 2. Strongest certified upper family

Stage20 gives, for every fixed

\[
0<\eta<1/46,
\]

\[
M_3(B)\ll_\eta B(\log B)^{5-\eta}.
\]

Stage18 gives

\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0.
\]

Hence for every fixed `0<eta<1/46`,

\[
\boxed{r(B)\ll_\eta(\log B)^{-\eta}}.
\]

Since exactly

\[
\Phi=\frac{r}{1+r}\le r,
\qquad
\Theta=\frac{3r}{1+3r}\le3r,
\]

the same upper family holds:

\[
\boxed{\Phi(B)\ll_\eta(\log B)^{-\eta}},
\qquad
\boxed{\Theta(B)\ll_\eta(\log B)^{-\eta}}.
\]

The endpoint `eta=1/46` is not part of the audited Stage20 theorem.

## 3. Endpoint-free little-o strengthening

Fix any

\[
0<\delta<1/46.
\]

Choose once and for all an `eta` with

\[
\delta<\eta<1/46.
\]

Then

\[
(\log B)^\delta r(B)
\ll_\eta(\log B)^{-(\eta-\delta)}\to0.
\]

Therefore

\[
\boxed{r(B)=o((\log B)^{-\delta})}
\qquad(0<\delta<1/46).
\]

By the exact inequalities above,

\[
\boxed{\Phi(B)=o((\log B)^{-\delta})},
\qquad
\boxed{\Theta(B)=o((\log B)^{-\delta})}
\]

for every fixed `0<delta<1/46`.

This is a genuine quantifier strengthening of the convenient single choice `eta=1/50`. It does **not** prove the endpoint `delta=1/46`, an exact logarithmic decay exponent, or any polynomial saving in `B`.

## 4. Directional shared-edge chambers

The hostile-audited Stage25-reentry phase60 receiver gives, for each `j in {a,b,c}`,

\[
P_j(B)=M_{2,j}(B)+M_3(B),
\qquad
\Theta_j(B)=\frac{M_3(B)}{P_j(B)},
\]

with

\[
M_{2,j}(B)\sim C_jB(\log B)^5,\qquad C_j>0.
\]

Thus the same quantifier argument yields

\[
\boxed{\Theta_j(B)=o_j((\log B)^{-\delta})}
\qquad(0<\delta<1/46).
\]

The already-audited directional ratio law remains

\[
\frac{\Theta_j(B)}{\Theta_k(B)}\to\frac{C_k}{C_j}.
\]

So the absolute completion rate vanishes in every chamber with the same certified open log-saving threshold, while the relative directional imbalance is governed by the raw-host constants.

## 5. Mechanism ledger

The quantitative upper input is not an independence heuristic. The accepted Stage20 geometry is:

```text
BASE_HOST=split_4A1_quartic_del_Pezzo_shared_edge_surface
RESOLUTION=Bl_4(P1xP1)
BASE_PICARD_RANK=6
THIRD_FACE_TARGET=degree_2_K3_cover
PHYSICAL_HEIGHT=Euclidean_R_anticanonical_on_base
```

The exact local blocker law on the matched pre-completion host is

\[
\delta_2=2/9,
\qquad
\delta_p=\frac{2(p-\chi_4(p))}{p^2+6p+1}
=\frac2p+O(p^{-2})
\]

for odd primes.

Two audited upper mechanisms coexist and must not be multiplied:

1. the explicit thin-cover/Huang interface gives
   \[
   M_3(B)\ll_\eta B(\log B)^{5-\eta},\qquad \eta<1/46;
   \]
2. the separate growing-prime Selberg sieve gives
   \[
   M_3(B)\ll B(\log B)^5/(\log\log B)^2.
   \]

The first is the stronger current asymptotic upper interface for Stage26. The second records the causal local-obstruction mechanism and independently proves thinning, but its saving is not multiplied into the Huang saving.

## 6. What checkpoint40 actually closes

Checkpoint40 closes the **current upper-bound ledger** at the resolution supplied by the audited Stage20 theorem:

```text
FOR_EVERY_FIXED_DELTA_LT_1_OVER_46=true
R=o((log B)^(-delta))
PHI=o((log B)^(-delta))
THETA=o((log B)^(-delta))
DIRECTIONAL_THETA_J=o_j((log B)^(-delta))
ENDPOINT_DELTA_1_OVER_46_PROVED=false
EXACT_LOG_DECAY_EXPONENT_PROVED=false
FIXED_POWER_SAVING_IN_B_PROVED=false
M3_ASYMPTOTIC_PROVED=false
```

The mechanism boundary is equally important: the third face is a thin degree-two K3-cover problem over the two-face toric host. The present proof does not identify a product of independent prime events, does not turn Picard-rank subtraction into a K3 counting theorem, and does not explain the true `M3` growth exponent.

Checkpoint50 should next record the strongest lower/construction ledger, centered on the primitive Saunderson family and what it does or does not say about the completion proportion.

## 7. Exit

```text
TASK_ID=Stage26-40
CHECKPOINT=40
UPSTREAM_CHECKPOINT30_MERGED_PR=1016
UPSTREAM_CHECKPOINT30_MERGE_COMMIT=e5e884e37f62db78a31f09d8927be230f07b0f2f
UPPER_FAMILY_IMPORTED_EXACTLY=true
ENDPOINT_FREE_LITTLE_O_CANDIDATE=true
DIRECTIONAL_LITTLE_O_CANDIDATE=true
LOCAL_BLOCKER_AND_THIN_COVER_SAVINGS_MULTIPLIED=false
FINITE_DATA_USED_AS_PROOF=false
TRUE_M3_EXPONENT_IDENTIFIED=false
K3_MANIN_TRANSFER=false
INDEPENDENCE_CLAIM=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=50
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage26-audit
```
