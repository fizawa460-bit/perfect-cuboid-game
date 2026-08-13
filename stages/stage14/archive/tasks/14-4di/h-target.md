# Stage14-4diH immutable theorem target

```text
H_STAGE=Stage14-4diH
SOURCE_STAGE=Stage14-4di
TARGET_FREEZES_AT_DISPATCH=true
REQUESTED_OBJECT=SquareRootQuarterFullConductorPrimitivePythagoreanThreeProjectionPhysicalPrincipalDensityAndInverseFractionCovariancePowerSaving
```

Retain all physical filters and endpoint/2-primary decorations from merged `4dh`, merged `s7-49`, merged `X15`, and the 4di conductor-loss theorem.

```text
m,n=B^(1/4+o(1)),
C_*=B^(chi+o(1)), 1/6<=chi<=1/4,
q=C_*B^o(1),
gcd(h0,q)=1,
rho^2=-1 mod q,
P_-=mn=epsilon_-u_*RJ,
m^2+n^2=2epsilon_+C_*ST,
m^2-n^2=4alpha*delta*r*s,
phase=e_q(h0*m-h0*rho*P_-*inverse(m)).
```

The eight blocks `alpha,delta,C_*,S,T,u_*,R,J` are pairwise separated at fixed-power scale. The X15 third projection is the same root line and must not be charged as an independent modulus.

4di proves every fixed-power conductor loss is strict sub-square-root, so only full conductor can still saturate.

## Question

Audit whether an existing theorem or direct theorem transfer gives a fixed `delta>0`, uniform in the theta-quarter band and all retained masks, such that

```text
N_sat(B) << B^(1/2-delta+o(1)).
```

Distinguish strictly between

```text
oscillatory-error saving,
principal-density saving,
main-term-scale signed anti-correlation,
whole-family saving.
```

A power-saving bound for only the centered/full-conductor oscillatory error is not sufficient: merged 4dg leaves a principal term of exponent `1/2`, and merged X15 leaves three pairwise covariance terms plus a genuine triple covariance.

A positive whole-family verdict must certify at least one of

```text
PRINCIPAL_DENSITY_FIXED_POWER_LOSS=true
MAIN_TERM_SCALE_SIGNED_ANTICORRELATION=true
FRESH_EXACT_PRINCIPAL_TERM_REDUCTION=true
```

and explicitly control all X15 covariance terms.

At minimum audit current forms of:

```text
Dong--Robles--Zeindler: bilinear Kloosterman fractions
Blomer--Pascadi: bilinear Kloosterman sums via quadratic characters
Milicevic--Qin--Wu: bilinear Kloosterman sums for arbitrary moduli
Kerr--Shparlinski--Wu--Xi: incomplete Kloosterman bilinear forms
Wright: partially fixed-modulus trilinear Kloosterman fractions / dispersion
```

Check coefficient geometry, support/interval hypotheses, modulus role, averaging variables, coprimality, and whether the theorem controls an error term or the positive principal density.

```text
DO_NOT_REOPEN_SH48=true
DO_NOT_USE_OPEN_S7_50_AS_THEOREM_SOURCE=true
DO_NOT_CROSS_PROMOTE_FIXED_U_RESULTS=true
DO_NOT_TREAT_X15_THIRD_PROJECTION_AS_INDEPENDENT_MODULUS=true
DO_NOT_DROP_PHYSICAL_BALANCED_CELL_MASKS=true
DO_NOT_DROP_SQUAREFREE_OR_PAIRWISE_SEPARATION=true
DO_NOT_REPLACE_FULL_COUNT_BY_ONLY_CENTERED_ERROR=true
DO_NOT_COUNT_THE_SAME_C_STAR_MODULUS_TWICE=true
```

Required output:

```text
STAGE14_4DIH=COMPLETE|INCOMPLETE
SOURCE_SNAPSHOT_SHA=<immutable 4di head>
TARGET_FILE=stages/stage14/14-4di/h-target.md
TARGET_FROZEN=true
FULL_REQUIRED_MASKS_RETAINED=true
FULL_CONDUCTOR_ENDPOINT_USED=true
OFF_THE_SHELF_THEOREM_APPLICABLE=true|false
OSCILLATORY_ERROR_POWER_SAVING_CERTIFIED=true|false
PRINCIPAL_DENSITY_FIXED_POWER_LOSS_CERTIFIED=true|false
MAIN_TERM_SCALE_SIGNED_ANTICORRELATION_CERTIFIED=true|false
X15_ALL_COVARIANCE_TERMS_CONTROLLED=true|false
FIXED_POWER_SAVING_PROVED=true|false
CERTIFIED_B_POWER_SAVING_EXPONENT=<number>
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=true|false
NEXT=Stage14-4dj
```