# Stage14-4diH — frozen full-conductor principal/covariance theorem audit

## Frozen source

```text
H_STAGE=Stage14-4diH
AUDITED_THROUGH=Stage14-4di
SOURCE_SNAPSHOT_SHA=0a2d313b4bd1baf8fad29cda70cc0f8a44e1b153
TARGET_FILE=stages/stage14/14-4di/h-target.md
REQUESTED_OBJECT=SquareRootQuarterFullConductorPrimitivePythagoreanThreeProjectionPhysicalPrincipalDensityAndInverseFractionCovariancePowerSaving
TARGET_FROZEN=true
SOURCE_SNAPSHOT_FROZEN=true
```

This audit reads exactly the immutable 4di source snapshot. Later mainline, s, X, t, q or toolbox changes do not alter the audited object.

## 1. Frozen receiver

The live packet is

```text
m,n=B^(1/4+o(1)),
C_*=B^(chi+o(1)),
1/6<=chi<=1/4,
q=C_*B^o(1),
gcd(h0,q)=1,
rho^2=-1 mod q,

P_-=mn=epsilon_-u_*RJ,
m^2+n^2=2epsilon_+C_*ST,
m^2-n^2=4alpha*delta*r*s,

phase=e_q(h0*m-h0*rho*P_-*inverse(m)).
```

The eight blocks

```text
alpha,delta,C_*,S,T,u_*,R,J
```

are pairwise separated at fixed-power scale. All balanced-cell, squarefree, reciprocal, endpoint-small and orientation masks are retained. The X15 third projection is the same Gaussian root line and is not charged as a second modulus.

Stage14-4di already removes every fixed-power conductor-loss stratum. Thus the only nonzero-frequency endpoint capable of saturating the square-root bound is full conductor.

## 2. Strict whole-family verdict

No audited off-the-shelf theorem directly proves

```text
N_sat(B) << B^(1/2-delta+o(1))
```

for a fixed `delta>0` uniformly in the full theta-quarter band while retaining the entire frozen physical packet.

```text
FULL_REQUIRED_MASKS_RETAINED=true
FULL_CONDUCTOR_ENDPOINT_USED=true
OFF_THE_SHELF_THEOREM_APPLICABLE=false
FIXED_POWER_SAVING_PROVED=false
CERTIFIED_B_POWER_SAVING_EXPONENT=0
```

This is a theorem-applicability certificate, not a theorem that strict sub-square-root saving is impossible.

## 3. Principal term remains outside the scope of oscillatory estimates

The frozen count contains the exact root-line decomposition

```text
1_{C_*|m^2+n^2}
 = r_-(C_*)/C_* + centered full-conductor correlation.
```

Merged 4dg proves that the principal density term can still have exponent `1/2`. Merged X15 further proves that exact triple centering in the three physical weights `W_+,W_-,W_k` leaves

```text
principal term,
three pairwise covariance terms,
genuine triple covariance.
```

Consequently, even a power-saving theorem for a centered/full-conductor oscillatory error would not by itself prove a whole-family saving unless the principal term and all remaining covariance terms were controlled on the same physical packet.

The audited literature does not provide a fixed-power conditional-density theorem for the principal term and does not provide a main-term-scale signed anti-correlation theorem adapted to these three physical weights.

```text
PRINCIPAL_DENSITY_FIXED_POWER_LOSS_CERTIFIED=false
MAIN_TERM_SCALE_SIGNED_ANTICORRELATION_CERTIFIED=false
X15_ALL_COVARIANCE_TERMS_CONTROLLED=false
```

## 4. Dong--Robles--Zeindler

The 2026 Dong--Robles--Zeindler theorem treats bilinear forms with Kloosterman fractions of the schematic form

```text
sum_{m,n} alpha_m beta_n e(a*inverse(m)/(b*n))
```

with dyadic independent variables and arbitrary coefficient sequences.

The frozen 4di phase is instead a fixed-modulus incomplete Kloosterman phase

```text
e_q(h0*m-h0*rho*P_-*inverse(m)),
```

where the second coefficient `P_-` is itself the physical rotated product and is coupled to the balanced `(u_*,R,J)` factorization and the X15 third projection.

No exact transformation in the frozen source converts the full physical packet into the denominator-varying bilinear-fraction geometry of the theorem while retaining all masks and controlling the principal term.

```text
DONG_ROBLES_ZEINDLER_DIRECTLY_APPLICABLE=false
DONG_ROBLES_ZEINDLER_WHOLE_FAMILY_TRANSFER_CERTIFIED=false
```

## 5. Blomer--Pascadi

Blomer--Pascadi prove strong bilinear bounds for complete Kloosterman sums for arbitrary moduli; in the critical square-root range their theorem saves a fixed power over the trivial bilinear bound.

However the frozen receiver is not yet a bilinear form in complete sums `S(am,n;q)`. Producing such a form requires completing the physical `m`-sum and reorganizing the coupled `P_-`, root label, full-conductor frequency, balanced cell factors, and X15 third weight into independent coefficient sequences with controlled norms.

The frozen stage does not provide this completion/decoupling adapter. More importantly, a bound for the resulting oscillatory error would still leave the principal density and X15 covariance terms.

```text
COMPLETE_KLOOSTERMAN_BILINEAR_FORM_DERIVED=false
BLOMER_PASCADI_DIRECTLY_APPLICABLE=false
BLOMER_PASCADI_WHOLE_FAMILY_TRANSFER_CERTIFIED=false
```

## 6. Milicevic--Qin--Wu

Milicevic--Qin--Wu give power-saving estimates for general bilinear forms with Kloosterman sums modulo arbitrary moduli, including ranges shorter than the classical Polya--Vinogradov threshold.

The same structural obstruction remains: the frozen physical count has not been converted into their complete-sum bilinear geometry with independent coefficient sequences, and their result is an oscillatory bilinear estimate rather than a positive principal-density theorem for the physical packet.

```text
MILICEVIC_QIN_WU_DIRECTLY_APPLICABLE=false
MILICEVIC_QIN_WU_WHOLE_FAMILY_TRANSFER_CERTIFIED=false
```

## 7. Kerr--Shparlinski--Wu--Xi

Kerr--Shparlinski--Wu--Xi prove strong Type-II/incomplete Kloosterman bilinear estimates and related bounds. These results target oscillatory bilinear sums after a suitable incomplete-Kloosterman representation.

The frozen 4di packet retains a coupled modulus/root/product/factorization structure and a three-weight physical incidence. No theorem-ready coefficient factorization matching the required hypotheses is supplied by the exact identities alone, and again the principal term lies outside the oscillatory estimate.

```text
KERR_SHPARLINSKI_WU_XI_DIRECTLY_APPLICABLE=false
KERR_SHPARLINSKI_WU_XI_WHOLE_FAMILY_TRANSFER_CERTIFIED=false
```

## 8. Wright partially fixed-modulus dispersion

Wright's 2026 trilinear Kloosterman-fraction/dispersion results exploit partially fixed moduli and, in the stated distribution application, require a coefficient sequence with suitable equidistribution in small moduli.

The frozen physical coefficients coming from balanced squarefree cells, reciprocal completion and the X15 third projection have no such equidistribution theorem in the source snapshot. The modulus `q` is itself the full common-core conductor and is correlated with the physical factorization packet.

Therefore the required dispersion hypotheses are not established.

```text
WRIGHT_PARTIALLY_FIXED_MODULUS_DIRECTLY_APPLICABLE=false
PHYSICAL_COEFFICIENT_SMALL_MODULUS_EQUIDISTRIBUTION_PROVED=false
```

## 9. What is and is not certified for the oscillatory part

The audited theorems make the full-conductor oscillatory phase analytically plausible, especially after a future legal completion/decoupling adapter. But the frozen snapshot does not contain that adapter with all coefficient norms and masks controlled.

Therefore this audit does not certify a uniform oscillatory-error exponent either:

```text
OSCILLATORY_ERROR_POWER_SAVING_CERTIFIED=false
```

This negative field is deliberately stronger than saying that a theorem might become applicable after more algebra/dispersion work. It records only what is justified for the frozen source.

## 10. Minimal remaining obstruction

The H gate is complete. The mainline is no longer waiting for theorem lookup.

The minimal remaining obstruction is

```text
FullConductorPhysicalPrincipalDensityAndJointThreeProjectionCovariance
```

and the preferred next receiver is

```text
FullConductorConditionalPrincipalDensityDeficitOrSignedThreeProjectionAnticorrelation
```

The next mainline stage should work internally on one of two exact adapters:

```text
1. condition on a legal physical sigma-algebra and prove a fixed-power deficit in the principal density without conditioning on the event C_*|m^2+n^2 itself;
2. derive a signed joint identity in which the principal term and all X15 pairwise/triple covariance terms are controlled together.
```

It must not merely re-run a generic Kloosterman theorem audit.

```text
MAINLINE_H_COMPLETED=true
MAINLINE_H_RESULT=NO_CERTIFIED_UNIFORM_WHOLE_FAMILY_POWER_SAVING
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
```

## Whole-family boundary

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

Next:

```text
NEXT=Stage14-4dj
```

## H boundary

```text
STAGE14_4DIH=COMPLETE_FULL_CONDUCTOR_PRINCIPAL_COVARIANCE_APPLICABILITY_AUDIT
H_STAGE=Stage14-4diH
AUDITED_THROUGH=Stage14-4di
SOURCE_SNAPSHOT_SHA=0a2d313b4bd1baf8fad29cda70cc0f8a44e1b153
TARGET_FILE=stages/stage14/14-4di/h-target.md
TARGET_FROZEN=true
SOURCE_SNAPSHOT_FROZEN=true
FULL_REQUIRED_MASKS_RETAINED=true
FULL_CONDUCTOR_ENDPOINT_USED=true
OFF_THE_SHELF_THEOREM_APPLICABLE=false
OSCILLATORY_ERROR_POWER_SAVING_CERTIFIED=false
PRINCIPAL_DENSITY_FIXED_POWER_LOSS_CERTIFIED=false
MAIN_TERM_SCALE_SIGNED_ANTICORRELATION_CERTIFIED=false
X15_ALL_COVARIANCE_TERMS_CONTROLLED=false
FIXED_POWER_SAVING_PROVED=false
CERTIFIED_B_POWER_SAVING_EXPONENT=0
MINIMAL_REMAINING_OBSTRUCTION=FullConductorPhysicalPrincipalDensityAndJointThreeProjectionCovariance
PREFERRED_RECEIVER=FullConductorConditionalPrincipalDensityDeficitOrSignedThreeProjectionAnticorrelation
MAINLINE_H_COMPLETED=true
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT=Stage14-4dj
```