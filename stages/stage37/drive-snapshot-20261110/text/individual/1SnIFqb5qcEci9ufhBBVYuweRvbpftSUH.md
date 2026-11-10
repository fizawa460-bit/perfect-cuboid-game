# M3-T11-042-B — Exact common-u norm saturation inside the cubic denominator

CARD_ID: M3-T11-042
CANONICAL_CARD_KEY: M3-T11-042-B
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-042
ID確認: ID重複 2/2
現行一覧の状態: PROVED_EXACT
種別: EXACT_STRUCTURE / INTEGER_NORMAL_FORM / ANTI_LOOP_FIREWALL
要点: Write u=a/b reduced, N_u=a^2+b^2, g_u=gcd(4,N_u) in {1,2}, and retain S=T_1/D, E=T_2/D, P=T_3/D. The canonical symmetric parameterization gives exactly N_u*T_3=4*a^2*T_1, N_u*T_2=4
主張の抜粋: Write u=a/b reduced, N_u=a^2+b^2, g_u=gcd(4,N_u) in {1,2}, and retain S=T_1/D, E=T_2/D, P=T_3/D. The canonical symmetric parameterization gives exactly N_u*T_3=4*a^2*T_1, N_u*T_2=4*a*b*T_1-4*a^2*D. Hence N_u/g_u | T_1 and, using the second identity, boxed: N_u/g_u | D. Let d=gcd(T_1,T_3), epsilon=sign(T_1), and R_u=N_u
対象・測度: Exact fixed-content/coefficient nondegenerate relative-fresh endpoint packet on the audited symmetric (S,u) coordinates.
依存関係: M3-T11-031, M3-T11-035, M3-T11-033, M3-T11-040, M3-T11-041.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 49.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

ID_COLLISION: Original ID has two distinct claims. A/B is a storage key only; no historical mathematical ID was reassigned.

## Retained LEDGER source 1
SOURCE_START: 648836
SOURCE_END: 651927
SOURCE_SHA256: 1f12a32339ff91ed1984afc08870f9c35119c2460f9fbacae7d6b6180600043b

## M3-T11-042
TITLE: Exact common-u norm saturation inside the cubic denominator
TYPE: EXACT_STRUCTURE / INTEGER_NORMAL_FORM / ANTI_LOOP_FIREWALL
STATUS: PROVED_EXACT


CLAIM:
Write u=a/b reduced, N_u=a^2+b^2, g_u=gcd(4,N_u) in {1,2}, and retain S=T_1/D, E=T_2/D, P=T_3/D.


The canonical symmetric parameterization gives exactly


N_u*T_3=4*a^2*T_1,


N_u*T_2=4*a*b*T_1-4*a^2*D.


Hence


N_u/g_u | T_1


and, using the second identity,


boxed:
N_u/g_u | D.


Let d=gcd(T_1,T_3), epsilon=sign(T_1), and R_u=N_u/g_u.  Since M3-T11-035 gives R_u=|T_1|/d, there is an integer K>0 with


D=K*R_u,
T_1=epsilon*d*R_u,
S=epsilon*d/K,


and


T_3=epsilon*(4*d/g_u)*a^2,
T_2=(4/g_u)*(epsilon*a*b*d-a^2*K).


Thus


g_u*F_v(X)
=
N_u*K*X^3
-epsilon*d*N_u*X^2
+4*(epsilon*a*b*d-a^2*K)*X
-epsilon*4*a^2*d.


For every fresh p^lambda||m_i, p does not divide d*g_u and v_p(D)=4*lambda.  Combining S=epsilon*d/K with M3-T11-040 yields


v_p(K)=2*lambda-c_p,


and therefore the previous capped common-u norm valuation upgrades to


boxed:
v_p(N_u)=2*lambda+c_p


for every fresh prime, including c_p=2*lambda.


Consequently


boxed:
(N_u)_{M_rel-fresh}=M_rel^2*C_u,


and for N_*=N_u/(M_rel^2*C_u),


boxed:
gcd(N_*,M_rel)=1.


Combining with M3-T11-041 gives W_*^2=-N_*Phi_* with all residual fresh valuation carried by Phi_*, and v_p(Phi_*) even.


POPULATION:
Exact fixed-content/coefficient nondegenerate relative-fresh endpoint packet on the audited symmetric (S,u) coordinates.


HEIGHT:
Exact physical R<=B retained.


DEPENDS_ON:
M3-T11-031,
M3-T11-035,
M3-T11-033,
M3-T11-040,
M3-T11-041.


NOVELTY:
The divisor N_u/g_u|D and the resulting uncapped valuation v_p(N_u)=2*lambda+c_p were not present in the prior conductor-partition card.  This removes a genuine uncertainty at the extreme c_p=2*lambda boundary.


IMPLIES:
The C_u factor is the entire fresh common-u norm excess, not a capped proxy.
Fresh valuation v_p(N_u)>4*lambda is impossible.
The normalized factor N_* is coprime to all fresh conductor primes.
At an extreme amplified-u prime, any residual p-factor of Phi_* is even and, when present, lies on the S Gaussian root line from the M3-T11-041 resultant.


DOES_NOT_IMPLY:
No fixed-power extreme-tail theorem.
No global character dispersion theorem.
No P/M3 limit theorem.


NO_DOUBLE_CHARGE:
Since N_u/g_u is already an exact divisor of D, do not charge the amplified-u C_u condition and a separate divisor-density event N_u/g_u|D as independent savings.


ANTI_LOOP:
Do not search for fresh valuation beyond p^(4*lambda) in A_u^2+B_u^2.  M3-T11-042 proves this branch is saturated exactly at the M3-T11-040 cap.


FLAGS:
M3_T11_COMMON_U_NORM_OVER_G_DIVIDES_D=true
M3_T11_COMMON_U_INTEGER_NORMAL_FORM=true
M3_T11_FRESH_COMMON_U_NORM_VALUATION_EXACT=true
M3_T11_COMMON_U_NORM_FRESH_PART=MREL2_TIMES_CU
M3_T11_NORMALIZED_N_FRESH_COPRIME=true
M3_T11_FRESH_NORM_ABOVE_MREL4_IMPOSSIBLE=true
M3_T11_AMPLIFIED_U_DIVISOR_DENSITY_INDEPENDENT=false
M3_T11_EXTREME_RESIDUAL_TAIL_PROVED=false
P_OVER_M3_LIMIT_PROVED=false


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 49.


---
