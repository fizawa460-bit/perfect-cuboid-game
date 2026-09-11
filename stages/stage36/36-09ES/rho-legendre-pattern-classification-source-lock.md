# Stage36 36-09ES — exact six-template labelled-Legendre pattern classification

## Purpose

36-09EP proves that the rho full-2 Selmer matrix is determined by the labelled radical Legendre datum

```text
R(a,b)=(S_P,S_Q,S_D; q mod 8; epsilon_2; directed Legendre bits),
```

and 36-09EQ/ER give graph certificates for every exact `Sel2_dim=2` row in the EO diagnostic box. This leaf removes the actual prime values from those certificates and classifies the maximal-rank examples into abstract arithmetic templates.

## Pattern equivalence

For primitive positive `p=a/b`, define the odd support vertices by the triples

```text
(label(q), q mod 8),  label(q) in {P,Q,D},
```

together with the directed bits

```text
lambda(q,r)=0 if (r/q)=+1,
lambda(q,r)=1 if (r/q)=-1
```

for distinct support primes, and the dyadic branch `epsilon_2`.

Two data are **pattern-equivalent** if there is a bijection of odd support vertices preserving mod-8 classes and all directed Legendre bits and either

1. preserving the P/Q/D labels, or
2. interchanging P and Q everywhere while fixing D.

The second option is legitimate because

```text
y^2=X(X-P^2)(X-Q^2)
```

is literally unchanged when P and Q are interchanged. At descent-matrix level this only changes the chosen naming of the two nonzero roots / associated Kummer coordinates and hence preserves rank.

Positive valuation exponents are absent by 36-09EP.

## Abstract matrix theorem

Given an abstract pattern, construct the Selmer matrix without choosing integer representatives:

- global generators are `[-1,2]` plus one generator per abstract odd support vertex;
- localization of `-1` and `2` at an odd vertex is determined by its mod-8 class;
- localization of one abstract prime at another is the retained directed Legendre bit;
- the self-localization has odd valuation bit one;
- the Q2 squareclass of each odd abstract prime is determined by mod 8;
- the odd local Kummer block is selected from 36-09EM by P/Q/D label and mod 8;
- the Q2 block is selected from 36-09EN by `epsilon_2`;
- the real block is the uniform 36-09EN block.

Call this matrix `M_T`. By the 36-09EP entry formulas, if `R(a,b)` is pattern-equivalent to `T`, then the actual matrix `M_R(R(a,b))` is row/column permutation-equivalent to `M_T`. Therefore

```text
rank M_R(R(a,b)) = rank M_T.
```

So any abstract template with `rank M_T=2n-2` gives a global sufficient condition for

```text
Sel2_dim(E_rho,p)=2.
```

This theorem is not restricted to the EO box.

## The six exact maximal-rank templates

Canonicalization is by lexicographic minimization over permutations within equal `(label,mod8)` classes and over the optional global P/Q swap. Because the full directed Legendre-bit matrix participates in that lexicographic minimization, the canonical P/Q orientation is not determined by the vertex multiset alone. The canonical compact JSON SHA-256 identifiers are:

```text
T1 seed 2/1:
  ee1d27ad67abd6f37ebf6d71794a53b03f229d7aa0c7148396bc64133f48cb75
  canonical vertices: D3, P7
  n=4, rank=6
  graph certificate: leaf-only

T2 seed 1/5:
  7c342b8cb3df57cb259c7f959602d83d3b8b8832d5a9c3d6846b661518905073
  canonical vertices: D3, D5, P7, Q1
  n=6, rank=10
  graph certificate: leaf-only

T3 seed 2/7:
  f3a8734144e03d36a04f57e51506873bbc632d9807f9b77ba22bb94e060a04e9
  canonical vertices: D3, D5, D7, P1, Q1
  n=7, rank=12
  graph certificate: leaf-only

T4 seed 2/9:
  6b6299864b83e8e21938f14c7054415fbf47553de5ece93241a9c8515d4b56c3
  canonical vertices: D3, D3, D7, P1, Q1
  n=7, rank=12
  graph certificate: leaf-only

T5 seed 6/43:
  4e26e5ba1e9269376a3f4a62899c3e68e43c64694d0a31acfd0d91b2a25236d2
  canonical vertices: D3, D3, D5, D7, P1, Q1, Q1
  n=9, rank=16
  graph certificate: leaf-only

T6 seed 3/47:
  4b2b444bf1d8af43e1b9b7a49b8dd19befebd0d2cb6da1887637ec4f0150fa7a
  canonical vertices: D3, D3, D5, D7, P1, P7, Q1, Q1
  n=10, rank=18
  graph certificate: leaf-plus-odd-core
```

All six have the shallow dyadic branch.

For each template the abstract matrix itself has rank `2n-2`; this is checked independently of the seed's integer matrix.

## Exact EO classification

On all 1546 primitive ordered rows `1<=a,b<=50`, a row matches one of the six templates if and only if it is one of the exact 24 `Sel2_dim=2` rows. The six pattern classes are exactly the six four-point literal/rho orbits:

```text
T1: {1/3,1/2,2,3}
T2: {1/5,2/3,3/2,5}
T3: {2/7,5/9,9/5,7/2}
T4: {2/9,7/11,11/7,9/2}
T5: {6/43,37/49,49/37,43/6}
T6: {3/47,22/25,25/22,47/3}
```

Thus EQ/ER's apparently different graph mechanisms are now organized into six arithmetic template classes: five peelable classes and one cyclic-core class.

## Consequence and limitation

For an arbitrary primitive positive rational parameter, matching any one of `T1` through `T6` proves `Sel2_dim=2` without local point search, valuation exponents, or Gaussian elimination on the parameter-specific matrix. To obtain a physical fixed-p exclusion through 36-09EH one must still independently discharge the no-rational-4-torsion and no-rational-3-torsion conditions.

No assertion is made that these six templates exhaust all possible maximal-rank patterns.

The next leaf is a targeted realization step, not a blind larger-box Selmer search:

```text
36-09ET_RHO_TEMPLATE_REALIZATION_PREFLIGHT.
```

It should search specifically for new primitive parameters realizing one of the six already-proved templates, then apply the independent EH torsion checks.

## Credit firewall

This leaf adds no new fixed-p exclusion by itself. The following remain false:

```text
six_templates_exhaust_all_max_rank_patterns,
uniform_Sel2_dimension_2_theorem,
candidate_parameter_set_shrunk,
receiver_emptiness_proved,
R29_CAMP2_closed,
Q11_CAMPEDELLI_closed,
endpoint_closed,
perfect_cuboid_nonexistence_claim.
```
