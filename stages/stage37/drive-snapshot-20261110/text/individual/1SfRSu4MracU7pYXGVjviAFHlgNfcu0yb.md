# M3-T11-093 — Fourth-power recombined defect coordinate and theta=0 Gaussian conic carrier

CARD_ID: M3-T11-093
CANONICAL_CARD_KEY: M3-T11-093
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-093
現行一覧の状態: PROVED_EXACT / HOSTILE_AUDIT_PASS / MREL4_NUMERATOR_CARRIER / FIXED_THETA_BO1 / THETA0_ROUTER_SUPERSEDED_BY_094 / NO_POWER_SAVING
種別: EXACT_STRUCTURE / MOVING_SUPPORT_COORDINATE / SINGULAR_CARRIER_SPLIT
要点: The recombined defect theta=16ell+3(v+1) carries M_rel^4 in one rational coordinate on the generic full-S branch; theta!=0 has a fixed-theta elliptic compression, while theta=0 becomes an explicit Gaussian conic carrier.
主張の抜粋: Exact factorization theta=(v+1)^2(v+1-48x+64x^2)/(256vx^2) gives M_rel^4|Num(theta). Extra fresh valuation is the x=3/4 collision below saturation; fresh p==5 mod12 are exactly saturated. Fixed theta!=0 maps to Z^2=(v+1)(8+(7+4theta)v-v^2), smooth with rational 2-torsion. The unique singular theta=0 carrier is u^2+w^2=8. With q=c/d, the two branches have S denominators F_+=(2c+d)^2+c^2 or F_-=(c-2d)^2+d^2; resultants supported only on 2,3 imply the full fresh conductor satisfies M_rel^2|F_+ or M_rel^2|F_- with no extra fresh valuation. No fixed-power saving is claimed.
対象・測度: Exact fixed-content/coefficient nondegenerate generic full-S-denominator physical branch with R<=B and hard M_rel>B^(1/12-eta), split into theta!=0 and theta=0.
依存関係: M3-T11-091/092; M3-T11-045 / Section 52; hostile-audit-passed M3-T11-036; exact full-S saturation and fresh p==1 mod4.
再開条件の抜粋: Reopen if the theta factorization, fixed-theta discriminant/pushforward, theta=0 conic parameterization, or fresh no-cancellation resultant argument fails.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 103.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit

## Retained LEDGER source 1
SOURCE_START: 873973
SOURCE_END: 878871
SOURCE_SHA256: be3c8f08e5237d599f88c07d48613259a00537e0c4d886c3cf284d6740ef7e2c

RESEARCH_CARD=M3-T11-093
---
CARD_ID=M3-T11-093
TITLE=Fourth-power recombined defect coordinate and theta=0 Gaussian conic carrier
STATUS=PROVISIONAL EXACT_SAME_MEASURE_ADAPTER / MREL4_NUMERATOR_CARRIER / FIXED_THETA_BO1_CANDIDATE / SINGULAR_THETA0_ROUTER / HOSTILE_AUDIT_REQUIRED / NO_POWER_SAVING
TYPE=EXACT_STRUCTURE / MOVING_SUPPORT_COORDINATE / SINGULAR_CARRIER_SPLIT
CLAIM:
Define theta=16*ell+3*(v+1). Exact factorization gives
theta=(v+1)^2*(v+1-48*x+64*x^2)/(256*v*x^2).
On the exact generic full-S branch, v_p(v+1)=2lambda and x,v are p-units for every p^lambda||M_rel. Hence
M_rel^4|Num(theta)
and
gcd(Den(theta),M_rel)=1.
For theta!=0 the exact valuation is
v_p(theta)=4lambda+v_p(v+1-48x+64x^2),
and below the 2lambda saturation threshold the extra term is exactly the collision 4x-3:
min(v_p(theta)-4lambda,2lambda)=min(v_p(4x-3),2lambda).
If p==5 mod12, the Section-52 Legendre condition rules out x==3/4 mod p because it would require 3 to be a quadratic residue; therefore v_p(theta)=4lambda exactly at every fresh p==5 mod12.


For fixed theta, eliminating x gives
E_theta:
Z^2=(v+1)*(8+(7+4theta)*v-v^2),
with rational 2-torsion (-1,0) and discriminant
16*theta^2*(16*theta^2+56*theta+81).
The second factor has discriminant -2048, so every rational theta!=0 fiber is smooth. Reusing hostile-audit-passed M3-T11-036 gives the provisional same-measure adapter
fixed realized theta!=0 + fixed packet => B^o(1) physical endpoints.


The only singular value theta=0 is the conic
u^2+w^2=8,
x=(3+/-w)/8.
With parameter q,
u=2*(q^2-2q-1)/(1+q^2),
the two branches are
x_+=(q^2-4q+5)/(8*(1+q^2)),
S_+=4*(q^2-2q-1)/(5q^2+4q+1),
and
x_-=(5q^2+4q+1)/(8*(1+q^2)),
S_-=4*(q^2-2q-1)/(q^2-4q+5).
For q=c/d primitive define
F_-=(c-2d)^2+d^2,
F_+=(2c+d)^2+c^2.
The relevant resultants are supported only on 2 and 3:
Res(F_-,F_+)=1152,
Res(F_-,A_q)=Res(F_+,A_q)=8,
Res(F_-,B_q)=Res(F_+,B_q)=32.
Thus no fresh p can cancel between the displayed forms. Full-S exact saturation therefore gives
+ branch: M_rel^2|F_+ and gcd(F_+/M_rel^2,M_rel)=1,
- branch: M_rel^2|F_- and gcd(F_-/M_rel^2,M_rel)=1.
So theta=0 routes to one explicit Gaussian-norm square-divisor support problem. Fixed q fixes u and gives B^o(1) physical multiplicity via M3-T11-036.


POPULATION:
Exact fixed-content/coefficient nondegenerate generic full-S-denominator physical branch with R<=B and hard M_rel>B^(1/12-eta), split into theta!=0 and theta=0.


DEPENDENCIES:
M3-T11-091/092; M3-T11-045 / Section 52; hostile-audit-passed M3-T11-036; exact full-S saturation v_p(v+1)=2lambda and fresh p==1 mod4.


REQUIRED_OUTPUT:
For theta!=0, prove a same-physical-measure fixed-power bound for realized theta under the deterministic M_rel^4 numerator carrier. For theta=0, prove a one-twelfth bound for realized conic parameters q carrying the exact F_+ or F_- Gaussian norm square divisor.


DOES_NOT_IMPLY:
No M_rel^-4 ambient density, no closure of theta=0, no denominator-extreme support deficit, no primary-gate closure, no endpoint theorem, no P(B)/M3(B), and no Perfect Cuboid nonexistence.


NO_DOUBLE_CHARGE:
theta is an algebraic recombination of ell and v+1 on the same physical measure. Do not multiply the theta fourth-power carrier by the ell M_rel^2 carrier, residual character lock, fixed-fiber multiplicities, or old root-line factors.


ALIASES:
GenericFullSThetaNonzeroFourthPowerSupportOneTwelfth;
ThetaZeroConicGaussianNormSquareDivisorOneTwelfth;
FullSRecombinedDefectMrel4Carrier.


DUPLICATE_OF:
Not a duplicate. M3-T11-091 gives M_rel^2 in ell; M3-T11-092 gives the homogeneous defect/collision and residual character lock. M3-T11-093 finds the exact linear recombination theta whose numerator contains M_rel^4, proves the fixed-theta elliptic compression, identifies the sole singular theta=0 carrier, and converts that carrier to two explicit Gaussian norm square-divisor forms.


REOPEN_CONDITION:
Failure of the theta factorization; failure of fixed-theta discriminant or height/pushforward; failure of the theta=0 conic parameterization; fresh cancellation at primes outside {2,3}; or hostile audit finding a normalization error.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 103.


FLAGS:
M3_T11_FULL_S_THETA_COORDINATE=PROVISIONAL
M3_T11_FULL_S_THETA_MREL4_NUMERATOR=PROVISIONAL
M3_T11_FULL_S_THETA_OVERVALUATION_X_THREE_QUARTERS=PROVISIONAL
M3_T11_FULL_S_THETA_P5MOD12_EXACT_SATURATION=PROVISIONAL
M3_T11_FIXED_THETA_ELLIPTIC_2TORSION_CANDIDATE=true
M3_T11_FIXED_THETA_BO1_PROVED=false
M3_T11_THETA_ZERO_CONIC_CARRIER=PROVISIONAL
M3_T11_THETA_ZERO_GAUSSIAN_NORM_ROUTER=PROVISIONAL
M3_T11_DENOMINATOR_EXTREME_SUPPORT_DEFICIT_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
NEXT_LEGAL_ACTION=Hostile-audit M3-T11-090 through M3-T11-093. Mainbatch may prioritize the theta!=0 M_rel^4 support receiver and keep theta=0 on its separate Gaussian conic carrier.
NEXT_RESEARCH_CARD_ID=M3-T11-094.
