# Stage15-6bu — universal-torsor elementary lattice audit

Audit verdict: BLOCK.

The raw Pythagorean parametrization satisfies

\[
R_{raw}^2=4(m^2r^2+n^2s^2)(m^2s^2+n^2r^2).
\]

For fixed actual core q the two root lines indeed define an index-q^2 lattice in `(m,n,r,s)`. However the physical primitive height is obtained only after a moving gcd normalizer. Stage15-6aj removes that normalizer by passing to the Gaussian square variables `(k,z,w)`, where the q-lattice density is no longer a free independent box factor.

Therefore summing an index-q^2 box count against `R_raw` would count the wrong measure. No elementary universal-torsor `B/Q` estimate is certified here.

```text
STAGE15_6_SUBSTAGE=6bu
STAGE15_6BU_AUDIT_VERDICT=BLOCK
STAGE15_6BU_RAW_HEIGHT_FACTORIZATION=true
STAGE15_6BU_JOINT_LATTICE_INDEX=q^2
STAGE15_6BU_MOVING_GCD_NORMALIZER_OBSTRUCTION=true
STAGE15_6BU_ELEMENTARY_B_OVER_Q_PROVED=false
STAGE15_6BU_EXIT=STAGE14_DISPERSION_CROSS_PROMOTION_AUDIT_READY
```
