# M3-T11-099 — Interior residual character linearization to S-numerator and equidistribution main-term firewall

CARD_ID: M3-T11-099
CANONICAL_CARD_KEY: M3-T11-099
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-099
現行一覧の状態: PROVED_EXACT / HOSTILE_AUDIT_PASS / EXACT_CHARACTER_LINEARIZATION / CRT_MAIN_TERM_FIREWALL / GENERIC_CHARACTER_EQUIDISTRIBUTION_NO_GO / NO POWER SAVING
種別: EXACT_STRUCTURE / SAME_MEASURE NO-DOUBLE-CHARGE / GLOBAL_DISPERSION_PREFLIGHT / ANTI_LOOP_FIREWALL
要点: After forced conductor removal, every interior residual character becomes a prescribed Legendre sign of the single numerator s of S=s/t. CRT leaves exactly a 2^(-omega(q_int)) fraction of unit classes, so selector-only generic equidistribution cannot yield a uniform fixed-power saving.
主張の抜粋: For p^lambda with 0<c_p<2lambda, write k_p=2lambda-c_p, t=p^k_p tau_p, N_u=p^(2lambda+c_p) nu_p. Since P=v_1v_2v_3=4a^2s/(tN_u), Pi_p=p^(4lambda)P=4a^2s/(tau_p nu_p). With a==rho b and rho^2==-1 mod p, chi_p(-rho Pi_p)=chi_p(rho tau_p nu_p)chi_p(s). Thus chi_p(s)=chi_p(rho tau_p nu_p). Across q_int, exactly phi(q_int)/2^omega(q_int) unit classes survive, leaving an unavoidable selector-only principal density 2^(-omega(q_int)).
対象・測度: Exact same physical Section-48 interior-prime branch inside the fixed-content/coefficient nondegenerate endpoint population with R<=B. No theta/Kummer 097/098 input.
依存関係: Hostile-audit-passed Section 35 symmetric incidence; Section 48 fresh allocation/residual selector; M3-T11-040 conductor allocation.
再開条件の抜粋: Reopen if the exact P identity, Section-48 normalization, or residual character formula fails; or if a future theorem uses extra endpoint-incidence information beyond selector-only equidistribution.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 109.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 906069
SOURCE_END: 911134
SOURCE_SHA256: dfd56561723259fb793d5e6832a1b59464ac3c1e5d978c8f5f2467b5954f1e21

RESEARCH_CARD=M3-T11-099
---
CARD_ID=M3-T11-099
TITLE=Interior residual character linearization to S-numerator and equidistribution main-term firewall
STATUS=PROVISIONAL EXACT_CHARACTER_LINEARIZATION / CRT_MAIN_TERM_FIREWALL / GENERIC_CHARACTER_EQUIDISTRIBUTION_NO_GO / HOSTILE_AUDIT_REQUIRED / NO_POWER_SAVING
TYPE=EXACT_STRUCTURE / SAME_MEASURE_NO_DOUBLE_CHARGE / GLOBAL_DISPERSION_PREFLIGHT / ANTI_LOOP_FIREWALL
CLAIM:
Retain the hostile-audit-passed Section-35 identity
P=v_1*v_2*v_3=4*u^2*S/(1+u^2)
and the Section-48 interior-prime normalization. Write u=a/b, S=s/t, N_u=a^2+b^2. For p^lambda||m_i with 0<c_p<2lambda, set
k_p=2lambda-c_p,
t=p^k_p*tau_p,
N_u=p^(2lambda+c_p)*nu_p,
with tau_p and nu_p p-adic units.
Then exactly
P=4*a^2*s/(t*N_u)
and
Pi_p:=p^(4lambda)*P=4*a^2*s/(tau_p*nu_p).


For the oriented Gaussian root a==rho*b mod p, rho^2==-1 mod p,
a^2==-b^2 mod p,
so
-rho*Pi_p==4*rho*b^2*s/(tau_p*nu_p) mod p.
Therefore
chi_p(-rho*Pi_p)=chi_p(rho*tau_p*nu_p)*chi_p(s).
The physical Section-48 selector chi_p(-rho*Pi_p)=+1 is exactly
chi_p(s)=chi_p(rho*tau_p*nu_p).


Let q_int be the squarefree radical of the interior fresh support. For fixed auxiliary data and epsilon_p=chi_p(rho*tau_p*nu_p), CRT gives exactly
phi(q_int)/2^omega(q_int)
unit classes s mod q_int satisfying all selectors. Equivalently, for gcd(s,q_int)=1,
1_select(s)=2^(-omega(q_int))*product_{p|q_int}(1+epsilon_p*chi_p(s)).
Thus selector-only equidistribution has an unavoidable principal term of relative density 2^(-omega(q_int)); uniformly this is only q_int^(-o(1)) in the worst case and equals 1/2 for prime q_int. Cancellation of nonprincipal character sums alone cannot yield a uniform q_int^(-delta) saving.


POPULATION:
Exact same physical Section-48 interior-prime branch inside the fixed-content/coefficient nondegenerate endpoint population with exact R<=B.


HEIGHT:
No change. Exact physical R<=B measure.


DEPENDS_ON:
Hostile-audit-passed Section 35 symmetric incidence; hostile-audit-passed Section 48 interior normalization and residual character; M3-T11-040 conductor allocation. Independent of provisional M3-T11-097/098.


IMPLIES:
The interior residual character is a prescribed Legendre sign of the single S-numerator s after forced conductor removal. Generic selector-only equidistribution/Burgess/large-sieve treatment cannot itself give a fixed-power support deficit. Any surviving interior-character route must add endpoint-incidence, moving-theta, or other structural correlation.


ALIASES:
InteriorCharacterSingleSNumerator;
InteriorCharacterCRTMainTermFirewall;
InteriorCharacterSelectorOnlyDispersionNoGo.


DUPLICATE_OF:
none. This sharpens the old Section-48 statement that local tensorization is only M_int^(-o(1)) by identifying the exact global variable carrying every residual sign and the exact CRT main term.


SUPERSEDES:
The unrestricted interpretation of InteriorCharacterGlobalDispersion as a generic equidistribution problem for isolated residual signs. It does not supersede structural endpoint-incidence correlation or theta moving-support attacks.


DO_NOT_REPEAT:
Do not pursue isolated-selector Burgess, large-sieve, or generic equidistribution estimates as though their nonprincipal cancellation could remove the exact 2^(-omega(q_int)) principal density. New character work must couple to additional endpoint-incidence information.


REOPEN_CONDITION:
Hostile audit rejects P=4*u^2*S/(1+u^2), the Section-48 normalization, or the character simplification; an audited dependency changes; or a future theorem exploits extra endpoint-incidence information beyond selector-only equidistribution.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 109.


CREDIT:
No fixed-power moving-support deficit. No denominator-extreme closure. No primary-gate closure. No endpoint theorem. No P(B)/M3(B) limit. No Perfect Cuboid nonexistence credit.


FLAGS:
M3_T11_INTERIOR_CHARACTER_SINGLE_S_NUMERATOR=PROVISIONAL
M3_T11_INTERIOR_CHARACTER_CRT_EXACT_ACCEPTANCE=PROVISIONAL
M3_T11_INTERIOR_CHARACTER_EQUIDISTRIBUTION_ONLY_FIXED_POWER=false
M3_T11_INTERIOR_CHARACTER_GENERIC_DISPERSION_ATTACK_RETIRED=PROVISIONAL
M3_T11_INTERIOR_CHARACTER_ENDPOINT_CORRELATION_OPEN=true
M3_T11_DENOMINATOR_EXTREME_SUPPORT_DEFICIT_PROVED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
LATEST_RESEARCH_CARD=M3-T11-099
LATEST_AUDITED_RESEARCH_CARD=M3-T11-096
PROVISIONAL_FRONTIER_CARD=M3-T11-099
PROVISIONAL_FRONTIER_AUDIT_STATUS=HOSTILE_AUDIT_REQUIRED
CURRENT_ATTACK=GenericFullSThetaNonzeroFourthPowerSupportOneTwelfth|InteriorCharacterGlobalDispersionBeyondSelectorEquidistribution
NEXT_ATTACK=ThetaFourthPowerMovingSupportBeyondKummer|InteriorCharacterEndpointIncidenceCorrelation
NEXT_LEGAL_ACTION=Hostile-audit M3-T11-097 and M3-T11-098 as one dependency chain and hostile-audit M3-T11-099 independently. Mainbatch may continue only with genuinely non-Kummer/global moving-theta support or an interior-character theorem using structural correlation beyond selector-only equidistribution.
NEXT_RESEARCH_CARD_ID=M3-T11-100
