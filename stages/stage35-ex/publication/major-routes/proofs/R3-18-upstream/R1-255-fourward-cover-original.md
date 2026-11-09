# Stage35EX R1-255 — Four genuine signed-18 Ward-square factors: global 16-fold cover, genus 5169, 15 character-quotient decomposition

lane_id: R1
run_id: R1-20261024T0346Z-R1-255-W18-FOURFACTOR-COVER-GENUS-CHARACTER-SPLIT
command: stage35ex-a
route_id: R1-09/R1-01
semantic_key: original-signed-orbit-gaussian-eds-global-intersection
base_snapshot: C35-183 COMPLETE / V74_GOAL4AK_SECTION334 (paired R0 receipt 1LcKdH6hV5-jR8VWbvZp5ZzxbOldlxnj9DYTh-rv9KZQ)
mathematical_status: PASS_SCOPED_DEPENDENT_GLOBAL_GEOMETRY_NOT_PHYSICAL_EXCLUSION
lane_authority: PROVISIONAL_LANE_ONLY
parent_credit: false
external_hostile_audit: false
R0_accepted: false
Branch_A: USER_PAUSED
Branch_B: OPEN

## Scope
For one actual positive primitive labelled A²+B²=C², C odd, set D=AC, original E:y²=x(x−A²)(x+C²), P=(D,BD), T0=(0,0), D_n=T0+[2n]P with signed n=±18. Restrict only the necessary A-even/B-odd Euclid orientation A=2uv,B=u²-v²,C=u²+v², gcd(u,v)=1, opposite parity, u>v>0. ALL original true masks remain retained: negative x/y and positive r,s,p,q, SAME Q/Qsharp infinite class, odd coprime M>N>1, common alpha, FOUR positive global integer S243 roots/common c, S251/253, corrected S267 H, SAME primitive integer Gaussian f,g + global quartic/role + actual signed W_n/W_2|n| POINT, TRUE S270 all four GOOD/critical-H TOP and ALL proper/noncritical ordinary uncapped beta. Neither the rational cover nor its boundary Q-points asserts a true physical source.

## Necessary four-factor equations
Use actual R1-239/R1-254 integer specialization. Let t=u/v, h(t)=(t²-1)²/[2t(t²+1)], z=h(t)²=B⁴/(A²C²). Let g1,g2 be the two monic irreducible degree36 factors of f17(z), and g3,g4 the two monic irreducible degree45 factors of -f19(z), in the normalized model E_z:Y²=X³+zX²-zX, Q=(1,-1), genuine f_k=psi_k(Q). For each degree d_i define
F_i(t)=Σ_{j=0}^{d_i} [z^j]g_i(z)*(t²-1)^{4j}*[2t(t²+1)]^{2(d_i-j)}.
The homogeneous original integer G_i(u,v)=v^{8d_i} F_i(u/v) MUST be a strictly positive integer square for a complete signed-18 source. Hence every such source maps into the affine Q-locus y_i²=F_i(t) for all i. The converse does NOT hold: Q-rational cover points need not have primitive integer u,v, positive factors, correct signed physical chamber, SAME gaussian, Q or S270.

## Theorem A: exact separability, disjoint branch and genus
The specialized f17,-f19 factor into four distinct irreducible monic factors over Q[z] with degrees (36,36,45,45), each with nonzero values at z=0 and z=-4. The rational map h(t) has derivative numerator (t-1)(t+1)(t⁴+6t²+1). The critical h-values away from zeros/poles satisfy the exact resultant 256*(H²+4)²; hence the only finite critical values of z=h² are z=0,-4. Because each g_i avoids 0,-4, its pullback F_i is squarefree with precisely 8d_i simple distinct complex roots. The four F_i are pairwise coprime; F_i has degree8d_i, leading coefficient1, and none is zero at infinity on P¹_t. Thus the 4 squareclasses in Q(t)*/Q(t)*² are independent, and the simultaneous cover
C18: y_1²=F_1(t),...,y_4²=F_4(t)
has degree16, Galois group (Z/2)^4, branch supports (288,288,360,360), sum1296, all inertia orders2 and no infinity ramification. By Riemann-Hurwitz:
2g(C18)-2=16*(-2)+(16/2)*1296=10336,
SO g(C18)=5169 (smooth projective normalization). The product-square quotient y²=F1 F2 F3 F4 is a hyperelliptic genus647 curve.

## Theorem B: exact 15 rational character quotients and cusps
For every nonempty subset S⊆{1,2,3,4}, the character quotient C_S:y²=∏_{i∈S}F_i(t) has genus g_S=(Σ_{i∈S}8d_i-2)/2. The 15 values are
 singleton: 143,143,179,179;
 pairs: 287 (1),323 (4),359 (1);
 triples: 467 (2),503 (2);
 all four: 647 (1).
The sum of the fifteen quotient genera is 5169. Over Q, the direct sum of pullbacks of holomorphic differentials along the 15 quotient maps spans H^0(C18,Ω^1) by distinct (Z/2)^4-character eigenspaces; consequently the induced product of quotient Jacobian pullback homomorphisms is an isogeny over Q from ∏_{S≠∅}Jac(C_S) to Jac(C18). (This is an isogeny, not a canonical product equality.)
Each F_i has monic even degree8d_i, so at infinity y_i/t^{4d_i}=±1 and C18 has exactly SIXTEEN distinct Q-rational, nonsingular infinity points. The total product quotient similarly has two rational points at infinity. Hence a strategy asserting C18(Q)=∅ or C_product(Q)=∅ is factually false; only nonboundary positive primitive t and integer-square-compatible fibres could be excluded. None of the 15 natural sign-character quotients has genus <143, so this NATURAL involution quotient menu does not directly offer genus<=4 arithmetic. This does NOT disprove other special quotient/automorphisms.

## Reproduction and scope
Exact SymPy ZZ[z] recurrence f0..f19 and factor_list confirms irreducible degrees, separability and pairwise gcd1, special-point nonzero, derivative and exact resultant, 15 genus sum. python3 r1_255_geometry.py. Evidence r1_255_geometry_evidence.json. This is an exact algebraic structural theorem relying on old necessary factor equations and classical RH/character decomposition; no finite sample extrapolation.

## Research loop and novelty
KNOWN ZERO RECREDIT: OLD S263/R1-239 true signed18 four-factor integer-square necessary receiver; OLD C122 arbitrary fixed-index Faltings qualitative finite-base; R1-241 and R1-254 all single-factor infinity Runge method; R1-253/C183 signed +18 third exclusion and first/center/−18 surviving signs; S269 and R1-228 same-source signed point/fourth-power inverse; R4 source-only reconstruction; R3 all separate genus4/S333 curves; all S270. Existing INDEX and R1 sheet do not give independent 18-cover physical credit.
NEW scoped delta: exact global four-square *simultaneous* cover geometry, 1296 branch points, genus5169, 15 explicit character quotient genera/isogeny, and 16 rational boundary points. This prevents misidentifying the old genus647 product-square quotient with the required four-square rational cover, and rules out an emptiness-only argument for either. A change from product-square to four independent squareclasses materially changes the underlying curve. This is not a new full-source exclusion, independently new Diophantine method, Faltings endpoint, signed geometry/GOOD upper, or parent credit.
LOOP_RESULT: PASS_DEPENDENT_NONLOCAL_FOURFACTOR_COVER_STRUCTURAL_AUDIT; no physical candidate removed. No re-open of old finite-S/Runge/Faltings-only paths.
BLOCKERS: Need a true affine positive primitive u/v, GLOBAL integer-square four-factor obstruction, OR one SAME primitive integer Gaussian f,g,M,N quartic+original signed indexed D_n exact W18/W36 POINT contradiction, SAME Q and S243 four roots, or strict TRUE S270 protected four-pool ordinary uncapped beta upper. Genus/isogeny alone supplies none of these. Fixed n does not cover all indices. B-even old S264 remains separate; Bwide unbridged.
REOPEN: exploit arithmetic of one or more of the 15 explicit character quotients that actually forbids ALL nonboundary *original primitive* t in a surviving original signed chamber, not Faltings qualitative finiteness; or direct original signed source H_n fourth-power/global Gaussian collision; or strict S270 fourpool upper.
NEXT: R1-09 priority remains global one-Gaussian original signed POINT/W and S270 on −18 THIRD and actual first/center phases; geometrical decomposition is a technical receiver to provide to R3 only if a concrete quotient arithmetic/rank certificate emerges. Do not launch broad high-genus rational point enumeration without an effective uniform arithmetic bound.
PERSISTENCE: If R1 owner STATE in-place replacement and final SUBMIT cannot be safely executed, retain PREPARED only and do not assert COMMITTED; record URL and update sheet only for verified artifacts.
