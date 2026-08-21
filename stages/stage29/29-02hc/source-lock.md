# Stage29-02hc source lock

## S1 — Suciu, non-Fano characteristic and covering package

Alexander I. Suciu, **Fundamental groups of line arrangements: Enumerative aspects**, Contemporary Mathematics 276 (2001), 43–79.

- arXiv: `math/0010105`
- DOI: `10.1090/conm/276/04510`
- stable arXiv PDF: https://arxiv.org/pdf/math/0010105

Load-bearing locators:

- §6.1, pp. 15–16 of PDF: definition of the branched congruence/Kummer cover and Hirzebruch surface `M_N(A)`; `H1(projective complement)=Z^(n-1)` and deck group `(Z/N)^(n-1)`.
- Theorem 6.3: Chern-number formulas.
- Theorem 6.5: Sakuma formula for `b1(M_N)` through torsion-character depths.
- Example 10.5 / Figure 6, p. 28 of PDF: non-Fano defining polynomial
  `xyz(x-y)(x-z)(y-z)(x+y-z)`, incidence data `n=7,s=9,m2=3,m3=6`, characteristic varieties, special order-2 character `rho`, congruence-cover parity formula, compact-cover formula `b1(M_N)=9(N-1)(N-2)`, and Chern formulas specialized to non-Fano.

Exact quoted data used here:

```text
Q_NF=xyz(x-y)(x-z)(y-z)(x+y-z)
b1(M_N)=9(N-1)(N-2)
c1^2(M_N)=N^4(10N^2-32N+25)
c2(M_N)=N^4(4N^2-16N+21)
```

## S2 — Hirzebruch original construction

Friedrich Hirzebruch, **Arrangements of Lines and Algebraic Surfaces**, in *Arithmetic and Geometry II*, Progress in Mathematics 36, Birkhäuser (1983), pp. 113–140.

- DOI: `10.1007/978-1-4757-9286-7_7`
- Max Planck Hirzebruch Collection: https://hirzebruch.mpim-bonn.mpg.de/id/eprint/244/
- public PDF: https://hirzebruch.mpim-bonn.mpg.de/id/eprint/244/1/hirzebrucharr.pdf

Use: original source for the branched abelian/Kummer covering-surface construction and Chern-number method. Stage29-02hc relies on Suciu for the compact modern notation and exact non-Fano specialization, with Hirzebruch as primary provenance.

## S3 — uniqueness/name lock for the non-Fano arrangement

Hal Schenck and Ştefan O. Tohăneanu, **The Orlik-Terao algebra and 2-formality**, Mathematical Research Letters 16 (2009), 171–182.

- arXiv: `0901.0253`
- DOI: `10.4310/MRL.2009.v16.n1.a17`

Load-bearing locator: Example 1.7 states that the non-Fano arrangement is the unique configuration of seven lines in `P^2` having six triple points; it is free and 2-formal.

This is used only as an independent naming/incidence cross-check. The exact cuboid-to-standard-non-Fano identification is stronger and is given by an explicit `PGL3(Q)` transformation in this PR.

## S4 — cuboid endpoint source baseline

Damiano Testa and Michael Stoll, **Curves on the surface of cuboids**, Mathematics of Computation, DOI `10.1090/mcom/4238`, arXiv `1009.0388`.

Use: audited Stage29 baseline for the cuboid surface equations, 48 A1 singularities, minimal resolution invariants, Picard data, and automorphisms. No new claim from S1–S3 is allowed to override the Testa–Stoll arithmetic model without the explicit adapter recorded here.

## Scope firewall

The literature does **not** appear, in the searches performed for this stage, to state the perfect-cuboid surface identification in the exact form

```text
S_cub = M_2(non-Fano)
```

but absence from search results is not a literature-novelty proof. Therefore:

```text
LITERATURE_NOVELTY_CLAIM=false
REPO_ADAPTER_NOVELTY=HIGH_VALUE_CANDIDATE
```
