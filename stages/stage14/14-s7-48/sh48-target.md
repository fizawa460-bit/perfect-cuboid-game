# Stage14-sH48 target — Gaussian norm / rotated coordinate-product balanced factorization power saving

## Snapshot protocol

Prepared by `Stage14-s7-48` under `stages/stage14/H-PROTOCOL.md`.

```text
H_STAGE=Stage14-sH48
SOURCE_STAGE=Stage14-s7-48
TARGET_FILE=stages/stage14/14-s7-48/sh48-target.md
TARGET_FREEZES_AT_DISPATCH=true
RUNNING_SH48_MAY_CHASE_S7_49_PLUS=false
SH48_DISPATCHED_BY_S7_48=false
```

At dispatch, freeze the exact s7-48 source head SHA.  Later s/mainline/t/X progress must not mutate this mathematical question; a materially different receiver uses the next H identifier.

## Requested object

```text
SquareRootQuarterScalePairwiseSeparatedGaussianNormRotatedCoordinateProductDualBalancedCellFactorizationPowerSaving
```

## Audited-through exact reduction

Fix a square-root saturation block with

```text
theta=1/4,
1/6<=chi<=1/4,
phi=(chi+1/4)/2,
```

and fixed endpoint-small / 2-primary decorations `epsilon_+,epsilon_-=B^o(1)`.

The pairwise-separated physical variables satisfy

```text
C_*=B^(chi+o(1)),
u_*=B^(1/4-chi+o(1)),
S,T=B^(1/4-chi/2+o(1)),
R,J=B^(phi+o(1)),
```

with all four norm blocks

```text
C_*, S*T, u_*, R*J
```

pairwise coprime at fixed-power scale.

Put

```text
Z=D+iA,
D>A>0,
D,A=B^(1/4+o(1)).
```

The exact kernel is

```text
N(Z)=D^2+A^2=epsilon_+ C_* S T,
(1+i)conjugate(Z)=(D+A)+i(D-A),
(D+A)(D-A)=D^2-A^2=epsilon_- u_* R J.
```

Physical completion requires the balanced squarefree cell splits and all merged reciprocal/orientation/reconstruction masks.

Stage14-s7-48 proves:

```text
fixed (C_*,S,T) => full packet multiplicity B^o(1),
fixed (u_*,R,J) => full packet multiplicity B^o(1),
plus complete count exponent = 1/2,
minus complete count exponent = 1/2,
no nonzero algebraic eliminant among the six norm blocks follows from the two square equations alone,
no second deterministic divisor-switch saving remains.
```

Do not reopen common-core/root-line spacing, sH44, the same-side overlap saving of s7-47, or a second count of the same finite-fiber coordinates.

## Exact analytic target

Determine whether there exists an absolute fixed `delta>0`, uniform for

```text
1/6<=chi<=1/4,
```

such that the physical admissible count satisfies

```text
N_phys(B;chi)
 << B^(1/2-delta+o(1)).
```

The theorem must exploit correlation between

```text
Gaussian norm factorization:
  N(Z)=epsilon_+ C_* S T

and rotated coordinate-product factorization:
  Re((1+i)conjugate Z) * Im((1+i)conjugate Z)
  =epsilon_- u_* R J,
```

for the **same** Gaussian integer `Z`.

A logarithmic saving is not enough for the requested verdict field `CERTIFIED_B_POWER_SAVING_EXPONENT`; report `0` unless a fixed power is rigorous.

## Physical masks that must be retained

Retain, directly or with only certified `B^o(1)` loss:

```text
D>A>0 and D,A~B^(1/4),
C_*u_*~B^(1/4),
pairwise fixed-power separation of C_*,S*T,u_*,R*J,
S,T balanced at B^(1/4-chi/2),
R,J balanced at B^((chi+1/4)/2),
squarefree/pairwise-coprime physical xi cells,
mixed fourth-root allocation inherited from s7-46/47,
first signed residual allocation,
reciprocal/orientation masks,
post-column physical completion finite fiber,
charged-once accounting of every modulus/support.
```

Do not replace the physical family by an unrestricted positive Gaussian norm family if the replacement destroys the coordinate-product factorization or cell masks.

## Candidate theorem technologies to audit

Audit strict applicability, not superficial resemblance, for at least:

```text
1. determinant / bilinear-trilinear point bounds after expanding Z into Gaussian factors;
2. divisor switching plus inverse-fraction / Kloosterman-fraction bilinear forms;
3. complete Kloosterman / Kuznetsov style bilinear estimates if a legal completion adapter exists;
4. modular-square-root energy estimates for the mixed +/- root allocation;
5. sieve or divisor-distribution results for values of binary quadratic forms / products of linear forms;
6. Gaussian-integer factorization or shifted/rotated coordinate divisor theorems;
7. multiplication-table / balanced-divisor distribution results, noting that logarithmic-density losses do not certify fixed B-power saving.
```

Relevant Stage14 literature radar includes `Stage14-q10`, but no q10 theorem may be imported unless its exact hypotheses are verified for this frozen receiver.

## Applicability standard

A positive verdict requires all of:

```text
FULL_REQUIRED_MASKS_RETAINED=true,
NO_ALREADY_CHARGED_CORE_REUSED_AS_FRESH_MODULUS=true,
NO_PLUS_MINUS_COMPLETE_COUNTS_MULTIPLIED=true,
UNIFORM_IN_CHI=true,
FIXED_DELTA_POSITIVE=true,
```

and an explicit derivation from the theorem statement to

```text
B^(1/2-delta+o(1)).
```

If a theorem handles only a one-sided norm count, only nonzero Fourier frequencies, only a fixed modulus, or only generic coefficients while leaving a principal `B^(1/2)` physical density term, it is not sufficient.

## Required verdict fields

```text
H_STAGE=
AUDITED_THROUGH=Stage14-s7-48
SOURCE_SNAPSHOT_SHA=
TARGET_FILE=stages/stage14/14-s7-48/sh48-target.md
REQUESTED_OBJECT=SquareRootQuarterScalePairwiseSeparatedGaussianNormRotatedCoordinateProductDualBalancedCellFactorizationPowerSaving
TARGET_FROZEN=true
FULL_REQUIRED_MASKS_RETAINED=true|false
OFF_THE_SHELF_THEOREM_APPLICABLE=true|false
FIXED_POWER_SAVING_PROVED=true|false
CERTIFIED_B_POWER_SAVING_EXPONENT=<delta or 0>
UNIFORM_IN_CHI=true|false
MINIMAL_REMAINING_OBSTRUCTION=
PREFERRED_RECEIVER=
S_ROUTE_BLOCKED_WAITING_FOR_H=false
NEXT_H_NEEDED=true|false
```

## Expected output

```text
stages/stage14/14-sH48/result.md
stages/stage14/14-sH48/literature.md
stages/stage14/14-sH48/BOUNDARY.txt
stages/stage14/scripts/14-sH48/<audit>.py
.github/workflows/<dedicated-sH48-workflow>.yml
```

Dedicated CI must validate the frozen source SHA/target, the arithmetic reduction, theorem-boundary markers, and relevant merged predecessor regressions.
