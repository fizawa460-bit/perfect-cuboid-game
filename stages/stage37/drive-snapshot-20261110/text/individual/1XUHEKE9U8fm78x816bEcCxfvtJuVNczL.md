# M3-T11-045 — Full-S-denominator Legendre x-coordinate and generic fixed-x cubic

CARD_ID: M3-T11-045
CANONICAL_CARD_KEY: M3-T11-045
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-045
現行一覧の状態: PROVED_EXACT_WITH_PROVISIONAL_COUNTING_ADAPTER
種別: EXACT_STRUCTURE / SAME_MEASURE_LOCAL-TO-GLOBAL_ADAPTER / THEOREM-GATE_REFINEMENT / FIREWALL
要点: On the canonical symmetric packet put S=s/t, u=a/b, N=1+u^2, and on a remaining full-S-denominator fresh prime p^lambda||m_i with c_p=0 put n=2*lambda. Then v_p(N)=v_p(t)=n. Define
主張の抜粋: On the canonical symmetric packet put S=s/t, u=a/b, N=1+u^2, and on a remaining full-S-denominator fresh prime p^lambda||m_i with c_p=0 put n=2*lambda. Then v_p(N)=v_p(t)=n. Define T=N*S, delta=T-16u, and boxed: x=T/(16u)=((1+u^2)S)/(16u)=(a^2+b^2)*s/(16*a*b*t). Exact algebra gives boxed: N^3*Q(S,u)=delta*T^3-4*N*H(del
対象・測度: Exact fixed-content/coefficient nondegenerate relative-fresh endpoint packet, restricted primewise to the c_p=0 full-S-denominator allocation when invoking the x-congruence.
依存関係: M3-T11-031; M3-T11-036 for the previously audited fixed-field Dujella theorem species; M3-T11-040; M3-T11-041; M3-T11-042 exact fresh norm saturation / E denominator inputs; M3-T11-043.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 52.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 657529
SOURCE_END: 663824
SOURCE_SHA256: 7849e08be3978e41f2c4d226b55beba6164de34d9c15bb0419eb063d0a77fd6b

## M3-T11-045
TITLE: Full-S-denominator Legendre x-coordinate and generic fixed-x cubic
TYPE: EXACT_STRUCTURE / SAME_MEASURE_LOCAL-TO-GLOBAL_ADAPTER / THEOREM-GATE_REFINEMENT / FIREWALL
STATUS: PROVED_EXACT_WITH_PROVISIONAL_COUNTING_ADAPTER


CLAIM:
On the canonical symmetric packet put
S=s/t,
u=a/b,
N=1+u^2,
and on a remaining full-S-denominator fresh prime p^lambda||m_i with c_p=0 put n=2*lambda.
Then
v_p(N)=v_p(t)=n.
Define
T=N*S,
delta=T-16u,
and
boxed:
x=T/(16u)=((1+u^2)S)/(16u)=(a^2+b^2)*s/(16*a*b*t).


Exact algebra gives
boxed:
N^3*Q(S,u)=delta*T^3-4*N*H(delta,u),
with
H(delta,u)
=
-11*delta^2*u^2+delta^2
-364*delta*u^3+20*delta*u
+4*u^6-3000*u^4+68*u^2.


Since Y^2=-NQ,
boxed:
(NY)^2=-delta*T^3+4*N*H.
Modulo p^n this yields, after division by the square p-unit (16uT)^2,
boxed:
r^2 == x*(1-x) mod p^n,
r=NY/(16uT).


If
M_0=product p^lambda
over all c_p=0 fresh prime powers, CRT gives
boxed:
r^2 == x*(1-x) mod M_0^2.


Also, using Q=Phi/(t^4*b^2),
boxed:
min(v_p(Phi_*),n)=min(v_p(x-1),n).
Thus the M3-T11-043 normalized collision is exactly x==1 mod p; below saturation the residual exponent equals v_p(x-1) and is even.


For fixed rational x, substituting delta=16u(x-1), v=u^2 and R_x=NY/(4u) gives
boxed:
R_x^2=P_x(v),
where
P_x(v)
=
v^3
+(3-48*x-704*x^2)*v^2
+(3-96*x-640*x^2+4096*x^3-4096*x^4)*v
+(1-48*x+64*x^2).


Its discriminant is
boxed:
2^24*x^8*(8*x+1)*(40*x-27)^3.
Hence every rational fixed-x fiber outside
x in {0,-1/8,27/40}
is a smooth elliptic cubic.


Its 3-division polynomial contains the factor
3*v+64*x^2-48*x+3.
At
v_0=-(64*x^2-48*x+3)/3,
boxed:
P_x(v_0)=-4096*x^4*(40*x-27)^2/27.
Therefore every smooth fixed-x fiber has an explicit exact order-3 point over the one fixed field K=Q(sqrt(-3)):
boxed:
(v_0,R_0)
=
(
 -(64*x^2-48*x+3)/3,
 (64/9)*sqrt(-3)*x^2*(40*x-27)
).


The corresponding Dujella/fixed-height B^o(1) replay is a candidate only and is not promoted until an independent hostile audit verifies the new fixed-x physical pushforward and height adapter.


The two rational singular carriers are explicit:
boxed:
x=-1/8:
P_x(v)=(v-2)^2*(v+2),
and the original anti-root cubic factors as
[(1+u^2)z-2u]*[(1+u^2)z^2+4uz-4u^2]/(1+u^2)^2,
so physical full splitting requires the rational conic
w^2=u^2+2.
Moreover
x(1-x)=-9/64,
so the Legendre detector is automatic at every fresh split prime p==1 mod 4.


boxed:
x=27/40:
P_x(v)=(v-350)*(25v-2)^2/625,
so the discriminant-square condition forces the necessary conic
w^2=u^2-350;
full anti-root splitting is an additional open condition.


LOCAL-DENSITY FIREWALL:
For p==1 mod 4, among residues x mod p with x not in {0,1}, exactly (p-3)/2 satisfy that x(1-x) is a nonzero square.
Each has p^(n-1) lifts modulo p^n.
Thus the full-modulus detector admits at least
((p-3)/2)*p^(n-1)
classes mod p^n and has positive-constant local density.
Naive CRT tensorization therefore gives only a subpower factor 2^(-omega(M_0))*M_0^o(1), not a fixed-power saving.


POPULATION:
Exact fixed-content/coefficient nondegenerate relative-fresh endpoint packet, restricted primewise to the c_p=0 full-S-denominator allocation when invoking the x-congruence.


HEIGHT:
Exact physical R<=B retained.
The exact coordinate x is a fixed-degree rational function of the already-audited S,u coordinates.
The generic fixed-x B^o(1) theorem remains provisional pending hostile audit.


DEPENDS_ON:
M3-T11-031;
M3-T11-036 for the previously audited fixed-field Dujella theorem species;
M3-T11-040;
M3-T11-041;
M3-T11-042 exact fresh norm saturation / E denominator inputs;
M3-T11-043.


IMPLIES:
The c_p=0 branch has one full-modulus Legendre coordinate rather than separate first-order residual and unit-character descriptions.
The positive residual valuation is exactly the truncated p-adic distance of x from 1.
The live denominator-extreme theorem can be reformulated as
FullSDenominatorLegendreXSupportOneTwelfth,
plus the explicit singular carriers x=-1/8 and x=27/40.


DOES_NOT_IMPLY:
No fixed-power moving-x support deficit.
No canonical fixed-x B^o(1) theorem before audit.
No bound for either singular carrier.
No independence from the already-consumed Q_S/C_u conductor partition.
No P(B)/M3(B) limit theorem.


NO_DOUBLE_CHARGE:
The modulus M_0^2 is the same fresh conductor already allocated to the full-S-denominator side of M3-T11-040.
The Legendre congruence repackages the exact endpoint condition on that same measure; it is not an additional independent density factor.


ALIASES:
FullSDenominatorLegendreX;
FullSDenominatorLegendreXSupportOneTwelfth;
CPZeroFullModulusLegendre;
SymmetricXFixedFiberCubic;
DenominatorExtremeXMinusOneValuation.


DUPLICATE_OF:
NONE.


SUPERSEDES:
Only the use of the first mod-p collision from M3-T11-043 as the sole description of the c_p=0 branch.
M3-T11-043 itself remains canonical.


DO_NOT_REPEAT:
Do not claim a fixed-power saving from naive local quadratic-residue tensorization.
Do not treat the provisional generic fixed-x Dujella replay as audited theorem credit.
Do not discard x=-1/8: its local Legendre condition is automatic at every fresh split prime.
Do not merge the two singular fixed-x carriers into the generic elliptic family.


PROMOTION_CONDITION:
Independent hostile audit of the fixed-x cubic torsion/pushforward/height adapter before setting M3_T11_FIXED_X_GENERIC_BO1_PROVED=true.
The singular carriers require separate same-measure counting arguments.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 52.


FLAGS:
M3_T11_FULL_S_DENOMINATOR_LEGENDRE_X=true
M3_T11_CP0_FULL_MODULUS_LEGENDRE_CRT=true
M3_T11_CP0_RESIDUAL_VALUATION_EQUALS_X_MINUS_ONE_TRUNCATED=true
M3_T11_FIXED_X_GENERIC_ELLIPTIC_CUBIC=true
M3_T11_FIXED_X_GENERIC_3TORSION_OVER_QSQRTM3=true
M3_T11_FIXED_X_GENERIC_BO1_PROVED=false
M3_T11_X_MINUS_ONE_EIGHTH_EXCEPTIONAL_CONIC=true
M3_T11_X_27_OVER_40_EXCEPTIONAL_CONIC=true
M3_T11_CP0_LOCAL_TENSORIZATION_FIXED_POWER=false
M3_T11_DENOMINATOR_EXTREME_SUPPORT_DEFICIT_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
CURRENT_SUPPORTING_ATTACK=FullSDenominatorLegendreXSupportOneTwelfth|InteriorCharacterGlobalDispersion
NEXT_AUDIT_TARGET=M3-T11-045-fixed-x-cubic-torsion-height
NEXT_ATTACK=GenericXMovingSupportDispersion|XMinusOneEighthExceptionalCarrier|X27Over40ExceptionalCarrier|InteriorCharacterGlobalDispersion


---
