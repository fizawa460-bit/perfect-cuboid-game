# M3-T11-197 — Third-face shared-coordinate incidence and five elliptic factors of the fixed pair-phase cover

CARD_ID: M3-T11-197
STATUS: EXACT_THIRD_FACE_ELLIPTIC_INCIDENCE / EXPLICIT_FIXED_PAIR_PHASE_FIVE_ELLIPTIC_FACTORS / THIRD_FACE_NOT_INDEPENDENT_OF_192 / GLOBAL_GATE_OPEN
PRIMARY_GATE: M3-T11-GATE-001 OPEN
GLOBAL_COUNTING_CREDIT: 0
INDEPENDENT_HOSTILE_AUDIT: NOT_RUN

## 1. Authority and decision

Fresh MAIN, short RESULT-LEDGER, operational CARD-INDEX latest196/blank next row,196 and active ROUTE17 were checked. Needed190, BASE-002/176 INDEX summaries and bounded genus-five/five-elliptic/Jacobian searches were used for overlap. Generic full-lift genus5 is already retained in190/176/BASE-002; it receives no new credit. ONE-005 has a different fixed-source genus3 decomposition. The additions here are the fixed PAIR-PHASE chart, its five explicit rational elliptic maps and their differential proof, and the exact third-face incidence inside196's integer W chart.

197 continues196's large-Theta/Phi two-point receiver. It identifies the precise missing third-face condition when starting from the relaxed two-point locus. Once192's original W and integral n_face are retained, that elliptic condition is automatic, so it is NOT an independent selector or density saving. All original phase/intrinsic/positivity/cyclic masks remain. No new negligible sector, moving-support deficit, endpoint upper bound or closure is proved.

## 2. Fixed pair-phase complete cover

Let the ACTUAL rational pair phase be a+i b, a²+b²=1, a,b nonzero, a!=±1. Write normalized edges xi_l=e_l/R and signed diagonals eta_l=f_l/R. For pair i,j and complement k, put

z=xi_k, S=xi_i+xi_j, D=xi_i−xi_j, t=eta_k.

The smooth projective normalization C_a of the affine system is

S²=(1+a)(1−z²/a),
D²=(1−a)(1+z²/a),
t²=1−z².                                   (197.1)

The first two equations are194's exact reconstruction; the third is the missing opposite face. Conversely, on the rational open with a,b!=0, reconstruct

xi_i=(S+D)/2, xi_j=(S−D)/2,
eta_j=(a xi_j−xi_i)/b,
eta_i=b xi_j+a eta_j, xi_k=z, eta_k=t.

The equations give the sphere and all three circle squares. Impose positive edges and restore all original signed phase/cyclic masks. Primitive R=lcm(Den xi_1,Den xi_2,Den xi_3); integral diagonal squares and rationality make R*eta_l integers. This is the same primitive normalization as194/196, not a free scale. All current original U,V and receiver tests remain post-filters.

Over the algebraic closure the three square-root polynomials have disjoint branch pairs z²=a,−a,1. Their squareclasses are independent, so C_a is geometrically connected of degree8 over z. The six finite simple branch points each have ramification index2; infinity is unramified because each polynomial has even degree. Riemann–Hurwitz gives2g−2=−16+6*4=8, hence g5. The exclusions a0,±1 are exactly what keeps the branch sets disjoint. This verifies genus in the new chart; the generic genus itself is already known.

## 3. Five rational elliptic maps and Jacobian proof

Set V=(a/b)S D and Y=V t. Then

V²=a²−z⁴, Y²=(a²−z⁴)(1−z²).

Every map below is rational over Q, extends to a morphism on the smooth projective models, and is nonconstant:

| Factor | Curve equation | Image of a point on C_a |
| --- | --- | --- |
| E_SD | y²=x³−a²x | x=−z², y=z V |
| E_St | y²=((1+a)/a)x(a−x)(1−x) | x=z², y=z S t |
| E_Dt | y²=((1−a)/a)x(a+x)(1−x) | x=z², y=z D t |
| E_+ | y²=(a²−x²)(1−x) | x=z², y=Y |
| E_- | y²=(a²x²−1)(x−1) | x=1/z², y=Y/z³ |

E_SD is194's congruent-number receiver. The three pair-character quartics provide the first three elliptic factors. The triple-character even genus2 curve Y²=(a²−z⁴)(1−z²) has the last two elliptic quotients. At z0 the last displayed affine formula has a pole; its map extends on the projective curve.

All five curves are nonsingular and have full rational2-torsion. Their cubic branch triples are respectively {0,±a}, {0,a,1}, {0,−a,1}, {−a,a,1}, {−1/a,1/a,1}. Leading coefficients are nonzero; rational scaling gives monic Weierstrass models if required. Their points at infinity are rational.

The isogeny is proved explicitly rather than inferred from the number of maps. The pullbacks of invariant elliptic differentials are nonzero constants times

dz/(S D), dz/(S t), dz/(D t),
z dz/(S D t), dz/(S D t).                    (197.2)

The first three have different sign characters under the independent sign changes of S,D,t. The last two share the triple character but are independent since1,z are independent rational functions. All five forms are regular: the first three descend from smooth genus1 quartics, and the last two from the two standard genus2 differentials. Thus they form a basis of the five-dimensional differential space of C_a. The morphisms induce a homomorphism on Jacobians whose differential has full rank; in characteristic0 and equal dimension it is an isogeny. Therefore

Jac(C_a) ~_Q E_SD × E_St × E_Dt × E_+ × E_-. (197.3)

Primary methodological check: Reyes-Carocca and Rodríguez, “A generalisation of Kani-Rosen decomposition theorem for Jacobian varieties”, arXiv:1702.00484v2, introduction/Theorem C and Theorem1, gives the quotient-Jacobian decomposition framework. Source https://arxiv.org/pdf/1702.00484 . The five maps and the complete differential rank argument above are this card's deduction; the paper does not prove this Stage37-specific family or its counting bound. No unverified admissibility claim is needed for our explicit differential proof.

## 4. Shared-coordinate third-face incidence in196

Use196's integer pair parameter Theta=kappa*q, divisor Phi and negative point on E_Theta. Write

U=(Phi e_k/R)²=−X_minus>0.

The third face adds a point on the full-2-torsion curve

F_Theta,Phi: V3²=(U²−Theta²)(U−Phi²),
V3=Phi³ T f_k/R³, T=e_i f_i+e_j f_j.         (197.4)

This is E_+ above under x->Phi²x, y->Phi³y (V3 uses the opposite sign of the table's Y), because a=Theta/Phi². Its rational2-torsion roots are−Theta,+Theta,Phi². They are distinct on physical points: Theta!=0 and |Theta|<Phi², the latter from b!=0. Its coefficient/point heights are polynomial in B.

From196, Y_minus²=U(Theta²−U²) and U is a nonzero rational square. On the physical open T!=0, Theta²−U² is also a nonzero rational square. Therefore existence of rational V3 at this SAME U is equivalent to

Phi²−U being a rational square,
equivalently1−(e_k/R)² being a rational square. (197.5)

This is exactly the third-face condition. It is not the existence of an arbitrary rational point on F_Theta,Phi. The same-coordinate restriction is essential. T=0 would force S*D=0 by b*T/R²=−a*S*D; S=0 contradicts positive edges, D=0 forces equal edges and nonintegral positive third face, so original endpoints exclude this exception.

Thus a relaxed196 two-point state can fail the third face, while a physical endpoint supplies the F point. For fixed Theta and Phi the F curve has full rational2-torsion and the retained uniform count applies, but its point is evaluated at U already fixed by the negative point. Counting it independently or multiplying elliptic sparsities is not valid.

## 5. Exact integer W transport: why this selector is already paid

Retain192/196's integer variables, including integral n_face with A²+F²=n_face² and

W²=L²−n_face²D0²,
B_T=D0(epsilon1 A L1+epsilon2 F L2),
G=kappa*H², Phi=L/H, Theta=kappa*B_Q/G.

The196 identities give

U=W²/H²,
Theta²−U²=B_T²/H⁴,
Phi²−U=n_face²D0²/H².

Consequently the197 shared-coordinate point is automatically

V3=B_T*n_face*D0/H³.                         (197.6)

Every quantity is rational and uses the SAME integer W and normalization H, not an independent face sign or scale. Equations(197.4)–(197.6) are exact. Once192's integer n_face/W and original branch are imposed, asking for this third elliptic point supplies no new arithmetic restriction. If n_face²=A²+F² is retained only as a numeric integer while n_face itself is irrational, the squared identity still holds but V3 need not be rational; that is the partial-sphere over-cover used in verification, not a full endpoint.

This is the precise obstruction to using the added elliptic factor as a second density gain. The five quotients share z and the original cover; their point counts are not independent. Complete elliptic splitting of the Jacobian also does not make the genus5 curve a product parameterization.

## 6. Counting consequence and scope

Fixed actual pair phase already has ALL-content B^{o(1)} physical multiplicity by194. The new cover gives an explicit complete chart and quotient adapter for that same measure. Its five torsion elliptic factors have polynomial model/point heights after rational denominator clearing, but the single E_SD projection already has bounded cover degree and supplies the existing fixed-phase upper bound. No improved exponent comes from multiplying five subpower counts. Fixed Theta/Phi statements, old small-Phi/Theta sectors and177/180 fixed-content depth compression are not re-charged.

The current missing theorem remains a moving LARGE-Theta/Phi occupied-support estimate on the diagonal shared-coordinate incidence with all192 and original U,V,N_T/Den(S) masks. Neither genus5/finiteness nor the Q-isogeny(197.3) supplies that average. K=1 large-s/unshared conductor and K>1/large-c low-median averaging remain OPEN.

## 7. Verification and next handoff

verify_m3_t11_197.py and M3-T11-197-verification.json PASS:2688 nondegenerate full-cover finite-field points over17,41,73, giving13440 checks of the five elliptic maps;28 rational partial-sphere third-face equivalence checks;84 scaled integer W/H identities; differential sign-character orthogonality checked exactly. None of the28 partial-sphere examples passes the third face. Finite-field points and partial spheres are not positive rational endpoints; physical endpoints checked0. Finite tests verify identities, not the genus/isogeny proof or moving count. Independent audit not run.

LATEST197; NEXT198. Retain196 shared signed collision and same-curve W incidence,195 all-content Phi sum,194 phase fiber,193 T0 tail,192 original W and all masks,180/174 filters,134 fresh D-only. Gate OPEN/global credit0; audit162–185 scope unchanged;186–197 independent audit not run; TI parked120/retracted147–149/frozen.

NEXT198 should use the explicit complete pair-phase cover and its SAME-coordinate third-face incidence to formulate/prove a summed diagonal occupancy theorem in the large-Theta/Phi residual. Any new selector must not be algebraically implied by192 W+integer n_face, or by(197.6); demonstrate its actual extra content and pay moving coefficient costs. One may use the five explicit maps to transport a valid theorem, but fixed elliptic fibers, quotient independence or the Jacobian isogeny alone are insufficient. No old sector re-charge and no independent density product. Detailed proofs remain in this card; MAIN/INDEX/short LEDGER point to197/NEXT198.

## 8. Artifact IDs

SCRIPT=1j9Wk8y1VxvGNDrYNQO79cXkU0vk-3BWs
JSON=1XK0gAwt_CKcn8vVs5OsCcgXnBra36hx-
Both are in Stage37 verification research auxiliaries; this card is in the research-card folder.
