# StructureRadar literature ledger — search batch 18

SEARCH_TASK=SR-SEARCH-01
BATCH_ID=SR-BATCH-LITERATURE_SEARCH-18-R01
SEARCH_DATE=2026-08-19
STRUCTURES=SR-STR-155,SR-STR-156,SR-STR-157,SR-STR-158,SR-STR-159,SR-STR-160,SR-STR-175,SR-STR-176,SR-STR-177,SR-STR-178
SEARCH_BATCH_SIZE=10
NOVELTY_BY_SEARCH_ABSENCE=false
VALIDATION_RETRIGGER=exact-head controller after self-clean

## Primary-source literature checked
- Takumi Yoshida, *The relationship between face cuboids and elliptic curves* (arXiv:2407.09825). The paper defines the exact family E_{1,s}: y^2=x(x-(2s)^2)(x+(s^2-1)^2), proves the face-cuboid correspondence, records the rank-one fiber s=5/3, and proves infinitely many positive-rank specializations. It does not by itself prove the repo geometric generic-rank-zero statement or a global quantitative exceptional-fiber bound.
- Remke Kloosterman, *Chevalley-Weil formula for hypersurfaces in P^n-bundles over curves and Mordell-Weil ranks in function field towers* (arXiv:1501.05184). Gives general Mordell-Weil rank bounds under Galois base change; adjacent to SR-STR-157/158 but not an exact classification of the repo degree-two maps or commuting lifts.
- Yusuke Kimura, *F-theory models on K3 surfaces with various Mordell-Weil ranks — constructions that use quadratic base change of rational elliptic surfaces* (arXiv:1802.05195). Demonstrates Mordell-Weil rank growth under quadratic base change in elliptic K3 constructions; adjacent mechanism only, not the explicit R504 quotient calculation.
- John Cremona, Tom Fisher, Michael Stoll, *Minimisation and reduction of 2-, 3- and 4-coverings of elliptic curves* (arXiv:0908.1741). Treats degree-4 genus-one models arising in explicit descent, including the two-quadrics framework; this is a direct external carrier for the general genus-one complete-intersection species behind SR-STR-175, not for its repo packet equations or physical denominator.
- Tom Fisher, Graham Sills, *Local solubility and height bounds for coverings of elliptic curves* (arXiv:1103.4944). Gives local-solubility algorithms and height comparisons for 2-,3-,4-coverings; adjacent to SR-STR-175/178 but does not identify the repo compact physical denominator or its five-column routing.
- Tom Fisher, *Higher descents on an elliptic curve with a rational 2-torsion point* (arXiv:1509.03234). Gives higher-descent machinery tailored to rational 2-torsion, including full rational 2-torsion cases; adjacent to SR-STR-176/178, not a carrier for the repo-specific torsion-translation denominator cancellation.

## Search outcome
- SR-STR-155: keep the repo fixed-curve B^(2/5+o(1)) ceiling and moving-family quantifier firewall. Standard fixed-curve height counting does not provide constants uniform over a B-dependent Jacobi/Kummer family.
- SR-STR-156: Yoshida directly carries the E_{1,s} family, the s=5/3 positive-rank example, and infinitely many positive-rank specializations; the geometric generic-rank-zero and orbit-height sparsity assertions remain repo-specific and are not attributed to Yoshida.
- SR-STR-157/158: general base-change rank literature is adjacent, while the split/nonsplit degree-two normal forms, commuting-lift loci, and explicit R504 V4 quotient/rank-jump calculation remain repo-exact.
- SR-STR-159: the common-squarefree-core equivalence is an exact repo receiver; descent literature does not turn it into a whole-family physical-height counting theorem.
- SR-STR-160: retain the three directional quarter-power lower bounds as repo explicit-family results; no checked external theorem was promoted to the exact primitive/canonical Stage19 directional populations.
- SR-STR-175: the smooth two-quadrics genus-one structure is externally standard in explicit degree-4 descent, but existence of a rational point and uniform moving-family counting remain separate.
- SR-STR-176: rational 2-torsion descent literature is adjacent; the compact translation denominator D_T and four physical sign/orientation packets are repo-specific.
- SR-STR-177: the four-cell selector gcd matrix is an exact algebraic cancellation certificate; its automatic square cannot be recharged as a new independent saving.
- SR-STR-178: Fisher-Sills/Fisher support local covering and rational-2-torsion descent machinery, but the Euclid five-column routing and covering-specific local image conditions remain repo-specific.

## SR-STR-155 — Fixed rational-curve sub-square-root ceiling and moving-family gate
With exact physical Kummer height H_M=d=R, the M.C=4 physical rational-bisection mechanism is empty. Hence every fixed physical rational curve has M.C>=5 and contributes O(B^(2/5+o(1))); every fixed finite union is strict sub-square-root. No uniform implied constant or o(1) is proved across a B-dependent moving family, leaving the moving Jacobi/Kummer first-small-point gate unresolved.
Potential weapon types: UPPER_BOUND, GEOMETRY_ADAPTER, EXTERNAL_GATE, NO_DOUBLE_CHARGE_FIREWALL.
Applicability gaps: The per-fixed-curve B^(2/5+o(1)) estimate cannot be summed over a growing family without a new uniform theorem; no whole-family strict sub-square-root bound follows.
Transfer verdict: `FIXED_CURVE_CEILING_WITH_UNIFORMITY_FIREWALL` — fixed rational curves are strict sub-half, but no uniform moving-family summation theorem is supplied.
Arsenal decision: `ACTIVE`.

## SR-STR-156 — Yoshida face-cuboid generic-rank-zero and explicit-orbit height-sparsity gate
For E_{1,s}: y^2=x(x-(2s)^2)(x+(s^2-1)^2), with (a,b,c)=(2s,s^2-1,s^2+1), the geometric generic Mordell-Weil rank is 0. Yoshida's displayed fixed-fiber orbit at s=5/3 has h(t_n)=Theta(n^2), hence contributes only O(sqrt(log B)) indices below physical height B; the displayed positive-rank s-sequence likewise has O(sqrt(log X)) parameters of height <=X.
Potential weapon types: NO_GO_FIREWALL, HEIGHT_TOOLKIT, EXTERNAL_GATE.
Applicability gaps: Does not imply positive-rank specializations are finite or globally sparse.; Does not rule out low-degree base changes, multisections, or a quantitative exceptional-fiber theorem.; The O(sqrt(log B)) bound applies only to Yoshida's displayed fixed-fiber orbit.
Transfer verdict: `PARTIAL_DIRECT_YOSHIDA_CARRIER` — Yoshida carries the exact family and positive-rank specializations; generic-rank-zero and quantitative height-sparsity remain repo results.
Arsenal decision: `ACTIVE`.

## SR-STR-157 — Complete rational degree-two base-change descent with split/nonsplit commuting-lift loci
For target-fixed degree-two phi in Q(u), the unique deck involution is Q-rational. Up to source PGL2(Q), split maps are (A u^2+B)/(C u^2+D); nonsplit squareclass d maps are (A(u^2+d)+Bu)/(C(u^2+d)+Du). In the split stratum the reciprocal commuting-lift locus factors (AB-CD)(AB+CD)(AD+BC)=0. In the nonsplit stratum genuine commuting Q-lifts occur on BD=4dAC and D^2-B^2+4d(A^2-C^2)=0; the third candidate B^2+D^2=4d(A^2+C^2) has lift discriminant -Delta^2 and no nondegenerate Q-involutive lift.
Potential weapon types: NORMAL_FORM, DESCENT, ELLIPTIC_FIBRATION.
Applicability gaps: Classification is target-coordinate fixed and modulo source PGL2(Q), not dynamical conjugacy.; The commuting-lift loci do not classify every possible noncommuting or Prym elliptic factor.; The earlier (a u^2+b)/(u^2+1) complete-normal-form claim is explicitly superseded.
Transfer verdict: `REPO_EXACT_DEGREE_TWO_DESCENT_CLASSIFICATION` — general base-change literature does not replace the split/nonsplit PGL2 and commuting-lift classification.
Arsenal decision: `ACTIVE`.

## SR-STR-158 — Explicit nonsplit degree-two R504 rank-jump construction
For phi(u)=(u^2+4u-3)/(7-u^2), with nonsplit squareclass -6 and deck delta=-(u+7)/(u+1), the second involution epsilon=(5-u)/(u+1) gives quotient V^2=2(x^4+8x^3-64x-64) with I=3072,J=0 and Jacobian Q-isomorphic to E0:y^2=x^3-4x. The inherited and new E0 quotient differential lines are independent, so rank E_phi(Q(u))>=2.
Potential weapon types: CONSTRUCTION, ELLIPTIC_FIBRATION, BASE_CHANGE.
Applicability gaps: The rank jump alone is not a Stage19 population lower bound.; Physical-height, primitive, exactly-two and multiplicity adapters are separate; later R504 toolkit materializes one P+2R family only.
Transfer verdict: `REPO_EXPLICIT_RANK_JUMP` — quadratic-base-change rank growth is externally standard, but the R504 quotient and differential independence are repo-exact.
Arsenal decision: `ACTIVE`.

## SR-STR-159 — R505 common-squarefree-core Stage19 receiver with R506 rank-one coordinate subsumption
For A=m^2 r^2+n^2 s^2 and B=m^2 s^2+n^2 r^2, Stage19 space integrality is exactly AB square, equivalently sf(A)=sf(B), equivalently A=kP^2 and B=kQ^2 for one positive squarefree k. The common-leg coordinates u=mr,v=ns,w=ms,z=nr satisfy uv=wz and A=u^2+v^2, B=w^2+z^2, so R506 is the same rank-one toric receiver rather than an independent parameter dimension. Fixed finite core/cell elliptic slices alone do not supply a polynomial lower; the remaining R505 progress gate is a genuinely stronger whole-family physical-height theorem or a new explicit family, not an impossibility statement.
Potential weapon types: NORMAL_FORM, ROUTE_SUBSUMPTION, EXTERNAL_GATE.
Applicability gaps: The common-core receiver is not itself a construction or counting theorem.; The external gate is reopenable by genuinely new whole-family uniformity or a new explicit parametric family.
Transfer verdict: `REPO_EXACT_COMMON_CORE_RECEIVER` — descent language does not discharge the moving-core whole-family physical-height gate.
Arsenal decision: `ACTIVE`.

## SR-STR-160 — All-shared-edge directional quarter-power Stage19 lower
For each canonical shared edge j in {a,b,c}, N2,j(B) >>_j B^(1/4). R501 on 9/2<t<5 supplies canonical shared edge a, the audited R501 cone supplies b, and R502 supplies c. Hence N2,j/M2,j >>_j B^(-3/4)(log B)^(-5) and the matched Stage24 interaction J2,j >>_j B^(1/4)(log B)^(-5) -> infinity in every direction; also N2,j/N1 has the adjacent-stratum corridor B^(-3/4)(log B)^(-3) <<_j N2,j/N1 <<_epsilon B^(-1/2+epsilon)(log B)^(-3).
Potential weapon types: LOWER_BOUND, DIRECTIONAL_REFINEMENT, POPULATION_TRANSITION.
Applicability gaps: Does not improve the global N2(B) exponent above 1/4.; N2,j/N1 is a matched adjacent-stratum population-size ratio, not literal subset survival.; No strict whole-family sub-half upper or true exponent is proved.
Transfer verdict: `REPO_DIRECTIONAL_QUARTER_POWER_LOWER` — all three directional lower families remain active with no global-exponent overclaim.
Arsenal decision: `ACTIVE`.

## SR-STR-175 — Integral full-2-descent witness as a smooth intersection of two quadrics
For E_{S,X}: W^2=Z(Z-S^2)(Z+X^2), write Z=A/D^2 and Y^2=G0G1G2 with G0=A, G1=A-S^2D^2, G2=A+X^2D^2. Factoring Gi=di ui^2 gives two quadrics Q1=d0u0^2-d1u1^2-S^2D^2 and Q2=d2u2^2-d0u0^2-X^2D^2. For a nonzero fixed packet their pencil has determinant proportional to lambda*mu*(lambda-mu)*(lambda*S^2+mu*X^2), so the four singular members are distinct and the projective intersection is a smooth degree-4 genus-one curve.
Potential weapon types: FULL_2_DESCENT, GENUS_ONE.
Applicability gaps: Smooth genus one gives neither a rational point nor a uniform moving-family count.; D is not automatically the physical compact denominator.
Transfer verdict: `DIRECT_EXTERNAL_DESCENT_SPECIES_CARRIER` — degree-4 genus-one/two-quadrics descent is externally standard; repo packet equations and moving count remain separate.
Arsenal decision: `ACTIVE`.

## SR-STR-176 — Compact rational-2-torsion translation and canonical physical denominator
Translation by T0=(0,0) sends Z to -S^2X^2/Z. For a physical point this lies in (-X^2,0), and in the two-face chart D_T^2=X2^2/gcd(X2^2,U V), dividing H2-S2. The compact class lies in four sign/orientation packets. D_T is physical-point dependent and differs from generic D and least-packet D_min.
Potential weapon types: TORSION_TRANSLATION, DENOMINATOR_ADAPTER.
Applicability gaps: Requires an actual physical point.; Do not identify this translation with later j=1728 correspondences.
Transfer verdict: `RATIONAL_TWO_TORSION_ADJACENT_ONLY` — general torsion descent does not identify the repo compact physical denominator.
Arsenal decision: `ACTIVE`.

## SR-STR-177 — Dual half-angle selector cancellation with four-cell gcd matrix
For H2±S2=kappa(s^2,t^2), the two compact selectors have exact square cancellations gcd(N_-,H2-S2)=kappa k_-^2 and gcd(N_+,H2+S2)=kappa k_+^2. The four pairwise-coprime good-odd cells q_{--},q_{-+},q_{+-},q_{++} form the selector gcd matrix, and the product identity yields QK=X2/kappa. The complete matrix square is automatic.
Potential weapon types: EXACT_FACTORIZATION, GCD_MATRIX, NO_DOUBLE_CHARGE.
Applicability gaps: No independent 1/q saving may be charged from the automatic square.; Orientation and kappa must be preserved.
Transfer verdict: `REPO_EXACT_GCD_CANCELLATION` — automatic square factors are recorded only as an adapter and are not double charged.
Arsenal decision: `ACTIVE`.

## SR-STR-178 — Euclid five-column squarefree-kernel routing and local Hilbert adapter
For primitive opposite-parity m>n, support refines to m,n,m-n,m+n,m^2+n^2 with orientation-aware routing to S,X,H. The Q2 pairing uses epsilon(u)=(u-1)/2 and omega(u)=(u^2-1)/8 mod 2, but the generic Hilbert table alone does not classify the covering image.
Potential weapon types: LOCAL_DESCENT, HILBERT_SYMBOL.
Applicability gaps: Covering-specific image conditions remain necessary.; Historical column labels are not rational-coordinate variables.
Transfer verdict: `LOCAL_DESCENT_ADJACENT_WITH_IMAGE_FIREWALL` — general local-solubility/Hilbert machinery is useful, but covering-specific image conditions are still required.
Arsenal decision: `ACTIVE`.

## Firewalls
- Search absence is not a novelty claim.
- Yoshida is not credited with the repo generic-rank-zero or quantitative exceptional-fiber theorem.
- General quadratic-base-change results are not substituted for the exact R504/R505 degree-two classification or physical-height adapters.
- Degree-4 descent literature carries the genus-one/two-quadrics species, not rational solvability or uniform moving-family counts.
- Automatic gcd/square cancellations are not recharged as independent savings.
- Fixed-curve sub-half bounds are not summed over growing families without uniform constants and quantifiers.
- No perfect-cuboid existence or nonexistence claim is made.
