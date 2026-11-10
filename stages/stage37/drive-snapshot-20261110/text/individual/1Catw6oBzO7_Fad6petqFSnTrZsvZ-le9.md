# M3-T11-208 — Primitive third-face branch mask on the exact raw content-tail measure

Date: 2026-10-03 JST.
Status: PROVED_EXACT_PRIMITIVE_BRANCH_CHARACTER_ADAPTER / SAME_MEASURE_NECESSARY_MASK / VERIFIED_FINITE_FILTER_ONLY. Gate OPEN; global counting credit0; no asymptotic saving, no retraction. 162–185 separate-chat audit scope retained; 186–208 separate-chat audit NOT RUN.
Authority read: fresh MAIN, short RESULT-LEDGER, CARD-INDEX through207,207,174/175/172/168, active ROUTE166–168/current split and CROSS-GCD XG005–008. Relevant earlier local saturation014 and index099/100 are reused principles, not rediscovered as new general theorems.

## 1. Concrete advance and scope

207 distinguished the all-pair c_max from eligible-chart c_chart on raw two-face objects. This card preserves that exact primitive physical measure and constructs an additional necessary endpoint mask which is nonconstant on the raw tail.

The weak test “the missing face square is locally soluble at content primes” is automatic, but the primitive coprime-factor square branches are stronger. Their two Legendre signs coincide at each content prime. An endpoint requires their common sign to be+1. This gives a genuine filter, with one coupled sign per prime, and no further unit-square restriction from higher prime powers.

A stronger mask tests the two normalized factors separately in Q_p for all p dividing2R. Every full endpoint passes it; many raw objects do not. This defines a strictly smaller same-measure upper-cover receiver for the useful-cutoff tail. A uniform asymptotic count for that receiver remains OPEN. The elementary factorization itself is standard; the new Stage37 contribution is its raw eligible-chart normalization, exact coupled character formula, all-2R branch-mask inclusion and complete207-census audit.

## 2. Exact primitive normalization on any eligible chart

Let a be the shared physical edge of two integral faces, with other edges x,y. Thus a²+x² and a²+y² are squares, and a²+x²+y²=R². The primitive positive triple is counted once after sorting. Select the eligible pair achieving c_chart, ties lexicographically; equivalently select its shared edge a. On exactly-two-face raw objects the choice is unique. On full endpoints choose the same canonical rule.

Put

h=gcd(R,a), D=R/h, u=a/h,
epsilon=2 if a is odd, and epsilon=1 if a is even,
A_-=(D-u)/epsilon, A_+=(D+u)/epsilon.

Primitive integer sphere data force R odd: if R were even, the three edge squares sum to0 mod4 only if all three edges are even. Thus h is odd and D,u are coprime; D is odd and u has the parity of a. The definitions give positive integers with

gcd(A_-,A_+)=1,
F:=R²-a²=(epsilon*h)² A_- A_+.                 (208.1)

Indeed gcd(D-u,D+u) divides2; it equals2 for u odd and1 for u even. Therefore

F is an integer square iff A_- and A_+ are each integer squares. (208.2)

This equivalence uses positive coprime integer factors. Merely testing their product in one local field is weaker, because both factors may be in the same nonsquare unit class there.

Let h_x=gcd(R,x),h_y=gcd(R,y), and c=h_x h_y, the cross-gcd of this eligible chart. Retained XG007 gives the two primitive space triangles opposite x,y. Primitive sphere data also give pairwise-coprime h_a,h_x,h_y: a prime dividing R and two edges divides the third by the sphere equation, contradicting primitivity. Hence

c divides R, gcd(c,a)=gcd(c,h)=1.             (208.3)

Every prime dividing R is1 mod4. For any p dividing R, at least one of the two eligible reduced space hypotenuses R/h_x,R/h_y retains p, because h_x,h_y are coprime. That primitive Pythagorean hypotenuse has only split odd prime divisors. In particular p dividing c is odd and1 mod4. These support facts reuse the raw two-space-triangle adapter; no third face is assumed.

## 3. Coupled branch character at c

For p dividing c, D=0 modp and u is a p-unit. Write chi_p for the Legendre symbol. Reduction of(208.1) gives

A_-=-u/epsilon modp, A_+=u/epsilon modp,
chi_p(A_-)=chi_p(A_+)=chi_p(u/epsilon)=:eta_p. (208.4)

The equality uses chi_p(-1)=1. Therefore the primitive square branches impose exactly the necessary condition

eta_p=+1 for every p dividing c.              (208.5)

By contrast F=-a² modp and gcd(a,p)=1, so F is automatically a unit square in Q_p. Hensel's lemma makes this true at every p-power. A product-face-square sieve on c-supported moduli therefore removes no raw objects. This extends014's weak product-square warning from endpoint tau support to the pre-third-face raw chart, with explicit normalized branch separation.

The stronger branch mask(208.5) is not automatic. If eta_p=+1, both A_-,A_+ are p-adic unit squares and lift at every p-power. If eta_p=-1, neither is a square even modp. Thus there is one coupled sign, not two independent half-densities, and deeper prime powers impose no additional unit-square predicate. The general Hensel/no higher-power gain principle is already100; the new formula here is chi_p((a/h)/epsilon) on this raw physical measure.

For fixed unit h and epsilon and mod p^k, the unit-square test on u/epsilon admits exactly phi(p^k)/2 unit u classes. For a modulus supported on c the formal unit-class fraction is2^(-omega(c)), not a c^(-alpha) density. This is an ambient class-count statement, not a raw-family equidistribution theorem. No class fraction is multiplied into the Stage14 half-power count; additional correlations on the physical family could still give a stronger result.

A raw example shows the strictness: e=(252,2261,2640),R=3485,shared a=252,h=1,c=85. Then A_-=3233,A_+=3737; the common branch character is-1 at both5 and17. F is nevertheless locally square at all primes dividing R and at2. Product local solubility misses this actual branch exclusion.

## 4. All-2R branch mask and exact upper receiver

Define M_c^branch to be(208.5), and

M_2R^branch=1 iff A_- and A_+ are squares in Q_p for every prime p dividing2R. (208.6)

This is explicit. For odd p and positive integer A, write A=p^t v with p not dividing v: it is a Q_p-square iff t is even and chi_p(v)=+1. At2 it is a square iff t=v_2(A) is even and A/2^t=1 mod8. Apply these tests to each coprime factor. Global integer squares pass all these tests, so every endpoint has M_2R^branch=1. Also M_2R^branch implies M_c^branch.

On the canonical chart from Section2 let

T_2R(B,C)=#{raw sorted primitive sphere objects R<=B, at least two integral faces, c_chart>C, M_2R^branch=1}.

207 endpoint inclusion sharpens to

#E(B;c_max>C) <= T_2R(B,C)
 <= T_cbranch(B,C) <= T_chart(B,C).            (208.7)

Proof: a full endpoint has c_chart=c_max, the chosen shared edge has integer remaining face, and(208.2) makes both factors integer squares. The same sorted object is mapped injectively; no chart, sign, Euclid or radial multiplicity is added. The receiver is a necessary-condition relaxation and its survivors are not claimed endpoints. In particular this is not a proof of full-S/product-phase compatibility on those survivors.

A sufficient NEXT bound is T_2R(B,B^(1/6+xi))<=B^(1/3-xi+o(1)), for fixed0<xi<1/12; the convenient form B^(1/2+o(1))/C at that one cutoff would suffice. Neither is proved here. It is not necessary to prove the larger unmasked raw-tail conjecture first. The175 raw lower family is not asserted to survive this branch mask; no new R502 classification is performed.

## 5. Localization of what is still missing

For comparison, the weaker product F test at p dividing R has the following exact depth table. Let r=v_p(R),s=v_p(a), p odd.

| Depth | Primitive unit reduction | Product F local square |
|:---|:---|:---|
| s<r | F/p^(2s)=-a_0² modp | automatic, since p=1 mod4 |
| s>r | F/p^(2r)=R_0² modp | automatic |
| s=r | F/p^(2r)=R_0²-a_0² | test even valuation and unit Legendre+1 |

Only the equal-depth row can obstruct F itself at conductor primes. This does not mean the two branches are automatic in the other rows: their common unit sign can still be-1, as(208.4) illustrates. Do not replace the branch mask by the product mask.

Write A_-=kappa_- z_-²,A_+=kappa_+ z_+² with positive squarefree kernels. Coprimality gives gcd(kappa_-,kappa_+)=1 and squarefree kernel(F)=kappa_- kappa_+. On M_2R^branch, both kernels are coprime to2R and chi_p(kappa_-)=chi_p(kappa_+)=+1 for every odd p dividing R. Hence a nonendpoint survivor has a nontrivial kernel in at least one factor supported entirely outside2R. “Outside2R” here is not185/186's relative-fresh phase-support terminology.

Example surviving all these local branch tests: e=(533,756,3360),R=3485,c=205,shared a=756, A_-=2729,A_+=4241. The coprime squarefree kernels are2729 and4241, outside2R, while neither factor is globally square. Thus the all-2R branch mask is necessary and genuinely narrower, but insufficient. The remaining task is an actual joint count for these moving coprime-factor kernels/roots and the original two-face reconstruction, or for the full endpoint subset. A fixed kernel label, an unweighted CRT count or another local-power refinement does not pay that support.

## 6. Complete bounded audit, not an asymptotic saving

Reused source:207's completely enumerated, independently matched255 sorted primitive raw objects at R<=10^6. The255 population was already160; it is not counted as a new discovery. All have exactly two integral faces. The new script checks(208.1)–(208.5), conductor depth cases, kernel factorization and masks on each record, then recomputes the useful-cutoff subsets using exact integer comparisons c^den>B^num.

| B | exponent | unmasked chart tail | content branch mask | plus weak F tests at2R | all-2R separate branch mask |
|---:|:---:|---:|---:|---:|---:|
| 1000 | 3/16 | 2 | 2 | 1 | 0 |
| 1000 | 5/24 | 2 | 2 | 1 | 0 |
| 1000 | 11/48 | 2 | 2 | 1 | 0 |
| 10000 | 3/16 | 16 | 6 | 5 | 3 |
| 10000 | 5/24 | 16 | 6 | 5 | 3 |
| 10000 | 11/48 | 16 | 6 | 5 | 3 |
| 100000 | 3/16 | 62 | 30 | 25 | 10 |
| 100000 | 5/24 | 62 | 30 | 25 | 10 |
| 100000 | 11/48 | 58 | 26 | 23 | 9 |
| 1000000 | 3/16 | 192 | 81 | 64 | 22 |
| 1000000 | 5/24 | 183 | 73 | 58 | 22 |
| 1000000 | 11/48 | 183 | 73 | 58 | 22 |

At10^6 the masks retain142 of255 on c-supported branches and38 of255 on all-2R branches. The weak product F tests alone retain188 at2R. There are776 conductor-prime depth checks:751 with s<r,25 with s=r, none with s>r in this bounded population. All25 equal-depth incidences fail the weak product test here; this observation is NOT a theorem that the equal-depth row is always impossible. The proof table treats all three cases.

Supporting root replay:2496 F/content-prime-power checks and2520 accepted normalized-branch prime-power checks at orders1 through6. Direct valuation/unit tests are cross-checked against the independently factored squarefree kernels. The symbolic arguments establish all B and all prime-power orders; bounded replay only verifies the implementation and table. Physical endpoint count0 remains bounded, not a general nonexistence conclusion. Within-session review only; no independent hostile audit.

## 7. NEXT209 and preserved constraints

Attack T_2R at the useful cutoff, keeping its actual primitive normalization, canonical eligible chart, moving coprime factors A_-,A_+, raw two-face/space compatibility and intrinsic R<=B. Alternatively count full endpoints directly. A character average, factor/root support bound or physical measure adapter must produce a fixed-power gain with all moving support costs included. Need no stronger uniform all-C law;156 rejects that historical request.172/175 uncapped moment obstruction remains retained. The elementary index2 sign count alone supplies no such theorem.

Preserve207 chart/all-pair distinction,206 original signed G_gap/N_T,205 large-u and other valid sectors; do not multiply their savings. c_max remains distinct from c_u. large-c_u/full-S joint occupancy remains a separate OPEN gate. Do not keep refining the same c-supported unit square to higher p powers or recycle the fixed-fiber counts.

Drive writeback also synchronizes the stale short-LEDGER current-control pointer (which still said204/NEXT205) to208/NEXT209; historical entries remain unchanged. No mathematical authority/credit/closure flag changes beyond the exact208 adoption above.

## 8. Reproduction and durable files

Python3 standard library only. Download the207 source TSV and the208 script into one directory; run `python3 stage37_raw_local_208.py`. It generates M3-T11-208-verification.json, including every labeled record, masks, examples, spectrum and source/script SHA256. The JSON is evidence, the present card is the proof authority.
- 207 source TSV: https://drive.google.com/file/d/1yxcVSTyp0cl-PM-4rFaYRsdvDssUDnYm/view ; FILE_ID=1yxcVSTyp0cl-PM-4rFaYRsdvDssUDnYm
- 208 script: https://drive.google.com/file/d/1UyFUGnBSsMvJEGyoO-u7fBoTtLdzqIsx/view?usp=drivesdk ; FILE_ID=1UyFUGnBSsMvJEGyoO-u7fBoTtLdzqIsx
- 208 JSON: https://drive.google.com/file/d/1uhhVhXKwiae-7sHeYw29pn7uVeCp_9iG/view?usp=drivesdk ; FILE_ID=1uhhVhXKwiae-7sHeYw29pn7uVeCp_9iG
- 207 card: https://drive.google.com/file/d/1vgDMV2S2BSJXf8s3gIglsJE93fd4juR_/view
- retained014: https://drive.google.com/file/d/1KWnXzE0vUBBCbF5Hm9pQUCmPwW0YLfDv/view
- CROSS-GCD active source: https://docs.google.com/document/d/1hRZvWUMvITpvzj8E6AI8hFnOc0PTmB1yO6RvvB6rhUg/edit
- active ROUTE: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit
