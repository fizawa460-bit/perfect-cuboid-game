# Research Arsenal × Literature Strengthening Audit — Phase 5

Status: `LITERATURE_DISCOVERY_ONLY`

```text
ARSENAL_BASE_MAIN=9306238c7ada55e31311245019d6b7e474ad837f
STAGE36_EXCLUDED=true
STAGE35_PROVISIONAL_COMPARISON_HEAD=3fc684677ef1570a820420079088667f558e0983
ARSENAL_AUTHORITY_CHANGED=false
STABLE_ID_CREATED=false
```

This phase compares the frozen Arsenal finite-group, lattice, symplectic and equivariant interfaces with standard exact structure theorems and algorithms. It does **not** replace source marking, semantic identification, or Stage authority.

## 1. Reviewed Arsenal interfaces

| Card | Frozen role | Phase-5 focus |
|---|---|---|
| `S30-W01` | `FINITE_EQUIVARIANT_ACTION_IDENTIFICATION` | replace brute equivariant relabeling by orbit/stabilizer/transporter structure where possible |
| `S30-W02` | `SEMILINEAR_GALOIS_DESCENT_ADAPTER` | replace all-element semilinear equality scans by generator/presentation verification when homomorphism hypotheses are certified |
| `S30-W03` | `MARKED_DEFECT_EQUIVARIANT_DESCENT_CLASSIFIER` | orbit/stabilizer and generator-level equivariance algorithms; marked arithmetic relation remains source-bound |
| `S32-PW03` | `LATTICE_IMAGE_HNF_GATE` | canonical exact integer-module image membership via HNF/SNF |
| `S32-PW04` | `FINITE_LATTICE_QUOTIENT_BOUND` | invariant-factor quotient/saturation/reachable-subgroup algorithms without confusing them with classwise bounds or CVP |
| `S32-PW05` | `FINITE_GROUP_EQUIVARIANT_RECONSTRUCTION` | orbital/double-coset reconstruction instead of explicit all-pair propagation when advantageous |
| `S32-PW06` | `BASIS_INDEPENDENT_SYMPLECTIC_TRANSVECTION_PRUNER` | exact F2 symplectic transvection normal form and direction parametrization |
| `S33-PW02` | `FINITE_MODULE_NORMAL_FORM_AND_EXTENSION_GATE` | standard reversible SNF is source anchor/algorithm layer; raw extension/Bockstein data remains separate |
| `S33-PW04` | `EXACT_MARKED_SOURCE_ADAPTER` | literature cannot remove locked marking/source witness obligations |
| `S33-PW05` | `EQUIVARIANT_SOURCE_TARGET_COMPATIBILITY_AUDIT` | module-isomorphism/intertwiner algorithms versus large explicit linear compatibility systems |

### Frozen concrete sizes used only as provenance

- Stage30 exact action orders: arrangement group `24`, modular `PSL_2(Z/4)` image `24`, `SL_2(Z/4)` lift `48`, deck/kernel block order `4`.
- Stage30 final exact endpoint equivariance instance: `24 × 8` checks.
- Stage30 defect population: `|K8|=8`; ordinary orbit sizes `[1,3,3,1]`; eight marked Q-descent singleton classes.
- Stage32 `PW03`: Picard rank `64`, known-curve population `140`.
- Stage32 `PW04`: Smith diagonal `[1,2,2]`, generator orders `[20,20,40]`, reachable shift classes `640`.
- Stage32 `PW05`: `140` labels, group order `1536`, `19,600` ordered pairs.
- Stage32 `PW06`: frozen source instance pruned `16 -> 3`; this count is not reusable mathematics.
- Stage33 `PW05` frozen compatibility audit: `2688` F2 equations in `1792` variables, rank `781`, nullity `1011`; among `1023` nonzero retained source masks, the locked target is unreachable from `23` and reachable from `1000`. These numbers are diagnostics, not a generic theorem.

## 2. Literature anchors

### 2.1 Exact integer normal forms

**R. Kannan and A. Bachem**, *Polynomial Algorithms for Computing the Smith and Hermite Normal Forms of an Integer Matrix*, SIAM Journal on Computing **8** (1979), 499–507, DOI `10.1137/0208040`.

Paper-level algorithm contract recovered in this audit:

```text
INPUT=integer matrix A encoded in binary
OUTPUT=Hermite normal form and Smith normal form plus multiplier matrices
COMPLEXITY=number of algebraic operations and bit lengths of all intermediates polynomial in input length
RECONSTRUCTION=multiplier matrices K,U',K' are produced with AK=HNF and U'AK'=SNF
```

The canonical HNF/SNF output is therefore suitable for exact certificate interfaces. The unimodular multiplier witnesses reconstruct the coordinate change; those multipliers are not themselves a unique semantic marking.

**C. S. Iliopoulos**, *Worst-Case Complexity Bounds on Algorithms for Computing the Canonical Structure of Finite Abelian Groups and the Hermite and Smith Normal Forms of an Integer Matrix*, SIAM Journal on Computing **18** (1989), 658–669, DOI `10.1137/0218045`.

Indexed algorithm bounds:

```text
SNF / finite-Abelian canonical structure: O(s^5 M(s^2))
HNF: O(s^3 M(s^2))
```

This strengthens complexity/implementation guarantees, not Arsenal mathematical credit.

### 2.2 Permutation actions, stabilizers and backtracking

**Á. Seress**, *Permutation Group Algorithms*, Cambridge Tracts in Mathematics 152, Cambridge University Press, 2003, DOI `10.1017/CBO9780511546549`.

Relevant authoritative algorithm families:

- Chapter 4: bases and strong generating sets;
- Chapter 5: stabilizer/orbit/transporter low-level algorithms;
- Chapter 6: nearly-linear-time permutation-group algorithms;
- Chapter 9: backtrack methods.

The structural reduction used here is standard finite G-set theory: a transitive G-set is equivalent to `G/H` for a point stabilizer `H`, and equivariant isomorphism of transitive actions reduces to conjugacy/transporter data for stabilizers. For multiple orbits, match orbit types/multiplicities and solve transporters instead of enumerating arbitrary set bijections.

This may replace candidate **enumeration**, but it does not identify which abstract orbit/stabilizer object is the repo source object.

### 2.3 Matrix-module isomorphism / intertwiners

**A. Chistov, G. Ivanyos and M. Karpinski**, *Polynomial time algorithms for modules over finite dimensional algebras*, Proceedings ISSAC 1997, 68–74, DOI `10.1145/258726.258751`.

Relevant algorithmic problem:

```text
INPUT=finite families of matrices representing modules over a finite-dimensional algebra
TASK=decide module isomorphism / simultaneous equivalence and construct an invertible intertwiner when one exists
FIELD=field input; finite-field instances included
OUTPUT=constructive isomorphism, not a semantic source identification
COMPLEXITY=polynomial-time algorithm in the stated algebra/module model
```

This is a genuine generic replacement for brute-force matrix-intertwiner search in the algebraic layer of `S33-PW05`. It does not prove that a returned intertwiner is the marked geometric/source adapter required by `S33-PW04`.

Adjacent source: **L. Rónyai**, *Computing the structure of finite algebras*, Journal of Symbolic Computation **9** (1990), 355–373, DOI `10.1016/S0747-7171(08)80017-X`, gives polynomial-time structural algorithms over finite fields and constructive matrix-algebra decomposition machinery.

### 2.4 Constructive recognition of classical groups

**P. A. Brooksbank**, *Constructive recognition of classical groups in their natural representation*, Journal of Symbolic Computation **35** (2003), 195–239, DOI `10.1016/S0747-7171(02)00132-3`.

```text
INPUT=generators G <= GL(V), V finite-dimensional over a finite field
APPLICABILITY=G is one of the natural classical groups covered, including Sp(V)
OUTPUT=constructive recognition
COMPLEXITY=polynomial in input length, assuming a discrete-logarithm oracle for the field
```

This is only applicable after the repo has an exact natural matrix representation and the task is recognition of the whole classical group. It does not source-identify a geometric action or a marked line.

### 2.5 Symplectic transvections in characteristic two

**J. McLaughlin**, *Some groups generated by transvections*, Archiv der Mathematik **18** (1967), 364–368, DOI `10.1007/BF01898827`.

**H. S. Pollatsek**, *Irreducible groups generated by transvections over finite fields of characteristic two*, Journal of Algebra **39** (1976), 328–333, DOI `10.1016/0021-8693(76)90080-6`.

These are structure-theorem anchors for groups generated by transvections. Exact theorem numbering was not recovered from the indexed original metadata in Phase 5, so no theorem number is invented here; any Phase-6 promotion using the generation/classification theorem must source-lock the numbered statement from the original text.

For `S32-PW06`, a more elementary exact normal form is already enough:

Let `(V,B)` be a nondegenerate symplectic vector space over `F2`. If `T` is symplectic, `T != I`, and `rank(T-I)=1`, then there is a **unique** nonzero vector `v=im(T-I)` such that

```text
T = t_v,
t_v(x) = x + B(x,v) v.
```

Conversely every nonzero `v` defines such a transvection. Moreover

```text
g t_v g^-1 = t_{g v}.
```

Hence `im(T-I) <= W` is exactly `v in W\{0}`. Therefore the transvection component may be enumerated by at most `2^dim(W)-1` directions rather than by arbitrary operators in `Sp(V)`. This is a derived F2-linear-algebra consequence consistent with the transvection literature; it still requires a repo source proof that the geometric action being used is the relevant transvection.

## 3. Card-by-card hostile comparison

### S30-W01 — finite equivariant action identification

**Verdict:** `STRUCTURE_THEOREM_STRENGTHENING + ENUMERATION_REPLACEMENT + EXTEND_EXISTING + SOURCE_ANCHOR_REMAINS_REQUIRED`.

Current finite relabeling enumeration can be replaced, where the same acting group is explicit, by:

```text
exact G-actions
-> orbit decomposition
-> point stabilizers / orbit type invariants
-> stabilizer conjugacy + transporter calculation
-> equivariant candidates only
-> REPO SOURCE/COMMON ANCHOR
-> semantic adapter credit
```

For linear actions, module-isomorphism algorithms can replace a second layer of candidate search.

**Gain:** potentially changes factorial-size raw bijection search into orbit/stabilizer/transporter computations. The exact reduction depends on orbit multiplicities and stabilizers; Phase 5 does not invent an asymptotic for the concrete Stage30 instance.

**Firewall:** no classification theorem removes Step 5 of the current card. `abstract conjugacy/classification != source marking`.

### S30-W02 — semilinear Galois descent adapter

**Verdict:** `ALGORITHM_STRENGTHENING + ENUMERATION_REPLACEMENT + EXTEND_EXISTING + SOURCE_ANCHOR_REMAINS_REQUIRED`.

If both maps

```text
beta1(g)=sigma(alpha(g))
beta2(g)=c_sigma alpha(theta(g)) c_sigma^-1
```

are independently certified homomorphisms from the same finitely generated group `G`, then equality on a generating set implies equality on all `G`. Thus a complete all-element scan may be replaced by:

```text
certify group presentation / strong generators
+ certify alpha,theta and target operations are homomorphisms
+ verify c_sigma sigma(c_sigma)=1
+ verify beta1(s)=beta2(s) on generators s
+ verify relators/projective-deck convention
```

For tiny frozen groups all-element replay remains a useful hostile certificate, but it need not be the generic mathematical interface.

**Firewall:** the theorem does not generate `sigma`, `theta`, or `c_sigma`; these remain source-derived.

### S30-W03 — marked defect equivariant descent classifier

**Verdict:** `ALGORITHM_STRENGTHENING + ENUMERATION_REPLACEMENT + SOURCE_ANCHOR_REMAINS_REQUIRED`.

Use bases/strong generators, orbit/stabilizer algorithms, and generator-level equivariance instead of a literal `G x D` scan when large. If the marked relation is encoded as a twisted action, semidirect/twisted orbit algorithms may compute classes without enumerating every pair.

**Frozen instance:** `|D|=8`; there is little performance pressure. Generic strengthening is still mathematically clean.

**Firewall:** ordinary orbits, stabilizers, and even a computed twisted orbit relation do not identify the intended arithmetic marked relation unless that relation is source-locked.

### S32-PW03 — lattice image HNF gate

**Verdict:** `ALGORITHM_STRENGTHENING + NEW_GENERIC_ADAPTER + EXTEND_EXISTING`.

Candidate generic interface:

```text
EXACT_INTEGER_MODULE_IMAGE_GATE
input: A: Z^m -> Z^n with locked source/target bases
compute: column/row HNF or SNF + unimodular multipliers
output: canonical image lattice, exact membership test, quotient invariants, reconstruction witness
```

Kannan–Bachem supplies polynomial-time exact normal forms with multiplier matrices.

**Expected reduction:** membership becomes canonical integer linear algebra rather than branch-specific congruence code. This is primarily generality/auditability, not stronger theorem credit.

**Firewall:** changed source marking still requires an adapter; HNF coordinates are not geometry.

### S32-PW04 — finite lattice quotient bound

**Verdict:** `STRUCTURE_THEOREM_STRENGTHENING + ALGORITHM_STRENGTHENING + NEW_GENERIC_ADAPTER`.

SNF can canonically expose the abstract finite quotient and its invariant factors. A composed homomorphism followed by HNF/SNF can also compute the **reachable subgroup** rather than materializing every ambient quotient class.

Potential generic pipeline:

```text
source shift lattice -> quotient presentation
-> reversible SNF
-> image/reachable subgroup via exact homomorphism
-> invariant factors / saturation certificate
-> only then classwise quadratic lower bound
```

For the frozen Stage32 instance there are `640` reachable classes. If the bound depends only on coarser invariant data, quotient structure may avoid enumerating all 640; if the bound genuinely varies class-by-class, exact class evaluation remains necessary.

**Firewalls:** `finite quotient bound != actual quotient enumeration`; `SNF quotient != reachable subset`; `lower bound != exact CVP`.

### S32-PW05 — finite group equivariant reconstruction

**Verdict:** `ALGORITHM_STRENGTHENING + EXTEND_EXISTING + SOURCE_ANCHOR_ONLY` for the core mathematical idea.

The card already uses the standard orbit principle. For a transitive action with stabilizer `H`, ordered-pair orbits (orbitals) can be represented through point-stabilizer suborbits / double-coset data. Thus one need not materialize all `19,600` ordered pairs merely to discover orbit representatives.

Potential algorithm:

```text
validated finite action
-> strong generating set / stabilizer chain
-> orbital or double-coset representatives
-> one source seed per orbital
-> propagate only on demand or materialize with certified coverage
```

The current card remains useful because its fail-closed seed/conflict/coverage contract is repo proof engineering not supplied by an abstract orbit theorem.

### S32-PW06 — basis-independent symplectic transvection pruner

**Verdict:** `STRUCTURE_THEOREM_STRENGTHENING + ENUMERATION_REPLACEMENT + EXTEND_EXISTING + SOURCE_ANCHOR_REMAINS_REQUIRED`.

Direct safe strengthening:

```text
rank(T-I)=1 + T symplectic + T!=I over F2
<=> unique transvection direction v!=0 with T=t_v.

im(T-I)<=W
<=> v in W\{0}.
```

This can replace arbitrary candidate-operator enumeration by direction enumeration in `W` for the transvection component. It also gives exact conjugacy transport `t_v -> t_{gv}` and allows orbit reduction under any independently validated subgroup preserving `W`.

Possible **further** strengthening from McLaughlin/Pollatsek classification is currently `RESEARCH_GAP`: the present card supplies one source-derived transvection constraint, not a source-locked set generating an irreducible transvection group. Required new hypotheses include multiple exact transvections, their generated subgroup, irreducibility, and the exact characteristic-two classification branch.

**Firewall:** the unique algebraic direction extracted from an operator is not automatically the absolute source marking. A source proof still has to identify the geometric action and source-bound `W`.

### S33-PW02 — finite module normal form and extension gate

**Verdict:** `ALGORITHM_STRENGTHENING + EXTEND_EXISTING + SOURCE_ANCHOR_ONLY` for the SNF portion.

Reversible SNF is standard exact algebra. It can be shared with `PW03/PW04` through a generic normal-form adapter. However the card's strongest semantic feature is **not** SNF: it keeps raw mixed-order representatives and the doubling/Bockstein/liftability obstruction.

No normal-form theorem recovers extension data that was discarded. Therefore:

```text
SNF/invariant factors != raw extension class
quotient exponent 2 != every raw lift has order 2
```

remains load-bearing.

### S33-PW04 — exact marked source adapter

**Verdict:** `SOURCE_ANCHOR_REMAINS_REQUIRED`.

Lattice/module canonical forms can normalize coordinates and reduce finite ambiguity, but cannot establish that independently computed coordinates refer to the same geometric marked source. This card is intentionally the semantic boundary literature algorithms must not erase.

### S33-PW05 — equivariant source-target compatibility audit

**Verdict:** `ALGORITHM_STRENGTHENING + ENUMERATION_REPLACEMENT + NEW_GENERIC_ADAPTER + SOURCE_ANCHOR_REMAINS_REQUIRED`.

For the pure module layer, Chistov–Ivanyos–Karpinski supplies a constructive polynomial-time module-isomorphism/intertwiner route. A proposed generic adapter is:

```text
FINITE_MODULE_INTERTWINER_SOLVER
input: source/target modules with exact generator matrices over a field
output: no isomorphism, or a constructive invertible intertwiner / solution algebra
```

The frozen Stage33 calculation already uses linear algebra rather than blind matrix enumeration (`2688` equations / `1792` variables). Therefore the literature gain is mainly a reusable solver abstraction and possible reduction of future brute-force relabeling/intertwiner searches.

Compatible **extension** data may impose additional affine/cohomological equations beyond module isomorphism. A positive module-isomorphism answer does not repair the frozen locked source-target semantic mismatch.

**Firewall:** `existence of intertwiner != semantically correct adapter`.

## 4. Candidate classification summary

| Candidate | Targets | Classification | Direct effect |
|---|---|---|---|
| stabilizer/transporter action matcher | `S30-W01` | `STRUCTURE_THEOREM_STRENGTHENING`, `ENUMERATION_REPLACEMENT` | replace arbitrary relabeling enumeration by orbit/stabilizer data |
| generator-complete semilinear verifier | `S30-W02` | `ALGORITHM_STRENGTHENING`, `ENUMERATION_REPLACEMENT` | prove all-element compatibility from generators once homomorphism/presentation is certified |
| orbit/stabilizer marked-state engine | `S30-W03` | `ALGORITHM_STRENGTHENING` | avoid literal `G x D` scans |
| reversible integer-module normal form | `S32-PW03`,`S32-PW04`,`S33-PW02` | `NEW_GENERIC_ADAPTER`, `ALGORITHM_STRENGTHENING` | shared HNF/SNF/multiplier/image/quotient certificates |
| finite lattice quotient+saturation adapter | `S32-PW04` | `STRUCTURE_THEOREM_STRENGTHENING`, `NEW_GENERIC_ADAPTER` | canonical quotient/reachable subgroup before classwise bound |
| orbital/double-coset reconstruction | `S32-PW05` | `ALGORITHM_STRENGTHENING`, `SOURCE_ANCHOR_ONLY` | one seed per orbital; on-demand propagation |
| F2 transvection direction normal form | `S32-PW06` | `STRUCTURE_THEOREM_STRENGTHENING`, `ENUMERATION_REPLACEMENT` | arbitrary operator scan -> nonzero directions in W |
| transvection-generated subgroup classification | `S32-PW06` | `RESEARCH_GAP` | stronger group-level pruning only after multiple source transvections + irreducibility |
| finite-module intertwiner solver | `S33-PW05` | `NEW_GENERIC_ADAPTER`, `ALGORITHM_STRENGTHENING`, `ENUMERATION_REPLACEMENT` | constructive module isomorphism/intertwiner layer |
| marked source identification | `S30-W01`,`S30-W02`,`S30-W03`,`S32-PW06`,`S33-PW04`,`S33-PW05` | `SOURCE_ANCHOR_REMAINS_REQUIRED` | no literature theorem replaces source semantics |

## 5. Not-applicable / non-replacements

1. Classical-group recognition is `NOT_APPLICABLE` unless the exact repo input is a natural matrix representation of the whole target classical group. Recognizing `Sp(V)` does not identify a geometric source action.
2. Pollatsek/McLaughlin group-generation classification is not yet a direct `PW06` theorem because current input does not certify a generated irreducible transvection subgroup.
3. SNF/HNF cannot replace the `S33-PW02` raw extension/Bockstein gate.
4. Module isomorphism cannot replace `S33-PW04` marked-source equality.
5. Schreier–Sims/orbit algorithms optimize finite reconstruction; they do not generate endpoint or arithmetic theorem credit.

## 6. Credit firewalls

```text
abstract conjugacy/classification != source marking
existence of intertwiner != semantically correct adapter
basis-independent predicate != absolute source identification
normal form != theorem/endpoint credit
finite quotient bound != actual quotient enumeration
transvection classification != given geometric action is that transvection without source lock
SNF quotient != reachable subgroup without exact map/image proof
orbit representative != source-derived semantic label
constructive classical-group recognition != geometric/moduli identification
```

## 7. Phase-6 freeze manifest

| Priority | Candidate | Targets | Classification | Promotion gate |
|---|---|---|---|---|
| P0 | `F2_SYMPLECTIC_TRANSVECTION_DIRECTION_NORMAL_FORM` | `S32-PW06` | `STRUCTURE_THEOREM_STRENGTHENING` + `ENUMERATION_REPLACEMENT` | nondegenerate alternating F2 form; exact source action proved symplectic rank-one nonidentity; source-bound W; no absolute W-line credit |
| P0 | `FINITE_ACTION_STABILIZER_TRANSPORTER_EQUIVARIANT_MATCHER` | `S30-W01` | `STRUCTURE_THEOREM_STRENGTHENING` + `ENUMERATION_REPLACEMENT` | exact common acting group and action conventions; complete orbit/stabilizer/transporter logic; source/common semantic anchor remains mandatory |
| P0 | `GENERATOR_COMPLETE_SEMILINEAR_COMPATIBILITY_VERIFIER` | `S30-W02` | `ALGORITHM_STRENGTHENING` + `ENUMERATION_REPLACEMENT` | certify both sides as homomorphisms from the same generated/presented group; exact sigma/theta/cocycle/deck data; generator + relator replay |
| P1 | `REVERSIBLE_INTEGER_MODULE_NORMAL_FORM_ADAPTER` | `S32-PW03`,`S32-PW04`,`S33-PW02` | `NEW_GENERIC_ADAPTER` + `ALGORITHM_STRENGTHENING` | Kannan–Bachem-style exact HNF/SNF with unimodular multipliers; locked source/target bases |
| P1 | `FINITE_LATTICE_QUOTIENT_SATURATION_ADAPTER` | `S32-PW03`,`S32-PW04` | `NEW_GENERIC_ADAPTER` + `STRUCTURE_THEOREM_STRENGTHENING` | exact lattice homomorphism, quotient presentation, reachable-image proof; no classwise-bound or CVP overclaim |
| P1 | `FINITE_MODULE_INTERTWINER_ISOMORPHISM_SOLVER` | `S33-PW05` (`S33-PW04` consumer boundary) | `NEW_GENERIC_ADAPTER` + `ALGORITHM_STRENGTHENING` | exact module generator matrices over fixed field; constructive invertible intertwiner; semantic source adapter separately required |
| P2 | `ORBITAL_DOUBLE_COSET_RECONSTRUCTION_ENGINE` | `S32-PW05`,`S30-W03` | `ALGORITHM_STRENGTHENING` | validated finite action, strong generating set, complete orbital coverage and source seed/conflict checks |
| P2 | `CLASSICAL_GROUP_CONSTRUCTIVE_RECOGNITION_GATE` | `S30-W01`,`S32-PW06` | `ALGORITHM_STRENGTHENING` / `NOT_APPLICABLE` until input match | natural finite-field matrix representation of claimed whole classical group; algorithm/oracle assumptions recorded; no semantic marking credit |
| P2 | `TRANSVECTION_GENERATED_SUBGROUP_CLASSIFIER` | `S32-PW06` | `RESEARCH_GAP` | multiple source-locked transvections, exact generated subgroup, irreducibility and exact characteristic-two theorem hypotheses |

## 8. Stop boundary

The strongest Phase-5 structural result is that three current enumeration layers have exact replacements or reductions:

```text
S30-W01 candidate relabelings
  -> orbit/stabilizer/transporter matching

S30-W02 all-element semilinear equality
  -> generator/presentation equality after homomorphism certification

S32-PW06 arbitrary symplectic operator candidates
  -> unique transvection directions v in W\{0}
```

The lattice/module side also admits a clean shared exact normal-form layer using reversible HNF/SNF, and `S33-PW05` admits a generic constructive module-intertwiner solver. None of these changes the semantic firewall: the final source marking/common geometric anchor remains repo-specific.

No current Arsenal card is promoted, retired, deduplicated or weakened in Phase 5.