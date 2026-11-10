# M3-PESCH-TI-GATE-001 — Close Stage37 if the exact M3 mass with both primitive Euclid sources TI-hard is o(M3(B)).

CARD_ID: M3-PESCH-TI-GATE-001
CANONICAL_CARD_KEY: M3-PESCH-TI-GATE-001
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-PESCH-TI-GATE-001
現行一覧の状態: OPEN
種別: THEOREM_GATE / TWO_SOURCE_WEIGHTED_HARD_LOCUS
要点: Close Stage37 if the exact M3 mass with both primitive Euclid sources TI-hard is o(M3(B)).
主張の抜粋: Let H_TI be primitive source pairs not killed by the torsion-intersection criterion. M3-PESCH-TI-001 gives P(B)<=#{E in M3(B): p1(E),p2(E) in H_TI}. A same-R<=B weighted o(M3) theorem for this locus closes P/M3.
対象・測度: Exact primitive canonical M3 with both source pairs, exact R<=B.
依存関係: M3-PESCH-TI-001; M3-MASTER-001.
再開条件の抜粋: PARKED_BY_EXPLICIT_USER_REQUEST / 既存結果保持。現在のprimaryはM3-T11-GATE-001。通常stage37mainbatchでTIを自動再開しない。TI再開時は最新TI-005からTI-006へ。1072 HOLD、global saving未証明。
旧詳細位置: M3-PESCH-TI-001 card, section 5.
旧詳細リンク: https://docs.google.com/document/d/1Tmy_8CX29vqVaJah5WhOuTyzDrqveeYOdCvH9MVt-9U/edit
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 1056477
SOURCE_END: 1057424
SOURCE_SHA256: db4b78617ea1c7d8ff6935e3e196d8216663f0c2a65703874b1a67baf2273229

## M3-PESCH-TI-GATE-001
TYPE: THEOREM_GATE
STATUS: OPEN
CLAIM:
Let H_TI be the primitive Euclid-source pairs not closed by the torsion-intersection criterion. Prove on the exact R<=B M3 measure that
#{E in M3(B): p1(E),p2(E) in H_TI}=o(M3(B)).
Then P(B)/M3(B)->0.
POPULATION:
exact primitive canonical M3 with its two primitive Euclid source pairs.
DEPENDS_ON:
M3-PESCH-TI-001; M3-MASTER-001.
REOPEN/ATTACK CONDITION:
A same-R<=B weighted theorem for torsion-intersection closure among physical primitive Pythagorean sources, a uniform rank-zero/torsion theorem for the quotient family (especially E_3), or a two-source correlation theorem. Raw unweighted density of source pairs is insufficient.
CREDIT:
Open receiver only; no saving or closure credit yet.
DETAIL_DOC:
1Tmy_8CX29vqVaJah5WhOuTyzDrqveeYOdCvH9MVt-9U
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false

## Retained LEDGER source 2
SOURCE_START: 1066350
SOURCE_END: 1069728
SOURCE_SHA256: cfa29aae7a4c7b96d2dc9f1ba6d2a8a104ead63df8fe08ab08bfa6ed74e4096c

## M3-PESCH-TI-GATE-001 — user-authorized primary-route selection and exact weight formulation
CHANGE_KIND=Operational roadmap/addendum to the existing gate; no new research-card ID or new closure credit.
ACTIVE_ROUTE_FILE_ID=198IsZ3zb1FRRbnO3BLiyqCJglDFw_4AU
SOURCE_CARD_DOC_ID=1Tmy_8CX29vqVaJah5WhOuTyzDrqveeYOdCvH9MVt-9U
SCOPED_AUDIT_DOC_ID=1Nc-9HIo6uaqWRTuFfimIzJXwE5d7O5BdAYPwUjSISfA
For each canonical E in M3(B), fix its Master source pair (p1,p2). Define mu_B(p,q)=1/2 sum_E(1_{(p1,p2)=(p,q)}+1_{(p2,p1)=(p,q)}). Each object contributes total mass one, including the diagonal case. Sum mu_B=M3(B). With H_TI the complement of unconditionally TI_CLOSED sources, R_HH=sum_{p,q in H_TI}mu_B counts the two-hard physical objects exactly. Existing TI-001 gives P(B)<=R_HH. The main target is R_HH=o(M3). Since M3(B)>>B^(1/3), R_HH<<B^(1/3-eta) is a sufficient stronger target.
The marginal F_B(p)=sum_q mu_B(p,q) gives R_HH<=sum_{p in H_TI}F_B(p). Thus an o(M3) weighted hard marginal suffices, while joint two-source correlation may work without such a marginal theorem. No independence is assumed. A positive constant closed mass, bare source density or finite 1072-fiber count alone does not establish the limit.
RESEARCH_ORDER=Exact Master source-weight adapter and bounds; E3 unconditional rank-zero/torsion closed families (E_uV auxiliary); weighted hard marginal or joint hard-locus asymptotics. The first concrete task is the exact E3 Weierstrass/torsion interface coupled to the physical source-weight receiver. Unknown/GRH-only/lift-unverified rows remain hard. The 1072 aggregate remains HOLD.
T11_121=Retained exact auxiliary result, parked as primary research; no deletion/retraction.
TI route detail and next-chat continuation contract are in the active route file. Old T11/S4/theta continuation is backup, not the default next task.
PRIMARY_GATE=M3-PESCH-TI-GATE-001
PRIMARY_GATE_STATUS=OPEN
ACTIVE_ROUTE=M3-PESCH-TI-ROUTE-MAIN
ACTIVE_ROUTE_FILE_ID=198IsZ3zb1FRRbnO3BLiyqCJglDFw_4AU
ACTIVE_RESEARCH_CARD=M3-PESCH-TI-001
ACTIVE_RESEARCH_CARD_DOC_ID=1Tmy_8CX29vqVaJah5WhOuTyzDrqveeYOdCvH9MVt-9U
ACTIVE_RECEIVER_AUDIT_DOC_ID=1Nc-9HIo6uaqWRTuFfimIzJXwE5d7O5BdAYPwUjSISfA
ACTIVE_RECEIVER_STATUS=PROVED_EXACT_ADAPTER / EXTERNAL_CORE_THEOREM_SCOPED_PASS
M3_PESCH_TI_1072_AGGREGATE_STATUS=HOLD
M3_PESCH_TI_WEIGHTED_HARD_LOCUS_SAVING_PROVED=false
LATEST_RESEARCH_CARD=M3-T11-121
LATEST_AUDITED_RESEARCH_CARD=M3-T11-121
T11_121_RESEARCH_STATUS=RETAINED_PROVED_EXACT_STRUCTURE / PARKED_PRIMARY_RESEARCH
T11_120_STATUS=RETRACTED_PHYSICAL_ADAPTER
NEXT_RESEARCH_CARD_ID=M3-PESCH-TI-002
NEXT_T11_RESEARCH_CARD_ID=M3-T11-122
PROVISIONAL_FRONTIER_CARD=NONE
PROVISIONAL_FRONTIER_AUDIT_STATUS=NOT_APPLICABLE
STRATEGY_SELECTION=USER_AUTHORIZED; no new mathematical promotion from route selection
CURRENT_ATTACK=TIClosedFamilyExactM3Weight|TwoSourceHardLocusCorrelation
NEXT_LEGAL_ACTION=Read active TI route, then TI-001 and its scoped audit. Derive E3 family Weierstrass model/torsion conditions and connect them to the exact Master source-weight receiver. Seek unconditional closed arithmetic families and a bound on their physical hard complement. No fixed-source or unweighted-count result alone closes the gate.
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
