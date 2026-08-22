# Stage29-15 — external Work theorem rematch (post-audit input)

Status: `NEW_INPUT_REQUIRING_REAUDIT`.

This file records the post-audit external theorem hunt supplied on 2026-08-22. It is not allowed to inherit the previous `PASS_AFTER_MATERIAL_POSITIVE_REPAIR` automatically. The strongest claims are to be source-checked during the renewed 29-15 audit.

## 1. Portfolio-level theorem compression

### Cao–Demarche–Xu

Yang Cao, Cyril Demarche, Fei Xu, *Comparing descent obstruction and Brauer–Manin obstruction for open varieties*, Trans. AMS 371 (2019), 8625–8650, Theorem 1.5 / Theorem 7.5.

For smooth quasi-projective geometrically integral varieties over a number field,

```text
X(A)^descent = X(A)^{et,Br}.
```

The Stage29 physical open `U` satisfies the required geometric scope after the already-audited smooth-open removal. Consequence:

```text
R29-OPEN-DESCENT-SPECIES=MERGED_WITH_ETALE_BRAUER
```

This is an obstruction-species identification only. It does not make the set of physical twists finite or compute `U(A)^{et,Br}`.

### Cao

Yang Cao, *Sous-groupe de Brauer invariant et obstruction de descente iteree*, Algebra & Number Theory 14 (2020), 2151–2183, Corollary 1.2 (from Theorem 1.1 plus CDX Theorem 1.5).

For smooth quasi-projective geometrically integral varieties over a number field,

```text
X(A)^{descent,descent} = X(A)^descent.
```

Therefore iterated/second descent on `U` is not a separate attack route:

```text
ITERATED_DESCENT_SUBROUTE=MERGED_INTO_ONE_STEP_DESCENT_ETALE_BRAUER
```

This does not discharge `R29-BEAU1C`, `R29-BEAU2`, `R29-BEAU3`, `R29-BR0B`, `R29-BR2A`, or `R29-BR2B`.

## 2. New finite Brauer input A — Ford seven-line precursor

Timothy J. Ford, *The Brauer Group of an Affine Double Plane Associated to a Hyperelliptic Curve*, Comm. Algebra 45 (2017), 1416–1442, DOI `10.1080/00927872.2016.1175608`.

The external Work report source-locks a line-arrangement theorem giving the geometric `d`-torsion Brauer precursor from the incidence graph of the deleted projective arrangement, with line-arrangement generators represented by symbols and relations imposed by concurrence.

For the Stage29 seven lines

```text
Lx   : x=0
Ly   : y=0
Lz   : z=0
Lxy  : x+y=0
Lxz  : x+z=0
Lyz  : y+z=0
Ls   : x+y+z=0
```

the exact incidence computation is executed separately in `brauer-line9-execution.md` and `verify_brauer_line9.py`.

Result:

```text
TRIPLE_POINTS=6
DOUBLE_POINTS=3
INCIDENCE_GRAPH_VERTICES=16
INCIDENCE_GRAPH_EDGES=24
INCIDENCE_GRAPH_CONNECTED=true
B1_GAMMA=9
R29-BR-LINE9=EXECUTED_GEOMETRIC_INCIDENCE_PRECURSOR
```

The renewed audit must verify the exact Ford theorem/proof locator and hypotheses before promoting the conditional geometric consequence

```text
Br(P2_Qbar - D)[2] ~= (Z/2)^9
```

as a source-certified statement. Even after source certification this is **not** `Br(U)/Br(Q)`: the multiquadratic cover, exceptional divisors, Galois descent, 72-component physical boundary, and local evaluation remain separate.

## 3. New finite Brauer input B — Creutz–Viray ruled-double-cover presentation

Brendan Creutz and Bianca Viray, *On Brauer groups of double covers of ruled surfaces*, Math. Ann. 362 (2015), 1169–1200, DOI `10.1007/s00208-014-1153-0`.

The source gives a finite presentation of geometric `Br(X)[2]` for desingularizations of double covers of geometrically ruled surfaces with reduced flat branch divisor having at worst simple singularities, with explicit central-simple-algebra generators and Neron–Severi relations.

New child receiver:

```text
R29-K3-RULED2
 = instantiate the Creutz–Viray ruled-double-cover presentation on K_c first,
   then only on K_a/K_b if K_c survives arithmetically.
```

Mandatory finite adapter:

1. exhibit a valid geometrically ruled base model, not merely `Bl_4(P1xP1)`;
2. push/transform the six-line branch to that model and verify flatness/reducedness/simple singularities;
3. enumerate the paper's finite squareclass/divisor group and Neron–Severi relations;
4. retain the exact Q/Galois action separately;
5. do not infer an endpoint obstruction before local evaluation on the lift locus.

Current class:

```text
R29-K3-RULED2=class 2 CURRENT_TOOL_LIMIT_EXECUTED
EXACT_LIMIT=explicit ruled-model transformation plus source-locked symbolic/CAS presentation not yet materialized
```

This is a finite computation wall, not a new theorem requirement.

## 4. Strong theorem matches that refine existing receivers without creating new OPEN work

- Dimitrov–Gao–Habegger uniform Mordell–Lang for curves: useful once moving genus-3 rank is uniformly controlled; absorbed into `R29-FIB2` / all-fiber arithmetic, no new route.
- de Grey–Gibbs–Helm rank-zero aspect-ratio filters: useful fixed-aspect-ratio eliminators; no uniform endpoint coverage, no new primary receiver.
- Luca square-Heron/rational-bisector equivalence plus Li all-square Heron fibers: a potentially useful model change, but without a theorem controlling the bisector sublocus it is recorded as an Arsenal lead rather than an OPEN receiver.
- Balestrieri–Johnson–Newton effective singular-K3 Brauer computation (GRH-conditional in the general singular-K3 form): quotient-level input only; a sign K3 such as `K_c` already has rational points, so the endpoint lift condition remains decisive.
- Creutz–Viray two-primary sufficiency for Kummer varieties: useful if an exact Kummer adapter is proved; does not replace physical-open boundary arithmetic already isolated in Stage29.
- Stoll finite descent on proper varieties: reinforces the exact `R29-BEAU1C` firewall; the physical open is nonproper and point-dependent boundary valuations prevent automatic finite twist support.
- Bauer–Stoll Burniat/etale-product theorems: no direct cuboid consequence from the currently audited `q=0` universal-cover tower; do not create a Campedelli route from geometric similarity.

## 5. Rejected/duplicate theorem species

The external Work report independently reconfirms:

```text
PESCHMANN_MASTER_COVERAGE=DUPLICATE_ALREADY_CONSUMED
PESCHMANN_1072_FIBERS=DUPLICATE_ALREADY_CONSUMED
HUANG_TORIC_SIEVE=DUPLICATE_WRONG_M3_CONDITIONAL_MEASURE
SURFACE_CHABAUTY_FULL_ENDPOINT=NONAPPLICABLE_ALBANESE_ZERO
AVERAGE_SELMER=NONAPPLICABLE_TO_INDIVIDUAL_THIN_PHYSICAL_TWISTS
BOGOMOLOV_BOUNDED_GENUS=NONAPPLICABLE_C1SQ_16_LT_C2_80_AND_NO_POINT_COVERAGE
CORVAJA_ZANNIER_FIXED_S_INTEGRAL=NONAPPLICABLE_PHYSICAL_POINTS_HAVE_MOVING_BOUNDARY_PRIMES
```

No claimed 2025–2026 global perfect-cuboid nonexistence proof survives the hostile coverage audit.

## 6. Parent-route consequence

No parent color changes from this Work input:

```text
ATTACK_ROUTE_COUNT=11
GREEN_ROUTE_COUNT=1
AMBER_ROUTE_COUNT=10
P_OVER_M3_SCALE_KNOWN=false
```

The material changes are portfolio compression and stronger finite Brauer infrastructure, not a perfect-cuboid existence/nonexistence theorem.

## 7. Re-audit requirement

The pre-existing 29-15 audit predates this file. Therefore:

```text
PREVIOUS_AUDIT_SUPERSEDED_BY_NEW_EXTERNAL_INPUT=true
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage29-audit
```

Renewed audit priorities:

1. source-check CDX/Cao exact hypotheses and confirm the route-merging semantics;
2. independently verify Ford's exact theorem statement and whether the incidence graph calculation indeed gives the claimed geometric 2-torsion precursor;
3. audit `verify_brauer_line9.py` and the six-triple/three-double incidence list;
4. determine whether `R29-K3-RULED2` is truly class 2 or can be promoted to class 1 and executed now from existing K_c equations;
5. test whether any other Work theorem creates a hidden class-1 receiver under the mandatory four-class rule;
6. preserve all physical-height, open-boundary, Q/Qbar and quotient-vs-lift firewalls.

```text
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
