# Stage15-6-cycle — 6av through 6ay

Base: merged Stage15-6ar--6au (`PR #846`, merge commit `cb27d626`).

This cycle attempts the exact adapter demanded by the previous `NEW_GATE`. The audit stages are deliberately visible.

## Visible stage / audit ledger

```text
6av  explicit binary-quartic covering map
     AUDIT=PASS
     Hessian collapses to 12*kappa^2*k^2*Z^2
     X=d*(f^2+g^2)/(2*f*g)

6aw  non-torsion image
     AUDIT=PASS
     E_d(Q)_tors=(Z/2Z)^2
     only f=g=1 unit state maps to torsion
     all nonunit Stage15 states map to non-torsion points

6ax  direct Stage15 height -> Petit almost-minimal height
     AUDIT=BLOCK
     h_x <= log(2*d*k*Z^2)
     generic canonical-height comparison gives only polynomial control
     does not imply hat_h <= (1/8+alpha)log d, alpha<1/120

6ay  complete 2-descent image
     AUDIT=PASS
     X=U^2
     X-d=k*V_minus^2
     X+d=k*V_plus^2
     exact norm-core squareclass in both translated coordinates
```

## Main exact advance

The binary-quartic covering map is no longer an abstract existence statement. For a Stage15 one-state coordinate pair

\[
f+ig=Kz^2,
\qquad fg=\kappa T^2,
\qquad f^2+g^2=kZ^2,
\]

the image on

\[
E_d:Y^2=X^3-d^2X,
\qquad d=sf(2k\kappa),
\]

has

\[
\boxed{X=d\frac{f^2+g^2}{2fg}.}
\]

Writing

\[
\lambda=1\quad(k\kappa\text{ odd}),
\qquad
\lambda=2\quad(k\kappa\text{ even}),
\]

gives the exact complete-2-descent coordinates

\[
U=\frac{kZ}{\lambda T},
\quad
V_-=\frac{f-g}{\lambda T},
\quad
V_+=\frac{f+g}{\lambda T},
\]

with

\[
\boxed{X=U^2,\quad X-d=kV_-^2,\quad X+d=kV_+^2.}
\]

Thus the previously moving norm core `k` is exactly the squareclass of both translated x-coordinates in the standard rational 2-descent packet.

## Why the cycle stops here

Petit/Le Boudec small-height arguments obtain the sharp twist exponent after complete 2-descent and size restrictions on the descent variables. Stage15 has now identified the exact descent cell, but has not proved that `(U,V_-,V_+)` satisfy the required almost-minimal size boxes.

The next task is therefore not another broad theorem search and not another generic canonical-height comparison. It is the exact size audit

```text
Stage15 physical product height
+ low-core branch memory
+ exact U,V_minus,V_plus formulas
          |
          v
Petit/Le Boudec complete-2-descent small-height boxes ?
```

If this size implication fails, the Petit route is blocked as a whole-family causal mechanism and the surviving route returns to direct norm-core correlation.

## Frozen cycle exit

```text
STAGE15_6_CYCLE_START=6av
STAGE15_6_CYCLE_END=6ay
STAGE15_6_CYCLE_AUDIT_LEDGER=PASS,PASS,BLOCK,PASS
STAGE15_6_CYCLE_EXPLICIT_2COVERING_MAP=true
STAGE15_6_CYCLE_NONTORSION_IMAGE_PROVED=true
STAGE15_6_CYCLE_DIRECT_PETIT_HEIGHT_BRIDGE=false
STAGE15_6_CYCLE_COMPLETE_2DESCENT_IMAGE_EXACT=true
STAGE15_6_CYCLE_DESCENT_X_SQUARE=true
STAGE15_6_CYCLE_DESCENT_X_PLUS_MINUS_d_CORE=k
STAGE15_6_CYCLE_PETIT_SMALL_HEIGHT_SIZE_ADAPTER_PROVED=false
STAGE15_6_CYCLE_GLOBAL_NORM_CORE_AGGREGATION_PROVED=false
STAGE15_6_CYCLE_CAUSAL_HALF_POWER_REDERIVED=false
STAGE15_6_CYCLE_EXIT=COMPLETE_2DESCENT_SMALL_HEIGHT_SIZE_AUDIT_READY
```

Next: `Stage15-6az` should audit the exact descent-variable sizes against the small-height boxes used in the congruent-number twist literature. No new theorem species should be introduced before that audit.
