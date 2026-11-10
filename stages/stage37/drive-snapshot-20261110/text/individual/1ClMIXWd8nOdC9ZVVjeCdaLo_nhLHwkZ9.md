# M3-T11-191 — Exact halfpoint denominators, arithmetic height and the cancellation-sector firewall

CARD_ID: M3-T11-191
STATUS: PROVED_EXACT_DENOMINATOR_AND_NAIVE_HEIGHT / LOST_CONTENT_NUMERATOR_TRANSFER / CANCELLATION_SECTOR_SUBSUMED_163
PRIMARY_GATE: M3-T11-GATE-001 OPEN
GLOBAL_COUNTING_CREDIT: 0
INDEPENDENT_HOSTILE_AUDIT: NOT_RUN

## 1. Current authority and scope
Fresh MAIN, operational CARD-INDEX latest190/blank next row, short RESULT-LEDGER, active ROUTE17 and190 were checked first. Only needed retained170/174/163 were fetched subsequently. This continues190's explicit request to prove arithmetic denominator/height control before counting its canonical halfpoint. The new result is exact denominator cancellation and ordinary rational height, plus a transfer law for lost content. It is not a canonical-height theorem or a new whole-population bound. A tempting cancellation-sector estimate is proved below but marked as subsumed by163.

Keep the original positive primitive endpoint R<=B, K=1 chart h1=h2=1,h3=h, all134 square/intrinsic-R/content/orientation/cyclic masks, and actual phase derived from original U,V,N_T. Retain189 projection obstruction,187/188 sectors,186 conservation and134 fresh D-only. Large-c threshold tail and K>1 remain separate OPEN. No external counting theorem is introduced.

## 2. Exact denominator theorem
Use190: e1=gA,e2=gF with gcd(A,F)=1, A odd,F even,A²+F²=n²; f_i below are POSITIVE absolute diagonals. K=1 gives gcd(R,e1)=gcd(R,e2)=1, hence gcd(R,g)=gcd(f1,g)=gcd(f2,g)=1. Put

N=(R+f1)(R+f2), M=f1+f2,
x=N/g², y=-NM/g³.

Define d by the reduced denominator Den(x)=d². Then d is an integer divisor of g, Den(y)=d³, and d is specified exactly as follows.

For every odd p with v_p(g)=v>0:
- If p divides neither R+f1 nor R+f2, v_p(d)=v.
- Otherwise v_p(d)=0.

Thus the odd part of d is a unitary divisor of the odd part of g: every prime power is retained whole or removed whole. For g odd, this is the entire rule. For g even, let v=v_2(g)>=1. Then

v_2(d)=v-1 if v_2(R+f1)=v_2(R+f2)=1;
v_2(d)=0 otherwise.                           (191.1)

When v=1 both alternatives give0. In particular d divides g/2 when g is even.

Proof at odd p: (R-fi)(R+fi)=e_i². Since R,fi are p-units, at most one of R±fi is divisible by p. A divisible plus factor therefore has valuation 2v_p(e_i)>=2v; if neither plus factor is divisible the numerator N is a unit. This gives precisely the displayed denominator exponent, with no partial odd-prime cancellation.

At2, R,f1,f2 are odd when g is even. Exactly one of R±fi has valuation1, the other valuation 2v_2(e_i)-1. Hence v_2(R+f1) is1 or2v-1; v_2(R+f2) is1 or2(v+v_2(F))-1. Both minima give v_2(N)=2, otherwise v_2(N)>=2v. This proves(191.1).

Finally y²=x(x-A²)(x-F²) with integral coefficients. At a prime where v_p(x)<0 the three factors have the same valuation; 2v_p(y)=3v_p(x). Negative x valuation is therefore even and y has the associated cube denominator. Where x is integral, y is integral by the same equation. Thus the EXACT reduced denominators are d² and d³. This proof needs the two primitive space triangles, not the remaining face lift; applying it to the full endpoint remains a post-filter.

## 3. Ordinary arithmetic height is now controlled
Write x=X/d², y=Y/d³ in lowest terms, X>0,Y<0. Then

X=N d²/g²,
R²(d/g)² < X < 4R²(d/g)²,
|Y|<8R³(d/g)³.                               (191.2)

Since R>g, x>1; the ordinary multiplicative rational height H_Q(x)=max(X,d²) equals X. Consequently

H_Q(x)<4B²(d/g)²<=4B²,
H_Q(y)<=8B³.                                 (191.3)

Unlike190's numerical coordinate upper bound alone, these are actual reduced numerator/denominator bounds. They do not assert a canonical elliptic height or a uniform rank bound. On a fixed primitive face the integral coefficients A²,F² have polynomial height, so the retained rational-point input already used in010/170 may be applied at polynomial ordinary height. This recovers a fixed-face B^o fiber; it does not sum the moving faces, and is not new counting credit.

The forced190 squareclass implies X=kappa V², kappa=2 for g odd and1 for g even, with gcd(V,d)=1. Its numerator root satisfies V<2B d/g. This is one coordinate identity, not an independent square-density saving.

## 4. Lost denominator is transferred to the ordinate numerator
The190 inverse gives

R/g = -(X²-A²F² d⁴)/(2Yd).

Since gcd(R,g)=1 and d|g, it follows that

g/d divides 2Y.                               (191.4)

Cancellation in x therefore does not make intrinsic g disappear. The ordinate numerator carries the lost factor; g must still be reconstructed through the inverse and g=Den(t) on the full lift.

There is an exact good-prime statement. Let p be odd, p|g/d and p not dividing A F (A²-F²). By section2 p does not divide d. Reduction of Q=(x,y) is integral, and the inverse z=-(x²-A²F²)/(2y) has pole of order v_p(g). Hence y vanishes modulo p and x reduces to one of0,A²,F². At any of these roots the inverse numerator x²-A²F² is a p-unit under the excluded-prime condition. Therefore

v_p(Y)=v_p(g).                                (191.5)

This shows the precise transfer away from the bad face primes. At primes of2AF(A²-F²), only(191.4) is asserted here. The lost factor need not be supported on190's delta conductor; no new fresh selector or independence of x/y denominator conditions follows.

## 5. A moving-face estimate, and why it gives no new disposal
Consider any dyadic population G<=g<2G, D<=d<2D. Original R<=B implies n<B/G. Primitive Pythagorean faces with n<=L number at most L log(2L): Euclid parameters have m²+k²<=L, giving O(L) pairs, or equivalently the standard divisor bound. Bounded face ordering is harmless.

For each face, section3 gives x=kappa(V/d)² with V<4BD/G, and at most O(D) candidate denominators d. A rational x gives at most two y, two w on the full190 cover, and bounded original sign witnesses; the inverse reconstructs t and g=Den(t), so there is no extra independent G factor. Every delta is derived from these same coordinates; do not multiply a separate delta support size. Ignoring all remaining square/phase filters is an upper bound. Thus

#E(G,D) <= B²(D/G)² B^{o(1)}.                  (191.6)

This pays moving faces and denominators explicitly, but is weaker than an existing sector bound where it might dispose endpoints.

Indeed d/g<=rho with 1/B<=rho<=1 forces g>=1/rho (since d>=1). Therefore n<=B/g<=B rho, so the primitive face short leg min(A,F)<=B rho. Retained163, already summed over all families/content, gives

#E(d/g<=rho) <= B rho B^{o(1)}.                (191.7)

The same dyadic sum of(191.6) gives B² rho² B^o, and B² rho²>=B rho throughout the nonempty range rho>=1/B. For rho<1/B the sector is empty. Thus(191.6) creates NO sector outside163's coverage. In particular rho=B^(-2/3-epsilon), fixed epsilon>0, is negligible by163; calling it a new cancellation disposal would double count an old short-face sector.

The current163 interior with min(A,F)>E implies g<B/E and d/g>=1/g>E/B. Extreme denominator compression is already excluded there. The remaining d/g is not forced close to1, but this argument supplies no new power saving on that interior.

## 6. Residual and NEXT192
Use the complete190 cover E plus w²=H, the exact191 denominator d²/d³ and height X<4B²(d/g)², and lost-content condition g/d|2Y (good primes have(191.5)). Retain g=Den(t), R=gz, recovered h/tau/n=h*k_shared, the forced Kummer bit and delta|rad(2|A²-F²|), and actual original phase both-legs/gap cutoffs. No independent phase variables, density multiplication or free g summation.

NEXT192: seek a joint moving-face occupancy estimate on the163 interior, exploiting the ordinate-numerator transfer together with the split-quartic square and original intrinsic height, or prove an effective c/tau cap from this simultaneous system. A fixed-face elliptic fiber and an x-denominator cancellation estimate alone are exhausted by old sectors. Prove a new coupling before claiming count credit; pay all moving face/content costs. Large-c threshold tail and K>1 low-median averaging stay separate OPEN.

## 7. Verification and retained authority
verify_m3_t11_191.py and M3-T11-191-verification.json: 6585 pairs of two primitive space triangles of common odd R<=20000, with primitive normalized adjacent legs of opposite parity. Exact Fraction checks pass for denominator rule, cube ordinate denominator, arithmetic height, elliptic equation, inverse and(191.4). 5986 g-odd and599 g-even cases;1113 show cancellation and216 partial cancellation;6216 have integral halfpoint. These are intentionally a larger two-triangle locus: the remaining face/full positive endpoint is NOT asserted. Physical endpoints enumerated=0. General statements above are deductive; finite checks do not prove an occupancy estimate. No independent hostile audit. Separate-chat audit remains162–185 and is not extended to186–191.

No retraction.190 numeric-bound wording is strengthened by this proved reduced-denominator theorem, not retrospectively treated as an arithmetic theorem. Gate OPEN/global credit0. TI parked,120 retracted,147–149 frozen;134 fresh D-only and all original masks retained.

## Durable references
190: https://drive.google.com/file/d/1r94c4fxMP3SXlWFh13JviKo0t7-ld9SV/view
163: https://docs.google.com/document/d/1Iz44vneEdanTNfZq7BRrNrl6ns26GTYze4--BVJ36V4/edit
170: https://docs.google.com/document/d/1qTO06Ir76L3FGzRMU8JtvvN-3MEKiWaUowGiVhRZqA8/edit
MAIN: https://docs.google.com/document/d/1gMO3D7hK2C4WgmpTz9RqeYEhvqAeKMqa0xOTxYW8TTE/edit
CARD-INDEX: https://docs.google.com/spreadsheets/d/1skBS4TxofX8A25cnhfoxO5VZZjfBRlW_sfzHkSTNiL4/edit
RESULT-LEDGER: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit
SCRIPT_DRIVE_ID: 1UdIDMQ1SKAtunM3WkrfoflAN8wEQD3Qv
JSON_DRIVE_ID: 1OPcOTI3DI0Y6lq6FiMCwzhvATDhDsFae
