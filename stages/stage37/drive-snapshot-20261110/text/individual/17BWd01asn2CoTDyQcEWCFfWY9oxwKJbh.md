# M3-T11-108 — For the M3-T11-105 residual quartic, the standard cubic resolvent is irreducible over Q for every nonzero rational u. Hence the rational resolvent-reducible exceptional branch is empty and no rational 2+2 quartic specialization exists for u!=0.

CARD_ID: M3-T11-108
CANONICAL_CARD_KEY: M3-T11-108
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-108
現行一覧の状態: PROVED_EXACT / HOSTILE_AUDIT_PASS / UNIFORM_RATIONAL_RESOLVENT_IRREDUCIBILITY / EXCEPTIONAL_SPECIALIZATION_CUT / TWO_QUADRATIC_SPECIALIZATION_NO_GO / NO POWER SAVING
種別: EXACT_STRUCTURE / EXCEPTIONAL_SPECIALIZATION_CONTROL / ELLIPTIC_DESCENT / ANTI_LOOP_FIREWALL
要点: For the M3-T11-105 residual quartic, the standard cubic resolvent is irreducible over Q for every nonzero rational u. Hence the rational resolvent-reducible exceptional branch is empty and no rational 2+2 quartic specialization exists for u!=0.
主張の抜粋: With v=u^2 the resolvent-root curve F(v,y)=0 has rational normalization v=-(t-2)(t+1)^2/((t+4)(t^2-4t+13)). Requiring v to be a rational square gives W^2=-(t-2)(t+4)(t^2-4t+13), birational to E: Y^2=x(x^2+2x+5). Exact 2-isogeny descent gives rank E(Q)=0 and E(Q)={O,(0,0)}; back-substitution gives only u=0 or a pole. The 1+3 quartic-factor and A4 discriminant-square branches remain open, so uniform S4 is not claimed.
対象・測度: Exact fixed-content/coefficient nondegenerate Stage37 physical endpoint population with R<=B; theorem uniform for all u in Q^*; same measure; no density, height, denominator, multiplicity, primary-gate, endpoint, or P-over-M3 credit.
依存関係: M3-T11-105/106/107 HOSTILE_AUDIT_PASS; exact standard cubic resolvent; exact symbolic elimination/parametrization; standard 2-isogeny descent and good-reduction torsion facts.
再開条件の抜粋: Reopen if hostile audit rejects the resolvent convention, F(v,y), the rational normalization/inverse, the square-pullback elliptic model, the 2-isogeny descent, or the torsion computation; or if an audited dependency changes.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 122.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 961020
SOURCE_END: 967548
SOURCE_SHA256: 9dadcf6d59b6e1f0b996108030f3f3e5478b3bd299323268d499ac0d322a4f02

M3-T11-108
STATUS=PROVISIONAL / UNIFORM_RATIONAL_RESOLVENT_IRREDUCIBILITY / EXCEPTIONAL_SPECIALIZATION_CUT / TWO_QUADRATIC_SPECIALIZATION_NO_GO / HOSTILE_AUDIT_REQUIRED / NO POWER SAVING
TYPE=EXACT_STRUCTURE / EXCEPTIONAL_SPECIALIZATION_CONTROL / ELLIPTIC_DESCENT / ANTI_LOOP_FIREWALL
SUMMARY=For the M3-T11-105 residual quartic Q_u, the standard cubic resolvent is irreducible over Q for every nonzero rational u. Equivalently, the rational resolvent-reducible exceptional-specialization branch is empty on u in Q^*. Consequently Q_u has no rational 2+2 factorization for any u in Q^*. This does not prove uniform quartic irreducibility or uniform S4: the 1+3 quartic-factor branch and the A4 discriminant-square branch remain separate.


EXACT_RESOLVENT_ROOT_CURVE:
Set v=u^2. A rational root y of the cleared standard cubic resolvent lies on
F(v,y)=(v+1)^3*y^3+(-11*v^3-21*v^2-9*v+1)*y^2+4*v*(v-11)*(v+1)*y-4*v*(11*v^2+3*v+8)=0.
Disc_y(F)=-16*v*(v+1)^8*(25*v-2)^3.
Disc_v(F)=-256*(y+1)*(27*y+28)^3.


NORMALIZATION:
v=-(t-2)*(t+1)^2/((t+4)*(t^2-4*t+13)).
y=-(t+1)*(2*t^2-11*t+23)/27.
Inverse away from the finite exceptional locus:
t=-2*(3*v*y+17*v+3*y+2)/(3*v*y-8*v+3*y+4).
On F the inverse denominator can vanish only at v=-1 or v=2/25; neither is a nonzero rational square.


SQUARE_PULLBACK:
For u!=0, with r=u/(t+1),
r^2=-(t-2)/((t+4)*(t^2-4*t+13)).
Equivalently
W^2=-(t-2)*(t+4)*(t^2-4*t+13).
With X=-6/(t-2), Y=2W/(t-2)^2, x=X-1 this is
E: Y^2=x*(x^2+2*x+5).


ELLIPTIC_DESCENT:
For E: Y^2=x^3+2*x^2+5*x, the 2-isogeny alpha image is {1,5}. The dual curve is Ebar: Y^2=x^3-4*x^2-16*x. Its possible extra squareclasses +/-2 would require
N^2=2*m^4-4*m^2*e^2-8*e^4
or
N^2=-2*m^4-4*m^2*e^2+8*e^4,
which are impossible mod 16 for primitive m,e in all parity cases. Thus the dual alpha image is {1,-1}, and the 2-isogeny rank formula gives rank E(Q)=0.
At p=3, #E(F_3)=2. The 3-division polynomial is (x+1)*(3*x^3+5*x^2+25*x-25); the cubic factor is irreducible over Q and x=-1 gives Y^2=-4. Hence E(Q) has no rational 3-torsion and E(Q)={O,(0,0)}.


BACK_SUBSTITUTION:
O maps to t=2 and v=0. The point (0,0) maps to t=-4, a pole of v(t). The canceled t=-1 also gives only v=0. Therefore no finite u in Q^* yields a rational resolvent root.


IMPLIES:
M3_T11_RATIONAL_U_NONZERO_CUBIC_RESOLVENT_IRREDUCIBLE=PROVISIONAL
M3_T11_RATIONAL_U_NONZERO_TWO_QUADRATIC_SPECIALIZATION=false
M3_T11_EXCEPTIONAL_RESOLVENT_REDUCIBLE_BRANCH_EMPTY=PROVISIONAL
M3_T11_UNIFORM_RATIONAL_U_QUARTIC_IRREDUCIBILITY_PROVED=false
M3_T11_UNIFORM_RATIONAL_U_S4_PROVED=false
M3_T11_FIXED_SQUARECLASS_FULL_GENUS2_SELMER_COLLAPSE_PROVED=false
M3_T11_DENOMINATOR_EXTREME_SUPPORT_DEFICIT_PROVED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false


POPULATION=Exact fixed-content/coefficient nondegenerate Stage37 physical endpoint population with R<=B. The resolvent theorem is uniform for all u in Q^*. Same physical measure; no density, height, denominator, or multiplicity change.
DEPENDS_ON=M3-T11-105/106/107 HOSTILE_AUDIT_PASS; exact M3-T11-105 standard resolvent; exact symbolic elimination/parametrization; standard 2-isogeny descent and good-reduction torsion facts.
DO_NOT_REPEAT=Do not search for rational roots of the standard cubic resolvent or rational 2+2 factorizations for u!=0. Do not infer uniform S4 or uniform quartic irreducibility. Do not claim a power saving from this structural empty-branch theorem.
REOPEN_CONDITION=Hostile audit rejects the resolvent convention, F(v,y), the rational normalization/inverse, the square-pullback elliptic model, the 2-isogeny descent, or the torsion computation; or an audited dependency changes.
DETAIL_DOC=K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 122.


LATEST_RESEARCH_CARD=M3-T11-108
LATEST_AUDITED_RESEARCH_CARD=M3-T11-107
PROVISIONAL_FRONTIER_CARD=M3-T11-108
PROVISIONAL_FRONTIER_AUDIT_STATUS=HOSTILE_AUDIT_REQUIRED
CURRENT_ATTACK=GenericFullSThetaNonzeroFourthPowerSupportOneTwelfth|InteriorS4EtaleGlobalNonlocalSupport
NEXT_ATTACK=ThetaFourthPowerMovingSupportBeyondKummer|InteriorS4EtaleGlobalClassCorrelationOrRemainingExceptionalA4OnePlusThreeControl
NEXT_LEGAL_ACTION=Hostile-audit M3-T11-108. Mainbatch may continue only with the remaining exact 1+3 quartic-specialization locus, the A4 discriminant-square specialization locus, genuinely global/nonlocal S4 etale-Selmer information beyond the primewise local tuple, or the independent theta moving-support route.
NEXT_RESEARCH_CARD_ID=M3-T11-109




## AUDIT PROMOTION — M3-T11-108
HOSTILE_AUDIT=PASS
AUDITED_CARD=M3-T11-108
AUDIT_DOC_ID_108=18rDf9voOTpj4g2uwdIG8nPLYMRWjHv1Iy7FvRafNIgE
LATEST_RESEARCH_CARD=M3-T11-108
LATEST_AUDITED_RESEARCH_CARD=M3-T11-108
PROVISIONAL_FRONTIER_CARD=NONE
PROVISIONAL_FRONTIER_AUDIT_STATUS=NOT_APPLICABLE


M3_T11_108_HOSTILE_AUDIT=PASS
M3_T11_RATIONAL_U_NONZERO_CUBIC_RESOLVENT_IRREDUCIBLE=true
M3_T11_RATIONAL_U_NONZERO_TWO_QUADRATIC_SPECIALIZATION=false
M3_T11_EXCEPTIONAL_RESOLVENT_REDUCIBLE_BRANCH_EMPTY=true
M3_T11_UNIFORM_RATIONAL_U_QUARTIC_IRREDUCIBILITY_PROVED=false
M3_T11_UNIFORM_RATIONAL_U_S4_PROVED=false
M3_T11_FIXED_SQUARECLASS_FULL_GENUS2_SELMER_COLLAPSE_PROVED=false
M3_T11_DENOMINATOR_EXTREME_SUPPORT_DEFICIT_PROVED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false


AUTHORITY_SUMMARY=M3-T11-108 is hostile-audit PASS. For every nonzero rational u, the standard cubic resolvent of the M3-T11-105 residual quartic is irreducible over Q, so the rational resolvent-reducible exceptional branch and every rational 2+2 quartic specialization are empty. This gives exact exceptional-specialization control only: the rational 1+3 quartic-factor branch and the A4 discriminant-square branch remain live, and no counting saving is charged.


CURRENT_ATTACK=GenericFullSThetaNonzeroFourthPowerSupportOneTwelfth|InteriorS4EtaleGlobalNonlocalSupport
NEXT_ATTACK=ThetaFourthPowerMovingSupportBeyondKummer|InteriorS4EtaleGlobalClassCorrelationOrRemainingExceptionalA4OnePlusThreeControl
NEXT_RESEARCH_CARD_ID=M3-T11-109
NEXT_LEGAL_ACTION=Mainbatch may continue only with the exact rational 1+3 quartic-specialization locus, the A4 discriminant-square locus, genuinely global/nonlocal S4 etale-Selmer information beyond the primewise local tuple, or the independent theta moving-support route. Do not reopen rational resolvent-root or rational 2+2 specialization searches for u!=0. No fixed-power, primary-gate, endpoint, P(B)/M3(B), or Perfect Cuboid nonexistence credit
