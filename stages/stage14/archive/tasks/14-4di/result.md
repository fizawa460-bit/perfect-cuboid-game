# Stage14-4di — full-conductor mainline endpoint and H gate

## Status

`COMPLETE_CONDUCTOR_LOSS_POWER_SAVING_FULL_CONDUCTOR_ENDPOINT_AND_MAINLINE_H_GATE`

Only merged sources are consumed:

```text
Stage14-4dh
Stage14-s7-49
Stage14-X15
```

The open `Stage14-s7-50` branch is not a theorem source.

## 1. Exact conductor-loss saving

Merged s7-49 gives

```text
1_{C_*|m^2+n^2}
 = r_-(C_*)/C_*
 + (1/C_*) sum_{rho^2=-1 mod C_*} sum_{0!=h mod C_*}
     e_{C_*}(h(m-rho*n)).
```

For a nonzero frequency set

```text
g_h=gcd(h,C_*),
q=C_*/g_h,
h=g_h*h0,
gcd(h0,q)=1.
```

The exact-`q` frequencies are parametrized by reduced residues `h0 mod q`, hence there are exactly `phi(q)`. Every coefficient is `1/C_*`, so per Gaussian root line

```text
phi(q)/C_* <= q/C_* = 1/g_h.
```

The root multiplicity is `B^o(1)`. Charge once the complete plus-side coordinate system

```text
(C_*,S,T),
chi+(1/4-chi/2)+(1/4-chi/2)=1/2.
```

On

```text
g_h=B^(lambda+o(1))
```

we obtain

```text
boxed: E_4di(lambda)<=1/2-lambda.
```

Thus every `lambda>0` stratum is strict sub-square-root and possible saturation forces

```text
gcd(h,C_*)=B^o(1),
q=C_*B^o(1).
```

```text
CONDUCTOR_LOSS_FIXED_POWER_SAVING_PROVED=true
CONDUCTOR_LOSS_STRATUM_EXPONENT=1/2-lambda
SQRT_SATURATION_FREQUENCY_GCD=Bo1
FULL_CONDUCTOR_ENDPOINT_PROVED=true
EFFECTIVE_MODULUS_EQUALS_C_STAR_AT_FIXED_POWER=true
```

This is a charged-once statement and is not multiplied by the 4dh Ramanujan estimate, the minus-side complete count, the s7-47 overlap saving, or the X15 k-agreement count.

## 2. Three projections carry the same root

At the effective modulus `q`, let

```text
m=rho*n (mod q),
rho^2=-1 (mod q).
```

With

```text
m=D+A,
n=D-A,
D=delta*s,
A=alpha*r,
```

we get

```text
(1-rho)D=-(1+rho)A (mod q).
```

Since `q` is odd and `rho^2=-1`, `1-rho` is a unit and

```text
(1+rho)/(1-rho)=rho.
```

Therefore

```text
boxed: delta*s=-rho*alpha*r (mod q).
```

Also, for

```text
X_-=mn,
X_0=(m^2-n^2)/2,
```

we have

```text
boxed: X_0=rho*X_- (mod q).
```

Hence the norm root line, k-agreement ratio and X15 third projection use one root and one modulus.

```text
FULL_CONDUCTOR_THREE_PROJECTION_SAME_ROOT=true
X15_K_AGREEMENT_ROOTLINE_EQUIVALENT=true
THIRD_PROJECTION_INDEPENDENT_FULL_CONDUCTOR_SAVING=false
SECOND_LOCAL_MODULUS_DENSITY_ALLOWED=false
```

## 3. Full-conductor absolute boundary

On the only potentially saturating stratum `g_h=B^o(1)`, the exact-conductor coefficient mass is merely

```text
phi(q)/C_*=B^o(1).
```

Charging any one of the three X15 complete coordinate systems therefore still gives

```text
B^(1/2+o(1)).
```

There is no fixed-power conductor parameter left to peel.

```text
FULL_CONDUCTOR_ABSOLUTE_BOUND_EXPONENT=1/2
ABSOLUTE_FULL_CONDUCTOR_TREATMENT_STRICT_SAVING=false
CONDUCTOR_GCD_PEEL_EXHAUSTED=true
```

## 4. Principal/covariance obstruction

The deterministic saving above concerns `h!=0`; the zero mode

```text
r_-(C_*)/C_*
```

is unchanged. Merged 4dg leaves its exponent at `1/2`. Merged X15 retains, for `W_+,W_-,W_k`, the principal term, three pairwise covariance terms, and one genuine triple covariance. Therefore a theorem only for the oscillatory error is insufficient.

A strict whole-family theorem must certify at least one of

```text
PRINCIPAL_DENSITY_FIXED_POWER_LOSS
MAIN_TERM_SCALE_SIGNED_ANTICORRELATION
FRESH_EXACT_PRINCIPAL_TERM_REDUCTION
```

and must control all X15 covariance terms.

```text
PRINCIPAL_ZERO_MODE_STILL_EXPONENT_HALF=true
OSCILLATORY_ERROR_SAVING_ALONE_SUFFICIENT=false
X15_ALL_COVARIANCE_TERMS_MUST_BE_RETAINED=true
```

## 5. Receiver and H gate

The remaining receiver is

```text
SquareRootQuarterFullConductorPrimitivePythagoreanThreeProjectionPhysicalPrincipalDensityAndInverseFractionCovariance
```

with

```text
m,n=B^(1/4+o(1)),
C_*=B^(chi+o(1)), 1/6<=chi<=1/4,
q=C_*B^o(1),
gcd(h0,q)=1,
rho^2=-1 mod q,
P_-=mn=epsilon_-u_*RJ,
m^2+n^2=2epsilon_+C_*ST,
m^2-n^2=4alpha*delta*r*s,
phase=e_q(h0*m-h0*rho*P_-*inverse(m)),
alpha,delta,C_*,S,T,u_*,R,J pairwise separated,
all balanced-cell, squarefree, reciprocal, endpoint and orientation masks retained.
```

Exact gcd/conductor/root-line peeling is exhausted at this receiver. The immutable H target is

```text
stages/stage14/14-4di/h-target.md
```

and is executed directly as `Stage14-4diH`.

```text
MAINLINE_H_NEEDED=true
MAINLINE_BLOCKED_BY_H=true
MAINLINE_H_STAGE=Stage14-4diH
SH48_REOPENED=false
OPEN_S7_50_USED_AS_THEOREM_SOURCE=false
```

## Whole-family boundary

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT=Stage14-4dj_after_4diH
```

## Stage boundary

```text
STAGE14_4DI=COMPLETE_CONDUCTOR_LOSS_POWER_SAVING_FULL_CONDUCTOR_ENDPOINT_AND_MAINLINE_H_GATE
MERGED_4DH_IMPORTED=true
MERGED_S7_49_IMPORTED=true
MERGED_X15_IMPORTED=true
OPEN_S7_50_USED_AS_THEOREM_SOURCE=false
CONDUCTOR_LOSS_FIXED_POWER_SAVING_PROVED=true
CONDUCTOR_LOSS_STRATUM_EXPONENT=1/2-lambda
SQRT_SATURATION_FREQUENCY_GCD=Bo1
FULL_CONDUCTOR_ENDPOINT_PROVED=true
EFFECTIVE_MODULUS_EQUALS_C_STAR_AT_FIXED_POWER=true
FULL_CONDUCTOR_THREE_PROJECTION_SAME_ROOT=true
X15_K_AGREEMENT_ROOTLINE_EQUIVALENT=true
THIRD_PROJECTION_INDEPENDENT_FULL_CONDUCTOR_SAVING=false
FULL_CONDUCTOR_ABSOLUTE_BOUND_EXPONENT=1/2
CONDUCTOR_GCD_PEEL_EXHAUSTED=true
PRINCIPAL_ZERO_MODE_STILL_EXPONENT_HALF=true
OSCILLATORY_ERROR_SAVING_ALONE_SUFFICIENT=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
REMAINING_RECEIVER=SquareRootQuarterFullConductorPrimitivePythagoreanThreeProjectionPhysicalPrincipalDensityAndInverseFractionCovariance
MAINLINE_H_NEEDED=true
MAINLINE_BLOCKED_BY_H=true
MAINLINE_H_STAGE=Stage14-4diH
SH48_REOPENED=false
NEXT=Stage14-4dj_after_4diH
```