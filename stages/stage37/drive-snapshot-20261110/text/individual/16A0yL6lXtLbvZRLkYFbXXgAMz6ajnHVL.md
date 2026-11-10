# M3-T11-209 — Uniform short transverse-prime completion of the third-face mask

STATUS = PROVED_UNIFORM_DETECTOR_AND_EXACT_ENDPOINT_RECEIVER / FINITE_REPLAY_PASS / GLOBAL_COUNTING_CREDIT=0.
Current authority: Stage37 MAIN, CARD-INDEX, short RESULT-LEDGER, active ROUTE and card208. Gate OPEN; TI parked;120 retracted;147–149 frozen. No retraction. Separate-chat hostile audit covers162–185 only;186–209 not independently audited.

## 1. New result and physical measure

This card proves a uniform, height-compatible completeness bound for the external prime tests missing from208. It does not prove a bound for the number of surviving physical objects. In particular it does not claim T_2R(B,C) <= B^(1/2+o(1))/C.

Let R2(B) be the sorted primitive positive integer sphere objects e=(e1,e2,e3), sum ei²=R², R<=B, with at least two integral faces, each object counted once. An eligible label i has R²-ei² an integer square. Choose the eligible pair maximizing gcd(R,ei)gcd(R,ej), with lexicographic tie break; c_chart is this maximum. Its complementary label is the shared edge a. As in207, on full endpoints all labels are eligible and c_chart=c_max (the all-pair physical content); these remain distinct on raw objects. c_u is a different phase statistic.

Set h=gcd(R,a),D=R/h,u=a/h,epsilon=2 when a is odd and1 otherwise, and A-=(D-u)/epsilon,A+=(D+u)/epsilon. Retain208's exact facts: R odd, gcd(A-,A+)=1, A± positive, and F=R²-a²=(epsilon h)²A-A+. Third face integral iff both A± are integer squares.

M_2R(e) means A- and A+ are squares in Q_p for every prime p|2R. Factor A±=kappa± z±² with positive squarefree kappa± and integer z±. On this mask:

* kappa± are odd, kappa±≡1 mod8 and gcd(kappa-kappa+,2R)=1.
* For every odd p|R, (kappa±/p)=+1.
* kappa±<=A±<2R/(epsilon h)<=2B. The shared h need not be1.

These are exact valuation/unit consequences, not probabilistic class densities.

## 2. External analytic input, verified scope

Y.-K. Lau and J. Wu, “On the least quadratic non-residue”, HKU IMR Preprint2007-4, Theorem1, PDF page2 (printed page2), proof§2 printed pages4–6:
https://hkumath.hku.hk/~imr/IMRPreprintSeries/2007/IMR2007-4.pdf

Input contract: for every eta>0, uniformly for nonprincipal Dirichlet characters chi modulo a cubefree q>=2, the least positive integer n with chi(n) not in {0,1} satisfies n <<_eta q^(1/(4 sqrt(e))+eta). The theorem explicitly allows composite cubefree moduli. No GRH. Its general non-cubefree exponent is different and is not used here. The implied constant is not calibrated numerically in this batch.

Only this contract is imported. The following physical adapter and exact receiver are deductions for Stage37, not results stated in that paper. Prior CARD-INDEX search for Burgess yielded no card; nonresidue search located legacy common-divisor character transfer/eulerian-support cards and199's rational family, none of which supplies this209 completeness adapter.

## 3. Uniform transverse witness theorem and proof

Write delta=1/(4 sqrt(e))=0.151632664928... . For each eta>0 there is K_eta>=1 such that every raw object passing M_2R whose third face is not integral has an odd prime ell not dividing2R and a branch sigma with

ell <= K_eta kappa_sigma^(delta+eta) <= K_eta (2R/(epsilon h))^(delta+eta),
(kappa_sigma/ell)=-1, ell not dividing kappa_sigma.

Consequently A_sigma is not a square in Q_ell. This is a unit nonresidue witness; a smaller odd-valuation witness is also allowed by the exact local detector below.

Proof. A nonintegral third face means some kappa_sigma>1. Since kappa_sigma is squarefree and1 mod8, it is a positive fundamental discriminant. Thus chi(n)=(kappa_sigma/n)_K is a primitive nonprincipal real Dirichlet character of conductor q=kappa_sigma, which is squarefree and hence cubefree. Apply the input contract. For a quadratic character, chi(n) not in {0,1} means chi(n)=-1. Complete multiplicativity then gives a prime divisor ell of n with chi(ell)=-1 and ell<=n. The value at2 is+1, so ell is odd. Since chi(ell)=-1, ell does not divide the conductor. At every odd p|R the208 mask gives chi(p)=(kappa_sigma/p)=+1; hence ell cannot divide2R. Finally A_sigma=kappa_sigma z_sigma² has even ell-valuation and the same nonsquare unit class as kappa_sigma. This proves all claims. Constants depend only on eta, not on R,a,h,content,chart or the physical object. Enlarge K_eta for the finite small-conductor range if needed. End proof.

This proof survives moving composite kernels and arbitrary shared content. It does not silently replace the family by fixed R or by h=1.

## 4. Exact endpoint receiver with a short exterior sieve

For a positive integer A and odd prime ell define Q_ell(A)=1 iff v_ell(A) is even and the ell-free unit has Legendre symbol+1. At2 require even valuation and odd unit1 mod8. Testing just whether A has a root modulo ell is insufficient: A≡0 modell can hide odd valuation.

For B>=1 put L_B=K_eta(2B)^(delta+eta). Define

J_B(e)=1_{M_2R(e)} product_{ell prime,ell<=L_B,ell not dividing2R} [Q_ell(A-)Q_ell(A+)].

Then on R2(B), J_B(e)=1 iff the third face is integral. Forward: if a kernel were>1,§3 would provide a tested unit nonresidue prime and force the product0. Reverse: integer-square branches pass every local square test. Positivity supplies the real-place condition. Coprimality of A± makes square product equivalent to square branches.

Therefore for every C>=0 the distinct physical endpoint count has the exact identity

#E(B;c_max>C) = sum_{e in R2(B)} 1_{c_chart(e)>C} J_B(e).

There is no duplication or fiber weighting: the canonical pair is deterministic and every sorted primitive object contributes once. An object already having three integral faces also obeys the same identity. Using object-specific L(e)=K_eta(2R/(epsilon h))^(delta+eta) instead of L_B preserves the equivalence.

For the active C=B^(1/6+xi),0<xi<1/12, choose e.g. eta=1/200. Then alpha=delta+eta=0.156632664928...<1/6 and L_B/C ->0 as B->infinity. The comparison includes K_eta; it is not a claimed numerical cutoff for the existing finite census. This locates a complete third-face test below the content scale uniformly, unlike the208 necessary conductor-only mask.

## 5. What remains to be counted

The receiver is now complete but unsummed. To extract any saving, estimate this short-exterior-sieve sum on the same moving canonical sphere/two-face family, with primitive reconstruction, intrinsic R<=B, and all content costs retained. The prime test set excludes prime divisors of the object-dependent2R; its moduli and character values vary with the object. Two branches share D,u and the two-face equations. No multiplication of single-character fractions, independent signs, assumed equidistribution, or fixed-fiber divisor bound proves such a sum. The product contains many local tests; naively multiplying their moduli and using a residue-class main term can cost more than the height budget. No analytic estimate for this physical sum has been obtained.

T_2R itself still counts the nonendpoint survivors before exterior tests and remains OPEN. A bound for the exact J_B endpoint sum would be a different, explicitly endpoint-only route. Existing205/206/171/174 scoped sectors remain available; their gains are not multiplied. large c_u/full-S,large W,unshared conductor and fixed-q_min/low-median averaging remain OPEN. The172/175 forbidden all-C/uncapped shortcut is not reopened.

NEXT210: derive a summed correlation/square-sieve estimate for the exact J_B receiver at C=B^(1/6+xi), or a useful-cutoff T_2R bound, keeping the object-dependent excluded primes and all moving family costs. Start from209§4–5 and208 normalization; consult active ROUTE17.3–17.4/192 physical support only as needed. Do not rerun historical cards from the beginning or infer a universal cutoff17 from§6.

## 6. Finite reproducibility check (separate from theorem)

Replay input:208 verification JSON, DRIVE_ID=1uhhVhXKwiae-7sHeYw29pn7uVeCp_9iG, SHA256=3bce05e1ded1adabf70dd597de2e76ed8c0d4fdc96f604a2b5b7de239280adcd. This is the207 independently reproduced255 raw objects at R<=10^6. No new enumeration beyond that height.

The209 script independently factors A±, reconstructs the208 mask, checks kernel fundamental-discriminant/coprimality conditions, and scans exterior primes in increasing order using exact valuation/unit tests. It also finds a separate unit-nonresidue character witness for every survivor. All38 M_2R survivors are nonendpoints. Least exterior obstruction histogram:3:24,5:8,7:2,11:2,13:1,17:1. Maximum least unit witness also17.2184 local checks PASS. The value17 is solely a finite observation; K_eta is not fitted from it.

At B=10^6 all three strict thresholds3/16,5/24,11/48 have22 M_2R survivors. After exterior prime cutoffs3,5,7,11,13,17 the corresponding numbers are10,6,4,2,1,0 in each case. No asymptotic density or tail bound follows.

The c_chart=R example (3960,7616,16095),R=18241,A-=14281,A+=22201=149² fails at ell13 on the minus branch. The c_chart=R example (14784,32175,60088),R=69745,A-=54961,A+=84529 has its first obstruction at ell17: minus has odd valuation; plus has a unit nonresidue. This distinguishes full Q_ell tests from zero-accepting modular root tests and shows how the209 detector handles the quotient1 survivors of208 without assuming they vanish at2R.

SCRIPT_DRIVE_ID=1_v5rk5cEM5_Jhe2UUFx4CVMruG1QbnjR (stage37_transverse_209.py).
JSON_DRIVE_ID=10AVPFiZuAuLGV5fzmab3ErLkSMCirNGc (M3-T11-209-verification.json).
Reproduction: download208 input JSON and209 script into one directory; python stage37_transverse_209.py. Standard Python only. Output includes all38 witness records and12 threshold rows.

Adoption: this uniform detector/exact receiver is substantive new progress; global counting credit remains0 and Gate OPEN. Readback PASS: card, script and JSON downloaded from Drive and byte-compared; MAIN changes, all14 INDEX fields/chip/link and shortLEDGER history/append verified. MAIN latest209/NEXT210; INDEX row438 and208 restart synchronized; LEDGER control209/NEXT210. No independent hostile audit claimed.
