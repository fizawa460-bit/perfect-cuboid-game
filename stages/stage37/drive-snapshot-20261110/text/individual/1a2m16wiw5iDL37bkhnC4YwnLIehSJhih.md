# M3-T11-148 — Full signed quartic parameter obstruction and single-pair power firewall

CARD_ID: M3-T11-148
CANONICAL_CARD_KEY: M3-T11-148
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-148
現行一覧の状態: PROVED_FULL_SIGNED_DEGREE4_PARAMETER_OBSTRUCTION / GLOBAL_COUNTING_CREDIT=0
種別: DEGREE4_PARAMETER_OBSTRUCTION / RANK8_CIRCUIT
要点: full signed非定数次数4もzero edge。single-pair powerは全次数で排除。
主張の抜粋: 2根対の9配分square行列はrank8、一意関係に8非定数modeが必要。3座標は最大6modeなのでboundary。exact minorsを次数付き補間証明。
対象・測度: basepoint-free P1_Q parameter map・generic146open。非contained degree4は<=64endpoint。全quartic曲線の排除でない。
依存関係: 146/147/139;historical M-degree comparison未証明。
再開条件の抜粋: 148基準の次149：次数6full signed allocationまたはdirect global support。one-pair classは既排除。global credit0、gate OPEN、TI保留。
旧詳細位置: RESULT-LEDGER「M3-T11-148 — Full signed quartic parameter obstruction and single-pair power firewall」; audit 1GX_OBnelty8WC8SgSL7aecgvxGivZNJH
旧詳細リンク: https://drive.google.com/file/d/1ywVZmoeVhD5oOHYy0aPiHsu4bC-H2e7S/view
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 145330
SOURCE_END: 160095
SOURCE_SHA256: 9dad5aaaa8dc8260ccd436b56748c60eea6f696f956d58e37ad20c148587eead

CURRENT AUTHORITY CONTROL — M3-T11-148 / FULL SIGNED DEGREE4 PARAMETER OBSTRUCTION
PRIMARY_GATE=M3-T11-GATE-001
PRIMARY_GATE_STATUS=OPEN
ACTIVE_ROUTE=K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE
ACTIVE_ROUTE_DOC_ID=1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE
ACTIVE_RESEARCH_CARD=M3-T11-148
ACTIVE_RESEARCH_CARD_FILE_ID=1ywVZmoeVhD5oOHYy0aPiHsu4bC-H2e7S
LATEST_RESEARCH_CARD=M3-T11-148
LATEST_AUDITED_RESEARCH_CARD=M3-T11-148
LATEST_AUDIT_FILE_ID=1GX_OBnelty8WC8SgSL7aecgvxGivZNJH
LATEST_VERIFICATION_SCRIPT_FILE_ID=19iqRFK-l8iSFx_FCLSeOgbHL6XepPj7d
LATEST_VERIFICATION_JSON_FILE_ID=1jc4CazXssHWgUjS7aaBFPGTx3yRcxJ3q
LATEST_CARD_STATUS=PROVED_FULL_SIGNED_DEGREE4_PARAMETER_OBSTRUCTION / WITHIN_SESSION_EXACT_ALGEBRA_PASS_WITH_SCOPE_LIMITS / GLOBAL_COUNTING_CREDIT0
LATEST_AUDIT_MODE=WITHIN_SESSION_EXACT_ALGEBRA_CERTIFICATE_NOT_EXTERNAL
NEXT_RESEARCH_CARD_ID=M3-T11-149
CURRENT_ATTACK=DegreeSixFullSignedAllocationOrDirectSupportEstimate
PHYSICAL_148_SCOPE=Common homogeneous basepoint-free P1_Q parameter degree in138/139 plusprojection; NOT arbitrary geometric curve degree/genus/historical Mdegree.146 genericopen supplies degreepreserving signedpolynomiallift;147 Rhasnorealzeros.
PHYSICAL_148_SINGLEPAIR=R=Q^n definitequadratic,ALLn: Hi/R=ci z^ki,|ci|1; sphereLaurentconstant m/2+sumfixed ai²=1 excludesm1/3; m2 frequenciesmatch andfixededge0;m0 constant/commonfactor. Every nonconstant singleconjugatepairpower lift haszeroedge.
PHYSICAL_148_TWO_PAIRS=Normalize realroots toi,ki,k>0,k!=1;R=(t²+1)(t²+k²). Exhaustive9 Hi=ci H_ab,a/b=-1,0,1;H_ab=(t-i)^(1+a)(t+i)^(1-a)(t-ki)^(1+b)(t+ki)^(1-b),|ci|1.
PHYSICAL_148_CIRCUIT=9squaresC_ab have rank8,one relation: w00=4(k⁴-10k²+1);axial=-2(k²-1)²;same-sign=(k-1)⁴;opposite-sign=(k+1)⁴. ALL8offcenterweightsnonzero;center mayvanishandisnotassumednonzero.
PHYSICAL_148_RANK=Odd4x4minor=-32768k^6(k²-1)²;even4x4minor=-2048k³(k²-1)³. Disjointparity givesrank>=8;relationgives<=8.17exactnodes+degree<=16 certifydeterminantpolynomialidentities;kerneldegree<=8 certifiedexactly.
PHYSICAL_148_SPARSE=Sphereidentity sum(ci² Cmode+conjci² Coppositemode)+2C00=0 has<=6offcentermodes;nonzerocircuitneeds8,so coefficientvectorZERO.2rotatingcoordinatesmustsameoppositepairandfixedci=+/-i=>edge0;3rotatingcenter2fails;1fails;0constant. Bothsquarefreeandrepeatquarticphysicallyexcluded.
PHYSICAL_148_DEPENDENCE=z=(t-i)/(t+i),w=(t-ki)/(t+ki) AREdependent;rankcircuitaccountsforit. DoNOTtreatasindependentLaurentvariables.
PHYSICAL_148_RECEIVER=Contained genericopen degree4 P1_Q map hasNOpositive3edgeendpoint. Noncontaineddegree4pullbackPdegree64=>atmost64eligibleendpoints via146uniqueinverse,includinginfinity. No globalcurvecovercost.
PHYSICAL_148_NEXT_DEGREE=147odd/degree2 plus148degree4 leavesfirstpossiblecontainednonconstantP1_Qparameterdegree6; existenceNOTproved. Positivegenus/ellipticcubics/nonsplitnormalization/isolatedsingularQpoints/constantperfectcuboidsNOTexcluded.
PHYSICAL_148_DEDUPE=Historical Stage19M4/oddMabsence alreadyretained;no newcreditforrediscovery,no degreecomparisonproved;Stage20SaundersonM6retained;Stage19M6absenceNOTproved.
PHYSICAL_148_VERIFICATION=17exactinterpolationnodes/153kernelcoefficientchecks/729allocationsupportpatterns/6singlepairboundarypowers PASS. Thisisdegreeboundedpolynomialidentitycertificate,NOTcensus extrapolation;withinsessionNOTexternal.
NEXT_LEGAL_ACTION=Read148card/audit/script/json. Degree6fullsignedallocations overone/two/threeconjugatepairs andmultiplicities (singlepairalreadyexcludedALLdegrees),or directglobaleligible-supportbound. DoNOTextendquarticrankcircuitto3pairswithoutproof orpromoteuncostedcurvecover.
GLOBAL_COUNTING_CREDIT=0
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
TI_RESEARCH_STATUS=PARKED_BY_EXPLICIT_USER_REQUEST / RESULTS_RETAINED
TI_RESUME_POLICY=Do not automatically resume TI during ordinary stage37mainbatch.
T11_120_STATUS=RETRACTED_PHYSICAL_ADAPTER
PRIOR_RESULTS=147odd/degree2/conicreceiver;146 arbitraryfield squarecollapse/uniquegradientinverse/degreepreservinglift;145 lineoccupancy16;144 unsignedlogcounts;143 unsignedfirewall;139 fullsignedeliminant;138 height allretainedwithin scopes. Originalsource/packet/coefficient/orientation/cyclic/content/canonical masks REQUIRED.
STARTUP=MAIN/INDEX current148 -> standalone148card/audit/script/json -> ROUTE/LEDGER148;147/146/139 andolderdependenciesonlyasneeded. No fullhistoryreread.
ARTIFACT_READBACK=148card/audit/script/JSON fetchedfromDrive andexactbytescompared PASS beforecontrolupdate.
LOWER_OPERATIONAL_POINTERS=Historical and superseded operationally; prior mathematics retains audited scope.


# M3-T11-148 — Full signed quartic parameter obstruction and single-pair power firewall


STATUS=PROVED_FULL_SIGNED_DEGREE4_PARAMETER_OBSTRUCTION
AUDIT_MODE=WITHIN_SESSION_EXACT_ALGEBRA_CERTIFICATE_NOT_EXTERNAL
GLOBAL_COUNTING_CREDIT=0
PRIMARY_GATE_STATUS=OPEN
TI=PARKED
NEXT=M3-T11-149 DegreeSixFullSignedAllocationOrDirectSupportEstimate


Authority: freshly read MAIN / INDEX / RESULT-LEDGER / active ROUTE all147; standalone147 card/audit read. Use146's degree-preserving unique polynomial lift on the generic138/139 open mask and147's real basepoint obstruction. Preserve original endpoint masks, retracted120 and parked TI. No full-history reread.


## 1. Scope and dedupe


The degree here is the common degree d of a homogeneous basepoint-free P1_Q parameter map into the138/139 plus coordinates [A_1:A_2:A_3:R], after common factors are removed. It is not automatically the degree of its image, genus or the historical K3 quasi-polarization M-degree. Historical M3-HIST28-GEOMETRY-FW-001 already records Stage19 physical M4 and odd-M absence, Stage20 Saunderson M6, and no proved Stage19 M6 absence. Keep those facts and do not count their rediscovery as new credit. We still have no comparison identifying M-degree with this projection parameter degree. This card supplies a direct146 receiver and exact factor-allocation certificate, rather than a new global low-degree spectrum.


We prove: a nonconstant basepoint-free degree4 real polynomial lift satisfying
 E_i^2+F_i^2=R^2, sum_i E_i^2=R^2
cannot have all three E_i strictly positive at any real parameter. In fact at least one E_i is identically zero. Thus a contained generically open degree4 P1_Q parameter map in P=0 has no eligible positive endpoints, by146. Constant positive rational lifts are NOT excluded; one would already be a perfect cuboid. Curves of positive genus, nonsplit normalization and isolated singular rational points are not covered by this theorem.


## 2. Single conjugate root pair: exclusion for every power


By147, R has no real projective zero. Suppose R is proportional to Q^n with Q a definite real quadratic. Normalize R=(L*bar(L))^n. Put H_i=E_i+iF_i. Unique factorization of H_i*bar(H_i)=R^2 gives
 H_i=c_i L^(n+k_i) bar(L)^(n-k_i), -n<=k_i<=n, |c_i|=1.
Hence H_i/R=c_i z^k_i, z=L/bar(L), and E_i/R=(c_i z^k_i+bar(c_i)z^(-k_i))/2. For k_i=0 this is a fixed real ratio a_i; otherwise the square has constant coefficient1/2. The nonconstant z makes Laurent coefficients independent. The sphere identity forces
 m/2+sum_fixed a_i^2=1,
where m is the number of nonzero k_i, and cancellation of every nonzero frequency. m=1 is impossible; m=3 has constant coefficient3/2. If m=2, their absolute frequencies must agree, their squared phases cancel, and the sole fixed a_i=0. If m=0 the image is constant and all forms share R. Thus every nonconstant single-pair-power lift has a zero edge, for ALL n. In particular the repeated-quadratic quartic case R=Q^2 is excluded physically. Boundary maps remain: take E_1+iE_2=(t-i)^(2n), E_3=0 and R=(t^2+1)^n.


## 3. Distinct pairs: real normalization and nine exhaustive allocations


The remaining real quartic with no real zero has two distinct conjugate pairs. A real projective change of parameter sends their upper half-plane roots to i and k*i, with k>0 and k!=1. For completeness: first send the first root to i by translation/scaling. For a second root p+iq, q>0, a transformation (cos(theta)z+sin(theta))/(-sin(theta)z+cos(theta)) fixes i; the numerator of its real part is p*cos(2theta)+(1-p^2-q^2)*sin(2theta)/2. Choose theta making this zero. Its denominator cannot vanish in the upper half-plane, and injectivity prevents k=1 for distinct roots. This is a real change; losing rational coefficients causes no issue for a real impossibility theorem.


Absorb a nonzero real scalar into all forms and normalize
 R=(t^2+1)(t^2+k^2).
The homogeneous statement includes infinity. For a,b in {-1,0,1}, define degree4 forms (dehomogenized below)
 H_ab=(t-i)^(1+a)(t+i)^(1-a)(t-ki)^(1+b)(t+ki)^(1-b).
Conjugation gives bar(H_ab)=H_(-a,-b), H_ab*bar(H_ab)=R^2. Every H_i=E_i+iF_i is exactly c_i H_(a_i,b_i), |c_i|=1. At each conjugate pair the exponents sum2, by H_i*bar(H_i)=R^2, so these nine allocations are exhaustive, not an ansatz. Put C_ab=H_ab^2, degree8, and C_00=R^2.


## 4. Exact rank8 circuit of the nine squared allocations


The nine C_ab have a one-dimensional relation space. Its generator has weights
 w_00=4(k^4-10k^2+1),
 w_a0=w_0b=-2(k^2-1)^2 for a,b nonzero,
 w_ab=(k-1)^4 for ab=1,
 w_ab=(k+1)^4 for ab=-1.
Then sum_(a,b) w_ab C_ab=0. Every one of the EIGHT off-center weights is nonzero for k>0,k!=1; the center weight may vanish, and we do NOT assume otherwise.


Here is a reproducible universal rank certificate, not a finite parameter census. Choose representatives (1,1),(1,0),(1,-1),(0,1). Write B_j=Im(C_rep_j) and T_j=Re(C_rep_j); these are odd and even polynomials respectively. In the odd coefficient rows t,t^3,t^5,t^7, the determinant of the four B columns is
 -32768*k^6*(k^2-1)^2.
In the even rows t^2,t^4,t^6,t^8, the determinant of columns T_1,T_2,T_3,R^2 is
 -2048*k^3*(k^2-1)^3.
Both are nonzero on the stated range. Odd and even coefficient subspaces are disjoint, so rank is at least8; the displayed relation makes it at most8. Passing between conjugate pairs and their real/imaginary parts is invertible over C. Thus the relation space is exactly one-dimensional.


verify148.py proves these determinant formulas by exact Gaussian rational arithmetic and interpolation: every matrix entry is a polynomial in k of degree<=4; a4x4 determinant has degree<=16. Its exact values at17 distinct integers determine it uniquely, and the interpolated coefficients equal the displayed polynomial coefficients. The relation coefficients have degree<=4 and C coefficients degree<=4, so their sum has degree<=8; exact zeros at17 distinct integers certify the identity coefficient by coefficient (nine coefficient rows). This is a finite certificate of polynomial identities with an explicit degree bound, not empirical extrapolation. Degenerate test nodes k=0,1 are allowed for polynomial certification; they are excluded from the rank theorem.


## 5. Sparse three-coordinate identity forces a boundary edge


Since E_i=(H_i+bar(H_i))/2 and H_i*bar(H_i)=R^2, the sphere identity is precisely
 sum_i (c_i^2 C_(a_i,b_i)+bar(c_i)^2 C_(-a_i,-b_i)) + 2 C_00 =0.
Three coordinates contribute at most SIX distinct off-center allocation modes. Consequently the resulting coefficient vector omits at least two off-center entries. By section4, any nonzero relation must have all eight off-center entries nonzero. Our coefficient vector must therefore be ZERO entry by entry.


Call (a,b)=(0,0) fixed, and group nonfixed modes into opposite pairs. A single coordinate in an opposite-pair group contributes a nonzero squared phase, so it cannot cancel. If two of the three coordinates rotate, they must lie in the SAME opposite-pair group and their squared phases cancel; the fixed coordinate c has center equation2+2 Re(c^2)=0. Since |c|=1, c=+/-i and its E is identically zero. If all three rotate, the center coefficient is2, impossible, even if all are in one group. One rotating coordinate is impossible. With zero rotating coordinates all forms are proportional to R and the projective image is constant/common-factor. This exhausts every allocation and proves the theorem. Surviving two-rotating boundary maps are algebraically valid; positivity removes them.


The two phase functions z=(t-i)/(t+i),w=(t-ki)/(t+ki) are algebraically dependent. Treating them as independent Laurent variables would be invalid. The rank8 circuit explicitly accounts for this dependence. Its center coefficient can vanish without weakening the sparse-support obstruction.


## 6. Projection receiver, counts and limits


For a degree4 basepoint-free Q parameter map contained in P=0 with generic146 open mask,146 supplies a polynomial signed lift of the same degree and no common basepoint. Sections2–5 exclude all-positive endpoints. If the open mask fails identically, it cannot contain an original eligible positive rational endpoint, by146's mask inclusion. A NONCONTAINED degree4 parameter map has a nonzero homogeneous degree64 pullback of P, so at most64 projective parameter roots and, by146 uniqueness, at most64 eligible endpoints. This includes infinity and does not assert a bound on the number/cost of such maps.


Together with147's odd-degree and degree2 obstructions, the first remaining possible nonconstant contained P1_Q parameter degree is6. Existence at degree6 is not proved, and no assertion is made about historical Stage19 M6. Smooth elliptic cubics, positive-genus quartics, rational curves whose normalization has no Q parameterization and isolated singular rational points are not silently removed. No global population estimate, exponent saving or perfect-cuboid nonexistence follows.


## 7. Replay and handoff


Self-contained verify148.py / verification148.json:17 exact interpolation nodes for both determinant polynomials;153 exact kernel coefficient checks;729 three-coordinate allocation support patterns; six exact single-pair boundary powers. The algebra certificate proves the universal rank statements with degree bounds. Boundary and constant cases are retained explicitly. Audit is within-session, not independent external review.


Next149: degree6 full signed factor allocations (one/two/three conjugate pairs and multiplicities) or a direct global eligible-support estimate. The one-pair-power class is now excluded for all degrees; do not re-enumerate it as new credit. For three pairs the mode count and rank may change: do not extend the quartic sparse circuit without proof. Preserve all original positivity/source/coefficient/orientation/cyclic/content/canonical masks, TI parked and120 retracted. GLOBAL_COUNTING_CREDIT=0; PRIMARY_GATE_STATUS=OPEN.




PRIOR AUTHORITY MATERIAL — HISTORICAL OPERATIONAL POINTERS BELOW; MATHEMATICS RETAINED WITHIN ITS AUDITED SCOPE.
