# Stage32 MB104 source note — ambient Kummer torsor and finite-etale monodromy

Status: **SOURCE LOCK / STANDARD KUMMER + FINITE-ETALE INPUT / NO STAGE32 CREDIT BY ITSELF**

## Sources

Stacks Project:

1. Etale Cohomology, Section 59.28, `Kummer theory`, tag `03PK`:
   https://stacks.math.columbia.edu/tag/03PK
2. Fundamental Groups of Schemes, Section 58.6, `Fundamental groups`, tag `0BQ8`; Theorem 58.6.2, tag `0BND`:
   https://stacks.math.columbia.edu/tag/0BQ8
   https://stacks.math.columbia.edu/tag/0BND
3. Varieties, Section 33.41, `Normalization of one dimensional schemes`, tag `0C44`; Lemma 33.41.2, tag `0C1R`:
   https://stacks.math.columbia.edu/tag/0C44
   https://stacks.math.columbia.edu/tag/0C1R

The previously retained singular-Picard glueing source note remains:

```text
STACKS-NORMALIZATION-PICARD-GLUING-SOURCE-NOTE.md
```

## Locked statements used by MB104

In characteristic zero, the Kummer sequence for `n=2`

```text
0 -> mu_2 -> G_m --square--> G_m -> 0
```

is exact on the etale site. A line bundle with a chosen square trivialization therefore defines a `mu_2`-torsor; restriction/base change pulls back that torsor functorially.

For a connected scheme, finite etale covers are equivalently finite continuous `pi_1`-sets. In particular a degree-two etale cover determines a continuous character

```text
chi : pi_1(-) -> Z/2,
```

well-defined up to the harmless choice of identifying the two-element fibre with `Z/2`.

For a reduced one-dimensional scheme, normalization is finite and is an isomorphism off the singular locus. Thus a cover that becomes split after pullback to the normalization can still carry nontrivial descent/glueing data only at the singular identifications; this is the same distinction source-locked in the normalization-Picard note.

## Stage32 specialization

Let

```text
U := S \ B_abs.
```

The retained relation

```text
2 L_abs ~ B_abs
```

and its canonical branch section define the ambient degree-two cover

```text
pi_U : Y_U -> U
```

as a `mu_2`-torsor. Denote its character by

```text
alpha_abs : pi_1(U) -> Z/2.
```

For every carrier `C subset U`, the restricted etale double cover is obtained by base change, so its character is exactly the restriction of `alpha_abs`. Pulling further to the normalization `nu:E->C` gives the retained residual normalization character `eta`.

Hence in the retained `e=2` case, `eta=0` means precisely that `alpha_abs` is trivial on the image of `pi_1(E)`, while the singular conductor/glueing character can still be nonzero on loops created by identifying distinct normalization branches over singular points.

## Scope firewall

- This note does not compute `alpha_abs` on any Stage32 conductor loop.
- It does not identify arbitrary singularities with a nodal dual graph.
- It does not assert a numerical upper bound on cross-sheet conductor intersection.
- It supplies only the functorial ambient-monodromy interpretation needed by the next retained reduction.