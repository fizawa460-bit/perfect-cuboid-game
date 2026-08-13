# Stage14-4au — full local indicator expansion and reciprocal off-diagonal obstruction

## Result

Stage14-4at identified the first quantitative gap in the main line:

```text
centered prime-level second moment
        -> nonnegative full local 2-descent indicator
        -> explicit rho_loc / E_loc.
```

Stage14-4au closes the **logical** part of this conversion and isolates the remaining analytic obstruction. It does not claim the missing bilinear estimate.

For primitive opposite-parity Euclid parameters write

\[
F_1=m,\quad F_2=n,\quad F_3=m-n,\quad F_4=m+n,\quad F_5=m^2+n^2,
\]

and let

\[
P_F=\operatorname{rad}_{\rm odd}(F_1F_2F_3F_4F_5).
\]

The five factors have pairwise disjoint odd-prime support. A nontrivial full-2-descent state `xi` chooses an odd support subset; its label is already forced columnwise by s5c,

```text
m,n                 -> 13
m-n,m+n             -> 12
m^2+n^2             -> 23,
```

and its prime-2 squareclass state lies in the exact eight-state image from s5f.

Let `L_F(xi)` be the indicator that this fixed descent state passes every local row. Define

\[
N_{\rm loc}(F)=\sum_{\xi\ne0}L_F(\xi).
\]

Then the actual base indicator is exactly

\[
s(F)=1_{N_{\rm loc}(F)\ge1},
\]

so in particular

\[
\boxed{s(F)\le N_{\rm loc}(F).}
\]

Thus the existence condition can be replaced by a **nonnegative support count** for an upper bound. No signed centered trace is used at this step.

## Support multiplicity is not a power-scale obstruction

For fixed `F`, before local rows are imposed there are at most

\[
8\,2^{\omega(P_F)}
\]

odd-support / `Q_2` states. In a dyadic box inside `m^2+n^2<=B`,

\[
F_1F_2F_3F_4F_5\ll B^3,
\]

hence the standard divisor bound gives

\[
2^{\omega(P_F)}\le \tau(P_F)=B^{o(1)}.
\]

Therefore replacing one-base existence by the support sum costs at most a subpower factor. It may affect logarithms and constants, but it is not the missing fixed power of `B`.

## Exact Boolean-to-character expansion

Every odd row from s5c/s5d is an exact Boolean polynomial in quadratic-character bits.

For example a condition `chi_p(D)=+1` is

\[
\frac{1+\chi_p(D)}2,
\]

while a supported row with two required signs is the product of two such factors. For an unselected `X`-prime the row is automatic at `p=3 mod 4`, and at `p=1 mod 4` is again one affine character factor. The exact `Q_2` state contributes only a finite `0/1` coefficient.

For a fixed support state `xi`, expanding all odd rows therefore gives a finite Fourier expansion

\[
L_F(\xi)=1_{Q_2(\xi,F)}
\sum_{\omega}c_{\xi,\omega}\,\mathcal X_{\xi,\omega}(F),
\qquad |c_{\xi,\omega}|\le1.
\]

The unit part `d_j` appearing in a row at a prime `p` is itself a product of selected squarefree pieces from the other Euclid-factor columns. Consequently, after collecting prime-by-prime Legendre symbols, every nonconstant `mathcal X` is a product of off-diagonal Jacobi symbols

\[
\left(\frac{u_i}{u_j}\right),\qquad i\ne j,
\]

plus the already explicit mod-4 sign bits. This is exactly the reciprocity matrix of s5b.

The constant Fourier mode is the diagonal/main part. Every nonconstant mode is a reciprocal off-diagonal term.

## Dyadic nonnegative conversion

Fix a dyadic Euclid box `m~M, n~N` and a permitted nonnegative weight `W(F)`. Since `s(F)<=N_loc(F)`,

\[
S_W:=\sum_F W(F)s(F)
\le \sum_F W(F)N_{\rm loc}(F).
\]

Expanding the support states and their Boolean rows gives

\[
\sum_F W(F)N_{\rm loc}(F)
= D_{\rm loc}(M,N)+\sum_{\omega\ne0}\mathcal B_\omega(M,N),
\]

where `D_loc` is the total constant-mode contribution. Hence the rigorous upper-bound interface is

\[
\boxed{
S_W\le D_{\rm loc}(M,N)
+\sum_{\omega\ne0}|\mathcal B_\omega(M,N)|.}
\]

Accordingly, any uniform estimates

\[
D_{\rm loc}\le \rho_{\rm diag}A_W+E_{\rm diag},
\qquad
\sum_{\omega\ne0}|\mathcal B_\omega|\le E_{\rm rec}
\]

immediately instantiate the 4as local input with

\[
\rho_{\rm loc}=\rho_{\rm diag},\qquad
E_{\rm loc}=E_{\rm diag}+E_{\rm rec}.
\]

This is a deterministic implication; no independence hypothesis is introduced.

## The precise reciprocal obstruction

After dyadically decomposing selected squarefree pieces, a representative nonconstant block has the form

\[
\mathcal B_{ij}(U,V;M,N)
=\sum_{\substack{m\asymp M\\n\asymp N}}
 w_{m,n}
 \sum_{\substack{u\mid \operatorname{rad}_{\rm odd}(F_i(m,n))\\u\asymp U}}
 \sum_{\substack{v\mid \operatorname{rad}_{\rm odd}(F_j(m,n))\\v\asymp V}}
 a_{u;m,n}\,b_{v;m,n}
 \left(\frac{u}{v}\right),
\qquad i\ne j.
\]

The coefficients include the complementary divisor pieces, the remaining local rows, and the finite `Q_2` state. They are therefore **not free independent coefficient sequences** in `u` and `v`: both divisor variables are tied to the same polynomial tuple

```text
m, n, m-n, m+n, m^2+n^2.
```

This is the obstruction that the prime-level s5g second moment does not resolve. s5g controls centered traces `chi_p(P_e(m,n))-beta_{p,e}` with one external prime `p`; the full indicator expansion contains products of moving Jacobi symbols between divisor pieces of two or more moving columns.

Thus the missing analytic statement is now sharply localized: one needs a uniform reciprocal-divisor bilinear estimate, after hyperbola/dyadic decomposition, strong enough to bound the total nonconstant-mode mass by an explicit `E_rec` (and separately evaluate the diagonal mass).

A sufficient power-saving target for a nonconstant block is schematically

\[
\mathcal B_{ij}(U,V;M,N)
\ll (MN)^{1-\eta_{\rm rec}+o(1)}
\]

uniformly over the ranges that survive the divisor decomposition, for some fixed `eta_rec>0`, with summable losses over the `B^{o(1)}` state/mode family. This is a target, not a proved estimate.

## Relation to the 14-4at Q-budget

The 14-4at benchmark

\[
Q_*(B)=B^{1/4-\eta}
\]

remains the safe depth for the **candidate prime-level** second moment `(MN+Q^4)` on bulk boxes. Stage14-4au confirms that `Q^4` still cannot be identified with `E_loc`: the conversion from prime-level centered traces to the reciprocal-divisor expansion above is exactly where the new bilinear input is needed.

Therefore the first quantitative gap is narrowed from the broad phrase `FULL_LOCAL_INDICATOR_CONVERSION` to the explicit object

```text
RECIPROCAL_DIVISOR_OFF_DIAGONAL_BILINEAR_BOUND.
```

The existence-to-support-count step and Boolean-to-character expansion are no longer the conceptual obstruction.

## Boundary

```text
STAGE14_4AU=FULL_LOCAL_INDICATOR_EXPANDED_AND_RECIPROCAL_OFF_DIAGONAL_OBSTRUCTION_ISOLATED
BASE_EXISTENCE_TO_NONNEGATIVE_SUPPORT_COUNT=true
SUPPORT_MULTIPLICITY_B_TO_O1=true
ALL_ODD_ROWS_BOOLEAN_CHARACTER_POLYNOMIALS=true
FULL_FIXED_SUPPORT_FOURIER_EXPANSION_FORMULATED=true
CONSTANT_MODE_VS_RECIPROCAL_OFF_DIAGONAL_SPLIT=true
LOCAL_RHO_E_TRANSFER_FROM_DIAGONAL_AND_RECIPROCAL_BOUNDS=true
S5G_PRIME_LEVEL_SECOND_MOMENT_CONTROLS_FULL_INDICATOR=false
RECIPROCAL_DIVISOR_BILINEAR_BOUND_PROVED=false
EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED=false
EXPLICIT_E_LOC_PROVED=false
POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false
POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

No quadratic-large-sieve theorem is imported through a coefficient factorization that has not been justified. No reciprocal off-diagonal power saving, nontrivial local retainer, or `sqrt(B)` law is claimed.

```text
NEXT=Stage14-4av dyadically factor the reciprocal-divisor blocks into quadratic-character bilinear forms with controlled correlated coefficients, then prove a first uniform block estimate or identify the remaining coefficient-correlation obstruction
```
