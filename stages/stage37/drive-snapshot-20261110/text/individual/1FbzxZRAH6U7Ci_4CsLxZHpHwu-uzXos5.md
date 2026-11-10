# M3-T11-086 — Triple-spin sigma dual-conductor root line

CARD_ID: M3-T11-086
CANONICAL_CARD_KEY: M3-T11-086
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-086
現行一覧の状態: PROVED_EXACT / HOSTILE_AUDIT_PASS / SAME_MEASURE_DUAL_CONDUCTOR_ROOTLINE / SUPPORT_REDUCTION / TOTAL_POWER_SAVING_OPEN
種別: EXACT_STRUCTURE / SAME_MEASURE_DUAL_CONDUCTOR_ROOTLINE / SUPPORT_REDUCTION
要点: x=-1/8: the triple-spin square root sigma carries the relative fresh conductor in its denominator and the all-same fresh core as one Gaussian numerator root line, sharpening the large-D_fr square-divisor branch to one rational coordinate.
主張の抜粋: Write sigma=A_sigma/B_sigma reduced with sigma^2=|A|^2-1. From conj(A)*U=-1+epsilon*i*sigma, p^a||tau_0^sharp gives A_sigma==rho_0*B_sigma mod p^(2a), hence (tau_0^sharp)^2|A_sigma^2+B_sigma^2. Section-37 valuations give v_p(sigma)=-2a for p^a||m_i, so the fresh part of Den(sigma) is exactly M_rel^2. Thus (A_sigma,B_sigma) lies in one lattice B_sigma==0 mod M_rel^2, A_sigma==rho_0*B_sigma mod (tau_0^sharp)^2 of exact index M_rel^2*(tau_0^sharp)^2. On the 085 large-D_fr branch the selected modulus gives D_fr^2|A_sigma^2+B_sigma^2 and reduces the count to realized sigma support. No lattice-density saving is claimed.
対象・測度: Exact fixed-content/coefficient nondegenerate relative-fresh physical x=-1/8 singular carrier, exact R<=B; the sigma identities hold on the nondegenerate relative-fresh common-phase locus.
依存関係: Section 17.3/17.4; M3-T11-033 / Section 37; M3-T11-046; hostile-audit-passed M3-T11-080; M3-T11-085 for the selected large-D_fr branch.
再開条件の抜粋: Reopen if the common-phase valuation transfer, Section-37 trace valuations, M3-T11-046 support reduction, or polynomial-height adapter fails. The moving-sigma one-twelfth bound remains open.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 96.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 838965
SOURCE_END: 844493
SOURCE_SHA256: 3fd9ec90b1ffefb5de0cef3a27a23bfbcdfdca29fb747e67c36a2a18b867be63

## M3-T11-086
TITLE: Triple-spin sigma dual-conductor root line
TYPE: EXACT_STRUCTURE / SAME_MEASURE_DUAL_CONDUCTOR_ROOTLINE / SUPPORT_REDUCTION
STATUS: PROVISIONAL / HOSTILE_AUDIT_REQUIRED / TOTAL_POWER_SAVING_OPEN


CLAIM:
Let sigma in Q be the triple-spin square root
sigma^2=|A|^2-1=Lambda(s_24)*Lambda(t)*Lambda(t/s_24),
with A=r_1^2+r_2^2+r_3^2 and Section-24 variables s_24=r_2/r_1, t=r_3/r_1.


For sigma=A_sigma/B_sigma in lowest terms, the all-same fresh core and the relative fresh conductor act on this same rational coordinate in complementary ways.


First, from
conj(A)*U=-1+epsilon*i*sigma,
U=Q^2,
for every p^a||tau_0^sharp and oriented pi^a||G_0^sharp one has
pi^(2a)|(-B_sigma+epsilon*i*A_sigma),
so
(tau_0^sharp)^2|A_sigma^2+B_sigma^2
and gcd(B_sigma,tau_0^sharp)=1.


Second, M3-T11-033/Section 37 gives primewise, for every p^a||m_i,
v_p(sigma)=-2a.
Hence the fresh part of Den(sigma) is exactly M_rel^2:
v_p(B_sigma)=2*v_p(M_rel) for p|M_rel,
with gcd(A_sigma,M_rel)=1.


Therefore, for fixed oriented all-same root rho_0, the reduced pair (A_sigma,B_sigma) lies in the joint rank-two lattice
B_sigma==0 mod M_rel^2,
A_sigma==rho_0*B_sigma mod (tau_0^sharp)^2,
of exact index M_rel^2*(tau_0^sharp)^2.
On the M3-T11-085 large-D_fr branch, restricting the all-same modulus to the selected D_fr gives a lattice of exact index M_rel^2*D_fr^2 and
D_fr^2|A_sigma^2+B_sigma^2.


On x=-1/8, M3-T11-046 additionally gives one empty relative fresh core, so the M_rel^2 denominator is contributed by only two relative fresh cores. Physical polynomial height gives H(sigma)=B^O(1). Hence fixed sigma has only B^o(1) compatible squarefree D_fr labels. Together with hostile-audit-passed M3-T11-080 and B^o(1) packet-supported D_pkt choices,
# physical x=-1/8 endpoints on the large-D_fr branch
<=B^o(1)*# realized sigma.


POPULATION:
Exact fixed-content/coefficient nondegenerate relative-fresh physical x=-1/8 carrier, exact R<=B; structural sigma identities themselves hold on the nondegenerate relative-fresh common-phase locus.


HEIGHT:
Exact physical R<=B retained. sigma is a fixed-degree rational trace expression in retained Gaussian phases, so its numerator and denominator are polynomially bounded on the physical packet.


DEPENDS_ON:
Section 17.3/17.4 common-phase and triple-spin identities;
M3-T11-033 / Section 37 exact relative-fresh valuations;
M3-T11-046 x=-1/8 one-relative-fresh-core-empty structure;
hostile-audit-passed M3-T11-080 for fixed-D B^o(1);
M3-T11-085 for the selected large D_fr branch.


IMPLIES:
The live M3-T11-085 generic large Gaussian-square-divisor receiver is sharpened to the one-coordinate same-measure receiver
XMinusOneEighthDualConductorTripleSpinRootLineOneTwelfth.
A sufficient continuation is a fixed-power bound below B^(1/12) for realized sigma on that exact physical branch.


DOES_NOT_IMPLY:
No lattice-index density saving by itself.
No multiplication with previously consumed M_rel^2, determinant, or one-core root-line savings.
No total moving-D deficit.
No total x=-1/8 power saving.
No primary-gate, endpoint, or P(B)/M3(B) theorem.


NO_DOUBLE_CHARGE:
conj(A)*U=-1+epsilon*i*sigma shows the Section-28.3 all-same square-divisor is endogenous to the same common-phase equation. The sigma root line is a sharper coordinate presentation of that conductor, not a new independent probability factor. The relative and all-same congruences are packaged on one realized pair (A_sigma,B_sigma).


ALIASES:
XMinusOneEighthDualConductorTripleSpinRootLineOneTwelfth;
TripleSpinSigmaDualConductor;
SigmaRelativeDenominatorAllSameRootLine.


DUPLICATE_OF:
NONE.
Not Section 34: that identity multiplies the three corrected anti-roots and explicitly gives no G_0 root line.
Not M3-T11-035: the common-u root line carries M_rel in a different symmetric coordinate and does not encode the all-same tau_0 fresh root line.
Not M3-T11-085: 085 only routes large D_fr to a Gaussian square divisor of Num_Gauss(A); 086 places the selected all-same conductor and the relative conductor on one rational sigma coordinate.


DO_NOT_REPEAT:
Do not treat Section 34 as this result.
Do not replace the physical packet by an ambient sigma box.
Do not charge M_rel^2*D_fr^2 as a density factor before a same-measure range theorem.
Do not infer a fixed-power saving from divisor-many D_fr over fixed sigma alone.


REOPEN_CONDITION:
Failure of the common-phase valuation transfer, the exact Section-37 trace valuations, the x=-1/8 M3-T11-046 support reduction, or the polynomial-height adapter.


FIRST_MISSING_LEMMA:
XMinusOneEighthDualConductorTripleSpinRootLineOneTwelfth.


REQUIRED_OUTPUT:
Uniformly per fixed content/coefficient packet, prove
# {realized sigma on the exact x=-1/8 physical measure with D_fr>B^(1/12-eta) and the dual-conductor constraints}
<<B^(1/12-delta)
for some fixed delta>eta>0.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 96.


FLAGS:
M3_T11_TRIPLE_SPIN_SIGMA_TAU0_FRESH_ROOTLINE=PROVISIONAL
M3_T11_TRIPLE_SPIN_SIGMA_RELATIVE_FRESH_DENOMINATOR_MREL2=PROVISIONAL
M3_T11_TRIPLE_SPIN_SIGMA_DUAL_CONDUCTOR_LATTICE=PROVISIONAL
M3_T11_X_MINUS_ONE_EIGHTH_SIGMA_DFR_ROOTLINE=PROVISIONAL
M3_T11_X_MINUS_ONE_EIGHTH_ACTIVE_SIGMA_SUPPORT_DEFICIT_PROVED=false
M3_T11_X_MINUS_ONE_EIGHTH_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false


NEXT_LEGAL_ACTION=Hostile-audit M3-T11-084/085/086. In mainbatch, attack only XMinusOneEighthDualConductorTripleSpinRootLineOneTwelfth on the exact x=-1/8 physical measure.
NEXT_RESEARCH_CARD_ID=M3-T11-087.




---
