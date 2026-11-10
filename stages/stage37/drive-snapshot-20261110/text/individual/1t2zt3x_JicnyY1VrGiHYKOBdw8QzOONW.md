# M3-T11-096 — On the surviving theta!=0 full-S branch, the normalized theta congruence makes the M3-T11-092 residual-character lock automatic, and ordinary rational-2-torsion/2-isogeny descent loses the fresh M_rel^2 conductor in its Kummer class. These are not independent saving routes.

CARD_ID: M3-T11-096
CANONICAL_CARD_KEY: M3-T11-096
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-096
現行一覧の状態: PROVED_EXACT / HOSTILE_AUDIT_PASS / CHARACTER-COLLAPSE / 2-ISOGENY NO-GO / NO POWER SAVING
種別: EXACT_STRUCTURE / SAME_MEASURE NO-DOUBLE-CHARGE / 2-ISOGENY NO-GO / CHARACTER-REDUNDANCY
要点: On the surviving theta!=0 full-S branch, the normalized theta congruence makes the M3-T11-092 residual-character lock automatic, and ordinary rational-2-torsion/2-isogeny descent loses the fresh M_rel^2 conductor in its Kummer class. These are not independent saving routes.
主張の抜粋: With M=M_rel, ell=M^2 L, kappa=(v+1)/M^2=N_0/b^2 and Theta=theta/M^4, 16L+3kappa=M^2Theta, so L==-3kappa/16 mod M^2. Since W_flat^2=-N_0 Phi_flat, 3L Phi_flat==(3W_flat/(4b))^2 mod M^2. Also E_theta^-: Z^2=X(X^2+(9+4theta)X+4theta), X=-(v+1), maps under the standard 2-isogeny to dual X=(3-2w)^2; the source Kummer class is [-N_0] and the dual class is trivial. The isogeny factorization is exactly the known M^2 times M^2 split of theta M^4.
対象・測度: Exact fixed-content/coefficient nondegenerate generic full-S-denominator physical branch with R<=B and theta!=0. Same physical measure; no fixed-power saving credit.
依存関係: M3-T11-090..095 audited; especially M3-T11-092 normalized endpoint square/character lock, M3-T11-093 theta M_rel^4 carrier/fixed-theta elliptic curve, M3-T11-094 full-S normalization, M3-T11-095 Z/w tangent identity.
再開条件の抜粋: Reopen only if an audited dependency changes, or a genuinely new global theorem uses information strictly beyond the audited theta/squareclass identities and proves a same-physical-measure moving-support/dispersion deficit.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 106.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 888199
SOURCE_END: 895923
SOURCE_SHA256: 695629b8e0d96906393f802fbc011e0a2af05cbc829c6356679264fc894f99ff

## M3-T11-096 — PROVISIONAL EXACT REDUNDANCY / NO-DOUBLE-CHARGE FIREWALL
Research status: PROVISIONAL; hostile audit required before canonical promotion.
Scope: same fixed-content/coefficient nondegenerate generic full-S-denominator physical branch with theta!=0 and R<=B. No theorem, endpoint, or Perfect Cuboid nonexistence credit.


Exact normalization:
M=M_rel,
N_u=M^2*N_0,
t=M^2*t_0,
ell=M^2*L,
kappa=(v+1)/M^2=N_0/b^2,
Theta=theta/M^4.
From theta=16ell+3(v+1),
boxed:
16L+3kappa=M^2*Theta,
so
boxed:
L==-3kappa/16 mod M^2.


Normalized-theta residue formula:
with w=M^2*omega, omega=a*t_0/(b*s), x=kappa/(16omega),
boxed:
Theta=kappa*(kappa-12omega+4M^2omega^2)/(4v),
and therefore
boxed:
Theta==16*(t_0/s)^2*x*(4x-3) mod M^2.
This identifies the normalized theta squareclass at exact-saturation fresh primes but gives no density credit by itself.


Residual-character redundancy:
audited M3-T11-092 gives
W_flat^2=-N_0*Phi_flat.
Since kappa=N_0/b^2,
kappa*Phi_flat=-(W_flat/b)^2.
Therefore
boxed:
3L*Phi_flat==(3W_flat/(4b))^2 mod M^2.
Hence the M3-T11-092 unit-square character lock is implied on the surviving theta branch by the theta M^4 identity plus the normalized endpoint square. It cannot be multiplied with theta as an independent saving and is not a standalone theta-branch dispersion condition unless supplemented by genuinely new global information.


2-isogeny redundancy:
translate the audited fixed-theta elliptic curve by X=-(v+1):
boxed:
E_theta^-: Z^2=X(X^2+(9+4theta)X+4theta).
The standard rational 2-isogenous model is
boxed:
E_theta^+: Y^2=Xp(Xp^2-2(9+4theta)Xp+16theta^2+56theta+81),
with
Xp=Z^2/X^2,
Y=Z(4theta-X^2)/X^2.
For the physical point Z=(v+1)(3-2w), define q=3-2w and k=(4theta-(v+1)^2)/(v+1). Then
boxed:
phi(P)=(q^2,qk).
Thus the dual Kummer class is trivial. The source Kummer class is
boxed:
[X]=[-(v+1)]=[-N_0] in Q*/Q*^2,
so the fresh M^2 factor is invisible to the ordinary 2-isogeny squareclass map.
Moreover
(q^2-(9+4theta)-k)(q^2-(9+4theta)+k)=16theta,
with factors
-2(1+v-12w+4w^2)/v
and
-2(1+v).
On full-S these are precisely the already-known M^2 theta-cofactor and M^2 (v+1) factors. Their product is the old theta M^4 carrier, not a new split saving.


No-double-charge / route verdict:
- FullSDefectResidualCharacterDispersionOneTwelfth is retired PROVISIONALLY as a standalone theta-branch attack.
- Ordinary fixed-theta rational-2-torsion / 2-isogeny Kummer descent is retired PROVISIONALLY as a fresh-conductor detector.
- GenericFullSThetaNonzeroFourthPowerSupportOneTwelfth remains load-bearing.
- InteriorCharacterGlobalDispersion remains available only if it uses information genuinely independent of the collapsed M3-T11-092 character.
- no fixed-power saving is proved.


FLAGS:
M3_T11_THETA_NORMALIZED_CONGRUENCE=PROVISIONAL_TRUE
M3_T11_THETA_NORMALIZED_SQUARECLASS_X_4XMINUS3=PROVISIONAL
M3_T11_092_CHARACTER_INDEPENDENT_ON_THETA_BRANCH=PROVISIONAL_FALSE
M3_T11_THETA_2ISOGENY_SOURCE_KUMMER_CLASS_MINUS_N0=PROVISIONAL_TRUE
M3_T11_THETA_2ISOGENY_DUAL_KUMMER_CLASS_TRIVIAL=PROVISIONAL_TRUE
M3_T11_THETA_2ISOGENY_FRESH_CONDUCTOR_VISIBLE=PROVISIONAL_FALSE
M3_T11_THETA_2ISOGENY_NEW_SAVING=PROVISIONAL_FALSE
M3_T11_FULL_S_RESIDUAL_CHARACTER_STANDALONE_ATTACK_RETIRED=PROVISIONAL
M3_T11_DENOMINATOR_EXTREME_SUPPORT_DEFICIT_PROVED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
LATEST_RESEARCH_CARD=M3-T11-096
LATEST_AUDITED_RESEARCH_CARD=M3-T11-095
PROVISIONAL_FRONTIER_CARD=M3-T11-096
PROVISIONAL_FRONTIER_AUDIT_STATUS=REQUIRED
CURRENT_ATTACK=GenericFullSThetaNonzeroFourthPowerSupportOneTwelfth|InteriorCharacterGlobalDispersion
NEXT_ATTACK=ThetaFourthPowerMovingSupportBeyondSquareclass|InteriorCharacterGlobalDispersion
NEXT_RESEARCH_CARD_ID=M3-T11-097
NEXT_LEGAL_ACTION=Hostile-audit M3-T11-096 before canonical retirement; mainbatch continuation before audit must keep zero saving credit and avoid squareclass/2-isogeny loops
## M3-T11-096 — HOSTILE AUDIT PROMOTION
Research status: PROVED_EXACT / HOSTILE_AUDIT_PASS / SAME-MEASURE NO-DOUBLE-CHARGE / NO POWER SAVING.
AUDIT_DOC_ID=1cGtPtIX2-9NmEG0OaR-zWxtPRsj2RqSDeJhr7T_V_eY
AUDIT_RESULT=PASS
Audited claims:
- 16*L+3*kappa=M^2*Theta exactly and L==-3*kappa/16 mod M^2.
- Theta==16*(t_0/s)^2*x*(4*x-3) mod M^2; this is an exact router only.
- 3*L*Phi_flat==(3*W_flat/(4*b))^2 mod M^2, so the M3-T11-092 residual-character condition is dependent on theta M^4 plus the normalized endpoint square on the surviving theta branch.
- For the translated fixed-theta elliptic curve, the standard 2-isogeny sends the physical point to dual X=(3-2w)^2. Source Kummer class is [-N_0]; dual class is trivial; the fresh M_rel^2 square factor is invisible.
- The two isogeny factors are exactly the retained M^2 by M^2 factorization of theta M^4. No independent fresh-conductor factor or support deficit is obtained.
Canonical route consequences:
FullSDefectResidualCharacterDispersionOneTwelfth standalone theta-branch attack = RETIRED.
Ordinary fixed-theta rational-2-torsion / 2-isogeny Kummer fresh-conductor attack = RETIRED.
GenericFullSThetaNonzeroFourthPowerSupportOneTwelfth remains load-bearing.
InteriorCharacterGlobalDispersion remains legal only if it uses information genuinely independent of the collapsed M3-T11-092 character.
FLAGS:
M3_T11_096_HOSTILE_AUDIT=PASS
M3_T11_THETA_NORMALIZED_CONGRUENCE=true
M3_T11_THETA_NORMALIZED_SQUARECLASS_X_4XMINUS3=true
M3_T11_092_CHARACTER_INDEPENDENT_ON_THETA_BRANCH=false
M3_T11_THETA_2ISOGENY_SOURCE_KUMMER_CLASS_MINUS_N0=true
M3_T11_THETA_2ISOGENY_DUAL_KUMMER_CLASS_TRIVIAL=true
M3_T11_THETA_2ISOGENY_FRESH_CONDUCTOR_VISIBLE=false
M3_T11_THETA_2ISOGENY_NEW_SAVING=false
M3_T11_FULL_S_RESIDUAL_CHARACTER_STANDALONE_ATTACK_RETIRED=true
M3_T11_THETA_ORDINARY_2ISOGENY_FRESH_CONDUCTOR_ATTACK_RETIRED=true
M3_T11_DENOMINATOR_EXTREME_SUPPORT_DEFICIT_PROVED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
LATEST_RESEARCH_CARD=M3-T11-096
LATEST_AUDITED_RESEARCH_CARD=M3-T11-096
PROVISIONAL_FRONTIER_CARD=NONE
PROVISIONAL_FRONTIER_AUDIT_STATUS=NOT_APPLICABLE
CURRENT_ATTACK=GenericFullSThetaNonzeroFourthPowerSupportOneTwelfth|InteriorCharacterGlobalDispersion
NEXT_ATTACK=ThetaFourthPowerMovingSupportBeyondSquareclass|InteriorCharacterGlobalDispersion
NEXT_RESEARCH_CARD_ID=M3-T11-097
NEXT_LEGAL_ACTION=Continue from M3-T11-097 on genuinely new same-physical-measure theta moving-support/global-dispersion information beyond the audited squareclass identities.






## Historical hostile-audit promotion — M3-T11-081 / M3-T11-082
AUDIT_DOC_ID=1w8gqZwla4lkElFMhd76PaIR4iFduZ9EjLRrwx3EdfqQ
AUDIT_RESULT=PASS
M3-T11-081:
- F(r,s)=r^4+4*s^4=D*(epsilon*M_rel*h)^2 exactly on the primitive x=-1/8 physical carrier.
- The distinguished point P_D=(-alpha^2,alpha*beta*gamma) lies on y^2=x^3-D^2*x with X+D=beta^2 and X-D=-gamma^2.
- Every realized D is in the corresponding non-2-torsion congruent-number class.
M3-T11-082:
- P_D=(-b^2/q^2,a*b*c/q^3), q=M_rel*h, is the same point.
- gcd(q,a*b*c)=1; hence q is exactly the standard denominator root in the integral Weierstrass model.
- H_x(P_D)=max(b^2,q^2), q^2<=H_x(P_D)<=D*q^2.
- On M_rel>B^(1/12-eta), q>B^(1/12-eta) and H_x(P_D)>B^(1/6-2*eta).
NO_DOUBLE_CHARGE:
081 and 082 are two coordinate descriptions of one rational point. No independent density saving may be multiplied.
FLAGS:
M3_T11_081_HOSTILE_AUDIT=PASS
M3_T11_082_HOSTILE_AUDIT=PASS
M3_T11_081_082_SAME_RATIONAL_POINT=true
M3_T11_081_082_INDEPENDENT_SAVINGS=false
M3_T11_X_MINUS_ONE_EIGHTH_ACTIVE_D_SUPPORT_DEFICIT_PROVED=false
M3_T11_X_MINUS_ONE_EIGHTH_POWER_SAVING_PROVED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
LATEST_AUDITED_RESEARCH_CARD=M3-T11-096
NEXT_RESEARCH_CARD_ID=M3-T11-097
0
