# R2 C184 — sparse prime-cut LCM + EXACT TRUE S270 protected TOP/PROPER gcd partition and stronger unconditional-on-index lower coefficients
RUN_ID=R2-20261024T093000Z-C184-PRIME-CUT-EXACT-TOP-GCD-V1
COMMAND=stage35ex-b; LANE_ID=R2; ROUTE_ID=R2-01 main / R2-02 original-indexed first-entry support
SEMANTIC_KEY=four-branch-good-h-joint-log-mass-upper
BASE_SNAPSHOT=C35-184 COMPLETE; PAIRED_R0_COMPLETE_RECEIPT=1S8OhCQXR3f6qk2QMNnrE_GN4GHaJpH-TyLB_YjcjDqE
MATH_STATUS=PASS_SCOPED_DEPENDENT_EXACT_SPARSE_PROPER_TOP_GCD_AND_SHARPER_LOWER_COEFFICIENT
AUTHORITY=PROVISIONAL_LANE_ONLY; parent_credit=false; external_hostile_audit=false; R0_adopted=false
NEW_INDEPENDENT_METHOD=0; NEW_ORIGINAL_SIGNED_INDEX_EXCLUSIONS=0; TRUE_S270_GOOD_H_JOINT_UPPER_BELOW_75=false; MID_ONE_HOLE=false; HIGH_ONE_BRANCH_BELOW1=false; NEW_PARENT_BARRIER=0.
PARENT=PB-R2-04 main mass open; PB-R2-05 historical dedup; PB-R2-08 correct indexed transfer.


1. Complete original source masks retained, quantifier discipline.
ONE primitive positive labelled A²+B²=C² (C odd), D=AC, H=A²+C², E:y²=x(x−A²)(x+C²), P=(D,BD),T0=(0,0), signed D_n=T0+[2n]P with m=|n|≥3 and −B²<x(D_n)<0,y(D_n)<0, original positive r/s/p/q and rational squares, SAME Q/Qsharp + infinite quotient mod E[2]+ZP. ONE coprime odd M=b_J>N=b_K>1, b_m=M N, gcd(b_m,2ABC)=1, alpha=M/N in(1,sqrt(C/A)); S243 all FOUR positive GLOBAL INTEGER common-c roots; S251/253 Kummer/half/order, S263 signed Ward W_n/W_(2m) adjacent parity, S267 corrected GOOD half and H classification, S268 actual first-entry and complete joint cofactor with ALL ordinary-beta (no truncation), S269 ONE primitive integer Gaussian F>G, exact norm/quartic/Ward leg units and SIGNED orbit; S270 four TRUE GOOD/ACTUAL critical H TOP branches and all proper/noncritical H. Older constraints and HOLD/withdrawals retained; Branch A user-paused. Weak indexed denominator tests do NOT assert a complete packet.


2. Old source results, explicit dedup.
OLD S268 §4: for every prime p|b_m, a unique first index h_p divides m, m/h_p is ODD, p∤h_p, and with beta_p=v_p(b_{h_p}), v_p(b_m)=beta_p+v_p(m). Actual H classification splits into noncritical H initial-product T_e (e=v2(m)), with T_e≤H_odd², and PROTECTED top primes: first h_p=m, p GOOD or ACTUAL CRITICAL H. Let U_all be the entire protected top product. S268 proves b_m/U_all | m T_e *product_{h=m/q, q odd divisor>=3} b_h (OLD bound, counting all proper divisors).
OLD S275 §2: four canonical square factors tilde_u_J+,tilde_u_J-,tilde_u_K+,tilde_u_K- are positive pairwise coprime integers whose product is SAME b_m; each p^v_p(b_m) sits on exactly one canonical factor. The TRUE S270 branch U_i is the protected-top p-power subproduct, NOT the canonical all-prime factor for arbitrary composite m or when noncritical H exact top occurs. OLD S318 corrects exactly this protected-vs-noncritical-H boundary at prime/dyadic m.
OLD R2 C160 all-pairs exact original-denominator gcd formula gcd(b_m,b_h)=b_g for same v2 and g=gcd(m,h); hence b_{m/ell}|b_m for any odd prime ell|m. Reusing that result and S268 first-entry is DEPENDENT; no source-exclusion credit. Bounded C184 INDEX/R2 history search for prime-cut lcm cofactor exact identity did not locate the same formula, which is NOT a claim of repository-wide absence.


3. NEW exact sparse PRIME-CUT theorem at every ORIGINAL indexed m (subject to actual first-entry interface).
Let Q_m={ell: ell is an ODD PRIME divisor of m}. Define lcm(empty)=1 and
    L_m=lcm_{ell in Q_m} b_{m/ell}.                             (3.1)
By S268/C160, b_{m/ell}|b_m and all odd quotient division preserves v2; thus L_m|b_m. Write
    R_m=gcd(b_m/L_m,m);        P_m=m L_m.                        (3.2)
Then the product of the FULL current p^v_p(b_m) of ALL proper first-entry primes h_p<m is EXACTLY
    C_prop(m)=L_m R_m = gcd(b_m,P_m).                           (3.3)
Proof: For a top p (h_p=m), p∤m and p∤b_{m/ell}, hence p∤P_m. For proper p, q=m/h_p is odd>1. Choose any odd prime ell|q: h_p|m/ell and v_p(b_{m/ell})=beta_p+v_p(m)-1_{ell=p}. This reaches v_p(b_m) if ell≠p; if all ell|q equal p, then L_m has p-adic valuation v_p(b_m)-1, while multiplication by m restores the missing one power. Thus every proper p appears in gcd(b_m,P_m) to exactly v_p(b_m), no top p appears. This is an EQUALITY, unlike the general OLD bound C_prop|F_m. It counts each p ONCE, irrespective of multiple proper indices, and counts the full uncapped beta and any index extra.


4. NEW squarefree correction and four-branch exact formula.
From the proof above, for each p|b_m/L_m with p|m, v_p(b_m/L_m) is either0 or1. Hence
    R_m is squarefree, R_m | rad_odd(m).                         (4.1)
The nontrivial correction p occurs only when m/h_p is a pure positive p-power. All other proper prime powers are already fully present in L_m. This is stronger than just R_m|m.
The all-first-entry-top factor (GOOD/critical H/noncritical H) is
    V_m=b_m/(L_m R_m).                                          (4.2)
Let H_nc(m)=gcd(V_m,T_e). Since T_e contains the FULL p^beta of exactly the NONCRITICAL H initial primes and every genuine top p satisfies p∤m, this is EXACTLY the noncritical H top part (with no critical beta cap). Therefore the TRUE protected S270 combined TOP product is
    U_all=V_m/H_nc(m)
         = b_m / [gcd(b_m,P_m)*gcd(b_m/gcd(b_m,P_m),T_e)]
         = b_m / gcd(b_m,P_m T_e).                              (4.3)
The final equality is an elementary gcd identity for all integers b,P,T.
Now use OLD S275 canonical all-prime factors z_i=tilde_u_i, i=J+,J-,K+,K-. For EACH EXACT true S270 protected branch,
    q_i=gcd(z_i,P_m),
    v_i=z_i/q_i,
    h_i=gcd(v_i,T_e),
    U_i=v_i/h_i=z_i/gcd(z_i,P_m T_e).                           (4.4)
Thus all four TRUE GOOD/ACTUAL critical H TOP pools, and all proper/noncritical-H cofactors, are extracted from a SINGLE original indexed b_m with gcd/lcm and the four S275 canonical factors, with ZERO factorization of the large denominator into primes. The original S243/269 complete-source masks are STILL mandatory to assert these z_i belong to an actual packet; no converse from formal lcm values.


5. Novel main-route quantitative consequence: improved full S270/S268 lower-growth coefficients (NOT an upper).
OLD S268 used F_old=m T_e product over ALL h=m/q for q any odd divisor >=3, with S_m=sum_{odd q|m,q>=3}q^-2<23/98 and nu_m<=m/2. The new sparse divisor
    F_sparse=m T_e L_m
satisfies b_m/U_all | F_sparse EXACTLY. Therefore
    log F_sparse <=log m+log T_e+sum_{ell|m,ell odd prime}log b_{m/ell}.   (5.1)
Let S_m^prime=sum_{ell|m,ell odd prime} 1/ell² and omega_m=#Q_m. S252 exact heights give
    log b_{m/ell}<=4(m/ell)² hhat(P)+c_E/6.
For every m>=3, omega_m<=m/3 and log m<=m/2. A rigorously certified uniform series bound is
    sum_{ell>=3 prime} ell^-2
    <= sum_{3<=ell<=127 prime}ell^-2 + 1/129²+1/258 < 41/200. (5.2)
The displayed finite sum is EXACT rational; the tail bounds all odd integers 129+2j by their first term and an elementary positive decreasing integral. The CODE/EVIDENCE verifies this exact strict inequality. Consequently
    1-4 S_m^prime >9/50, and beta_new=1/2+c_E/18.             (5.3)
Replace ONLY the old S_m,nu_m bounds by S_m^prime,omega_m in the exact old S270 algebra; the SAME four TRUE protected branch logs then satisfy its old (269.7) formula with the smaller losses:
    log U_i >=(1-4 S_m^prime)m² hhat(P)-log m-log T_e
            -(1/8)log(16 C^7/(A³ c²))-omega_m*c_E/6-c_E/24.  (5.4)
Let lambda>0 be old S252 exact positive rational lambda<=hhat(P) and Z4=ceil(16C^7 H_odd^16/(A³ c²)) OLD, K4=bit_length(Z4)/8+c_E/24 OLD. Define N4_sparse as largest N>=0 with
    (9/50)lambda*N²-(1/2+c_E/18)*N-K4<=0.                  (5.5)
THEN every COMPLETE original packet m>N4_sparse has all FOUR protected TOP branches nonempty (not a statement of full-packet existence).
At 1% mass per branch, subtract 0.01log b from (5.4), with old log b<=4m²hhat(P)+c_E/6. The leading coefficient is (9/50)-(1/25)=7/50, K1=bit_length(Z4)/8+13 c_E/300 OLD. Define N1_sparse via
    (7/50)lambda*N²-(1/2+c_E/18)*N-K1<=0.                  (5.6)
Then every COMPLETE original packet m>N1_sparse satisfies U_i^100>=b_m for EACH protected branch.
Identically S268's joint75% and per-role50% thresholds replace OLD a=(3/49)lambda,beta0=1/2+c_E/12 by a_sparse=(9/50)lambda,beta_new above and KEEP their original K75,K50 and H caps unchanged. The joint75% bound is a LOWER necessity, not the user's targeted TRUE FOURPOOL <75% UPPER.


6. EXACT calibration and proof/cycle boundaries.
At already-historically-excluded base(8,15,17): c=1,H_odd=353,c_E=99, old exact lambda=63/256. SAME OLD S270 constant definitions yield:
 OLD N4=583 -> SPARSE N4=139;
 OLD N1=1677 -> SPARSE N1=178;
 OLD S268 joint N75=N50=583 -> SPARSE N75=N50=139.
These are merely threshold certificates on a previously excluded base, NOT new signed-index exclusions or an improvement in R0 global hybrid worst-case without its own all-base check. No true GOOD/H joint75% UPPER, MID one-hole, HIGH one-branch<1% contradiction, new generic source emptiness or external hostile audit is claimed. The exact extracted factor U_i equals old S270 U_i: this is a NEW factor-free/formula/constant optimization, not an independent theorem about the source population.
;


7. Exact replay, controls, and proper source classification.
Full locally executed standard Python3 Fraction original EC E/P plus SymPy odd-prime factor used ONLY to select index prime cuts, not to factor giant original denominator b_m:
 LOCAL_EXECUTED_SCRIPT=/mnt/data/r2_c184_sparse_top_gcd_verify.py
 SHA256=18661df830f2c3b905826917c9d3ef68cdfe20ac32a354f495f9cae1d2d4055f
 EVIDENCE_FILE=/mnt/data/r2_c184_sparse_top_gcd_evidence.json
 SHA256=dd045b3d76608322326c2c3e8947b388526380f918a454821a7f6b812f96ee2d
 Four actual ORIGINAL indexed labelled bases (3,4,5),(5,12,13),(8,15,17),(12,5,13), m=3..11, total36 rational b_m points: L_m|b_m, sparse gcd agrees with OLD full proper-index product gcd, R_m squarefree. These are WEAK original indexed points; do NOT assert complete S243 four integer root source.
 A separate ARTIFICIAL valuation control at m=30 has proper first entries at10,6,10, with (3,5,7) initial exponents (2,3,2), top p31/41/61/71 across four labelled placeholder pools, one noncritical H top p73. L_m and the index extra R_m=15 give C_prop=826875 exactly; H_nc=73 and U_all=52473732928231; mock TRUE-protected four pools 961,41,3721,357911. This is a valuation-replay only, NOT a physical packet or actual S275 four-square lift, and certifies no source existence.
 Exact rational prime reciprocal-square finite sum p≤127 plus explicit odd integer tail <41/200 PASS. Old constants/endpoint quadratic interval calculation on already excluded (8,15,17): new N4=139,N1=178,new S268 joint N75=N50=139; all endpoint inequalities verified by rational arithmetic. The calibrated numbers are conditional constants, not a new original signed-index exclusion.
 Native CODE doc is a related compact reproducible checker; the FULL locally executed source digest above is the reference; do not assert byte equality unless separately established. Native EVIDENCE JSON gives full local digest and count summary. Full remote Drive original readbacks/digests will be recorded in owner STATE and SUBMIT.
 DEDUP: OLD C160 all-pair denominator strong gcd and S268 h_p valuation already imply L_m|b_m; OLD S275 all-index canonical four factors and old S318 protected-vs-noncritical-H classification are reused; OLD S270 root linear-form capacities unchanged. The new mathematical delta is the EXACT sparsification from all proper q to distinct ODD PRIME q with SQUAREFREE extra R_m, its TRUE 4BRANCH protected TOP gcd retrieval without factoring b_m, and the improved uniform reciprocal prime height coefficient/quantitative thresholds. Independently new source constraint0, GOOD/H upper0.
 LOOP_RESULT=PASS_SCOPED_DEPENDENT_SPARSE_PRIME_CUT_EXACT_TRUE_TOP_AND_IMPROVED_LOWER. PARENT_BARRIER=PB-R2-04 only; no new parent. Do NOT add STOP-R2-## again.
 BLOCKER=No opposite actual same-index inequality forcing a TOO LARGE sparse proper gcd C_prop*H_nc or a TOO SMALL protected branch U_i; HIGH prime/dyadic m may have L_m=1 and naturally nearly all TOP. Thus this exact formula is a computable RECEIVER, not a global 75%-upper proof.
 REOPEN/NEXT=Develop a SOURCE-EXACT lower bound on gcd(b_m,mL_m) from original signed Ward, S269 unique integer Gaussian quartic/common alpha and S243 four global integer roots, large enough to violate the S268 joint75% protected-TOP lower; or derive a single MID missing U_i / HIGH true branch <1% using four gcd formulas (4.4) on original indexed m. If no actual independent lower on the gcd, park sparse refinements; avoid repeating old exact-gcd/height coefficient improvements, finite bank, norm-only or C4 reparameterization.
 SOURCE_S268=https://drive.google.com/file/d/1QFsK3SpT-L9xfAiVOeAzV-qhlAoDfw9o/view
 SOURCE_S270=https://drive.google.com/file/d/11Khz8znsWCzovBnWPDhZvsE36IBTAYRh/view
 SOURCE_S275=https://docs.google.com/document/d/1y776bvqb7AWk55bYXsyksfEm2rCXcc6gU-jA1OOJHpI/edit
 SOURCE_C160=https://docs.google.com/document/d/1PpH1_0CsLp8_KiYHdSubMaYaNTJ78mt_js7qJ_f-SPg/edit
 R0_C184_RECEIPT=https://docs.google.com/document/d/1S8OhCQXR3f6qk2QMNnrE_GN4GHaJpH-TyLB_YjcjDqE/edit
 R2_PARENT_INDEX=https://docs.google.com/spreadsheets/d/15yOybk9fj7c5jCqEttEyKNtZ_kVtikTzkTMICvorw3s/edit
 REMOTE_ARTIFACT_SHA256_AND_SUBMIT=refer to R2 owner STATE and COMMITTED receipt.