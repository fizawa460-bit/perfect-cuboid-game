# M3-T11-109 — ResidualQuarticRationalSpecializationTrichotomy

CARD_ID: M3-T11-109
CANONICAL_CARD_KEY: M3-T11-109
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-109
現行一覧の状態: PROVED_EXACT / HOSTILE_AUDIT_PASS / EXACT_SPECIALIZATION_CLASSIFICATION / ONE_PLUS_THREE_PARAMETRIZATION / A4_PARAMETRIZATION / DISJOINT_THIN_IMAGES / NO POWER SAVING
種別: EXACT_STRUCTURE / EXCEPTIONAL_SPECIALIZATION_CONTROL / THIN_SET_PARAMETERIZATION / GALOIS_CLASSIFICATION / FIREWALL
要点: For every nonzero rational u, the residual quartic specialization is exactly classified into three types: an explicit degree-4 rational 1+3 image with Gal=S3, an explicit degree-2 discriminant-square image with Gal=A4, and an S4 irreducible complement. The two exceptional images are disjoint. Hostile audit PASS; no physical power saving.
主張の抜粋: The rational-root locus is u=phi(t)=-2(t-1)(t^2-2t-1)/(t^4-6t^3+12t^2-14t+11), degree 4 with ambient u-height count O(H^(1/2)). The A4 locus is u=psi(t)=(t^2-2t-1)/(5(t^2+1)), degree 2 with ambient count O(H). Substitution reduces intersection to Y^2=2(r^4-16r^3s+72r^2s^2-124rs^3+71s^4), impossible mod 5 because the right side is always 2 or 3 on P^1(F_5). Combined with audited M3-T11-108, phi gives exactly 1+3/S3, psi gives irreducible/A4, and the complement gives irreducible/S4.
対象・測度: Exact fixed-content/coefficient nondegenerate Stage37 physical endpoint population with R<=B; classification uniform for all u in Q^*. The O(H^(1/2)) and O(H) counts are ambient projective u-height only, not physical B-exponents; no density, multiplicity, primary-gate, endpoint, or P-over-M3 credit.
依存関係: M3-T11-105/106/107/108 HOSTILE_AUDIT_PASS; exact residual quartic; exact symbolic discriminant/parametrization identities; standard conic parametrization, quartic Galois criterion, and P^1 height functoriality.
再開条件の抜粋: Reopen if hostile audit rejects the u-discriminant, phi/psi parametrizations, resultant/degree calculations, mod-5 disjointness obstruction, specialization trichotomy, or an audited dependency changes.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 123.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 967548
SOURCE_END: 974233
SOURCE_SHA256: 8a09952d9bbb0d04c68d26ab00d6f13a1d9fd1fbdd8d80e8dd8a2ed9e4b50d21

M3-T11-109
STATUS:
PROVISIONAL EXACT_SPECIALIZATION_CLASSIFICATION / ONE_PLUS_THREE_PARAMETRIZATION / A4_PARAMETRIZATION / DISJOINT_THIN_IMAGES / HOSTILE_AUDIT_REQUIRED / NO POWER SAVING


TYPE:
EXACT_STRUCTURE / EXCEPTIONAL_SPECIALIZATION_CONTROL / THIN_SET_PARAMETERIZATION / GALOIS_CLASSIFICATION / FIREWALL


SUMMARY:
For Q_u(z)=(1+u^2)z^4-8uz^3+(11u^2-1)z^2+6uz-u^2 and every u in Q^*, the rational-specialization types left after audited M3-T11-108 are completely classified. The rational 1+3 locus is exactly one explicit degree-4 P^1 image phi, the A4 discriminant-square locus is exactly one explicit degree-2 P^1 image psi, and the two images are disjoint. Consequently every rational specialization has exactly one of the Galois/factorization types S3(1+3), A4(irreducible), or S4(irreducible). This is exact specialization control, not a Stage37 counting saving.


CLAIM:
Regarded as a quadratic in u,
Disc_u(Q_u(z))=-4z^2(z^2-2)^3.
For u!=0, Q_u has a rational root iff z^2+w^2=2 for rational z,w, hence iff
u=phi(t)
=-2(t-1)(t^2-2t-1)/(t^4-6t^3+12t^2-14t+11)
for some t in P^1(Q), excluding the u=0 image.
In homogeneous coordinates
U_13=-2s(r-s)(r^2-2rs-s^2),
V_13=r^4-6r^3s+12r^2s^2-14rs^3+11s^4,
with Res_r(U_13,V_13)=-4096s^16.
Thus phi has degree 4 and h(phi(t))=4h(t)+O(1), giving ambient count O(H^(1/2)).


The quartic discriminant squareclass is [2-25u^2]. Its square locus is exactly
u=psi(t)=(t^2-2t-1)/(5(t^2+1)).
In homogeneous coordinates
U_A4=r^2-2rs-s^2,
V_A4=5(r^2+s^2),
with Res_r(U_A4,V_A4)=200s^4.
Thus psi has degree 2 and h(psi(t))=2h(t)+O(1), giving ambient count O(H).


Substitution into the discriminant gives
2-25phi(t)^2
=
2(t^2+2t-1)^2
(t^4-16t^3+72t^2-124t+71)
/(t^4-6t^3+12t^2-14t+11)^2.
The homogenized residual quartic F satisfies 2F(r,s) in {2,3} modulo 5 for every [r:s] in P^1(F_5), hence it is never a rational square. Therefore the phi and psi images are disjoint.


Combining with M3-T11-108:
- phi image: exactly 1+3 and Gal=S3;
- psi image: irreducible and Gal=A4;
- complement: irreducible and Gal=S4.


POPULATION:
Exact fixed-content/coefficient nondegenerate Stage37 physical endpoint population with R<=B. The algebraic classification itself is uniform for all u in Q^*. No change of measure, field, height, or multiplicity.


HEIGHT:
The O(H^(1/2)) and O(H) statements use ordinary multiplicative projective height of u and are ambient P^1 image counts. They are not B-exponents on the physical R<=B population. No fixed-power Stage37 saving is charged without a same-measure height/multiplicity adapter.


DEPENDS_ON:
M3-T11-105/106/107/108 HOSTILE_AUDIT_PASS; exact residual quartic; exact symbolic identities; standard conic parametrization; standard quartic Galois criterion; standard P^1 height functoriality.


IMPLIES:
The remaining rational exceptional-specialization algebra is explicit and finite-cover controlled. On the complement of two explicit disjoint thin images the residual quartic is uniformly S4. The next useful question is quantitative/physical: whether these images admit an exact same-measure R<=B saving, or whether the generic S4 branch yields genuinely global nonlocal Selmer/support information.


ALIASES:
ResidualQuarticRationalSpecializationTrichotomy;
ResidualQuarticOnePlusThreeDegree4Image;
ResidualQuarticA4Degree2Image;
ResidualQuarticExceptionalThinImagesDisjoint;
GenericRationalSpecializationUniformS4OutsidePhiPsi.


DUPLICATE_OF:
NONE.


SUPERSEDES:
The post-M3-T11-108 description in which the rational 1+3 and A4 specialization loci were still algebraically uncontrolled.


DO_NOT_REPEAT:
Do not reopen rational resolvent-root or 2+2 specialization searches for u!=0. Do not re-search the 1+3 or A4 loci as unknown sets. Do not assume the two loci overlap. Do not convert ambient u-height sparsity into a physical B-saving without an exact adapter.


REOPEN_CONDITION:
Hostile audit rejects the quadratic discriminant in u, phi or psi parametrization, resultant/degree calculation, mod-5 disjointness obstruction, Galois trichotomy, or an audited dependency changes.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 123.


CREDIT:
No fixed-power saving. No full S4-etale Selmer collapse. No primary-gate/endpoint/P-over-M3/Perfect-Cuboid credit.


FLAGS:
M3_T11_RATIONAL_U_REDUCIBLE_IFF_PHI_IMAGE=PROVISIONAL
M3_T11_RATIONAL_U_ONE_PLUS_THREE_PARAMETER_DEGREE4=PROVISIONAL
M3_T11_RATIONAL_U_A4_PARAMETER_DEGREE2=PROVISIONAL
M3_T11_RATIONAL_U_ONE_PLUS_THREE_AND_A4_DISJOINT=PROVISIONAL
M3_T11_RATIONAL_U_GALOIS_TRICHOTOMY_S3_A4_S4=PROVISIONAL
M3_T11_RATIONAL_U_ONE_PLUS_THREE_AMBIENT_HEIGHT_COUNT=O(H^(1/2))
M3_T11_RATIONAL_U_A4_AMBIENT_HEIGHT_COUNT=O(H)
M3_T11_EXCEPTIONAL_SPECIALIZATION_PHYSICAL_POWER_SAVING_PROVED=false
M3_T11_FIXED_SQUARECLASS_FULL_GENUS2_SELMER_COLLAPSE_PROVED=false
M3_T11_DENOMINATOR_EXTREME_SUPPORT_DEFICIT_PROVED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false


LATEST_RESEARCH_CARD=M3-T11-109
LATEST_AUDITED_RESEARCH_CARD=M3-T11-108
PROVISIONAL_FRONTIER_CARD=M3-T11-109
PROVISIONAL_FRONTIER_AUDIT_STATUS=HOSTILE_AUDIT_REQUIRED
CURRENT_ATTACK=GenericFullSThetaNonzeroFourthPowerSupportOneTwelfth|InteriorS4EtaleGlobalNonlocalSupport
NEXT_ATTACK=HostileAuditM3T11109ThenThetaFourthPowerMovingSupportBeyondKummer|InteriorS4EtaleGlobalClassCorrelationOrPhysicalThinSpecializationAdapter
NEXT_RESEARCH_CARD_ID=M3-T11-110
NEXT_LEGAL_ACTION=Hostile-audit M3-T11-109 first. If PASS, continue only with an exact same-measure physical counting adapter for the explicit phi/psi images, genuinely global/nonlocal S4 etale-Selmer information beyond the primewise local tuple, or the independent theta!=0 moving-support route.
.




---
AUDIT PROMOTION: M3-T11-109


HOSTILE_AUDIT=PASS
AUDIT_DOC_ID_109=1bpbYjj-zFftOLH2Hgor6O9XzFWrj_3mYPONFlCGemLc
LATEST_AUDITED_RESEARCH_CARD=M3-T11-109


Promote the exact rational specialization classification:
M3_T11_109_HOSTILE_AUDIT=PASS
M3_T11_RATIONAL_U_REDUCIBLE_IFF_PHI_IMAGE=true
M3_T11_RATIONAL_U_ONE_PLUS_THREE_PARAMETER_DEGREE4=true
M3_T11_RATIONAL_U_A4_PARAMETER_DEGREE2=true
M3_T11_RATIONAL_U_ONE_PLUS_THREE_AND_A4_DISJOINT=true
M3_T11_RATIONAL_U_GALOIS_TRICHOTOMY_S3_A4_S4=true


For every u in Q^*:
phi image => exactly 1+3 with cubic Galois S3;
psi image => irreducible with Galois A4;
complement => irreducible with Galois S4.


The ambient image counts O(H^(1/2)) and O(H) remain ambient projective-u-height counts only. No physical R<=B power saving is promoted.


M3_T11_EXCEPTIONAL_SPECIALIZATION_PHYSICAL_POWER_SAVING_PROVED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
