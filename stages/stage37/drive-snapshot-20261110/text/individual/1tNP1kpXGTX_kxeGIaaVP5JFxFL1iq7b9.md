# M3-T11-015 — Equal-tau four-core decomposition and one-twelfth relative-spin receiver

CARD_ID: M3-T11-015
CANONICAL_CARD_KEY: M3-T11-015
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-015
現行一覧の状態: PROVED_EXACT_STRUCTURE / NEW_NARROW_GATE
要点: Equal-tau four-core decomposition and one-twelfth relative-spin receiver
主張の抜粋: On the Step-A complement write D_i=tau*c_i, c_1=h_2*h_3, c_2=h_1*h_3, c_3=h_1*h_2. Choose primitive Gaussian representatives A_i with N(A_i)=D_i and factor A_i=B_i Z_i, N(B_i)=c_i, N(Z_i)=tau. Primewise relative orientation of the equal-norm Z_i gives pairwise coprime factors tau=tau_0*tau_1*tau_2*tau_3 and Gaussian cores G_j, N(G_j)=tau_j, such that up to bounded units
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 17.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 354183
SOURCE_END: 356510
SOURCE_SHA256: b3f7b4837724ebeaad7dd3e66a2a1fbc8f41073fbef7b815debf633ba06c6140

CARD_ID: M3-T11-015
TITLE: Equal-tau four-core decomposition and one-twelfth relative-spin receiver
STATUS: PROVED_EXACT_STRUCTURE / NEW_NARROW_GATE
ROUTE: TrivialSplitCyclicDirectionOneThird


RESULT:
On the Step-A complement write


D_i=tau*c_i,
c_1=h_2*h_3,
c_2=h_1*h_3,
c_3=h_1*h_2.


Choose primitive Gaussian representatives A_i with N(A_i)=D_i and factor


A_i=B_i Z_i,
N(B_i)=c_i,
N(Z_i)=tau.


Primewise relative orientation of the equal-norm Z_i gives pairwise coprime factors


tau=tau_0*tau_1*tau_2*tau_3


and Gaussian cores G_j, N(G_j)=tau_j, such that up to bounded units


Z_1=G_0*conj(G_1)*G_2*G_3,
Z_2=G_0*G_1*conj(G_2)*G_3,
Z_3=G_0*G_1*G_2*conj(G_3).


Let q_j=G_j/conj(G_j), Q=q_0*q_1*q_2*q_3. After absorbing the fixed small c_i representations and the odd/even Pythagorean leg choice into norm-one coefficients r_i,


C_i/D_i=Re(Q/r_i),


with


A=r_1^2+r_2^2+r_3^2,
U=Q^2.


The endpoint sphere equation is exactly


conj(A) U^2 + 2U + A = 0.


Hence the all-same orientation core G_0 is not free. A necessary common-phase condition is


|A|^2-1=s^2


for s in Q, followed by the torus square-lift U=Q^2. Once the other three cores and small packet are fixed, G_0 has only O(1) possibilities.


Moreover


|A|^2-1
=
lambda_12*lambda_13*lambda_23,


where


lambda_ij
=
r_i/r_j+r_j/r_i
=
2 Re(r_i/r_j)
in Q.


Thus the huge-tau endpoint condition contains the exact global triple-spin squareclass relation


lambda_12*lambda_13*lambda_23 in Q^2,


plus the torus-doubling condition.


COUNTING_BUDGET:
If c_i<=C, then


h_1*h_2*h_3<=C^(3/2),


so the number of ordered content triples is


C^(3/2+o(1)).


For fixed content triple, the small c_i Gaussian coefficient packets cost only B^o(1).


At C=B^(1/6+xi), the outer packet count is


B^(1/4+(3/2)xi+o(1)).


Therefore a uniform bound


N_rel(B; fixed content triple and packet)
<<
B^(1/12-delta)


for some fixed delta>0 is sufficient for P(B)=o(B^(1/3)), after choosing xi small enough.


NEW_GATE:
CyclicFixedContentTripleRelativeSpinOneTwelfth.


DO_NOT_REPEAT:
Do not treat G_0 as an independent fourth moving equal-norm core.
Do not multiply primewise tau root labels.
Do not claim tH8/FI/Hecke readiness without an exact certificate for this triple-spin charged measure.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 17.


---
