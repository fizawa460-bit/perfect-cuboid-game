# M3-T11-102 — The audited splitting receiver fixes only d=[2*Pi], not exact Pi. Fixed d remains a two-dimensional endpoint surface; fixed (d,u) gives a smooth genus-3 square-coordinate double cover of the old fixed-u genus-one incidence.

CARD_ID: M3-T11-102
CANONICAL_CARD_KEY: M3-T11-102
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-102
現行一覧の状態: PROVED_EXACT / HOSTILE_AUDIT_PASS / EXACT_SQUARECLASS_GEOMETRY / FIXED_SQUARECLASS_SURFACE / GENUS3_DOUBLE_COVER / FIXED_PI_OVERREFINEMENT_FIREWALL / NO POWER SAVING
種別: EXACT_STRUCTURE / SAME_MEASURE_GLOBAL_GEOMETRY / CROSS_PRIME_RECEIVER_REFINEMENT / FIBRATION_PREFLIGHT / ANTI_LOOP_FIREWALL
要点: The audited splitting receiver fixes only d=[2*Pi], not exact Pi. Fixed d remains a two-dimensional endpoint surface; fixed (d,u) gives a smooth genus-3 square-coordinate double cover of the old fixed-u genus-one incidence.
主張の抜粋: Exact identities give [2*Pi]=[2*S*(1+u^2)]=[2*s*t*N_u]. Write 2*Pi=d*q^2 with signed squarefree d. Section 49 gives v_p(q)=-2lambda at every relative-fresh p^lambda||M_rel. For fixed d,u, T^2=-(1+u^2)F_{d,u}(q) with degree 8 and Disc_q(F)=-2^128*d^28*u^62*(1+u^2)^33*(25*u^2-2)^6, nonzero for rational physical d,u!=0; hence genus 3. The q->-q quotient is exactly the old fixed-u genus-one curve after x=d*q^2=2*Pi. Fixed-Pi genus-5 slices cannot count fixed d without a q-support theorem.
対象・測度: Exact fixed-content/coefficient nondegenerate Stage37 physical endpoint population with R<=B; same measure.
依存関係: M3-T11-101 HOSTILE_AUDIT_PASS; audited Section 35; Section 49 exact Pi denominator; audited fixed-u genus-one/B^o(1) geometry.
再開条件の抜粋: Reopen if hostile audit rejects the squareclass identities, fixed-squareclass dimension count, exact q fresh denominator, degree-8 substitution/discriminant, or quotient identification; or an audited dependency changes.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 114.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 924896
SOURCE_END: 931555
SOURCE_SHA256: e1915dabc1c0e4ca5d4ca4ec1da836aebc5f7513b31e7b734fabb3a9df177b51

M3-T11-102
STATUS:
PROVISIONAL EXACT_SQUARECLASS_GEOMETRY / FIXED_SQUARECLASS_SURFACE / GENUS3_DOUBLE_COVER / FIXED_PI_OVERREFINEMENT_FIREWALL / HOSTILE_AUDIT_REQUIRED / NO POWER SAVING


TYPE:
EXACT_STRUCTURE / SAME_MEASURE_GLOBAL_GEOMETRY / CROSS_PRIME_RECEIVER_REFINEMENT / FIBRATION_PREFLIGHT / ANTI_LOOP_FIREWALL


SUMMARY:
The audited M3-T11-101 splitting receiver fixes only the quadratic squareclass d=[2*Pi], not the exact value of Pi. Exact symmetric identities give
[2*Pi]=[2*S*(1+u^2)]=[2*s*t*N_u],
and on the nonzero split-discriminant locus also [2*Pi]=[-2*S*Q(S,u)].
Choose a signed squarefree representative d and q in Q* with 2*Pi=d*q^2. Section 49 gives v_p(Pi)=-4*lambda for every relative-fresh p^lambda||M_rel, hence p does not divide d and v_p(q)=-2*lambda. Thus q has exact relative-fresh denominator M_rel^2, but this is only the square root of the already-consumed Pi denominator and has zero independent saving credit.
Fixing d leaves the two-dimensional surface
S=d*q^2*(1+u^2)/(8*u^2)
together with the endpoint square equation. Fixed-Pi genus-5 curves are the stricter q^2-fixed slices of this surface.


CLAIM:
For fixed rational d!=0 and u!=0, substituting pi=d*q^2/2 into the audited M3-T11-101 fixed-Pi model and putting T=4Z gives
T^2=-(1+u^2)*F_{d,u}(q),
where
F_{d,u}(q)
=d^4*q^8*(1+u^2)^5
-128*d^3*q^6*u^3*(1+u^2)^3
+256*d^2*q^4*u^4*(1+u^2)^2*(11*u^2-1)
+24576*d*q^2*u^7*(1+u^2)
-65536*u^10.
Exactly,
Disc_q(F_{d,u})
=-2^128*d^28*u^62*(1+u^2)^33*(25*u^2-2)^6.
For rational d,u!=0 this is nonzero, since u^2=2/25 has no rational solution. Therefore every fixed-(d,u) fiber is a smooth degree-8 hyperelliptic curve of genus 3.
The involution q->-q has a smooth quartic genus-one quotient. With z=q^2 and x=d*z=2*Pi, followed by S=x*(1+u^2)/(8*u^2), that quotient is exactly the old audited Section-35 fixed-u genus-one incidence. Hence the new receiver is the square-coordinate double cover x/d=q^2, not a new elliptic quotient.


POPULATION:
Exact same fixed-content/coefficient nondegenerate Stage37 physical endpoint population with R<=B. No change of measure. The splitting-field interpretation uses audited M3-T11-101.


DEPENDS_ON:
Hostile-audit-passed M3-T11-101; audited Section 35 symmetric incidence; Section 49 exact fresh denominator of Pi; audited fixed-u genus-one/B^o(1) geometry.


IMPLIES:
The correct global interior receiver is a fixed-squareclass surface. Fixed d alone does not reduce the physical endpoint problem to one genus-5 curve. A valid continuation must control realized q / exact-Pi support inside d on the same measure, or exploit the genus-3 square-coordinate cover across moving u. The independent theta moving-support route remains live.


FIREWALL:
Do not identify fixed d with fixed Pi. Do not promote fixed-Pi genus-5 finiteness or any fixed-Pi multiplicity theorem to a fixed-squareclass count without a separate q-support theorem. Do not charge q's M_rel^2 denominator independently from Pi's M_rel^4 denominator. Do not charge the genus-one quotient again: it is the existing fixed-u quotient.


REOPEN_CONDITION:
Hostile audit rejects one of the exact squareclass identities, the fixed-squareclass dimension count, Section 49's exact Pi valuation, the degree-8 substitution/discriminant, or the quotient identification; or an audited dependency changes.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 114.


CREDIT:
No fixed-power support saving. No denominator-extreme closure. No primary-gate closure. No endpoint theorem. No P(B)/M3(B) limit. No Perfect Cuboid nonexistence credit.


FLAGS:
M3_T11_2PI_SQUARECLASS_SYMMETRIC_REPRESENTATIONS=PROVISIONAL
M3_T11_FIXED_SQUARECLASS_Q_MREL2_DENOMINATOR=PROVISIONAL
M3_T11_FIXED_SQUARECLASS_Q_DENOMINATOR_INDEPENDENT_SAVING=false
M3_T11_FIXED_2PI_SQUARECLASS_RECEIVER_DIMENSION=2
M3_T11_FIXED_2PI_SQUARECLASS_FIXED_U_GENUS3=PROVISIONAL
M3_T11_FIXED_2PI_SQUARECLASS_GENUS3_ELLIPTIC_QUOTIENT_OLD=true
M3_T11_FIXED_PI_GENUS5_OVERREFINEMENT_FIREWALL=PROVISIONAL
M3_T11_FIXED_SQUARECLASS_BO1_PROVED=false
M3_T11_DENOMINATOR_EXTREME_SUPPORT_DEFICIT_PROVED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false


LATEST_RESEARCH_CARD=M3-T11-102
LATEST_AUDITED_RESEARCH_CARD=M3-T11-101
PROVISIONAL_FRONTIER_CARD=M3-T11-102
PROVISIONAL_FRONTIER_AUDIT_STATUS=HOSTILE_AUDIT_REQUIRED
CURRENT_ATTACK=GenericFullSThetaNonzeroFourthPowerSupportOneTwelfth|InteriorSymmetricProductSplittingIncidence
NEXT_ATTACK=ThetaFourthPowerMovingSupportBeyondKummer|Interior2PiSquareclassSurfaceQSupport
NEXT_LEGAL_ACTION=Hostile-audit M3-T11-102. Mainbatch may continue on a same-measure bound for realized q / exact-Pi support inside one d=[2*Pi], or on a genuinely global theorem for the genus-3 square-coordinate cover across moving u, or on the independent theta moving-support route. Do not count fixed-Pi genus-5 slices as if the splitting field fixed Pi.
NEXT_RESEARCH_CARD_ID=M3-T11-103


## AUDIT PROMOTION — M3-T11-102
AUDIT_DOC_ID=1dlK8Pyj6HCa3sE2Ha-73NnH3W9-hSNn_yVpC9ueHx4k
HOSTILE_AUDIT=PASS
AUDITED_CARD=M3-T11-102
LATEST_AUDITED_RESEARCH_CARD=M3-T11-102


M3-T11-102 STATUS=PROVED_EXACT / HOSTILE_AUDIT_PASS / EXACT_SQUARECLASS_GEOMETRY / FIXED_SQUARECLASS_SURFACE / GENUS3_DOUBLE_COVER / FIXED_PI_OVERREFINEMENT_FIREWALL / NO POWER SAVING


CANONICAL_AUDIT_CONSEQUENCES:
- [2*Pi]=[2*S*(1+u^2)]=[2*s*t*N_u], and on Q(S,u)!=0 also [2*Pi]=[-2*S*Q(S,u)].
- For 2*Pi=d*q^2 with signed squarefree d, every relative-fresh p^lambda has p not dividing d and v_p(q)=-2*lambda; the resulting M_rel^2 denominator has zero independent saving credit.
- Fixed d leaves a two-dimensional endpoint surface. Fixed Pi is a stricter q^2-fixed slice and its genus-5 geometry cannot be charged as a fixed-squareclass theorem.
- For fixed rational d!=0 and rational physical u!=0, the q-fiber is smooth degree 8 / genus 3.
- The q->-q quotient is the already-audited Section-35 fixed-u genus-one incidence after x=d*q^2=2*Pi.


M3_T11_2PI_SQUARECLASS_SYMMETRIC_REPRESENTATIONS=true
M3_T11_FIXED_SQUARECLASS_Q_MREL2_DENOMINATOR=true
M3_T11_FIXED_SQUARECLASS_Q_DENOMINATOR_INDEPENDENT_SAVING=false
M3_T11_FIXED_2PI_SQUARECLASS_RECEIVER_DIMENSION=2
M3_T11_FIXED_2PI_SQUARECLASS_FIXED_U_GENUS3=true
M3_T11_FIXED_2PI_SQUARECLASS_GENUS3_ELLIPTIC_QUOTIENT_OLD=true
M3_T11_FIXED_PI_GENUS5_OVERREFINEMENT_FIREWALL=true
M3_T11_FIXED_SQUARECLASS_BO1_PROVED=false
M3_T11_DENOMINATOR_EXTREME_SUPPORT_DEFICIT_PROVED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
SURVIVING_FRONTIER=ThetaFourthPowerMovingSupportBeyondKummer|Interior2PiSquareclassSurfaceQSupport
NEXT_RESEARCH_CARD_ID=M3-T11-103
