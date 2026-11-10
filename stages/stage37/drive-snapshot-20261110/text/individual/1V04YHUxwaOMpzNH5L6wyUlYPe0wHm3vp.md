# M3-T11-023 — Torus-trace spectral separation of the triple-spin double-lift selector

CARD_ID: M3-T11-023
CANONICAL_CARD_KEY: M3-T11-023
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-023
現行一覧の状態: PROVED_EXACT_ADAPTER / SAME_MODULUS_SECOND_MOMENT_OPEN
種別: EXACT_STRUCTURE / ANALYTIC_ADAPTER
要点: Torus-trace spectral separation of the triple-spin double-lift selector
主張の抜粋: After retaining the torus double-lift instead of eliminating it, the Section-17 endpoint equation admits an exact two-variable norm-one-torus normalization. With s=r_2/r_1, t=r_3/r_1, C=q_0^2*q_1^2/(kappa_2*kappa_3), the endpoint equation is exactly C^2*s^2*t^2 +(1+C^2)*(s^2+t^2) +2*C*s*t +1=0. Its t-discriminant is -4*(1+C^2)*(1+s^2)*(1+C^2*s^2), so every physical endpoint satisfies the rational torus-trace square selector -Lambda(C)*Lambda(s)*Lambda(C*s) in Q^2, Lambda(z)=z+z^(-1). In half-angle coordinates C=r(c), s=r(u), this becomes the exact six-factor polynomial cover W^2 = -8(c-1)(c+1)(u-1)(u+1) (cu-c-u-1)(cu+c+u-1) after removing the square denominator. For every good split auxiliary prime p==1 mod4 define phi_p(z)=chi_p(z+z^(-1)). The endpoint local detector K_p(C,s) = chi_p(-1)*phi_p(C)*phi_p(s)*phi_p(Cs) has an exact two-dimensional multiplicative Fourier expansion K_p(C,s) = sum_{rho,sigma} W_p(rho,sigma) rho(C) sigma(s) with normalized Parseval energy sum_{rho,sigma}|W_p(rho,sigma)|^2<=1. Because phi_p(-z)=phi_p(z), only even rho,sigma occur. Therefore the induced Gaussian-core characters rho^2(q_0), (rho^2 sigma^(-2))(q_1), sigma^2(q_2) all have local exponents divis
対象・測度: Exact fixed-content/coefficient Step-A-complement active-tau endpoint packets.
依存関係: M3-T11-015, M3-T11-016, M3-T11-018, M3-T11-021, M3-T11-022, Stage14-tH1/tH3/tH4/tH6 infrastructure.
再開条件の抜粋: A same-modulus three-core second-moment / quadratic-Hecke theorem preserving the fixed-content active-tau physical weights, or an exact reduction of that three-core packet to a certified existing tH same-modulus theorem.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 24.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 582098
SOURCE_END: 586738
SOURCE_SHA256: a7cfc54661566f0be21484ae8d6e043d532b924b08a463d421559d1dc4fc1f02

CARD_ID: M3-T11-023
TITLE: Torus-trace spectral separation of the triple-spin double-lift selector
TYPE: EXACT_STRUCTURE / ANALYTIC_ADAPTER
STATUS: PROVED_EXACT_ADAPTER / SAME_MODULUS_SECOND_MOMENT_OPEN
ROUTE: TrivialSplitCyclicDirectionOneThird


CLAIM:
After retaining the torus double-lift instead of eliminating it, the Section-17 endpoint equation admits an exact two-variable norm-one-torus normalization.


With
s=r_2/r_1,
t=r_3/r_1,
C=q_0^2*q_1^2/(kappa_2*kappa_3),


the endpoint equation is exactly


C^2*s^2*t^2
+(1+C^2)*(s^2+t^2)
+2*C*s*t
+1=0.


Its t-discriminant is


-4*(1+C^2)*(1+s^2)*(1+C^2*s^2),


so every physical endpoint satisfies the rational torus-trace square selector


-Lambda(C)*Lambda(s)*Lambda(C*s) in Q^2,
Lambda(z)=z+z^(-1).


In half-angle coordinates C=r(c), s=r(u), this becomes the exact six-factor polynomial cover


W^2
=
-8(c-1)(c+1)(u-1)(u+1)
(cu-c-u-1)(cu+c+u-1)


after removing the square denominator.


For every good split auxiliary prime p==1 mod4 define
phi_p(z)=chi_p(z+z^(-1)).
The endpoint local detector


K_p(C,s)
=
chi_p(-1)*phi_p(C)*phi_p(s)*phi_p(Cs)


has an exact two-dimensional multiplicative Fourier expansion


K_p(C,s)
=
sum_{rho,sigma}
W_p(rho,sigma) rho(C) sigma(s)


with normalized Parseval energy


sum_{rho,sigma}|W_p(rho,sigma)|^2<=1.


Because phi_p(-z)=phi_p(z), only even rho,sigma occur. Therefore the induced Gaussian-core characters


rho^2(q_0),
(rho^2 sigma^(-2))(q_1),
sigma^2(q_2)


all have local exponents divisible by 4 and are mu4-trivial in the Stage14-tH1/tH3 normalization.


Moreover


rho(C)sigma(s)
=
fixed_packet_phase
*rho^2(q_0)
*(rho^2 sigma^(-2))(q_1)
*sigma^2(q_2),


so the transformed selector has exact corewise coefficient separation at one shared oriented auxiliary Gaussian prime modulus.


POPULATION:
Exact fixed-content/coefficient Step-A-complement active-tau endpoint packets.


HEIGHT:
Exact physical R<=B remains required.


DEPENDS_ON:
M3-T11-015,
M3-T11-016,
M3-T11-018,
M3-T11-021,
M3-T11-022,
Stage14-tH1/tH3/tH4/tH6 infrastructure.


IMPLIES:
The raw SR-STR-161 one-variable separation failure does not survive multiplicative torus Fourier transform.
The correct analytic receiver is now a same-modulus three-core Hecke/dispersion second moment with bounded local spectral L2 energy and mu4-trivial core characters.


ALIASES:
CyclicTorusTraceSpectralSeparation;
TorusTraceAutocorrelationHeckeAdapter;
CyclicTorusTraceSharedModulusThreeCoreSecondMomentOneTwelfth.


DUPLICATE_OF:
Not M3-T11-021: that card concerns the raw six-bilinear selector before multiplicative torus Fourier transform.
Not M3-T11-020: no determinant/Jacobian saving is used.
Structurally adjacent to SR-STR-165 and tH3/tH4, but on a new three-core M3 charged measure.


DO_NOT_REPEAT:
Do not call this a power saving.
Do not tensorize the shared auxiliary modulus into three independent moduli.
Do not replace the exact active-tau physical measure by the complete finite torus.
Do not count the zero/bad-prime states as accepted local detector values.
Do not recharge the Section-21 determinant.
Do not assume the G_3 projection is free until its B^o(1) reconstruction is explicitly attached to the analytic block.


REOPEN_CONDITION:
A same-modulus three-core second-moment / quadratic-Hecke theorem preserving the fixed-content active-tau physical weights, or an exact reduction of that three-core packet to a certified existing tH same-modulus theorem.


NEW_GATE:
CyclicTorusTraceSharedModulusThreeCoreSecondMomentOneTwelfth.


REQUIRED_OUTPUT:
Uniformly for each fixed content/coefficient packet, enough same-measure saving after tH4/tH6 exponent audit to imply


# active tau << B^(1/12-delta)


for some fixed delta>0.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 24.


P_OVER_M3_LIMIT_PROVED=false


ADDENDUM_TO_M3-T11-023:
The three-core pushforward is O(1), not merely B^o(1).


Fixing exact primary G_0,G_1,G_2 fixes r_1,C,s. The exact normalized endpoint equation is quadratic in t=r_3/r_1, hence gives at most two t-values. Each fixes r_3, then q_3^2=r_3/kappa_3 has bounded torus square roots, and primitive q_3 reconstructs G_3 up to bounded unit/conjugation choices.


Therefore


fixed (G_0,G_1,G_2, coefficient packet)
-> O(1) compatible G_3,


and the exact endpoint packet -> ordered three-core packet has O(1) multiplicity.


IMPLICATION:
The remaining M3-T11-023 obstruction is not projection multiplicity. It is the genuine same-modulus three-core residue/Hecke second moment on the original physical weights.


M3_T11_THREE_CORE_TO_G3_RECONSTRUCTION=O(1)
M3_T11_THREE_CORE_PUSHFORWARD_FIXED_POWER_LOSS=false


---
