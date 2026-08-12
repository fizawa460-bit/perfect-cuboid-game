# Stage14 final self-contained mathematical review

**Bundle ID:** `STAGE14-FINAL-SELF-CONTAINED-20260812-R02`

**R02 repair boundary.** R02 changes no Stage14 theorem, exponent, receiver, or route status. It repairs the R01 self-containment defect identified by external review by transcribing the already-merged proofs from 4ab, 4ag, 4cx, 4cy, s7-37, s7-40, and X13. No new mathematical bridge is asserted.

**Frozen source snapshot:** `2c7ec9433edbd4f06f298df73cba9e18e164057a` (`main`, 2026-08-12 audit)

**Purpose:** reconstruct, audit, compress, and freeze the final Stage14 state. This document starts no new Stage14 route.

---

## Executive Summary

Stage14 asked how many primitive rectangular boxes with integer space diagonal have **exactly two** integral face diagonals when the space diagonal is at most `B`. Stage12 counted individual integral-face records, and Stage13 isolated and asymptotically counted boxes with exactly one integral face. Stage14 addressed the rarer overlap population left below the Stage13 main term.

The final proved result is an **upper bound**

\[
N_2(B)\ll B^{1/2+o(1)}.
\]

An upper bound is a ceiling: the number of exactly-two boxes cannot grow faster than square-root scale up to subpolynomial factors. It is meaningful because Stage14 progressively lowered the best whole-family ceiling from exponent `41/42` to `1/2`, and the final proof covers every physical chamber rather than a fixed-parameter or local subfamily.

This does **not** say that the count is asymptotic to a constant times `sqrt(B)`. There is no matching lower bound, no asymptotic constant, and no proof that `1/2` is the true growth exponent. A strict fixed-power improvement `B^(1/2-delta)` is also not proved.

It is not a solution of the perfect-cuboid problem. Perfect cuboids have all three face diagonals integral; `N_2` counts boxes with exactly two. The triple population is retained separately, and Stage14 proves neither its emptiness nor its non-emptiness.

Stopping is mathematically justified because the square-root theorem is complete, while every route aimed at a strict sub-square-root saving has reached a sharply stated external theorem gate. The main, fixed-`U` (`T`), and conditioned-character (`S`) routes stop for different reasons. The final integration stage found no legal cross-promotion or uncharged internal reduction. Work can restart only after a materially new theorem or exact measure-preserving adapter appears.

---

## 1. Frozen problem and conventions

### 1.1 Physical objects and cutoff

A physical cuboid is a triple of positive integers

\[
0<a<b<c,\qquad \gcd(a,b,c)=1.
\]

This is the **primitive canonical convention**: primitiveness removes common scaling, and strict ordering chooses one representative of the permutation orbit. Its space diagonal `d` is required to be an integer:

\[
a^2+b^2+c^2=d^2,\qquad d\in\mathbf Z_{>0}.
\]

The cutoff is

\[
\mathcal C(B)=\{(a,b,c,d):0<a<b<c,\ \gcd(a,b,c)=1,\ a^2+b^2+c^2=d^2,\ d\le B\}.
\]

For real `B>=1`, the inequality `d<=B` is understood literally; changing `B` between consecutive integers does not change the population.

The three face-square predicates are

\[
I_{ab}=1_{a^2+b^2\ \mathrm{is\ a\ square}},\quad
I_{ac}=1_{a^2+c^2\ \mathrm{is\ a\ square}},\quad
I_{bc}=1_{b^2+c^2\ \mathrm{is\ a\ square}}.
\]

Define the exactly-one, exactly-two, and exactly-three populations by

\[
N_j(B)=\#\{C\in\mathcal C(B):I_{ab}+I_{ac}+I_{bc}=j\},\qquad j=1,2,3.
\]

The triple count is also written `T(B)=N_3(B)`. The exactly-two directional counts are

\[
N_a^{(2)}(B),\quad N_b^{(2)}(B),\quad N_c^{(2)}(B),
\]

according as the two integral faces share the smallest, middle, or largest edge, and

\[
N_2(B)=N_a^{(2)}(B)+N_b^{(2)}(B)+N_c^{(2)}(B).
\]

No assumption `T(B)=0` is made. The finite censuses happened to find no triple through their tested ranges; that is diagnostic evidence only.

### 1.2 Physical filters

All theorem statements refer to the same physical measure above. Intermediate parametrizations retain the following as filters: positivity, strict canonical ordering, primitiveness, parity and local coprimality, integral space diagonal, the required two face-square predicates, exclusion of the third face square for `N_2`, dyadic localization, sign/orientation conventions, and any recorded root/allocation/cell masks. A filter may discard algebraic candidates; it may not create candidates. Whenever an upper bound is proved before applying a later physical filter, preservation is therefore monotone.

### 1.3 Exact Stage12/13 interface

Stage12 counted primitive oriented one-face records and proved a `B(log B)^3` asymptotic. Stage13 resolved the projection multiplicity and the overlap contamination sufficiently to prove, for exact-one boxes,

\[
N_1(B)\sim \frac{\kappa}{24\pi}B(\log B)^3,
\]

with directional constants described by its fixed theorem contract. Its raw two-face overlaps and triples were only known to be `o(B(log B)^3)`. That statement supplied no polynomial exponent for the exact-two population.

Stage14 starts precisely at this unresolved overlap scale. It does not alter the Stage12/13 asymptotic and does not infer an exact-two law from the exact-one law. The interface is:

1. Stage12/13 fix the primitive/canonical physical population and identify exact-one as the dominant `B(log B)^3` family.
2. Stage14 retains the raw two-face incidences separately and seeks a sharper bound for the exact-two subpopulation.
3. Any directional Stage14 asymptotic would require new second-face information; it is not inherited from Stage13.

### 1.4 Relation to perfect cuboids

A perfect cuboid is a member of `C(B)` with all three face predicates equal to one, hence belongs to `T(B)`, not `N_2(B)`. The exact raw-incidence identity below includes triples, but the final upper bound only uses `N_2(B)<=E(B)`. It neither proves `T(B)=0` nor produces a member of `T(B)`. Therefore Stage14 has no perfect-cuboid existence or nonexistence result.

### 1.5 Latest-merged-state inventory

The audit used the state reachable from `main` commit `2c7ec9433edbd4f06f298df73cba9e18e164057a`; no stale branch or older roadmap receiver was substituted.

| Track | Latest authoritative state at the snapshot | Frozen interpretation |
|---|---|---|
| main | 14-4gh plus 14-4ghH, PR #782 | External MAIN first-moment gate unresolved; no 4gi continuation |
| H | 14-4ghH | Clean applicability audit complete; off-the-shelf theorem false |
| t | 14-t157, PR #790 | Final super-Kai fixed-residue long-interval receiver frozen |
| tH | 14-tH33, PR #794 | Negative applicability audit complete; fixed-`U` route blocked at named gate |
| s | 14-s7-164, PR #818 | `PARKED_EXTERNAL_GATE`; no s7-165 and no automatic continuation |
| q | 14-q26, PR #816 | Final reduced-modulus character literature radar; direct theorem count zero; q27 not needed |
| X | 14-Work-coX53, PR #819 | All active analytic routes parked; no common gate or legal cross-promotion |
| toolbox | coX53 final route-classification matrix | Integration/accounting controller complete; `STAGE14_ANALYTIC_AUTOMATIC_NEXT=NONE` |
| num | 14-num-alpha11 plus alpha11-diag11 | Exact B500m numerator census; matched B1m diagnostic; numerical branch parked, asymptotic claim false |
| whole family | X13 theorem retained through coX53 | Current exponent `1/2`; strict sub-square-root false |

---

## 2. Frozen main theorem

### Theorem 2.1 — physical whole-family square-root upper bound

For every `epsilon>0` there are constants `C_epsilon>0` and `B_epsilon>=1` such that, for every real `B>=B_epsilon`,

\[
N_2(B)\le C_\epsilon B^{1/2+\epsilon}.
\]

Equivalently,

\[
N_2(B)\ll B^{1/2+o(1)}.
\]

The quantifier ranges over the entire primitive canonical physical family with integer space diagonal `d<=B`; it is not a fixed-`U`, fixed-cell, fixed-direction, or averaged-over-parameter assertion.

#### Exact meaning and non-claims

The `o(1)` is an exponent loss tending to zero, and the displayed Vinogradov notation is interpreted by the epsilon formulation above. It allows divisor-type and finite-decoration losses such as `exp(O(log B/log log B))`; it does not hide a fixed positive power.

The theorem is not any of the following:

- `N_2(B)~C sqrt(B)` or even `N_2(B) asymp sqrt(B)`;
- a matching lower bound `N_2(B)>=B^(1/2-o(1))`;
- a proof that the true order of growth is square-root;
- a strict power saving `N_2(B)<<B^(1/2-delta)` for some fixed `delta>0`;
- an exact asymptotic constant or a directional asymptotic;
- a perfect-cuboid existence or nonexistence theorem.

---

## 3. Final proof chain in dependency order

Only the active proof chain is included here. Sieve, dispersion, squareclass, Gaussian-prime, and literature-audit routes that did not enter the square-root proof are recorded later as obstruction provenance, not as ingredients of Theorem 2.1.

### Lemma 3.1 — raw pair graph identity

**Statement.** Form a finite simple graph `G_B` whose vertices are primitive oriented Pythagorean face data `F=(S,X,H)` appearing in at least one physical raw two-face incidence of height `d<=B`, and whose edges are raw unordered pairs of integral faces belonging to one physical cuboid. Let `V(B)` and `E(B)` be its vertex and edge counts. Then

\[
E(B)=N_2(B)+3T(B),\qquad E(B)=\frac12\sum_F\deg_B(F).
\]

**Hypotheses.** The Stage14-4ab parameter/fiber multiplicity-one normalization and the frozen orientation convention are used, so one raw incidence is one simple graph edge.

**Conclusion.** `N_2(B)<=E(B)` without assuming `T(B)=0`.

**Dependency.** Exact two-face gluing and multiplicity-one; no analytic theorem.

**Physical-filter preservation.** The graph is built from physical incidences. Triple objects contribute exactly three raw pair edges; exact-two objects contribute exactly one.

**Loss.** None; these are exact identities.

**Whole-family promotion.** The identity already ranges over all physical incidences with `d<=B`.

**Proof of multiplicity one (4ab, transcribed).** For oriented primitive face data
`F_i=(S_i,X_i,H_i)`, a common physical edge has scales satisfying

\[
k_1S_1=k_2S_2.
\]

Put `g=gcd(S_1,S_2)`, `alpha=S_1/g`, and `beta=S_2/g`. Since `(alpha,beta)=1`, every positive solution is

\[
k_1=t\beta,\qquad k_2=t\alpha.
\]

The three physical edges are `t(e_0,x_0,y_0)` with

\[
e_0=g\alpha\beta,\qquad x_0=\beta X_1,\qquad y_0=\alpha X_2.
\]

If a prime divided all three minimal edges, then according as it divides `alpha`, `beta`, or only `g`, primitive-face coprimality would force it not to divide respectively `x_0`, `y_0`, or either nonshared edge. Hence `gcd(e_0,x_0,y_0)=1` and therefore `gcd(e,x,y)=t`. Global primitivity forces `t=1`. Each physical Pythagorean triangle has a unique scale-times-primitive-Euclid decomposition with the shared leg distinguished, and `x<y` removes the remaining face swap. Thus one raw shared-edge incidence has exactly one ordered parameter pair. Triple objects still yield three *different* intended shared-edge incidences; that is the coefficient `3T(B)`, not parametrization multiplicity.

### Lemma 3.2 — uniform elliptic-fiber multiplicity

**Statement.** Uniformly in every active face vertex,

\[
\deg_B(F)\le \exp\!\left(O\!\left(\frac{\log B}{\log\log B}\right)\right)=B^{o(1)}.
\]

Consequently,

\[
E(B)\le \tfrac12 V(B)\max_F\deg_B(F)\ll V(B)B^{o(1)}.
\]

**Hypotheses.** Each Stage14 elliptic fiber has rational `2`-torsion; its model height and the height of every physical point with `d<=B` are bounded by `B^O(1)`. The base field is `Q`.

**Conclusion.** A single prolific fiber cannot contribute a fixed positive power; raw edge count and active-vertex count have the same polynomial exponent.

**Dependency.** Dujella's uniform bounded-height rational-point theorem for elliptic curves with a rational point of exact prime order, together with elementary height comparison for the fixed Stage14 birational maps.

**Physical-filter preservation.** Dujella bounds a larger bounded-height rational-point set. Positivity, canonical chamber, integrality, and third-face masks only reduce it.

**Loss.** `B^o(1)`, uniform in `F`; no fixed power.

**Whole-family promotion.** Uniformity in the active vertex is essential. This is not a fixed-fiber-to-global extrapolation: the maximum degree is bounded uniformly before summing over all `V(B)` vertices.

**Uniformity proof (4ag, transcribed).** The fiber is

\[
E_t:Y^2=X(X-1)(X+t^2),
\]

so `(0,0)` is rational 2-torsion on every specialization. For a physical pair with `d<=B`, `H_1<d` gives polynomial height for the base parameter, while the second-face rational parameter has height `O(B^{1/2})` by the previously proved gluing inequalities. The quartic-to-Weierstrass maps have fixed degree, so elementary Weil-height inequalities bound both the model coefficients and the image point height by `B^{C_0}` for one absolute `C_0`, uniformly in the active face. Dujella's theorem over the fixed field `Q` with prime torsion order `ell=2` therefore gives

\[
\#\{P\in E_t(\mathbf Q):H(P)\le B^{C_0}\}
\le \exp\!\left(O\!\left(\frac{\log B}{\log\log B}\right)\right).
\]

The rational maps have fixed finite degree, and boundary, positivity, integrality, chamber, and third-face conditions only delete points. The constant is independent of the specialization, so taking `max_F` before summing is valid.

### Proposition 3.3 — complete balanced-packet reduction

**Statement.** After the exact Cayley/Gaussian parametrizations, gcd peels, finite sign and 2-primary decorations, and dyadic localization, every active face is covered with `B^o(1)` multiplicity by cells with

\[
\frac{3}{16}\le\theta\le\frac{5}{16},\quad
\frac18\le\phi\le\frac14,\quad
0\le\theta-\phi\le\frac18,\quad
\theta+\phi\ge\frac38,
\]

and common-core size

\[
C=B^{\chi+o(1)},\qquad \chi=2\theta+2\phi-\frac34.
\]

Two complete host bounds are always available:

\[
E_s\le\max(2\theta,1-2\theta),\qquad E_k\le3\theta-\frac14.
\]

The proportional branch has exponent at most `7/16`, and every fixed-power nonproportional cell with `chi>1/4` is empty.

**Hypotheses.** The frozen balanced-strip adapters through Stage14-4cx/4cy and s7-37/40, with their original quantifier order.

**Conclusion.** Only the nonproportional region `chi<=1/4` requires the final reconstruction.

**Dependency.** Exact parametrization, common-factor separation, proportional/nonproportional split, and complete host counts.

**Physical-filter preservation.** Every physical active face enters at least one retained decorated cell; all later masks are restrictive.

**Loss.** `B^o(1)` for dyadic choices, divisor fibers, signs, and 2-primary states. The displayed exponents are complete cell exponents.

**Whole-family promotion.** The strip and branch split cover every decorated physical cell. No fixed-`U` input is invoked.

**Proportional branch proof (s7-37, transcribed).** Write the proportional common scale with same-side and cross-side odd root gcds `K=B^{kappa+o(1)}` and `H=B^{eta+o(1)}`. Exact reducedness gives `(K,H)=1` and `kappa+eta=1/8`. Prime-by-prime Gaussian descent shows `(K,q_xi)=1`; since the common core `C` divides `q_xi`, also `(K,C)=1`. The already proved divisibility `K^2|C u_res` therefore sharpens to `K^2|u_res`. With `u_res<=B^{2theta-2phi+o(1)}`,

\[
\kappa\le\theta-\phi,\qquad
\eta\ge\frac18-\theta+\phi.
\]

The complete fourth-power host count is `E_H<=3phi-1/8-3eta`, hence

\[
E_H\le 3\theta-\frac12\le\frac7{16}
\]

because `theta<=5/16`. The `7/16` bound thus comes from `E_H`, not from the unrelated complete host expression `E_s`.

**Nonproportional high-core emptiness (4cx, transcribed).** Let `C_Cayley|C` be the Cayley-good core, `C_res=C/gcd(C,g_star^2)`, and `J=gcd(C_Cayley,C_res)`. Put `A_C=C_Cayley/J`. The Cayley unit equation and invertibility of the quotient product imply `gcd(C_Cayley,MN)=1`. Since the selected cross-root gcd `H_star` divides the Cayley numerator `M`, `(C_Cayley,H_star)=1`. The elementary identity `A/gcd(A,B)|C/B` for `A,B|C` gives

\[
A_C\mid C/C_{res}=\gcd(C,g_\star^2).
\]

The exact endpoint-small relation `g_star/H_star^2|Omega_1`, with `Omega_1=B^{o(1)}`, implies `A_C|H_star^4 Omega_1^2`. Coprimality cancels all `H_star`-supported prime powers, so `A_C|Omega_1^2` and `A_C=B^{o(1)}`. The remaining lost core `D=C/J` divides `B^{o(1)}H^2`, while exact endpoint-linear identities give `H^2|h_-` and `H^2|h_+`. If the two nonzero endpoint cofactors have total available size `B^{1/2+o(1)}`, the forced divisor `D_0` of exponent `chi` in their product consumes that support. For `chi>1/4`, the forced square/core divisibility exceeds the nonzero endpoint product cap, so the fixed-power cell is empty. For `chi<=1/4`, division by the already charged lost core leaves exactly `B^{1/4-chi+o(1)}` reduced column support.

### Lemma 3.4 — column reconstruction and charged support

In the surviving region set

\[
U=L_x^+,\quad V=L_x^-,\quad \gcd(U,V)=1,
\]

\[
M=4rsXY\epsilon_x\epsilon_k,\qquad N=abcd.
\]

After fixing the common-core data and a legal column sign allocation, the endpoint linear forms reconstruct `(z_1,z_2)` divisor-many, hence reconstruct `M`. The charged fixed-power costs are exactly

\[
\underbrace{\chi}_{C}
+\underbrace{(2\phi-\chi)}_{\text{primitive }(U,V)}
+\underbrace{(1/4-\chi)}_{\text{reduced column support}}.
\]

**Hypotheses.** Nonproportional, `chi<=1/4`, and the once-charged common-core/column quantifier order.

**Conclusion.** The column support costs `1/4-chi`, and `M` fixes

\[
XY=\frac{M}{4rs\epsilon_x\epsilon_k}.
\]

**Dependency.** The cross-root and lost-core peels of 4cx/4cy plus the exact endpoint-linear reconstruction.

**Physical-filter preservation.** Parity, signs, endpoint positivity, and canonical masks are checked after reconstruction and only reject candidates.

**Loss.** `B^o(1)` multiplicity beyond the displayed fixed-power support.

**Whole-family promotion.** It is applied cellwise inside the complete partition of Proposition 3.3; the number of cells is subpolynomial.

**Charged-once audit (4cy and s7-40, transcribed).** The common cross-root gcd satisfies `H|X,Y` and `H|c,d`, hence `H^2|M` and `H^2|N=abcd`. It is coprime to the Cayley-good modulus. One may therefore either divide both Cayley variables by `H^2` without changing that modulus (4cy), or combine `N=N_0(M) mod J` with `N=0 mod H^2` into one class modulo `JH^2` (s7-40). These are the same prime-by-prime fact. They remove `2s` from the later row lift but do not create a second saving: `H` is already the root-gcd variable in the complete host count, and `J` is already part of the once-charged core. This is why the column cost `1/4-chi` and the subsequent divisor fiber may be combined without recharging the lost core.

### Lemma 3.5 — reverse reciprocal divisor reconstruction

**Statement.** With

\[
a=c_x^+,\ b=c_x^-,\ c=c_k^+,\ d=c_k^-,\ p=L_k^+,\ q=L_k^-,
\]

the exact reciprocal equations are

\[
(aU)^2-(bV)^2=4rs\epsilon_kpq,
\]

\[
(cp)^2-(dq)^2=4XY\epsilon_xUV.
\]

For fixed `(U,V,M)` and the already fixed endpoint/2-primary decorations, there are only `B^o(1)` possibilities for `(a,b,c,d,p,q)` and hence for `N=abcd`.

**Proof.** Since `M` fixes `XY`, the positive integer

\[
W_2=4XY\epsilon_xUV
\]

is fixed. On a physical point,

\[
(cp-dq)(cp+dq)=W_2.
\]

A polynomially bounded integer has `B^o(1)` ordered positive divisor pairs. Each pair determines `cp` and `dq`, and divisor factorization gives `B^o(1)` possibilities for `(c,d,p,q)`. For each such tuple,

\[
W_1=4rs\epsilon_kpq
\]

is fixed and

\[
(aU-bV)(aU+bV)=W_1.
\]

Another divisor factorization, followed by divisibility by the fixed coprime `U,V`, gives `B^o(1)` possibilities for `(a,b)`. Multiplying the two subpolynomial fibers remains `B^o(1)`.

**Hypotheses.** Positivity of the two difference-of-square factor pairs and polynomial size of all physical coordinates; exactly the low-core nonproportional cell after Lemma 3.4.

**Conclusion.** The later Cayley congruences

\[
N\equiv M\pmod {C_-},\qquad N\equiv-M\pmod {C_+}
\]

are filters on an already divisor-many set. The row CRT lift is not an independent support variable.

**Dependency.** Lemma 3.4 and the earlier exact reciprocal identities. Only the elementary divisor bound is used.

**Physical-filter preservation.** Integrality, parity, coprimality, squarefree-cell, orientation, root/allocation, canonical and third-face conditions all reduce the reconstructed set.

**Loss.** `B^o(1)` and no fixed power.

**No-double-charge rule.** The common core is charged once in the primitive-pair/column support. The reverse step uses exact equalities and divisor multiplicity; it does not charge the core or the CRT row a second time.

**Whole-family promotion.** Uniform in every surviving cell. No theorem about a fixed `U` or a different charged measure is promoted.

### Proposition 3.6 — active-face square-root bound

On `chi<=1/4`, Lemmas 3.4–3.5 give the nonproportional complete exponent

\[
E_{\rm RRF}\le \chi+(2\phi-\chi)+(1/4-\chi)=1-2\theta.
\]

Now split the complete balanced strip:

- proportional branch: `E<=7/16<1/2`;
- nonproportional and `theta<=1/4`: `E<=E_k<=3theta-1/4<=1/2`;
- nonproportional and `theta>=1/4`: cells with `chi>1/4` are empty, and otherwise `E<=1-2theta<=1/2`.

Thus every physical cell is bounded and

\[
V(B)\ll B^{1/2+o(1)}.
\]

**Dependencies.** Propositions 3.3 and Lemmas 3.4–3.5.

**Loss.** Only `B^o(1)` cell/decorative/divisor factors.

**Whole-family promotion.** The cases are exhaustive and are bounds for the same physical active-face measure. The proof explicitly records that 4cz, t78, and tH22 are not cross-promoted, and that X13 needs no auxiliary H theorem.

### Proof of Theorem 2.1

By Lemma 3.1, `N_2(B)<=E(B)`. By Lemma 3.2,

\[
E(B)\ll V(B)B^{o(1)}.
\]

By Proposition 3.6,

\[
V(B)\ll B^{1/2+o(1)}.
\]

Absorbing the product of the two subpolynomial factors proves

\[
N_2(B)\ll B^{1/2+o(1)}.
\]

No subtraction of `3T(B)` and no assumption on perfect cuboids are required for this upper bound.

---

## 4. What was not used in the square-root proof

The proof above uses exact algebra, uniform finite fibers, the elementary divisor bound, complete host counts, and the Dujella degree bound. It does **not** use a squareclass sieve, Gaussian-prime occupancy theorem, Hecke zero-density theorem, dispersion theorem, determinant theorem, genus-one H theorem, or any q26 literature candidate. Those routes continued only to investigate a strict improvement below exponent `1/2` and ended at the gates recorded next.

---

## 5. Final stopping points of the independent routes

### 5.1 MAIN route

**Final receiver before audit**

`FixedAgreementPairKFreeMovingDivisorAllocationTwoLevelCRTFirstMomentAsymptoticOrPowerDeficit`.

The exact H normalization reduces the receiver further. For primitive rectangle variables and squarefree/nested divisor choices `t_p,t_q|m^circ`, with `f|N=t_pt_q`, the live simultaneous roots are

\[
G_-f^2\equiv-G_+N\pmod{2U},\qquad
G_-f^2\equiv G_+N\pmod{2V}.
\]

**Final external gate**

`UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment`.

**H verdict**

`COMPLETE_UNRESOLVED_EXTERNAL_FIRST_MOMENT_GATE`; `OFF_THE_SHELF_THEOREM_APPLICABLE=false`.

**Why existing theorems do not apply directly.** The target is not an ordinary divisor sum in one progression. It has two nested divisors of a moving product, two simultaneous quadratic root conditions modulo the primitive rectangle sides, every-principal-cell uniformity, and retained physical masks. The audited AP/binary-form/divisor-support papers cover nearby single-divisor, averaged, fixed-form, or specially factorable situations, but no exact adapter preserves all variables, uniformity, and masks. Main is therefore blocked by a genuinely external first-moment theorem, not by an unfinished algebraic simplification.

**Restart condition.** Prove the named gate uniformly in the frozen primitive-rectangle range, with either a full-exponent asymptotic, a fixed power deficit on the saturation band, or a dichotomy that disposes of every physical cell, plus an exact mask-preserving parameter map.

### 5.2 T route (fixed-`U` Gaussian route)

**Final receiver**

`SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio`.

For `K=Q(i)`, the packet fixes one odd squarefree modulus `d=B^o(1)`, one invertible Gaussian residue `beta_* mod d`, one strict canonical `D4` sector, lower scale `L_B=2sqrt(B)`, and upper scale `X=L_BR` with fixed-power headroom `R>=B^theta`. The required conclusion is pointwise lower occupancy at relative scale `B^{-o(1)}` for every retained fixed-`U` packet.

**tH verdict**

`COMPLETE_NEGATIVE_UNRESOLVED_SUPER_KAI_INDIVIDUAL_RESIDUE_GATE_AUDIT`; `DIRECT_THEOREM_APPLICABLE=false` on the final super-Kai range.

**Final obstruction.** Kai/Mitsui matches the individual residue and archimedean sector geometry and is direct in the completed safe range

\[
d^2\le \exp(\sqrt{\log X}/C_K).
\]

The final packet assumes the opposite inequality. Fixed-power headroom makes subtraction of the lower endpoint harmless, but it does not enlarge the modulus/conductor range. Stucky reaches a short Gaussian sector only for the conductor-one angular family and not one growing ordinary residue. Log-free Hecke zero-density and least-prime results give ingredients or existence, not the required density in every fixed residue. Bombieri–Vinogradov/BDH results average over moduli or residues and cannot be charged to this one packet without an exceptional-set-to-Stage14-measure adapter. Prime-product ray-class representation is not single-prime density.

**Why T stops.** Its remaining obstacle is analytic uniformity in a moving conductor and one prescribed residue, not the MAIN nested-divisor first moment and not the S conditioned-character measure.

**Restart condition.** Prove the named pointwise lower-ratio theorem beyond the Kai envelope, or prove an exact Stage14 adapter that turns an averaged theorem into the required every-packet statement while paying the exceptional set in the fixed-`U` physical measure.

### 5.3 S route (conditioned character/discrepancy route)

**Final receiver**

The terminal algebra is a valuation-averaged reduced-modulus character principal-domination problem, in two non-interchangeable charged measures: a scalar fixed-`E` variant and a polynomial outer `(E,m)`-pair variant. In the last notation,

\[
J_\nu=S_\nu(\rho_\nu),\qquad P_\nu=A_0/\varphi(q),
\]

where `J_nu` is the moving target-class mass and `P_nu` is the principal average.

**How far exact algebra peeled the problem.** S completed the second reverse encoding, self-coupled modulus cancellation, q17 kernel reidentification, the conditioned-measure firewall, good-packet intersection/indicator first-moment equivalence, moving common-core plus two coprime sides, unit/nonunit character splitting, valuation reduction, and recombination. It also proved:

- the relevant character family cannot uniformly collapse to `B^o(1)` characters on positive-exponent moduli;
- the naive `L^1` Fourier bound loses `phi(q)` and Parseval alone supplies no target-class lower bound;
- an abstract nonnegative mass distribution can have zero mass at the target class, so total mass and `L^2` control do not logically imply principal domination. This is a theorem-contract countermodel, not a physical cuboid counterexample.

**Final decision**

`PARKED_EXTERNAL_GATE`. Stage14-s7-164 found no exact mask-preserving adapter to Nguyen, Irving, Rodgers–Soundararajan, Frei–Sofos, or the other q26 candidates. There is no `s7-165`. The internal exact-reduction sequence is exhausted at the stated receiver.

**Restart condition.** Supply one of:

1. a new exact structure collapsing the moving target residue/character family;
2. a uniform target-class principal-domination theorem with the common-core, valuation, every-cell, and post-mask quantifiers;
3. an explicit measure-preserving adapter to an existing theorem.

The scalar and polynomial measures must remain separate unless a new pair-to-scalar host adapter is actually proved.

---

## 6. Audit of the long S <-> X exchange

### 6.1 Audit verdict

No first broken stage or blast radius was found. The later S/X sequence is a one-way refinement of the theorem object, not a chain of exponent improvements and not a license to recharge old savings. The final coX53 classification correctly parks all active analytic routes.

The controls that make this conclusion possible are explicit in the merged records:

- `CONSUMED` marks an exact adapter already incorporated into the next receiver;
- `SUPERSEDED` retires an older receiver after a strictly sharper exact normal form;
- `RECHARGE_FORBIDDEN` prevents its fiber, support reduction, second moment, or saving from being billed again;
- scalar fixed-`E` support and polynomial outer `(E,m)` support remain distinct;
- identification of an algebraic kernel with q17 does not identify its charged measure;
- `B^o(1)` fibers certify equivalence/multiplicity only and are not counted as a fixed-power saving;
- physical masks and the every-retained-cell quantifier remain attached through the progression.

### 6.2 Representative receiver progression

| Integration stage | Genuine refinement | Accounting firewall |
|---|---|---|
| ccX41 -> cdX42 | Common host algebra is separated from charged support; the first reverse layer is consumed and a second reverse receiver is exposed. | `SUBPOLYNOMIAL_HOST_FIBER_CANNOT_SCALARIZE_PAIR_SUPPORT`; pair-to-scalar adapter false; first reverse layer cannot be recharged. |
| ceX43 -> cfX44 | The second reverse weight/support first moment is encoded exactly; self-coupled modulus cancellation identifies the inner reciprocal-CRT kernel with q17. | Support-to-moment and multiplicity adapters consumed once; q17 kernel reused structurally, not its deficit; q17-to-S conditioned-measure adapter false. |
| cgX45 -> ciX47 | The conditioned-kernel measure firewall is made explicit; the target becomes lower coverage of the q17-good-packet pushforward intersection. | Identical kernel does not imply measure transfer; scalar/pair theorem species count remains two; good-hit fibers cannot be recharged. |
| cjX48 -> ckX49 | Intersection coverage is rewritten as an indicator first moment and then as a joint filtered-`tau_3`/q17 CRT incidence. | The second moment is automatically controlled and therefore superseded as an independent gate; q17 witness multiplicity is not a saving. |
| clX50 -> cmX51 | Joint incidence is peeled to a moving common core with two coprime sides, then split into unit and nonunit character strata. | Common-core side decomposition is consumed once; no positive-density factorization is silently assumed. |
| cnX52 -> s7-162..164 -> coX53 | Unit/nonunit strata are recombined over valuation-reduced moduli; character complexity and target-class logic are audited; literature adapters fail; S is parked. | Separate unit/nonunit gates are superseded, not accumulated; q26 is radar only; automatic continuation is set to none. |

### 6.3 Specific prohibited errors checked

**Receiver renaming.** Names became longer because exact couplings and quantifiers were retained. Each representative transition above either proves a new identity/equivalence or removes an invalid inference. The last three S stages do not claim mathematical progress after the no-go: they test character complexity, identify the precise logical gap, and park.

**Reappearance under another name.** q17 reappears only as the same reciprocal-CRT inner kernel. cfX44/cgX45 explicitly forbid importing q17's unconditioned conclusion into S's conditioned measure. The old filtered-`tau_3` obstruction and the independent second-moment gate are marked superseded.

**Double counting `B^o(1)`.** Finite or divisor-many fibers are used to preserve exponents when changing coordinates. They do not pay for a principal-class lower bound, an exceptional set, or a second fixed-power support reduction.

**Scalar versus polynomial measure.** ccX41 onward states that a scalar fixed-`E` theorem and an outer `(E,m)`-pair theorem are distinct species. `PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false` remains invariant to coX53.

**q17 recharge.** q17's kernel search is `CONSUMED`; `Q17_INNER_KERNEL_RESEARCH_RECHARGED=false`. Only the algebraic normal form is reused.

**Physical measure and quantifiers.** The residual root/canonical/allocation/cell/post-column mask remains separately charged after the arithmetic principal-domination estimate. No average-over-moduli theorem is substituted for an every-retained-cell statement.

---

## 7. Whole-family exponent progression

The following table contains only milestones that the cited merged stage itself labeled as the current physical whole-family/global upper bound. Intermediate local, fixed-`U`, branch-only, or diagnostic exponents are excluded. Every entry before `1/2` is superseded as a current theorem but retained as history.

| Exponent | Canonical stage(s) | Content commit on current tree | Status now | What changed |
|---:|---|---|---|---|
| 41/42 | s6-00 / 4bk | `0bde1bfd…` / `8656a2b7…` | SUPERSEDED | First post-local whole-family architecture. |
| 61/63 | 4bq | `df15c152…` | SUPERSEDED | Good-cell residual closed by diagonal pairs. |
| 20/21 | 4br / 4bs | `7893bc9b…` / `87d260f8…` | SUPERSEDED | Cross-factor threshold optimization and barrier. |
| 18/19 | s7-08 / 4bw | `3c45ef9d…` / `aa361f21…` | SUPERSEDED | Shared-xi cell switch. |
| 15/16 | 4bx | `bccfe450…` | SUPERSEDED | Thick-packet square-sieve optimization. |
| 13/14 | s7-10 / 4by | `ce6f1104…` / `4b690088…` | SUPERSEDED | Uniform two-cell mixed transform. |
| 10/11 | s7-12 | `e35ffe75…` | SUPERSEDED | Unbalanced-denominator bound. |
| 9/10 | 4ca | `aebf9898…` | SUPERSEDED | Dyadic short-denominator bound. |
| 7/8 | s7-13, PR #434 | `ff6ac72c…` | SUPERSEDED | Full-coordinate refinement. |
| 3/4 | X7, PR #519 | `9a251851…` | SUPERSEDED | Gaussian quotient/resultant minimax. |
| 2/3 | X8, PR #522 | `64a8d11c…` | SUPERSEDED | Two-thirds minimax promotion. |
| 5/8 | s7-31 / X9, PR #525 | `c06a48a7…` / `ef51a023…` | SUPERSEDED | Removed common-gcd square-root loss and classified the boundary. |
| 19/32 | 4cu | `9ede6a8a…` | SUPERSEDED | Low-core nonproportional improvement. |
| 47/80 | s7-34 | `db10d06a…` | SUPERSEDED | Fourth-power root transfer. |
| 7/12 | 4cv | `ee82cc4e…` | SUPERSEDED | Row/column reconstruction. |
| 4/7 | s7-35 | `461f7c15…` | SUPERSEDED | Endpoint-small extra-gcd collapse. |
| 9/16 | s7-36, PR #546 | `fd1df2a9…` | SUPERSEDED | Row/column and proportional bounds combined. |
| 19/34 | X11, PR #550 | `91c97374…` | SUPERSEDED | Proportional root-gcd decomposition. |
| 71/128 | X12, PR #556 | `45a84b77…` | SUPERSEDED | Lost-core fourth root coupled to column cofactor. |
| 61/112 | 4cw, PR #562 | `01a2481e…` | SUPERSEDED | Full-row fourth-root theorem. |
| 17/32 | s7-39 | `7d8e653d…` | SUPERSEDED | Cayley residual disjointness. |
| 23/44 | 4cy, PR #569 | `6468ba95…` | SUPERSEDED | Cross-root square row reduction. |
| **1/2** | **X13, PR #580** | `3ff32625…` (merge `6d0608d6…`) | **ACTIVE** | Reverse reciprocal divisor reconstruction eliminates the row-lift support. |

The final interpretation is deliberately limited: current methods prove a square-root upper bound, while a strict sub-square-root power saving and a matching lower bound remain unresolved. The table does not claim that `1/2` is the natural or true scale.

---

## 8. External theorem and literature contracts

### 8.1 Contract table

| Input | Exact hypothesis / parameter map | Uniformity, conductor, modulus, support | Physical compatibility | Verdict | Role in final proof |
|---|---|---|---|---|---|
| Marta Dujella, *Uniform Bounds for the Number of Rational Points of Bounded Height on Certain Elliptic Curves*, arXiv:2312.03655; Acta Arith. 217 (2025) | Fixed field `Q`; each Stage14 fiber has rational exact 2-torsion; model and physical point heights are `B^O(1)` | Uniform in the elliptic curve within the theorem's torsion class; bounded-height count `exp(O(log B/log log B))` | Yes; physical points form a subset of the bounded-height rational points | **DIRECT** | **Used** in Lemma 3.2 to obtain uniform `B^o(1)` graph degree |
| Elementary divisor bound `tau(n)=n^o(1)` | All reconstructed integers are positive and polynomially bounded in `B` | Uniform for every integer in the packet; no modulus/conductor issue | Yes; all physical filters only reduce factor pairs | **BACKGROUND/DIRECT** | **Used** in Lemma 3.5 |
| Frozen Stage12/13 exact-one theorem contract | Same primitive/canonical population and cutoff; exact-one main term | Upstream asymptotic, not an exact-two exponent theorem | Yes | **BACKGROUND_UPSTREAM** | Used only to define the interface and motivation; not used to prove `1/2` |
| Mitsui / Wataru Kai, arXiv:2209.11816v2 | `K=Q(i)`, one residue, fixed archimedean sector; Kai retains possible Siegel term | Direct while `d^2<=exp(sqrt(log X)/C_K)`; cumulative subtraction valid with fixed-power headroom | Yes in the tH31 safe branch | **DIRECT in safe subrange; BLOCKED at final T gate** | Not used in Theorem 2.1; used only to close one fixed-`U` depletion mechanism |
| Joshua Stucky, arXiv:2008.11325 | Gaussian primes in a narrow sector and norm interval | Comparator at `B^(7/20+epsilon)` after dropping growing ordinary residue; angular conductor-one | Dropping the residue changes the T object | **NEAR / COMPARATOR** | Radar/audit only |
| Thorner–Zaman, arXiv:1510.08086 and 1604.01750 | Hecke zero-density/repulsion and least-prime Chebotarev inputs | Ingredients or existence; no every-residue lower density in the super-Kai window | No direct fixed-packet density map | **BACKGROUND / BLOCKED** | Radar/audit only |
| Khale–O'Kuhn–Panidapu–Sun–Zhang, arXiv:2008.09677; Smith, arXiv:1210.3862/3863 | Short interval/sector or number-field BDH after averaging | Averaged over modulus/residue families | Needs an unproved exceptional-set-to-fixed-`U` measure adapter | **NEAR / BLOCKED** | Radar/audit only |
| Grimmelt–Merikoski, arXiv:2508.17979; Irving, arXiv:1403.8031; Nguyen I/II, arXiv:2308.06839 / 2302.12815; Zhong–Zhang, arXiv:2505.10341 | Divisor functions in AP/binary-cubic, smooth, averaged, or prime-power modulus settings | Do not state the nested two-divisor/two-root every-cell theorem | No exact preservation of moving rectangle variables and masks | **NEAR / BLOCKED** | MAIN-H and q radar only |
| Frei–Sofos, arXiv:1609.04002 | Generalised divisor sums of bounded-complexity binary forms | Fixed admissible forms/number-field setting | No exact bounded-complexity encoding of the witness-dependent Stage14 family | **NEAR / BLOCKED** | MAIN/S radar only |
| Rodgers–Soundararajan, arXiv:1610.06900 | Variance of divisor sums in AP | Averaged variance over residue classes/moduli | Does not imply a lower bound at the moving target class in every cell | **NEAR / BLOCKED** | q26/S radar only |
| Ford divisor-in-an-interval theorem | Single-divisor support in an interval | Single divisor, not nested simultaneous CRT roots | Incomplete parameter map | **NEAR / BLOCKED** | MAIN-H radar only |
| Xie, arXiv:2606.30567; Deshouillers–Gun–Ramaré–Sivaraman, arXiv:2210.11051 | Small products of prime ideals/ray-class representations | Product representation or upper bounds, not single-prime density | Does not meet final T lower-ratio contract | **BACKGROUND / TOO WEAK** | tH33 radar only |

### 8.2 Contract discipline

Only Dujella's theorem and the standard divisor bound enter the Stage14 square-root proof. Kai/Mitsui is genuinely applied only inside the separately audited tH31 safe subrange and is never promoted to the whole family. Every q26 candidate remains a literature-radar entry. Failure to find a direct theorem is an applicability result, not evidence that the requested theorem is false.

---

## 9. Numerical route: exact but diagnostic only

The exact alpha engine completed the canonical census through `B=500,000,000`:

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(1374,1371,750),\quad N_2=3495,\quad T=0.
\]

The predeclared three-transition stability gate failed, and later matched-denominator diagnostics through `B=1,000,000` found only `N_2=255` objects for the directional survival comparison. The robust finite signal was `ab<{ac,bc}` at the stated calibration, while `ac` versus `bc` was unresolved. The apparent `2:2:1` direction vector remained compatible with finite-count noise and was not promoted to an asymptotic law.

The numerical branch is parked after alpha11-diag11. It may reopen only for a materially larger matched raw-face denominator census or a proof-side predeclared directional prediction. Its finite `T=0` observation is not a perfect-cuboid nonexistence proof, and its failed operational stability gate neither proves nor refutes any asymptotic.

---

## 10. Open problems and theorem-level restart conditions

| Open statement | Frozen status | Concrete restart condition |
|---|---|---|
| Matching lower bound, e.g. `N_2(B)>=B^(1/2-o(1))` | UNPROVED | Construct a whole-family physical subfamily with controlled injectivity and square-root-many members, or prove a lower first moment with all primitive/canonical/third-face filters. No current receiver supplies this. |
| True asymptotic order of `N_2(B)` | UNPROVED | Combine comparable upper and lower bounds, or an asymptotic theorem. The present upper bound alone is insufficient. |
| Strict `B^(1/2-delta)` saving | UNPROVED | Close every square-root saturation packet. Sufficient restart inputs include `UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment`, `SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio` plus a fixed-`U` promotion adapter, or S's valuation-averaged target-class domination in both charged measures. |
| Exact asymptotic constant | UNPROVED | First prove the true order and a whole-family asymptotic with local densities and overlap/multiplicity control. |
| Two-face directional asymptotic law | UNPROVED | Prove asymptotics for each `N_a^(2),N_b^(2),N_c^(2)` under the same cutoff and physical filters. Finite `2:2:1` compatibility is not sufficient. |
| Perfect-cuboid existence/nonexistence | UNPROVED | A separate theorem proving `T(B)` eventually/nonuniversally zero or explicitly producing a triple object. No Stage14 exact-two receiver addresses this. |

No automatic Stage14 analytic continuation is authorized. A restart must identify the exact gate and preserve its charged measure and quantifier order.

---

## 11. Publication-extraction inventory (“buried-gold” audit)

The inventory distinguishes external-review urgency (`P0` highest) from publication potential (`A` highest). Counts used by the final verdict are `P0=3` and `P1=8`.

| ID | Candidate result | Review | Publication | Dependencies | Assessment |
|---|---|---:|---:|---|---|
| BG-01 | Physical whole-family theorem `N_2(B)<<B^(1/2+o(1))` | P0 | A | BG-02, BG-03, BG-04 | Stage14 main theorem; mandatory independent proof-chain review. |
| BG-02 | X13 reverse reciprocal reconstruction and complete square-root promotion | P0 | A | Balanced packet, exact reciprocal identities, divisor bound | Core new closure mechanism; strongest standalone mathematical section. |
| BG-03 | Final closure/obstruction judgment: main, T, S parked with no legal cross-promotion | P0 | B | H, tH33, s7-164, q26, coX53 | Essential for research governance and honest theorem scope; publish mainly as review/appendix. |
| BG-04 | Exact raw-pair graph identity plus uniform Dujella degree bridge | P1 | A | 4ab multiplicity-one; Dujella | Potentially reusable for other overlap counts on elliptic-fiber incidence graphs. |
| BG-05 | Exact two-face gluing and parameter/fiber multiplicity-one adapters | P1 | B | Primitive canonical conventions | Important algebraic foundation; notation-heavy but reusable. |
| BG-06 | Column reconstruction: fixed `(U,V,M)` determines `XY` and endpoint column up to divisor-many fibers | P1 | A | Lost-core/cross-root peels | Plausible standalone lemma when abstracted from Stage14 notation. |
| BG-07 | Row CRT lift is not independent support after reverse reciprocal factorization | P1 | A | BG-06 and exact reciprocal equations | Strong no-double-charge lemma; suitable with BG-02/BG-06 in one paper. |
| BG-08 | Common-core/allocation no-double-charge accounting and overlap separation | P1 | B | s7-46/47 lineage | Transferable proof-audit technique, likely supporting lemma rather than separate paper. |
| BG-09 | Conditioned-kernel measure firewall: identical q17 kernel does not transfer a saving across measures | P1 | B | cfX44/cgX45 | Reusable warning/lemma for analytic reductions with changed outer measures. |
| BG-10 | Scalar fixed-`E` versus polynomial `(E,m)` measure non-equivalence | P1 | B | ccX41 onward | Independent quantifier/measure audit; prevents invalid cross-promotion. |
| BG-11 | Valuation-reduced character recombination and target-class countermodel | P1 | B | cnX52, s7-159..163 | Clean no-go statement; candidate for an obstruction appendix. |
| BG-12 | Exact Stage13 one-face to Stage14 two-face endpoint bridge and conditional survival decomposition | P1 | B | num diag6–8; Stage13 census | Useful for future directional work, but currently partly diagnostic. |
| BG-13 | Routine gcd, parity, divisor-multiplicity, dyadic, and height audits | P2 | C | Local stage files | Necessary verification material, not separate publication targets. |
| BG-14 | Exact alpha census through B500m and matched survival diagnostics through B1m | P2 | C | Validated enumerators and SHA locks | Reproducibility/data appendix only; no asymptotic evidence claim. |
| BG-15 | Superseded exponent receivers and failed theorem candidates | P3 | C | Historical routes | Provenance/history only; exclude from the active theorem chain. |

**Standalone assessment.** BG-02/BG-06/BG-07 together form the clearest standalone mathematical candidate: an abstract reverse-reciprocal divisor reconstruction principle that removes an apparent CRT lift, with the Stage14 square-root theorem as application. BG-04 is a second plausible reusable lemma/note. BG-09–BG-11 are valuable methodological results but are better presented as rigorous obstruction/accounting appendices unless a broader family of applications is developed.

---

## 12. Final route matrix

| Route | Final mathematical state | External gate | Automatic next |
|---|---|---|---|
| MAIN | Exact primitive-rectangle nested K-free two-level CRT divisor-root first moment isolated; H complete | `UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment` | NONE |
| T | Fixed-`U` Gaussian packet reduced to one residue/sector with super-Kai modulus; tH33 complete negative applicability audit | `SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio` | NONE |
| S | Exact algebra exhausted at valuation-averaged target-class principal domination in scalar and polynomial measures; s7-164 parks route | New uniform target-class theorem or exact measure-preserving adapter | NONE |
| X/Q integration | coX53 verifies all active routes parked, q26 consumed as radar, q27 not needed | Material new input only | NONE |
| NUM | B500m exact census and B1m matched diagnostic; alpha11-diag11 park recommendation | Larger matched census or predeclared theorem-side prediction | NONE |

---

## 13. Final verdict

The bundle is self-contained as a map of definitions, exact proof dependencies, route stops, non-claims, and restart contracts. It states rather than reproves the one external theorem used quantitatively (Dujella), so the appropriate status is not “external-theorem-free.” No substantive mathematical gap was discovered in reconstructing the merged theorem chain.

```text
STAGE14_FINAL_BUNDLE_STATUS=SELF_CONTAINED_WITH_STATED_EXTERNAL_THEOREMS
STAGE14_MAIN_RESULT=N_2(B) << B^(1/2+o(1))
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
MATCHING_LOWER_BOUND_PROVED=false
TRUE_ORDER_OF_N2_PROVED=false
PERFECT_CUBOID_EXISTENCE_OR_NONEXISTENCE_PROVED=false

MAIN_ROUTE_STATUS=PARKED_EXTERNAL_GATE:UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment
T_ROUTE_STATUS=PARKED_EXTERNAL_GATE:SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio
S_ROUTE_STATUS=PARKED_EXTERNAL_GATE:ValuationAveragedReducedModulusTargetClassPrincipalDominationOrMeasurePreservingAdapter

EXTERNAL_REVIEW_P0_COUNT=3
EXTERNAL_REVIEW_P1_COUNT=8

NEXT_RECOMMENDED_PROJECT_DIRECTION=Stage12-14 publication extraction and independent P0 proof-chain review; reopen Stage14 only on a named material theorem/adapter input
```

---

## 14. Source map

The active mathematical chain is anchored at:

- `stages/stage14/archive/stage14-4ag-kummer-rank-jump.md` — raw-pair graph and uniform elliptic-fiber degree;
- `stages/stage14/14-X13/result.md` — reverse reciprocal reconstruction and square-root closure;
- `stages/stage14/14-4gh/result.md` and `14-4ghH/result.md` — final MAIN receiver and H audit;
- `stages/stage14/14-t157/result.md`, `14-tH31/result.md`, `14-tH32/result.md`, `14-tH33/result.md` — final T receiver and applicability boundary;
- `stages/stage14/14-s7-162/result.md` through `14-s7-164/result.md` — final S no-go and park;
- `stages/stage14/14-q26/result.md` — final literature radar;
- `stages/stage14/14-Work-ccX41/result.md` through `14-Work-coX53/result.md` — accounting and final integration;
- `stages/stage14/14-num-alpha11/result.md` and `14-num-alpha11-diag11/result.md` — latest exact/diagnostic numerical endpoints;
- `stages/stage13/main.md` and Stage14 roadmaps — frozen interface and definitions.

The compact PR/commit/status ledger is maintained separately and embedded in the standalone HTML appendix.
