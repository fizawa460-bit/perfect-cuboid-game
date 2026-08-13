# Stage15-6cq — dyadic physical root-line boundary audit

Base: merged Stage15-6cp with fresh audit PASS. Main-batch work unit 1.

For fixed channel moduli `(d,e)` write `q=de`. After fixing the legal S/O orientations and passing to one dyadic box
\[
m\asymp M,\ n\asymp N,\ r\asymp R_0,\ s\asymp S_0,
\]
the two torus coordinate pairs each lie on one primitive residue line modulo `q`. The elementary joint lattice count therefore has the exact shape
\[
\#_{q,\mathrm{box}}
\ll
\left(1+\frac{MN}{q}\right)
\left(1+\frac{R_0S_0}{q}\right),
\]
hence
\[
\#_{q,\mathrm{box}}
\ll
1+\frac{MN}{q}+\frac{R_0S_0}{q}
+\frac{MNR_0S_0}{q^2}.
\]
The last term is the desired codimension-two main density. The obstruction to a genuine `delta>0` is now localized to the two one-sided fringe moments
\[
\sum_{\mathrm{physical\ boxes}} MN,
\qquad
\sum_{\mathrm{physical\ boxes}} R_0S_0,
\]
plus the corner count.

If one had the physical boundary estimate
\[
\sum_{\mathrm{boxes}}(MN+R_0S_0+1)
\ll B^{1-\delta+o(1)}
\]
for some fixed `delta>0`, then the per-modulus profile would improve to
\[
N_{d,e}(B)
\ll B^{1+o(1)}q^{-2}+B^{1-\delta+o(1)}q^{-1},
\]
so the 6cp ledger would have `beta=-1` and polynomial window condition simply `theta<delta`.

Current certified physical inverse bounds are too weak to prove this fringe moment: the moving primitive gcd normalizer permits strongly unbalanced toric boxes, and summing only `MN` or only `R_0S_0` loses the exact product-height control. Thus no `delta>0` is claimed.

This is still a strict narrowing: the small-side theorem species is no longer an arbitrary softer toric error. It is the physical first moment of the **one-sided dyadic fringe areas**.

```text
STAGE15_6_SUBSTAGE=6cq
STAGE15_6CQ_DYADIC_JOINT_LATTICE_EXPANSION=true
STAGE15_6CQ_MAIN_LOCAL_DENSITY=q^-2
STAGE15_6CQ_FRINGE_TERMS=MN/q+R0S0/q+1
STAGE15_6CQ_CONDITIONAL_BETA=-1
STAGE15_6CQ_DELTA_PROVED=false
STAGE15_6CQ_SMALL_GATE=PHYSICAL_ONE_SIDED_FRINGE_MOMENT
STAGE15_6CQ_EXIT=PRIMITIVE_RECIPROCAL_NORMALIZER_AUDIT_READY
```