# M3-T11-035 — Fixed-field cubic-torsion uniform fiber upgrade for the symmetric (S,u) incidence

CARD_ID: M3-T11-035
CANONICAL_CARD_KEY: M3-T11-035
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-035
現行一覧の状態: PROVED_EXACT_WITH_OPEN_MOVING_SUPPORT_GATE HOSTILE_AUDIT_REQUIRED / NOT_YET_CANONICAL
種別: EXACT_STRUCTURE / SAME_MEASURE_ADAPTER / COMMON_GAUSSIAN_ROOTLINE THEOREM_CANDIDATE / SAME_MEASURE_FIXED_FIBER_ADAPTER
要点: Fixed-field cubic-torsion uniform fiber upgrade for the symmetric (S,u) incidence
主張の抜粋: Let S=v_1+v_2+v_3, P=v_1*v_2*v_3, r=P/S on the nondegenerate corrected three-anti-root endpoint locus. Then r=T_3/T_1, with M_rel^2|T_1 and gcd(T_3,M_rel)=1. Hence M_rel^2 | Den(r). Using the exact M3-T11-031 conic parameterization r=4*u^2/(1+u^2), write u=A_u/B_u reduced. On M_rel>1, r cannot equal 4, so u is finite. Moreover Den(r)=(A_u^2+B_u^2)/g_u, g_u in {1,2}. Since M_rel is odd, M_rel^2 | A_u^2+B_u^2. Thus one genuine common rational parameter satisfies A_u==rho_u*B_u mod M_rel^2, rho_u^2==-1 mod M_rel^2, gcd(B_u,M_rel)=1.
対象・測度: Exact fixed-content/coefficient relative-fresh endpoints on the nondegenerate large-M_rel branch.
依存関係: M3-T11-031; corrected M3-T11-030; M3-T11-033.
再開条件の抜粋: A same-measure moving-u support theorem, or an exact existing theorem adapter, yielding # active realized u << B^(1/12-delta) per fixed content/coefficient packet.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 41. K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 42.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 629255
SOURCE_END: 634683
SOURCE_SHA256: c51f7d77731b81d9d1b739e15dc8870d1adf2586c363819354a5fe7461c31ba5

CARD_ID: M3-T11-035


TYPE: EXACT_STRUCTURE / SAME_MEASURE_ADAPTER / COMMON_GAUSSIAN_ROOTLINE
STATUS: PROVED_EXACT_WITH_OPEN_MOVING_SUPPORT_GATE


CLAIM:
Let
S=v_1+v_2+v_3,
P=v_1*v_2*v_3,
r=P/S
on the nondegenerate corrected three-anti-root endpoint locus.


Then r=T_3/T_1, with
M_rel^2|T_1
and
gcd(T_3,M_rel)=1.


Hence
M_rel^2 | Den(r).


Using the exact M3-T11-031 conic parameterization
r=4*u^2/(1+u^2),
write u=A_u/B_u reduced.


On M_rel>1, r cannot equal 4, so u is finite.
Moreover
Den(r)=(A_u^2+B_u^2)/g_u,
g_u in {1,2}.


Since M_rel is odd,
M_rel^2 | A_u^2+B_u^2.


Thus one genuine common rational parameter satisfies
A_u==rho_u*B_u mod M_rel^2,
rho_u^2==-1 mod M_rel^2,
gcd(B_u,M_rel)=1.


POPULATION:
Exact fixed-content/coefficient relative-fresh endpoints on the nondegenerate large-M_rel branch.


HEIGHT:
Exact R<=B retained.
The common-u norm satisfies
A_u^2+B_u^2
=
g_u*|T_1|/gcd(T_1,T_3)
and is polynomially bounded on the physical packet.


DEPENDS_ON:
M3-T11-031;
corrected M3-T11-030;
M3-T11-033.


IMPLIES:
For fixed realized u, the compatible M_rel values are divisor-many:
B^o(1).
Therefore
# active M_rel
<=
B^o(1) * # active realized u.


A sufficient current target is
# active realized u << B^(1/12-delta).


ALIASES:
symmetric common-u root line;
valid full-fresh common rational coordinate;
common-u M_rel^2 Gaussian rootline;
active-u support receiver.


DUPLICATE_OF:
none.
This is not M3-T11-029 one-core v.
It is not the retracted Section-31 common-v CRT.
It is not the M3-T11-032/033 Gaussian product coefficient pair.


SUPERSEDES:
M3-T11-034, which is retracted.
It also supersedes ThreeAntiRootCubicCoefficientRootLineRangeAdapter as the active supporting attack.


DO_NOT_REPEAT:
Do not treat this pointwise common-u root line as a moving-support theorem.
Do not multiply it by the three one-core root-line savings without a no-double-charge theorem.
Do not reopen the u=infinity branch on M_rel>1.
Do not use fixed-u genus one as a uniform B^o(1) theorem without the missing uniform input.


REOPEN_CONDITION:
A same-measure moving-u support theorem, or an exact existing theorem adapter, yielding
# active realized u << B^(1/12-delta)
per fixed content/coefficient packet.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 41.


CURRENT_MINIMAL_TARGET=SymmetricCommonUFullFreshRootLineSupportOneTwelfth
M3_T11_COMMON_U_FULL_MREL2_ROOTLINE=true
M3_T11_FIXED_U_MREL_MULTIPLICITY=BO1
M3_T11_ACTIVE_U_SUPPORT_DEFICIT_PROVED=false
P_OVER_M3_LIMIT_PROVED=false




---
PROVISIONAL CANDIDATE — M3-T11-036
TITLE: Fixed-field cubic-torsion uniform fiber upgrade for the symmetric (S,u) incidence
TYPE: THEOREM_CANDIDATE / SAME_MEASURE_FIXED_FIBER_ADAPTER
STATUS: HOSTILE_AUDIT_REQUIRED / NOT_YET_CANONICAL


CLAIM_CANDIDATE:
Retain M3-T11-031 and M3-T11-035:
Y^2=-(1+u^2)Q(S,u)
with
Q(S,u)=-4S^2+S^4+48Su-16S^3u-16u^2+44S^2u^2+S^4u^2.


For every physical rational u!=0, the fixed-u binary quartic is smooth.  On the scaled Jacobian
y^2=x^3-27 I_u x-27 J_u
with
I_u=16(1+u^2)^3(1+109u^2),
J_u=128(1+u^2)^4(-1+268u^2+1727u^4),
the point
x=-36(1+u^2)^2,
y=48*sqrt(-3)*(1+u^2)^2*(25u^2-2)
has exact order 3 over the fixed field K=Q(sqrt(-3)).


Likewise, treating the same incidence as a quartic in u for fixed rational S, its discriminant is
2^20*S^2*(S^2-8)^3*(1+S^2)^6,
and its scaled Jacobian has the K-rational exact 3-torsion point
x=-36(S^2-2)^2,
y=96*sqrt(-3)*(S^2-8)*(1+S^2)^2.


PROPOSED_OUTPUT_IF_AUDITED:
Using Marta Dujella's uniform bounded-height theorem over the one fixed number field K, together with the fixed-degree binary-quartic covering map and the exact physical polynomial-height adapter,
fixed realized u + fixed content/coefficient packet
=> B^o(1) physical endpoint states,
and symmetrically
fixed realized S + fixed content/coefficient packet
=> B^o(1) physical endpoint states.


EXTERNAL_THEOREM:
Marta Dujella, "Uniform Bounds for the Number of Rational Points of Bounded Height on Certain Elliptic Curves" (Acta Arith. 217; arXiv:2312.03655).
Required theorem feature: fixed number field k; elliptic curve carries a k-rational point of exact prime order; uniform exp(C(k) log H/log log H) bounded-height count.


HEIGHT:
Exact physical R<=B.  The promotion audit must verify uniformly that the anti-root coordinates, S,u, quartic coefficients, covering map, and Jacobian image heights are B^O(1).


ANTI_LOOP_ADDENDUM:
The exact identity
u^2=T_3/(4T_1-T_3)
gives
T_3=G A_u^2,
4T_1-T_3=G B_u^2,
4T_1=G(A_u^2+B_u^2),
with G=gcd(T_3,4T_1-T_3)=gcd(T_3,4T_1)=4*gcd(T_1,T_3)/g_u up to the common sign, g_u in {1,2}.
This is not a new independent squareclass saving; it is equivalent to the M3-T11-035 common-u norm carrier.


DOES_NOT_IMPLY:
No moving-u support deficit.
No new root-line density factor.
No proof of #active realized u << B^(1/12-delta).
No P/M3 limit theorem.


PROMOTION_BOUNDARY:
If hostile audit passes, promote the former open fixed-u-uniformity flag and register the symmetric fixed-S fiber theorem.  Until then, all new positive flags remain CANDIDATE only.


CANDIDATE_FLAGS:
M3_T11_FIXED_U_K_RATIONAL_3TORSION_CANDIDATE=true
M3_T11_FIXED_S_K_RATIONAL_3TORSION_CANDIDATE=true
M3_T11_FIXED_U_UNIFORM_BO1_CANDIDATE=true
M3_T11_FIXED_S_UNIFORM_BO1_CANDIDATE=true
M3_T11_ACTIVE_U_SUPPORT_DEFICIT_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
NEXT_REQUIRED_ACTION=stage37audit
DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 42.




---
