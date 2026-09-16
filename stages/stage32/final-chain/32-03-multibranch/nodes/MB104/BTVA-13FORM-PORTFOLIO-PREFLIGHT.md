# Stage32 MB104 — BTVA 13-form exceptional-valuation portfolio preflight

Status: **ACTIVE PREFLIGHT / NO MATHEMATICAL CREDIT**

## Why this is now the concrete next computation

The retained MB104 inequality is

```text
d <= 16g - 16 + 4R8,
```

so the remaining task is a genuinely branch-sensitive upper bound on the number `R8` of minimal cusp branches. Several scalar routes are now dominated: exceptional mass/Hodge, simple genus-5 fibration intersections, summed unit Riemann--Hurwitz charging, the published GFU correction term, and pure powers of the single BTVA form `omega_7`.

BTVA nevertheless provide more structure than `omega_7` alone. On the perfect cuboid surface they compute

```text
dim H^0(X, SymHat^2 Omega_X^1) = 13
```

and give an explicit 13-element basis in their ancillary Magma output. In the same calculation they exhibit nonuniform exceptional behavior: `omega_1` already pulls back regularly over the exceptional curves above singular points satisfying `y1=0`; by symmetry analogous statements hold after permuting the coordinate directions. Thus the 13-dimensional space has node-dependent intrinsic regularity that is invisible in the one-form/pure-power wall.

This makes the exact **48-node exceptional-valuation matrix of the 13-dimensional order-two space** the next load-bearing object.

## Local linear-algebra target

For every one of the 48 `A1` nodes `P_i`, let

```text
V = H^0(X, SymHat^2 Omega_X^1),   dim V=13.
```

The BTVA local Euler characteristic for an `A1` singularity at symmetric order `m=2` is

```text
chi^0(P_i, Sym^2 Omega) = 3.
```

Accordingly, regular extension across the exceptional component over `P_i` is controlled by at most three independent local principal-part conditions on `V`. The production object to materialize is a matrix

```text
L_i : V -> W_i,   dim W_i <= 3,
```

whose kernel is exactly the subspace of the 13 explicit forms with regular pullback at that exceptional curve.

The first computation should reconstruct each `L_i` from the explicit BTVA forms/local `A1` coordinates, not infer it from the dimension count alone. The `chi^0=3` value is a budget/checksum, not a claim that every `L_i` has rank exactly three.

## Required finite computation

1. Source-lock the 48 singular points and the 13 BTVA order-two generators in a common coordinate convention.
2. For each node, choose the standard `A1` resolution chart and compute the pullback principal part of all 13 generators.
3. Reduce those principal parts to an exact coefficient matrix `L_i` over the source field.
4. Record `rank(L_i)`, `dim ker(L_i)`, and a canonical basis for the kernel.
5. Quotient the 48 matrices by the already retained `Aut(S)` action, while preserving exact source-node labels.
6. Compute intersections and products of the intrinsic-regularity subspaces. In particular test whether there is a nonzero order-two form regular at all 48 exceptional components, and if not, determine the best achievable exceptional coverage without external hyperplane twisting.
7. Only after that, solve the higher-order product/twist optimization: combine intrinsically regular factors with hyperplane vanishing and ask whether the effective regularization cost per minimal branch can be driven below the retained `1/2` order ratio.

## Exact success criterion for MB104 relevance

A positive portfolio result matters only if it yields a global differential inequality whose minimal-branch penalty improves the FSM coefficient enough to imply

```text
R8 <= alpha*d + beta,  alpha < 1/4,
```

or directly gives a finite degree window on the remaining high-span sectors.

It is not enough merely to find a form regular at many nodes: node support and normalization multiplicity are distinct. The resulting differential must still be evaluated branchwise on multiple normalization branches above one node.

## Source locks to use

Primary source:

```text
Bruin--Thomas--Varilly-Alvarado,
Explicit computation of symmetric differentials and its application to quasi-hyperbolicity,
arXiv:1912.08908 / Algebra & Number Theory 16 (2022).
```

Required source facts:

- the perfect cuboid surface has 48 `A1` singularities;
- the reflexive order-two symmetric-differential space has dimension 13;
- Table 7.1 / ancillary output gives explicit generators;
- `omega_7` has one hyperplane of vanishing;
- `omega_1` has regular pullback above the stated `y1=0` singular subset;
- Corollary 3.4 gives the `floor(m/2)` hyperplane-twist regularization rule.

Repository-side geometry lock:

```text
MichaelStollBayreuth/Verification
commit 51233ed5ef2bf228fac9416c66db9adc0ebcaadd
Cuboids/cuboids.magma
blob 0422b69847f2afb97cb7b3ed02ebef91279f61b1
```

This supplies the 48 singular points, Picard model, and `Aut(S)` permutation action already consumed by MB103.

## Firewalls

This preflight does **not** claim that the 48 local matrices have been materialized, that a globally regular symmetric differential exists, or that any `R8` upper bound has been obtained. MB104 remains incomplete and MB105 remains unreleased. No receiver/effectivity/final-milestone/theorem/endpoint/Perfect-Cuboid/merge credit is granted.
