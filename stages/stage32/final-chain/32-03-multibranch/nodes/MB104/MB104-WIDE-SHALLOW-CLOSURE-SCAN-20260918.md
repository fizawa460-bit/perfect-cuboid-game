# Stage32 MB104 — wide shallow closure scan — 2026-09-18

Status: **ACTIVE SEARCH MODE / BROAD SHALLOW PORTFOLIO / NO MATHEMATICAL CREDIT**

## Operating rule

Do not advance MB104 by taking one parked route and manufacturing its missing adapter.

The purpose of this phase is to search broadly for theorem/geometry/computation routes whose *native conclusion* can close the exact balanced MB104 ray

```
D_l=7lH-4l sum_(p in Sigma)E_p,
|Sigma|=14,
g(normalization)=1,
D_l^2=336l^2,
K.D_l=112l,
Delta=168l^2+56l.
```

A route may need an adapter later, but the shallow scan asks first whether the route has enough asymptotic strength and coverage to close MB104 at all.

One mainbatch invocation may scan 4--6 candidates. No candidate receives DEEP work until it survives two independent kill tests.

## Candidate W1 — Bogomolov--Reider superabundance trap

Idea: use the *existence of superabundance* rather than trying to remove it. Classical Bogomolov--Reider arguments turn a zero-dimensional cluster that fails to impose independent conditions into a rank-two bundle; Bogomolov instability then forces an effective destabilizing divisor of controlled numerical class.

Why it could close: U1 already says the exact genus-one condition is highly obstructed/superabundant. If an actual carrier canonically supplies a special cluster to which Reider/Beltrametti--Sommese applies, the conclusion is an effective divisor on S, not a branch-lift object. The rank-64 Picard lattice can then test the resulting divisor inequalities uniformly in l.

First shallow gate:
1. identify the smallest *standard* cluster attached to an actual integral carrier for which non-surjectivity is automatic;
2. compute c1^2-4c2 asymptotically;
3. stop immediately if the discriminant cannot be positive for any source-complete cluster.

External precedent: Chiantini--Sernesi and Keilen use precisely this mechanism for obstructed nodal/equisingular families.

Priority: **HIGH**.

## Candidate W2 — symbolic-power / Waldschmidt effectivity obstruction

Idea: forget genus one temporarily and attack the stronger prerequisite that the class lD1 be effective. On the canonical model, the class corresponds to a degree/contact ray with multiplicity proportional to 4l at the fourteen selected A1 nodes. This is a symbolic-power/Waldschmidt/Seshadri problem for the exact 14-node configuration.

Why it could close: proving the asymptotic vanishing threshold is strictly larger than the ray ratio excludes *every* l before singularity/genus questions arise.

First shallow gate:
1. source-lock the exact local translation between coefficient -4l E_p and symbolic vanishing order at an A1 node;
2. compute a cheap lower bound for the Waldschmidt/effective threshold using known conics, hyperplanes, fibrations and Aut-orbit incidence;
3. if the ray is already safely inside the effective cone, park; if it lies on/outside the boundary, promote.

No section enumeration in the first gate.

Priority: **VERY HIGH**.

## Candidate W3 — Aut(S)-norm / invariant-section obstruction

Idea: if a section cutting a hypothetical lD1 exists, multiply its Aut(S)-translates over a support orbit. The norm is an invariant section whose divisor has computable total degree and amplified vanishing at the full node orbit.

This is different from H1: H1 compared C with one translate by Bezout/intersection. W3 uses the product of all translates and the invariant ring / invariant divisor cone.

Why it could close: a large symmetry orbit may convert a 14-node local condition into a 48-node uniform vanishing condition. If invariant sections of the required weight cannot vanish that much, all l are excluded.

First shallow gate:
1. compute orbit-incidence multiplicity of each of the 48 nodes under the support orbit;
2. determine the degree/weight of the norm section;
3. compare with the lowest possible invariant divisor generators or a Hilbert-series/valence bound.

Stop if the norm ratio is exactly compatible with a known invariant generator.

Priority: **VERY HIGH**.

## Candidate W4 — 2026 Stoll--Testa K3-quotient pushdown

The 2026 Stoll--Testa paper gives seven coordinate-sign involution quotients of S whose minimal resolutions are K3 surfaces and records
`pi^*pi_*C=C+sigma(C)+exceptional corrections`.

Idea: push the exact active ray through all coordinate K3 quotients and test the resulting classes using K3 intersection/effectivity geometry.

Why it could close: K3 adjunction is much tighter (`K=0`). A quotient image with impossible square/genus/divisibility, or one forced to split into known (-2)-curves, would exclude the carrier uniformly.

First shallow gate:
1. for each coordinate involution and each active support orbit, compute the numerical pushdown class and square only;
2. compare with the K3 lattice and known branch conics;
3. no low-degree enumeration unless one quotient produces a genuinely restrictive class.

Priority: **HIGH**.

## Candidate W5 — higher symmetric-differential exceptional locus

Bruin--Thomas--Varilly-Alvarado and Garcia-Fritz--Urzua already obtain explicit low-genus restrictions on the cuboid surface from symmetric differentials.

Idea: instead of using only their published node-count lower bounds, compute or combine additional explicit symmetric differentials and intersect their induced differential equations. If their common low-genus exceptional locus becomes a finite union of known curves/divisors, the MB104 ray is excluded directly.

First shallow gate:
1. inventory the explicit differential sections/equations already available for the cuboid surface;
2. evaluate whether their common zero/differential locus still contains a positive-dimensional family compatible with the active support;
3. stop if existing equations only reproduce the known "at least two/four nodes" bounds.

Priority: **MEDIUM-HIGH**.

## Candidate W6 — modular-form vanishing / valence on X(8)xX(8)

The box surface is explicitly a quotient of `X(8)xX(8)`.

Idea: pull an effective section in class lD1 to the product and interpret its prescribed node/cusp vanishing as vanishing of a bi-modular form/section. Apply factorwise valence or modular-form slope bounds.

This is not H5/H6 correspondence classification: it attacks the *existence of the divisor section*, not the normalization branches.

First shallow gate:
1. determine the bidegree/weight of the pullback line bundle of D1;
2. translate only divisorial node vanishing, not conductor sheets;
3. compare total required cusp/fixed-point vanishing with the factorwise valence budget.

Priority: **HIGH** if the translation is clean; otherwise park immediately.

## Candidate W7 — cyclic/abelian-cover BMY amplification

H8 tested log BMY directly on `(S,aC+sum b_iE_i)` and found positive slack.

Idea: test whether an actual cyclic or abelian cover branched along the carrier plus fixed divisors produces stronger Chern-number corrections at the singularities than the direct log inequality.

First shallow gate: derive only the leading l^2 coefficient of `c1^2-3c2` after resolution for a generic cover order. If it can never become positive/contradictory, reject without local-resolution work.

Priority: **MEDIUM-LOW** because H8 is strong counterevidence.

## Candidate W8 — simultaneous sign-quotient genus budget

There are several coordinate involutions/K3 quotients and the Beauville/product quotients.

Idea: apply Riemann--Hurwitz simultaneously across the finite family of sign quotients to an actual genus-one normalization. The same supported branches may be forced to contribute to several quotient ramification budgets.

This differs from the parked 28-fibration unit-charge route: the objects are finite involution quotients with exact fixed loci, not arbitrary fibration criticality.

First shallow gate: finite group incidence count of how many quotient involutions necessarily see each of the 14 supported node types. Compare forced total branching with the exact lift genus.

Priority: **MEDIUM**.

## Candidate W9 — finite-characteristic specialization of the effective ray

Idea: effectivity specializes. Seek a good reduction where the specialization of D1 can be tested against a computable nef/effective cone or Frobenius-stable Picard lattice, possibly through a K3 quotient.

First shallow gate: determine whether the active support/class is defined over a bounded number field and whether one fixed good prime can receive every hypothetical divisor class. If not, stop. If yes, test only one or two small primes.

Priority: **MEDIUM**.

## Candidate W10 — ambient complete-intersection fat-point Hilbert function

The canonical model is a `(2,2,2,2)` complete intersection in P6 with explicit equations.

Idea: compute the postulation of the exact fourteen-node fat-point scheme inside the canonical coordinate ring. A uniform Hilbert-series or initial-ideal argument could prove that the graded pieces on the ray `(degree,multiplicity)=(7l,4l)` vanish.

This is the computational version of W2 and can succeed even when a general Seshadri theorem is unavailable.

First shallow gate: l=1 and l=2 exact Gröbner/Hilbert values only, followed by inspection for a monomial/semigroup pattern. Do not extrapolate without a proved initial-ideal or Rees-algebra statement.

Priority: **HIGH**.

## Candidate W11 — elliptic-normalization linear-series collapse

On the active equality ray the 14 supported node fibers contain exactly `14*8l=112l=d` normalization points, and the support lies in the retained P5 incidence configuration.

Idea: use the induced `g^6_{112l}` on the elliptic normalization directly. Hyperplanes through the node support give exact large effective divisors on the elliptic curve; multiple independent hyperplanes/subspaces may force Abel--Jacobi or linear-series relations incompatible with birationality.

First shallow gate: count the independent hyperplane/subspace divisor identities that follow from the actual node positions, before introducing any product-cover lift. Stop if they reduce exactly to the already-retained Beauville equality/eta relations.

Priority: **MEDIUM-HIGH**.

## Candidate W12 — receiver-preserving toric/Gröbner degeneration

Idea: choose an explicit weight degeneration of the four quadrics defining the box surface and of the fourteen-node fat-point ideal. If the initial system has no section on the target ray, semicontinuity can obstruct the general/original system.

First shallow gate: verify direction of semicontinuity and whether nonexistence on the initial fibre implies nonexistence on the original fibre. If the implication goes the wrong way, reject immediately.

Priority: **LOW-MEDIUM**.

## Wide-scan execution order

Do not process these one at a time to completion.

Round A: W1, W2, W3, W4, W6.
Round B: W5, W8, W10, W11.
Round C only if needed: W7, W9, W12 plus newly discovered routes.

For each candidate record only:

```
native closing statement
does it cover all l?
does it cover current active support/e?
one cheap numerical/source test
fatal counterexample / known wall
PASS-TO-SECOND-SCAN | DROP | UNCLEAR
```

No missing adapter may receive its own research branch during this phase.

## Credit firewall

This document is a search portfolio only. It proves no exclusion and changes no mathematical credit.


## Newly generated direct-closing candidates after Round B

### W13 — stable factorization / fixed-component section-ring theorem

W10 showed that the ray is effective, so vanishing of the whole graded piece is impossible.  A stronger direct target is instead:

```
every section of O_S(lD_1) factors through a fixed known curve/component
```

for every `l>=1`.

This would exclude an irreducible carrier even though `h^0(lD_1)` is large.

First shallow gate: test whether the known zero-pairing quartics or another explicit curve has zero restriction for the entire `l=1` system. If not, drop the stable-factorization architecture before any section-ring computation.

Priority: **HIGH**.

### W14 — zero-quartic restriction-map obstruction

For every active balanced support and every zero-pairing elliptic quartic `Q`, retained work proves

```
D_1.Q=0,
O_Q(D_1) ~= O_Q.
```

What is not known is the map

```
H^0(S,O_S(lD_1)) -> H^0(Q,O_Q) ~= C.
```

If this map is zero, `Q` is a fixed component of every effective divisor in `|lD_1|`, directly excluding an integral carrier. If it is nonzero, this particular fixed-component route dies cleanly.

First shallow gate: use the exact sequence for `D_1-Q` and Riemann--Roch/intersection data to determine the `l=1` restriction map or reduce it to one exact cohomology dimension.  No branch-lift data are required.

Priority: **VERY HIGH**.

### W15 — simultaneous zero-quartic restriction rank

The active `000707` support has two zero-pairing quartics. Even if each individual restriction map is nonzero, the joint map

```
H^0(S,O_S(lD_1)) -> C^2
```

may have rank one or satisfy a fixed relation forced by the section geometry. A rank defect that forces one quartic component in every divisor would again close irreducibility directly.

First shallow gate: only after W14 shows both individual maps can be nonzero, test the joint rank at `l=1`.

Priority: **HIGH CONDITIONAL ON W14**.


## Archive semantic precheck rule after Round C

Before promoting any new wide-scan candidate, search the retained MB104 archive semantically, not only by remembered filename.  The W14 restriction-map idea was independently rediscovered even though the retained archive already contained the exact primitive-rank resolution.

A rediscovered route is marked `DROP_ALREADY_RETAINED`, not promoted.

## Round D genuinely untested candidates

The archive filename/semantic precheck found no retained MB104 leaf explicitly implementing the mechanisms below.

### W16 — minimal Cayley--Bacharach conductor subcluster

W1 failed only because the **full** genus-defect cluster has too large a `c2` for Bogomolov instability.

New idea: use the adjoint/conductor Cayley--Bacharach property of a normalization-genus-one integral curve to extract a *minimal obstructing subcluster* whose length may be much smaller than the full
`Delta=168l^2+56l`.

Numerical shallow gate: determine whether standard Cayley--Bacharach/Serre construction can force a subcluster length below

```
(D_l-K)^2/4
 =84l^2-56l+4.
```

If no theorem gives such a source-complete subcluster, DROP immediately.  Do not construct the subcluster ad hoc.

Priority: **HIGH**.

### W17 — support-stabilizer carrier dichotomy

The active support stabilizer has order two.

Split a hypothetical carrier into:

```
sigma(C)=C
or
sigma(C)!=C.
```

If invariant, `sigma` acts on the genus-one normalization and exact Riemann--Hurwitz/quotient geometry becomes available.

If non-invariant, compare `C` with the same-class translate `sigma(C)` and ask whether the exact 14-node / 8l-branch packet forces more local intersection than

```
C.sigma(C)=D_l^2=336l^2.
```

First shallow gate: check whether retained landing freedom already gives a compatibility witness with zero forced strict-transform intersection. If yes, DROP the non-invariant half; if the invariant half also has a compatible involution type, DROP the route.

Priority: **MEDIUM-HIGH**.

### W18 — elliptic projection / secant-center capacity

The normalization line bundle

```
L=nu^*O_S(H)
```

has degree `112l`, while the 7 ambient coordinates define only a `g^6_{112l}`.

At each supported box node, `8l` distinct normalization points are identified by this linear series.

Interpret the map as a projection of the complete elliptic normal curve in `P^(112l-1)`.  Each identified cluster forces the projection center to meet a corresponding secant span.

First shallow gate: dimension-count the simultaneous secant-center conditions for fourteen clusters of size `8l`.  If the Grassmannian of projection centers still has positive linear-in-`l` slack, DROP without geometry.

Priority: **MEDIUM**.

### W19 — adaptive Wronskian / unbounded-jet budget

The fixed-jet wall only kills bounded jet depth.  Test an order/depth growing with `l`.

For the genus-one `g^6_{112l}`, the total ramification weight of a basepoint-free linear series is linear in degree.  Compare the maximal global Wronskian/jet budget with the amount required to distinguish or regularize `8l` minimal branches at 14 nodes.

First shallow gate: leading-coefficient comparison only.  If the available Wronskian budget is at least the required branch cost with positive slack, DROP.  No explicit high-order differential is built.

Priority: **MEDIUM-HIGH**.

### W20 — support-hyperplane residue / Abel relation

The unique support hyperplane cuts the normalization in exactly the `112l` supported points, with no residual degree.

Take ratios of the remaining ambient coordinate sections to this saturated hyperplane section. Their poles are exactly those `112l` points.  Residue/Abel constraints group the poles into fourteen fibers over fixed box nodes.

First shallow gate: compute the rank of the first residue-moment relations from the exact 14-node configuration. If the nullspace still has dimension growing with `l` or the relations reduce to ordinary Abel's theorem already built into `O_E(B)`, DROP.

Priority: **MEDIUM**.

Round D order:

```
W16, W17, W18, W19, W20
```

One cheap test each; no adapter subprojects.


## Round D disposition

Round D screened five archive-prechecked routes:

```
W16 minimal Cayley--Bacharach conductor subcluster  DROP
W17 support-stabilizer carrier dichotomy            DROP
W18 elliptic projection / secant-center capacity    DROP
W19 adaptive Wronskian / unbounded-jet budget       DROP
W20 support-hyperplane residue / Abel relation      DROP
```

No second-scan or DEEP candidate remains.

Key shallow reasons:

- W16: the canonical linear-size landing cluster is the complete intersection `C intersect B_E`; its Serre bundle is the tautological split bundle `O(D_l) direct_sum O(B_E)`.
- W17: the unique support involution pairs all fourteen supported nodes with no fixed supported node; both invariant and non-invariant carrier branches remain packet-compatible.
- W18: simultaneous collision constraints leave at least `112l` raw linear parameters, or `112l-49>0` after target-basis quotient.
- W19: equal images of distinct normalization points force no ramification; even an artificial unit charge uses only `112l` of total Wronskian weight `784l`.
- W20: the support-hyperplane divisor is tautologically the divisor of one section of a degree-`112l` elliptic line bundle; principal parts remain free.

## Round E candidates — archive semantic precheck passed

Repository semantic searches found no retained MB104 leaf explicitly carrying these mechanisms.

### W21 — first-jet bundle / polar singularity capacity

For a divisor section of `L=O_S(D_l)`, singular points are zeros of its first jet.  The first jet bundle `J^1(L)` has rank three and an exact Chern class computable from

```
K^2=16,
c2(S)=80,
K.D_l=112l,
D_l^2=336l^2.
```

First shallow gate: compare `c2(J^1(L))` with the required total defect `168l^2+56l`.  If the jet-bundle capacity is much larger, DROP immediately; no polar scheme is constructed.

Priority: **HIGH** because it attacks the full singularity budget globally.

### W22 — stable-map virtual dimension / normal-sheaf negativity

For a genus-one normalization map `f:E->S` in class `D_l`, the expected stable-map dimension and the degree of `f^*T_S` are controlled by `-K.D_l=-112l`.

First shallow gate: determine whether this negativity is an actual nonexistence theorem or only an obstruction/rigidity statement.  If negative virtual dimension merely means isolated obstructed maps can occur, DROP.

Priority: **MEDIUM**.

### W23 — Castelnuovo--Severi on the retained joint factor pair

The retained equality geometry gives a birational map

```
E -> P1 x P1
```

of bidegree

```
(28l,28l) or (56l,56l).
```

First shallow gate: apply Castelnuovo--Severi / arithmetic-genus inequalities in both directions and ask whether genus one is incompatible with birationality plus those degrees.  If the inequalities are only upper bounds permitting genus one, DROP without passport work.

Priority: **MEDIUM-HIGH**.

### W24 — dualizing conductor / different identity

For an integral Gorenstein divisor `C in |D_l|`, adjunction gives

```
omega_C ~= (K_S+C)|_C.
```

Pull this to the elliptic normalization and compare the different/conductor degree with

```
(K_S+D_l).D_l
```

and the exact defect `2 Delta`.

First shallow gate: check whether the resulting equality is stronger than the genus formula or merely restates it.  If tautological, DROP.

Priority: **MEDIUM**.

### W25 — Lefschetz-pencil singular-fiber budget

Embed a hypothetical genus-one member inside a pencil of `|D_l|` and compare its defect with the total topological singular-fiber budget after blowing up the `D_l^2` base points.

First shallow gate: compute only the total Euler/Lefschetz budget coefficient and compare it with `Delta=168l^2+56l`.  If one genus-one fiber fits comfortably inside the total budget, DROP.

Priority: **MEDIUM**.

Round E order:

```
W21, W22, W23, W24, W25
```

One cheap test each; no adapter construction and no deep continuation inside the same round.
