# Stage29-02hb source lock

## S1 — Khar'lamov--Kulikov, Campedelli line arrangements

V. M. Kharlamov and Vik. S. Kulikov, *Surfaces with DIF != DEF real structures*.

Relevant source locator: Section 1.5, especially the definition immediately before Theorem 1.9 and Theorems 1.9--1.10.

Locked content used here:

- seven distinct lines are labeled by the seven nonzero elements of `(Z/2)^3`;
- a Campedelli arrangement has no point of multiplicity at least four and no triple point whose three labels sum to zero;
- the associated `(Z/2)^3` Galois cover of `P^2` is the canonical model of a Campedelli surface;
- Lemma 1.7 supplies the local canonical-singularity criterion at multiple points.

Audit-relevant web locator used during preparation:

```text
https://webdoc.sub.gwdg.de/ebook/serien/e/mpi_mathematik/2005/76.pdf
Section 1.5 / Theorem 1.9 / Theorem 1.10
```

No claim is made that this paper discusses perfect cuboids.

## S2 — Mendes Lopes--Pardini--Reid, degree-8 covers

M. Mendes Lopes, R. Pardini, M. Reid,
*Campedelli surfaces with fundamental group of order 8*,
Geometriae Dedicata 139 (2009), 49--55,
DOI `10.1007/s10711-008-9317-2`, arXiv `0805.0006`.

Locked theorem-level content from the abstract/paper:

```text
If Y -> S is an etale cover of degree 8 of a Campedelli surface,
then the canonical model of Y is a complete intersection of four
quadrics in P^6. Consequently Y is the universal cover of S and
the covering group is pi_1(S).
```

Stable arXiv locator:

```text
https://arxiv.org/abs/0805.0006
```

## S3 — Calabri--Mendes Lopes--Pardini, classical Campedelli description

A. Calabri, M. Mendes Lopes, R. Pardini,
*Involutions on numerical Campedelli surfaces*,
Tohoku Math. J. 60 (2008), 1--22.

Locked content:

- numerical Campedelli means `pg=q=0`, `K^2=2`;
- the classical `(Z/2)^3`-torsion family has the seven-line `(Z/2)^3` cover description;
- the seven nontrivial involutions are controlled through the bicanonical construction; quotient surfaces are among rational/Enriques-type cases in the cited analysis.

Stable locator:

```text
https://www.jstage.jst.go.jp/article/tmj/60/1/60_1_1/_pdf
Section 5, Example 1 / classical Campedelli discussion
```

## Scope firewall

The source literature certifies the Campedelli surface technology. The new repo-specific content is the exact identification and finite enumeration of those Campedelli quotient kernels inside the audited perfect-cuboid sign cover.

```text
LITERATURE_NOVELTY_CLAIM=false
PERFECT_CUBOID_CAMPEDelli_IDENTIFICATION_SOURCE_STATED_DIRECTLY=false
REPO_ADAPTER_AUDIT_REQUIRED=true
```
