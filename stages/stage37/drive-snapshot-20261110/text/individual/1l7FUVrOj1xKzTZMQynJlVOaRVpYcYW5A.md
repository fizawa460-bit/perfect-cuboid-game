# M3-T11-101 — Interior selector globalizes to the symmetric-product quadratic squareclass; fixed-Pi fiber is smooth genus 5

CARD_ID: M3-T11-101
CANONICAL_CARD_KEY: M3-T11-101
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-101
現行一覧の状態: PROVED_EXACT / HOSTILE_AUDIT_PASS / EXACT_GLOBAL_SQUARECLASS / INTERIOR_SPLITTING_RECEIVER / FIXED_PI_GENUS5 / RECIPROCITY_ONLY_NO_GO / NO POWER SAVING
種別: EXACT_STRUCTURE / SAME_MEASURE_GLOBALIZATION / CROSS_PRIME_RECEIVER / FIBER_COMPLEXITY_PREFLIGHT / ANTI_LOOP_FIREWALL
要点: The interior selector globalizes to the single moving symmetric-product squareclass [2*Pi]; every interior conductor prime splits in its quadratic algebra. Fixed nonzero rational Pi gives a smooth genus-5 hyperelliptic fiber.
主張の抜粋: With M=M_rel and J=t*N_u/M^4, audited conductor allocation gives J in Z. At every interior p, chi_p(J)=chi_p(tau_p nu_p) and chi_p(rho)=(2/p), so M3-T11-099 becomes chi_p(2sJ)=+1. Since Pi=4a^2s/(tN_u), (sJ)Pi=(2as/M^2)^2 and [2sJ]=[2Pi]. For fixed Pi=pi!=0, substitution S=pi(1+u^2)/(4u^2) gives a degree-12 hyperelliptic model with discriminant 2^156*pi^32*(729*pi^2-512)^3*(256*pi^4+96417*pi^2-746496), nonzero for rational pi!=0; hence genus 5. No fixed-power saving follows.
対象・測度: Exact fixed-content/coefficient nondegenerate Stage37 physical endpoint population with R<=B; same measure; Pi!=0 on the nondegenerate carrier.
依存関係: Hostile-audit-passed M3-T11-099/100; Sections 35, 48, 49; M3-T11-040 conductor allocation.
再開条件の抜粋: Reopen if audit rejects M^4|t*N_u, [2*s*t*N_u/M^4]=[2*Pi], chi_p(rho)=(2/p), the fixed-Pi genus-5 calculation, or an audited dependency changes.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 112.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 918070
SOURCE_END: 924896
SOURCE_SHA256: c527ec1c852fade1df78171c187a8d7f5d24031beb5415a1b726db5fc6241783

CARD_ID=M3-T11-101
TITLE=Interior selector globalizes to the symmetric-product quadratic squareclass; fixed-Pi fiber is smooth genus 5
STATUS=PROVISIONAL EXACT_GLOBAL_SQUARECLASS / INTERIOR_SPLITTING_RECEIVER / FIXED_PI_GENUS5 / RECIPROCITY_ONLY_NO_GO / HOSTILE_AUDIT_REQUIRED / NO POWER SAVING
TYPE=EXACT_STRUCTURE / SAME_MEASURE_GLOBALIZATION / CROSS_PRIME_RECEIVER / FIBER_COMPLEXITY_PREFLIGHT / ANTI_LOOP_FIREWALL


CLAIM:
On the exact fixed-content/coefficient nondegenerate physical endpoint population, write M=M_rel, S=s/t, u=a/b, N_u=a^2+b^2. The audited M3-T11-040 valuation allocation implies M^4|t*N_u. Define
J=t*N_u/M^4 in Z.
For every interior p^lambda||M, one has
chi_p(J)=chi_p(tau_p*nu_p).
With the oriented Gaussian root rho=a/b mod p, rho^2=-1 and p==1 mod4 imply
chi_p(rho)=(2/p).
Hence the audited M3-T11-099 selector
chi_p(s)=chi_p(rho*tau_p*nu_p)
is exactly
chi_p(2*s*J)=+1.


The symmetric product
Pi=v_1*v_2*v_3=4*a^2*s/(t*N_u)
satisfies exactly
(s*J)*Pi=(2*a*s/M^2)^2.
Therefore
[2*s*J]=[2*Pi] in Q*/Q*^2.
Equivalently, every interior conductor prime has trivial local quadratic character in the single moving squareclass [2*Pi]; for nontrivial [2*Pi], every interior conductor prime splits in K_Pi=Q(sqrt(2*Pi)).
Section 49 gives v_p(Den(Pi))=4*lambda at every fresh p, so this forced conductor denominator is a fourth power and is invisible to the quadratic squareclass. It gives no ramification/discriminant lower bound for K_Pi.


FIXED_PI_GEOMETRY:
For a fixed rational Pi=pi!=0, use
S=pi*(1+u^2)/(4*u^2)
in the audited Section-35 discriminant equation and set Z=16*u^4*Y. Then
Z^2=-(1+u^2)*G_pi(u),
where
G_pi(u)=
pi^4*(1+u^2)^5
-64*pi^3*u^3*(1+u^2)^3
+64*pi^2*u^4*(1+u^2)^2*(11*u^2-1)
+3072*pi*u^7*(1+u^2)
-4096*u^10.
The degree-12 leading coefficient is 4096-704*pi^2-pi^4 and is nonzero for rational pi. The exact discriminant is
2^156*pi^32*(729*pi^2-512)^3*(256*pi^4+96417*pi^2-746496).
For rational pi!=0 all factors are nonzero; the last quadratic in pi^2 has roots
(-96417+/-24327*sqrt(17))/512.
Thus every nonzero rational fixed-Pi fiber is a smooth genus-5 hyperelliptic curve.


POPULATION:
Exact same fixed-content/coefficient nondegenerate Stage37 physical endpoint population with R<=B. The nondegenerate carrier has Pi!=0. No change of measure.


DEPENDS_ON:
Hostile-audit-passed M3-T11-099 and M3-T11-100; audited Sections 35, 48, 49; M3-T11-040 conductor allocation.


IMPLIES:
The surviving interior cross-prime route has one canonical global receiver: the moving symmetric-product quadratic squareclass [2*Pi] together with the condition that every interior conductor prime split in it. The p-dependent auxiliary signs tau_p,nu_p,rho are not independent global data. Fixed-Pi fibers are explicitly genus 5, so any support theorem using this receiver must be genuinely uniform/global.


RECIPROCITY_FIREWALL:
Quadratic reciprocity, Jacobi products, selector-only character sums, or the mere statement that all interior primes split in K_Pi do not by themselves give a uniform fixed-power deficit. The exact selector principal density remains 2^(-omega(q_int)), including 1/2 when q_int is prime. The fresh M_rel^4 denominator of Pi cannot be recycled as a large quadratic-field discriminant because it is a squareclass-trivial fourth power.


DO_NOT_REPEAT:
Do not treat tau_p,nu_p,rho as separate cross-prime invariants after the [2*Pi] globalization. Do not reopen reciprocity-only, selector-only, or deeper-local-Hensel routes as fixed-power attacks. Do not use qualitative fixed-genus-5 finiteness as a uniform B^o(1) endpoint bound.


REOPEN_CONDITION:
Hostile audit rejects M^4|t*N_u, the squareclass identity [2*s*t*N_u/M^4]=[2*Pi], chi_p(rho)=(2/p), the fixed-Pi genus-5 calculation, or an audited dependency changes.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 112.


CREDIT:
No fixed-power support saving. No denominator-extreme closure. No primary-gate closure. No endpoint theorem. No P(B)/M3(B) limit. No Perfect Cuboid nonexistence credit.


FLAGS:
M3_T11_INTERIOR_GLOBAL_J_INTEGER=PROVISIONAL
M3_T11_INTERIOR_SELECTOR_GLOBAL_2PI_SQUARECLASS=PROVISIONAL
M3_T11_INTERIOR_PRIMES_SPLIT_IN_K_2PI=PROVISIONAL
M3_T11_INTERIOR_AUXILIARY_LOCAL_SIGNS_ELIMINATED=PROVISIONAL
M3_T11_INTERIOR_QUADRATIC_RECIPROCITY_ONLY_FIXED_POWER=false
M3_T11_FIXED_PI_GENERIC_GENUS5=PROVISIONAL
M3_T11_FIXED_PI_BO1_PROVED=false
M3_T11_DENOMINATOR_EXTREME_SUPPORT_DEFICIT_PROVED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false


LATEST_RESEARCH_CARD=M3-T11-101
LATEST_AUDITED_RESEARCH_CARD=M3-T11-100
PROVISIONAL_FRONTIER_CARD=M3-T11-101
PROVISIONAL_FRONTIER_AUDIT_STATUS=HOSTILE_AUDIT_REQUIRED
CURRENT_ATTACK=GenericFullSThetaNonzeroFourthPowerSupportOneTwelfth|InteriorSymmetricProductSplittingIncidence
NEXT_ATTACK=ThetaFourthPowerMovingSupportBeyondKummer|InteriorGlobal2PiSplittingEndpointGeometry
NEXT_LEGAL_ACTION=Hostile-audit M3-T11-101. Mainbatch may continue on a theorem coupling realized Pi support/geometry with the requirement that every interior conductor prime split in K_Pi, or on the independent theta moving-support route. Do not spend another loop on p-dependent auxiliary-sign bookkeeping, Jacobi/reciprocity alone, selector-only character sums, or deeper local Hensel refinement.
NEXT_RESEARCH_CARD_ID=M3-T11-102


## AUDIT PROMOTION — M3-T11-101
AUDIT_DOC_ID=1OVWtL8f3E065ErxzMulISFEVF--_gFn9ySsM220P9hc
HOSTILE_AUDIT=PASS
AUDITED_CARD=M3-T11-101
LATEST_AUDITED_RESEARCH_CARD=M3-T11-101


M3-T11-101 STATUS=PROVED_EXACT / HOSTILE_AUDIT_PASS / EXACT_GLOBAL_SQUARECLASS / INTERIOR_SPLITTING_RECEIVER / FIXED_PI_GENUS5 / RECIPROCITY_ONLY_NO_GO / NO POWER SAVING


CANONICAL_AUDIT_CONSEQUENCES:
- M_rel^4|t*N_u and J=t*N_u/M_rel^4 is integral.
- Every interior fresh prime satisfies chi_p(2*s*J)=+1.
- [2*s*J]=[2*Pi] in Q*/Q*^2, so the interior system is one global moving squareclass.
- For nontrivial [2*Pi], every interior conductor prime splits in K_Pi=Q(sqrt(2*Pi)).
- The exact M_rel^4 denominator of Pi is squareclass-trivial and gives no quadratic-field discriminant credit.
- Every rational nonzero fixed-Pi fiber is a smooth degree-12 genus-5 hyperelliptic curve.
- Fixed-Pi uniform B^o(1) remains unproved.


M3_T11_INTERIOR_GLOBAL_J_INTEGER=true
M3_T11_INTERIOR_SELECTOR_GLOBAL_2PI_SQUARECLASS=true
M3_T11_INTERIOR_PRIMES_SPLIT_IN_K_2PI=true
M3_T11_INTERIOR_AUXILIARY_LOCAL_SIGNS_ELIMINATED=true
M3_T11_INTERIOR_QUADRATIC_RECIPROCITY_ONLY_FIXED_POWER=false
M3_T11_FIXED_PI_GENERIC_GENUS5=true
M3_T11_FIXED_PI_BO1_PROVED=false
M3_T11_DENOMINATOR_EXTREME_SUPPORT_DEFICIT_PROVED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
SURVIVING_FRONTIER=ThetaFourthPowerMovingSupportBeyondKummer|InteriorGlobal2PiSplittingEndpointGeometry
NEXT_RESEARCH_CARD_ID=M3-T11-102
