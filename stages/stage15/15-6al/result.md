# Stage15-6al — four-cell decomposition of the global coordinate-product squareclass

Base: Stage15-6ak in the same cycle. Stage15-6ak replaced the moving outer-curve sum by the global primitive Gaussian-square receiver

\[
\alpha_0=x+i y=K_\alpha z^2,
\qquad
\beta_0=p+i q=K_\beta w^2,
\]

with toric compatibility exactly

\[
\boxed{xypq\in\mathbf Z^2.}
\]

Stage15-6al decomposes this square condition primewise and identifies the next legal spacing modulus. No global saving is claimed yet.

## 1. Common coordinate-product squareclass

Because `(x,y)` and `(p,q)` are primitive pairs,

\[
\gcd(x,y)=\gcd(p,q)=1.
\]

The product-square condition is equivalent to

\[
\boxed{
\operatorname{sf}(xy)=\operatorname{sf}(pq)=:\kappa.
}
\]

Thus a second squarefree object appears naturally:

- `k` is the common **Gaussian norm core** from Stage15-4;
- `kappa` is the common **coordinate-product core**.

These are distinct arithmetic objects.

## 2. Exact four-cell split

Let

\[
s_x=\operatorname{sf}(x),\quad s_y=\operatorname{sf}(y),
\quad s_p=\operatorname{sf}(p),\quad s_q=\operatorname{sf}(q).
\]

Primitivity gives

\[
(s_x,s_y)=(s_p,s_q)=1.
\]

Define the four squarefree cells

\[
\kappa_{xp}=(s_x,s_p),\quad
\kappa_{xq}=(s_x,s_q),\quad
\kappa_{yp}=(s_y,s_p),\quad
\kappa_{yq}=(s_y,s_q).
\]

Every prime of the common squareclass occurs in exactly one cell, so the cells are pairwise coprime and

\[
\boxed{
\kappa=\kappa_{xp}\kappa_{xq}\kappa_{yp}\kappa_{yq}.
}
\]

Moreover there are positive integers `X,Y,P,Q` with

\[
\boxed{
\begin{aligned}
x&=\kappa_{xp}\kappa_{xq}X^2,\\
y&=\kappa_{yp}\kappa_{yq}Y^2,\\
p&=\kappa_{xp}\kappa_{yp}P^2,\\
q&=\kappa_{xq}\kappa_{yq}Q^2.
\end{aligned}}
\]

This decomposition is unique.

The two useful aggregates are

\[
\kappa_{\rm agree}=\kappa_{xp}\kappa_{yq},
\qquad
\kappa_{\rm switch}=\kappa_{xq}\kappa_{yp},
\]

with

\[
\kappa_{\rm agree}\kappa_{\rm switch}=\kappa.
\]

## 3. Toric ratios in the four-cell coordinates

Substituting the cell decomposition into the 6ak reverse map gives

\[
\frac mn
=
\frac{\kappa_{xp}XP}{\kappa_{yq}YQ},
\qquad
\frac rs
=
\frac{\kappa_{xq}XQ}{\kappa_{yp}YP},
\]

followed only by reduction to lowest terms.

Thus the four cells are not decorative. They encode exactly which squarefree support enters the numerator/denominator of each reconstructed toric ratio.

## 4. The norm core k and coordinate core kappa are coprime

Since

\[
x^2+y^2=kN(z)^2
\]

and `(x,y)=1`, no prime dividing `k` can divide `x` or `y`: if `\ell|k` and `\ell|x`, then the norm equation forces `\ell|y`, contradicting primitivity. The same holds for `(p,q)`.

At `2`, if `2|k`, primitive sum-of-two-squares parity forces both coordinates odd, so `2` still does not enter `kappa`.

Therefore

\[
\boxed{(k,\kappa)=1.}
\]

This is critical proof accounting. `kappa` is not a renamed piece of the already-charged Stage15 norm core and may be used as genuinely new arithmetic information without violating AR-028.

```text
STAGE15_6AL_NORM_CORE_COORDINATE_CORE_COPRIME=true
```

## 5. Coordinate cells give genuine quadratic root lines

Fix `K_alpha=A+iB`. Then

\[
x=A(a^2-b^2)-2Bab,
\]

\[
y=B(a^2-b^2)+2Aab.
\]

For any odd prime `\ell|\kappa` assigned to either `x` or `y`, we have `\ell\nmid k` by the previous section. The corresponding binary quadratic form has discriminant

\[
4(A^2+B^2)=4k,
\]

which is a unit modulo `\ell`. Since the actual point supplies a root, the form splits into at most two primitive projective root lines modulo `\ell`.

Primewise cell allocation followed by CRT therefore compresses the **odd part** `\kappa^\circ` to one of

\[
2^{O(\omega(\kappa))}=B^{o(1)}
\]

primitive root lines for the pair `(a,b)` modulo `\kappa^\circ`.

Exactly the same statement holds for `(u,v)` through `K_beta`.

The 2-primary part of `kappa` costs only an absolute constant and is not used as a spacing modulus.

Thus `kappa` is a legal new Stage15 root-line modulus, unlike the private/recharged moduli forbidden earlier in 6ae.

```text
STAGE15_6AL_COORDINATE_CORE_ROOTLINE_ADAPTER=true
STAGE15_6AL_COORDINATE_CORE_IS_NEW_NOT_RECHARGED=true
```

## 6. Why this does not yet prove a saving

For a dyadic Gaussian box with norm scale `N(w)~W`, a fixed odd `kappa` root-line gives the familiar bound

\[
\#w\ll B^{o(1)}\left(1+\frac{W}{\kappa^\circ}\right).
\]

But 6al has not shown that `kappa` is large on most survivors. Small `kappa`, including `kappa=1`, is still possible a priori.

The correct next split is therefore not another pair-overlap split. It is a **one-point coordinate-core size split**:

```text
large kappa  -> genuine root-line spacing
small kappa  -> coordinate-product squareclass density problem
```

## 7. Arsenal relation

The four-cell pattern is structurally close to the Stage14 squareclass orientation mechanisms, but no Stage14 exponent is imported.

```text
AR-009=EXACT_STAGE15_COORDINATE_CORE_ROOTLINE_ADAPTER
AR-016=FINITE_CELL/ORIENTATION_MULTIPLICITY_ONLY
AR-018=STRUCTURAL_ANALOGY_ONLY; STAGE15_CELLS_PROVED_DIRECTLY
AR-023/024=GLOBAL_MEASURE_PRESERVED_BY_6AK_RECONSTRUCTION
AR-028=PASS_BECAUSE_gcd(k,kappa)=1
```

Targeted Stage14-s7-48 remains related but not identical: that stage counted one Gaussian norm together with the rotated-coordinate product of the same Gaussian integer under a balanced Stage14 packet measure. Stage15-6al has two primitive Gaussian core-squares and an exact common coordinate-product squareclass under the product height `kN(z)N(w)<=2B`.

## 8. Frozen exit

```text
STAGE15_6_SUBSTAGE=6al
STAGE15_6AL_STARTING_GATE=DECOMPOSE_GLOBAL_COORDINATE_PRODUCT_SQUARECLASS
STAGE15_6AL_COMMON_COORDINATE_CORE_DEFINED=true
STAGE15_6AL_COORDINATE_CORE=kappa=sf(x*y)=sf(p*q)
STAGE15_6AL_FOUR_CELLS_PAIRWISE_COPRIME=true
STAGE15_6AL_FOUR_CELL_RECONSTRUCTION=true
STAGE15_6AL_NORM_CORE_COORDINATE_CORE_COPRIME=true
STAGE15_6AL_COORDINATE_CORE_ROOTLINE_ADAPTER=true
STAGE15_6AL_COORDINATE_CORE_IS_NEW_NOT_RECHARGED=true
STAGE15_6AL_COORDINATE_CORE_LARGE_BRANCH_COUNT_PROVED=false
STAGE15_6AL_LOW_CORE_GLOBAL_COUNT_PROVED=false
STAGE15_6AL_EXIT=COORDINATE_CORE_SIZE_DICHOTOMY_READY
```

Stage15-6al stops before choosing the large/small threshold.