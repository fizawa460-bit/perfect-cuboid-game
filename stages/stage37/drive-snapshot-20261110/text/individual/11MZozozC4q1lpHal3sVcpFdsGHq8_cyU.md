# M3-T11-088 — XMinusOneEighthSigmaAntirootProductExactKernelSupportOneTwelfth

CARD_ID: M3-T11-088
CANONICAL_CARD_KEY: M3-T11-088
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-088
現行一覧の状態: PROVED_EXACT / HOSTILE_AUDIT_PASS / DETERMINISTIC_DFR_RECOVERY / ZERO_POWER_SUPPORT_ENRICHMENT / NO_POWER_SAVING
種別: EXACT_STRUCTURE / SAME_MEASURE_SUPPORT_COORDINATE / WITNESS_ELIMINATION / THEOREM_ROUTER
要点: On x=-1/8, the anti-root product denominator and sigma fresh denominator jointly recover D and D_fr exactly, without a fixed-power support cost.
主張の抜粋: Let Omega=v_1*v_2*v_3. From P_ar=4u^2S/(1+u^2) and S=-2u/(1+u^2), Omega=-8u^3/(1+u^2)^2=-8a^3b/N_u^2. Since N_u is odd and gcd(N_u,2ab)=1, Den(Omega)=N_u^2 exactly. Audited M3-T11-087 gives B_sigma,fr=M_rel^2 and audited M3-T11-080 gives D=sf(N_u/M_rel^2). Hence K_088=sqrt(Den(Omega))/B_sigma,fr is an integer, D=sf(K_088), and D_fr=D/gcd(D,Delta_pkt). Fixed sigma has B^o(1) physical multiplicity, so realized (sigma,Omega) support and sigma support have the same polynomial exponent. No density saving is claimed.
対象・測度: Exact fixed-content/coefficient nondegenerate relative-fresh physical x=-1/8 carrier, exact R<=B; preferred on the M3-T11-085 large-D_fr branch.
依存関係: Section 35; Section 53; M3-T11-080 hostile-audit PASS; M3-T11-085 hostile-audit PASS; M3-T11-087 hostile-audit PASS.
再開条件の抜粋: Reopen if Den(Omega)=N_u^2 fails on the primitive x=-1/8 carrier, B_sigma,fr=M_rel^2 fails, D=sf(N_u/M_rel^2) is retracted, or fixed-sigma B^o(1) physical multiplicity fails.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 98.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 852035
SOURCE_END: 855849
SOURCE_SHA256: 28b0879c0b086669161187cbb2d20ae7104afbf8242be34f3b9d144e97abfa86

M3-T11-088
STATUS:
PROVISIONAL EXACT_STRUCTURE / DETERMINISTIC_DFR_RECOVERY / ZERO_POWER_SUPPORT_ENRICHMENT / HOSTILE_AUDIT_REQUIRED / NO_POWER_SAVING.
TYPE:
EXACT_STRUCTURE / SAME_MEASURE_SUPPORT_COORDINATE / WITNESS_ELIMINATION / THEOREM_ROUTER.
ONE_LINE:
On x=-1/8, the reduced denominator of the anti-root product Omega=v_1v_2v_3 is exactly N_u^2; combining it with the audited fresh denominator B_sigma,fr=M_rel^2 makes the residual kernels D and D_fr deterministic functions of the realized pair (sigma,Omega), at zero fixed-power support cost.
EXACT_CLAIM:
Omega=-8*u^3/(1+u^2)^2=-8*a^3*b/N_u^2,
Den(Omega)=N_u^2,
K_088=sqrt(Den(Omega))/B_sigma,fr=N_u/M_rel^2,
D=sf(K_088),
D_fr=D/gcd(D,Delta_pkt),
Delta_pkt=rad(L_vee*c_1*c_2*c_3).
Hence M_rel and D_fr are both recovered from (sigma,Omega)+fixed packet.
SAME_MEASURE_COST:
M3-T11-087 gives fixed sigma+packet => B^o(1) physical endpoints. Therefore
# realized sigma <= # realized (sigma,Omega) <= B^o(1)*# realized sigma.
The pair support has the same polynomial exponent as sigma support.
POPULATION:
Exact fixed-content/coefficient nondegenerate relative-fresh physical x=-1/8 carrier, exact R<=B, with preferred application to the M3-T11-085 large-D_fr branch.
DEPENDENCIES:
Section 35 symmetric anti-root product formula; Section 53 x=-1/8 identity S=-2u/(1+u^2), parity and gcd(N_u,2ab)=1; hostile-audit-passed M3-T11-080; hostile-audit-passed M3-T11-085; hostile-audit-passed M3-T11-087.
REQUIRED_OUTPUT:
Uniformly per fixed content/coefficient packet, prove
# {realized (sigma,Omega) on the exact x=-1/8 physical measure
   with D_fr(sigma,Omega)>B^(1/12-eta)
   and D_fr(sigma,Omega)^2 | A_sigma^2+B_sigma^2}
<< B^(1/12-delta)
for some fixed delta>eta>0.
DOES_NOT_IMPLY:
No support deficit from denominator recovery alone.
No lattice-index or square-divisor density saving.
No total x=-1/8 power saving.
No primary-gate, endpoint, or P(B)/M3(B) theorem.
NO_DOUBLE_CHARGE:
The new denominator quotient is an exact coordinate identity on the same endpoint measure. It only removes witness ambiguity. It must not be multiplied by the M3-T11-086 lattice index, M3-T11-085 large-square-divisor condition, the old determinant M_rel^2, or fixed-sigma B^o(1) multiplicity as an independent probability.
ALIASES:
XMinusOneEighthSigmaAntirootProductExactKernelSupportOneTwelfth;
SigmaOmegaExactResidualKernelCoordinate;
AntirootProductDenominatorQuotient.
DUPLICATE_OF:
NONE. M3-T11-087 recovers M_rel from sigma but does not recover D or D_fr. M3-T11-080 defines D from N_u/M_rel^2 but does not encode N_u in a second rational invariant paired with sigma.
DO_NOT_REPEAT:
Do not treat Omega and sigma as independent random rational variables.
Do not count the deterministic D_fr recovery as a saving.
Do not replace the exact physical pair image by an ambient rational box.
Do not import SR-STR-170 or ordinary divisor-window density without a same-measure adapter.
REOPEN_CONDITION:
Failure of Den(Omega)=N_u^2 on the primitive x=-1/8 carrier; failure of B_sigma,fr=M_rel^2; retraction of D=sf(N_u/M_rel^2); or failure of fixed-sigma B^o(1) physical multiplicity.
DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 98.
FLAGS:
M3_T11_X_MINUS_ONE_EIGHTH_ANTIROOT_PRODUCT_DENOMINATOR_NU2=PROVISIONAL
M3_T11_X_MINUS_ONE_EIGHTH_SIGMA_OMEGA_RECOVERS_D=PROVISIONAL
M3_T11_X_MINUS_ONE_EIGHTH_SIGMA_OMEGA_RECOVERS_DFR=PROVISIONAL
M3_T11_X_MINUS_ONE_EIGHTH_SIGMA_OMEGA_SUPPORT_POWER_EQUIVALENT=PROVISIONAL
M3_T11_X_MINUS_ONE_EIGHTH_ACTIVE_SIGMA_SUPPORT_DEFICIT_PROVED=false
M3_T11_X_MINUS_ONE_EIGHTH_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
NEXT_LEGAL_ACTION=Hostile-audit M3-T11-088; mainbatch may continue only on the exact same-measure pair-support deficit without charging the recovery identity as density.
NEXT_RESEARCH_CARD_ID=M3-T11-089.
