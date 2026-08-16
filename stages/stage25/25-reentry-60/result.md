# Stage25-reentry-60 — deep Euler baseline reentry

STATUS=SUBMITTED_PENDING_FRESH_AUDIT
TASK_ID=Stage25-u20-r006a
TARGET_STAGES=20,18
PARENT_ROUTE=Stage25-um-r011a
PARENT_PR=1010
PARENT_MERGE_COMMIT=e64f21621bb1b7062dfd21f186e6ed1bcc191272

## 1. Goal

Phase60 freezes the strongest Stage26-ready interface for adding the third integral face on the primitive canonical no-space side. It does not reopen exhausted Stage14/15 P3 routes and does not infer an asymptotic from finite Euler-brick data.

Use the common Euclidean cutoff

\[
R=\sqrt{a^2+b^2+c^2}\le B.
\]

Let `M2(B)` be primitive canonical exactly-two-face cuboids and `M3(B)` primitive canonical Euler cuboids (all three face diagonals integral), with no space-diagonal integrality condition.

For `j in {a,b,c}`, let `P_j(B)` be the raw two-face shared-edge incidence chamber from r010a, before the third-face mask. Then

\[
\boxed{P_j(B)=M_{2,j}(B)+M_3(B)}
\]

exactly, and summing the three chambers gives

\[
\boxed{P(B):=P_a+P_b+P_c=M_2(B)+3M_3(B)}.
\]

The coefficient three is incidence multiplicity: every Euler cuboid has three choices of shared edge.

## 2. Literal third-face completion rates

Define the directional raw-incidence completion rates

\[
\boxed{\Theta_j(B):=\frac{M_3(B)}{P_j(B)}}
\]

and the total raw-pair-incidence completion rate

\[
\boxed{\Theta(B):=\frac{3M_3(B)}{P(B)}
=\frac{3M_3(B)}{M_2(B)+3M_3(B)}}.
\]

Unlike the object-count ratio `M3/M2`, these are literal proportions on a matched raw-pair incidence host: numerator and denominator use the same incidence multiplicity, cutoff, primitive convention, and physical measure.

## 3. Two-sided completion corridor

The audited Stage20 arsenal gives

\[
M_3(B)\gg B^{1/6}
\]

from the primitive Saunderson family and, for every fixed `eta<1/46`,

\[
M_3(B)\ll_\eta B(\log B)^{5-\eta}.
\]

The audited Stage18/r010a directional host theorem gives

\[
P_j(B)\sim C_jB(\log B)^5,\qquad C_j>0,
\]

and

\[
P(B)\sim C_{M_2}B(\log B)^5,
\qquad C_{M_2}=C_a+C_b+C_c>0,
\]

because `M3=o(M2)`.

Therefore, for every fixed `eta<1/46`,

\[
\boxed{
B^{-5/6}(\log B)^{-5}\ll_j \Theta_j(B)
\ll_{j,\eta}(\log B)^{-\eta}
}
\]

and

\[
\boxed{
B^{-5/6}(\log B)^{-5}\ll \Theta(B)
\ll_\eta(\log B)^{-\eta}.
}
\]

In particular every completion rate tends to zero, but the audited Saunderson family prevents it from decaying faster than the displayed polynomial-log floor.

The same inputs give the adjacent-stratum object-size corridor

\[
\boxed{
B^{-5/6}(\log B)^{-5}\ll
\frac{M_3(B)}{M_2(B)}
\ll_\eta(\log B)^{-\eta}.
}
\]

This last ratio is a population-size comparison, not a conditional probability.

## 4. Directional completion-ratio law

The common numerator gives an exact cancellation:

\[
\frac{\Theta_j(B)}{\Theta_k(B)}
=\frac{P_k(B)}{P_j(B)}.
\]

Hence the directional toric asymptotics imply

\[
\boxed{
\frac{\Theta_j(B)}{\Theta_k(B)}
\longrightarrow\frac{C_k}{C_j}
\qquad(j,k\in\{a,b,c\}).
}
\]

Thus the relative directional propensity to complete the third face is determined entirely by the inverse raw-pair host constants. No asymptotic for `M3` is needed for this ratio theorem.

This is the strongest new phase60 statement: it is a true third-face completion comparison on the correct incidence measure while the absolute Euler-brick exponent remains unknown.

## 5. Stage26-ready geometric/arithmetic interface

The receiver handed toward Stage26 is now:

```text
HOST=split_4A1_quartic_del_Pezzo_shared_edge_surface
HOST_RESOLUTION=Bl_4(P1xP1)
HOST_PICARD_RANK=6
HOST_HEIGHT=exact_Euclidean_R_anticanonical_height
TARGET=third_face_square_degree_2_K3_cover
RAW_PAIR_IDENTITY=P=M2+3M3
DIRECTIONAL_IDENTITY=P_j=M2,j+M3
LOCAL_BLOCKER=delta_2=2/9; delta_p=2(p-chi4(p))/(p^2+6p+1)
UPPER=M3<<_eta B(log B)^(5-eta), eta<1/46
LOWER=M3>>B^(1/6)
COMPLETION_RATE_TOTAL=3M3/(M2+3M3)
COMPLETION_RATE_DIRECTIONAL=M3/(M2,j+M3)
```

The r011a Manin `(a,b)` ledger explains the one-face/two-face source growth but is not extended through the K3 cover as a fake Picard-rank subtraction. The third-face problem is genuinely a thin-cover counting problem.

## 6. Reuse-preflight verdict

Phase10 already machine-indexed all 824 Stage14/15 attack records. For phase60 the compatible terminal cluster is `S1415-ATTACK-0215/0216/0217/0224` (two-face toric height, Euler K3 cover, local blocker, explicit `eta<1/46` upper). The P3 clusters are not reopened: no new equation, same-measure spectral estimate, or external theorem has appeared that would license repeating those attacks.

The fresh mutation is instead the exact completion-rate receiver above, obtained by combining S20-W01/W02/W03 with the audited Stage18/r010a raw-pair denominator.

## 7. Non-claims

Phase60 does not prove:

- an asymptotic formula for `M3(B)`;
- the true Euler-brick exponent;
- a matching power upper/lower bound;
- a fixed power saving `M3<<B^(1-delta)`;
- that the completion rates have an absolute asymptotic constant;
- independence of the local blocker primes beyond the audited sieve contract;
- any perfect-cuboid existence or nonexistence statement.

```text
TASK_ID=Stage25-u20-r006a
THEOREM_INTERFACE_VALID=true
REENTRY_RESEARCH_COMPLETE=true
STRONGER_RESULT_CANDIDATE=true
STRONGER_RESULT_PROVED=false
NEW_REUSABLE_WEAPON_CANDIDATE=true
NEW_REUSABLE_WEAPON_PROVED=false
RAW_PAIR_COMPLETION_RECEIVER_MATERIALIZED=true
DIRECTIONAL_COMPLETION_RATIO_CANDIDATE=true
TRUE_M3_EXPONENT_IDENTIFIED=false
STAGE20_STAGE26_READY_INTERFACE_CANDIDATE=true
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_REENTRY_PHASE=70
STAGE26_ALLOWED=false
PERFECT_CUBOID_CONCLUSION=NONE
NEXT_EXPECTED_COMMAND=Stage25-reentry-audit
```
