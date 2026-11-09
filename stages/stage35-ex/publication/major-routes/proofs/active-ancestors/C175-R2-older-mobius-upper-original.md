STAGE35EX-B / R2 — CONDITIONAL MULTI-PRIME TRUE PROTECTED TOP UPPER, 86% AND 82%
RUN_ID=R2-20261018-POSTC136-MULTIPRIME15-86-PRIMORIAL7-82-V1
BASE_HEAD=C35-136
OWNER_TICKET=R2_TRUE_FOURPOOL_GOOD_H_UPPER
FORMAL_AUTHORITY=V74_GOAL4AK_SECTION334
MATH_AUTHORITY=PROVISIONAL_DEPENDENT_SCOPED_THEOREM
R0_REVIEW=PENDING; R0_ACCEPTED=false; EXTERNAL_HOSTILE_AUDIT=false
BRANCH_A=USER_PAUSED; BRANCH_B=OPEN; STAGE35=OPEN; E1=UNPROVEN
ZERO_CLOSURE_CREDIT=true; NO_OWNER_STATE_MAIN_INDEX_HANDOFF_CURRENT_EDITS=true


I. FULL ORIGINAL POPULATION AND PRECISE POOL OBJECT


Assume ONE complete ORIGINAL signed physical packet, primitive positive LABELLED A²+B²=C², C odd, D=AC,H=A²+C², original E:y²=x(x−A²)(x+C²), P=(D,BD), T0=(0,0), D_n=T0+2nP, signed m=|n|≥3; strict −B²<x(D_n)<0 and y(D_n)<0; positive original rational r,s,p,q; SAME Q/Qsharp with infinite quotient; ONE odd coprime M=b_J>N=b_K>1, b=b_m=MN and ONE alpha=M/N∈(1,sqrt(C/A)); ALL FOUR S243 positive INTEGRAL roots with same c; ONE S269 primitive positive Gaussian F>G with quartic/shared units; SAME indexed Ward W_n/W_(2m); full original corrected Kummer/half/order8/orientation masks; ACTUAL S270 four disjoint GOOD, critical-H, noncritical-H TOP/PROPER factors with uncapped ordinary beta. All retained negative/HOLD entries apply; no physical packet existence or converse is asserted.


Let b_t be the positive reduced denominator from this ORIGINAL elliptic auxiliary orbit at t≥1, regardless of whether t itself is physical. OLD S268 first-entry law for each p|b_m states: h_p|m, m/h_p ODD, p∤h_p, and for every active t multiple of h_p with t/h_p odd, v_p(b_t)=β_p+v_p(t), β_p=v_p(b_(h_p))>0; b_1=1. The true four protected TOP product
   U=U_(J+) U_(J−) U_(K+) U_(K−)
counts ONLY the original exact-first-entry h_p=m GOOD plus ACTUAL critical H prime powers, once each, with full β_p. It divides the full first-entry product
   V_m=product_(h_p=m) p^β_p,
and both divide b_m. Noncritical H TOP is not treated as GOOD; PROPER sources are outside U.


II. THEOREM A — EXACT SUBSET MOBIUS TOP UPPER DIVISOR


Let S be ANY nonempty finite set of distinct ODD prime divisors of m, Q_S=prod_(q∈S)q, s=|S|. Define, using the SAME ORIGINAL auxiliary denominators,
   P_(m,S)=prod_(d|Q_S) b_(m/d)^μ(d).
Then P_(m,S) is a POSITIVE INTEGER, P_(m,S)|b_m, and
   U | V_m | P_(m,S) | b_m.                                 (A)
In particular, this uses ONE COMMON source denominator and no artificial multiplication of four separate role constraints. It applies to EVEN and ODD m and retains full ordinary beta.


Exact p-adic proof. Fix p|b_m and write h=h_p,k=m/h (ODD), T={q∈S:q|k}. Since p is present at m/d iff d|k, its exponent in P is
 sum_(d|prod T) μ(d)[β_p+v_p(m)−v_p(d)].
If T is empty, this is β_p+v_p(m), exactly its exponent in b_m. If T consists of ONE prime q, this is 1 when q=p, else 0. If |T|≥2, both Möbius sums vanish and it is 0. Every case is a nonnegative integer no larger than v_p(b_m). When h=m, k=1 and p∤h=m implies v_p(m)=0, so its exponent in P is EXACTLY β_p. No prime outside b_m can occur in P, by the same first-entry law. Therefore P divides b_m and contains V_m, proving (A). This is an exact partial Möbius filter, not a new EDS first-entry theorem. The previously accepted full-radical correction and odd-index case are OLD.


For S={3,5} and 15|m:
   P_(m,{3,5}) = b_m*b_(m/15)/(b_(m/3)*b_(m/5))
is an INTEGER dividing b_m, and U divides P. This is NOT an informal quotient of unrelated denominators.


III. THEOREM B — QUANTITATIVE ALL-BASE UPPER


Let k=bit_length(C)≥3, c_E=bit_length(256D^8H^4), h=hat h_E(P)>0. Retain OLD S252/S316:
   4t²h−log C−c_E/6 ≤ log b_t ≤ 4t²h+c_E/6,
   c_E≤24k+12,
   if k≤113 then h>2^(−205663),
   if k≥114 then h≥55k/1024.
Put θ_S=prod_(q∈S)(1−q^(−2)). Apply the upper height bound to μ(d)=+1 and the lower height bound to μ(d)=−1, on the SAME b_(m/d). There are 2^(s−1) terms of each sign. Hence
   log U ≤ log P_(m,S)
      ≤ 4m²h θ_S + 2^(s−1)log C + 2^s c_E/6.         (B1)
Together with the LOWER for log b_m, a sufficient STRICT all-base criterion for log U < a log b_m (rational a>θ_S) is
   4m²h(a−θ_S) >
   (2^(s−1)+a)log C +(2^s+a)c_E/6.                  (B2)
As log C<k and c_E/6≤4k+2, it is sufficient to verify the all-rational condition
   4m²h(a−θ_S) >
   [9*2^(s−1)+5a] k +2^(s+1)+2a.                   (B3)
These are UPPER bounds on actual four protected TOP pools, not estimates for synthetic pool labels or for all GOOD PROPER factors.


III.a. S={3,5}, 15|m, a=43/50=86/100:
  θ_S=(8/9)*(24/25)=64/75;
  a−θ_S=1/150;
  (B3) becomes (2/75)m²h >(223/10)k+243/25.
For k≤113 and m≥2^102840, m²h>2^(205680−205663)=2^17, so LHS > (2/75)*2^17; this exceeds RHS at k=113, exactly 28969/30 margin. For k≥114, m≥4096 gives the stronger slope comparison:
 (2/75)*(55/1024)*4096² >
  (223/10)+(243/25)/114;
 the exact positive margin is 34210661/1425. Therefore on EVERY complete signed original packet with 15|m and m≥2^102840:
  U < b_m^(43/50) = b_m^0.86.                       (B86)
Consequently the FOUR TRUE GOOD TOP subproduct G also obeys this upper, since G|U. It does NOT bound GOOD PROPER+TOP.


III.b. S={3,5,7,11,13,17,19}, Q_S=4,849,845, s=7, a=41/50=82/100:
  θ_S=12230590464/14933966047 (≈0.818978054825),
  a−θ_S=763084727/746698302350 (>0).
  RHS(B3)=(5801/10)k+6441/25.
For k≤113 and m≥2^102844, m²h>2^25; exact margin in (B3) at k=113 is
  53280074551987247/746698302350 >0.
For k≥114 and m≥4096, the slope margin, left minus RHS/k using k≥114, is
  105258018791837/33940831925 >0.
Therefore on EVERY complete original signed packet with 4,849,845|m and m≥2^102844:
  U < b_m^(41/50) = b_m^0.82.                       (B82)
In both regimes, NO packet was constructed; even/moving-base, all original masks, exceptional H, and full beta are preserved as assumptions, not bypassed.


IV. PRECISE GAPS, RELATED METHODS, ANTI-LOOP


With OLD R0 C35-136 accepted conditional ALL-INDEX 80% LOWER, on the common high-index subdomain m≥2^205678 and 4,849,845|m, one has the strict compatible interval
  0.80 < log U/log b_m < 0.82.
For 15|m under the same high range:
  0.80 < log U/log b_m < 0.86.
This is NOT a contradiction, because both inequalities can hold. The proven upper only concerns protected TOP, and cannot be interchanged with GOOD-only if critical H is present or with GOOD TOP+PROPER. Fixed-base H cutoffs do not become moving-base-uniform. Small indices, indices not divisible by the specified primes, and every unbounded base remain unresolved.


The asymptotic coefficients θ_S>8/pi²>0.80 are compatible with the old ODD-index Möbius θ result. Hence this particular subset-Möbius/height mechanism alone cannot furnish a <75% bound; proving a genuinely incompatible bound requires NEW global S243/S269/W/Q same-source arithmetic, not selecting more primes. This is a METHOD LIMIT, not a theorem of physical packet existence or nonexistence.


ALREADY OLD / ZERO METHOD CREDIT:
S252 original heights; S268 complete original entry law; S270 actual four protected TOP pools; S271 pure dyadic exact-top saturation; S316 all-base canonical-height floor; S317 odd-rough TOP near-quarter balance; R2-20261012 odd full-Möbius; R2 q-power; R2-20261013 LP relaxation no-go; R2 C35-135 3|m 89% TOP upper; C35-136 R0 80% lower; S269/S275 Gaussian/branch identities. No claim of worldwide originality. Dedup: fresh Drive title/content scans for 15|m 86, 64/75 TOP, multi-prime 82, primorial7 TOP, MAIN/INDEX/CURRENT search (86%,86/100,43/50,64/75,82%,82/100 and 7-prime) found no identical explicit all-base numerically effective two-tier TOP UPPER. R0 may classify as EQUIVALENT_OLD / dependent corollary.


REPLAY: local standalone exact Fraction/Python3 program r2_c136_multiprime_upper_verify.py, expected r2_c136_multiprime_upper_evidence.json. 480 synthetic prime-entry controls, 8 ACTUAL original auxiliary elliptic-orbit b_m controls at primitive labelled bases (3,4,5),(5,12,13),(8,15,17),(12,5,13), each m=15,30; both threshold margins EXACT positive. Finite tests do NOT prove old input laws or yield full physical packets. SOURCE_SHA256=8d396e61e54a504d6a55501c825a5029fbb7eac916aaa28d04c9d811cb4d2090; EVIDENCE_SHA256=79e10ce918da9c7f390750a1b3d5fd007a79d8afe7c8ab0393314e83a947e3ac; EVIDENCE_CANONICAL_SHA256=b0844a4fcba4c51540e748cc7ca5e663e3f0395407d6b25f4107b4943ab7c9d1.


R0_REQUEST: independently replay source and original b_m incidence, verify subset-Möbius integrality and the two exact rational threshold margins, then semantic-dedup vs S268/oddMobius/R2 89 and C35-136. If retained, count DEPENDENT_SCOPED_NUMERIC_UPPER on specified divisor subdomains ONLY. No new methods, no <75%, no completion/Branch B closure, no external hostile proof audit.
PROOF_END