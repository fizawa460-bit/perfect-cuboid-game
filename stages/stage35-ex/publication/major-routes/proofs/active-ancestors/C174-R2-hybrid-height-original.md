STAGE35EX-B / R2 RESEARCH CARD
RUN_ID=R2-20261022-POSTC171-S270-HYBRID-LAMBDA4-C65536-V1
LANE_ID=R2; ROUTE_ID=R2-01
BASE_SNAPSHOT=C35-171 COMPLETE
SEMANTIC_KEY=four-branch-good-h-joint-log-mass-upper
MATH_STATUS=PASS_SCOPED_DEPENDENT_HYBRID_HEIGHT_CERTIFICATE
AUTHORITY=PROVISIONAL_LANE_ONLY; PARENT_CREDIT=false; EXTERNAL_HOSTILE_AUDIT=false
RESEARCH_GOAL=R2-SOLO G2-L/M/H; these remain unproved
NEW_RESULT=UNIFORM_NEW_THRESHOLDS_FOR_CERTIFIED_LAMBDA_SELECTORS, NOT PHYSICAL_PACKET_EXCLUSION


1. EXACT CONCLUSION, AND WHAT IT DOES NOT CLAIM
Let (A,B,C) be every primitive positive LABELLED Pythagorean base, C odd, A²+B²=C², with D=AC and H=A²+C².
Keep the same original E:y²=x(x−A²)(x+C²), P=(D,BD), T0=(0,0), original signed T_n=T0+[2n]P and actual Ward reduced denominator b_m at m=|n|.
Retain strict signed x/y/chamber and original r/s/p/q, same Q/Qsharp and infinite original quotient, one pair of coprime odd M=b_J>N=b_K>1, alpha=M/N in the strict domain, four common-c positive INTEGER S243 roots, ONE global S269 primitive Gaussian F,G/quartic unit, signed W_n/W_(2m), S275 and the four TRUE S270 TOP and PROPER GOOD/actual-critical-H sources with full ordinary-beta, and all existing masks/retractions.


Define the certified S252 dyadic lower height:
 lambda_k=[3(bit_length(K_k)−1)−2 c_E]/(12·4^k)
 c_E=bit_length(256 D^8 H^4)
 K_k=max(|numerator(x([2^k]P))|, denominator(x([2^k]P))) after rational reduction.
S252 guarantees lambda_k is a lower bound for hhat(P) whenever positive; k is not claimed to be optimised.
Choose lambda*(A,B,C)=lambda_4 for C<2^16, otherwise lambda_3. (The new calibration uses 16P on small bases and the existing C157/C171 8P universal estimate for large bases.)
For the EXACT S270 quadratic definitions using this lambda*, define N4*,N1* by the largest nonnegative n with:
 (3/49)lambda* n²−beta0 n−K4<=0;
 (26/1225)lambda* n²−beta0 n−K1<=0;
 beta0=1/2+c_E/12,
 H_o=oddpart(H), c=1 if A even else 2,
 Z4=ceil(16 C^7 H_o^16/(A^3 c²)),
 K4=bit_length(Z4)/8+c_E/24, K1=bit_length(Z4)/8+13c_E/300.
THEOREM (SCOPED DEPENDENT): N4*<=582 and N1*<=1674 for EVERY primitive positive labelled base.


Consequences for ANY HYPOTHETICAL full SAME-source indexed packet: m>=583 forces all four TRUE exact TOP GOOD-or-actual-critical-H branch products >1, and m>=1675 forces U_i^100 >= b_m on each of four branches. This is a stronger sufficiently early threshold within S270, not a proof that any complete packet exists or is excluded.


2. LARGE BASE: C>=65536, exact rational analytic half
Set L=log2(C)>=16. OLD C157/C171 bounds retained without modification:
 lambda3 > L/16−41/768;
 beta0 < 2L+19/12;
 K4 < (47/8)L+79/24; K1 < (1183/200)L+497/150.
Hence the exact S270 quadratic at t is strictly greater than
 Phi4(t,L)=3/49*(L/16−41/768)*t²−(2L+19/12)*t−[(47/8)L+79/24];
 Phi1(t,L)=26/1225*(L/16−41/768)*t²−(2L+19/12)*t−[(1183/200)L+497/150].
At t=583 and L=16: Phi4=278855/12544>0, dPhi4/dL=100917/784>0.
At t=1675 and L=16: Phi1=2968209/156800>0, dPhi1/dL=1792579/4900>0.
Both quadratics are upward parabolas with negative value at zero, hence their unique positive zero lies below the first tested positive integer: N4(lambda3)<=582, N1(lambda3)<=1674 for every C>=65536.
All computations use exact rational coefficients; no floating point.


3. SMALL BASE: primitive exhaustive finite interval 5<=C<65536
All primitive positive integer right triangles (ordered label retained) arise from Euclid u>v>=1, gcd(u,v)=1, u-v odd:
 (A,B,C)=(u²−v²,2uv,u²+v²) AND (2uv,u²−v²,u²+v²).
Enumerate all u,v with u²+v²<65536. This is finite AND EXHAUSTIVE only for the small-base interval. Exactly 20856 oriented triples.
For each base calculate x(16P) twice, through full original E rational tangent/group doubling and independently by x-only recurrence
 x(2Q)=(x(Q)²+D²)²/[4 x(Q)(x(Q)−A²)(x(Q)+C²)].
Both exact rational reduced coordinates agree on all 20856 bases. Compute lambda4, cE, Ho, Z4 exact integers, and S270 N4,N1 by sign-bracketed binary search using Fraction. Each lambda4>0.
Finite maxima: N4(lambda4)<=395, N1(lambda4)<=1136; the maxima occur at ordered base (A,B,C)=(4,3,5), lambda4=755/3072, cE=65, bit_length(Z4)=100.
For (3,4,5): (N4,N1)=(364,1046); for (12,5,13): (367,1054).
The sorted entire entry array (A,B,C,N4,N1,lam_num,lam_den,xbits,ce,zbits), sort by (C,A), JSON canonical sorted keys and compact separators has SHA256:
57a76159593cb4e332406b1cce0819f447df545455d38bddef4425aa01a5b736
This exact digest matches the previous local run and the independent rerun on 2026-10-22. Replay returns 20856 entries and all assertions PASS. In particular these are not 20856 physical packets.


4. R2 SOLO TARGET SPLIT, QUANTIFIERS, AND PREDECESSORS
The same accepted residual signed even envelope starts |n|>=12. By new thresholds, a sufficient three-band goal may be restated (not proved):
G2-L* : exclude SAME-source full packets at every signed even |n|=12,14,...,582 for ALL moving primitive bases (286 distinct absolute even indices).
G2-M* : for every full source at signed even |n|=584,586,...,1674, force a genuine one-hole U_i=1 (546 distinct absolute even indices).
G2-H* : for every full source at signed even |n|>=1676 and retained signed odd n≡1(mod32), |n|>=7199, force one TRUE TOP branch U_i^100<b_m.
Any one direct global R2-A / R2-G8 source incompatibility remains an alternative to these three sufficient tasks.
Predecessors: OLD S252 exact lambda_k; S270 exact TRUE 4-source TOP H/GOOD thresholds; R5 C157 8P lower height; R2 post-C170 refined N4<=1111,N1<=3201, ACCEPTED by R0 C171. No new S252 theorem, no independent height method, no new upstream math, and no closure credit.
This changes the S270 lambda selector, not the numerical value of the prior fixed-lambda3 threshold. Do not claim previous N4 fixed-lambda3<=582 on small bases. No all-moving-base source exclusion and no TRUE TOP upper, and no independent external audit.


5. REPLAY / LOOP / NEXT / ARTIFACTS
REPLAY_SOURCE=R2-20261022-POSTC171-S270-HYBRID-LAMBDA4-EXACT-REPLAY-PY
REPLAY_DOC=https://docs.google.com/document/d/1P0loGD7wYAWV-gpz7yPTTv39IhUL4Yja4thCHOCjkCg/edit
LOCAL_REPLAYER=/mnt/data/r2_hybrid_replay.py ; LOCAL_FILE_SHA256=52580d2377153872546c232481df6b841fd75cdaa50027fc8df52498b96e842f (local execution only; not Google Doc byte hash).
REPLAY_SCOPE=Exactly 20856 primitive LABELLED Euclid bases, independent elliptic x-duplication checks per base; all rational endpoint and sign assertions passed. Existing S252/S270/C157 upstream proof not hostile re-audited here.
DEDUP=SCOPED_DEPENDENT_NEW_THRESHOLD_RECALIBRATION using lambda4 in finite small-base range; OLD R2-01 mass lower and prior lambda3 cutoffs reused. FINITE CRT/p97/G8, normalized proxy mass, capped beta, free Gaussian, independent alpha not used.
BLOCKER=No TRUE S270 all-moving-base four-TOP upper or same-source Gaussian/W/Q global contradiction proved. Count reduction does not turn 286 moving-base indices into 286 finite arithmetic cases.
REOPEN=Prove same-source moving-base inequalities or original S243/S269 integer/Gaussian incompatibility in one entire band.
NEXT=Attempt actual nonlocal root/ward/Gaussian link over LOW band, while maintaining TRUE GOOD/critical-H TOP, and seek an upper or empty-branch theorem for MID/HIGH. R0 should verify selector admissibility, independent finite enumeration/checksum, S270 boundary and credit.
STATUS=RESEARCH_ONLY; SUBMISSION_WILL_BE_SEPARATE; R0_REVIEW=PENDING; PARENT_CREDIT=false.