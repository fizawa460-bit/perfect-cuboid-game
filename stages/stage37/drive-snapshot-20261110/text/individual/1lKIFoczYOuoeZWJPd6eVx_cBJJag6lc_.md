# M3-T11-095 — The fixed-theta elliptic point has an exact 2-torsion tangent coordinate tau_theta=Z-3(v+1) with exact fresh M_rel^4 saturation. Its normalized slope is exactly old w=u/S, so it is not an independent carrier; fixing tau_theta gives a smooth genus-3 hyperelliptic fiber on the hard full-S branch.

CARD_ID: M3-T11-095
CANONICAL_CARD_KEY: M3-T11-095
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-095
現行一覧の状態: PROVED_EXACT / HOSTILE_AUDIT_PASS / EXACT_FRESH_SATURATION / OLD_W_IDENTIFICATION / GENUS3_PREFLIGHT / NO_POWER_SAVING
種別: EXACT_STRUCTURE / SAME_MEASURE_COMPATIBILITY / NO_DOUBLE_CHARGE / FIBER_COMPLEXITY_PREFLIGHT
要点: The fixed-theta elliptic point has an exact 2-torsion tangent coordinate tau_theta=Z-3(v+1) with exact fresh M_rel^4 saturation. Its normalized slope is exactly old w=u/S, so it is not an independent carrier; fixing tau_theta gives a smooth genus-3 hyperelliptic fiber on the hard full-S branch.
主張の抜粋: Z=3(v+1)-(v+1)^2/(8x); w=(v+1)/(16x)=u/S; tau_theta=-2w(v+1)=-(v+1)^2/(8x), so v_p(tau_theta)=4*lambda exactly for p^lambda||M_rel. Fixed tau yields Y_tau^2=-(1+v)F_tau(v) with discriminant tau^23*(125tau+27)^3*(729tau^2+351tau+128); the rational singular values tau=0,-27/125 are absent on the hard full-S branch.
対象・測度: Exact fixed-content/coefficient nondegenerate generic full-S-denominator physical branch with R<=B and theta!=0. Same physical measure; no power-saving credit.
依存関係: M3-T11-090/091/092/093/094; Section 52 x=((1+u^2)S)/(16u); full-S v_p(v+1)=v_p(t)=2*lambda and x fresh-unit; M3-T11-093 E_theta/Z.
再開条件の抜粋: Reopen if the Z tangent identity, w identification, exact full-S valuations, fixed-tau substitution, or discriminant factorization fails, or hostile audit rejects the M3-T11-090 through 094 dependency chain.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 105.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 880803
SOURCE_END: 888199
SOURCE_SHA256: 04c4976f99df81e52deb09f9e9f0da9ed3567cb4a01183342b111f785a5d6598

M3-T11-095
STATUS=PROVISIONAL_EXACT_TORSION_TANGENT_IDENTITY / EXACT_FRESH_SATURATION / OLD_W_IDENTIFICATION / GENUS3_PREFLIGHT / HOSTILE_AUDIT_REQUIRED / NO_POWER_SAVING
RESULT:
1. Exact fixed-theta 2-torsion tangent identity.
   Retain
   E_theta: Z^2=(v+1)*(8+(7+4*theta)*v-v^2),
   A_theta(v)=64*(v+1)^2-256*theta*v,
   B(v)=-48*(v+1)^2,
   Z=(2*A_theta(v)*x+B(v))/(16*(v+1)).
   Put D_theta=(v+1)^2-4*theta*v. The defining quadratic in x is
   64*D_theta*x^2-48*(v+1)^2*x+(v+1)^3=0.
   Substitution into Z gives exactly
   Z=3*(v+1)-(v+1)^2/(8*x).
2. Identification with the old scaled coordinate.
   Since x=((1+u^2)S)/(16u) and v=u^2,
   w=(v+1)/(16*x)=u/S.
   Hence
   Z/(v+1)=3-2*w,
   tau_theta:=Z-3*(v+1)
   =-2*w*(v+1)
   =-(v+1)^2/(8*x).
3. Exact full-S fourth-power saturation.
   For every p^lambda||M_rel on the hard full-S branch,
   v_p(v+1)=2*lambda,
   v_p(w)=2*lambda,
   v_p(x)=0.
   Therefore
   v_p(tau_theta)=4*lambda
   exactly.
   Thus M_rel^4 divides the reduced numerator of tau_theta with exact fresh valuation and gcd(Den(tau_theta),M_rel)=1.
   Unlike theta itself, tau_theta has no x=3/4 fresh overvaluation.
4. No-double-charge consequence.
   The normalized torsion slope defect is
   Z/(v+1)-3=-2*w.
   Therefore the apparent new 2-torsion root-line on E_theta is exactly the pre-existing scaled-symmetric w=u/S conductor presentation. It is structural, not a second arithmetic probability, and may not be multiplied with theta, the common-u Gaussian root line, old determinant indices, or residual-character carriers.
5. Fixed-tau fiber preflight.
   Let tau=tau_theta and v=u^2. From tau=-2*u*(1+u^2)/S,
   S=-2*u*(1+v)/tau.
   With Y_tau=tau^2*Y/(4*u), the canonical endpoint equation becomes
   Y_tau^2=-(1+v)*F_tau(v),
   where
   F_tau(v)=v*(1+v)^5
            +8*tau*v*(1+v)^3
            +tau^2*(1+v)*(11*v^2+10*v-1)
            -6*tau^3*(1+v)
            -tau^4.
   The degree-7 polynomial discriminant is exactly
   tau^23*(125*tau+27)^3*(729*tau^2+351*tau+128).
   The last quadratic has discriminant -3^6*7^3 and no rational root. The only rational singular tau are 0 and -27/125.
   Tau=0 is impossible on the nondegenerate full-S branch. Tau=-27/125 is incompatible with the hard branch M_rel>1 because tau has exact fresh M_rel^4 numerator and fresh-unit denominator. Therefore every realized hard-branch fixed-tau fiber is a smooth genus-3 hyperelliptic curve.
CONSEQUENCE:
M3_T11_THETA_2TORSION_TANGENT_IDENTITY=PROVISIONAL.
M3_T11_THETA_TANGENT_MREL4_EXACT_SATURATION=PROVISIONAL.
M3_T11_THETA_TANGENT_EQUALS_SCALED_W=PROVISIONAL.
M3_T11_THETA_TANGENT_INDEPENDENT_SAVING=false.
M3_T11_FIXED_TAU_GENERIC_GENUS3=PROVISIONAL.
M3_T11_FIXED_TAU_BO1_PROVED=false.
The exactly saturated tau coordinate is not currently a better support receiver than theta because it loses the elliptic fixed-fiber B^o(1) mechanism.
NO_CREDIT:
No moving-support fixed-power deficit; no denominator-extreme closure; no primary-gate closure; no endpoint theorem; P_OVER_M3_LIMIT_PROVED=false; no Perfect Cuboid nonexistence credit.
DEPENDENCY:
M3-T11-090/091/092/093/094 remain provisional as applicable. This card must be hostile-audited with that chain.
DETAIL:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 105.
NEXT:
GenericFullSThetaNonzeroFourthPowerSupportOneTwelfth | FullSDefectResidualCharacterDispersionOneTwelfth | InteriorCharacterGlobalDispersion.
NEXT_RESEARCH_CARD_ID=M3-T11-096.
LATEST_RESEARCH_CARD=M3-T11-095
LATEST_AUDITED_RESEARCH_CARD=M3-T11-089
PROVISIONAL_FRONTIER_CARD=M3-T11-095
NEXT_LEGAL_ACTION=Hostile-audit M3-T11-090 through M3-T11-095. Mainbatch continuation: theta!=0 global support or retained residual/global dispersion. Do not recharge the tangent/w identity as an independent saving.
## AUDIT PROMOTION ADDENDUM — M3-T11-090 through M3-T11-095
HOSTILE_AUDIT=PASS
AUDIT_DOC_ID=11ZQfatG59mNZLiXydBpvyRMhbZTJq24CWkaVZymcLmQ
PRIOR_AUDITED_FRONTIER=M3-T11-089
LATEST_AUDITED_RESEARCH_CARD=M3-T11-095


M3-T11-090:
STATUS=PROVED / HOSTILE_AUDIT_PASS / FIXED_X_BO1 / SAME_MEASURE_SUPPORT_COMPRESSION / NO_POWER_SAVING.
PROMOTED=M3_T11_FIXED_X_GENERIC_BO1_PROVED=true; M3_T11_GENERIC_X_SAME_MEASURE_SUPPORT_COORDINATE=true; M3_T11_GENERIC_X_ENDPOINT_POWER_EQUIVALENT=true; M3_T11_GENERIC_X_COMMON_U_POWER_EQUIVALENT=true.


M3-T11-091:
STATUS=PROVED_EXACT / HOSTILE_AUDIT_PASS / EXACT_FRESH_VALUATION_SATURATION / FIXED_DEFECT_BO1 / NO_POWER_SAVING.
PROMOTED=M3_T11_GENERIC_FULL_S_LEGENDRE_DEFECT_COORDINATE=true; M3_T11_GENERIC_FULL_S_LEGENDRE_DEFECT_FRESH_VALUATION_EXACT=true; M3_T11_GENERIC_FULL_S_LEGENDRE_DEFECT_NUMERATOR_MREL2=true; M3_T11_GENERIC_FULL_S_LEGENDRE_DEFECT_NO_EXTRA_FRESH_VALUATION=true; M3_T11_FIXED_LEGENDRE_DEFECT_ELLIPTIC_2TORSION=true; M3_T11_FIXED_LEGENDRE_DEFECT_BO1_PROVED=true; M3_T11_GENERIC_LEGENDRE_DEFECT_SUPPORT_COORDINATE=true.


M3-T11-092:
STATUS=PROVED_EXACT / HOSTILE_AUDIT_PASS / FULL_MODULUS_NORMALIZED_COLLISION / FRESH_CHARACTER_LOCK / NO_POWER_SAVING.
PROMOTED=M3_T11_FULL_S_HOMOGENEOUS_LEGENDRE_DEFECT_FORM=true; M3_T11_FULL_S_PHI_DEFECT_EXACT_DIVISION=true; M3_T11_FULL_S_DEFECT_PHI_FRESH_TRANSVERSALITY=true; M3_T11_FULL_S_NORMALIZED_COLLISION_MOD_MREL2=true; M3_T11_FULL_S_RESIDUAL_CHARACTER_LOCK=true.
RETAINED=M3_T11_FULL_S_RESIDUAL_CHARACTER_FIXED_POWER=false.


M3-T11-093:
STATUS=PROVED_EXACT / HOSTILE_AUDIT_PASS / MREL4_NUMERATOR_CARRIER / FIXED_THETA_BO1 / THETA0_ROUTER_SUPERSEDED_BY_094 / NO_POWER_SAVING.
PROMOTED=M3_T11_FULL_S_THETA_COORDINATE=true; M3_T11_FULL_S_THETA_MREL4_NUMERATOR=true; M3_T11_FULL_S_THETA_OVERVALUATION_X_THREE_QUARTERS=true; M3_T11_FULL_S_THETA_P5MOD12_EXACT_SATURATION=true; M3_T11_FIXED_THETA_ELLIPTIC_2TORSION=true; M3_T11_FIXED_THETA_BO1_PROVED=true.


M3-T11-094:
STATUS=PROVED_EXACT / HOSTILE_AUDIT_PASS / THETA0_PHYSICAL_EMPTY / FRESH_COLLISION_SEPARATION / THETA_NONZERO_SUPPORT_OPEN.
PROMOTED=M3_T11_FULL_S_THETA_HOMOGENEOUS_COFACTOR=true; M3_T11_FULL_S_THETA_PHI0_FRESH_SUPPORT_DISJOINT=true; M3_T11_THETA_ZERO_7ADIC_OBSTRUCTION=true; M3_T11_THETA_ZERO_PHYSICAL_EMPTY=true.
CONSEQUENCE=ThetaZeroConicGaussianNormSquareDivisorOneTwelfth is retired. Do not reopen absent an audited dependency change.


M3-T11-095:
STATUS=PROVED_EXACT / HOSTILE_AUDIT_PASS / EXACT_FRESH_SATURATION / OLD_W_IDENTIFICATION / GENUS3_PREFLIGHT / NO_POWER_SAVING.
PROMOTED=M3_T11_THETA_2TORSION_TANGENT_IDENTITY=true; M3_T11_THETA_TANGENT_MREL4_EXACT_SATURATION=true; M3_T11_THETA_TANGENT_EQUALS_SCALED_W=true; M3_T11_FIXED_TAU_GENERIC_GENUS3=true.
RETAINED=M3_T11_THETA_TANGENT_INDEPENDENT_SAVING=false; M3_T11_FIXED_TAU_BO1_PROVED=false.


GLOBAL_FIREWALL:
M3_T11_DENOMINATOR_EXTREME_SUPPORT_DEFICIT_PROVED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
No endpoint theorem and no Perfect Cuboid nonexistence credit.
Do not multiply deterministic M_rel^2/M_rel^4 carriers, theta/ell/tau_theta/w, residual-character locks, root-line factors, fixed-fiber B^o(1), or determinant factors as independent savings.


CURRENT_ATTACK=GenericFullSThetaNonzeroFourthPowerSupportOneTwelfth|FullSDefectResidualCharacterDispersionOneTwelfth|InteriorCharacterGlobalDispersion
LATEST_RESEARCH_CARD=M3-T11-095
LATEST_AUDITED_RESEARCH_CARD=M3-T11-095
PROVISIONAL_FRONTIER_CARD=NONE
PROVISIONAL_FRONTIER_AUDIT_STATUS=NOT_APPLICABLE
NEXT_RESEARCH_CARD_ID=M3-T11-096
NEXT_LEGAL_ACTION=Continue on the surviving theta!=0 same-physical-measure global support problem.
