# M3-T11-091 — Exact full-S Legendre defect saturates the fresh conductor and has fixed-defect elliptic fibers

CARD_ID: M3-T11-091
CANONICAL_CARD_KEY: M3-T11-091
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-091
現行一覧の状態: PROVED_EXACT / HOSTILE_AUDIT_PASS / EXACT_FRESH_VALUATION_SATURATION / FIXED_DEFECT_BO1 / NO_POWER_SAVING
種別: THEOREM_ADAPTER / MOVING_SUPPORT_COORDINATE / FRESH_CONDUCTOR_SATURATION
要点: On the generic full-S-denominator branch, the Legendre defect ell=r^2-x(1-x) carries the full fresh conductor square with exact valuation and has a fixed-ell elliptic compression.
主張の抜粋: Exact factorization gives ell=(v+1)G_x(v)/(4096*v*x^2), with G_x(v)=(v+1)^2-48(v+1)x+64(1-11v)x^2. For every p^lambda||M_rel on c_p=0, v_p(v+1)=2lambda and G_x(v)==768x^2 mod p is a fresh p-unit, so v_p(ell)=2lambda exactly. Thus M_rel^2|Num(ell), gcd(Num(ell)/M_rel^2,M_rel)=1 and gcd(Den(ell),M_rel)=1. Fixed ell maps to Z^2=(v+1)(11v^2+(19+64ell)v+8), smooth for rational ell!=0 and carrying rational 2-torsion (-1,0). Reusing audited M3-T11-036 gives the provisional candidate fixed ell + packet => B^o(1) physical endpoints. No support deficit is claimed.
対象・測度: Exact fixed-content/coefficient nondegenerate generic full-S-denominator physical branch with R<=B, all relative-fresh primes in c_p=0; hard branch M_rel>B^(1/12-eta).
依存関係: M3-T11-045 / Section 52 exact x,r,P_x(v) and Legendre congruence; hostile-audit-passed M3-T11-036; Sections 49-50 exact fresh norm saturation and full-S normalization.
再開条件の抜粋: Reopen if the Section-52 factorization/input coordinates fail, c_p=0 exact saturation v_p(N_u)=2lambda fails, M3-T11-036 is retracted, or hostile audit rejects the fixed-ell height/pushforward adapter.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 101.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 864936
SOURCE_END: 869309
SOURCE_SHA256: 1f3256ea42eb141fbee42bba3933bb87abed126071ab18341f97c1faba982609

RESEARCH_CARD=M3-T11-091
---
CARD_ID=M3-T11-091
TITLE=Exact full-S Legendre defect saturates the fresh conductor and has fixed-defect elliptic fibers
STATUS=PROVISIONAL EXACT_SAME_MEASURE_ADAPTER / EXACT_FRESH_VALUATION_SATURATION / FIXED_DEFECT_BO1_CANDIDATE / HOSTILE_AUDIT_REQUIRED / NO_POWER_SAVING
TYPE=THEOREM_ADAPTER / MOVING_SUPPORT_COORDINATE / FRESH_CONDUCTOR_SATURATION
CLAIM:
On the exact nondegenerate generic full-S-denominator branch define
ell=r^2-x*(1-x),
with the Section-52 coordinates v=u^2, r=R_x/(64*u*x), and R_x^2=P_x(v).
Then
P_x(v)-4096*v*x^3*(1-x)
=(v+1)*[(v+1)^2-48*(v+1)*x+64*(1-11*v)*x^2],
hence
ell=(v+1)*G_x(v)/(4096*v*x^2).
For every relative-fresh p^lambda||M_rel on this branch, c_p=0 gives v_p(v+1)=2*lambda while x,v are p-units and G_x(v)==768*x^2 mod p. Since fresh p==1 mod4, G_x(v) is a p-unit. Therefore
v_p(ell)=2*lambda
exactly for all p^lambda||M_rel. Equivalently
M_rel^2|Num(ell),
gcd(Num(ell)/M_rel^2,M_rel)=1,
gcd(Den(ell),M_rel)=1.
On M_rel>1, ell!=0.
For fixed ell, eliminating x gives
E_ell: Z^2=(v+1)*(11*v^2+(19+64*ell)*v+8),
with rational 2-torsion (-1,0). Its cubic discriminant is
4096*ell^2*(4096*ell^2+2432*ell+9);
the second factor has no rational zero, so every rational ell!=0 fiber is smooth.
The same M3-T11-036 uniform bounded-height theorem therefore gives the provisional same-measure adapter
fixed realized ell + fixed packet => B^o(1) physical endpoints.
POPULATION:
Exact fixed-content/coefficient nondegenerate generic full-S-denominator physical branch with exact R<=B, all relative-fresh primes in c_p=0, and x not in {0,-1/8,27/40}. The hard theorem branch has M_rel>B^(1/12-eta).
DEPENDENCIES:
M3-T11-045 / Section 52 exact x, r, P_x(v), and full-modulus Legendre congruence; hostile-audit-passed M3-T11-036 fixed-u physical multiplicity and uniform bounded-height theorem; Sections 49-50 exact fresh norm saturation and full-S c_p=0 normalization.
REQUIRED_OUTPUT:
Uniformly per fixed packet, prove a same-physical-measure fixed-power bound
# {realized ell on the exact generic full-S branch with M_rel>B^(1/12-eta),
   M_rel^2|Num(ell),
   gcd(Num(ell)/M_rel^2,M_rel)=1}
<<B^(1/12-delta)
for some fixed delta>eta>0, or an equivalent global dispersion/support theorem.
DOES_NOT_IMPLY:
No fixed-power saving follows from M_rel^2|Num(ell) alone. No denominator-extreme closure, primary-gate closure, endpoint theorem, P(B)/M3(B) limit, or Perfect Cuboid nonexistence.
NO_DOUBLE_CHARGE:
The exact numerator square is a deterministic re-expression of the already-present fresh conductor on the same physical measure. Do not charge M_rel^-2 as ambient density; do not multiply fixed-ell, fixed-x, or fixed-u B^o(1) fibers; do not multiply the local Legendre density independently.
ALIASES:
GenericFullSDenominatorLegendreDefectSquareNumeratorSupportOneTwelfth;
GenericFullSLegendreDefectExactFreshSaturation;
FixedLegendreDefectElliptic2TorsionCompression.
DUPLICATE_OF:
Not a duplicate. M3-T11-045 produced x and the congruence r^2==x(1-x) mod M_rel^2 but not an exact defect valuation or fixed-defect elliptic fiber. M3-T11-090 compresses fixed x; M3-T11-091 introduces a different support coordinate whose reduced numerator carries M_rel^2 with exact fresh valuation.
REOPEN_CONDITION:
Failure of the Section-52 factorization/input coordinates; failure of c_p=0 exact saturation v_p(N_u)=2lambda; retraction of M3-T11-036; or hostile audit finding that the fixed-ell height/pushforward adapter is not uniform.
DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 101.
FLAGS:
M3_T11_GENERIC_FULL_S_LEGENDRE_DEFECT_COORDINATE=PROVISIONAL
M3_T11_GENERIC_FULL_S_LEGENDRE_DEFECT_FRESH_VALUATION_EXACT=PROVISIONAL
M3_T11_GENERIC_FULL_S_LEGENDRE_DEFECT_NUMERATOR_MREL2=PROVISIONAL
M3_T11_GENERIC_FULL_S_LEGENDRE_DEFECT_NO_EXTRA_FRESH_VALUATION=PROVISIONAL
M3_T11_FIXED_LEGENDRE_DEFECT_ELLIPTIC_2TORSION_CANDIDATE=true
M3_T11_FIXED_LEGENDRE_DEFECT_BO1_PROVED=false
M3_T11_GENERIC_LEGENDRE_DEFECT_SUPPORT_COORDINATE=PROVISIONAL
M3_T11_DENOMINATOR_EXTREME_SUPPORT_DEFICIT_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
NEXT_LEGAL_ACTION=Hostile-audit M3-T11-090 and M3-T11-091. Mainbatch may attack the exact realized-ell support; do not charge the square numerator, fixed-fiber multiplicities, common-u support, or local Legendre tensorization as independent savings.
NEXT_RESEARCH_CARD_ID=M3-T11-092.






0
