# M3-T11-042-A — Collision-free fourth-power fresh denominator on the symmetric middle coefficient E

CARD_ID: M3-T11-042
CANONICAL_CARD_KEY: M3-T11-042-A
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-042
ID確認: ID重複 1/2
現行一覧の状態: PROVED_EXACT_WITH_OPEN_COUNTING_GATE
種別: EXACT_STRUCTURE / SAME_MEASURE_CONDUCTOR_RECOMBINATION / FIXED_FIBER_CANDIDATE
要点: For the corrected anti-roots v_i=A_i/B_i and symmetric middle coefficient E=T_2/D, with D=B_1*B_2*B_3, T_2=A_1*A_2*B_3+A_1*A_3*B_2+A_2*A_3*B_1, every fresh prime p^lambda||m_i sati
主張の抜粋: For the corrected anti-roots v_i=A_i/B_i and symmetric middle coefficient E=T_2/D, with D=B_1*B_2*B_3, T_2=A_1*A_2*B_3+A_1*A_3*B_2+A_2*A_3*B_1, every fresh prime p^lambda||m_i satisfies v_p(Den(E))=4*lambda. Hence exactly on the relative-fresh support boxed: M_rel^4 | Den(E), and gcd(Den(E),M_rel^infinity)=M_rel^4. For
対象・測度: Exact fixed-content/coefficient nondegenerate relative-fresh endpoint packet.
依存関係: M3-T11-031, M3-T11-033, M3-T11-040, M3-T11-041.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 49.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

ID_COLLISION: Original ID has two distinct claims. A/B is a storage key only; no historical mathematical ID was reassigned.

## Retained LEDGER source 1
SOURCE_START: 645195
SOURCE_END: 648836
SOURCE_SHA256: 7bc96d9e207f54369543efad0d6fd167e32e355b69a7ecdbe518a9110aa84994

## M3-T11-042
TITLE: Collision-free fourth-power fresh denominator on the symmetric middle coefficient E
TYPE: EXACT_STRUCTURE / SAME_MEASURE_CONDUCTOR_RECOMBINATION / FIXED_FIBER_CANDIDATE
STATUS: PROVED_EXACT_WITH_OPEN_COUNTING_GATE


CLAIM:
For the corrected anti-roots v_i=A_i/B_i and symmetric middle coefficient
E=T_2/D,
with
D=B_1*B_2*B_3,
T_2=A_1*A_2*B_3+A_1*A_3*B_2+A_2*A_3*B_1,
every fresh prime p^lambda||m_i satisfies
v_p(Den(E))=4*lambda.
Hence exactly on the relative-fresh support
boxed:
M_rel^4 | Den(E),
and
gcd(Den(E),M_rel^infinity)=M_rel^4.


For the audited coordinates S=s/t and u=a/b, N_u=a^2+b^2,
boxed:
E=4*a*(b*s-a*t)/(t*N_u).
The M3-T11-040 fresh exponents
v_p(t)=2*lambda-c_p
and
min(4*lambda,v_p(N_u))=2*lambda+c_p
therefore recombine to the full baseline 4*lambda in one reduced rational coordinate.
The M_rel^4 denominator is not an additional saving; it is a collision-free repackaging of the already-consumed S/u conductor partition.


FIXED-E QUOTIENT:
For fixed e=E and u!=0,
S=[e+(e+4)u^2]/(4u).
With x=u^2 and Z=16*u^2*Y/(1+u^2), the split-cubic discriminant gives
Z^2=-F_e(x),
where
F_e(x)
=
(e+4)^4*x^4
+4*(e+4)^2*(e^2-12*e+112)*x^3
+2*e*(3*e^3-40*e^2-16*e+1280)*x^2
+4*e^2*(e^2-12*e-16)*x
+e^4.


Its discriminant is
-2^36*e^6*(e+4)^4*(3e-8)^3*(e^3-4e^2+4e+196).


The cubic factor has no rational root, so the only rational singular parameters are
e=0,-4,8/3.
They are absent on M_rel>1 because M_rel^4|Den(e) but their reduced denominators are 1,1,3.


Thus every physical large-M_rel fixed-E quotient is smooth genus one.
Over K=Q(i) it has explicit K-points at x=0, Z=+/-i*e^2 and at infinity, so it is elliptic over one fixed field after choosing an origin.


TORSION DIAGNOSTIC:
For the standard scaled Jacobian, exact symbolic factorization over Q(i)(e) leaves the 2-, 3-, and 5-division polynomials irreducible of degrees 3, 4, and 12 respectively.
Hence no generic rational-function torsion section of order 2, 3, or 5 is available.
This blocks a direct reuse of the M3-T11-036 low-prime-torsion/Dujella argument, but does not rule out every higher-prime mechanism.


POPULATION:
Exact fixed-content/coefficient nondegenerate relative-fresh endpoint packet.


HEIGHT:
Exact physical R<=B retained; E has polynomial height.


DEPENDS_ON:
M3-T11-031,
M3-T11-033,
M3-T11-040,
M3-T11-041.


IMPLIES:
For fixed realized E, compatible M_rel values are divisor-many.
A new parallel route is available through either a uniform fixed-E B^o(1) theorem plus active-E support deficit, or a direct same-measure fourth-power-denominator tail.


DOES_NOT_IMPLY:
No fixed-E B^o(1) theorem.
No active-E support deficit.
No independent density gain beyond M3-T11-040.
No P/M3 theorem.


NO_DOUBLE_CHARGE:
The M_rel^4 denominator is the single-coordinate recombination of the M3-T11-040 Q_S/C_u allocation and M3-T11-033 denominator carriers. Do not multiply its putative saving with Q_S or C_u without a new same-measure theorem.


ARSENAL_AUDIT:
AR-014 is only a fixed-outer common-gcd square-divisor fiber adapter and does not give a whole-family denominator-event deficit.
SR-STR-170 likewise leaves a same-measure square-divisor threshold-event theorem external.


FLAGS:
M3_T11_E_FULL_MREL4_DENOMINATOR=true
M3_T11_E_RECOMBINES_SU_FRESH_CONDUCTOR=true
M3_T11_E_FIXED_FIBER_GENUSONE_QUOTIENT=true
M3_T11_E_FIXED_FIBER_SINGULAR_LARGE_MREL_EMPTY=true
M3_T11_E_GENERIC_2_3_5_TORSION_SECTION=false
M3_T11_FIXED_E_UNIFORM_BO1_PROVED=false
M3_T11_E_DENOMINATOR_TAIL_PROVED=false
M3_T11_E_INDEPENDENT_SAVING=false
P_OVER_M3_LIMIT_PROVED=false


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 49.




---
