# Stage14 Arsenal / Weapon Registry

**Registry version:** `STAGE14-ARSENAL-20260813-R02`

**Authority:** this Markdown file is the human-authoritative registry.
**Seed:** Stage14 final self-contained R04, frozen source/provenance ledgers, buried-gold inventory, final route matrix, external-theorem contracts, and the Stage15-0 reuse matrix. Targeted source inspection then covered X13, column/root-line/common-gcd precursors, q17/MAIN/T/S endpoints, Stage13 projection machinery, and the final accounting chain.

This is a toolbox, not a chronology and not a Stage14 continuation. Similar formulas are not interchangeable unless population, cutoff, charged measure, quantifier order, direction, primitive/canonical mask, and post-filters agree. `B^o(1)` below means multiplicity/equivalence unless an entry explicitly says otherwise; it is never a fixed-power saving.

## Invocation protocol

1. Search `docs/stage14-arsenal-index.md` by obstruction shape.
2. Read the candidate entry here and its dependencies.
3. Open only the canonical source named by the entry.
4. Match input shape, physical population, cutoff, measure, quantifiers, and masks.
5. Use `DIRECT_REUSE` only on an exact match. Otherwise prove an exact adapter, retain `SAME_KERNEL_DIFFERENT_MEASURE`, or reject promotion.

## Registry

### AR-001 — Primitive/canonical physical convention

- **CATEGORY:** exact algebra / population contract
- **ONE-LINE PURPOSE:** Deduplicate scale and permutation orbits before any arithmetic count.
- **INPUT SHAPE:** Positive integer edge triples, with a declared height/cutoff and face-square predicates.
- **OUTPUT:** The representative `0<a<b<c`, `gcd(a,b,c)=1`, with exactly-one/two/three face populations kept separate.
- **HYPOTHESES:** Scaling and edge permutation preserve the underlying object; any orientation multiplicity is handled explicitly.
- **PHYSICAL DEPENDENCE:** The convention itself is independent of space-diagonal integrality; Stage14's population additionally imposed integral `d`.
- **MEASURE:** Whole declared physical family after canonical projection.
- **QUANTIFIERS:** Pointwise exact normalization.
- **LOSS / COST:** None; orientation factors must be recorded, not absorbed into `B^o(1)`.
- **REUSE CLASS:** `DIRECT_REUSE`
- **TRIGGER SIGNATURE:** A new count mixes scaled copies, edge permutations, or exactly-two with triple-face objects.
- **FAILURE CONDITIONS:** Do not identify oriented records with canonical objects without a projection-fiber proof.
- **SOURCE:** `stages/stage14/final.md`, Sections 1.1–1.4; `stages/stage15/README.md`, Stage15-0 contract.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `ACTIVE`
- **DEPENDENCIES:** None.
- **KNOWN APPLICATION:** Stage14 physical `N_2(B)` and Stage15 `A_2(B) subset B_2(B)`.
- **POSSIBLE FUTURE USE:** Default normalization for any later face-integrality population.

### AR-002 — Primitive Euclid face decomposition

- **CATEGORY:** exact algebra / parametrization
- **ONE-LINE PURPOSE:** Replace an integral right-triangle face by a unique scale-times-primitive Euclid certificate.
- **INPUT SHAPE:** Positive integers `(e,x,u)` with `e^2+x^2=u^2` and a distinguished leg/orientation.
- **OUTPUT:** Primitive opposite-parity Euclid parameters plus a positive scale, unique after the stated orientation convention.
- **HYPOTHESES:** Exact square identity; parity and leg orientation fixed.
- **PHYSICAL DEPENDENCE:** Independent of integral space diagonal and of the third face.
- **MEASURE:** One-face certificate fiber.
- **QUANTIFIERS:** Pointwise exact.
- **LOSS / COST:** None.
- **REUSE CLASS:** `DIRECT_REUSE`
- **TRIGGER SIGNATURE:** A face-square condition appears and a primitive parameter pair is needed.
- **FAILURE CONDITIONS:** Do not forget the scale, swap the distinguished leg silently, or assume global cuboid primitivity from face primitivity.
- **SOURCE:** `stages/stage14/final.md`, Lemma 3.1 proof; `stages/stage13/final.md`, Sections 3.18–3.20 and 8.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `BACKGROUND`
- **DEPENDENCIES:** AR-001.
- **KNOWN APPLICATION:** Two-face gluing and the Stage12→13 projection bridge.
- **POSSIBLE FUTURE USE:** Stage15 ambient shared-edge normal forms and certificate validation.

### AR-003 — Exact two-face gluing and multiplicity one

- **CATEGORY:** exact algebra / reconstruction
- **ONE-LINE PURPOSE:** Glue two primitive oriented Pythagorean faces along a common leg without hidden scale multiplicity.
- **INPUT SHAPE:** `F_i=(S_i,X_i,H_i)`, a common physical edge, `k_1S_1=k_2S_2`, and global primitive canonical output.
- **OUTPUT:** With `g=gcd(S_1,S_2)`, `k_1=tS_2/g`, `k_2=tS_1/g`; the minimal glued triple is primitive, so global primitivity forces `t=1`.
- **HYPOTHESES:** Primitive face data (`gcd(S_i,X_i)=1`), distinguished shared edge, positivity, canonical ordering, global `gcd=1`.
- **PHYSICAL DEPENDENCE:** Independent of space-diagonal integrality as an algebraic gluing lemma; exact-two gives one shared edge and triple-face gives three.
- **MEASURE:** Raw shared-edge incidence measure.
- **QUANTIFIERS:** Pointwise exact.
- **LOSS / COST:** None.
- **REUSE CLASS:** `DIRECT_REUSE`
- **TRIGGER SIGNATURE:** Two face certificates share a leg and generator multiplicity must be proved.
- **FAILURE CONDITIONS:** Do not fold triple-face objects into exactly-two or omit orientation/swap conventions.
- **SOURCE:** `stages/stage14/final.md`, Lemma 3.1; `stages/stage14/archive/stage14-4ag-kummer-rank-jump.md`; `stages/stage15/README.md`, “Inclusion and multiplicity”.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `ACTIVE`
- **DEPENDENCIES:** AR-001, AR-002.
- **KNOWN APPLICATION:** Stage14 graph simplicity; Stage15 paired enumerator.
- **POSSIBLE FUTURE USE:** Any overlap graph built from two certified faces.

### AR-004 — Raw-pair incidence graph identity

- **CATEGORY:** counting / incidence geometry
- **ONE-LINE PURPOSE:** Convert exactly-two overlap counting into vertices times a uniform fiber degree.
- **INPUT SHAPE:** Physical integral-space-diagonal cuboids and primitive oriented face vertices; edges are raw unordered integral-face pairs.
- **OUTPUT:** `E(B)=N_2(B)+3T(B)=1/2 sum_F deg_B(F)` and `N_2(B)<=E(B)`.
- **HYPOTHESES:** AR-003 multiplicity one; exactly-two/triple separation; Stage14 cutoff `d<=B`.
- **PHYSICAL DEPENDENCE:** Primitive/canonical, integral space diagonal, whole family; triple objects retained.
- **MEASURE:** Whole Stage14 physical raw-incidence graph.
- **QUANTIFIERS:** Exact whole-family identity.
- **LOSS / COST:** None.
- **REUSE CLASS:** `STAGE14_SPACE_DIAGONAL_ONLY`
- **TRIGGER SIGNATURE:** Overlap objects can be represented as pairs of one-face records and vertex degrees may be controlled.
- **FAILURE CONDITIONS:** Not automatically an ambient Stage15 `B_2` theorem; rebuild the graph and degree model there.
- **SOURCE:** `stages/stage14/final.md`, Lemma 3.1; `stages/stage14/archive/stage14-4ag-kummer-rank-jump.md`.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `ACTIVE`
- **DEPENDENCIES:** AR-003.
- **KNOWN APPLICATION:** First step of the Stage14 square-root proof.
- **POSSIBLE FUTURE USE:** `A_2`-side overlap bounds or another family after a fresh graph statement.

### AR-005 — Uniform elliptic-fiber degree bridge

- **CATEGORY:** external theorem interface / finite fiber
- **ONE-LINE PURPOSE:** Bound every active graph vertex degree by `B^o(1)` uniformly.
- **INPUT SHAPE:** Stage14 fiber `E_t:Y^2=X(X-1)(X+t^2)`, rational exact 2-torsion, and physical/model point heights `B^O(1)` uniformly in the base face.
- **OUTPUT:** `max_F deg_B(F) <= exp(O(log B/log log B))=B^o(1)` and `E(B)<<V(B)B^o(1)`.
- **HYPOTHESES:** Base field `Q`; nonsingular physical specialization; explicit `t=2r/(1-r^2)`, `r=X_1/(H_1+S_1)`; fixed-degree birational maps; Dujella's theorem contract.
- **PHYSICAL DEPENDENCE:** Integral space diagonal and the Stage14 height comparison are essential; physical masks only delete points.
- **MEASURE:** Vertex/fiber measure, uniformly maximized before summing the whole graph.
- **QUANTIFIERS:** Pointwise in every active fiber, then whole-family promotion.
- **LOSS / COST:** `B^o(1)` multiplicity only; no fixed-power saving.
- **REUSE CLASS:** `STAGE14_SPACE_DIAGONAL_ONLY`
- **TRIGGER SIGNATURE:** An incidence graph has genus-one/elliptic degree fibers with uniform torsion and polynomial heights.
- **FAILURE CONDITIONS:** Never extrapolate a fixed curve to a family without uniform model and point heights; forbidden for Stage15 ambient `B_2` as currently formulated.
- **SOURCE:** `stages/stage14/final.md`, Lemma 3.2 and Section 8; `stages/stage14/archive/stage14-4ag-kummer-rank-jump.md`.
- **SOURCE CONFIDENCE:** `EXTERNAL_THEOREM_DEPENDENT`
- **STATUS:** `ACTIVE`
- **DEPENDENCIES:** AR-004.
- **KNOWN APPLICATION:** Stage14 `E(B)<<V(B)B^o(1)`.
- **POSSIBLE FUTURE USE:** Only after a new family's uniform elliptic model and height adapter are proved.

### AR-006 — Stage14 physical whole-family square-root theorem

- **CATEGORY:** counting theorem
- **ONE-LINE PURPOSE:** Bound primitive canonical exactly-two cuboids with integral space diagonal.
- **INPUT SHAPE:** `0<a<b<c`, `gcd(a,b,c)=1`, integer `d`, `a^2+b^2+c^2=d^2<=B^2`, exactly two integral face diagonals.
- **OUTPUT:** `N_2(B)<<B^(1/2+o(1))`.
- **HYPOTHESES:** Full R04 proof chain AR-003–AR-016; same cutoff and physical masks.
- **PHYSICAL DEPENDENCE:** Entirely Stage14 with integral space diagonal, whole-family, not fixed direction/cell/U.
- **MEASURE:** Whole physical `A_2` family.
- **QUANTIFIERS:** For every epsilon, all sufficiently large `B`; every physical chamber.
- **LOSS / COST:** `B^o(1)` only above exponent `1/2`.
- **REUSE CLASS:** `STAGE14_SPACE_DIAGONAL_ONLY`
- **TRIGGER SIGNATURE:** A later argument needs a certified upper bound on the `A_2` numerator.
- **FAILURE CONDITIONS:** Says nothing directly about Stage15 ambient `M_2`, a lower bound, a strict sub-square-root saving, or perfect-cuboid existence.
- **SOURCE:** `stages/stage14/final.md`, Theorem 2.1 and Proposition 3.6; `stages/stage14/archive/tasks/14-X13/result.md`.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `ACTIVE`
- **DEPENDENCIES:** AR-003–AR-016.
- **KNOWN APPLICATION:** Final Stage14 theorem; Stage15 numerator context.
- **POSSIBLE FUTURE USE:** Upper-bound numerator in matched A/B comparisons only.

### AR-007 — Balanced Cayley/Gaussian packet normal form

- **CATEGORY:** exact algebra / counting geometry
- **ONE-LINE PURPOSE:** Cover every active Stage14 face by a finite-decorated strip with explicit host exponents.
- **INPUT SHAPE:** Stage14 two-face integral-space-diagonal parametrization after Cayley/Gaussian transforms, gcd peels, signs, 2-primary data, and dyadic localization.
- **OUTPUT:** Feasible `(theta,phi,chi)` strip, `chi=2theta+2phi-3/4`, hosts `E_s<=max(2theta,1-2theta)`, `E_k<=3theta-1/4`, proportional/nonproportional split.
- **HYPOTHESES:** All original root/allocation/cell masks and charged-once quantifier order retained.
- **PHYSICAL DEPENDENCE:** Integral space diagonal, particular Stage14 parameter system, every decorated physical cell.
- **MEASURE:** Whole family partitioned into retained dyadic cells.
- **QUANTIFIERS:** Every retained cell; not an average.
- **LOSS / COST:** `B^o(1)` cell/decorations multiplicity.
- **REUSE CLASS:** `STAGE14_SPACE_DIAGONAL_ONLY`
- **TRIGGER SIGNATURE:** A future normal form reproduces the same balanced coefficient factorization and hosts exactly.
- **FAILURE CONDITIONS:** Similar exponent symbols or Cayley formulas are insufficient; prove a map preserving population, cutoff, masks, and measure.
- **SOURCE:** `stages/stage14/final.md`, Proposition 3.3; `stages/stage14/archive/tasks/14-X13/result.md`, Sections 1–2.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `ACTIVE`
- **DEPENDENCIES:** AR-001–AR-003.
- **KNOWN APPLICATION:** Stage14 whole-strip case split.
- **POSSIBLE FUTURE USE:** Candidate only after Stage15-4/5 supplies an exact ambient-to-square-condition normal form.

### AR-008 — Common-core/lost-core decomposition and high-core emptiness

- **CATEGORY:** exact algebra / counting
- **ONE-LINE PURPOSE:** Isolate a charged common core and prove nonproportional fixed-power cells with `chi>1/4` empty.
- **INPUT SHAPE:** AR-007 nonproportional packet with Cayley core, residual core, cross-root data, and endpoint forms `L_-,L_+`.
- **OUTPUT:** Good/bad core separation, `D_0|h_-h_+`, endpoint bound, hence `chi<=1/4` on surviving fixed-power cells.
- **HYPOTHESES:** Coprimalities `(J,H)=1`, exact divisibilities, positive nonproportional branch, all small factors only `B^o(1)`.
- **PHYSICAL DEPENDENCE:** Stage14 balanced packet with integral space diagonal.
- **MEASURE:** One retained nonproportional cell, promoted because AR-007 covers all cells.
- **QUANTIFIERS:** Every retained cell.
- **LOSS / COST:** Common core charged once; endpoint/divisor decorations `B^o(1)`.
- **REUSE CLASS:** `STAGE14_SPACE_DIAGONAL_ONLY`
- **TRIGGER SIGNATURE:** A common modulus/core also divides an endpoint product and may be too large for the available short support.
- **FAILURE CONDITIONS:** Do not import the `1/4` threshold without the exact endpoint bound and coprimality chain.
- **SOURCE:** `stages/stage14/final.md`, Proposition 3.3; `stages/stage14/archive/tasks/14-4cy/result.md`, Sections 1–3; upstream `Stage14-4cx` as cited there.
- **SOURCE CONFIDENCE:** `PROVED_BUT_SOURCE_FRAGMENTED`
- **STATUS:** `CONSUMED`
- **DEPENDENCIES:** AR-007, AR-028.
- **KNOWN APPLICATION:** Removed high-core Stage14 packets before X13.
- **POSSIBLE FUTURE USE:** Abstract lost-core obstruction after an exact adapter.

### AR-009 — Primitive Gaussian root-line lattice count

- **CATEGORY:** exact algebra / counting / Gaussian
- **ONE-LINE PURPOSE:** Count primitive pairs on quadratic CRT root lines without the crude boundary loss.
- **INPUT SHAPE:** `C_0|a_0^2U^2+b_0^2V^2`, `gcd(C_0,a_0b_0UV)=1`, `gcd(U,V)=1`, dyadic `U~U_0`, `V~V_0`.
- **OUTPUT:** At most `2^omega(C_0)=B^o(1)` lines `U=rho V mod C_0`; each line has `<=1+6U_0V_0/C_0` primitive points.
- **HYPOTHESES:** Odd solvable modulus (hence prime factors `1 mod 4`), unit coefficients, primitive pair, fixed CRT orientation.
- **PHYSICAL DEPENDENCE:** The lemma itself is abstract; Stage14 application used its common-core agreement-pair measure.
- **MEASURE:** Fixed residual/quotient data, counting one primitive-pair fiber.
- **QUANTIFIERS:** Pointwise for each modulus/root line and dyadic box.
- **LOSS / COST:** `B^o(1)` root orientations; the displayed density is a true modulus spacing, not a free global saving.
- **REUSE CLASS:** `REUSE_AFTER_EXACT_ADAPTER`
- **TRIGGER SIGNATURE:** A primitive pair satisfies a unit sum-of-two-squares congruence modulo a common core.
- **FAILURE CONDITIONS:** Without primitivity the determinant can vanish along multiples and the boundary term returns; do not cross-promote from fixed residual data to a whole family silently.
- **SOURCE:** `stages/stage14/archive/tasks/14-s7-29/result.md`, Sections 2–5; `stages/stage14/final.md`, Lemma 3.4.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `SUPERSEDED_BUT_REUSABLE`
- **DEPENDENCIES:** AR-016, AR-028.
- **KNOWN APPLICATION:** Cancelled the Stage14 common-core exponent and yielded the historical `3/4` bound.
- **POSSIBLE FUTURE USE:** Stage15-4 squareclass congruence if its ambient variables produce this exact primitive root-line shape.

### AR-010 — Primitive-ratio rigidity and one-pair reconstruction

- **CATEGORY:** exact algebra / reconstruction
- **ONE-LINE PURPOSE:** Show one primitive agreement pair determines the opposite agreement product and moving root product up to divisor-many fibers.
- **INPUT SHAPE:** The two exact reciprocal quadratic equations, fixed residual/quotient/small-decoration data, and coprime agreement pairs.
- **OUTPUT:** No free ratio scale; opposite agreement split, `X*Y`, and switch products are reconstructed with `B^o(1)` multiplicity.
- **HYPOTHESES:** Both original reciprocal equations retained, not only their product; primitive modulus pairs and physical divisibility masks.
- **PHYSICAL DEPENDENCE:** Stage14 reciprocal packet; fixed residual data.
- **MEASURE:** One primitive agreement-pair fiber.
- **QUANTIFIERS:** Pointwise after outer data are fixed.
- **LOSS / COST:** Divisor-many `B^o(1)` multiplicity; no saving by itself.
- **REUSE CLASS:** `REUSE_AFTER_EXACT_ADAPTER`
- **TRIGGER SIGNATURE:** A generic genus-one curve appears only because a moving coefficient was frozen too early.
- **FAILURE CONDITIONS:** Do not freeze `X*Y` as independent if the original equations reconstruct it; do not promote fixed-fiber multiplicity globally without counting the outer pair.
- **SOURCE:** `stages/stage14/archive/tasks/14-s7-28/result.md`, Sections 5–9.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `SUPERSEDED_BUT_REUSABLE`
- **DEPENDENCIES:** AR-016, AR-028.
- **KNOWN APPLICATION:** Replaced a nonminimal genus-one receiver by a primitive binary-quadratic divisor problem.
- **POSSIBLE FUTURE USE:** Simplify Stage15 square-condition coefficient spaces after the exact normal form exists.

### AR-011 — Endpoint-linear column reconstruction

- **CATEGORY:** reconstruction / counting
- **ONE-LINE PURPOSE:** Reconstruct the column variable `M` from reduced endpoint forms with a quantified short support.
- **INPUT SHAPE:** Fixed common-core data and legal sign allocation; `L_-=J_{L-}h_-`, `L_+=J_{L+}h_+`, with the Stage14 endpoint determinant identities.
- **OUTPUT:** `(z_1,z_2)` and `M` reconstructed up to divisor-many ambiguity; low-core column cost `B^(1/4-chi+o(1))`.
- **HYPOTHESES:** Nonproportional positive branch, exact endpoint linear system, lost/cross-root peels, fixed decorations.
- **PHYSICAL DEPENDENCE:** Stage14 balanced integral-space-diagonal packet and one column allocation.
- **MEASURE:** Fixed `(C,U,V)` cell/column fiber.
- **QUANTIFIERS:** Every surviving low-core cell.
- **LOSS / COST:** Fixed-power column support `1/4-chi`; remaining ambiguity `B^o(1)`.
- **REUSE CLASS:** `REUSE_AFTER_EXACT_ADAPTER`
- **TRIGGER SIGNATURE:** Two endpoint sum/difference forms determine two latent variables and a product/numerator.
- **FAILURE CONDITIONS:** Do not use the exponent outside its exact strip or omit determinant nonzero/positivity conditions.
- **SOURCE:** `stages/stage14/archive/tasks/14-4cy/result.md`; `stages/stage14/archive/tasks/14-X13/result.md`, Section 2; R04 Proposition 3.3/Lemma 3.4.
- **SOURCE CONFIDENCE:** `PROVED_BUT_SOURCE_FRAGMENTED`
- **STATUS:** `CONSUMED`
- **DEPENDENCIES:** AR-007, AR-008.
- **KNOWN APPLICATION:** Supplied `M` before X13 reverse reconstruction.
- **POSSIBLE FUTURE USE:** Any later support reconstruction with the same endpoint determinant pattern.

### AR-012 — X13 reverse reciprocal divisor reconstruction

- **CATEGORY:** reconstruction / exact algebra
- **ONE-LINE PURPOSE:** Reverse two coupled difference-of-squares equations so a fixed `(U,V,M)` has only divisor-many completions.
- **INPUT SHAPE:** `M` fixes `XY`; positive equations `(cp-dq)(cp+dq)=W_2` and `(aU-bV)(aU+bV)=W_1`, with fixed decorations and polynomially bounded positive integers.
- **OUTPUT:** `fixed (U,V,M) => #(a,b,c,d,p,q), #N = B^o(1)`.
- **HYPOTHESES:** Exact reciprocal identities, positivity (`cp>dq>0`, `aU>bV>0`), parity/divisibility/coprimality retained as filters, all integers `B^O(1)`.
- **PHYSICAL DEPENDENCE:** Stage14 application is integral-space-diagonal, nonproportional low-core and fixed column; abstract factorization lemma is broader.
- **MEASURE:** Post-column fixed `(U,V,M)` completion fiber.
- **QUANTIFIERS:** Pointwise for every fixed outer triple.
- **LOSS / COST:** Divisor-many `B^o(1)` multiplicity only.
- **REUSE CLASS:** `REUSE_AFTER_EXACT_ADAPTER`
- **TRIGGER SIGNATURE:** Two reciprocal variables are fixed in sequence and both equations factor as signed differences of squares.
- **FAILURE CONDITIONS:** No positivity, no fixed right-hand side, super-polynomial integers, or lost reciprocal coupling; `B^o(1)` is not a fixed-power saving.
- **SOURCE:** `stages/stage14/archive/tasks/14-X13/result.md`, Sections 3–5; `stages/stage14/final.md`, Lemma 3.5.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `ACTIVE`
- **DEPENDENCIES:** AR-010, AR-011, AR-016.
- **KNOWN APPLICATION:** Eliminated the last Stage14 row-support power and closed exponent `1/2`.
- **POSSIBLE FUTURE USE:** High-priority Stage15-4/5 candidate if the third square produces two fixed reciprocal factorizations.

### AR-013 — Row CRT lift is a post-reconstruction filter

- **CATEGORY:** proof accounting / reconstruction
- **ONE-LINE PURPOSE:** Prevent charging a CRT row variable that exact reciprocal reconstruction has already reduced to `B^o(1)` candidates.
- **INPUT SHAPE:** AR-012 has fixed divisor-many `N`; row congruences `N=M mod C_-`, `N=-M mod C_+` are applied afterward.
- **OUTPUT:** `ROW_CRT_LIFT_INDEPENDENT_SUPPORT=false`; congruences only reject candidates.
- **HYPOTHESES:** Quantifier order is column→`M`→reverse reconstruction→CRT filter; no omitted independent row variable.
- **PHYSICAL DEPENDENCE:** Stage14 application; principle is generic.
- **MEASURE:** Same fixed `(U,V,M)` fiber as AR-012.
- **QUANTIFIERS:** Pointwise post-reconstruction.
- **LOSS / COST:** No new fixed-power cost; at most `B^o(1)` candidates survive.
- **REUSE CLASS:** `REUSE_AFTER_EXACT_ADAPTER`
- **TRIGGER SIGNATURE:** A CRT lift is counted after an exact equality already reconstructs its lifted variable.
- **FAILURE CONDITIONS:** If CRT variables precede reconstruction or range independently, the lift may be real support.
- **SOURCE:** `stages/stage14/archive/tasks/14-X13/result.md`, Section 6; `stages/stage14/final.md`, Lemma 3.5 and buried-gold BG-07.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `ACTIVE`
- **DEPENDENCIES:** AR-012, AR-028.
- **KNOWN APPLICATION:** Removed the duplicate `1/4-chi` row cost.
- **POSSIBLE FUTURE USE:** Audit Stage15 support counts after a third-square CRT normal form.

### AR-014 — Fixed-outer common-gcd square-divisor adapter

- **CATEGORY:** gcd / valuation / counting
- **ONE-LINE PURPOSE:** Replace a crude free `sqrt(M)` common-gcd sum by divisor-many choices from already-fixed outer data.
- **INPUT SHAPE:** A pair `(x,y)` satisfying a quadratic root congruence modulo `Q`, with `oddpart(gcd(x,y))^2|W` and fixed `W`.
- **OUTPUT:** Nonprimitive root-pair count `<<B^o(1)(1+M/Q)`; admissible gcds are divisor-many.
- **HYPOTHESES:** The square-divisor lock is proved before counting `(x,y)`; polynomially bounded `W`; primitive reduction and 2-primary accounting.
- **PHYSICAL DEPENDENCE:** Abstract lemma is reusable; Stage14 derived `W=C u_res` from physical root structure.
- **MEASURE:** Fixed outer `(Q,W)` root-pair fiber.
- **QUANTIFIERS:** Pointwise in fixed outer data.
- **LOSS / COST:** `B^o(1)` gcd choices; removes a spurious square-root multiplicity but is not a global saving without the outer count.
- **REUSE CLASS:** `REUSE_AFTER_EXACT_ADAPTER`
- **TRIGGER SIGNATURE:** A nonprimitive quadratic-congruence count contains a `sqrt(M)` term and its common gcd may square-divide fixed data.
- **FAILURE CONDITIONS:** Do not use if only `h|W` (not `h^2|W`) or if `W` is not fixed first.
- **SOURCE:** `stages/stage14/archive/tasks/14-s7-31/result.md`, Sections 3–6.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `SUPERSEDED_BUT_REUSABLE`
- **DEPENDENCIES:** AR-009, AR-016, AR-028.
- **KNOWN APPLICATION:** Removed the historical common-gcd loss and produced the `5/8` bound.
- **POSSIBLE FUTURE USE:** Third-square valuation/gcd decompositions in Stage15.

### AR-015 — Proportional four-cell root-gcd transfer

- **CATEGORY:** gcd / branch decomposition
- **ONE-LINE PURPOSE:** Control the proportional branch by separating pairwise-coprime same-side and cross-side root gcds.
- **INPUT SHAPE:** Proportional Stage14 packet with four root-gcd cells, `(K,H)=1`, `kappa+eta=1/8`, and common residual norms.
- **OUTPUT:** Same-side `K` is coprime to the xi norm/core and `K^2|u_res`; proportional exponent `<=7/16`.
- **HYPOTHESES:** Exact four-cell decomposition, Gaussian descent, proportional hard scale, Stage14 residual bounds.
- **PHYSICAL DEPENDENCE:** Particular Stage14 proportional integral-space-diagonal branch.
- **MEASURE:** Every proportional retained cell.
- **QUANTIFIERS:** Pointwise cell identities and whole proportional-branch bound.
- **LOSS / COST:** `B^o(1)` decorations; fixed exponent `7/16` only in the Stage14 strip.
- **REUSE CLASS:** `REUSE_AFTER_EXACT_ADAPTER`
- **TRIGGER SIGNATURE:** A proportional branch contains same-side/cross-side gcd cells and a square may be forced into a residual norm.
- **FAILURE CONDITIONS:** Do not reuse the `7/16` exponent without the same strip; do not conflate same-side and cross-side primes.
- **SOURCE:** `stages/stage14/archive/tasks/14-s7-37/result.md`, Sections 1–4; `stages/stage14/final.md`, Proposition 3.3.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `SUPERSEDED_BUT_REUSABLE`
- **DEPENDENCIES:** AR-007, AR-014.
- **KNOWN APPLICATION:** Made the Stage14 proportional branch strictly sub-square-root.
- **POSSIBLE FUTURE USE:** Branch-specific Stage15 squareclass/gcd normalization after exact identification.

### AR-016 — Polynomially bounded divisor/finite-fiber adapter

- **CATEGORY:** counting / finite multiplicity
- **ONE-LINE PURPOSE:** Preserve polynomial exponents across exact reconstructions with divisor-many fibers.
- **INPUT SHAPE:** A fixed nonzero positive integer `n<=B^C`, or a fixed-degree map with uniformly bounded finite fibers.
- **OUTPUT:** `tau(n)=B^o(1)` factor pairs and `B^o(1)` total finite-decoration multiplicity.
- **HYPOTHESES:** Fixed `C`; positive/nonzero integer; number of reconstruction layers is fixed; each fiber bound uniform.
- **PHYSICAL DEPENDENCE:** None, but every application must preserve its outer measure and masks.
- **MEASURE:** The already-fixed outer fiber only.
- **QUANTIFIERS:** Pointwise uniform in the fixed outer data.
- **LOSS / COST:** `B^o(1)` multiplicity/equivalence, never a fixed-power saving or a density lower bound.
- **REUSE CLASS:** `DIRECT_REUSE`
- **TRIGGER SIGNATURE:** Product factorization, parity-filtered divisor pairs, finite root orientations, or fixed-degree maps.
- **FAILURE CONDITIONS:** Super-polynomial integers, growing number of layers, or using the fiber to change scalar/pair measure.
- **SOURCE:** `stages/stage14/final.md`, Lemmas 3.2 and 3.5, Sections 6.3 and 8.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `BACKGROUND`
- **DEPENDENCIES:** None.
- **KNOWN APPLICATION:** X13 factor pairs, reciprocal completions, dyadic/sign/2-primary decorations.
- **POSSIBLE FUTURE USE:** Universal exponent-preserving adapter.

### AR-017 — Gaussian quotient and cross-resultant dictionary

- **CATEGORY:** exact algebra / Gaussian / energy
- **ONE-LINE PURPOSE:** Distinguish self-generated Gaussian root data from transferable cross-point congruence information.
- **INPUT SHAPE:** Primitive `(U,V)` on a fixed common-core Gaussian root line, common-core divisor `Pi_C`, and quadratic value `a_0U+i b_0V`.
- **OUTPUT:** Exact quotient `W=(a_0U+i b_0V)/Pi_C`; real roots are two linear values; twisted roots factor `N(W)`; shared primes transfer between two points only through explicit same-role/cross-role resultants.
- **HYPOTHESES:** Unique factorization in `Z[i]`, fixed root orientation, unit/small defects controlled, two primitive points for energy statements.
- **PHYSICAL DEPENDENCE:** Algebra is broader; Stage14 charge was a fixed common-core primitive-pair measure.
- **MEASURE:** Pointwise quotient fiber; pair-energy measure only after a second point is introduced.
- **QUANTIFIERS:** Exact pointwise identities; transfer statements for pairs.
- **LOSS / COST:** Gaussian units/orientations `B^o(1)`; no automatic second spacing modulus.
- **REUSE CLASS:** `REUSE_AFTER_EXACT_ADAPTER`
- **TRIGGER SIGNATURE:** A quadratic `x^2+y^2` value has one fixed Gaussian divisor and remaining prime roots appear self-generated.
- **FAILURE CONDITIONS:** Never multiply the already charged common-core modulus by root moduli that are functions of the point; private primes give no cross spacing.
- **SOURCE:** `stages/stage14/archive/tasks/14-X7/result.md`, Sections 2–7; `stages/stage14/archive/tasks/14-X9/result.md`, Sections 5–8.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `SUPERSEDED_BUT_REUSABLE`
- **DEPENDENCIES:** AR-009, AR-028.
- **KNOWN APPLICATION:** Prevented illegal four-root recharge and defined the correct energy receiver.
- **POSSIBLE FUTURE USE:** Stage15 squareclass/Gaussian analysis of the third-square condition.

### AR-018 — Cayley/Gaussian squareclass orientation split

- **CATEGORY:** exact algebra / squareclass / Gaussian
- **ONE-LINE PURPOSE:** Partition one common core into same- and opposite-Gaussian-orientation support without double charging it.
- **INPUT SHAPE:** A good common core with primewise Gaussian orientations and Cayley congruences `C_-|M-N`, `C_+|M+N`.
- **OUTPUT:** Coprime split `C=C_+C_-` (up to controlled defects) tagged by orientation; exact same/opposite support information.
- **HYPOTHESES:** Unit local factors, fixed allocation/orientation, original Cayley identities.
- **PHYSICAL DEPENDENCE:** Stage14 coefficient space; the split itself is local algebra.
- **MEASURE:** One already-charged common-core packet.
- **QUANTIFIERS:** Primewise exact, recombined pointwise.
- **LOSS / COST:** Orientation choices `B^o(1)`; the two parts partition one charge and supply no independent saving.
- **REUSE CLASS:** `REUSE_AFTER_EXACT_ADAPTER`
- **TRIGGER SIGNATURE:** A sum-of-two-squares core carries conjugate-prime choices and simultaneous `M±N` divisibilities.
- **FAILURE CONDITIONS:** Do not count `C_+` and `C_-` as two moduli or infer energy from orientation tags alone.
- **SOURCE:** `stages/stage14/archive/tasks/14-X9/result.md`, Sections 5–7; `stages/stage14/archive/tasks/14-4cy/result.md`, Section 3.
- **SOURCE CONFIDENCE:** `PROVED_BUT_SOURCE_FRAGMENTED`
- **STATUS:** `SUPERSEDED_BUT_REUSABLE`
- **DEPENDENCIES:** AR-017, AR-028.
- **KNOWN APPLICATION:** Stage14 Cayley row and Gaussian boundary analysis.
- **POSSIBLE FUTURE USE:** Local squareclass splitting after Stage15-4 normalizes `R^2` square.

### AR-019 — q17 reciprocal divisor/CRT kernel

- **CATEGORY:** analytic interface / exact normal form
- **ONE-LINE PURPOSE:** Name the stable inner support problem of two coupled divisor choices and reciprocal CRT conditions.
- **INPUT SHAPE:** Fixed-E principal primitive rectangle, fixed agreement pair/radial-linear data, two divisor choices and a factor-pair equation with two CRT congruences.
- **OUTPUT:** Exact Boolean/witness kernel `FixedAgreementPairRadialLinearTwoLevelDivisorCRTReciprocalSolvabilitySupport`; candidate multiplicity is `B^o(1)`, but uniform nonempty support is not proved by q17.
- **HYPOTHESES:** Full reciprocal filters and quantifier order retained; fixed-E scalar outer measure.
- **PHYSICAL DEPENDENCE:** Stage14 fixed-E packet and post-mask separation.
- **MEASURE:** Fixed-E scalar primitive-pair measure.
- **QUANTIFIERS:** Required every principal cell; literature found mostly averaged/one-divisor substitutes.
- **LOSS / COST:** Witness multiplicity `B^o(1)` only; no support lower bound.
- **REUSE CLASS:** `REUSE_AFTER_EXACT_ADAPTER`
- **TRIGGER SIGNATURE:** Two nested divisor allocations feed reciprocal factor-pair CRT solvability.
- **FAILURE CONDITIONS:** Do not transfer q17 conclusions to conditioned filtered-tau3, `(E,m)` pair, post-mask, fixed-U, or averaged measures.
- **SOURCE:** `docs/stage14-q17-reciprocal-crt-literature-radar.md`; `docs/stage14-q17-summary.md`; `stages/stage14/archive/tasks/14-4gh/result.md`.
- **SOURCE CONFIDENCE:** `PROVED_BUT_SOURCE_FRAGMENTED`
- **STATUS:** `CONSUMED`
- **DEPENDENCIES:** AR-016, AR-023, AR-024.
- **KNOWN APPLICATION:** Precursor to the MAIN first-moment receiver and later S kernel identification.
- **POSSIBLE FUTURE USE:** Search template only after a new problem's outer measure is matched exactly.

### AR-020 — MAIN nested divisor-root first-moment receiver

- **CATEGORY:** external theorem interface / negative knowledge
- **ONE-LINE PURPOSE:** State exactly the missing theorem for the final Stage14 MAIN strict-saving route.
- **INPUT SHAPE:** Primitive rectangle; one primitive product; nested divisors `t_p|m°`, `t_q|m°`, `f|t_pt_q`; two simultaneous moving quadratic root congruences; fixed coefficient-prime support and masks.
- **OUTPUT:** Requested uniform first-moment asymptotic or fixed-power deficit; Stage14 proved only the exact theorem species, not the estimate.
- **HYPOTHESES:** Every retained principal cell, moving root target, both divisor levels, primitive rectangle, original masks.
- **PHYSICAL DEPENDENCE:** Stage14 integral-space-diagonal fixed-E two-sided strict-saving packet.
- **MEASURE:** Fixed-E scalar primitive-rectangle measure.
- **QUANTIFIERS:** Uniform every principal cell, not almost all moduli or averaged moduli.
- **LOSS / COST:** Existing witness multiplicity `B^o(1)` relates support and first moment; it does not estimate the first moment.
- **REUSE CLASS:** `EXTERNAL_THEOREM_GATE`
- **TRIGGER SIGNATURE:** A new normal form exactly matches nested K-free divisors plus two moving quadratic roots.
- **FAILURE CONDITIONS:** One-AP divisor theorems, Ford single-divisor support, binary-form results without exact encoding, or averaged modulus results are not direct.
- **SOURCE:** `stages/stage14/archive/tasks/14-4gh/result.md`; `stages/stage14/archive/tasks/14-4ghH/result.md`; `stages/stage14/final.md`, Sections 8 and 12.
- **SOURCE CONFIDENCE:** `AUDITED_NEGATIVE`
- **STATUS:** `PARKED_EXTERNAL_GATE`
- **DEPENDENCIES:** AR-019, AR-023, AR-027.
- **KNOWN APPLICATION:** Final MAIN route boundary; not used in the square-root theorem.
- **POSSIBLE FUTURE USE:** A theorem-radar query if Stage15-4 produces the exact same receiver and measure.

### AR-021 — Mitsui/Kai safe fixed-U Gaussian-prime occupancy

- **CATEGORY:** external theorem interface / local analytic
- **ONE-LINE PURPOSE:** Give a pointwise lower prime-occupancy ratio for one fixed Gaussian residue/sector in the certified modulus range.
- **INPUT SHAPE:** `K=Q(i)`, fixed strict D4 sector, one invertible ordinary Gaussian residue modulo `d`, fixed-power long interval/headroom, and `d^2` inside Kai's pseudopolynomial envelope.
- **OUTPUT:** Safe-range prime count is `B^{-o(1)}` times the unrestricted sector benchmark; long interval follows by cumulative subtraction.
- **HYPOTHESES:** Fixed-U packet, actual upper scale, Kai/Mitsui modulus condition, possible Siegel term retained.
- **PHYSICAL DEPENDENCE:** Fixed-U Stage14 T route only; not whole family.
- **MEASURE:** One charged fixed-U packet/residue.
- **QUANTIFIERS:** Pointwise for every admissible safe-range packet.
- **LOSS / COST:** Subpolynomial residue/Siegel factors; no whole-family saving.
- **REUSE CLASS:** `LOCAL_ONLY`
- **TRIGGER SIGNATURE:** A fixed Gaussian residue in a fixed sector has long interval headroom and small enough modulus.
- **FAILURE CONDITIONS:** Outside Kai's modulus range; short endpoint without headroom; average-to-pointwise promotion; whole-family or non-fixed-U use.
- **SOURCE:** `stages/stage14/archive/tasks/14-tH31/result.md`; `stages/stage14/final.md`, Section 8.
- **SOURCE CONFIDENCE:** `EXTERNAL_THEOREM_DEPENDENT`
- **STATUS:** `CONSUMED`
- **DEPENDENCIES:** AR-027.
- **KNOWN APPLICATION:** Closed one safe fixed-U depletion mechanism.
- **POSSIBLE FUTURE USE:** Local prime selector only after exact coefficient/range match.

### AR-022 — Super-Kai individual-residue no-go boundary

- **CATEGORY:** negative knowledge / external theorem gate
- **ONE-LINE PURPOSE:** Prevent extrapolating individual Gaussian-residue density beyond the certified conductor range.
- **INPUT SHAPE:** Same geometry as AR-021 but `d^2>exp(sqrt(log X)/C_K)`, `d=B^o(1)`, one fixed residue and sector.
- **OUTPUT:** No audited unconditional every-residue lower-ratio theorem; precise gate `SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio`.
- **HYPOTHESES:** Actual upper scale is Kai-inadmissible; principal benchmark is much larger than mere prime existence.
- **PHYSICAL DEPENDENCE:** Fixed-U Stage14 T route.
- **MEASURE:** One charged fixed-U packet/residue.
- **QUANTIFIERS:** Required pointwise every packet; known beyond-range tools average or prove existence.
- **LOSS / COST:** Fixed-power headroom helps subtraction, not modulus admissibility; `d=B^o(1)` is only a subpolynomial-size condition and supplies no density saving.
- **REUSE CLASS:** `EXTERNAL_THEOREM_GATE`
- **TRIGGER SIGNATURE:** Someone argues that `d=B^o(1)`, least-prime, sector-only, or average results imply density in one super-range residue.
- **FAILURE CONDITIONS:** Never treat BV/BDH, zero-density, least-prime, sector-only, or products-of-primes results as the requested pointwise density theorem.
- **SOURCE:** `stages/stage14/archive/tasks/14-t157/result.md`; `stages/stage14/archive/tasks/14-tH33/result.md`.
- **SOURCE CONFIDENCE:** `AUDITED_NEGATIVE`
- **STATUS:** `PARKED_EXTERNAL_GATE`
- **DEPENDENCIES:** AR-021, AR-027.
- **KNOWN APPLICATION:** Final T route park.
- **POSSIBLE FUTURE USE:** Immediate rejection test for out-of-range individual residue claims.

### AR-023 — Scalar fixed-E versus `(E,m)` pair-measure separation

- **CATEGORY:** proof accounting / measure
- **ONE-LINE PURPOSE:** Keep scalar and polynomial pair theorem species distinct even when `n=Em` has divisor-many fibers.
- **INPUT SHAPE:** A scalar host `n` and an outer pair `(E,m)` with pair-dependent prefilters or second-layer conditions.
- **OUTPUT:** `B^o(1)` factorization fibers do not scalarize the pair measure; a pair-to-scalar host adapter must be proved.
- **HYPOTHESES:** Pair-dependent conditions are not already proved constant/summably controllable on each scalar fiber.
- **PHYSICAL DEPENDENCE:** None as a logical firewall; Stage14 applied it to S branches.
- **MEASURE:** Explicit distinction between fixed-E scalar family and outer `(E,m)` pair family.
- **QUANTIFIERS:** Theorem-species/quantifier preservation.
- **LOSS / COST:** `B^o(1)` is multiplicity already charged, not permission to change measure.
- **REUSE CLASS:** `SAME_KERNEL_DIFFERENT_MEASURE`
- **TRIGGER SIGNATURE:** A product host is proposed to replace an outer factor pair because factorization count is small.
- **FAILURE CONDITIONS:** No reuse until every pair-dependent mask is preserved by a proved adapter.
- **SOURCE:** `stages/stage14/archive/tasks/14-Work-ccX41/result.md`, Sections 1–3; `stages/stage14/final.md`, Sections 6.3 and 11.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `ACTIVE`
- **DEPENDENCIES:** AR-016, AR-028.
- **KNOWN APPLICATION:** Split S scalar and polynomial theorem species.
- **POSSIBLE FUTURE USE:** Mandatory audit for any Stage15 host-variable compression.

### AR-024 — Conditioned-kernel measure firewall

- **CATEGORY:** proof accounting / negative knowledge
- **ONE-LINE PURPOSE:** Forbid transferring a saving merely because two routes have the same inner reciprocal-CRT kernel.
- **INPUT SHAPE:** Identical q17-style inner equations but different outer conditioning, witness weights, post-masks, or scalar/pair measures.
- **OUTPUT:** Kernel identification is consumed; lower ratios/savings do not transfer without a measure-preserving adapter.
- **HYPOTHESES:** First-layer filtered conditioning remains active.
- **PHYSICAL DEPENDENCE:** Logical principle is general; Stage14 S application retained its physical masks.
- **MEASURE:** Original conditioned scalar or `(E,m)` outer measure, not q17's unconditioned fixed-E measure.
- **QUANTIFIERS:** Every retained conditioned cell.
- **LOSS / COST:** `B^o(1)` witness fibers cannot establish conditioned lower density.
- **REUSE CLASS:** `SAME_KERNEL_DIFFERENT_MEASURE`
- **TRIGGER SIGNATURE:** “The inner formulas are identical, so the old theorem applies.”
- **FAILURE CONDITIONS:** Never infer common measure from common kernel; do not recharge earlier kernel research.
- **SOURCE:** `stages/stage14/archive/tasks/14-Work-cgX45/result.md`, Sections 1–3.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `ACTIVE`
- **DEPENDENCIES:** AR-019, AR-023, AR-028.
- **KNOWN APPLICATION:** Prevented illegal q17→S promotion.
- **POSSIBLE FUTURE USE:** General analytic-reduction firewall in Stage15/later.

### AR-025 — Valuation-reduced character recombination receiver

- **CATEGORY:** analytic / valuation / character interface
- **ONE-LINE PURPOSE:** Recombine unit and nonunit strata into one reduced-modulus principal/nonprincipal discrepancy problem.
- **INPUT SHAPE:** Filtered reciprocal-CRT first moment, moving common core, valuation pattern `nu`, reduced modulus `Q_nu`, target class `rho_nu`, scalar or pair outer measure.
- **OUTPUT:** Exact decomposition into principal mass plus aggregate nonprincipal characters; separate unit/nonunit gates are consumed.
- **HYPOTHESES:** All valuations, witness filters, common-core average, and residual post-mask retained.
- **PHYSICAL DEPENDENCE:** Stage14 S conditioned packet; two theorem species remain.
- **MEASURE:** Valuation-averaged scalar fixed-E or polynomial `(E,m)` pair measure.
- **QUANTIFIERS:** Needed every retained principal cell after valuation averaging.
- **LOSS / COST:** Number of valuation allocations per witness can be `B^o(1)`, but character family size `phi(Q_nu)` may be polynomial.
- **REUSE CLASS:** `EXTERNAL_THEOREM_GATE`
- **TRIGGER SIGNATURE:** Unit/nonunit CRT strata can be reduced to moving moduli and one target residue.
- **FAILURE CONDITIONS:** Do not collapse character complexity from `B^o(1)` valuation patterns; do not discard the common-core average or merge scalar/pair measures.
- **SOURCE:** `stages/stage14/archive/tasks/14-Work-cnX52/result.md`; `stages/stage14/archive/tasks/14-s7-162/result.md`; `stages/stage14/archive/tasks/14-s7-164/result.md`.
- **SOURCE CONFIDENCE:** `PROVED_BUT_SOURCE_FRAGMENTED`
- **STATUS:** `PARKED_EXTERNAL_GATE`
- **DEPENDENCIES:** AR-023, AR-024, AR-027.
- **KNOWN APPLICATION:** Final S theorem normal form.
- **POSSIBLE FUTURE USE:** Character receiver only after exact Stage15 measure and masks are matched.

### AR-026 — Target-class mass countermodel

- **CATEGORY:** negative knowledge / harmonic analysis
- **ONE-LINE PURPOSE:** Show that nonnegativity plus total mass and `L^1/L^2` character control do not force mass in one moving target class.
- **INPUT SHAPE:** Nonnegative residue masses `S_nu(r)` with principal term equal to uniform mean and a designated target `rho_nu`.
- **OUTPUT:** Abstract target-avoiding mass distributions satisfy the soft identities while `S_nu(rho_nu)=0`; a genuine target-class domination theorem is necessary.
- **HYPOTHESES:** Only the currently proved mass/Fourier identities, without an `o(P_nu^2)` variance or anti-concentration theorem.
- **PHYSICAL DEPENDENCE:** Countermodel is logical, not an actual cuboid example.
- **MEASURE:** One reduced-modulus residue distribution, and its valuation aggregate.
- **QUANTIFIERS:** Demonstrates insufficiency for pointwise target-class positivity.
- **LOSS / COST:** `L^1` loses full character-family size; Parseval is variance, not a target lower bound.
- **REUSE CLASS:** `NEGATIVE_RESULT`
- **TRIGGER SIGNATURE:** A proof claims second moment/Parseval or total mass makes a specific residue class positive.
- **FAILURE CONDITIONS:** The countermodel does not prove the arithmetic theorem false; it only rejects the stated inference.
- **SOURCE:** `stages/stage14/archive/tasks/14-s7-163/result.md`.
- **SOURCE CONFIDENCE:** `AUDITED_NEGATIVE`
- **STATUS:** `NEGATIVE`
- **DEPENDENCIES:** AR-025.
- **KNOWN APPLICATION:** Proved S's remaining gap is genuine equidistribution/anti-concentration.
- **POSSIBLE FUTURE USE:** Quick rejection of target-positivity arguments based only on global moments.

### AR-027 — Averaged-versus-every-cell exceptional-set firewall

- **CATEGORY:** proof accounting / negative knowledge
- **ONE-LINE PURPOSE:** Prevent averaged modulus/residue theorems from being charged to one fixed packet or every retained cell.
- **INPUT SHAPE:** Desired pointwise/every-cell conclusion and a candidate theorem averaged over moduli, residues, cells, or characters.
- **OUTPUT:** Promotion forbidden until an exceptional-set bridge maps the theorem's average to the physical charged measure with affordable loss.
- **HYPOTHESES:** Exceptional packets cannot already be discarded by an independent physical measure bound.
- **PHYSICAL DEPENDENCE:** General; Stage14 instances include MAIN, fixed-U T, and S.
- **MEASURE:** Whatever physical packet/cell/fixed-U measure is charged; must be written explicitly.
- **QUANTIFIERS:** Distinguishes pointwise/every-cell, almost-all, average, positive density, and existence.
- **LOSS / COST:** Exceptional-set loss must be paid in the same measure; no implicit promotion.
- **REUSE CLASS:** `NEGATIVE_RESULT`
- **TRIGGER SIGNATURE:** “Almost all moduli” or mean-square/variance is used for one frozen modulus or every cell.
- **FAILURE CONDITIONS:** Direct reuse only after an explicit exceptional-set-to-physical-measure adapter is proved.
- **SOURCE:** `stages/stage14/archive/tasks/14-4ghH/result.md`; `stages/stage14/archive/tasks/14-tH33/result.md`; `stages/stage14/archive/tasks/14-s7-164/result.md`; `stages/stage14/final.md`, Section 8.
- **SOURCE CONFIDENCE:** `AUDITED_NEGATIVE`
- **STATUS:** `NEGATIVE`
- **DEPENDENCIES:** AR-028.
- **KNOWN APPLICATION:** Rejected divisor-AP, BV/BDH, and variance cross-promotions.
- **POSSIBLE FUTURE USE:** Mandatory theorem-applicability audit for Stage15/later.

### AR-028 — Consumed/superseded/recharge-forbidden discipline

- **CATEGORY:** proof accounting
- **ONE-LINE PURPOSE:** Charge each support/core/fiber once and retain reusable mechanisms even after their exponent theorem is superseded.
- **INPUT SHAPE:** A multi-stage reduction ledger with exact data dependencies and competing parameterizations.
- **OUTPUT:** Each asset labeled `ACTIVE`, `CONSUMED`, `SUPERSEDED_BUT_REUSABLE`, `PARKED_EXTERNAL_GATE`, `NEGATIVE`, or `BACKGROUND`; recharging consumed support is forbidden.
- **HYPOTHESES:** Quantifier order and source-to-target maps recorded.
- **PHYSICAL DEPENDENCE:** General; Stage14 used it across MAIN/T/S/X/Q.
- **MEASURE:** The original charged outer measure of each item.
- **QUANTIFIERS:** Ledger-level invariant.
- **LOSS / COST:** Prevents duplicated fixed-power costs/savings; `B^o(1)` fibers remain multiplicity.
- **REUSE CLASS:** `DIRECT_REUSE`
- **TRIGGER SIGNATURE:** A later stage renames an old receiver, multiplies two counts of the same core, or deletes a superseded mechanism.
- **FAILURE CONDITIONS:** Superseded theorem exponent does not imply its exact lemma is false; consumed data cannot be charged again.
- **SOURCE:** `stages/stage14/final.md`, Sections 6–7; `docs/review/stage14-final-self-contained-provenance-20260812-r01.md`; `stages/stage14/archive/tasks/14-Work-coX53/result.md`.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `ACTIVE`
- **DEPENDENCIES:** None.
- **KNOWN APPLICATION:** Final no-double-charge and route-closure audit.
- **POSSIBLE FUTURE USE:** Default proof-engineering ledger for all later stages.

### AR-029 — Stage13→14 oriented/canonical projection interface

- **CATEGORY:** reconstruction / upstream interface
- **ONE-LINE PURPOSE:** Transfer oriented one-face counts to canonical face incidences while accounting for projection multiplicity and overlaps.
- **INPUT SHAPE:** Primitive oriented Stage12 face records and primitive canonical cuboids with a distinguished integral face.
- **OUTPUT:** Unique complementary parameter, exactly two supported face-leg orientations per canonical incidence, and explicit raw/exact-one overlap correction.
- **HYPOTHESES:** Same space-diagonal cutoff, primitive convention, exact orientation map, exactly-one/two/three separated.
- **PHYSICAL DEPENDENCE:** Integral space diagonal and Stage12/13 population; A-side only.
- **MEASURE:** Oriented record measure mapped to canonical raw-face incidence measure.
- **QUANTIFIERS:** Pointwise fiber identity plus whole-family asymptotic transfer after overlap control.
- **LOSS / COST:** Exact factor 2, not `B^o(1)`; overlaps separately charged.
- **REUSE CLASS:** `REUSE_AFTER_EXACT_ADAPTER`
- **TRIGGER SIGNATURE:** An upstream oriented count is projected to canonical objects or a face-record weight looks like object multiplicity.
- **FAILURE CONDITIONS:** Do not interpret representation richness `G(p)-1` as repeated weight on one incidence; do not transfer Stage13 asymptotics to ambient Stage15 `B_2`.
- **SOURCE:** `stages/stage13/final.md`, Sections 3.17–3.23 and 8; `stages/stage14/final.md`, Section 1.3.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `BACKGROUND`
- **DEPENDENCIES:** AR-001, AR-002, AR-003.
- **KNOWN APPLICATION:** Frozen Stage13 exact-one theorem and Stage14 starting interface.
- **POSSIBLE FUTURE USE:** A-side validation and orientation audits, not ambient asymptotic transfer.

### AR-030 — Physical masks as monotone post-filters

- **CATEGORY:** proof accounting / local-global interface
- **ONE-LINE PURPOSE:** Permit upper bounds on algebraic supersets while preserving every physical restriction as a named filter.
- **INPUT SHAPE:** A larger parametrized candidate set containing the physical population.
- **OUTPUT:** Positivity, ordering, primitivity, parity/local coprimality, space square, exact face count, signs, cells, and post-column conditions may only reduce an upper bound.
- **HYPOTHESES:** Superset inclusion is proved and no filter is used to create candidates or a lower bound.
- **PHYSICAL DEPENDENCE:** General; integral-space condition is one filter only when the ambient superset is correctly defined.
- **MEASURE:** Original physical population; algebraic superset is an upper-count host.
- **QUANTIFIERS:** Pointwise inclusion and whole-family monotonicity.
- **LOSS / COST:** None for upper bounds; lower bounds require quantitative filter survival.
- **REUSE CLASS:** `DIRECT_REUSE`
- **TRIGGER SIGNATURE:** A reconstruction postpones parity, positivity, coprimality, ordering, or third-face exclusion.
- **FAILURE CONDITIONS:** Cannot drop filters in a lower-bound/asymptotic argument; cannot change the outer measure unnoticed.
- **SOURCE:** `stages/stage14/final.md`, Sections 1.2, 3, 6.3; `stages/stage14/archive/tasks/14-X13/result.md`, Sections 4–6.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `ACTIVE`
- **DEPENDENCIES:** AR-001, AR-028.
- **KNOWN APPLICATION:** Dujella and divisor bounds counted supersets; physical masks were restored as filters.
- **POSSIBLE FUTURE USE:** Stage15-4/5 upper-bound reductions, with special care for exactly-two subtraction.

### AR-031 — Finite census and directional diagnostics only

- **CATEGORY:** negative knowledge / numerical diagnostic
- **ONE-LINE PURPOSE:** Preserve exact finite evidence without promoting it to an asymptotic theorem.
- **INPUT SHAPE:** Validated exact enumerators and frozen cutoffs.
- **OUTPUT:** Stage14 finite `N_2` directional counts, `T=0` through tested ranges, and observed direction/defect signals.
- **HYPOTHESES:** Reproducible locked data and matching cutoff/convention.
- **PHYSICAL DEPENDENCE:** Stage14 integral-space-diagonal finite samples.
- **MEASURE:** Finite census only.
- **QUANTIFIERS:** At named cutoffs; no asymptotic quantifier.
- **LOSS / COST:** Sampling/finite-range uncertainty; no theorem saving.
- **REUSE CLASS:** `DO_NOT_REUSE`
- **TRIGGER SIGNATURE:** A future implementation needs regression locks or a conjecture suggests a predeclared diagnostic.
- **FAILURE CONDITIONS:** Never infer a directional limit, true exponent, matching lower bound, or perfect-cuboid nonexistence.
- **SOURCE:** `stages/stage14/final.md`, Sections 9 and 11 (BG-14); `stages/stage14/archive/tasks/14-num-alpha11/result.md`; `stages/stage14/archive/tasks/14-num-alpha11-diag11/result.md`.
- **SOURCE CONFIDENCE:** `HEURISTIC_DIAGNOSTIC`
- **STATUS:** `NEGATIVE`
- **DEPENDENCIES:** AR-001.
- **KNOWN APPLICATION:** Stage15 paired-enumerator regression check.
- **POSSIBLE FUTURE USE:** Validation only after restricting to the same `A_2` cutoff.

### AR-032 — Primitive-first Möbius reindexing

- **CATEGORY:** exact algebra / primitive counting
- **ONE-LINE PURPOSE:** Insert the common-scale Möbius inversion before truncation so primitive coefficients and boundary layers are counted in their natural variables.
- **INPUT SHAPE:** A homogeneous raw parameter count whose objects have a unique positive common integer scale.
- **OUTPUT:** An exact primitive-first sum with the Möbius variable absorbed into the height coefficient, eliminating a separate outer truncation error.
- **HYPOTHESES:** Scaling acts freely away from explicitly removed ties; the cutoff is homogeneous; the raw-to-primitive relation is exact at object level.
- **PHYSICAL DEPENDENCE:** The mechanism is general; Stage12 used the primitive oriented one-face population with space-diagonal cutoff.
- **MEASURE:** Whole raw population projected to its primitive oriented measure.
- **QUANTIFIERS:** Exact finite reindexing before any asymptotic estimate.
- **LOSS / COST:** No analytic loss; orientation and overlap corrections remain separate.
- **REUSE CLASS:** `REUSE_AFTER_EXACT_ADAPTER`
- **TRIGGER SIGNATURE:** A late Möbius truncation creates a boundary layer or an apparent outer error.
- **FAILURE CONDITIONS:** Do not move Möbius inversion across a nonhomogeneous cutoff, nonunique scaling fiber, or changed canonical/oriented measure.
- **SOURCE:** `stages/stage12/final.md`, embedded definition sheet ``4–6 and Stage12-N1-2j ``1–5.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `BACKGROUND_REUSABLE`
- **DEPENDENCIES:** AR-001, AR-029.
- **KNOWN APPLICATION:** Stage12 primitive oriented asymptotic and removal of the historical outer Möbius boundary.
- **POSSIBLE FUTURE USE:** Any later primitive ambient or square-survivor count after its scale and cutoff adapter is written.

### AR-033 — Weighted coprime rectangle convolution

- **CATEGORY:** analytic counting / Euler product
- **ONE-LINE PURPOSE:** Transfer one-variable summatory estimates through a two-variable coprime correction with a rigorously summable coefficient tail.
- **INPUT SHAPE:** `S(R,S)=sum beta(r)beta(s)1_(r,s)=1` with a factorization into two one-variable series and a cross correction `C(s_1,s_2)`.
- **OUTPUT:** A uniform rectangle main term and the certified tail `R^(3/4+epsilon)S+RS^(3/4+epsilon)`, plus logarithmic refinements when finite-order expansions are inserted.
- **HYPOTHESES:** `B_beta(X)<<X`; weighted absolute norm `sum |c(a,b)|/(ab)^(1/2+delta)<infinity`; fixed `epsilon<1/8`.
- **PHYSICAL DEPENDENCE:** Abstract analytic lemma; the Stage12 weights and local factors are population-specific.
- **MEASURE:** Two-variable scalar coefficient measure on a rectangle.
- **QUANTIFIERS:** Uniform in `R,S>=2`; kernel promotion requires a separately proved partial-summation norm.
- **LOSS / COST:** The `3/4+epsilon` tails are retained; the invalid historical `1/2+delta` strengthening is forbidden.
- **REUSE CLASS:** `REUSE_AFTER_EXACT_ADAPTER`
- **TRIGGER SIGNATURE:** A coprime two-variable host factors into marginal Dirichlet series times an absolutely summable cross correction.
- **FAILURE CONDITIONS:** Do not reuse only the main Euler factor while omitting the weighted tail norm, or assume a rectangle estimate transfers to a curved region without a kernel-variation proof.
- **SOURCE:** `stages/stage12/final.md`, Stage12-N1-3a Lemma 3a.1, integrated proof `6, and Stage12-N1-3i ``1–4.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `ACTIVE_REUSABLE`
- **DEPENDENCIES:** AR-023, AR-024.
- **KNOWN APPLICATION:** Stage12 parity-weighted coprime rectangle and corrected boundary exponent.
- **POSSIBLE FUTURE USE:** Stage15 coefficient rectangles if its normal form exposes the same scalar coprime convolution.

### AR-034 — Core/wing/shallow boundary separation

- **CATEGORY:** analytic counting / boundary control
- **ONE-LINE PURPOSE:** Separate small-coordinate wings and fixed-height shallow sectors from the retained core before applying smooth rectangle or radial transfer.
- **INPUT SHAPE:** A coupled positive region with a dyadic core, small-coordinate wings, and a shallow radial or height sector.
- **OUTPUT:** Direct lower-order bounds on wings and shallow sectors, leaving a core with controlled partial-summation kernel and no artificial boundary main term.
- **HYPOTHESES:** Direct summatory majorants on excluded sectors; explicit core cutoff; kernel boundary and mixed-variation bounds on retained boxes.
- **PHYSICAL DEPENDENCE:** General decomposition; all numerical cutoffs and Stage12 weights are source-specific.
- **MEASURE:** Whole scalar parameter sum partitioned exactly into disjoint regions.
- **QUANTIFIERS:** Bound excluded regions first, then sum the uniform core estimate.
- **LOSS / COST:** Source-dependent lower-order errors; no wing estimate may be silently reused as a shallow estimate.
- **REUSE CLASS:** `REUSE_AFTER_EXACT_ADAPTER`
- **TRIGGER SIGNATURE:** A curved or radial region has axes, cusps, shallow annuli, or dyadic boxes where uniform asymptotics fail.
- **FAILURE CONDITIONS:** Do not merge geometrically different exceptional regions, create an uncharged artificial boundary, or infer lower order without summing all boxes.
- **SOURCE:** `stages/stage12/final.md`, Stage12-N1-3f ``1–7 and Stage12-N1-3g ``1–8.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `ACTIVE_REUSABLE`
- **DEPENDENCIES:** AR-033.
- **KNOWN APPLICATION:** Stage12 small-coordinate wing and fixed-height shallow-sector closure.
- **POSSIBLE FUTURE USE:** Any Stage15 asymptotic transfer with unbalanced parameter wings or a thin height boundary.

### AR-035 — Fixed-prime overlap sieve with ordered limits

- **CATEGORY:** sieve / overlap control
- **ONE-LINE PURPOSE:** Prove an additional square-condition overlap is lower order using finitely many independent local rejection factors without invoking a growing-modulus theorem.
- **INPUT SHAPE:** A raw incidence asymptotic admitting congruence refinement for every fixed finite set of suitable inert primes.
- **OUTPUT:** Pair and triple overlap `o` of the ambient main scale when each added prime has acceptance bounded uniformly below one.
- **HYPOTHESES:** Fixed-modulus refined asymptotic with the same pole order; multiplicative local acceptance; sufficiently large primes with acceptance at most a fixed `rho<1`.
- **PHYSICAL DEPENDENCE:** Stage13 used primitive canonical space-diagonal one-face incidences; a new population needs its own congruence-refined asymptotic.
- **MEASURE:** Raw incidence population before exact-one subtraction.
- **QUANTIFIERS:** Fix `k` primes, take `B->infinity`, and only then let `k->infinity`.
- **LOSS / COST:** Qualitative `o` only unless the refined theorem is effective uniformly in `k`.
- **REUSE CLASS:** `REUSE_AFTER_EXACT_ADAPTER`
- **TRIGGER SIGNATURE:** A second or third square condition imposes a local quadratic-residue restriction at many inert primes.
- **FAILURE CONDITIONS:** Never interchange the limits, let the modulus grow inside a fixed-modulus theorem, or conclude a quantitative rate from the qualitative diagonal argument.
- **SOURCE:** `stages/stage13/final.md`, ``7.2, 8.5, and 9.3; hardened source `stages/stage13/archive/tasks/13-13ft/r07-hardening-lemma.md`.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `ACTIVE_REUSABLE`
- **DEPENDENCIES:** AR-024, AR-027, AR-029.
- **KNOWN APPLICATION:** Stage13 pair/triple face overlaps are `o(B(log B)^3)` without assuming perfect-cuboid nonexistence.
- **POSSIBLE FUTURE USE:** High-priority Stage15 square-survivor thinning route after a fixed-modulus ambient refinement is proved.

### AR-036 — Ordered-chamber Gelfand--Leray directional transfer

- **CATEGORY:** archimedean geometry / directional asymptotic
- **ONE-LINE PURPOSE:** Convert a symmetric ambient shell count into canonical direction constants by integrating the induced real density over the ordered chamber.
- **INPUT SHAPE:** A homogeneous shell with canonical order `0<a<b<c` and a distinguished constraint surface whose coarea density is known.
- **OUTPUT:** Directional constants `I_q`, their exact sum, and a normalized limiting vector after arithmetic factors are proved common across directions.
- **HYPOTHESES:** Exact coarea/Gelfand--Leray density; boundary has lower order; arithmetic main factor is direction-independent; oriented/canonical projection is audited.
- **PHYSICAL DEPENDENCE:** The principle is general; Stage13's `1/sqrt(x_i^2+x_j^2)` densities and constants are specific to one integral face.
- **MEASURE:** Archimedean chamber measure coupled to the matching arithmetic population.
- **QUANTIFIERS:** Whole-family asymptotic after exact chamber partition and projection.
- **LOSS / COST:** None at the formal integral level; analytic transfer and overlap removal retain their own errors.
- **REUSE CLASS:** `REUSE_AFTER_EXACT_ADAPTER`
- **TRIGGER SIGNATURE:** Canonical sorting breaks apparent coordinate symmetry and directional counts need separate leading constants.
- **FAILURE CONDITIONS:** Canonical relabeling alone does not create the bias; do not transfer Stage13 constants when the density, cutoff, or arithmetic factor changes.
- **SOURCE:** `stages/stage13/final.md`, ``3.6–3.10, 7.1, and 9.1–9.4.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `BACKGROUND_REUSABLE`
- **DEPENDENCIES:** AR-001, AR-029, AR-035.
- **KNOWN APPLICATION:** Stage13 exactly-one directional vector and its non-`2:1:1` limiting law.
- **POSSIBLE FUTURE USE:** Directional decomposition of Stage15 ambient or survivor counts after matching coarea and arithmetic-factor proofs.

### AR-037 — Finite-order Selberg--Delange contract

- **CATEGORY:** external theorem interface / analytic verification
- **ONE-LINE PURPOSE:** Lock exactly which finite-order Selberg--Delange theorem is imported and verify every coefficient, analytic-region, and vertical-growth hypothesis separately.
- **INPUT SHAPE:** `F(s)=zeta(s)^z H(s)` with fixed-degree divisor majorant and `H` regular in a standard zero-free-shaped region.
- **OUTPUT:** Any prescribed fixed logarithmic saving by choosing a fixed expansion depth `J`, with constants and uniformity recorded.
- **HYPOTHESES:** Analyticity of `H`; polynomial vertical growth on fixed strips; coefficient majorant; nonzero leading factor; all auxiliary parameters inside the declared uniformity.
- **PHYSICAL DEPENDENCE:** None in the contract; the factorizations `H` and their uniform ranges are application-specific.
- **MEASURE:** One-variable multiplicative coefficient sum, before any two-variable or curved-region transfer.
- **QUANTIFIERS:** Choose the required fixed log-saving and then fix `J`; no parameter-dependent expansion depth.
- **LOSS / COST:** External theorem dependence; later box summation must budget the chosen logarithmic power.
- **REUSE CLASS:** `REUSE_AFTER_EXACT_ADAPTER`
- **TRIGGER SIGNATURE:** An Euler product has a finite-order pole and a proof needs strong fixed log-power remainder rather than a guessed subexponential error.
- **FAILURE CONDITIONS:** Do not cite the theorem without mapping its analytic region and vertical growth, or use one-variable uniformity after introducing an uncontrolled conductor.
- **SOURCE:** `stages/stage12/final.md`, embedded Selberg--Delange reference lock and Stage12-N1-3h/3i/3j; Tenenbaum, Chapter II.5, Theorem II.5.2.
- **SOURCE CONFIDENCE:** `EXTERNAL_THEOREM_DEPENDENT`
- **STATUS:** `ACTIVE_REUSABLE`
- **DEPENDENCIES:** AR-024, AR-033.
- **KNOWN APPLICATION:** Stage12 `beta` and `1*beta` summatory expansions with arbitrary fixed log-power saving.
- **POSSIBLE FUTURE USE:** Any later Euler-product host after its exact factorization and uniformity ledger are supplied.

## Audit summary

- Every `DIRECT_REUSE` entry states exact hypotheses and measure.
- Stage14-space-diagonal theorems are primary-class marked; other Stage14-dependent entries also say so under physical dependence.
- Fixed-U AR-021/022 are local and cannot silently become whole-family results.
- Every `B^o(1)` occurrence is labeled multiplicity/equivalence unless a separate analytic role is stated.
- Same-kernel/different-measure cases are AR-023/024 and indexed explicitly.
- Superseded but reusable mechanisms AR-009/010/014/015/017/018 are retained.
- External/no-go knowledge AR-020/022/025/026/027 and diagnostic AR-031 are retained.
- Upstream reusable mechanisms AR-032–AR-037 are provenance-labeled and require exact population/measure adapters.
- The registry asserts no new Stage14 theorem and restarts no parked route.

## Frozen registry report

```text
ARSENAL_ENTRY_COUNT=37
DIRECT_REUSE_COUNT=6
ADAPTER_REQUIRED_COUNT=19
NEGATIVE_KNOWLEDGE_COUNT=8
SPACE_DIAGONAL_ONLY_COUNT=5
STAGE15_CURRENTLY_RELEVANT_COUNT=10
UNINDEXED_STAGE14_REGIONS_REMAINING=NONE_IDENTIFIED_AFTER_R04_BURIED_GOLD_AND_TARGETED_SOURCE_AUDIT
ARSENAL_READY_FOR_FUTURE_AGENT_SEARCH=true
```

`ADAPTER_REQUIRED_COUNT` combines seventeen `REUSE_AFTER_EXACT_ADAPTER` entries and two `SAME_KERNEL_DIFFERENT_MEASURE` entries. `NEGATIVE_KNOWLEDGE_COUNT` counts AR-020, AR-022–AR-027, and AR-031. Historical exponent-only stages not cited by R04's source/provenance/buried-gold ledgers remain deliberately outside the Arsenal; their current bounds are superseded and no additional reusable mechanism was identified by the targeted audit.

**High-value reusable weapons:** AR-003 two-face gluing; AR-009 primitive Gaussian root lines; AR-012 reverse reciprocal reconstruction; AR-016 divisor/finite-fiber adapter; AR-023 scalar/pair separation; AR-028 recharge discipline; AR-032 primitive-first Möbius; AR-033 weighted rectangles; AR-035 fixed-prime overlap sieve; AR-036 ordered-chamber transfer.

**Five most dangerous traps:** AR-024 same kernel/different conditioned measure; AR-023 scalarizing `(E,m)` through divisor-many fibers; AR-027 average→every-cell promotion; AR-021/022 fixed-U or conductor-range promotion; AR-005/006 Stage14 integral-space-diagonal→Stage15 ambient promotion.
