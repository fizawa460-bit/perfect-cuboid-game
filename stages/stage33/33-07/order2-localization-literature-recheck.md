# Stage33-07 order-two localization literature recheck

This recheck was started for PR #1414 and is continued in PR #1419 after the
quotient-to-raw order-four Bockstein layer was put in exact normal form.

## Exact current receiver

The absolute order-two localization obstruction is correctly split into:

1. restriction to `G_L`, for `L=Q(i,sqrt(2))`, represented by a `14 x 26`
   tensor of classes in `L*/L*2`;
2. only on the Stage-A kernel, the uniquely inflated finite `V4` class in
   `H^1(V4,Br(Sbar)[2])`, of dimension 16.

The project-specific Stage-A tensor has 364 squareclass entries.  Its entries
are not supplied by the abstract coefficient module or by the boundary graph.

PR #1419 further proves that the finite quotient-to-raw boundary extension is
not itself an unresolved ambiguity.  The 26 boundary directions admit mixed
first-residue models with 17 raw-order-two and 9 raw-order-four directions, and
the exact raw extension is

```text
(Z/4)^9 direct_sum (Z/2)^52.
```

The remaining constructive target is therefore a genuine global geometric
Gersten lift for the nine order-four boundary packages and the Galois
difference cocycles of those lifts.

## Primary-source verdicts

### Creutz--Viray

Brendan Creutz and Bianca Viray, *On Brauer groups of double covers of ruled
surfaces*, Math. Ann. 362 (2015), 1169--1200,
arXiv:1306.3251, Theorem I / Corollary 4.5.

The theorem gives a Galois-equivariant finite presentation of the **proper**
geometric `Br(Xbar)[2]` by explicit central simple algebras and Neron--Severi
relations.  Stage33-05 already consumed this input to construct `J2` and
Stage33-07 used it to obtain the exact 14-dimensional coefficient module.  It
does not give a section of the open-surface boundary localization sequence and
does not compute the 26 lift-torsor restriction classes.  Verdict: `REUSED`
for the coefficient module, `NOT_DIRECT` for the present Stage-A tensor.

### Ford localization

Timothy J. Ford, *On the Brauer group of a localization*, J. Algebra 147
(1992), 365--378, DOI `10.1016/0021-8693(92)90211-4`.

Ford studies the localization over an algebraically closed field using the
boundary graph.  This matches the already accepted geometric residue/cycle
layer, but it does not compute arithmetic descent of a chosen geometric lift
to `Q`, nor the `G_L` squareclass cocycle.  Verdict: `GEOMETRIC_DUPLICATE`.

### Oesinghaus root-stack residue

Jakob Oesinghaus, *Geometric Brauer residue via root stacks*, Res. Math. Sci.
5 (2018), article 28, DOI `10.1007/s40687-018-0146-0`, arXiv:1803.04326,
Theorem 1 / Proposition 3.

The paper geometrizes the residue of an **already given** Brauer class through
a root stack and gives geometric representatives for residues of conic/Brauer--
Severi bundles.  It does not invert the global localization map for the cuboid
surface and does not determine the Galois cocycle of its lift torsor.  Verdict:
`DIRECTION_REVERSED_NEAR_MISS`.

### Berg explicit cocycle lifting on affine Chatelet surfaces

J. Berg, *Obstructions to integral points on affine Chatelet surfaces* (2017).
The paper develops explicit representatives, including non-cyclic Brauer
classes, and an effective cocycle-lifting procedure for the special affine
Chatelet surface geometry `x^2-a y^2=P(t)`.  This is a useful constructive
analogy for the present leaf, but its algorithm depends on that special
function-field presentation and does not supply a section of the cuboid
surface Gersten residue map.  Verdict: `CONSTRUCTIVE_ANALOGY_NOT_DIRECT`.

### Merkurjev--Suslin / norm residue

A. S. Merkurjev and A. A. Suslin, *K-cohomology of Severi-Brauer varieties and
the norm residue homomorphism* (1983).

Norm-residue surjectivity ensures symbol generation in the relevant field
cohomology and underlies the Gersten framework, but it is existential at the
level needed here: it does not choose the cuboid-specific nine global lifts or
compute their `G_L` differences.  Verdict: `EXISTENCE_BACKGROUND_NOT_EXPLICIT_SPLITTING`.

### Brandhorst--Veniani / finite quadratic modules

Simon Brandhorst and Davide Cesare Veniani, *Hensel lifting algorithms for
quadratic forms*, Math. Comp. 93 (2024), 1963--1991.

This is relevant to orthogonal groups of discriminant modules and would have
been a plausible tool during the index-512/full-Q4 branch.  PR #1414 inherits
exact rejection of K1/K2/K3 and the elementary geometric sign reduction, so it
does not address the current localization-torsor tensor.  Verdict:
`SUPERSEDED_BRANCH_ONLY`.

## Consequence after PR #1419

No searched theorem turns the now-explicit mixed-order boundary residue
packages into the required cuboid-specific global geometric lifts or their
arithmetic Galois cocycles.  The finite Bockstein extension is already closed;
the next authorized route remains constructive and strictly narrower:

```text
R33-BR2A-9-ORDER4-GERSTEN-LIFT-GALOIS-DIFFERENCE-COCYCLE
L33-07-MATERIALIZE-9-ORDER4-GLOBAL-GEOMETRIC-GERSTEN-LIFTS-AND-GALOIS-DIFFERENCES
```

No theorem, endpoint, Brauer--Manin, or perfect-cuboid credit is claimed.
