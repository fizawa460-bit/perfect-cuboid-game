# Stage14-4av — CRT factorization of the first Euclid-incidence reciprocal blocks

## Result

Stage14-4au reduced the first local quantitative gap to reciprocal divisor blocks. Stage14-s5h has since supplied the first unconditional separable quadratic-character estimate

\[
\left|\sum_{u\asymp U}^{*}\sum_{v\asymp V}^{*}
\alpha_u\beta_v\left(\frac uv\right)\right|
\ll_\varepsilon
(UV)^\varepsilon\sqrt{U+V}\,\|\alpha\|_2\|\beta\|_2,
\]

but s5h correctly stops before the full Stage14 incidence weight because the actual coefficient is a two-variable matrix.

Stage14-4av proves that this matrix obstruction is **not already present in the bare geometry of the six whole-kernel reciprocal edges among the four linear Euclid factors**. For those edges the divisibility incidence has a separable CRT main term plus an elementary boundary error, and the s5h bilinear theorem therefore gives a genuine uniform power saving on the interior dyadic divisor range.

This does not yet control the full state-split local indicator. The remaining correlation is now localized in the growing auxiliary divisor/state weight, primitive-gcd bookkeeping, the state-split `m^2+n^2` pieces, and dyadic endpoint ranges.

## 1. The six linear whole-kernel edges

Use

\[
L_1=m,\qquad L_2=n,\qquad L_3=m-n,\qquad L_4=m+n.
\]

There are six unordered pairs. Their coefficient determinants have absolute values

```text
m -- n       : 1
m -- (m-n)   : 1
m -- (m+n)   : 1
n -- (m-n)   : 1
n -- (m+n)   : 1
(m-n)--(m+n) : 2
```

so the only non-unimodular pair has determinant `2`, harmless for the odd moduli in the reciprocal system. This is the same six-edge whole-kernel graph isolated in s5h after the `m^2+n^2` column collapses.

## 2. Bare opposite-parity incidence

Fix a dyadic rectangle

\[
M<m\le2M,\qquad N<n\le2N,
\]

and distinct linear forms `L_i,L_j`. For coprime odd `u,v`, let

\[
C_{ij}(u,v;M,N)
\]

be the number of integer pairs in the rectangle satisfying

\[
m\not\equiv n\pmod2,\qquad
u\mid L_i(m,n),\qquad v\mid L_j(m,n).
\]

The two odd congruences impose an index-`uv` lattice condition. Because `uv` is odd, the two opposite-parity residue classes split this lattice with total density `1/2`. Explicit elimination for the six pairs (with `2` invertible for the `(m-n,m+n)` pair) and the standard count of one residue class in an interval give uniformly

\[
\boxed{
C_{ij}(u,v;M,N)
=\frac{MN}{2uv}
+O\!\left((M+N)\left(\frac1u+\frac1v\right)+1\right).}
\]

The implied constant is absolute for this fixed six-form system.

This is a statement about the **bare divisibility incidence**. It deliberately does not include the primitive condition `gcd(m,n)=1`, complementary state pieces, other local rows, or the physical height weight.

## 3. Reciprocal block estimate

Define

\[
\mathcal B_{ij}^{\rm bare}(U,V;M,N)
=\sum_{u\asymp U}^{*}\sum_{v\asymp V}^{*}
\left(\frac uv\right) C_{ij}(u,v;M,N),
\]

with odd squarefree support and the Jacobi symbol zero on non-coprime pairs if necessary.

Insert the CRT asymptotic. The main term is

\[
\frac{MN}{2}
\sum_{u\asymp U}^{*}\sum_{v\asymp V}^{*}
\frac1u\frac1v\left(\frac uv\right).
\]

Apply the s5h separable bilinear estimate with

\[
\alpha_u=u^{-1},\qquad \beta_v=v^{-1}.
\]

Since

\[
\|\alpha\|_2\ll U^{-1/2},\qquad
\|\beta\|_2\ll V^{-1/2},
\]

the main term is

\[
\ll_\varepsilon
MN(UV)^\varepsilon
\frac{\sqrt{U+V}}{\sqrt{UV}}.
\]

For the lattice remainder, triangle inequality is now safe because it is an explicit geometric error, not the character main term. Summing the remainder over `u~U,v~V` gives

\[
\ll (M+N)(U+V)+UV.
\]

Hence

\[
\boxed{
\mathcal B_{ij}^{\rm bare}
\ll_\varepsilon
MN(UV)^\varepsilon\frac{\sqrt{U+V}}{\sqrt{UV}}
+(M+N)(U+V)+UV.}
\]

This is the first uniform Euclid-**incidence** reciprocal block estimate in the main `14-4` track.

## 4. Interior dyadic power saving

On a balanced Euclid box `M~N~X`, suppose for fixed

\[
0<\kappa<\frac12
\]

that both divisor sides lie in the interior range

\[
X^\kappa\le U,V\le X^{1-\kappa}.
\]

Then

\[
\frac{\sqrt{U+V}}{\sqrt{UV}}
\ll X^{-\kappa/2},
\]

and the two geometric remainder terms satisfy

\[
X(U+V)\ll X^{2-\kappa},\qquad
UV\ll X^{2-2\kappa}.
\]

Therefore

\[
\boxed{
\mathcal B_{ij}^{\rm bare}
\ll_\varepsilon X^{2-\kappa/2+\varepsilon}.}
\]

Relative to the trivial `X^2` family scale, this is a fixed power saving `X^{-kappa/2+epsilon}` on every interior block. No independence heuristic is used.

## 5. What remains correlated

The actual 14-4au block contains more than the bare incidence kernel. Its coefficient retains:

1. complementary selected/unselected divisor pieces from the other local rows;
2. the primitive `gcd(m,n)=1` restriction, which becomes a Möbius sum if separated;
3. state-split pieces of `m^2+n^2`, for which the whole-kernel `e`-column collapse from s5h cannot simply be applied piecewise;
4. endpoint blocks where one divisor side is very small, very large, or the two sides are strongly unbalanced.

If finitely many auxiliary residue conditions with a **fixed modulus** coprime to `2uv` are frozen, the same CRT argument persists: the main density remains separable up to the fixed residue-class factor. The real problem is that the full local expansion sums over a **growing auxiliary modulus/state**, so the coefficient matrix is not yet a bounded finite-rank perturbation of the bare kernel.

Thus the remaining obstruction is refined to

```text
GROWING_AUXILIARY_STATE_INCIDENCE_COUPLING
```

rather than bare Euclid divisibility itself.

## 6. Repair of the merged 14-4au CI artifact

The merged 14-4au mathematical audit succeeded, but its dedicated workflow failed at the generated-summary diff check. The committed JSON had the `five_factors` array on one line, while `json.dumps(indent=2)` rewrote that array over multiple lines. The failure was formatting-only; the deterministic audit itself had already completed successfully.

Stage14-4av normalizes that JSON to the exact generated format. Because the 4au workflow watches that summary path, the new PR also re-runs the 4au validation.

## Boundary

```text
STAGE14_4AV=BARE_LINEAR_EDGE_CRT_FACTORIZATION_AND_INTERIOR_POWER_SAVING_PROVED
S5H_SEPARABLE_BILINEAR_BOUND_IMPORTED=true
SIX_LINEAR_WHOLE_KERNEL_EDGES_CRT_FACTORIZED=true
BARE_OPPOSITE_PARITY_INCIDENCE_ASYMPTOTIC_PROVED=true
BARE_RECIPROCAL_BLOCK_BOUND_PROVED=true
INTERIOR_DYADIC_POWER_SAVING_PROVED=true
FULL_AUXILIARY_STATE_WEIGHT_SEPARABILITY_PROVED=false
ENDPOINT_DYADIC_BLOCKS_CONTROLLED=false
EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED=false
EXPLICIT_E_LOC_PROVED=false
POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false
POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

The result is therefore a genuine local analytic advance, but not yet a completed `rho_loc/E_loc` theorem. In particular it does not promote the bare-block saving to the full Selmer indicator before the growing auxiliary state weight and endpoint ranges are controlled.

```text
NEXT=Stage14-4aw lift the bare CRT block estimate to the growing auxiliary state weight via modulus freezing/dispersion and primitive Mobius bookkeeping, while isolating and summing the dyadic endpoint ranges
```
