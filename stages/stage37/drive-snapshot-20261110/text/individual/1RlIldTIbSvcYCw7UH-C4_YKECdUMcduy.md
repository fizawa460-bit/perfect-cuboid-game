# M3-T11-217 — row(B) cubefull unitary divisor and shared-tau tail localization

STATUS: PROVED_ROW_B_CUBEFULL_UNITARY_DIVISOR / PROVED_SCOPED_SHARED_TAU_B_TAIL / HIDDEN_AND_FRESH_S_OCCUPANCY_OPEN. Gate OPEN; global counting credit 0. No retraction. Independent audit186–217 NOT RUN; separate162–185 audit unchanged.

## Authority and scope

Fresh Drive MAIN, short LEDGER, INDEX latest216/NEXT217 are current authority. They supersede this session's older213 state. Read216,203,186,183 and targeted active CROSS-GCD route; do not restart graph-character iteration retired by215. Only the exact finite nonzero-u primitive positive endpoint population of183/186 is counted, with all intrinsic R<=B, content, orientation, cyclic and four-square masks. c=c_u is NOT raw c_chart or c_max.

Dependencies:216 native1b66rF2gK-40peHVDukj6apPG_cexOI6-CmiWdLAdIKc;203 native1VW2ya-fuknvwzGls_7q5tx7BUZpd02el83m3PIINWH4;186 markdown18OiB75lUTZzAWsW_SxDaAMCiZ6dL_V94;183 native156OI672uaTABWO1UaogndaieH8kYIUL7LFizZATcqGg. Their exact contracts are restated below so continuation does not depend on chat. Index search for cubefull found no existing registered receiver before this card.

## 1. Retained contracts; new subbranch

216 gives H=H_Q H_S, tau=tau_Q tau_S, both splits unitary, and

    c=tau_S H_Q² tau_Q³,
    D_S=H_S tau_S, q_phase=H_Q tau_Q,
    gcd(c,D_S)=tau_S,
    gcd(H_S,H_Q)=gcd(tau_S,tau_Q)=gcd(H_S,tau_Q)=1.

203 gives H_Q=gcd(H,|N_T|)=gcd(H,q_phase), a unitary divisor of H. The three content rows for alpha=v_p(H)>0,beta=v_p(tau)>0 are:

| Row | v_p(H_Q) | v_p(H_S) | v_p(tau_Q) | v_p(tau_S) | v_p(N_T) |
|---|---:|---:|---:|---:|---:|
| A | alpha | 0 | beta | 0 | >=2(alpha+beta) |
| B | alpha | 0 | 0 | beta | 2alpha |
| C | 0 | alpha | 0 | beta | 0 |

Fresh S-side primes have alpha=0 and all beta in tau_S. No probabilities are assigned to rows. At beta=0 the A/B saturated collapse adds no shared tau factor.

Define three pairwise-coprime unitary factors of tau_S by its actual prime blocks:

    tau_B = product_(p|H_Q) p^v_p(tau_S),
    tau_C = product_(p|H_S) p^v_p(tau_S),
    tau_F = tau_S/(tau_B tau_C).

Then tau_S=tau_B tau_C tau_F. These are row(B), row(C), and fresh-S factors respectively. Let

    J_B=product_(p|tau_B) p^v_p(H_Q).

J_B is a unitary divisor of H_Q, not a partial-depth gcd. It is precisely the full content blocks on the shared-visible row(B) support. This split has the original physical N_T bridge: row(B) support is visible with numerator depth2alpha; row(C) support is an N_T-unit. tau_F is outside H.

## 2. Cubefull unitary divisor

Set

    P_B=J_B² tau_B.

At each prime of tau_B, alpha>=1,beta>=1, tau_Q has depth0, and c has exactly depth2alpha+beta. Consequently

    P_B || c,
    rad(P_B)=rad(tau_B)=rad(J_B),
    every p|P_B has v_p(P_B)>=3.

Thus P_B is cubefull (1 allowed). It is the ENTIRE c prime-power block on row(B) support, not merely a selected cube divisor. P_B>=tau_B; more sharply P_B>=rad(tau_B)² tau_B and P_B>=A²T if J_B>=A and tau_B>=T.

This is the new information beyond216's square-cube quotient: the S-side beta may be arbitrarily deep, but when it overlaps visible content it combines with the two visible alpha powers inside the SAME c label. It does not become a tau_Q³ divisor; those are distinct, coprime row supports. No density factors are multiplied.

The same assertion is false for all tau_S: row(C) with alpha=beta=1 has c-depth1, as does a fresh-S prime with beta=1. These are allowed retained local exponent states, not asserted global endpoints. They disprove a deduction of cubefullness from these tables alone. Extending this receiver to tau_C or tau_F requires new physical input.

## 3. Elementary cubefull reciprocal tail

Let A_3(U) count positive cubefull integers <=U. Every such integer has a canonical representation

    n=a³ b⁴ d⁵,

with b,d squarefree and coprime: at each exponent k>=3 use residue0 modulo3 in a, residue1 as4+3j in b, residue2 as5+3j in d. Dropping squarefree/coprime tests for an upper bound gives

    A_3(U)<=U^(1/3) sum_b b^(-4/3) sum_d d^(-5/3)
           <=10 U^(1/3).

The final constant uses the integral bounds zeta(4/3)<=4 and zeta(5/3)<=5/2. Dyadic summation yields, for Y>=1,

    sum_(n cubefull,n>=Y) 1/n <=40 Y^(-2/3).

Indeed each interval [2^jY,2^(j+1)Y) contributes at most10*2^(1/3)(2^jY)^(-2/3), and the geometric constant is <40. The theorem is universal; finite checks are not its proof.

## 4. New all-content same-physical endpoint tail

183 supplies a uniform global fixed-c fiber m_c(c;B)<=B^o(1) for polynomially bounded c, over ALL content packets. Count actual endpoints with c<=Z and P_B>=Y. Their c label has a cubefull divisor n>=Y. Relax unitary and physical tests only for this upper-bound label sum: for each such n, there are at most Z/n multiples up to Z. Therefore

    #E(c<=Z,P_B>=Y) <= (Z/Y^(2/3)) B^o(1).

In particular

    #E(c<=Z,tau_B>=T) <= (Z/T^(2/3)) B^o(1),
    #E(c<=Z,J_B>=A,tau_B>=T)
      <= [Z/(A²T)^(2/3)] B^o(1).

The second form uses a single lower bound on P_B, not two independent savings. There is no outer content sum, since fixed-c multiplicity is global. Any D_S or existing sector constraints may be retained as postfilters. Do not multiply this bound by216's tau_Q tail or193's T0 tail; a union/minimum with appropriate physical sectors is permitted, not independent credit.

These are threshold-specific endpoint inequalities, not a bound for every raw two-face object or the whole residual. For a fixed eta>0, the P_B-heavy sector is negligible at the retained B^(1/3) comparison scale if

    Z/Y^(2/3)<=B^(1/3-eta).

For the tau_B version this requires T>=Z^(3/2) B^(-1/2+3eta/2). No claim is made that every current dyadic cell meets this window. Since tau_B<=tau_S<=tau<=B, some large Z cells do not; record the remaining budget rather than claiming closure. A bare little-o condition is insufficient to absorb a B^o fiber; the fixed power margin is required.

## 5. Residual localization and next counted theorem

For G,T>=1, the exact tau_S split gives the deterministic cover

    {tau_S>=G}
      subset {tau_B>=T} union {tau_C tau_F>G/T}.

The first branch now has the new counted tail above. In any closing threshold window, the remaining large-shared-gcd population is localized to the genuinely hidden/fresh-S product tau_C tau_F. On row(C), full alpha+beta is in D_S, c sees only beta, and N_T is a p-unit. On fresh-S, the beta block has no content amplification. Counting a supported integer tau_C tau_F alone yields no new power saving; that is not a proposed theorem.

NEXT218: use actual primitive space triangles, original signed N_T, four-square/intrinsic-R reconstruction and171/174 sectors to bound the occupied hidden/fresh-S product, or derive a structural restriction that changes its exponent budget. Retain J_B/P_B when applying the new window; do not rediscover the depth table, identify q_phase with q_min, restart K1 conductor177–181, or double-charge193/216. large-c threshold tail, K>1 low-median averaging and215 moving-squareclass gate remain separately OPEN.

## 6. Verification and handoff

stage37_rowb_217.py and M3-T11-217-verification.json verify480 symbolic local exponent states, including saturated collapse and fresh Q/S rows. Every nontrivial P_B has depth>=3 and is the full c block on its support. They also check cubefull counts up to200000 (168 labels), five count cutoffs and six truncated reciprocal tails against the universal proved constants. PASS. These are synthetic/local and integer-label checks, not global endpoint witnesses, a hostile audit or finite evidence for asymptotic physical occupancy.

No new global saving or closure is claimed. MAIN/INDEX/short LEDGER should be latest217/NEXT218; proof occurs here once. The older213 card and both verification outputs were additionally re-fetched and byte-compared successfully this session; its historical next214 is superseded by214–216, not current authority.

Drive reproduction artifacts: SCRIPT_FILE_ID=1Iw9OoD2XvL7ZMYPmwUJ6S2fWiobYmlK8; JSON_FILE_ID=1sZhc4F5_pF7TMwLpzfYJpsxIl2iVuVJD. Both reside in the Stage37 auxiliary-artifact folder. No external library or endpoint dataset is required to run the symbolic verification. The authoritative written proof and retained dependencies, not these finite checks, establish the count.
