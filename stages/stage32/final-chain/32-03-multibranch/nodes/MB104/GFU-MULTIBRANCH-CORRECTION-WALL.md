# Stage32 MB104 — exact Garcia-Fritz--Urzua multibranch correction wall

Status: **RETAINED NEGATIVE ROUTE / MB104 INCOMPLETE / NO CREDIT**

## Source theorem reopened

Garcia-Fritz--Urzua, *Families of explicit quasi-hyperbolic and hyperbolic surfaces*, Theorem 3.1, works on the minimal resolution `X3'` of the cuboid surface. For an irreducible image curve `C subset X3`, strict transform `C'`, and normalization `Ctilde`, the load-bearing line-bundle degree is exactly

```text
-deg(C) + (E.C') + 4g(C) - 4,
```

where `E` is the reduced sum of all 48 exceptional curves.

If that degree is negative, the curve is forced into the corresponding omega-integral locus. The paper's smooth-at-node Corollary 3.3 gives

```text
deg(C) <= 4g(C)+44.
```

The reason this sharpens in the smooth-at-node sector is that a curve smooth at a box node has only one local branch there and meets the exceptional curve with multiplicity one, so `(E.C')` is at most the number of the 48 nodes.

## MB101 adapter

For the multibranch normalization profile retained by MB101,

```text
M_i = D.E_i = sum_j m_ij,
M   = sum_i M_i = E.D.
```

Thus the GFU correction term is exactly the exceptional mass

```text
E.D = M.
```

There is no additional negative branch-excess term and no negative delta term in the theorem's degree formula. The geometric genus `g` already enters only through `4g-4`.

Consequently, outside the omega-integral exceptional locus, the direct contrapositive gives only

```text
d <= M + 4g - 4.
```

Since every minimal FSM cusp branch has exceptional multiplicity one,

```text
R8 <= M,
```

but this is the wrong direction for MB104: the GFU inequality does not upper-bound either `M` or `R8`.

## Multiple-differential refinement

Garcia-Fritz--Urzua then use four twisted differentials with different exceptional divisors. For rational curves their Theorem 3.5 / Corollary 3.6 yields lower incidence constraints, culminating in

```text
C.E >= 8
```

outside the stated exceptional/integral loci. Again this is a lower exceptional-incidence bound, not an upper normalization-branch bound.

Therefore neither the original GFU degree formula nor its four-differential refinement supplies the needed

```text
R8 <= alpha*d+beta with alpha<1/4.
```

## Exact route verdict

The hoped-for cancellation

```text
M - branch_excess,
M - Delta_exc,
or M - Delta_total
```

does not occur in the source theorem. Any such cancellation would be a new theorem, not a re-reading of GFU.

This wall does not invalidate the general strategy of constructing new twisted differentials with stronger exceptional valuations. It only closes reuse of the published GFU formulas as an existing `R8` upper-bound weapon.

## Source

- Natalia Garcia-Fritz and Giancarlo Urzua, *Families of explicit quasi-hyperbolic and hyperbolic surfaces*, Math. Z. 296 (2020), arXiv:1804.07671.
- Theorem 3.1: exact degree `-deg(C)+(E.C')+4g(C)-4`.
- Corollary 3.3: `deg(C)<=4g(C)+44` in the smooth-at-singularities sector.
- Theorem 3.5 / Corollary 3.6: lower exceptional-incidence bounds for rational curves.

## Firewalls

MB104 remains incomplete. No finite population-wide degree window, MB105 release, receiver/effectivity/final-milestone/theorem/endpoint/Perfect-Cuboid/merge credit is granted.
