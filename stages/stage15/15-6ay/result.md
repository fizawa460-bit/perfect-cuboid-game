# Stage15-6ay — exact complete 2-descent squareclass image

Base: Stage15-6ax blocked the direct generic canonical-height implication and pointed to the complete 2-descent coordinates used in congruent-number height arguments. Stage15-6av already gives the exact image

\[
X=d\frac{f^2+g^2}{2fg}
\]

on `E_d:Y^2=X^3-d^2X`.

This substage computes the three rational 2-descent squareclasses of the Stage15 image explicitly.

Audit verdict: `PASS`.

## 1. The two translated x-coordinates factor as squares

From the explicit covering coordinate,

\[
\boxed{
X-d=d\frac{(f-g)^2}{2fg},
}
\]

and

\[
\boxed{
X+d=d\frac{(f+g)^2}{2fg}.
}
\]

Also

\[
f^2+g^2=kZ^2,
\qquad fg=\kappa T^2.
\]

Put `s=k*kappa`, which is squarefree, and define

\[
\lambda=\begin{cases}
1,&s\text{ odd},\\
2,&s\text{ even}.
\end{cases}
\]

Since

\[
d=\begin{cases}
2k\kappa,&s\text{ odd},\\
k\kappa/2,&s\text{ even},
\end{cases}
\]

the three identities simplify simultaneously to

\[
\boxed{
X=U^2,
\qquad
X-d=kV_-^2,
\qquad
X+d=kV_+^2,
}
\]

where

\[
\boxed{
U=\frac{kZ}{\lambda T},
\qquad
V_- =\frac{f-g}{\lambda T},
\qquad
V_+=\frac{f+g}{\lambda T}.
}
\]

All three are rational numbers attached functorially to the Stage15 state.

## 2. Exact 2-descent squareclasses

Thus in `Q*/Q*^2`,

\[
\boxed{[X]=1,\qquad[X-d]=[k],\qquad[X+d]=[k].}
\]

This is the complete rational 2-descent label of the Stage15 image relative to the rational 2-torsion roots `0,d,-d`.

The norm core `k` is therefore not merely an external label of the quartic. It is exactly the nontrivial squareclass carried by **both translated x-coordinates** of the image point.

This identity does not recharge `k` as a congruence modulus. It is a reconstruction statement in the 2-descent coordinates.

## 3. Pell-type form

The same identities may be written

\[
\boxed{U^2-kV_-^2=d,}
\]

\[
\boxed{U^2-kV_+^2=-d.}
\]

Subtracting gives

\[
\boxed{k(V_+^2-V_-^2)=2d.}
\]

These are not new independent equations; they are the exact complete-2-descent presentation of the Stage15 covering point.

## 4. Relation to the Stage15 four-cell decomposition

Stage15-6al previously split the coordinate-product core into four pairwise-coprime cells

\[
\kappa_{xp},\kappa_{xq},\kappa_{yp},\kappa_{yq}
\]

and square variables. The present identities show that after passing through the explicit covering map, the remaining norm core `k` lands in the standard 2-descent squareclasses `X+-d`, while the twist packet satisfies `d=sf(2k*kappa)`.

Thus the connection to complete 2-descent is now exact at the squareclass level rather than a structural analogy.

## 5. What is still missing for Petit

Congruent-number small-height arguments use complete 2-descent **together with size restrictions** on the squarefree and square variables. Stage15-6ay has identified the correct descent cell, but it has not proved that

\[
U,V_-,V_+
\]

lie in the almost-minimal height boxes required by Petit's theorem.

Accordingly:

```text
PETIT_COMPLETE_2DESCENT_CELL_IDENTIFIED=true
PETIT_SMALL_HEIGHT_SIZE_ADAPTER_PROVED=false
```

This is the next narrow gate. Broad theorem search remains unnecessary.

## 6. Audit verdict

```text
AUDIT_STAGE=Stage15-6ay
AUDIT_TARGET=EXACT_COMPLETE_2DESCENT_SQUARECLASS_DICTIONARY
AUDIT_VERDICT=PASS
X_IS_RATIONAL_SQUARE=true
X_MINUS_d_SQUARECLASS=k
X_PLUS_d_SQUARECLASS=k
DESCENT_U=k*Z/(lambda*T)
DESCENT_V_MINUS=(f-g)/(lambda*T)
DESCENT_V_PLUS=(f+g)/(lambda*T)
NORM_CORE_RECHARGED=false
PETIT_DESCENT_CELL_IDENTIFIED=true
PETIT_SMALL_HEIGHT_SIZE_ADAPTER_PROVED=false
```

## 7. Frozen exit

```text
STAGE15_6_SUBSTAGE=6ay
STAGE15_6AY_AUDIT=true
STAGE15_6AY_AUDIT_VERDICT=PASS
STAGE15_6AY_COMPLETE_2DESCENT_IMAGE_EXACT=true
STAGE15_6AY_X_SQUARE=true
STAGE15_6AY_X_PLUS_MINUS_d_CORE=k
STAGE15_6AY_PETIT_DESCENT_CELL_IDENTIFIED=true
STAGE15_6AY_PETIT_SMALL_HEIGHT_SIZE_ADAPTER_PROVED=false
STAGE15_6AY_EXIT=COMPLETE_2DESCENT_SIZE_AUDIT_READY
```

Next: audit the exact sizes of `(U,V_-,V_+)` against the almost-minimal-height descent boxes. If that fails, the Petit route is blocked as a whole-family mechanism and the remaining route returns to direct norm-core correlation.
