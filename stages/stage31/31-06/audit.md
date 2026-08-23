# Stage31-06 final hostile audit

Verdict: `PASS_STAGE31_CLOSED_DIRECT_QUARTIC_CERTIFICATION`.

The audited target is exactly `K16-C2-EXT-E-INTEGRAL-CERTIFICATION / R29-EXT-CHANG-E`, parent `J12-PARAMETRIC`. The closure remains confined to the prime-parameter Sophie--Germain thin subfamily.

## Independent audit findings

1. The frozen Paper-E certification gap was real: the source used bounded `ellratpoints` and a sampled height-difference constant, not a complete integral-point certificate.
2. Stage31 does not rely on the unsafe statement `C_anom(Z) -> E_anom(Z)`. Instead it uses the exact integral scaling `U=10Z`:

```text
C_anom: 20 Z^2 = Y^4+8Y^3+18Y^2-8Y+1
Q:      U^2 = 5Y^4+40Y^3+90Y^2-40Y+5
```

For integral `Y,Z`, `(Y,U)=(Y,10Z)` is integral on `Q`; conversely an integral point on `Q` lies on `C_anom(Z)` exactly when `10|U`, with `Z=U/10`.
3. Magma V2.29-9 `IntegralQuarticPoints(Q,[1,10])` was executed successfully in GitHub Actions. The Magma handbook specifies this routine as returning all integral points on the quartic when a rational point is supplied. The computation yielded one representative for each hyperelliptic sign pair:

```text
(-1,10), (1,-10), (11,370)
```

Restoring `U -> -U` and filtering by `10|U` gives exactly

```text
C_anom(Z)={(-1,±1),(1,±1),(11,±37)}.
```

No bounded-search or sampled-height completeness claim is used.
4. The explicit rational birational map to `E_anom: y^2=x^3-275x+1750` was algebraically rechecked. On `Y != 1` the submitted formulas satisfy the elliptic equation modulo the quartic equation, and the exceptional points `C(1,1)->O`, `C(1,-1)->(9,2)` are separately recorded. The direct quartic completeness proof does not depend on preservation of integrality under this map.
5. Magma `MordellWeilGroup(E)` returned `Z/2 + Z` with both status flags true. Magma documentation defines the second boolean as true exactly when the returned group is known to be the full Mordell--Weil group. Thus the rank/full-group/saturation cross-check is certified. This MW certificate is not load-bearing for quartic completeness.
6. The six quartic points all satisfy the quartic equation exactly. The frozen branch dictionary leaves no prime Case-I point; Case II leaves only `p=11,q=71`. Exact integer arithmetic reconstructs `(a,b,c)=(3124,4557,9840)`, with two face squares and the space square, while `b^2+c^2=117591849` lies strictly between `10843^2` and `10844^2`.

## Scope repair

The submitted phrase `DIRECT_QUARTIC_INTEGRALITY_TRANSFER=VERIFIED` is accepted only in the following precise sense:

```text
C_anom(Z) <-> { (Y,U) in Q(Z) : 10 | U }
```

It does **not** mean that the quartic-to-elliptic birational map preserves integrality. The original Stage29 elliptic-transfer wall is bypassed by a stronger direct complete integral-point certificate on the quartic itself. Therefore receiver discharge is credited as `DIRECT_QUARTIC_CERTIFICATION_BYPASS`, not as proof of an unproved `C(Z)->E(Z)` implication.

## Final state

```text
QUARTIC_ELLIPTIC_BIRATIONAL_MAP=VERIFIED
C_TO_E_INTEGRALITY_TRANSFER_PROVED=false
DIRECT_SCALED_QUARTIC_INTEGRAL_EQUIVALENCE=VERIFIED
DIRECT_QUARTIC_INTEGRAL_POINT_COMPLETENESS=VERIFIED
MW_FULL_GROUP_CERTIFICATE=VERIFIED_CROSSCHECK
QUARTIC_INTEGRAL_POINTS=COMPLETE_6_SIGNED_POINTS
PRIME_SOPHIE_GERMAIN_SUBFAMILY_EXCLUSION=VERIFIED
R29_EXT_CHANG_E=DISCHARGED_DIRECT_QUARTIC_CERTIFICATION
K16_C2_EXT_E_INTEGRAL_CERTIFICATION=CLOSED
FALLBACK_UNIT_ACTIVATED=false
NEW_CLASS3_THEOREM_GATE=NONE
J12_PARAMETRIC=AMBER
ROUTE_COLOR_CHANGED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

Post-Stage31 research-OS delta:

```text
ACTIVE_KERNEL_COUNT=11
CLASS2_KERNEL_COUNT=2
CLASS3_KERNEL_COUNT=9
```

Stage31 may close.