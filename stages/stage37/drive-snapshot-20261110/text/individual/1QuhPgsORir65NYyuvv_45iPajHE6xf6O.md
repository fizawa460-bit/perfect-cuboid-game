# M3-T11-059 — Primitive common-norm descent to four exact squarefree-kernel packets

CARD_ID: M3-T11-059
CANONICAL_CARD_KEY: M3-T11-059
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-059
現行一覧の状態: PROVED_EXACT_DESCENT / GLOBAL_CLASSIFICATION_OPEN
種別: EXACT_DESCENT / THEOREM_GATE
要点: In the M3-T11-058 common-norm presentation R=b*(124a^2+9b^2), I=a*(100a^2+7b^2), Y_h^2=R^2+14I^2, gcd(a,b)=1, b>0, put d=gcd(R,I). Then d is supported on {2,3,5} with exact valuati
主張の抜粋: In the M3-T11-058 common-norm presentation R=b*(124a^2+9b^2), I=a*(100a^2+7b^2), Y_h^2=R^2+14I^2, gcd(a,b)=1, b>0, put d=gcd(R,I). Then d is supported on {2,3,5} with exact valuations v_3(d)=min(v_3(a),2), v_5(d)=min(v_5(b),2), and v_2(d)=0 if b odd, v_2(d)=2 if v_2(b)>=2, while for b=2c with c odd, v_2(d)=min(3+v_2(31
対象・測度: Exact x=27/40 translated-lift carrier inherited from M3-T11-045 through M3-T11-058.
依存関係: M3-T11-056; M3-T11-057; M3-T11-058; elementary primitive factorization of (Y0-R0)(Y0+R0)=14I0^2.
再開条件の抜粋: Distribute the nearly-coprime factors of I=a*(100a^2+7b^2) across u,v in each delta packet, respecting the exact d valuation profile, and reduce every surviving packet to a solvable lower-genus/Thue/elliptic problem; intersect with M3-T11-0
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 66.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 713451
SOURCE_END: 716628
SOURCE_SHA256: 20984a23de1a6cba7dd3428c0da2e2a40f6f735b29daf42888cb3c428f0d21b0

## M3-T11-059
ID:
M3-T11-059
TYPE:
EXACT_DESCENT / THEOREM_GATE
TITLE:
Primitive common-norm descent to four exact squarefree-kernel packets
STATUS:
PROVED_EXACT_DESCENT / GLOBAL_CLASSIFICATION_OPEN


CLAIM:
In the M3-T11-058 common-norm presentation
R=b*(124a^2+9b^2),
I=a*(100a^2+7b^2),
Y_h^2=R^2+14I^2,
gcd(a,b)=1, b>0,
put d=gcd(R,I). Then d is supported on {2,3,5} with exact valuations
v_3(d)=min(v_3(a),2),
v_5(d)=min(v_5(b),2),
and
v_2(d)=0 if b odd,
v_2(d)=2 if v_2(b)>=2,
while for b=2c with c odd,
v_2(d)=min(3+v_2(31a^2+9c^2),2+v_2(25a^2+7c^2)) in {5,6}.


After primitive normalization
R0=R/d, I0=I/d, Y0=Y_h/d,
one has
gcd(R0,I0)=1,
R0 odd,
I0 even,
7∤R0.
Putting
A=(Y0+R0)/2,
B=(Y0-R0)/2
gives gcd(A,B)=1 and
A*B=14*(I0/2)^2.
Therefore there is a unique delta in {1,2,7,14} and coprime u,v such that
A=delta*u^2,
B=(14/delta)*v^2,
hence
R0=delta*u^2-(14/delta)*v^2,
I0=2uv,
Y0=delta*u^2+(14/delta)*v^2.


This is an exact four-packet classification of the primitive Q(sqrt(-14)) common-norm receiver and uses no UFD assumption.


LOCAL CONSEQUENCES:
- if b odd, a must be even;
- if v_2(b)>=2, the translated-lift equation has no solution;
- if v_2(b)=1, b=2c, a,c odd, a solution requires
  c^2==a^2 mod 32;
- necessarily
  7∤b*(a^2-b^2).


POPULATION:
Exact x=27/40 translated-lift carrier inherited from M3-T11-045 through M3-T11-058.


DEPENDS_ON:
M3-T11-056;
M3-T11-057;
M3-T11-058;
elementary primitive factorization of (Y0-R0)(Y0+R0)=14I0^2.


IMPLIES:
The M3-T11-058 ideal-class descent is no longer an open abstract class-group classification problem. It is replaced by four explicit squarefree-kernel packets delta=1,2,7,14 together with exact 2,3,5 common-content valuations and a ramified-7 exclusion.


ALIASES:
X27Over40FourNormPackets;
X27Over40PrimitiveMinus14NormPacketDescent;
X27Over40FourNormPacketsFactorDistribution.


DO_NOT_REPEAT:
Do not invoke unique factorization in Z[sqrt(-14)].
Do not reopen a generic ideal-class enumeration before using the four explicit packets.
Do not treat the four-packet classification as a rational-point classification.
Do not promote fixed-power saving or P/M3 credit from these local/descent constraints alone.


REOPEN_CONDITION:
Distribute the nearly-coprime factors of
I=a*(100a^2+7b^2)
across u,v in each delta packet, respecting the exact d valuation profile, and reduce every surviving packet to a solvable lower-genus/Thue/elliptic problem; intersect with M3-T11-057.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 66.


FLAGS:
M3_T11_X_27_OVER_40_COMMON_CONTENT_VALUATIONS_EXACT=true
M3_T11_X_27_OVER_40_PRIMITIVE_NORM_FOUR_PACKETS=true
M3_T11_X_27_OVER_40_PRIMITIVE_NORM_R_ODD_I_EVEN=true
M3_T11_X_27_OVER_40_RAMIFIED_7_EXCLUSION=true
M3_T11_X_27_OVER_40_V2B_GE2_EXCLUDED=true
M3_T11_X_27_OVER_40_V2B_EQ1_MOD32_FILTER=true
M3_T11_X_27_OVER_40_RATIONAL_POINTS_CLASSIFIED=false
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
CURRENT_X27_FIRST_ATTACK=X27Over40FourNormPacketsFactorDistribution
CURRENT_X27_SECOND_ATTACK=X27Over40EllipticLogHeightReductionBelow1328040
CURRENT_X27_THIRD_ATTACK=X27Over40SplitJacobianQuadraticChabauty
RESEARCH_CARD=M3-T11-059
