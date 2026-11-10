# M3-T11-128 — Exact real evaluation image versus the universal norm witness

CARD_ID: M3-T11-128
CANONICAL_CARD_KEY: M3-T11-128
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-128
現行一覧の状態: PROVED_EXACT_REAL_SIGNATURE / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS / GLOBAL_CREDIT0
種別: GENUINE_NON_NORM_REAL_EVALUATION / SCALAR_QUOTIENT_FIREWALL
要点: 4実埋め込みでは普遍norm証人gammaが実評価像に入らない。
主張の抜粋: D0>0: xi符号{--++,-+-+}; gammaと-gamma除外。2実埋め込みはscalar quotient後に除外不可。|H∞|=|T∩sigma(V)|*|ker sigma|。
対象・測度: ExactR<=B retained;718 exactSturm algebraicpackets, no physicalenumeration; per-u labels only.
依存関係: 105/106/109/123; Bruin–Stoll Section5/6;127 retainedtheta scope.
再開条件の抜粋: 129完了：global alternatepoleclass + allplace nonpolelocal persistence。次130 fullphysicallift;gamma除外保持。TIparked。
旧詳細位置: ROUTE/LEDGER128; audit 1l_WtXDu3InsPn6fwMR0cJVqyAijT43bk
旧詳細リンク: M3-T11-128.md
旧LEDGERリンク: K16-C3-M3-RESULT-LEDGER

## Retained LEDGER source 1
SOURCE_START: 1158801
SOURCE_END: 1171714
SOURCE_SHA256: ba65e01d252e9bd456fb7db2e01712f5917b8a79234c19db09bc76c2fcadfd15

# M3-T11-128 — Exact real evaluation image versus the universal norm witness


STATUS=PROVED_EXACT_REAL_SIGNATURE / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS / GLOBAL_COUNTING_CREDIT0
TYPE=GENUINE_NON_NORM_LOCAL_COMPATIBILITY / NORMALIZATION_AND_SCALAR_QUOTIENT_FIREWALL
POPULATION=Audited123 irreducible-S4 rational-u complement of retained nondegenerate fixed-packet physical endpoints, one endpoint one count.
HEIGHT=Exact physical R<=B retained; no auxiliary-box replacement. Algebraic assertions hold for every reduced u=a/b, a!=0,b>0, regardless of Galois group.
DEPENDS_ON=105 necessary negative-square quartic;106 actual z=S/2;109 S4 complement;123 integral packet and universal gamma. No extra charge of105–107 local selectors.
ALIASES=S4OrderedRealEvaluationSignature; S4UniversalGammaRealExclusion; S4RealSignatureKernelAdapter.
DUPLICATE_OF=NONE. Targeted canonical ledger/route search found123 retains archimedean signs but does not compute their evaluation image or gamma obstruction.
SUPERSEDES=No theorem. Refines123's explicit warning that its coarse norm fiber is not a locally compatible descent set.


## 1. Exact coordinates and the curve being tested
Use123's N=a²+b², D0=2b²-25a²,
F(X)=N X⁴-8abX³+(11a²-b²)X²+6abX-a²,
theta_root=theta, alpha=Ntheta,
G(X)=N³F(X/N), beta=Nm-nalpha, gamma=alpha(aN-balpha), xi=beta/gamma.
The ACTUAL physical z=S/2=m/n is reduced with n>0. Restore
[z-theta]=[Nn beta]=[Nn gamma xi].
Nn is positive at infinity. Thus beta and the original evaluation have identical real signs; beta cannot be confused with the original class at finite places.


The necessary residual curve is C_u: w²=-F(z)/N, with w!=0. This squarefree quartic defines a genus1 curve after smooth completion, not the full genus2 physical cover. Physical points project to it by105. We compute only its non-root affine real evaluation image and the induced necessary physical condition; we neither identify its fake Selmer set with the full physical cover nor prove a lifting converse.


## 2. Exact root ordering, without numerical precision assumptions
disc(F)=16a²N²D0³, F(0)=-a²<0, F(a/b)=a²(a²+2b²)²/b⁴>0. D0 cannot vanish for nonzero rational u.
F has at least two real roots since its leading coefficient is positive and F(0)<0. A separable real quartic with positive discriminant has zero or four real roots, and one with negative discriminant has two. Consequently:
D0>0: four real embeddings; D0<0: two real embeddings and one complex pair.


For a>0, Descartes applied to F(-X) gives exactly one negative root: its coefficient signs are +,+,(either sign),-,-, with one variation. In the four-real case the other three roots are positive. Write r1<r2<r3<r4. Since F(0)<0 and F(u)>0, either r2<u<r3 or r4<u. The second possibility contradicts Vieta:
sum r_i=8u/(1+u²)>3u, whereas r1<0 and the other three roots<u would give sum r_i<3u. Here D0>0 implies u²<2/25, so the strict inequality holds. Hence
a>0,D0>0: r1<0<r2<u<r3<r4.
a>0,D0<0: r1<0<r2<u.
For a<0 use F_{-a,b}(X)=F_{a,b}(-X) and reflect the ordered roots:
a<0,D0>0: r1<r2<u<r3<0<r4.
a<0,D0<0: u<r1<0<r2.
The roots of G are N*r_i, so their order agrees. Neither 0 nor u is a root.


## 3. The real evaluation image and gamma's mismatch
In increasing root order, beta_i=Nn(z-r_i). For real non-root points on C_u, F(z)<0. Thus its exact sign image is
four real roots: E_inf={+---, +++-}, from z in(r1,r2) or(r3,r4);
two real roots: E_inf={+-}, from z in(r1,r2).
Every displayed vector is realized on the residual REAL curve; omitted physical packet/pole constraints can make the actual physical image smaller. These are not rational-point existence assertions.


gamma_i=N²*r_i*(a-b*r_i). It is positive precisely for roots strictly between0 andu. Therefore:


| Regime | sign(gamma) | necessary sign(xi) |
| --- | --- | --- |
| D0>0,a>0 | -+-- | {--++, -+-+} |
| D0>0,a<0 | --+- | {--++, -+-+} |
| D0<0,a>0 | -+ | {--} |
| D0<0,a<0 | +- | {++} |


In the four-real regime, BOTH gamma and -gamma miss E_inf. Thus123's universal supported norm[-1] class fails even the residual real evaluation condition, including after quotienting by rational scalars. In particular xi cannot be the identity squareclass for a physical point there. This is a genuine distinction beyond the norm condition: gamma is still a valid member of the coarse norm fiber, with Norm(gamma)=-(a²N³(a²+2b²))².


In the two-real regime, gamma fails the normalized image for a>0 but -gamma passes its REAL sign test. For a<0 gamma itself passes. Hence gamma is NOT excluded in the rational-scalar quotient in this regime. Never extend the four-real exclusion to all u or confuse failure of a representative with failure of its projective descent class. Passing this real test establishes no finite local/global compatibility.


## 4. Exact finite-packet signature adapter, retaining class groups
Let V_u be123's supported norm kernel and sigma_inf:V_u -> E_r the sign homomorphism, where E_r consists of vectors with product+1 in the r real embeddings. Complex norms are positive. Put W_u=ker(sigma_inf), and let T_u be the xi set in the table. Define ONLY the necessary real-compatible normalized packet
H_u^{-,inf}={gamma*xi:xi in V_u, sigma_inf(xi) in T_u}.
Then exactly
|H_u^{-,inf}|=|T_u intersect sigma_inf(V_u)|*|W_u|.
In particular it is at most2|W_u| for four real roots and at most|W_u| for two real roots. The set can be empty; no signature surjectivity or nonemptiness is assumed. The universal gamma construction does NOT prove this smaller packet is nonempty in the four-real regime.


For four real embeddings the ambient norm[-1] real sign set has8 vectors and E_inf has2; after quotienting by simultaneous sign reversal there are4 ambient classes and2 evaluation classes. These ambient ratios are NOT probabilities on the global packet or physical measure. sigma_inf(V_u) may be a proper subgroup; its intersection with T_u must be calculated, not replaced by a1/4 factor.
Retain123's bound
|V_u|<=2^(4+4omega(|2aND0|))*|Cl(K_u)[2]|.
No class group, actual signature image, full Selmer set or moving-u distribution is computed here. This adapter filters labels per u; it does not bound the number of occupied u. It yields NO independent counting credit or fixed power saving.


## 5. Verification and method source
Independent standard-library replay uses exact rational Sturm sequences to count all real roots and roots below0 andu for718 primitive signed packets with1<=|a|,b<=24:100 four-real,618 two-real. Complete finite sign enumeration checks gamma, E_inf, T_u, scalar-quotient inclusion/exclusion and ambient cardinalities. No floating-root arithmetic, Galois-group/class-group computation or physical endpoint enumeration is used. These separable algebraic samples support the proof; they are not claimed allS4 or physical.
Wolfram exact expansion independently returns disc(F), F(u), F'(u)=2a(2a⁴+a²b²+2b⁴)/b³ and reflection residual0. All multiplications are explicit in the retained replay; an initial unretained input token abx was corrected before using the symbolic output.
Primary method context: Bruin–Stoll, Two-cover descent on hyperelliptic curves, arXiv:0803.2052v2, Section5 (ordered real evaluation signs and scalar quotient) and Section6 (local-compatible intersection distinct from supported packets). Our increasing ordering, negative-leading residual curve and positive normalization are derived here.
https://arxiv.org/html/0803.2052v2


## 6. Continuation and firewalls
NEXT_RESEARCH_CARD_ID=M3-T11-129
CURRENT_ATTACK=S4GlobalSignatureImageAndBadPrimeCompatibility
NEXT_LEGAL_ACTION=On retained irreducible-S4 u, determine whether sigma_inf(V_u) intersects the explicit T_u and combine with genuine bad-prime evaluation conditions on original[Nn gamma xi]. Seek an exact algebraic certificate or same-R<=B moving-u obstruction, not ambient sign ratios. A full Selmer computation requires its precise curve/cover and scalar quotient. Retain Cl(K_u)[2], actual n, pole/root exclusions,105–107 no-double-charge and fixed-u036 multiplicity. Do not claim moving-u contraction from merely excluding gamma. TI remains parked; theta127 full original-r realization stays open but inactive.
DO_NOT_REPEAT=No universal norm witness=>locally compatible class; no sign parity=>ordered evaluation; no two-real normalized representative failure=>projective exclusion; no constant sign fraction=>power saving; no real point=>rational/physical point; no uncomputed signature surjectivity or class-group deletion.
REOPEN_CONDITION=New exact global signature/bad-prime image calculation or a same-physical-measure cross-u realization theorem.
AUDIT_MODE=Within-session adversarial rederivation, not external audit.
GLOBAL_COUNTING_CREDIT=0
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false


CARD_FILE_ID=1kpKI_V4ra45LC8s835Wx9RzmsYOLgBgE
AUDIT_FILE_ID=1l_WtXDu3InsPn6fwMR0cJVqyAijT43bk
VERIFICATION_SCRIPT_FILE_ID=1Utnc1T5na_nREEHZXHyhpJiriag2eogC
VERIFICATION_JSON_FILE_ID=1ETRImWk2HE5HR1J5zGnIhMJ4u7XQB_29
SYMBOLIC_REPLAY_FILE_ID=1GTOYdc62UHjEakLjI2YD-xzXI_WnYAnW


CURRENT_CONTROL_AT_PROMOTION
CURRENT AUTHORITY CONTROL — M3-T11-128 AUDITED / EXACT S4 REAL EVALUATION SIGNATURE
PRIMARY_GATE=M3-T11-GATE-001
PRIMARY_GATE_STATUS=OPEN
ACTIVE_ROUTE=K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE
ACTIVE_ROUTE_DOC_ID=1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE
ACTIVE_RESEARCH_CARD=M3-T11-128
ACTIVE_RESEARCH_CARD_FILE_ID=1kpKI_V4ra45LC8s835Wx9RzmsYOLgBgE
LATEST_RESEARCH_CARD=M3-T11-128
LATEST_AUDITED_RESEARCH_CARD=M3-T11-128
LATEST_AUDIT_FILE_ID=1l_WtXDu3InsPn6fwMR0cJVqyAijT43bk
LATEST_VERIFICATION_SCRIPT_FILE_ID=1Utnc1T5na_nREEHZXHyhpJiriag2eogC
LATEST_VERIFICATION_JSON_FILE_ID=1ETRImWk2HE5HR1J5zGnIhMJ4u7XQB_29
LATEST_SYMBOLIC_REPLAY_FILE_ID=1GTOYdc62UHjEakLjI2YD-xzXI_WnYAnW
LATEST_CARD_STATUS=PROVED_EXACT_REAL_SIGNATURE / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS / GLOBAL_COUNTING_CREDIT0
LATEST_AUDIT_MODE=WITHIN_SESSION_ADVERSARIAL_REDERIVATION_NOT_EXTERNAL
NEXT_RESEARCH_CARD_ID=M3-T11-129
CURRENT_ATTACK=S4GlobalSignatureImageAndBadPrimeCompatibility
NEXT_LEGAL_ACTION=Determine actual sigma_inf(V_u) intersection with128 T_u on retained irreducible-S4 u; combine with genuine bad-prime evaluation on original[Nn gamma xi]. Seek algebraic certificate or same-R<=B moving-u contraction. Define precise curve/cover and scalar quotient before calling a packet fullSelmer. Retain Cl(K_u)[2], actual n, pole/root exclusions,105–107 no-double-charge and036 fixed-u multiplicity. Excluding gamma alone is not occupied-u contraction.
S4_128_REAL_RESULT=D0>0 gives4realroots, evaluation{+---,+++-}, gamma(-+--)fora>0/(--+-)fora<0; xi signs{--++,-+-+}. gamma and-gamma excluded evenmodscalars.
S4_128_TWO_REAL_FIREWALL=D0<0 gives2realroots; xi{--}fora>0/{++}fora<0. gamma normalizedfailurefora>0 disappears afterrational sign quotient. No blanketgamma exclusion.
S4_128_PACKET_ADAPTER=|H_minus_infty|=|T_u intersect sigma_inf(V_u)|*|ker sigma_inf|. No surjectivity/nonemptiness/ambientprobability assumed; classgroup retained.
S4_128_RESIDUAL_CURVE=w²=-F(z)/N is necessary genus1 quartic, notfullphysicalgenus2cover; realimage notrationalorphysicalexistence.
S4_128_VERIFICATION=718 exact rationalSturm packets:100 fourreal,618 tworeal; noGalois/classgroup/physicalendpoint computation.
S4_RESTART_CARD_FILE_ID=1ZRAejZp3nVSQnKHYOVOm9wjev0WWcDWD
S4_RESTART_AUDIT_FILE_ID=1KwRZFElqPWGoTYTwDykPhKMWuo0Qy23y
S4_123_STATUS=RETAINED universalCOARSE norm[-1]fiber; refinedrealcompatiblefiber notuniformlyempty/nonemptyproved. Original[Nn beta],gamma,xi andCl(K_u)[2]retained.
THETA_127_STATUS=RETAINED scopedrelaxedglobalEpoint/componentimpostorfamily; standaloneexistencereceiverretired.
THETA_FULL_PHYSICAL_GLOBAL_R_AND_EXACT_HEIGHT_GATE=OPEN_RETAINED_NOT_NEXT_ACTIVE_ATTACK
THETA_124_126_STATUS=RETAINED scopedlabeltail,denominatorparity,splitcomponents; noneglobalcountcredit.
PHI_122_STATUS=JOINT_DENOMINATOR_SUPPORT_RECEIVER_RETIRED
T11_120_STATUS=RETRACTED_PHYSICAL_ADAPTER
BACKWARD_REAUDIT_117_119=PASS_WITH_RETAINED_SCOPE_LIMITS
STARTUP=MAIN topcontrol ->128 card/audit/replay -> targeted123 coordinates -> activeROUTE/RESULT-LEDGER/INDEX latestcontrol. Known fullhistoryneednotbereread.
PRIMARY_RECEIVER=P(B)<=B^o(1) A_1,1(B); sufficient A_1,1(B)<<B^(1/3-eta) forfixedeta>0 onexactphysicalmeasure.
TI_RESEARCH_STATUS=PARKED_BY_EXPLICIT_USER_REQUEST / RESULTS_RETAINED
TI_RESUME_POLICY=Do not automatically resume TI during ordinary stage37mainbatch.
GLOBAL_COUNTING_CREDIT=0
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
LOWER_OPERATIONAL_POINTERS=Historical and superseded by this current control; mathematical statements retain their audited scope.






CANONICAL M3-T11-129 — GLOBAL S4 POLE CLASS / AUDIT PASS
