# Stage32 MB104 — BTVA low-support finiteness adapter

Status: **RETAINED PARTIAL FINITENESS / NON-EFFECTIVE FOR PRODUCTION / NO RECEIVER CREDIT**

## Source result

Bruin--Thomas--Várilly-Alvarado, *Explicit computation of symmetric differentials and its application to quasi-hyperbolicity* (Algebra & Number Theory 16 (2022), arXiv:1912.08908), Section 7 applies their symmetric-differential machinery to the perfect cuboid surface `X_pc`, which has 48 `A1` singularities.

Their asymptotic calculation gives regular symmetric differentials on the resolution after allowing exceptional components over 35 of the 48 singularities. They conclude explicitly:

```text
there are only finitely many curves of genus 0 or 1 on X_pc
that pass through at most 13 singularities.
```

The same section notes that the Euler-characteristic lower bound first becomes positive at symmetric degree `m>=862`; the result is a finiteness theorem, not an explicit enumeration of those curves.

Their degree-two explicit forms additionally produce support/span restrictions, but those restrictions are not needed for the bounded statement retained here.

## Adapter to MB104

For an `R29-LG2-MB` carrier, let

```text
N = #{i : r_i>0}
```

be the number of **distinct** box nodes met by the normalization profile. This is exactly the singular-support quantity used by the BTVA theorem: multiple normalization branches above one surface node still contribute one point to the set of singularities through which the image curve passes.

Therefore:

```text
N <= 13
=> the genus-0/1 carrier belongs to a finite set of integral curves on X_pc.
```

This is a genuine population reduction. Any potentially infinite family in the multibranch receiver must lie in

```text
N >= 14.
```

## Why this does not close MB104

The theorem is not an explicit list and does not supply a numerical maximum canonical degree for its finite low-support set. The current Stage32 production contract requires a justified finite degree/intersection restriction before finite Picard enumeration. A bare existence statement that a finite exceptional set exists is therefore insufficient to release MB105 production enumeration.

More importantly, the remaining sector `N>=14` still has no upper bound on

```text
R8 = number of minimal cusp normalization branches (A,B)=(1,1).
```

BTVA's published support/span conclusions count distinct singular points, not normalization multiplicity over a fixed node. The retained A1 local adapter allows arbitrarily many formal minimal branches at one node with distinct exceptional landing parameters, so no implication `R8<=f(N)` is available from the current local packet.

Thus the exact state becomes:

```text
low-support sector N<=13: mathematically finite, not effectively enumerated here;
high-support sector N>=14: still requires a branch-sensitive R8 upper bound.
```

## Meromorphic extension warning

Corollary 3.4 in BTVA shows that twisting a symmetric differential by a hyperplane through an `A1` point regularizes its pullback along the corresponding exceptional component. Their genus-0/1 arguments choose hyperplanes using the set of singular points met by the curve. This explains why the retained theorem naturally controls support/span.

A new branchwise meromorphic refinement could in principle track poles separately on normalization branches, but that refinement is not contained in the published theorem and no `R8` upper bound follows from the cited result alone. Such a refinement remains new-theorem work.

## Firewalls

- `N<=13` finiteness is retained as a partial theorem-backed reduction.
- No explicit degree cap for that finite set is claimed.
- No enumeration completeness is claimed.
- No `R8` upper bound for `N>=14` is claimed.
- MB104 remains incomplete; MB105 is not released.
- No receiver, effectivity, final-milestone, theorem, endpoint, Perfect Cuboid, or merge credit is granted.
