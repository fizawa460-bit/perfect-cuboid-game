# Stage15-6ax — canonical-height bridge audit for the Petit gate

Base: Stage15-6av gives the explicit non-torsion image on

\[
E_d:Y^2=X^3-d^2X,
\qquad
X=d\frac{f^2+g^2}{2fg},
\]

and Stage15-6aw removes the finite torsion-image branch. This substage addresses Gate C from Stage15-6au: does the existing Stage15 physical/product height force the image to satisfy Petit's almost-minimal canonical-height condition?

Audit verdict: `BLOCK` for the **direct height implication**. This is not a theorem that the Petit route can never work; it says the current height bridge is quantitatively too weak.

## 1. Exact naive height from the covering map

Put

\[
S=f^2+g^2=kZ^2,
\qquad P=fg=\kappa T^2.
\]

Then

\[
X=\frac{dS}{2P}.
\]

Before rational cancellation, both numerator and denominator are bounded by

\[
\max(dS,2P)\le 2dkZ^2
\]

for `d>=1`. Hence the logarithmic Weil x-height satisfies

\[
\boxed{h_x(P)\le \log(2dkZ^2).}
\]

Any standard comparison between naive and canonical height on the twist family therefore gives only a bound of the shape

\[
\boxed{\hat h_{E_d}(P)=O(\log(dkZ^2)),}
\]

with an absolute/twist-coefficient contribution of order `log d`.

This is a useful polynomial height control, but it is not the exponent needed by Petit.

## 2. Petit's required scale is much sharper

The targeted theorem counts twists whose lowest non-torsion point satisfies

\[
\eta_d\le d^{1/8+\alpha},
\qquad 0<\alpha<1/120,
\]

where

\[
\log\eta_d=\min_{Q\notin E_d(\mathbf Q)_{tors}}\hat h_{E_d}(Q).
\]

To enter that family using the Stage15 image one would need an implication

\[
\boxed{
\hat h_{E_d}(P)
\le(1/8+\alpha)\log d
}
\]

for some fixed `alpha<1/120`, apart from an absorbable absolute constant.

The bound from Section 1 contains the independent factor `kZ^2`. The exact physical product height

\[
kZW\le2B
\]

controls `Z` only relative to the other Gaussian state `W`; it does not turn `kZ^2` into `d^{1/4+o(1)}` uniformly.

Likewise the small-coordinate-core condition

\[
\kappa^2<ZW
\]

and the remembered 6ac low-core inequality do not supply the missing one-state relation between `Z` and `d`.

Therefore the implication required by Petit is not derivable from the current Stage15 size ledger.

## 3. This is exactly where complete 2-descent enters the literature

The relevant congruent-number height arguments do not obtain the sharp exponent from a generic projective-height comparison. They pass to a complete 2-descent parametrization and impose simultaneous bounds on four squarefree/square factors.

Stage15 already has a four-cell decomposition from 6al, so this failure points to a much more specific next adapter rather than to another generic canonical-height estimate.

## 4. Formal scale countermodel to the current implication

The insufficiency can be seen already at the level of the certified inequalities. They allow blocks with

```text
d = O(1),
k = O(1),
kappa = O(1),
Z growing polynomially with B,
W chosen so kZW <= 2B.
```

On such a block the certified x-height bound grows like `log Z`, while the Petit threshold `(1/8+alpha) log d` is bounded.

This is a countermodel to the **size-inequality implication**, not an assertion that every such formal block contains a physical Stage15 point.

## 5. Audit verdict

```text
AUDIT_STAGE=Stage15-6ax
AUDIT_TARGET=DIRECT_STAGE15_HEIGHT_TO_PETIT_SMALL_HEIGHT
AUDIT_VERDICT=BLOCK
EXPLICIT_COVERING_HEIGHT_AVAILABLE=true
NAIVE_X_HEIGHT_BOUND=log(2*d*k*Z^2)
CANONICAL_HEIGHT_POLYNOMIAL_CONTROL=true
PETIT_REQUIRED_COEFFICIENT=1/8+alpha_with_alpha<1/120
DIRECT_PETIT_SMALL_HEIGHT_IMPLICATION=false
PETIT_THEOREM_APPLIED=false
COMPLETE_2DESCENT_ADAPTER_SUGGESTED=true
```

AR-027 remains active: a twist-family theorem cannot replace the weighted Stage15 packet until this height condition is proved on the actual population.

## 6. Frozen exit

```text
STAGE15_6_SUBSTAGE=6ax
STAGE15_6AX_AUDIT=true
STAGE15_6AX_AUDIT_VERDICT=BLOCK
STAGE15_6AX_DIRECT_CANONICAL_HEIGHT_BRIDGE=false
STAGE15_6AX_GENERIC_PROJECTIVE_HEIGHT_TOO_WEAK=true
STAGE15_6AX_COMPLETE_2DESCENT_ROUTE_INDICATED=true
STAGE15_6AX_EXIT=DIRECT_PETIT_IMAGE_ROUTE_BLOCKED_DESCENT_CELL_DICTIONARY_READY
```

Next: Stage15-6ay audits whether the four Stage15 coordinate squareclass cells from 6al can be matched to the four-factor complete 2-descent receiver used in congruent-number small-height counting. No new broad theorem search is needed.
