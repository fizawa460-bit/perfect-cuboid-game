# Stage25-reentry r011a hostile audit

AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
ROUTE_ID=Stage25-um-r011a
PR=1010

The geometric common-ledger claim is accepted with the submitted scope firewall.

Accepted:
- the Euler one-face raw model has minimal resolution F_2 with hyperplane pullback H=S+2F and K=-2H, hence generalized height invariants (a,b)=(2,2);
- the nested one-face-plus-space surface is a Q(i)-twist of the Stage15 split 4A1 quartic-del-Pezzo model under [E:X:Y:U:V]=[p:i*b:c:a:d];
- the induced conjugation X->-X is realized by (m:n)<->(n:m) with the second Pythagorean parameter pair fixed;
- on Pic(Bl_4(P1xP1)) this fixes the two ruling classes and pairs the four exceptional corner classes into two Galois orbits, giving rational Picard invariant rank 4;
- adjunction plus crepant A1 resolution gives the anticanonical height, hence (a,b)=(1,4) for N1;
- the Stage15 split model has (a,b)=(1,6) for M2;
- these three invariant pairs match the already proved scales B^2 log B, B(log B)^3, and B(log B)^5;
- therefore Stage21 has (Delta a,Delta b)=(-1,+2), Stage22 has (-1,+4), and the additive geometric ledger b_M2-b_M1=(4-2)+(6-4)=2+2=4 is valid.

Scope firewall:
- this does not exhibit four independent arithmetic events;
- this does not prove a common source/target Dirichlet pole-slot ledger;
- this does not revive the phase50 rejected pole-order-subtraction wording;
- H(P) one-log / L_B(P) one-log remains unproved;
- the fine mechanism is closed only at the geometric Manin-invariant level;
- no perfect-cuboid existence or nonexistence conclusion is made.

The cross-target M2/N1 ~ (24*pi*C_M2/kappa)(log B)^2 statement is accepted only as a population-size comparison of non-nested strata.

Submission head b123eded07a0f30078d14509f59b353553b94f10 has SUCCESS for the dedicated `Stage25 reentry r011a log4 geometric ledger`, phase50, reentry roadmap contract, Stage25-70 closeout, and relevant Stage25 reentry regressions. The unrelated Stage15-8 failure is outside this Stage25 audit scope.

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
R011A_STATUS=AUDITED_PASS_AWAITING_MERGE
GEOMETRIC_MANIN_INVARIANT_LEDGER_PROVED=true
M1_MANIN_A=2
M1_MANIN_B=2
N1_MANIN_A=1
N1_MANIN_B=4
M2_MANIN_A=1
M2_MANIN_B=6
G21_LOG2_FINE_MECHANISM=CLOSED_AT_GEOMETRIC_INVARIANT_LEVEL
G22_LOG4_FINE_MECHANISM=CLOSED_AT_GEOMETRIC_INVARIANT_LEVEL
LOG4_DECOMPOSITION_AS_B_JUMPS=2+2
COMMON_DIRICHLET_POLE_SLOT_LEDGER_PROVED=false
FOUR_INDEPENDENT_LOG_FACTORS_PROVED=false
ADVANCE_ALLOWED=true
NEXT_REENTRY_PHASE=60
PHASE60_ALLOWED_BEFORE_MERGE=false
MERGE_ALLOWED=true
STAGE26_ALLOWED=false
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
NEXT_EXPECTED_COMMAND=merge PR #1010; then Stage25-reentry-main-batch
```
