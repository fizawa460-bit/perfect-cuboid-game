# Stage15-6-cycle — 6bd through 6bg

Base: merged Stage15-6az--6bc (`PR #850`, merge commit `9f0e284b`).

This cycle starts from the weighted same-twist / same-2-descent-cell second-moment gate and first checks whether that gate is actually minimal.

## Visible audit ledger

```text
6bd  eliminate explicit global norm-core sum                 PASS
6be  fixed physical-diagonal fiber multiplicity              PASS
6bf  exact rational denominator rigidity                     PASS
6bg  integral-point second-moment audit / support receiver   NEW_GATE
```

The internal literature verdict inside 6bg is `DIRECT_REUSE_BLOCKED`; the stage-level verdict is `NEW_GATE` because a smaller exact receiver is identified.

## 6bd — global k sum disappears

For one state,

\[
F=\kappa_f^2c^4+\kappa_g^2e^4=kZ^2,
\]

so `k=sf(F)` is reconstructed. For two states,

\[
\boxed{F_1F_2=S^2}
\]

is exactly the common norm-core condition, with

\[
\boxed{S=kZW=\frac{\gamma}{2}R\le2B.}
\]

Thus the polynomial outer sum over `k` was an artifact of a conditioned disintegration.

## 6be — fixed S fiber is B^o(1)

Fix `S`. Then `F_1|S^2`, `F_2=S^2/F_1`, so there are only `tau(S^2)=B^o(1)` value pairs.

For each `F`,

\[
f^2+g^2=F
\]

has at most `r_2(F)<=4*tau(F)=B^o(1)` integral representations. The coordinate squareclass split is unique, Gaussian core decorations are subpolynomial, and Stage15-6ak reconstructs the toric pairs uniquely.

Hence

\[
\boxed{\#\{\text{physical survivors above fixed }S\}=B^{o(1)}.}
\]

## 6bf — Stage15 points are genuinely rational

With

\[
f=\kappa_fc^2,\qquad g=\kappa_ge^2,
\]

primitivity gives `(c,e)=1`, and every odd prime dividing `ce` is coprime to `kZ`. For the explicit descent coordinate

\[
U=\frac{kZ}{\lambda ce},
\]

the reduced denominator is exactly

\[
\boxed{ce\quad(2\nmid\kappa),\qquad 2ce\quad(2\mid\kappa).}
\]

Thus generic Stage15 points are not integral points on the minimal congruent-number twist model.

## 6bg — external second moments are not the minimal theorem

Targeted primary-source audit:

- Chan, arXiv:2004.03331: integral points on the congruent-number curve and integer simultaneous-Pell applications;
- Choi, arXiv:2509.03274: integral points on general quadratic twist families and bounded average integral-point count;
- Alpöge–Ho, arXiv:1807.03761: bounded moments for `S`-integral points over all short Weierstrass curves / positive-density subfamilies with fixed finite `S`.

They do not directly count the Stage15 host with moving rational denominators. More importantly, 6be has already made a point-count second moment unnecessary at fixed physical diagonal.

Define the admissible support

\[
\mathcal S(B)=\{S\le2B:\text{the exact Stage15 product-square receiver has a physical point}\}.
\]

Then

\[
N_2(B)\ll |\mathcal S(B)|B^{o(1)}.
\]

For fixed coordinate-cell allocations the exact support receiver is

\[
\boxed{
Y^2=
(\kappa_{f,1}^2c_1^4+\kappa_{g,1}^2e_1^4)
(\kappa_{f,2}^2c_2^4+\kappa_{g,2}^2e_2^4),
\qquad Y=S\le2B.
}
\]

This is the new Kummer-type `(4,4)` product-square support problem under **Y-height**, not ordinary projective box height.

## Frozen cycle exit

```text
STAGE15_6_CYCLE_START=6bd
STAGE15_6_CYCLE_END=6bg
STAGE15_6_CYCLE_AUDIT_LEDGER=PASS,PASS,PASS,NEW_GATE
STAGE15_6_CYCLE_EXPLICIT_SUM_OVER_k_ELIMINATED=true
STAGE15_6_CYCLE_FIXED_S_PHYSICAL_FIBER=B^o(1)
STAGE15_6_CYCLE_GENERIC_TWIST_POINT_HAS_MOVING_DENOMINATOR=true
STAGE15_6_CYCLE_INTEGRAL_POINT_SECOND_MOMENT_DIRECT_REUSE=false
STAGE15_6_CYCLE_WEIGHTED_TWIST_SECOND_MOMENT_GATE_SUPERSEDED=true
STAGE15_6_CYCLE_NEW_SUPPORT_VARIABLE=S=k*Z*W=(gamma/2)*R
STAGE15_6_CYCLE_SUPPORT_RECEIVER=Y^2=F1*F2;Y<=2B
STAGE15_6_CYCLE_TARGET_SUPPORT_EXPONENT=1/2
STAGE15_6_CYCLE_SUPPORT_BOUND_PROVED=false
STAGE15_6_CYCLE_CAUSAL_HALF_POWER_REDERIVED=false
STAGE15_6_CYCLE_EXIT=ADMISSIBLE_DIAGONAL_KUMMER_SUPPORT_THEOREM_GATE
```

Next: audit the exact `(4,4)` product-square/Kummer-type support receiver under `Y<=2B`. Do not restart the old `sum_k`, Petit-small-height, or integral-point-second-moment routes without a new exact adapter.
