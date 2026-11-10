# M3-T11-153 — Proof and aggregate-budget audit

VERDICT=PASS_WITHIN_SESSION
REVIEW_MODE=WITHIN_SESSION_REDERIVATION_NOT_EXTERNAL_INDEPENDENT_REVIEW
PRIMARY_GATE_STATUS=OPEN
GLOBAL_COUNTING_CREDIT=0
SECTOR_COUNTING_PROGRESS=true

## Claim audited

On the original primitive canonical positive endpoint population, at exact R<=B, let N(B,Y) count the union over ALL p^n||R with m=R/p^n<=Y. The proved bound is

 N(B,Y)<=512 Y(1+log Y)^27(1+log B),  B>=2, 1<=Y<=B.

This is an aggregate theorem, not a fixed-m or fixed-p estimate. Taking Y=B^(1/3)/(1+log B)^30 yields O(B^(1/3)/(1+log B)^2)=o(M3). It leaves the balanced residual defined in the research card unbounded.

## Load-bearing checks

1. Population bridge:151 already supplies an injection from original endpoints into primitive positive integer edge/complementary-diagonal data.153 does not replace this by a curve parameter population. Every qualifying endpoint has at least two p-unit edges. All primes ofR are split and at least5.

2. Orientation: one pi above each p is chosen deterministically. Independently conjugating each H_i preserves its real edge and moves its entire p^(2n) Gaussian factor onto bar(pi). The resulting cofactor G_i has norm m^2. Units are included in the full set H(m); there is no omitted sign/orientation packet.

3. Nonzero eliminant: C=sum G_i^2 cannot vanish for a positive endpoint. For r=2 vanishing forces the third edge to zero; for r=3 it contradicts R>0. Zero witnesses must be discarded BEFORE prime enumeration. Replay confirms the zero-edge boundary(0,3,4;R=5) has C=0, so this step is not a genericity assertion.

4. Prime cost: pi^2|C implies p^2|Norm(C), not merely p|Norm(C). For fixed witness, Norm(C) is a specific nonzero integer at most9m^4. Its distinct eligible primes cost at most log(9m^4)/(2log5). We drop the orientation-specific divisibility only to enlarge the candidate set. This is a deterministic integer-divisor budget, not a probability assigned to prime splitting or phases.

5. No inverse-multiplicity gap: specifying m,I,G_i,p,n determines the p-unit edges. With r=2 the missing positive edge is uniquely determined by the sphere equation. Its two signs are not both physical. Complementary face diagonals and the original canonical endpoint follow from the retained bridge. Nonintegral or invalid data contribute zero. There is no extra R^o(1) fiber factor and no hidden family cost. Multiple encodings only overcount safely; a least qualifying p selects an injection.

6. Exponents: sum all n>=1 satisfying mp^n<=B, at cost at most logB/log5. This handles the r=2 high-valuation branch; it does not import the stronger r=3 inequality into r=2.

7. Witness sum: if D(m)=product(2a+1), then 3(4D)^2+(4D)^3<=112D^3. The local inequality (2a+1)^3<=binom(a+26,26) follows by induction from the displayed polynomial ratio identity. Therefore D^3<=tau_27. The27-fold divisor sum is at mostY(1+logY)^26 by an elementary factor-tuple count. Extending split odd m to all m only enlarges the sum. The fixed absolute constant512 covers112*4/[2(log5)^2]<87 and replacement of logB by1+logB.

8. Residual accounting:152's small alphabet sector is assigned first;153's qualifying cofactor sector is assigned second outside it; the remainder has no small complementary factor. Thus the partition is disjoint, and no overlapping savings are multiplied. P_small and P_peel are both o(M3), making the full target equivalent to the still-unproved P_bal=o(M3).

9. Nonvacuity of the algebraic receiver versus existence: finite cofactor witnesses with nonzero C and candidate primes do occur (see JSON). They are NOT asserted to be physical cuboids. No existence or nonexistence of cuboids is inferred from the replay. On top dyadic shells,153's new nearly1/3-threshold sector is restricted by151 to r=2 and n>=2. This limitation is stated in the card; claiming removal of all large squarefree-prime mass would be false.

## Improvement over an initially looser proof

A first counting idea multiplied the witness count by the whole fixed-R Gaussian triple count R^o(1). Reconstructing the last positive edge removes that unnecessary factor. Charging D(m)^3 against tau_27 also replaces an unspecified m^o(1) sum by an explicit logarithmic cost. These corrections yield the nearly B^(1/3) threshold with a proved logarithmic saving. This is why the final result is more than another fixed-cofactor lemma.

## Dedupe and limits

151 contains the Gaussian divisibility and the failure of the scalar dominant-prime candidate sieve. It does not sum the nonzero cofactor witnesses.152 counts one prescribed prime alphabet and proves separate all-height finiteness. Neither estimates the union over unrestricted moving p via small m. COMMON-001, XD-001 and118/119 were checked in the live ledger: their populations and summation interfaces differ and are not imported here. Old Stage14 charged-cofactor work is not rebranded as this theorem. No claim of literature-wide novelty is made.

The elementary proof is self-contained once the audited151 endpoint bridge is retained. No new external theorem, unit-equation constant, PNT, determinant method or independence heuristic is needed. The application has a within-session audit, not an external independent hostile audit.

## Exact replay

verify153.py uses only the Python standard library. Recorded PASS checks:

-1001 local binomial/ratio-identity checks;
-exact divisor-sum majorants for seven cutoffs;
-67664 ordered Gaussian witness tuples over nine split cofactors, checking the nonzero norm bound and squared-prime budget;
-736 exact Gaussian orientation/reconstruction roundtrips;
-64 exponent-budget checks;
-the zero-edge C=0 counterexample;
-the logarithmic budget30-27-1=2.

These finite checks supplement the written uniform proof and exercise failure cases. They do not replace it. Verification153.json records the domains and examples.

## Durable continuation

Latest result153; next154=BalancedResidualJointGaussianCount. Prove a summed estimate for the residual with some prime outside S_B and R/p^v_p(R)>Y_B for every p|R. Preserve TI parked,120 retracted,147–149 retained and no automatic curve-degree escalation. Do not credit the full global gate or repeat the already-summed small-cofactor sector.

Handoff repair: direct fetch and exact-byte comparison recovered all four152 artifacts, including verify152.py (1WBlzhBdvCA-oyMhNJC6V_JJHW4GMy1vM) and verification152.json (1Q1gCTytRlm6xCxROlIb4477ZbCyiwA7I). The prior authority's NOT_CONFIRMED_BY_CURRENT_DRIVE_SEARCH statement is obsolete as an operational pointer; no mathematical result is retracted by this repair.
