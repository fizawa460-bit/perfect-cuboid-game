# M3-T11-053 — Exact quadratic-twist identification for the x=27/40 E2 saturation lookup

CARD_ID: M3-T11-053
CANONICAL_CARD_KEY: M3-T11-053
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-053
現行一覧の状態: PROVED_EXACT_FIREWALL / SATURATION_INDEX_BOUND_OPEN
種別: FIREWALL / EXACT_STRUCTURE
要点: For the Stage37 elliptic quotient
主張の抜粋: For the Stage37 elliptic quotient E_2: V^2=U*(U^2+1244*U+562500), the change X=U+1244/3 gives V^2=X^3+(139964/3)X-2447480432/27. Let E_0 denote the short-model representative of the LMFDB 210.d8 base twist class obtained from the displayed short model of 35490.bo8 by undoing its recorded twist by 13: E_0: y^2=x^3+94475
対象・測度: Exact x=27/40 singular physical carrier inherited from M3-T11-045 through M3-T11-052. No population or height change.
依存関係: M3-T11-050; M3-T11-051; M3-T11-052; exact algebraic short-Weierstrass conversion; external database preflight recording that LMFDB 35490.bo8 has the same j-invariant and is the twist by 13 of 210.d8.
再開条件の抜粋: Identify the exact quadratic twist-[2] database/CAS model of 210.d8, write an explicit Q-isomorphism to Stage37 E_2, and compare a certified Mordell-Weil basis with Q; alternatively prove I<257 independently.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 60.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 695425
SOURCE_END: 707052
SOURCE_SHA256: 3805e4fac69bfdc4fdb7d8e44eb6c4515bcc58228d7e2b06b6ab470e8e4f8cbd

## M3-T11-053


ID:
M3-T11-053


TYPE:
FIREWALL / EXACT_STRUCTURE


TITLE:
Exact quadratic-twist identification for the x=27/40 E2 saturation lookup


STATUS:
PROVED_EXACT_FIREWALL / SATURATION_INDEX_BOUND_OPEN


CLAIM:
For the Stage37 elliptic quotient


E_2:
V^2=U*(U^2+1244*U+562500),


the change X=U+1244/3 gives


V^2=X^3+(139964/3)X-2447480432/27.


Let E_0 denote the short-model representative of the LMFDB 210.d8 base twist class obtained from the displayed short model of 35490.bo8 by undoing its recorded twist by 13:


E_0:
y^2=x^3+944757x-8260246458.


Then exactly


139964/3=944757*(2/9)^2,
-2447480432/27=-8260246458*(2/9)^3.


Hence Stage37 E_2 is the quadratic twist of E_0 by d=2/9, i.e. twist squareclass [2].


LMFDB 35490.bo8 is twist squareclass [13] of the same base class. Therefore the relative twist class is


[(2/9)/13]=[26].


Because 26 is nonsquare in Q and the common j-invariant
42841933504271/13565917968750
is neither 0 nor 1728, Stage37 E_2 and 35490.bo8 are not Q-isomorphic.


POPULATION:
Exact x=27/40 singular physical carrier inherited from M3-T11-045 through M3-T11-052. No population or height change.


HEIGHT:
Exact physical R<=B remains inherited.


DEPENDS_ON:
M3-T11-050;
M3-T11-051;
M3-T11-052;
exact algebraic short-Weierstrass conversion;
external database preflight recording that LMFDB 35490.bo8 has the same j-invariant and is the twist by 13 of 210.d8.


IMPLIES:
The Mordell-Weil generator displayed for 35490.bo8 cannot be imported to Stage37 E_2 via a Q-isomorphism and gives no saturation certificate for Q=(50,5600).


Any external database/CAS basis route must identify the exact twist-[2] member of the 210.d8 family and verify an explicit Q-isomorphism to Stage37 E_2 before comparing generators.


ALIASES:
X27Over40ExactTwist2Model;
X27Over40SameJGeneratorImportFirewall;
X27Over40LMFDBTwistClassFirewall.


DUPLICATE_OF:
none.


SUPERSEDES:
The unverified shortcut that a same-j rank-one curve such as 35490.bo8 can donate its Mordell-Weil generator directly to Stage37 E_2.


DO_NOT_REPEAT:
Do not infer Q-isomorphism from equality of j-invariants.
Do not use the 35490.bo8 generator to claim I=1.
Do not use rank agreement alone to transfer a Mordell-Weil basis across a nontrivial quadratic twist.
Do not promote generator status until the exact twist-[2] model is identified and explicitly Q-isomorphic to E_2, or an independent I<257 proof is obtained.


REOPEN_CONDITION:
Identify the exact quadratic twist-[2] database/CAS model of 210.d8, write an explicit Q-isomorphism to Stage37 E_2, and compare a certified Mordell-Weil basis with Q; alternatively prove I<257 independently.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 60.


FLAGS:
M3_T11_X_27_OVER_40_E2_TWIST_CLASS_2_OVER_210D8=true
M3_T11_X_27_OVER_40_35490_BO8_RELATIVE_TWIST_CLASS_26=true
M3_T11_X_27_OVER_40_35490_BO8_Q_ISOMORPHIC_TO_E2=false
M3_T11_X_27_OVER_40_SAME_J_GENERATOR_IMPORT_FIREWALL=true
M3_T11_X_27_OVER_40_E2_INDEX_UPPER_BOUND_LT_257_PROVED=false
M3_T11_X_27_OVER_40_E2_P_SATURATED_GENERATOR_PROVED=false
P_OVER_M3_LIMIT_PROVED=false


CURRENT_X27_FIRST_ATTACK=X27Over40ExactTwist2ModelAndMordellWeilBasisIdentification
CURRENT_X27_SECOND_ATTACK=X27Over40E2IndexUpperBoundBelow257
CURRENT_X27_THIRD_ATTACK=X27Over40E2TorsionNormalizedTranslatedLiftMordellWeilSieve
CURRENT_X27_FALLBACK=X27Over40SplitJacobianQuadraticChabauty








M3-T11-053 ADDENDUM — exact integral twist-[2] model and Q-isomorphism


The twist-class statement has an explicit integral representative.


From
X=U+1244/3
put
x=9X=9U+3732,
y=27V.


Then direct substitution gives exactly


y^2=x^3+3779028*x-66081971664.


For the chosen 210.d8 base-class representative


E_0:
y^2=x^3+944757*x-8260246458,


the standard short twist by d=2 is


E_0^(2):
y^2=x^3+4*944757*x+8*(-8260246458)
=x^3+3779028*x-66081971664.


Therefore the map


(U,V) -> (x,y)=(9U+3732,27V)


is an explicit Q-isomorphism from Stage37 E_2 to this exact integral twist-[2] model, with inverse


U=(x-3732)/9,
V=y/27.


This strengthens the external-basis continuation: a database/CAS model is acceptable only after it is identified with this exact integral curve or connected to it by a verified Q-isomorphism.


M3_T11_X_27_OVER_40_E2_EXACT_INTEGRAL_TWIST2_MODEL=true


M3-T11-054 — Stage37 E2 exact same-j twist-screen / local-trace fingerprint


RESULT:
The x=27/40 elliptic quotient
E2: V^2=U*(U^2+1244*U+562500)
is already explicitly Q-isomorphic to
E_*: y^2=x^3+3779028*x-66081971664
via (x,y)=(9U+3732,27V), with Q_*=(4182,151200) and T_*=(3732,0).


Relative to the retained base short model
E_0: y^2=x^3+944757*x-8260246458,
Stage37 is twist squareclass [2].


Two additional same-j LMFDB candidates were checked exactly and excluded:
- 33600.df8 -> after x=X+1/3, short coefficients (3499100/3, 305935054000/27); coefficient ratios to E_0 are 100/81 and -1000/729, hence twist squareclass [-10].
- 35280.bj8 -> short coefficients (5143677,104935723522); coefficient ratios to E_0 are 49/9 and -343/27, hence twist squareclass [-21].
Since j is nonexceptional, neither is Q-isomorphic to Stage37 twist-[2]. Together with the existing 35490.bo8 twist-[13] exclusion, this forms a three-candidate same-j firewall.


Exact Stage37 good-prime local trace fingerprint:
11:(#E=12,a=0)
13:(#E=16,a=-2)
17:(#E=24,a=-6)
19:(#E=16,a=4)
23:(#E=24,a=0)
29:(#E=24,a=6)
31:(#E=36,a=-4)
37:(#E=40,a=-2)


Continuation rule:
candidate external models must match [2], match these local traces, and then be connected to E_* by an explicit Q-isomorphism before any Mordell-Weil generator/regulator is imported.


No endpoint credit. No saturation close. I remains 1 or >=257.


M3_T11_X_27_OVER_40_33600_DF8_TWIST_CLASS_MINUS10=true
M3_T11_X_27_OVER_40_35280_BJ8_TWIST_CLASS_MINUS21=true
M3_T11_X_27_OVER_40_SAME_J_DATABASE_TRAP_PANEL_3=true
M3_T11_X_27_OVER_40_E2_LOCAL_TRACE_FINGERPRINT_11_TO_37=true
M3_T11_X_27_OVER_40_E2_EXACT_DATABASE_LABEL_IDENTIFIED=false
M3_T11_X_27_OVER_40_E2_P_SATURATED_GENERATOR_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
M3-T11-055 — exact conductor-6720 isogeny-class identification
RESULT:
Stage37 x=27/40 E2 is already retained as twist squareclass [2] of the 210.d8 base class, with exact model
E_*: y^2=x^3+3779028*x-66081971664,
Q_*=(4182,151200), T_*=(3732,0).
LMFDB represents the conductor-6720 twist family by twist parameter 8, and [8]=[2]. The LMFDB curve 6720.bb5 records minimal quadratic twist 210.d5, twist by 8, and belongs to the 8-curve rank-1 isogeny class 6720.bb. Since quadratic twisting carries the entire Q-isogeny class functorially, the twist-[2] member corresponding to 210.d8 lies in exact isogeny class 6720.bb.
Independent check: the 6720.bb modular form has coefficients a_11=0, a_13=-2, a_17=-6, a_19=4, exactly matching the retained Stage37 trace fingerprint.
Thus the external-model search space is reduced exactly to the 8 members of 6720.bb.
Firewall: the exact individual member has not yet been directly read from the full class table/data; do not guess 6720.bb8 or import a generator by numbering analogy. Require exact j=42841933504271/13565917968750 plus explicit Q-isomorphism to E_*.
Saturation remains I=1 or I>=257; no endpoint/theorem credit.
Source: https://www.lmfdb.org/EllipticCurve/Q/6720/bb/5
M3_T11_X_27_OVER_40_E2_EXACT_ISOGENY_CLASS_6720_BB=true
M3_T11_X_27_OVER_40_E2_EXACT_DATABASE_LABEL_IDENTIFIED=false
M3_T11_X_27_OVER_40_E2_P_SATURATED_GENERATOR_PROVED=false
P_OVER_M3_LIMIT_PROVED=false






M3-T11-055 ADDENDUM A — exact small integral translation fingerprint for the 6720.bb member search
RESULT:
Retain all M3-T11-055 theorem/status flags. No new card is opened because this is an exact coordinate adapter inside the same external-model identification gate.


Starting from
E2: V^2=U*(U^2+1244*U+562500),
put
x=U+415,
y=V.
Then exact expansion gives
y^2=x^3-x^2+46655*x-90662975.
Thus the integral Weierstrass coefficient fingerprint is
[a1,a2,a3,a4,a6]=[0,-1,0,46655,-90662975].


The retained points become exactly
Q=(50,5600) -> Q_small=(465,5600),
T=(0,0) -> T_small=(415,0).


The exact relation with the retained integral short model
E_*: y_*^2=x_*^3+3779028*x_*-66081971664
is
x_*=9*x-3,
y_*=27*y,
with inverse
x=(x_*+3)/9,
y=y_*/27.


Exact invariants of this translated integral model are
c4=-2239424,
c6=78319373824,
Delta=-3556224000000000000
     =-2^19*3^4*5^12*7^3,
j=42841933504271/13565917968750.


These give a stricter direct-data fingerprint than j alone for resolving the individual member inside 6720.bb. A future database/CAS record may be accepted only after its model is explicitly Q-isomorphic to this coefficient fingerprint (equivalently to E_*).


External-database diagnostic:
the directly readable 6720.bb5 member is not the Stage37 curve: it has different j and rational torsion Z/2 x Z/2. Across independently readable twist-family classes 1470.m, 33600.df, 35280.bj and 35490.bo, the same target j occurs at suffix 8, so 6720.bb8 is a strong database-numbering candidate. This remains NON-CERTIFYING evidence only. The M3-T11-055 firewall is retained: do not promote the individual label until direct 6720.bb full-class/member data is read and the explicit Q-isomorphism is checked.


No proof of I<257 or I=1 is obtained here.
LATEST_RESEARCH_CARD remains M3-T11-055.
M3_T11_X_27_OVER_40_E2_SMALL_INTEGRAL_TRANSLATION_FINGERPRINT=true
M3_T11_X_27_OVER_40_E2_EXACT_DATABASE_LABEL_IDENTIFIED=false
M3_T11_X_27_OVER_40_E2_P_SATURATED_GENERATOR_PROVED=false
P_OVER_M3_LIMIT_PROVED=false


M3-T11-056 — x=27/40 E2 full Mordell-Weil saturation by explicit degree-6 isogeny
RESULT: EXACT / SATURATION CLOSED / SUPPORTING BRANCH ADVANCED.


Curve:
E2: V^2=U*(U^2+1244*U+562500), Q=(50,5600), T=(0,0), rank=1.


Exact chain:
1. 2-isogeny phi2 sends E2 to
   E3: Y^2=X*(X-2744)*(X+256)
   by X=V^2/U^2 and Y=V*(U^2-562500)/U^2,
   with phi2(Q)=(12544,-1254400).
2. psi3(E3)=(3X+1568)*(X^3-3840X^2+602112X-314703872), so the rational cyclic 3-isogeny kernel has x=-1568/3.
3. Velu quotient:
   C: y^2=x^3-2488x^2-(83643392/3)x+2341774131200/27.
   The map sends phi2(Q) to (38848/3,-1216512).
4. x_C=36*x_bb+2452/3, y_C=216*y_bb identifies C with LMFDB 6720.bb5:
   y_bb^2=x_bb^3-x_bb^2-23105x_bb+1346625.
   Therefore Q maps under the composite degree-6 isogeny to (337,-5632).
5. LMFDB 6720.bb5 gives free generator P=(67,308) and 2-torsion A=(81,0). Exact group law gives P+A=(337,5632). Thus phi(Q)=-(P+A), primitive modulo torsion.
6. In rank one, if Q=nG+torsion, every isogeny image has free coefficient divisible by n. Since phi(Q) has coefficient +/-1, |n|=1.


CONCLUSION:
E2(Q)=<Q> direct-sum <T> and I=[E2(Q):<Q,T>]=1.
The former alternative I=1 or I>=257 is now resolved on the I=1 side. The individual Stage37 LMFDB member label inside 6720.bb is no longer a proof blocker.


NEXT: run the torsion-normalized translated-lift Mordell-Weil sieve on X*(225-X)=14*s^2 with physical finite-point exclusions. Split-Jacobian quadratic Chabauty remains fallback.


No rational-point classification, fixed-power saving, or P/M3 theorem credit yet.


Sources:
LMFDB 6720.bb5 https://www.lmfdb.org/EllipticCurve/Q/6720/bb/5
Velu formulas https://people.cs.nycu.edu.tw/~rjchen/ECC2012S/Elliptic%20Curves%20Number%20Theory%20And%20Cryptography%202n.pdf


M3_T11_X_27_OVER_40_E2_EXPLICIT_DEGREE6_ISOGENY_TO_6720_BB5=true
M3_T11_X_27_OVER_40_E2_P_SATURATED_GENERATOR_PROVED=true
M3_T11_X_27_OVER_40_E2_INDEX_UPPER_BOUND_LT_257_PROVED=true
M3_T11_X_27_OVER_40_E2_INDEX_ONE=true
M3_T11_X_27_OVER_40_RATIONAL_POINTS_CLASSIFIED=false
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
