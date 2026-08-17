# Stage27-20-r301z — fixed-width wall-slab receiver is the exact remaining upper gate

STATUS=AUDITED_PASS_MERGED
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_RECEIVER_SYNTHESIS
PARENT_ROUTE=Stage27-20-r301w-y
SOURCE_STAGE=Stage20
AUDIT_PR=1062
AUDIT_COMMIT=60edf5a7cb02cbfc1905fd61874a8f1e716d43f0
MERGE_COMMIT=96e99d8e4232ad06da748ad4e37b8c43f16e944b

## 1. What the audited r301 package already proves

R301s gives exponent equivalence between the Stage27 population and occupied first-coordinate support:

\[
|Q(B)|\le N_2(B)\le |Q(B)|B^{o(1)}.
\]

R301t embeds occupied `q1` support into the Stage14 active-face packet decomposition with only `B^{o(1)}` packet/decorative multiplicity. R301u then proves, for every fixed `eta>0`,

\[
|Q_{\rm off,eta}(B)|
\ll B^{1/2-\min(2\eta,1/16)+o(1)}.
\]

The proportional branch is already bounded by `B^(7/16+o(1))`. R301v identifies the only nonproportional saturation segment of the available complete-host package as

\[
\theta=\frac14,
\qquad \frac18\le\phi\le\frac14,
\qquad \chi=2\phi-\frac14.
\]

R301w-y then audits and closes three circular/internal-looking ways to attack this segment: reusing the already charged local-root ledger, using the injective `q1 -> q0` collision energy, and using the exponent-neutral `q0` or `j` projections.

## 2. Replace the vague shrinking-neighborhood issue by one fixed slab

Fix a constant `eta_0>0`. Let `P_wall,eta0(B)` be the set of **nonproportional occupied Stage14 packet-face incidences** arising from the r301t injection and satisfying

\[
|\theta-1/4|<\eta_0.
\]

All physical masks, dyadic decorations, and packet multiplicities are retained. The number of packet incidences above one occupied `q1` is `B^{o(1)}`, so packet support and `q1` support have the same fixed-power exponent.

A sufficient new theorem is therefore the fixed-width wall-slab estimate

\[
\boxed{
|P_{\rm wall,eta_0}(B)|
\ll B^{1/2-\delta+o(1)}
}
\tag{R301Z-WALL}
\]

for some fixed constants `eta_0>0` and `delta>0`, uniformly over the full feasible `phi,chi` range and every retained physical packet.

This formulation is stronger and cleaner than a theorem only on the exact line `theta=1/4`. An exact-line theorem alone leaves cells with `|theta-1/4|=o(1)` untreated and therefore does not combine with r301u to give a fixed global power saving.

## 3. Exact gluing with the off-wall theorem

Assume `(R301Z-WALL)` for fixed `eta_0,delta>0`. The nonproportional occupied support splits into the wall slab and its complement. R301u handles the complement, while the proportional branch stays at exponent `7/16`. Therefore

\[
|Q(B)|
\ll
B^{1/2-\delta+o(1)}
+
B^{1/2-\min(2\eta_0,1/16)+o(1)}.
\]

Hence

\[
\boxed{
|Q(B)|
\ll
B^{1/2-\Delta+o(1)},
\qquad
\Delta=\min(\delta,2\eta_0,1/16)>0.
}
\]

Using r301s,

\[
\boxed{
N_2(B)\ll B^{1/2-\Delta+o(1)}.
}
\]

Thus `(R301Z-WALL)` is sufficient for `mu<1/2`.

Conversely, any global strict sub-square-root support theorem for `Q(B)` automatically bounds every fixed wall slab because the slab is a subset of the occupied packet support up to `B^{o(1)}` multiplicity. Therefore, inside the audited r301 support architecture, the fixed-width wall-slab deficit is the exact remaining positive-power gate: the off-wall region is already solved.

## 4. The genuinely new theorem class

The Stage14 final review records one still-unproved theorem class capable in principle of producing a fixed-power deficit on its saturation band:

`UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment`.

R301z does **not** claim that theorem, nor does it claim an off-the-shelf result applies. The compatible target-specific specialization would have to count the occupied nonproportional wall slab itself, retain the nested moving-divisor and simultaneous quadratic-root conditions together with every physical mask, and prove `(R301Z-WALL)` uniformly across a fixed `theta` neighborhood.

Equivalently, a different new theorem is legal if it proves the same wall-slab deficit by a genuinely independent invariant or correspondence with `B^{o(1)}` fibers and a uniform cutoff transfer. What is no longer legal is to multiply the Stage14 complete-host/local-root factors by themselves, or merely rename `q1` through a bounded-degree projection.

## 5. r301 closure and handoff

The r301 letter series has now done all of the following:

- derived the exact Stage20 space-diagonal cover and squareclass/fiber structure;
- reduced the unknown exponent to occupied `q1` support;
- imported the Stage14 off-wall saving without double charging;
- isolated the unique critical wall of the available host package;
- closed the three internal-looking critical-support weapons;
- converted the remaining shrinking-wall ambiguity into the single uniform fixed-width theorem `(R301Z-WALL)`.

No new support exponent is proved in this route. Checkpoint 40 remains open and checkpoint 50 remains blocked.

The next serial is **not** `r301aa`. Per the frozen numbering contract, continuation switches to `Stage27-20-r302-main-batch`, whose first task is to attack `(R301Z-WALL)` with a genuinely new theorem/receiver rather than another r301 reparametrization.

```text
STAGE27_20_R301Z_STATUS=AUDITED_PASS_MERGED
FIXED_WIDTH_WALL_SLAB_RECEIVER_DERIVED=true
WALL_SLAB_THETA_CONDITION=abs(theta-1/4)<eta0
WALL_SLAB_NONPROPORTIONAL_ONLY=true
EXACT_THETA_LINE_ALONE_SUFFICIENT=false
OFF_WALL_FIXED_DISTANCE_SAVING_REUSED=true
GLOBAL_DEFICIT_IF_WALL_THEOREM=Delta=min(delta,2eta0,1/16)
R301Z_WALL_THEOREM_PROVED=false
STAGE14_MAIN_FIRST_MOMENT_GATE_IMPORTED_AS_CANDIDATE_CLASS=true
OFF_THE_SHELF_FIRST_MOMENT_APPLICABILITY_CLAIMED=false
CRITICAL_Q1_SUPPORT_FIXED_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
CURRENT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
AUDIT_STATUS=PASS
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
FRESH_REAUDIT_REQUIRED=false
NEXT_BATCH=Stage27-20-r302-main-batch
R301AA_FORBIDDEN=true
STOP_REASON=UNIFORM_FIXED_WIDTH_WALL_SLAB_SUPPORT_DEFICIT_THEOREM_REQUIRED
```
