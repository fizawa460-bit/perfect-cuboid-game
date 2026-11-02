# MB104 — coreless square-class interface: the missing divisor condition

Batch: MB104-DRIVE-20261026-SQUARECLASS-01. Route E. Status: PROVISIONAL / CONDITIONAL EXACT REDUCTION / NO CLOSURE CREDIT.

## Result and scope

Two character square classes identify the odd parts of the two branch pullbacks. They do not identify their even parts by parity alone. An explicit candidate ramification clump exists exactly when the sums of the even half-divisors agree. Separately, multiplicative decomposition of any one of a, b, a/b into functions from the two quotient pencils forces a common nonconstant function and therefore a core. This supplies a precise sufficient target for a contradiction to the surviving CORELESS / NO NONEMPTY CLUMP branch; it does not prove that target.

This is a consequence of the labelled common-H-cover model in the retained note, not an independently audited reconstruction of its historical H-generator marking. No actual carrier, new finite cutoff, or clump is constructed.

## Source and duplicate boundary

Input: MB104-000707-CORELESS-INVARIANT-LINE-WALL-20260926.md, Drive ID 1ZzJNR6Ug6kbnSaLDSqkUHwme4DFp0jjT, exact SHA256 c66c5d88218ca42af669694da44cd56b3556fb8d99a4fa506c3d40e7b25af24a.

The current STATE records the older common-H factor-line source blob 1e121116c1591e3b3d9f748f306151ab0e89b580. Its full text was not found by the targeted Drive filename/content searches in this batch. Thus the character-labelled setup below is taken conditionally from the retained current note. No assertion of global novelty or exhaustive comparison with unavailable historical notes is made. Existing canonical-line NO-GO is reused; it is not re-proved as a new result.

## Setup

Work over an algebraically closed field of characteristic zero. Let p:Z->E be the common H=(Z/2)^2 quotient and pi:C->P1_r the fixed cover

u^2=(r^4+4)/4, v^2=(r^4-4)/4.

Let f_i:Z->C be finite etale and pi o f_i = psi_i o p. Put r_i=psi_i^*r. All maps are nonconstant. The two character labels must be fixed, with no unrecorded interchange. Write

F_i+ = r_i^4+4, F_i- = r_i^4-4,
F_1+ = a^2 F_2+, F_1- = b^2 F_2-, a,b in k(E)^*.

Let B+ and B- be the four roots of r^4=-4 and r^4=4 on P1. Put D_i±=psi_i^*B± and I_i=psi_i^*(infinity). Then div(F_i±)=D_i±-4I_i.

## 1. Odd parts agree; even halves remain

The square-class equations imply equality of every valuation modulo 2. Hence there are common reduced divisors S± and effective divisors T_i± with

D_i± = S± + 2 T_i±,
div(a) = T_1+ - T_2+ - 2(I_1-I_2),
div(b) = T_1- - T_2- - 2(I_1-I_2).

Here T is the even half-divisor, not merely a numerical degree or divisor class. In the etale commutative square, ramification indices satisfy e(psi_i)*e(p)=e(pi)*e(f_i). Since e(f_i)=1 and e(pi)=1 or 2, preimages of B± have e(psi_i)=1 or 2. Thus the S± are exactly the corresponding branch points of p, and T_i± are reduced, unramified over p. All the T_i± are disjoint from S+ union S-. The signs are disjoint within each i.

Parity does not set T_1±=T_2±. The local pattern D_1+=2 and D_2+=0 is compatible with the square equation through ord(a)=1. This is a local compatibility observation, not a global example satisfying all retained geometry.

## 2. Exact criterion for the fixed ramification-set clump

Let R± be the reduced ramification points of pi over B±, so pi^*B±=2R±. Pull back the commutative square:

f_i^*R± = (p^*S±)/2 + p^*T_i±.

The half is integral because p has index two over S±. Since f_i are etale, these pullbacks are reduced. Therefore

f_1^{-1}(R+ union R-) = f_2^{-1}(R+ union R-)
iff T_1+ + T_1- = T_2+ + T_2- as actual divisors.

Pullback of divisors by a finite surjective p is injective, so the reverse implication is also exact. When equality holds, this common finite nonempty subset of Z is a union of complete fibers of both legs: it is a clump. The surviving no-clump hypothesis therefore forbids that equality for this particular candidate set. This does not classify all possible clumps.

Equivalently the missing equality is

div(ab) + 4(I_1-I_2) = 0.

Being principal, having zero degree, or having the same line-bundle class is insufficient: a nonzero principal divisor need not vanish. This is precisely the distinction lost in a line-class-only shortcut.

## 3. A multiplicative-factorization target that forces a core

Put q+(r)=r^4+4, q-(r)=r^4-4, q0(r)=(r^4+4)/(r^4-4).

For (q,c)=(q+,a),(q-,b),(q0,a/b) we have q(r_1)=c^2 q(r_2).

If c=alpha(r_1)/beta(r_2), alpha,beta in k(r)^*, then

(q/alpha^2)(r_1) = (q/beta^2)(r_2).

Each function q/alpha^2 is nonconstant: q has simple zero/pole at the designated branch values, and division by a square cannot remove odd valuations. Pulling the equality to Z gives a common nonconstant function from the two copies of C. By the definition of a core, the correspondence has a core.

Consequently the coreless branch requires all three multipliers a, b, a/b to avoid k(r_1)^* k(r_2)^*. In particular none can be constant. This is only a necessary condition on a surviving candidate. No argument in this batch forces a multiplier into that product subgroup.

## What is closed, what remains, what to do next

Closed as a shortcut: identifying odd branch supports, or principal divisor classes, and then announcing a clump. The equations preserve the even-half discrepancy. This is not a proof that the full two-character common-cover route is NO-GO.

OPEN: whether the retained 000707 support/common-etale data force either (i) the actual even-half divisor equality above, or (ii) multiplicative factorization of a, b, or a/b. Either implication would contradict a surviving hypothesis. Neither is established here.

Next shallow gate: find an explicit geometric adapter from the retained common-H/support data to one of (i),(ii), preserving actual point/divisor information. Read/recover the missing labelled factor-line source before claiming the historical action marking has been independently verified. Do not repeat the square-class derivation, canonical-line argument, or parity/degree/class comparison as if they supplied that adapter. If no adapter is available, record PARKED / ADAPTER MISSING rather than declaring all coreless correspondences impossible.

## Verification and claim boundary

The companion verifier checks the locked input-note hash, exact polynomial elimination identities, and all allowed local ramification/parity patterns used in the divisor formulas. The geometric arguments in sections 2 and 3 are explicit proofs conditional on the stated commutative square; finite algebra checks do not certify global existence/nonexistence.

No external literature was fetched, no GitHub access was made, and no heavy compute was run. Retained frontier, historical source claims, receiver/effectivity/theorem/endpoint/merge credit remain unchanged. This note is a provisional Drive result awaiting independent audit before promotion.
