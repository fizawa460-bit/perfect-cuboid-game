# M3-T11-043 — Amplified-u extreme residual elimination and denominator-extreme normalization

CARD_ID: M3-T11-043
CANONICAL_CARD_KEY: M3-T11-043
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-043
現行一覧の状態: PROVED_EXACT
種別: EXACT_STRUCTURE / EXTREME_BRANCH_ELIMINATION / FIREWALL
要点: On the canonical symmetric packet write S=s/t and u=a/b reduced, N_u=a^2+b^2, and for p^lambda||m_i set c_p=v_p(C_u), k_p=2*lambda-c_p. The retained exact middle-coefficient identi
主張の抜粋: On the canonical symmetric packet write S=s/t and u=a/b reduced, N_u=a^2+b^2, and for p^lambda||m_i set c_p=v_p(C_u), k_p=2*lambda-c_p. The retained exact middle-coefficient identity E=4*a*(b*s-a*t)/(t*N_u) has v_p(Den(E))=4*lambda on every relative-fresh p. The current exact saturation gives v_p(N_u)=2*lambda+c_p and 
対象・測度: Exact fixed-content/coefficient nondegenerate relative-fresh endpoint packet on the canonical symmetric (S,u) pushforward.
依存関係: M3-T11-041; retained Section-49 exact flag M3_T11_E_FULL_MREL4_DENOMINATOR=true; current exact common-u saturation M3_T11_FRESH_COMMON_U_NORM_VALUATION_EXACT=true.
再開条件の抜粋: Retract the exact E fourth-power denominator or the exact common-u fresh saturation; otherwise only a genuinely new non-valuation same-measure mechanism may revisit this branch.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 50.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 651927
SOURCE_END: 655251
SOURCE_SHA256: 5845aa782f05eadf887029d7edccf5cdf07ea8576044d8a174d59a5676ec7690

## M3-T11-043
TITLE: Amplified-u extreme residual elimination and denominator-extreme normalization
TYPE: EXACT_STRUCTURE / EXTREME_BRANCH_ELIMINATION / FIREWALL
STATUS: PROVED_EXACT
CLAIM:
On the canonical symmetric packet write S=s/t and u=a/b reduced, N_u=a^2+b^2, and for p^lambda||m_i set c_p=v_p(C_u), k_p=2*lambda-c_p.
The retained exact middle-coefficient identity
E=4*a*(b*s-a*t)/(t*N_u)
has v_p(Den(E))=4*lambda on every relative-fresh p.
The current exact saturation gives
v_p(N_u)=2*lambda+c_p
and
v_p(t)=k_p.


If c_p=2*lambda, then p does not divide t and v_p(N_u)=4*lambda.
Exact preservation of the p^(4*lambda) denominator of E forces
p not dividing (b*s-a*t).
If p divided Phi_*, then k_p=0 gives p|Phi; with rho=a*b^(-1) mod p and rho^2=-1, the exact triple-root identity
a*s^3+3*b*s^2*t-3*a*s*t^2-b*t^3
==
b*rho*(s-rho*t)^3 mod p
would force s==rho*t mod p, hence p|(b*s-a*t), contradiction.
Therefore
c_p=2*lambda => v_p(Phi_*)=0.


Together with M3-T11-041 for 0<c_p<2*lambda,
boxed:
c_p>0 => v_p(Phi_*)=0,
so
boxed:
gcd(Phi_*,C_u)=1.
All residual fresh Phi_* support is therefore confined to the full-S-denominator extreme c_p=0.


For c_p=0, n=2*lambda, write N_u=p^n*n_0 and t=p^n*t_0.
Modulo p after removing the forced p^n factor,
boxed:
p^(-n)*Phi == s^3*(n_0*s-16*a*b*t_0).
Hence residual p-divisibility requires
boxed:
n_0*s == 16*a*b*t_0 mod p,
and the normalized square forces the residual exponent to be even.


POPULATION:
Exact fixed-content/coefficient nondegenerate relative-fresh endpoint packet on the canonical symmetric (S,u) pushforward.
HEIGHT:
Exact physical R<=B retained.
DEPENDS_ON:
M3-T11-041;
retained Section-49 exact flag M3_T11_E_FULL_MREL4_DENOMINATOR=true;
current exact common-u saturation M3_T11_FRESH_COMMON_U_NORM_VALUATION_EXACT=true.
IMPLIES:
The amplified-u extreme is not a live residual valuation tail.
ExtremePhiResidualTail reduces to FullSDenominatorExtremeResidualTail.
Residual fresh Phi_* primes are disjoint from C_u support.
DOES_NOT_IMPLY:
No fixed-power estimate for c_p=0.
No independence or dispersion theorem for residual unit characters.
No P(B)/M3(B) limit theorem.
NO_DOUBLE_CHARGE:
The E denominator is used only to contradict same-orientation cancellation on c_p=2*lambda; it contributes no separate density saving.
ALIASES:
AmplifiedUExtremePhiResidualEmpty;
PhiStarCuCoprime;
FullSDenominatorExtremeResidualOnly.
DUPLICATE_OF:
NONE.
SUPERSEDES:
The part of the prior extreme-residual frontier that left c_p=2*lambda open.
DO_NOT_REPEAT:
Do not search for higher or residual fresh Phi_* valuation on c_p=2*lambda.
REOPEN_CONDITION:
Retract the exact E fourth-power denominator or the exact common-u fresh saturation; otherwise only a genuinely new non-valuation same-measure mechanism may revisit this branch.
DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 50.
ID_HYGIENE:
The existing research history already contains two entries labelled M3-T11-042. This card names its exact dependencies by formula/flag and does not renumber prior material.
FLAGS:
M3_T11_AMPLIFIED_U_EXTREME_PHI_RESIDUAL_EMPTY=true
M3_T11_PHI_STAR_COPRIME_TO_CU=true
M3_T11_RESIDUAL_FRESH_PHI_SUPPORT_ONLY_CP_ZERO=true
M3_T11_DENOMINATOR_EXTREME_NORMALIZED_COLLISION=true
M3_T11_DENOMINATOR_EXTREME_RESIDUAL_TAIL_PROVED=false
P_OVER_M3_LIMIT_PROVED=false


---
