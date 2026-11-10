# M3-T11-142 — Linear-height nonphysical family defeats counting the bare Heron cover

STATUS=PROVED_LINEAR_SUPPORT_IMPOSTOR_FAMILY_FOR_ENLARGED_HERON_RECEIVER
AUDIT_MODE=WITHIN_SESSION_ADVERSARIAL_REDERIVATION_NOT_EXTERNAL
GLOBAL_COUNTING_CREDIT=0
PRIMARY_GATE_STATUS=OPEN
TI=PARKED
NEXT=M3-T11-143 JointSignedLiftHeronRealizedSupportBeyondBareCover

## Authority and target
Fresh MAIN/INDEX/RESULT-LEDGER/active ROUTE141 and latest141, with140 proper factor/parity,139 signed integer reconstruction and138 physical projective height. No full-history reread. The question is whether141's content-complete large-square-divisor cover alone can furnish a sufficiently small moving support count. The answer for the enlarged integer cover is NO: an explicit fixed-content family has linear support in the same height window, while none of its points is physical.
This does not refute a count imposing the original T11 packet or the full139 signed/monic lift. Those additional conditions are not verified in this family. Preserve every established physical result and all credit/closure flags.

## 1. Explicit arithmetic progression and primitive plus-vector impostors
For k>=0, put
 n=241+8670k, R=17n,
 A=(6n+5,6n+3,3n+4).
The step8670=2*3*5*17^2. Thus n is odd, n=1 mod3 and5, n=241 mod289, and n is a17-unit.
Every A is positive and odd. A_1-A_2=2, so gcd(A_1,A_2)=1 and the triple is primitive.
For primes of n, gcd(n,A_i)=gcd(n,5),gcd(n,3),gcd(n,4), respectively, all1.
Modulo17, A=(6,4,13), all units. Hence gcd(A_i,R)=1 for all i: the algebraic content profile is h_i=1, H_c=1 and tau=R.

These are integer candidate coordinates, not values recovered from any physical endpoint. Their actual height is H=max A_i=6n+5. For n>=241,
 R/3<H<R,
so they satisfy138's two-sided height window (including the stronger Cauchy lower constant, which is less than1/3), and each A_i^2<2R^2. Also F_0/R^2 lies between81/289 and1, within the retained physical Cauchy norm window. Thus the failure is not caused by an inflated ambient height or a moving content constant.

## 2. They pass the full bare quadratic square-divisor cover
Their four Heron forms are exactly
 F_0=81n^2+120n+50,
 F_1=9n^2,
 F_2=9n^2+48n+32,
 F_3=63n^2+72n+18.
All are positive; their residues are3,1,1,1 mod8. Direct substitution n=241 mod289 gives289|F_0. The other three factors are17-units (since all A_i are17-units, uniqueness also follows from140).
Moreover gcd(n,F_0)=gcd(n,50)=1,
 gcd(n,F_2)=gcd(n,32)=1,
 gcd(n,F_3)=gcd(n,18)=1.
The assumptions on n make each gcd equal1.

Therefore the141 canonical maximum-depth allocation is
 (q_0,q_1,q_2,q_3)=(17,n,1,1).
Indeed at17 only F_0 has positive valuation, and at every p^lambda||n only F_1 has positive valuation, exactly2lambda. The allocation is unique and product q_j=R=tau; q_j^2|F_j.
The quotients zeta_j=F_j/q_j^2 have the required residues, with the fixed SMALL quotient
 zeta_1=9.
They satisfy141's explicit quotient-height bounds and H_c^2|product zeta (here H_c=1).

The original global divisor holds: R^2|product F_j. No individual F_j is divisible by R^2: F_1 is not a17^2 multiple, while F_0,F_2,F_3 are coprime to n>1. Thus they also pass140's no-full-factor-saturation and two-color conditions. Their largest allocation is q_1=R/17, while the only other nontrivial color is the FIXED17. Properness and two colors by themselves do not force any secondary color >=R^epsilon.
For n>=241, n^4>=17n, so the141 large-square-divisor threshold q_1>=tau^(1/4) is passed, with room to spare.

These claims concern the bare necessary cover and content/height conditions only. They do not certify the original Gaussian coefficient/orientation/cyclic masks, the original fresh unit-root destinations, or the139 monic/signed physical lift.

## 3. Every point fails a mandatory physical square test
From139 any integer signed physical reconstruction would require
 Bminus_2^2=2R^2-A_2^2.
But R=17n is a3-unit, so R^2=1 mod3, while A_2=6n+3=0 mod3. Hence
 2R^2-A_2^2=2 mod3,
which is not a square. Every member of the infinite family is NONPHYSICAL, independent of any sign choice. No positive physical endpoint was found.
This fixed-prime obstruction is used only to certify the counterfamily. It is not a newly credited character sieve or a proposal to iterate local screens for a power saving.

## 4. Quantitative no-go for the enlarged receiver
Let C_bare(B) count distinct primitive projective A satisfying this bare Heron/content/height/proper-factor cover with R<=B, without imposing the full physical lift or original packet masks.
The constructed family gives
 C_bare(B)>=max(0,1+floor((B/17-241)/8670)).
Thus C_bare(B) is Omega(B).
Its projective points are distinct: primitive positive representatives can only be equal up to sign, and A_1-A_2=2 fixes any proportionality to1; then n is determined.

Consequently no uniform bound C_bare(B)<<B^alpha with alpha<1 can hold for this enlarged receiver, even at FIXED H_c=1 and FIXED zeta_1=9. It cannot alone supply a sublinear support estimate, let alone the old hard one-twelfth budget or the applicable primary budget. This is an exact family/count argument, not a finite census extrapolation.

This is NOT a lower bound on the realized physical plus support, NOT a family in a proved original T11 coefficient packet, and NOT a contradiction of141's necessary-condition theorem. It rules out transferring an estimate for the enlarged cover directly to the required physical count without the missing lift/packet restrictions. No original receiver is retracted.

## Verification and audit
Python PASS for1000 members of the explicit AP: primitive odd content1 vectors, form identities, full tau canonical allocation, quotient residues and fixed9, R^2 product divisor, all proper factors, physical height window, and the mod3 minus-square failure.
Symbolic replay returns the three expanded F_i, expanded F_0,289 divisibility at241, and17-unit vector (6,4,13).
All1000 samples are certified nonphysical; no actual endpoint is enumerated. Algebra above proves every k and the linear cardinality. Within-session audit checked the progression, primitive/projective injectivity, exact R window, fixed content, maxima at prime powers, properness, and the explicit distinction from original packet/monic/signed conditions. Not an external audit.

## Handoff
M3-T11-143: the bare Heron large-square-divisor or small-zeta count is insufficient. Continue from141 ONLY with the139 signed minus-square/monic lift and original T11 packet coupled to exact R. A proposed moving-support theorem must genuinely use those missing restrictions and defeat this family at its proper step; do not substitute enlarged-cover sparsity, two-color properness, or fixed small quotient for physical scarcity. Consider a joint integral lift/nonlocal count, not additional leading-character filters.138 bounded fibers,140 parity/proper factors,141 content-complete allocation and120 retraction retained; global credit0/gateOPEN/TIparked and existing exponent budgets unchanged.

