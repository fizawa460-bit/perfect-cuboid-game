# M3-T11-161 — Principal class: summed short primitive-face sector

STATUS: PROVED_USING_RETAINED_UNIFORM_010 / LONG_FACE_TAIL_OPEN

PRIMARY_GATE: M3-T11-GATE-001, OPEN. GLOBAL_COUNTING_CREDIT: 0.

Goal remains **P(B)/M3(B) -> 0** under the exact physical space-diagonal cutoff R<=B. This card supplies a restricted endpoint-count saving, not a global solution or a nonexistence theorem.

## Current authority and sources

Fresh MAIN, RESEARCH-INDEX, RESULT-LEDGER, active T11 ROUTE and complete card160 all designated160 before this continuation. Known history was searched selectively, not reread in full.

- [Active ROUTE](https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit): section14.1 = retained010 uniform fixed-edge-ratio bound; section25.4 = tH14 residue/global-squareclass firewall; section82.5 = TQ005 exact common-core adapter.
- [Card160](https://drive.google.com/file/d/1c9OWzC-JvfW9UWg3KR3EktRZju86B88H/view): physical first-cover normalization and high-kernel energy bound; principal class remains open.
- [RESULT-LEDGER](https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit): retained010,011,012 and the global counting firewall.

## 1. Set counted, including all content and families

Use the ORIGINAL physical first-cover state population H_F(B), before imposing the missing-face square H. All original physical masks, contents, lifts and chart conventions remain in force. For a state with positive missing-face legs C,X, put

g=gcd(C,X), c0=C/g, x0=X/g, kappa=sf(c0^2+x0^2).

On kappa=1, p0=sqrt(c0^2+x0^2) is a positive integer, p0<=R<=B. Rational square roots of integers are integers. Thus (c0,x0,p0) is a primitive positive Pythagorean triple and

p0 = sqrt(C^2+X^2)/gcd(C,X).

The cutoff p0<=T is on the **primitive missing-face hypotenuse**, not the space diagonal R, physical face diagonal, common Gaussian core, or011's collision-direction hypotenuse N.

Define r_1,<=T(B) to count states in H_F(B) with kappa=1 and p0<=T. Contents are NOT fixed in this definition.

## 2. Summed principal-sector bound

Let D(T) be all ordered positive primitive Pythagorean leg directions (c0,x0) with hypotenuse<=T. Euclid's primitive parameterization gives m>n>0, gcd(m,n)=1, opposite parity,

{c0,x0}={m^2-n^2,2mn}, p0=m^2+n^2<=T.

There are at most T parameter pairs, by putting both m,n in the square of side floor(sqrt(T)). At most two leg orientations occur. Consequently #D(T)<=2T. This deliberately elementary envelope includes every direction, with no split-prime or angular assumption.

Retained010, uniformly in each physical rho=C/X, gives

m_rho(B)=#{s in H_F(B): C(s)/X(s)=rho} <= B^o(1).

For each epsilon>0 this means one constant K_epsilon works for ALL ratios of allowed physical height. Since a positive rational ratio has a unique primitive vector, summing these fibers gives, for 1<=T<=B,

**r_1,<=T(B) <= 2 K_epsilon T B^epsilon = T B^o(1).**

The moving-family count 2T is paid explicitly. Retained010 already sums physical lifts and contents; no additional content sum is silently omitted. The uniformity in010 is an essential retained dependency, not reproved here or replaced by fixed-twist finiteness.

## 3. Actual endpoint consequence and charging

For a primitive canonical positive endpoint E, define for each of its three faces

p_ij(E)=sqrt(e_i^2+e_j^2)/gcd(e_i,e_j), and p_min(E)=min_ij p_ij(E).

Let P_short(B;T) count original endpoints at R<=B with p_min<=T. Choose deterministically the first minimum face in canonical edge-label order and use its complementary edge as the shared edge Y. The other two faces and the space diagonal are integral, so card160's physical first-cover construction supplies a state with this face missing and kappa=1. The state retains its physical parent, hence this deterministic assignment is injective at the parent level. The existing first-cover endpoint coverage, not the255-state census normalization, is used here. A fixed chart convention may change the harmless absolute constant.

Therefore

**P_short(B;T) <= O(r_1,<=T(B)) <= T B^o(1).**

For EVERY fixed delta>0 with delta<1/3, choose T=floor(B^(1/3-delta)). Taking epsilon<delta and using retained M3(B)>>B^(1/3) yields

**P_short(B;T)/M3(B) -> 0.**

This covers all families/content in this endpoint sector and all three possible choices of the small face through deterministic charging. It is not a fixed-curve theorem. Equal missing-face legs cannot occur in class1 because 2c0^2 is not a square.

The exact residual is P_long(B;T): original endpoints with **all three p_ij>T**. Thus P=P_short+P_long. The identity is bookkeeping; only the displayed bound on P_short is new scoped counting credit. No bound below B^(1/3) is obtained for P_long.

## 4. Why counting every principal direction does not close the gate

The elementary direction-family size is actually Theta(T), not subpolynomial. Here is a self-contained lower envelope, not an endpoint lower bound. Let U=sqrt(T), restrict odd m to (U/2,3U/4] and even n to (0,U/4]. Then m>n, m^2+n^2<=5T/8 and there are T/64+O(U) pairs. Every noncoprime pair has a common odd prime. For such a prime p, the number is T/(64p^2)+O(U/p+1). Summing p<=U costs O(U log U), and

sum_(odd primes p) 1/p^2 <= sum_(n>=3)1/n^2 <= 4/9 <1.

Hence at least (5/576)T-O(sqrt(T)log T) primitive parameter pairs survive, giving distinct oriented directions. With the upper bound above, #D(T)=Theta(T).

At T=B the unselected family costs order B. Uniform fixed-ratio occupancy B^o alone consequently provides an O(B^(1+o)) envelope, worse than the retained whole-host B^(1/2+o). This is a limitation of that summation, NOT a lower bound for physical states or endpoints. A physical admissible-direction sparsity/incidence estimate is still indispensable. Neither linear direction-family growth nor finite principal-class absence demonstrates impossibility of the goal.

## 5. Existing analytic receiver range check

TQ005 (ROUTE82.5) is an exact squareclass identity on fixed t37 common-core packets. Its square norm factor disappears from [H], but it does not count moving principal directions or sum physical packets. tH14 (ROUTE25.4) explicitly closes same-modulus residue collisions and explicitly leaves distinct exact pairs sharing one global rational squareclass open. Therefore neither supplies the missing bound on P_long or r_1 by merely specializing kappa=1. This audit reuses their recorded scope, rather than claiming a new refutation of those routes.

## 6. Endpoint count versus energy

Within the short principal sector, the pair energy is r_short^2<=T^2 B^o=o(B^(2/3)) at the displayed cutoff. However the FULL principal energy also includes 2 r_short r_long. Using only the retained host bound gives mixed energy <=T B^(1/2+o); for small delta this is not o(B^(2/3)). Do NOT promote the restricted energy bound to disposal of every collision touching a short state.

The endpoint-count argument can discard P_short directly and need not solve this mixed-energy problem. Similarly160's high-kernel energy saving remains valid but supplies no class1 endpoint-count saving.

## 7. Verification and scope

verify161.py independently enumerates primitive principal directions by Euclid parameters and by integer circle coordinates at p0<=1000: both produce316 oriented directions.1264 integer content-invariance checks pass. These are ARITHMETIC DIRECTIONS, not physical endpoints. Physical endpoints enumerated=0. This test checks the direction normalization and finite family inclusion only; it does not establish010, actual principal occupancy, or the asymptotic theorem by experiment.

Proof review is within this session, not an independent external audit. No literature-wide novelty is asserted for elementary Pythagorean counting. The scoped result is its uniform, fully summed application to the original principal endpoint sector.

NEW_ENDPOINT_SECTOR_BOUND=true
NEW_GLOBAL_ENDPOINT_BOUND=false
PRINCIPAL_CLASS_GLOBALLY_CONTROLLED=false
P_OVER_M3_LIMIT_PROVED=false
GLOBAL_COUNTING_CREDIT=0

## 8. Concrete continuation

LATEST_RESEARCH_CARD=M3-T11-161. NEXT candidate162.

CURRENT_ATTACK=PrincipalClassLongPrimitiveFacePhysicalSupportEstimate.

Continue on the original physical class1 population, with exact R and all packet/content costs. Seek a genuine bound P_long=o(M3), or a uniform/averaged admissible-direction incidence estimate strong enough to imply it. A fixed-power #D_adm(B)<<B^(1/3-eta), with the retained010 uniform fiber bound, would suffice, but no such estimate is currently proved. D_adm counts only actual physical principal states in the long sector; its sparsity must be established, not assumed from the full family's size. Defining this set is not research credit.

Do not issue162 merely for another arbitrarily smaller cutoff, another fixed hypotenuse, or a renamed residual. Do not require all nonprincipal kernels to be solved when pursuing the direct endpoint goal. Candidate③ global principal incidence remains OPEN; the separate A001 analytic receiver is not exhausted by this card. Retain152/153, E_bal unresolved,010/011/012 scopes,155–160 scopes; TI parked,120 retracted,147–149 curves frozen.
