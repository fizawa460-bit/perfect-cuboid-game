# Stage28-50-r2 fresh audit

```text
AUDITED_PR=1279
AUDITED_SUBMISSION_HEAD=0d9e79484c1b01c61c5d64eb576208d01c5706ed
AUDIT_VERDICT=PASS
CHECKPOINT50_R2_AUDIT=PASS
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
ADVANCE_TO_CHECKPOINT60=true
NEXT_CHECKPOINT=60
NEXT_EXPECTED_COMMAND=Stage28-main-batch
```

## Audit findings

The new Saunderson injective-cone argument is valid. For primitive Euclid parameters `u=r^2-s^2`, `v=2rs`, `w=r^2+s^2`, the exact physical height identity

\[
R^2=w^6+16u^2v^2w^2
\]

reduces, with `y=(s/r)^2`, to the submitted polynomial expression. The displayed factorization of the difference from `64` is consistent, and its second factor is positive on `0<=y<=1`; hence `R<=8r^6` is valid.

On the cone `1/8<=s/r<=4/5`, the normalized legs satisfy `alpha>=9/41` and `beta>=16/65`, both larger than `(sqrt(2)-1)/2`. Therefore each of the other two face diagonals is strictly larger than `w^3`, making `w^3` the unique smallest face diagonal. The physical output consequently recovers `w`, then `uv` from the opposite edge, then the unordered pair `{u,v}` from `u^2+v^2=w^2`; primitive parity fixes the oriented input. Thus the Saunderson output map is injective on this cone.

The cone area is `27T^2/80`; multiplying by the standard coprime opposite-parity density `4/pi^2` gives

\[
#C(T)=\frac{27}{20\pi^2}T^2+O(T\log T).
\]

Since `R<=8T^6`, choosing `T=(B/8)^(1/6)` yields

\[
M_3(B)\ge\left(\frac{27}{40\pi^2}+o(1)\right)B^{1/3},
\]

and hence

\[
\liminf_{B\to\infty} M_3(B)/B^{1/3}\ge 27/(40\pi^2)>0.
\]

This strengthens coefficient information only; it does not improve the exponent above `1/3`, identify the true `M3` exponent, prove an asymptotic, or order `M3` against `N2`.

The additional L9-L14 routes are materially distinct enough for the bounded-exploration requirement. The remaining receiver `HigherEfficiencyOffBranchPhysicalConstructionOrUniformMovingEllipticSquareLiftCount` is sufficiently narrow and research-request-ready. No further currently available repo-native construction route was identified that legally improves the exponent beyond `1/3` for `M3` or beyond `1/4` for `N2` without new global arithmetic input or entering the deferred perfect-cuboid endpoint.

```text
SAUNDERSON_HEIGHT_R_LE_8_R6_AUDIT=PASS
SAUNDERSON_INJECTIVE_CONE_AUDIT=PASS
PHYSICAL_OUTPUT_FIBER_ON_CONE_AUDIT=PASS_1
PRIMITIVE_CONE_DENSITY_AUDIT=PASS
M3_EXPLICIT_ONE_THIRD_LIMINF_COEFFICIENT_AUDIT=PASS_27_OVER_40_PI2
MATERIALLY_DISTINCT_LOWER_ROUTES_TOTAL_AUDIT=PASS_14
MAXIMAL_BOUNDED_EXPLORATION_CLAIM_AUDIT=PASS
OPEN_GATE_RESEARCH_REQUEST_READY_AUDIT=PASS
M3_EXPONENT_ABOVE_ONE_THIRD_PROVED=false
N2_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
SOURCE_TARGET_ASYMPTOTIC_ORDERING_IDENTIFIED=false
PERFECT_CUBOID_CONCLUSION=NONE
```