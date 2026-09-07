# Research Arsenal × Literature Strengthening Audit — Phase 3 Descent / Squareclass / S-unit / Thue–Mahler

```text
ARSENAL_BASE_MAIN=9306238c7ada55e31311245019d6b7e474ad837f
STAGE36_EXCLUDED=true
STAGE35_PROVISIONAL_COMPARISON_HEAD=3fc684677ef1570a820420079088667f558e0983
LITERATURE_DISCOVERY_ONLY=true
ARSENAL_AUTHORITY_CHANGED=false
STABLE_ID_CREATED=false
```

This phase compares the frozen Phase-1 Arsenal contracts to explicit descent, S-unit, Thue, Thue–Mahler, norm-form, Baker/LLL and finite-support literature. It creates no Arsenal credit and does not change `docs/arsenal/index.json`, generated cards, Stage authority, or Stage36.

## 1. Reviewed Arsenal surface

Primary cards:

- `S34-W01 SUCCESSIVE_EXACT_FACTOR_SQUARECLASS_DESCENT`
- `S35-PW01 PARAMETRIC_SQUARECLASS_COMPATIBILITY_GRAPH` (audited provisional comparison snapshot only)
- `S31-W01 GENUS_ONE_QUARTIC_ELLIPTIC_BIRATIONAL_ADAPTER`
- `S31-W02 DIRECT_INTEGRAL_MODEL_COMPLETENESS_TRANSFER`
- `S31-W03 COMPLETE_POINT_SET_PARAMETER_PULLBACK`
- `S31-WF01 CAS_MW_FULL_GROUP_CERTIFICATION`
- `S32-PW01 EXACT_ENUMERATION_COMPRESSION_AND_INDEXER`
- `S32-PW03 LATTICE_IMAGE_HNF_GATE`
- `S32-PW04 FINITE_LATTICE_QUOTIENT_BOUND`
- `S35-PW03 RATIONAL_SOURCE_LIFT_PRESERVING_KUMMER_NORMAL_FORM`
- `S34-W03 RECEIVER_RESTRICTED_INTERSECTION_EXCLUSION`
- `S34-WF01 CLASS3_RECEIVER_REPLACEMENT_THEOREM_PIPELINE`

Stage35 provisional extensions to formal `S34-W01`, not new card IDs:

- `DISC-S35-A02` dynamic-reservoir preflight: records complete pairwise-gcd reservoir incidence and separates odd-prime from sign/2-adic support, but deliberately fails closed when support remains parameter-dependent.
- `DISC-S35-A09` primitive pair-gcd skeleton: extracts pairwise-coprime shared gcds/private cofactors and only source-justified coprimality/parity relations; it does not prove finite prime support.

## 2. Main answer: can S34-W01 bypass bespoke low-genus design?

**Conditionally yes.** The frozen `S34-W01` already does the hard arithmetic preconditioning: exact factorization, gcd/resultant/valuation support, complete sign/2-adic bookkeeping and a finite exhaustive squareclass branch family. When a residual branch can additionally be normalized into one of the following fixed equation classes,

```text
fixed S-unit equation
fixed irreducible Thue equation F(X,Y)=m
fixed irreducible Thue–Mahler equation F(X,Y)=a*prod(p_i^z_i)
fixed norm-form equation
proved explicit n-cover / Selmer-cover object
```

then standard effective literature can replace a branch-specific genus-one/genus-two design by a reusable terminal solver.

The safe typed route is therefore

```text
S34-W01 finite exhaustive squareclass branches
-> FIXED_EQUATION_CLASS_NORMALIZER
-> [S_UNIT | THUE | THUE_MAHLER | NORM_FORM | EXPLICIT_COVER]
-> effective bound/reduction
-> certified finite enumeration or empty covering family
-> S31-W03 pullback / S34-W03 receiver closure
```

This is not universal. Reducible forms, variable coefficients, parameter-dependent prime support, number-field equation classes without a complete solver, or Kummer-looking square systems without a proved torsor/cover identity still require separate mathematics.

## 3. The missing gate after S35-PW01

`S35-PW01` explicitly permits live parameter-dependent squareclass reservoirs. Neither `DISC-S35-A02` nor `DISC-S35-A09` changes that. Therefore no fixed-`S` theorem may be applied directly.

Phase-6 candidate typed chain:

```text
PARAMETRIC_SQUARECLASS_COMPATIBILITY_GRAPH
-> PARAMETRIC_RESERVOIR_FINITE_SUPPORT_CERTIFICATE
-> FIXED_S_EQUATION_NORMALIZER
-> S_UNIT / THUE_MAHLER TERMINAL
```

A valid `PARAMETRIC_RESERVOIR_FINITE_SUPPORT_CERTIFICATE` must record at least:

1. coefficient field `K` and the exact ring of integers / `S`-integers used;
2. a finite set `S` of finite places fixed independently of the live parameters, plus infinite places where the theorem's convention requires them;
3. an exact proof that every allowed denominator, shared gcd, squareclass representative and residual RHS is supported on `S` (or belongs to one of finitely many branch-indexed fixed sets `S_i`);
4. primitive/content/gcd normalization and every allowed common-factor split;
5. sign and 2-adic treatment and all zero/pole/infinity boundaries;
6. fixed coefficients/RHS or an exact finite reduction to fixed coefficient/RHS cases;
7. forward and converse reconstruction to the source receiver.

If support still varies with an unrestricted parameter, the result remains `RESEARCH_GAP`; S-unit/Thue–Mahler finiteness is unavailable.

## 4. Literature candidates

### L3-SU01 — Evertse fixed-S finiteness / quantitative source anchor

J.-H. Evertse, *On equations in S-units and the Thue-Mahler equation*, Inventiones Mathematicae **75** (1984), 561–584. DOI `10.1007/BF01388644`. Locator: Corollary 2 for the quantitative Thue–Mahler solution-count bound cited by later explicit algorithms.

- equation class: S-unit / Thue–Mahler;
- field: number-field framework;
- `S`: fixed finite set;
- effective/computable: quantitative finiteness/counting theorem, not by itself a practical complete enumerator;
- unit rank: determined by `K,S`;
- primitive/coprime and irreducibility: equation-specific hypotheses remain load-bearing;
- output: finiteness / explicit number bound, not a list of all solutions.

Classification: `SOURCE_ANCHOR_ONLY` for `S34-W01`; `NOT_APPLICABLE` to live `S35-PW01` reservoirs before the finite-support gate.

### L3-SU02 — de Weger fixed-S S-unit terminal

B. M. M. de Weger, *Solving exponential Diophantine equations using lattice basis reduction algorithms*, Journal of Number Theory **26** (1987), 325–367. DOI `10.1016/0022-314X(87)90088-6`.

The paper fixes a finite set of rational primes and gives algorithms for equations including `x+y=z` in positive integers supported on that set. It combines real and p-adic multidimensional Diophantine approximation with LLL/L3 reduction.

- equation class: rational S-unit/exponential equations;
- field: `Q` in the explicit formulation;
- `S`: fixed;
- effective: yes;
- input height bound: Baker/logarithmic estimates plus reduction machinery inside the method;
- local information: real and p-adic approximation;
- completeness: yes for the stated algorithmic equation classes;
- software: historically bespoke; modern implementations exist elsewhere but are supplementary.

Classification: `NEW_S_UNIT_TERMINAL` once an exact branch-to-S-unit adapter exists.

### L3-SU03 — Győry–Yu explicit S-unit height bounds

K. Győry and K. Yu, *Bounds for the solutions of S-unit equations and decomposable form equations*, Acta Arithmetica **123** (2006), 9–41. DOI `10.4064/aa123-1-2`. Locators: Theorems 1–2.

- equation class: `alpha*x+beta*y=1` with `x,y` S-units, plus decomposable forms;
- field: number field;
- `S`: fixed finite set containing the archimedean places in the paper's convention;
- output: completely explicit height bounds depending on field/S data;
- completeness: a bound, not enumeration.

Classification: `SOURCE_ANCHOR_ONLY` / bound source for `NEW_S_UNIT_TERMINAL`; the bound cannot close an Arsenal branch without certified enumeration.

### L3-T01 — complete practical Thue terminal

N. Tzanakis and B. M. M. de Weger, *On the practical solution of the Thue equation*, Journal of Number Theory **31** (1989), 99–132. DOI `10.1016/0022-314X(89)90014-0`. Locator status: paper-level general algorithm; the paper does not expose one single top-level numbered `Algorithm N` to source-lock.

Input is an irreducible binary form `F in Z[X,Y]`, degree at least 3, and fixed nonzero integer RHS `m`. The method explicitly determines **all** integral solutions by Baker linear-form bounds plus computational Diophantine approximation/reduction.

- `S`: not a variable input; fixed RHS Thue equation;
- irreducibility: required;
- primitive/coprime: any source reduction imposing primitivity must be preserved explicitly;
- effective: yes;
- completeness: yes;
- MW/Selmer data: not required.

Classification: `NEW_THUE_TERMINAL` for a finite `S34-W01` branch family after exact `FINITE_BRANCH_TO_THUE` normalization.

### L3-TM01 — Bugeaud–Győry explicit Thue/Thue–Mahler and norm bounds

Y. Bugeaud and K. Győry, *Bounds for the solutions of Thue-Mahler equations and norm form equations*, Acta Arithmetica **74** (1996), 273–292. DOI `10.4064/aa-74-3-273-292`.

Verified locators:

- Theorem 3: explicit size bounds for integer solutions of irreducible Thue equations `F(x,y)=b`, `deg F=n>=3`, fixed nonzero `b`;
- Theorem 4: explicit bounds for Thue–Mahler equations `F(x,y)=b p_1^{z_1}...p_s^{z_s}` with fixed distinct rational primes, `z_i>=0`, and the stated coprimality condition involving `(x,y,p_1...p_s)`;
- Theorems 1–2: number-field norm-form bounds.

- `S`: fixed in Theorem 4;
- field: Thue/Thue–Mahler statement over `Z/Q`; norm-form results extend to number fields/S-integers;
- output: completely explicit height/exponent/size upper bounds;
- completeness: **not** enumeration. The paper itself notes the practical size problem of general bounds.

Classification: `EXTEND_S34_W01` as a reusable effective-bound layer and `SOURCE_ANCHOR_ONLY`; never terminal by itself.

### L3-TM02 — classical complete Thue–Mahler terminal

N. Tzanakis and B. M. M. de Weger, *How to explicitly solve a Thue-Mahler equation*, Compositio Mathematica **84** (1992), 223–288; corrigendum, Compositio Mathematica **89** (1993), 241–242. No DOI was assigned in the bibliographic record used here; stable Numdam record `CM_1992__84_3_223_0`. Locator status: paper-level general algorithm plus corrigendum, not one single top-level numbered algorithm.

The method combines:

1. algebraic-number-theory reduction to finitely many auxiliary equations;
2. explicit archimedean and p-adic logarithmic bounds;
3. real and p-adic Diophantine approximation / LLL reduction;
4. final finite lattice enumeration, including Fincke–Pohst style short-vector enumeration.

- equation class: fixed Thue–Mahler equation;
- coefficient field: binary form over integers, auxiliary number fields computed from the form;
- `S`: fixed;
- irreducibility/primitive normalization: required by the standard equation setup;
- effective: yes;
- completeness: yes;
- MW/Selmer: not required.

Classification: `NEW_THUE_MAHLER_TERMINAL`.

### L3-TM03 — modern efficient arbitrary-degree Thue–Mahler terminal

A. Gherga and S. Siksek, *Efficient resolution of Thue-Mahler equations*, Algebra & Number Theory **19** (2025), 667–714. DOI `10.2140/ant.2025.19.667`.

Exact equation class:

```text
F(X,Y)=a*p_1^z_1*...*p_v^z_v,
gcd(X,Y)=1,
z_i>=0,
```

where `F` is an irreducible homogeneous binary form of degree `d>=3` in `Z[X,Y]`, `a!=0`, and `p_i` are fixed distinct rational primes with the paper's normalization restrictions. The algorithm works in `K=Q(theta)` for one root, rather than the larger three-root field of older general methods.

Verified algorithm/proposition locators:

- Algorithm 2.6 + Proposition 2.7: finite local ideal-data construction and termination;
- Proposition 3.1: finite ideal-equation covering of solutions;
- Propositions 10.2–10.3: local lattice / finite quotient sieve machinery;
- Procedure 10.4 `Solutions(...)`: bounded-exponent solution enumeration, ending in exact finite lattice enumeration when needed.

Additional exact normalization: the implementation assumes an auxiliary coprimality such as `gcd(a_0,Y)=1`; the paper explains finite splitting that removes this as a loss of generality. A repo adapter must reproduce that finite split rather than assume it silently.

- `S`: fixed finite rational-prime set;
- unit rank: the relevant algebraic S-unit rank is derived from `K` and local data, not a free repo parameter;
- effective: yes;
- local solubility: used as pruning only;
- completeness: yes for the normalized equation;
- software: Magma implementation/TMSolver available as supplementary implementation evidence.

Classification: highest-priority `NEW_THUE_MAHLER_TERMINAL` for `S34-W01` output. Required new adapter: `FINITE_SQUARECLASS_BRANCH_TO_THUE_MAHLER`.

### L3-MULTI01 — von Känel–Matschke Q-specific terminal suite

R. von Känel and B. Matschke, *Solving S-Unit, Mordell, Thue, Thue–Mahler and Generalized Ramanujan–Nagell Equations via the Shimura–Taniyama Conjecture*, Memoirs of the AMS **286**, no. 1419 (2023). DOI `10.1090/memo/1419`.

Verified locators:

- Algorithm 3.14: complete S-unit solver over `Q` using explicit height bounds and refined sieves;
- Algorithm 5.4: cubic Thue solver after the specified elliptic/Mordell–Weil input is supplied;
- Algorithm 5.5: cubic Thue–Mahler solver, requiring Mordell–Weil bases for the finite family of associated elliptic curves described in the algorithm;
- Algorithm 6.2: generalized Ramanujan–Nagell solver via a finite reduction to earlier algorithms.

The work also contains an elliptic-logarithm sieve for bounded S-integral points. It is particularly useful as a standard terminal framework for cubic branches, but it does **not** make arbitrary-degree Thue–Mahler branches cubic.

Classification: `NEW_S_UNIT_TERMINAL`, `NEW_THUE_TERMINAL`, `NEW_THUE_MAHLER_TERMINAL`; `RESEARCH_GAP` on a specific branch if the required MW bases are unavailable. `S31-WF01` is the natural repo certification workflow for those bases.

### L3-LAT01 — certified lattice enumeration anchor

U. Fincke and M. Pohst, *Improved methods for calculating vectors of short length in a lattice, including a complexity analysis*, Mathematics of Computation **44** (1985), 463–471. DOI `10.1090/S0025-5718-1985-0777278-8`.

This is the exact-enumeration endpoint used by classical Thue–Mahler implementations after logarithmic/lattice reduction. It is not the same contract as `S32-PW04`, whose current output is only a safe lower bound on finitely many affine shift classes.

Classification: `SOURCE_ANCHOR_ONLY` for `S32-PW04`, plus a Phase-6 `CERTIFIED_BOUND_REDUCTION_ENUMERATION` adapter candidate. Do not relabel `S32-PW04` itself as a complete CVP/enumerator.

### L3-DESC01 — explicit n-descent / genus-one coverings

J. E. Cremona, T. A. Fisher, C. O'Neil, D. Simon and M. Stoll, *Explicit n-descent on elliptic curves, I. Algebra*, J. Reine Angew. Math. **615** (2008), 121–155. DOI `10.1515/CRELLE.2008.012`.

Same authors, *Explicit n-descent on elliptic curves, II. Geometry*, J. Reine Angew. Math. **632** (2009), 63–84. DOI `10.1515/CRELLE.2009.050`.

J. E. Cremona, T. A. Fisher and M. Stoll, *Minimisation and reduction of 2-, 3- and 4-coverings of elliptic curves*, Algebra & Number Theory **4** (2010), 763–820. DOI `10.2140/ant.2010.4.763`.

These papers provide the standard algebraic/geometric realization and reduction of Selmer elements as explicit genus-one coverings.

Classification:

- `S31-W01`: `SOURCE_ANCHOR_ONLY`; literature does not replace its repo-specific forward/inverse rational functions, denominators and exceptional loci.
- `S34-W01`: `EXPLICIT_DESCENT_ADAPTER` when a finite squareclass branch is proved to represent an actual `n`-cover/Selmer object.
- `S35-PW03`: `EXPLICIT_DESCENT_ADAPTER / RESEARCH_GAP`; Kummer-style simultaneous squares alone do not establish the torsor/cover class.

### L3-DESC02 — hyperelliptic 2-Selmer computation

M. Stoll, *Implementing 2-descent for Jacobians of hyperelliptic curves*, Acta Arithmetica **98** (2001), 245–277. DOI `10.4064/aa98-3-4`.

The algorithm computes the size/data of the 2-Selmer group of the Jacobian in the stated hyperelliptic cases (even genus or a rational Weierstrass point in the paper's setup), giving an upper bound for Mordell–Weil rank.

Classification: `EXPLICIT_DESCENT_ADAPTER` / `SOURCE_ANCHOR_ONLY`. A Selmer set is not a rational point set.

### L3-DESC03 — two-cover descent nonexistence terminal

N. Bruin and M. Stoll, *Two-cover descent on hyperelliptic curves*, Mathematics of Computation **78** (2009), 2347–2370. DOI `10.1090/S0025-5718-09-02255-8`.

The algorithm computes a set of unramified covers through which every rational point lifts. If the returned covering set is empty, the curve has no rational points. A nonempty cover set is only a reduction and must be solved downstream.

Classification: `EXPLICIT_DESCENT_ADAPTER`, with a genuine terminal nonexistence output in the empty-cover case. Natural targets are `S34-W01`, `S35-PW03` and `S34-W03` after exact hyperelliptic/cover adapters.

## 5. Exact candidate adapters

### `FINITE_SQUARECLASS_BRANCH_TO_THUE`

Input:

```text
one finite S34-W01 branch
+ exact binary form F
+ fixed RHS m
+ irreducibility certificate degree>=3
+ exact primitive/content normalization
+ complete forward/converse branch dictionary
```

Output: one or finitely many fixed Thue equations whose complete solution sets exhaust the branch.

Classification: `EXTEND_S34_W01` + `NEW_THUE_TERMINAL`.

### `FINITE_SQUARECLASS_BRANCH_TO_THUE_MAHLER`

Input:

```text
one finite branch
+ F in Z[X,Y], irreducible degree>=3
+ fixed nonzero a
+ finite fixed rational-prime support S={p_i}
+ gcd/content normalization matching the chosen solver
+ exact exponent sign/nonnegativity convention
+ complete forward/converse branch dictionary
```

Output: one or finitely many solver-valid Thue–Mahler equations.

Classification: `EXTEND_S34_W01` + `NEW_THUE_MAHLER_TERMINAL`.

### `PARAMETRIC_RESERVOIR_FINITE_SUPPORT_CERTIFICATE`

Input: `S35-PW01` compatibility graph plus dynamic-reservoir/gcd-skeleton provenance.

Output: either a fixed finite `S`, a finite branch-indexed family `{S_i}`, or explicit `FAIL_VARIABLE_SUPPORT`.

Classification: `NEW_FINITE_SUPPORT_GATE`.

### `FINITE_BRANCH_TO_EXPLICIT_COVER`

Input: finite squareclass/Kummer branch plus exact curve/Jacobian, covering map and cohomological torsor/Selmer identity.

Output: a literature-valid 2/3/4-cover object with local-solubility and covering-family semantics.

Classification: `EXPLICIT_DESCENT_ADAPTER`.

### `CERTIFIED_BOUND_REDUCTION_ENUMERATION`

Input: a proved Baker/height/exponent bound, exact real/p-adic approximation lattice, exact or certified LLL reduction, and an exact finite enumeration region.

Output: complete finite candidate set with exact replay.

Classification: terminal-support candidate adjacent to `S32-PW03/PW04`, not a change to either current card.

## 6. Card-by-card classification

| Arsenal surface | Phase-3 classification | Exact conclusion |
|---|---|---|
| `S34-W01` | `EXTEND_S34_W01` | Preserve current finite-branch output; add typed routes to fixed S-unit/Thue/Thue–Mahler/norm/explicit-cover terminals. |
| `S35-PW01` | `NEW_FINITE_SUPPORT_GATE` / `RESEARCH_GAP` | Cannot enter fixed-S literature until live reservoirs are proved uniformly or finitely branchwise supported. |
| `DISC-S35-A02` | `DUPLICATE` as prerequisite data only | Dynamic reservoir incidence is exactly the preflight needed by the finite-support gate, but is not the gate result. |
| `DISC-S35-A09` | `DUPLICATE` as prerequisite data only | Primitive gcd skeleton supplies normalization facts, not finite support or terminal closure. |
| `S31-W01` | `SOURCE_ANCHOR_ONLY` | Explicit n-descent literature anchors genus-one models; repo map/exceptional-locus certificate remains necessary. |
| `S31-W02` | `NEW_THUE_TERMINAL` / `NEW_THUE_MAHLER_TERMINAL` downstream | Complete literature solver may supply the auxiliary complete point set; its iff integral transfer remains unchanged. |
| `S31-W03` | `DUPLICATE` as reconstruction discipline | Literature terminal output still requires exhaustive repo branch/source pullback. |
| `S31-WF01` | `SOURCE_ANCHOR_ONLY` / support for cubic terminals | Needed only for literature algorithms whose exact input includes MW bases; not required by Gherga–Siksek general Thue–Mahler. |
| `S32-PW01` | `DUPLICATE` / support only | Can index a proven finite candidate population; it supplies no Diophantine bound or equation equivalence. |
| `S32-PW03` | `SOURCE_ANCHOR_ONLY` | HNF image gate can cheaply prune exact finite/lattice conditions but is not Baker/LLL terminal reduction. |
| `S32-PW04` | `SOURCE_ANCHOR_ONLY` / `RESEARCH_GAP` for direct extension | Its lower bound must not be reinterpreted as exact CVP or finite enumeration; a separate reduction/enumeration adapter is required. |
| `S35-PW03` | `EXPLICIT_DESCENT_ADAPTER` / `RESEARCH_GAP` | Strong 2-cover candidate only after actual covering/torsor identity and local-solubility semantics are proved. |
| `S34-W03` | terminal consumer | An empty S-unit/Thue–Mahler/cover output can close the exact receiver intersection without solving a larger auxiliary universe. |
| `S34-WF01` | terminal router | Literature methods are suitable replacement theorems only after exact receiver quantifiers and all adapters match. |

## 7. Hypothesis mismatches / fail-closed cases

1. `S35-PW01` parameter-dependent reservoir with no fixed `S`: `NOT_APPLICABLE` to fixed-S S-unit/Thue–Mahler theorems.
2. Finite number of squareclass *patterns* but representatives containing unrestricted parameter values: still not fixed prime support.
3. Reducible or degree `<3` binary form: not directly a classical irreducible Thue/Thue–Mahler input; refactor into separate equation species first.
4. Missing `gcd(X,Y)=1`/content normalization: Gherga–Siksek cannot be invoked until the finite common-factor cases are handled exactly.
5. Variable coefficients/RHS across an infinite parameter: a fixed-equation solver does not create a uniform theorem.
6. Number-field receiver while using a `Q`-specific implementation: `NOT_APPLICABLE` unless a number-field terminal is source-locked; Bugeaud–Győry bounds alone are insufficient.
7. Explicit height bound only: no completeness until certified reduction and finite enumeration are supplied.
8. Selmer membership/local solubility only: no rational point existence or classification credit.
9. Empty two-cover set: nonexistence credit is allowed; nonempty two-cover set is only a downstream reduction.
10. Cubic von Känel–Matschke route without required MW bases: `RESEARCH_GAP`; do not substitute rank estimates or found generators.
11. Kummer-looking simultaneous squares without a source-locked cover/torsor map: no Selmer/covering credit.

## 8. Mandatory credit firewalls

```text
finite squareclass family != solved Diophantine equation
S-unit finiteness != explicit complete solution unless an effective complete algorithm is supplied
Selmer set != rational point set
local solubility != global point
height bound != enumeration unless reduction/search/completeness is certified
standard theorem citation != repo-specific adapter
fixed-S theorem != parameter-dependent reservoir theorem
LLL reduction != exact enumeration
finite cover family != empty curve unless the covering family itself is empty or every cover is closed
```

## 9. Phase-6 freeze manifest

| Candidate | Targets | Classification | Promotion gate |
|---|---|---|---|
| `S34W01_TERMINAL_EQUATION_ROUTER_EXTENSION` | `S34-W01` | `EXTEND_S34_W01` | Formalize equation-species output schema without changing existing finite-branch credit. |
| `PARAMETRIC_RESERVOIR_FINITE_SUPPORT_CERTIFICATE` | `S35-PW01`, A02, A09 | `NEW_FINITE_SUPPORT_GATE` | Prove fixed or finite branch-indexed support, exact normalization and converse; otherwise fail closed. |
| `FIXED_S_UNIT_TERMINAL` | `S34-W01`, `S31-W02`, `S34-W03` | `NEW_S_UNIT_TERMINAL` | Exact S-unit adapter, fixed S/field/unit group data, effective solver and complete enumeration certificate. |
| `FIXED_THUE_TERMINAL` | `S34-W01`, `S31-W02` | `NEW_THUE_TERMINAL` | Irreducible fixed binary form, fixed RHS, primitive/content normalization, complete Tzanakis–de Weger-style solver certificate. |
| `FIXED_THUE_MAHLER_TERMINAL` | `S34-W01`, `S31-W02`, `S34-W03` | `NEW_THUE_MAHLER_TERMINAL` | Exact fixed support and Gherga–Siksek/Tzanakis–de Weger normalization, executable complete solver and replay. |
| `NORM_FORM_BOUND_AND_TERMINAL_ADAPTER` | `S34-W01`, norm receivers | `RESEARCH_GAP` | Bugeaud–Győry gives bounds; promotion requires an exact norm-form normalizer plus a complete effective enumerator for the exact field/S class. |
| `FINITE_BRANCH_TO_EXPLICIT_N_COVER` | `S34-W01`, `S35-PW03` | `EXPLICIT_DESCENT_ADAPTER` | Prove cover/torsor/Selmer identity, local data and exhaustive covering semantics. |
| `CERTIFIED_BAKER_LLL_REDUCTION_ENUMERATION` | `S32-PW03`, `S32-PW04`, terminal solvers | `SOURCE_ANCHOR_ONLY` + new support adapter | Separate exact height bound, certified lattice reduction and exact finite enumeration; never upgrade current PW04 lower-bound semantics. |

Priority for Phase 6 implementation audit:

```text
P0  PARAMETRIC_RESERVOIR_FINITE_SUPPORT_CERTIFICATE
P0  FIXED_THUE_MAHLER_TERMINAL
P0  S34W01_TERMINAL_EQUATION_ROUTER_EXTENSION
P1  FIXED_S_UNIT_TERMINAL
P1  FIXED_THUE_TERMINAL
P1  FINITE_BRANCH_TO_EXPLICIT_N_COVER
P2  CERTIFIED_BAKER_LLL_REDUCTION_ENUMERATION
P2  NORM_FORM_BOUND_AND_TERMINAL_ADAPTER
```

## 10. Stop boundary

No theorem was promoted and no stable ID was created. The strongest Phase-3 conclusion is:

> `S34-W01` is already a literature-grade arithmetic preconditioner. Its finite exhaustive branch output can often be routed directly to standard complete S-unit/Thue/Thue–Mahler machinery, substantially reducing bespoke low-genus design, **but only after an exact fixed-equation/fixed-support adapter**. `S35-PW01` is one typed layer earlier and requires a separate finite-support theorem before any fixed-S terminal may be invoked.

`NO_DIRECT_MATCH_FOUND_IN_THIS_SEARCH`, where it occurs, has no novelty meaning.