# Stage14-tH17 — signed orthogonal-rectangle Kummer bilinear large-sieve audit

## Purpose

Merged Stage14-t61 reopens the zero-loss route before polar absolute value and asks for an independent audit of

```text
SignedOrthogonalRectangleKummerBilinearLargeSieve
```

on the exact t59 orthogonal-rectangle packet.

The target for one t59 family

\[
\mathcal R=\{A_j\times B_j\}_j
\]

is

\[
\boxed{
\sum_{p\ne q}
\left|
\sum_j\sum_{\pi\in A_j}\sum_{V\in B_j}
K_p(t_\pi,x_V)K_q(t_\pi,x_V)
\right|^2
\ll
P^2 R_{\mathcal R}B^{o(1)},
}
\tag{H17.1}
\]

where

\[
R_{\mathcal R}=\sum_j |A_j||B_j|.
\tag{H17.2}
\]

The mandatory structure is:

```text
same auxiliary pair (p,q) on both physical coordinates
signed Kummer kernel retained inside the outer pair average
pairwise-disjoint row projections A_j
pairwise-disjoint column projections B_j
t59 aspect-energy balance
no polar |C_pq|
no entrywise absolute-value replacement
no squareclass precollapse
no independent pi/V modulus tensorisation
```

Stage14-tH17 tests four possible tools:

1. same-modulus bilinear/trace large sieve before polarisation;
2. TT* / dual large sieve;
3. operator-valued / Hilbert-space large sieve;
4. t59 row/column orthogonality plus aspect-energy balance.

The outcome is mixed: TT* and operator language give a useful exact reduction, but no currently certified theorem supplies the required arithmetic vertical Gram bound. The exact minimal operator obstruction is smaller and cleaner than the pre-tH17 formulation.

No Stage14 global power saving is claimed.

---

## 1. Exact physical matrix formulation

Fix one t59 family and let

\[
S_{\mathcal R}=\bigsqcup_j(A_j\times B_j).
\]

Because the row and column projections are disjoint inside the family, the rectangles themselves are disjoint and

\[
|S_{\mathcal R}|=R_{\mathcal R}.
\tag{H17.3}
\]

For each good split auxiliary prime `r`, define the signed physical Kummer row vector

\[
V_{\mathcal R}(r,s)=K_r(s)
=K_r(t_\pi,x_V),
\qquad
s=(\pi,V)\in S_{\mathcal R}.
\tag{H17.4}
\]

Thus `V_R` is a `P x R_R` matrix indexed vertically by auxiliary primes and horizontally by physical states.

For the unit-weight raw physical trace, define

\[
T_{pq}=\sum_{s\in S_{\mathcal R}}K_p(s)K_q(s).
\tag{H17.5}
\]

Then exactly

\[
\boxed{
(T_{pq})_{p,q}=V_{\mathcal R}V_{\mathcal R}^{T}.
}
\tag{H17.6}
\]

Hence the requested signed two-prime moment is the off-diagonal Frobenius mass

\[
\boxed{
\sum_{p\ne q}|T_{pq}|^2
=\|\operatorname{offdiag}(V_{\mathcal R}V_{\mathcal R}^{T})\|_{HS}^2.
}
\tag{H17.7}
\]

No polar operator appears in (H17.6)--(H17.7). The signs of `K_r` are retained until the outer norm square is formed.

For bounded physical coefficients `w_s`, the corresponding exact identity is

\[
T_{pq}(w)=\bigl(V_{\mathcal R}D_wV_{\mathcal R}^{T}\bigr)_{pq},
\tag{H17.8}
\]

with `D_w=diag(w_s)`. The unit-weight case is the canonical t59/t61 target and is sufficient for the raw-trace route already frozen in t60.

```text
SIGNED_PHYSICAL_TO_VERTICAL_MATRIX_IDENTITY_PROVED=true
POLAR_ABSOLUTE_VALUE_USED=false
```

---

## 2. TT* gives an exact vertical Gram / Schatten-4 reduction

Let

\[
G_{\mathcal R}=V_{\mathcal R}^{T}V_{\mathcal R},
\qquad
G_{\mathcal R}(s,t)=\sum_{r\in\mathcal P}K_r(s)K_r(t).
\tag{H17.9}
\]

For real quadratic Kummer values, matrix algebra gives

\[
\|V_{\mathcal R}V_{\mathcal R}^{T}\|_{HS}^2
=\operatorname{Tr}\bigl((V_{\mathcal R}^{T}V_{\mathcal R})^2\bigr)
=\|V_{\mathcal R}\|_{S_4}^4.
\tag{H17.10}
\]

Equivalently,

\[
\boxed{
\sum_{p,q}|T_{pq}|^2
=\sum_{s,t\in S_{\mathcal R}}
\left|\sum_r K_r(s)K_r(t)\right|^2.
}
\tag{H17.11}
\]

This is the exact `TT*` identity for the signed rectangle problem.

The `p=q` diagonal satisfies trivially

\[
\sum_p |T_{pp}|^2\le P R_{\mathcal R}^2.
\tag{H17.12}
\]

Therefore in the already-used natural amplifier regime

\[
R_{\mathcal R}\le P B^{o(1)},
\tag{H17.13}
\]

the auxiliary diagonal is target-scale, and (H17.1) is equivalent up to `B^{o(1)}` bookkeeping to the one-prime operator theorem

```text
OrthogonalRectangleVerticalKummerSchatten4 (ORVKS4)
```

\[
\boxed{
\|V_{\mathcal R}\|_{S_4}^4
\ll P^2R_{\mathcal R}B^{o(1)}.
}
\tag{H17.14}
\]

Thus TT* does produce a useful reduction: the two-prime signed problem becomes a one-prime **vertical fourth-Schatten moment**.

However (H17.11) is positive after TT*. It does not preserve cancellation between different state pairs; it asks for square-summability of the vertical pair correlations. This is a different positivity mechanism from the forbidden t61 polar operator, but it exposes the principal-coherence obstruction directly.

```text
TTSTAR_VERTICAL_SCHATTEN4_IDENTITY_PROVED=true
TTSTAR_DIRECTLY_PROVES_TARGET=false
```

---

## 3. Stronger dual/Bessel theorem that would close the target

A standard Hilbert-space large-sieve route asks for the one-prime Bessel bound

```text
OrthogonalRectangleOnePrimeKummerBessel (ORKB)
```

\[
\boxed{
\sum_{r\in\mathcal P}
\left|
\sum_{s\in S_{\mathcal R}}a_sK_r(s)
\right|^2
\ll
P B^{o(1)}\sum_s|a_s|^2
}
\tag{H17.15}
\]

uniformly in coefficients `a_s` on the physical rectangle union.

In matrix language this is

\[
\boxed{
\|V_{\mathcal R}\|_{op}^2\ll P B^{o(1)}.
}
\tag{H17.16}
\]

Since every entry has modulus at most one,

\[
\|V_{\mathcal R}\|_{HS}^2\le PR_{\mathcal R}.
\tag{H17.17}
\]

Therefore

\[
\|V_{\mathcal R}\|_{S_4}^4
\le
\|V_{\mathcal R}\|_{op}^2
\|V_{\mathcal R}\|_{HS}^2
\ll
P^2R_{\mathcal R}B^{o(1)}.
\tag{H17.18}
\]

So ORKB implies ORVKS4 and hence the t61 signed target.

This implication is fully non-polar and costs no fixed power.

```text
ONE_PRIME_VERTICAL_KUMMER_BESSEL_IMPLIES_SIGNED_RECTANGLE_TARGET=true
ONE_PRIME_VERTICAL_KUMMER_BESSEL_PROVED=false
```

ORKB is stronger than necessary; ORVKS4 is the exact minimal operator target.

---

## 4. Dual large sieve does not manufacture the missing arithmetic

The dual Gram for ORKB is exactly (H17.9):

\[
G_{\mathcal R}(s,t)=\sum_rK_r(s)K_r(t).
\]

Hilbert-space duality converts (H17.15) into

\[
\|G_{\mathcal R}\|_{op}\ll P B^{o(1)}.
\tag{H17.19}
\]

This is a valid reformulation, not an estimate supplied for free.

The obstruction is visible on equal-squareclass states. If physical states `s,t` have the same relevant Kummer squareclass, then for every common good auxiliary prime

\[
K_r(s)K_r(t)=1.
\tag{H17.20}
\]

Hence

\[
G_{\mathcal R}(s,t)=P-O(B^{o(1)}).
\tag{H17.21}
\]

If `h` states form one coherent squareclass block, the corresponding Gram block is approximately `P J_h`, with largest eigenvalue approximately `Ph`. Thus ORKB forces

\[
h\le B^{o(1)}.
\tag{H17.22}
\]

This is at least as strong as excluding the principal squareclass coherence that Stage14 has been trying to prove.

For ORVKS4 the same block contributes approximately

\[
P^2h^2
\tag{H17.23}
\]

against target contribution `P^2h B^{o(1)}`. Thus the Schatten-4 formulation is not circular by definition, but it makes the exact principal obstruction transparent: coherent squareclass blocks must have near-linear total fourth energy.

Therefore a dual large-sieve proof may be useful only if it supplies a genuinely new arithmetic estimate for the **vertical Kummer Gram**. Merely invoking duality or a generic Bessel principle does not close the receiver.

This agrees with the general abstract large-sieve principle: the formal Hilbert-space inequality reduces the problem to bounding a large-sieve constant/operator norm, and arithmetic input is still required to estimate that constant.

```text
DUAL_LARGE_SIEVE_FORMULATION_VALID=true
DUALITY_ALONE_CLOSES_TARGET=false
DUAL_GRAM_PRINCIPAL_COHERENCE_OBSTRUCTION_EXPLICIT=true
```

---

## 5. t59 row/column orthogonality is valuable but not sufficient

For one t59 family define the physical coefficient matrix

\[
W_{\mathcal R}
=\sum_j {\bf1}_{A_j}{\bf1}_{B_j}^{T}.
\tag{H17.24}
\]

Because the row projections `A_j` are pairwise disjoint and the column projections `B_j` are pairwise disjoint, the rank-one blocks are orthogonal in Hilbert--Schmidt space. Therefore

\[
\boxed{
\|W_{\mathcal R}\|_{HS}^2
=\sum_j |A_j||B_j|
=R_{\mathcal R}.
}
\tag{H17.25}
\]

Moreover its nonzero singular values are exactly

\[
\sqrt{|A_j||B_j|}.
\tag{H17.26}
\]

Thus t59 has already solved the **source-energy geometry**: no ambient Cartesian mass and no rectangle-count Cauchy factor is necessary.

The aspect bucket gives

\[
\left(\sum_j|A_j|^2\right)
\left(\sum_j|B_j|^2\right)
\le2R_{\mathcal R}^2.
\tag{H17.27}
\]

This is exactly what t60 needed after obtaining separate one-side bounds.

But neither (H17.25) nor (H17.27) controls the vertical Gram (H17.9). A single rectangle already satisfies both identities optimally. If all Kummer rows are coherent on that rectangle, then

\[
T_{pq}=R_{\mathcal R}
\]

for all auxiliary pairs and

\[
\sum_{p\ne q}|T_{pq}|^2
=P(P-1)R_{\mathcal R}^2,
\tag{H17.28}
\]

which misses the desired scale by a factor `R_R`.

So:

```text
T59_RECTANGLE_ORTHOGONALITY_SOURCE_ENERGY_PROVED=true
T59_ASPECT_BALANCE_SOURCE_COMBINATION_PROVED=true
T59_GEOMETRY_ALONE_IMPLIES_VERTICAL_CANCELLATION=false
```

The t59 geometry should be retained, but the remaining theorem must use arithmetic variation in the Kummer values across auxiliary primes.

---

## 6. Horizontal same-modulus bilinear/trace theorems do not directly iterate

The t59 decomposition removes one previous support obstruction: on each rectangle, the physical support is literally `A_j x B_j`.

However the one-prime kernel remains

\[
K_r(t,x)
=\chi_r((x^2-t^2)(1-t^2x^2))
=A_r(x/t)A_r(tx),
\tag{H17.29}
\]

a genuinely bivariate rank-one Kummer kernel.

### Ping Xi arbitrary-set bilinear theorem

Ping Xi's arbitrary-set theorem is formulated for one finite field and bilinear forms of the type

\[
\sum_{m,n}\alpha_m\beta_n K(mn)
\]

with `K` coming from a bountiful sheaf (rank at least two), with special additional cases such as Kloosterman and elliptic Frobenius traces.

The t57/t61 kernel is rank one and is not a one-variable `K(mn)` kernel in the physical `(t,x)` rectangle coordinates. Therefore the theorem is not a direct import even after t59 rectangularization.

### Fouvry--Kowalski--Michel--Sawin type-I/II trace technology

The newer general trace-bilinear machinery also works by classifying correlations of a one-field trace-function family after specified monomial transforms. Merged t57 already records that its main high-rank/gallant theorem is not a ready-made rank-one theorem for the present ratio/product packet.

The t59 rectangles improve the support shape but do not change this algebraic mismatch.

### Why applying a one-prime theorem twice is not automatic

For the two-prime kernel

\[
K_{pq}(t,x)=K_p(t,x)K_q(t,x),
\tag{H17.30}
\]

one might try to apply a bilinear theorem at `p`, treating `K_q` as a coefficient. This is illegal for the standard separated bilinear hypotheses: `K_q(t,x)` is itself bivariate and does not factor as a row coefficient times a column coefficient.

Expanding `K_q` into its full Mellin packet restores coefficient separation but returns the full-mode Cauchy/orthogonality loss already rejected by tH16, unless a new matrix-valued theorem keeps the packet signed.

Thus

```text
PING_XI_RECTANGLE_DIRECT_IMPORT_VALID=false
FKMS_RECTANGLE_DIRECT_IMPORT_VALID=false
ONE_PRIME_HORIZONTAL_BILINEAR_THEOREM_ITERATES_TO_SHARED_PQ=false
```

No existing horizontal trace theorem is promoted here to proof of (H17.1).

---

## 7. Operator-valued large sieve: exact useful formulation, no automatic theorem

The natural operator-valued object is the analysis map

\[
\mathcal A_{\mathcal R}:\ell^2(S_{\mathcal R})\to\ell^2(\mathcal P),
\qquad
(\mathcal A a)(r)=\sum_s a_sK_r(s).
\tag{H17.31}
\]

Then

\[
\mathcal A=V_{\mathcal R},
\qquad
\mathcal A^*\mathcal A=G_{\mathcal R}.
\tag{H17.32}
\]

The desired strong operator-valued large-sieve constant is

\[
\|\mathcal A\|^2\ll PB^{o(1)}.
\]

This is exactly ORKB.

A weaker, target-exact operator statement is the Schatten condition

\[
\|\mathcal A\|_{S_4}^4\ll P^2R_{\mathcal R}B^{o(1)},
\]

which is ORVKS4.

Thus operator-valued language is useful because it identifies the correct norm and separates:

```text
horizontal one-modulus operator C_r       # t61
vertical auxiliary-prime analysis A_R     # tH17
```

These are different operators. The proved t61 estimate

\[
\|C_r\|_{op}\ll r^{-1/4}
\tag{H17.33}
\]

does not imply a bound for `||A_R||`: `C_r` acts between the complete row/column character spaces at one fixed modulus, while `A_R` acts from physical states to the family of varying auxiliary primes.

No standard operator-valued large-sieve theorem identified in the audit turns the horizontal bounds (H17.33), rectangle disjointness, and aspect balance alone into ORKB/ORVKS4.

```text
HORIZONTAL_C_R_OPERATOR_BOUND_TRANSFERS_TO_VERTICAL_A_R=false
OPERATOR_VALUED_FORMULATION_PROVED=true
OPERATOR_VALUED_LARGE_SIEVE_TARGET_PROVED=false
```

---

## 8. Exact minimal theorem contracts after tH17

Stage14-t62 has two legal targets, one exact and one stronger.

### Route A — exact minimal operator theorem

```text
OrthogonalRectangleVerticalKummerSchatten4
```

For every legal t59 energy-balanced orthogonal rectangle family,

\[
\boxed{
\sum_{s,t\in S_{\mathcal R}}
\left|\sum_{r\in\mathcal P}K_r(s)K_r(t)\right|^2
\ll
P^2R_{\mathcal R}B^{o(1)}.
}
\tag{H17.34}
\]

Equivalently,

\[
\|V_{\mathcal R}\|_{S_4}^4
\ll P^2R_{\mathcal R}B^{o(1)}.
\]

This is the signed two-prime receiver after TT*, not a stronger squareclass collapse.

A proof should separate:

1. exact diagonal `s=t`;
2. same-row / same-column physical pairs, where existing one-variable arithmetic may be reusable;
3. genuinely transverse nonprincipal pairs;
4. equal-squareclass principal transverse pairs.

It must not apply absolute Schur summation across all state pairs before that separation.

### Route B — stronger one-prime Bessel theorem

```text
OrthogonalRectangleOnePrimeKummerBessel
```

prove (H17.15). This immediately implies Route A via (H17.18).

However Route B already forbids any polynomial coherent squareclass block, so it should not be assumed merely as a generic large-sieve input.

### What is not enough

The following are insufficient on their own:

```text
t59 disjoint rectangles
+t59 aspect-energy balance
+t61 horizontal C_r operator norm
+generic Hilbert-space duality
+generic same-field bilinear trace theorem
```

The missing content is vertical arithmetic decorrelation across the auxiliary prime family.

---

## 9. Literature applicability boundary

The literature was used only to audit theorem shape.

- Emmanuel Kowalski, *The principle of the large sieve*, arXiv:math/0610021: supports the abstract operator/duality viewpoint, but the large-sieve constant still requires a separate arithmetic bound.
- Ping Xi, *Bilinear forms with trace functions over arbitrary sets, and applications to Sato--Tate*, arXiv:2211.14702: one-field `K(mn)` / bountiful-sheaf theorem; not a direct theorem for the rank-one bivariate Kummer rectangle packet.
- Fouvry--Kowalski--Michel--Sawin, *Bilinear forms with trace functions*, arXiv:2511.09459: powerful one-field type-I/II technology, but no certified direct import for the present shared-two-prime rank-one packet.

No cited theorem is promoted to proof of ORVKS4 or ORKB.

---

## 10. Direct handoff to Stage14-t62

Stage14-t62 may import:

```text
signed target
  = off-diagonal HS norm of V_R V_R^T

full pair moment
  = ||V_R||_S4^4
  = sum_{s,t}|sum_r K_r(s)K_r(t)|^2

natural amplifier diagonal
  p=q is target-scale when R_R <= P*B^o(1)

sufficient stronger theorem
  ||V_R||_op^2 <= P*B^o(1)
  => signed rectangle target

source geometry
  ||W_R||_HS^2 = R_R
  aspect balance remains exact

live arithmetic obstruction
  vertical Kummer Gram / coherent principal blocks
```

The recommended order is:

1. keep t59 rectangle family intact;
2. form the vertical one-prime Gram before any squareclass collapse;
3. remove exact / same-row / same-column contributions using already-proved local arithmetic where legal;
4. study the transverse vertical correlation
   \[
   \sum_rK_r(s)K_r(t)
   \]
   as a prime-family Frobenius/reciprocity object;
5. only after principal/nonprincipal separation decide whether a spectral, Chebotarev, reciprocity, or dispersion estimate can bound the remaining Schatten-4 energy.

Do not use `|C_{pq}|`, and do not replace the vertical Gram by its entrywise absolute value before principal/nonprincipal separation.

---

## Locked boundary

```text
STAGE14_TH17=COMPLETE_SIGNED_RECTANGLE_TTSTAR_OPERATOR_LARGE_SIEVE_APPLICABILITY_AUDIT
MERGED_T59_IMPORTED=true
MERGED_T61_IMPORTED=true
SIGNED_PHYSICAL_TO_VERTICAL_MATRIX_IDENTITY_PROVED=true
POLAR_ABSOLUTE_VALUE_USED=false
TTSTAR_VERTICAL_SCHATTEN4_IDENTITY_PROVED=true
AUXILIARY_DIAGONAL_TARGET_SCALE_IF_R_LE_P_BO1=true
ORTHOGONAL_RECTANGLE_VERTICAL_KUMMER_SCHATTEN4_DEFINED=true
ORTHOGONAL_RECTANGLE_VERTICAL_KUMMER_SCHATTEN4_PROVED=false
ONE_PRIME_VERTICAL_KUMMER_BESSEL_IMPLIES_SIGNED_RECTANGLE_TARGET=true
ONE_PRIME_VERTICAL_KUMMER_BESSEL_PROVED=false
DUAL_LARGE_SIEVE_FORMULATION_VALID=true
DUALITY_ALONE_CLOSES_TARGET=false
DUAL_GRAM_PRINCIPAL_COHERENCE_OBSTRUCTION_EXPLICIT=true
T59_RECTANGLE_ORTHOGONALITY_SOURCE_ENERGY_PROVED=true
T59_ASPECT_BALANCE_SOURCE_COMBINATION_PROVED=true
T59_GEOMETRY_ALONE_IMPLIES_VERTICAL_CANCELLATION=false
PING_XI_RECTANGLE_DIRECT_IMPORT_VALID=false
FKMS_RECTANGLE_DIRECT_IMPORT_VALID=false
ONE_PRIME_HORIZONTAL_BILINEAR_THEOREM_ITERATES_TO_SHARED_PQ=false
HORIZONTAL_C_R_OPERATOR_BOUND_TRANSFERS_TO_VERTICAL_A_R=false
OPERATOR_VALUED_FORMULATION_PROVED=true
OPERATOR_VALUED_LARGE_SIEVE_TARGET_PROVED=false
SIGNED_ORTHOGONAL_RECTANGLE_KUMMER_BILINEAR_LARGE_SIEVE_PROVED=false
SHARED_U_ENERGY_BALANCED_ORTHOGONAL_RECTANGLE_SECOND_MOMENT_PROVED=false
SHARED_U_CANONICAL_PRIME_DELTA_TOROIDAL_SECOND_MOMENT_PROVED=false
SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED=false
E4_COEFFICIENT_ENERGY_USED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
MINIMAL_REMAINING_OBSTRUCTION=OrthogonalRectangleVerticalKummerSchatten4
STRONGER_SUFFICIENT_THEOREM=OrthogonalRectangleOnePrimeKummerBessel
NEXT=Stage14-t62 attack the vertical Kummer Gram/Schatten-4 on the exact t59 rectangle family; separate diagonal, row/column, principal-transverse and nonprincipal-transverse pieces before any absolute Schur bound
```
