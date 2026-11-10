# M3-PESCH-TI-001 — Peschmann torsion-intersection gives an exact fixed-source endpoint killer on M3; every endpoint must have both Euclid source pairs in the TI-hard set.

CARD_ID: M3-PESCH-TI-001
CANONICAL_CARD_KEY: M3-PESCH-TI-001
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-PESCH-TI-001
現行一覧の状態: PROVED_EXACT_ADAPTER / EXTERNAL_CORE_THEOREM_SCOPED_PASS / 1072_AGGREGATE_HOLD
種別: EXACT_STRUCTURE / EXTERNAL_THEOREM_ADAPTER / FIBER_KILLER / TWO_SOURCE_RECEIVER
要点: Peschmann torsion-intersection gives an exact fixed-source endpoint killer on M3; every endpoint must have both Euclid source pairs in the TI-hard set.
主張の抜粋: For fixed p=(m,n), P_p(t^2)=M/b^4 is already square on M3 and Q_p(t^2)=f1/b^4, so H_p rational above physical t iff endpoint. If Theorem 4.5 closes p, no nondegenerate endpoint uses p. Source swap gives the two-hard-source receiver.
対象・測度: Exact primitive canonical M3, exact R<=B, ordered two-source Master coverage.
依存関係: M3-MASTER-001; M3-ONE-002; independently checked arXiv:2604.28072 core theorem; audit 1Nc-9HIo6uaqWRTuFfimIzJXwE5d7O5BdAYPwUjSISfA.
再開条件の抜粋: PARKED_BY_EXPLICIT_USER_REQUEST / 既存結果保持。現在のprimaryはM3-T11-GATE-001。通常stage37mainbatchでTIを自動再開しない。TI再開時は最新TI-005からTI-006へ。1072 HOLD、global saving未証明。
旧詳細位置: Card M3-PESCH-TI-001; audit PARTIAL_PASS/HOLD on 1,072 aggregate.
旧詳細リンク: https://docs.google.com/document/d/1Tmy_8CX29vqVaJah5WhOuTyzDrqveeYOdCvH9MVt-9U/edit
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 1054744
SOURCE_END: 1056477
SOURCE_SHA256: ee31e6916be3092259ef8eb314a1940ce7c937cbc97c06f62097048c3da8f19e

## M3-PESCH-TI-001
TYPE: EXACT_STRUCTURE / EXTERNAL_THEOREM_ADAPTER / FIBER_KILLER / TWO_SOURCE_RECEIVER
STATUS: PROVED_EXACT_ADAPTER / EXTERNAL_CORE_THEOREM_SCOPED_PASS
CLAIM:
For a fixed primitive second Euclid source p=(m,n), let H_p be the genus-3 curve v^2=P_p(t^2)Q_p(t^2) from Peschmann arXiv:2604.28072. On the exact M3 population, P_p(t^2)=M/b^4 is already a nonzero rational square and Q_p(t^2)=f1/b^4, so H_p has a rational point above the physical parameter t if and only if that M3 object is an endpoint. If p satisfies the torsion-intersection criterion of Theorem 4.5, that fixed-source fiber has no nondegenerate endpoint. Swapping the two primitive Euclid sources gives: every endpoint must have both source pairs in the torsion-intersection-hard set H_TI.
POPULATION:
exact primitive canonical M3, exact physical height R<=B, two-source Master coverage.
DEPENDS_ON:
M3-MASTER-001; M3-ONE-002; independently checked fixed-source algebra; scoped literature audit 1Nc-9HIo6uaqWRTuFfimIzJXwE5d7O5BdAYPwUjSISfA.
IMPLIES:
P(B) <= #{E in M3(B): p1(E) in H_TI and p2(E) in H_TI}.
AUDIT:
Core structural/torsion-intersection theorem PASS with a corrected nonfatal resultant identity. The manuscript's aggregate 1,072-fiber unconditional claim is HOLD pending resolution of the section-4.4 versus Appendix-B rank-certification conflict.
CREDIT:
Exact receiver only. No global fixed-power saving, primary-gate closure, P/M3 closure, or Perfect Cuboid nonexistence credit.
DO_NOT_REPEAT:
Do not promote the 1,072-fiber aggregate as unconditional until the actual worker/replay confirms an unconditional L-ratio or equivalent certificate for all ambiguous-rank rows.
DETAIL_DOC:
1Tmy_8CX29vqVaJah5WhOuTyzDrqveeYOdCvH9MVt-9U
---

## Retained standalone source — M3-PESCH-TI-001-PESCHMANN-2604.28072-TORSION-INTERSECTION-ADAPTER
SOURCE_FILE_ID: 1Tmy_8CX29vqVaJah5WhOuTyzDrqveeYOdCvH9MVt-9U
SOURCE_URL: https://docs.google.com/document/d/1Tmy_8CX29vqVaJah5WhOuTyzDrqveeYOdCvH9MVt-9U/edit?usp=drivesdk

﻿M3-PESCH-TI-001 — Peschmann torsion-intersection fixed-source adapter


STATUS=PROVED_EXACT_ADAPTER / EXTERNAL_CORE_THEOREM_SCOPED_PASS
FINITE_1072_AGGREGATE_STATUS=HOLD
TYPE=EXACT_STRUCTURE / EXTERNAL_THEOREM_ADAPTER / FIBER_KILLER / TWO_SOURCE_RECEIVER
SOURCE=arXiv:2604.28072v1
AUDIT_DOC_ID=1Nc-9HIo6uaqWRTuFfimIzJXwE5d7O5BdAYPwUjSISfA
RELATED=M3-MASTER-001;M3-ONE-002;M3-ONE-005;M3-TERM-002
DUPLICATE_OF=none
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false


1. Exact Stage37 dictionary


Fix the second primitive Euclid source p=(m,n), with
U2=m^2-n^2, V2=2mn, W2=m^2+n^2,
and write t=a/b for the first source.


Define
P_p(s)=V2^2 s^2+(4U2^2-2V2^2)s+V2^2,
Q_p(s)=W2^2 s^2+2(U2^2-V2^2)s+W2^2.


Direct substitution gives the exact identities
P_p(t^2)=M/b^4,
Q_p(t^2)=f1/b^4,
where
M=(V1 U2)^2+(U1 V2)^2
is the Master/M3 square condition and
f1=(W1 U2)^2+(U1 V2)^2
is the space-diagonal square condition.


Hence on the exact nondegenerate Stage37 M3 population, P_p(t^2) is already a nonzero rational square. Therefore
H_p: v^2=P_p(t^2)Q_p(t^2)
has a rational point above that physical M3 parameter t
if and only if Q_p(t^2) is a rational square,
equivalently if and only if that M3 object is an endpoint.


This is stronger than merely using H_p as a necessary relaxation: after conditioning on exact M3, H_p is an exact endpoint adapter at fixed second source.


2. Independently checked quotient geometry


The involutions t->-t, t->1/t, t->-1/t give the quotients
E_PQ: Y^2=P_p(s)Q_p(s), s=t^2,
E_uV: V^2=(V2^2 u^2+4(U2^2-V2^2))(W2^2 u^2-4V2^2), u=t+1/t,
E_3: V^2=(V2^2 w^2+4U2^2)(W2^2 w^2+4U2^2), w=t-1/t.


These formulas were independently rederived from P_p(t^2)Q_p(t^2)/t^4, so the Stage37 adapter does not rely solely on the companion-paper citation.


The paper's displayed resultant in section 3.1 contains a nonfatal algebraic error:
stated Res_s(P_p,Q_p)=256 U2^4 V2^4,
but direct symbolic calculation gives
Res_s(P_p,Q_p)=16 U2^8.
The corrected resultant is still nonzero for m>n, so the smooth genus-3 conclusion survives. The two displayed discriminants are correct.


3. Fiber-killer theorem imported into Stage37


Define TI_CLOSED(p) for a primitive source p=(m,n) when one of the following exact conditions holds for H_p:


A. rank E_3(Q)=0 and |E_3(Q)_tors|=4.


B. rank E_uV(Q)=0 and |E_uV(Q)_tors|=6.


C. rank E_uV(Q)=0, |E_uV(Q)_tors|=8, and the rational torsion lift count back to H_p is exactly 8.


Then H_p(Q) consists only of the eight degenerate points
t=0, t=+/-1, and the two points at infinity.
Therefore no nondegenerate Stage37 endpoint can have p as its fixed second Euclid source.


The proof is the degree-2 quotient count:
rank zero makes the quotient rational points torsion;
E_3 has no rational ramification because t^2=-1 has no rational solution;
E_uV has exactly four rational ramification points at t=+/-1;
the stated torsion/lift cardinalities force |H_p(Q)|<=8;
the eight known degenerate points give the matching lower bound.


4. Two-source consequence


By M3-MASTER-001 / the master-tuple reduction, every primitive canonical M3 object has two primitive Euclid source pairs p1 and p2. Swapping the two pairs swaps the two even-edge labels.


Therefore every perfect endpoint must satisfy
NOT TI_CLOSED(p1) AND NOT TI_CLOSED(p2).


Equivalently, if H_TI denotes the set of primitive source pairs not closed by the torsion-intersection criterion, then
P(B) <= #{E in M3(B): p1(E) in H_TI and p2(E) in H_TI}.


This is an exact two-source receiver. No independence assumption is used.


5. Canonical open gate


M3-PESCH-TI-GATE-001
TYPE=THEOREM_GATE
STATUS=OPEN
CLAIM:
Prove that the exact physical M3 mass on the two-hard-source locus is negligible:
#{E in M3(B): p1(E),p2(E) in H_TI}=o(M3(B)).
Any such theorem closes P(B)/M3(B)->0.


Stronger sufficient forms include a fixed-power deficit on the two-hard-source locus, or a same-R<=B weighted theorem showing that a sufficiently strong proportion of physical source mass is TI_CLOSED. A raw unweighted density of source pairs is not enough.


The natural new family target is E_3(p), because its closure criterion has no rational ramification correction. A uniform rank-zero/torsion theorem, or a weighted rank-distribution theorem on physical primitive Pythagorean sources, would feed this gate directly.


6. Scope and firewalls


The paper's generic torsion-intersection theorem is accepted here as an exact scoped Stage37 receiver.


The paper's claim that 1,072 explicit fibers are unconditionally certified is NOT promoted by this card. The full-literature audit found an implementation-description conflict between section 4.4 and Appendix B; see the audit receipt.


The finite list, even if fully certified, gives no asymptotic Stage37 saving by itself. The reusable value is the fixed-source fiber-killer criterion and its two-source consequence.


M3_PESCH_TI_FIXED_SOURCE_ENDPOINT_KILLER=true
M3_PESCH_TI_TWO_SOURCE_HARD_LOCUS_RECEIVER=true
M3_PESCH_TI_1072_UNCONDITIONAL_AGGREGATE_ACCEPTED=false
M3_PESCH_TI_WEIGHTED_HARD_LOCUS_SAVING_PROVED=false
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
