# Stage29-02hb audited source lock

## S1 — Kharlamov--Kulikov: Campedelli line arrangements

V. M. Kharlamov and Vik. S. Kulikov, *Surfaces with DIF != DEF real structures*, arXiv `math/0507059`.

Load-bearing locator: Section 1.5, definition of a Campedelli line arrangement and Theorems 1.9--1.10.

Exact content used:

- seven distinct lines are labeled by the seven nonzero elements of `(Z/2)^3`;
- there is no point of multiplicity at least four;
- at a triple point the three labels must not sum to zero;
- the associated `(Z/2)^3` Galois cover of `P^2` is the canonical model of a Campedelli surface.

Stable locators:

```text
arXiv:math/0507059
https://webdoc.sub.gwdg.de/ebook/serien/e/mpi_mathematik/2005/76.pdf
Section 1.5 / Theorems 1.9--1.10
```

This is a geometric source. It does not identify the perfect-cuboid quotient or a preferred Q-form.

## S2 — Calabri--Mendes Lopes--Pardini: local triple resolution and bicanonical cover

A. Calabri, M. Mendes Lopes, R. Pardini,
*Involutions on numerical Campedelli surfaces*, Tohoku Math. J. 60 (2008), 1--22, DOI `10.2748/tmj/1206734404`.

The fresh audit uses the detailed construction in Section 5, Example 1, not only the abstract.

Load-bearing statements there:

- a normal `G=(Z/2)^3` cover of `P^2` is given by branch divisors `D_g` and building bundles;
- for seven distinct branch lines, every nontrivial character has building bundle `O_P2(2)`;
- the assumptions are exactly: at most three lines concurrent and, at a triple point, `g1+g2+g3 != 0`;
- above such a triple point the canonical model has an `A1` rational double point;
- after blowing up the base triple point, the normalized cover is smooth above the exceptional divisor and its preimage is a `(-2)` curve;
- the resulting surface has `K^2=2`, `chi=1`, and the map to `P^2` is bicanonical.

Stable locator:

```text
https://www.jstage.jst.go.jp/article/tmj/60/1/60_1_1/_pdf
Section 5, Example 1
```

The same paper studies involution quotients. Its rational/Enriques terminology is geometric/birational; Stage29 does not turn that automatically into Q-rationality.

## S3 — Mendes Lopes--Pardini--Reid: degree-8 etale cover

M. Mendes Lopes, R. Pardini, M. Reid,
*Campedelli surfaces with fundamental group of order 8*,
Geometriae Dedicata 139 (2009), 49--55,
DOI `10.1007/s10711-008-9317-2`, arXiv `0805.0006`.

Exact theorem-level content:

```text
If Y -> S is an etale cover of degree 8 of a Campedelli surface,
the canonical model of Y is a complete intersection of four quadrics
in P^6. Consequently Y is the universal cover of S and the covering
group is pi_1(S).
```

This theorem is used only **after** the repo adapter has independently shown that the resolved cuboid quotient `S -> C_H` is genuinely finite etale degree eight. The theorem is not used to infer freeness from the visual similarity of two four-quadric models.

Stable locator:

```text
https://arxiv.org/abs/0805.0006
```

## Repo-specific adapter boundary

The literature does not state that the perfect-cuboid surface is the universal cover of these particular Campedelli surfaces. That identification is proved in-repo by the global factorization

```text
Sbar -> Sbar/H -> P2
```

of the already-audited sign-cover map, followed by the stabilizer and resolution audit.

Likewise, the source theorems are geometric. Each `C_H` here is Q-defined because `H` lies in the constant rational coordinate-sign group, but comparison with any other displayed Campedelli Q-model requires a separate Q-form/twist adapter.

```text
LITERATURE_NOVELTY_CLAIM=false
PERFECT_CUBOID_CAMPEDELLI_IDENTIFICATION_SOURCE_STATED_DIRECTLY=false
SAME_GLOBAL_MAP_PROVED_IN_REPO=true
SOURCE_GEOMETRY_TO_Q_ARITHMETIC_AUTOMATIC=false
Q_FORM_ADAPTER_REQUIRED_FOR_EXTERNAL_ARITHMETIC=true
```
