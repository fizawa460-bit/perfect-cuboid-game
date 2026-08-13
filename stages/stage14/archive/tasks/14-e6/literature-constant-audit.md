# Stage14-e6 — literature-first audit for the explicit ambient constant

## Scope

Stage14-e6 sharpens the e4 asymptotic

\[
E_q(B)\sim\Lambda_E M_q B(\log B)^5
\]

for the physical Euclidean projective height by computing the previously unnamed common factor `Lambda_E`.

The literature gate remains

```text
EXACT_COLLISION
ADJACENT_RESULT
REUSABLE_METHOD
NO_COLLISION_FOUND_IN_CURRENT_SEARCH
NOVELTY_BY_SEARCH_ABSENCE=false
```

Only theorem-level normalization and general toric machinery are imported.  The effective-cone volume, the physical finite-place metric, the exceptional `p=2` factor, and the resulting Euler product are computed for the repository's specific morphism.

## 1. Batyrev--Tschinkel — toric Manin asymptotic

Victor V. Batyrev and Yuri Tschinkel, *Manin's conjecture for toric varieties*, J. Algebraic Geom. 7 (1998), 15--53; arXiv:alg-geom/9510014.

Classification:

```text
REUSABLE_METHOD — THEOREM_LEVEL_INPUT
```

This is the global toric bounded-height theorem already used in e3.  It establishes the anticanonical Manin asymptotic for smooth projective toric varieties.

Related analytic source:

Victor V. Batyrev and Yuri Tschinkel, *Height Zeta Functions of Toric Varieties*, arXiv:alg-geom/9606003.

This treats height zeta functions for line bundles whose first Chern class lies in the interior of the effective cone and provides the analytic framework for the leading pole.

## 2. Peyre — normalization of the leading constant

Emmanuel Peyre, *Hauteurs et mesures de Tamagawa sur les varietes de Fano*, Duke Math. J. 79 (1995), 101--218.

Emmanuel Peyre, *Terme principal de la fonction zeta des hauteurs et torseurs universels*, Asterisque 251 (1998), 259--298; Numdam `AST_1998__251__259_0`.

Classification:

```text
REUSABLE_METHOD — CONSTANT_NORMALIZATION
```

For an almost-Fano height problem the leading coefficient is organized as

```text
alpha(Y) * beta(Y) * tau_H
```

with `alpha` determined by the dual effective cone, `beta` by Galois cohomology of the geometric Picard group, and `tau_H` the Tamagawa measure attached to the chosen adelic anticanonical metric.

Stage14-e6 follows this normalization.  It does not claim the general Peyre formalism as new.

## 3. Salberger — universal torsor / Tamagawa normalization

Per Salberger, *Tamagawa measures on universal torsors and points of bounded height on Fano varieties*, Asterisque 251 (1998), 91--258; Numdam `AST_1998__251__91_0`.

Classification:

```text
REUSABLE_METHOD — LOCAL_MEASURE_NORMALIZATION
```

This is a primary source for the split rational/torsor normalization and local Tamagawa factors.  It is used only as general background; e6 computes the local integrals directly from the physical projective metric.

## 4. Huang v3 — current equidistribution statement for arbitrary adelic norm

Zhizhong Huang, *Equidistribution of rational points and the geometric sieve for toric varieties*, arXiv:2111.01509v3, revised 17 July 2026.

Classification:

```text
REUSABLE_METHOD — THEOREM_LEVEL_INPUT
```

Huang proves the Manin--Peyre equidistribution principle for smooth proper split toric varieties over `Q` with globally generated anticanonical bundle.  The normalization uses

```text
alpha(V) beta(V) B (log B)^(rho-1)
```

and the Tamagawa measure induced by the fixed adelic norm on `-K_V`.  Huang also records that validity for one adelic norm is equivalent to validity for any adelic norm, which is important here because the physical Euclidean/projective metric is not the canonical toric metric at `p=2`.

## 5. Collision status for the e6 explicit product

The current primary-source search found the general constant formalism and toric theorem, but no source spelling out the Stage14-e physical metric on

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1)
\]

with the specific projective sections

\[
4u_1v_1u_2v_2,
\quad
2(u_1^2-v_1^2)u_2v_2,
\quad
2(u_2^2-v_2^2)u_1v_1,
\]

nor the resulting bad-prime `p=2` local integral.

Classification:

```text
DIRECT_STAGE14_E6_CONSTANT=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
NOVELTY_BY_SEARCH_ABSENCE=false
```

This is not a novelty certificate.  It only records the search boundary used for this substage.
