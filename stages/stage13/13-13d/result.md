# Stage13-13d — deterministic final consistency audit

> STATUS: `STAGE13_13D_COMPLETE_DETERMINISTIC_FINAL_CONSISTENCY_AUDIT`
>
> INPUT: merged Stage13-13c canonical proof.
>
> PURPOSE: verify every computable constant/interface in the canonical proof independently of numerical fitting, and reject stale/superseded formulas before the R04 review bundle is built.

## Decision

The audit passes.

```text
STAGE13_13D=COMPLETE_DETERMINISTIC_FINAL_CONSISTENCY_AUDIT
CANONICAL_CONSTANTS_REPRODUCED=true
STALE_SUPERSEDED_FORMULAS_IN_CANONICAL_FILES=0
THEOREM_CHANGED=false
NEXT=13-13e
```

No mathematical repair was made to `stage13-final-proof.md`.

## 1. Chamber integrals

The audit numerically integrates the actual spherical chamber

```text
0 < x < y < z,  x^2+y^2+z^2=1
```

using deterministic composite Simpson quadrature with `N=200` in each active integration variable. It reproduces

```text
I_ab = 0.659705248706466
I_ac = 0.302699752677505
I_bc = 0.271295548762532
```

against the locked validators

```text
I_ab = 0.659705248705705
I_ac = 0.3026997526726076
I_bc = 0.2712955487578571
```

with tolerance `1e-9`.

The independently computed sum is

```text
1.233700550146503
```

and agrees with

```text
pi^2/8 = 1.233700550136170
```

within the same tolerance.

## 2. Normalized directional vector and J_q bridge

From the recomputed chamber integrals the audit forms

```text
P_q = 8 I_q / pi^2
```

and obtains

```text
P_ab = 0.534736933232016
P_ac = 0.245359177836221
P_bc = 0.219903888940138
sum   = 1.000000000008376
```

which reproduces the locked direction vector to better than `1e-9`.

It also forms

```text
J_q = 2 I_q / pi
```

and obtains

```text
J_ab = 0.419981405261209
J_ac = 0.192704647645276
J_bc = 0.172712110497541
sum  = 0.785398163404026
```

against

```text
pi/4 = 0.785398163397448.
```

Thus the symbolic relations

```text
sum I_q = pi^2/8
P_q = 8 I_q/pi^2
J_q = 2 I_q/pi
sum J_q = pi/4
```

are numerically reproduced from the chamber itself.

## 3. Exact finite Stage12-to-Stage13 bridge checksum

The frozen `B=100000` fixture is checked as an exact integer identity:

```text
Stage12 projected = (168424, 86472, 81520)
raw incidence     = ( 84212, 43236, 40760)
raw total         = 168208
pair-overlap sum  = 89
triple overlap    = 0
exactly-one       = ( 84146, 43180, 40704)
exactly-one total = 168030
```

The audit verifies

```text
168424 = 2*84212
 86472 = 2*43236
 81520 = 2*40760
336416 = 2*168208
168030 = 168208 - 2*89 + 3*0
```

exactly.

This is a deterministic interface check only; it is not asymptotic evidence.

## 4. Inert-prime unit-state character count

For the inert primes

```text
p = 7, 11, 19, 23
```

the audit enumerates the finite-field unit state directly:

```text
X^2+Y^2=1
Delta^2-Z^2=1
```

and counts states with `X^2+Z^2` a square or zero.

Results:

```text
p= 7: total  48, accepted  32 = (p+1)^2/2, lambda_p=3/4
p=11: total 120, accepted  72 = (p+1)^2/2, lambda_p=2/3
p=19: total 360, accepted 200 = (p+1)^2/2, lambda_p=3/5
p=23: total 528, accepted 288 = (p+1)^2/2, lambda_p=7/12
```

Thus the deterministic finite-field checks reproduce

```text
alpha_p  = (p+1)/(2(p-1))
lambda_p = (p+5)/(2(p+1))
lambda_p <= 3/4 for p>=7.
```

The proof remains the symbolic character-sum derivation in the canonical text; enumeration is only a reproducibility check.

## 5. Canonical theorem lock scan

The script requires the canonical proof to contain the exact locked interfaces

```text
RAW_DIRECTIONAL=A_q(B) ~ kappa*I_q/(3*pi^3) B(log B)^3
PAIR_OVERLAP=O_qr(B)=o(B(log B)^3)
TRIPLE_OVERLAP=T(B)=o(B(log B)^3)
EXACT_ONE_DIRECTIONAL=N_q(B) ~ kappa*I_q/(3*pi^3) B(log B)^3
EXACT_ONE_TOTAL=N1(B) ~ kappa/(24*pi) B(log B)^3
DIRECTION_LIMIT=P_q=8*I_q/pi^2
CHAMBER_SUM=sum I_q=pi^2/8
JQ_BRIDGE=J_q=2*I_q/pi
INERT_LOCAL_MULTIPLIER=lambda_p=(p+5)/(2*(p+1))
NO_PERFECT_CUBOID_NONEXISTENCE_ASSUMPTION=true
```

All are present.

## 6. Superseded-formula scan

Only the mathematical core before the dedicated provenance appendix is scanned, so legitimate historical names in the provenance section do not create false positives.

The forbidden proof-core tokens are

```text
Stage13-7jb
Stage13-7jf
D_q/K_q
lambda_p <= 1/2 + O(1/p)
```

No hit is found.

```text
STALE_SUPERSEDED_FORMULAS_IN_CANONICAL_FILES=0
```

## 7. CI and machine-readable lock

The committed machine-readable result is

```text
stages/stage13/data/13-13d/final_consistency_audit.json
```

and the reproducibility script is

```text
stages/stage13/scripts/13-13d/final_consistency_audit.py
```

The dedicated workflow

```text
.github/workflows/stage13-13d-final-consistency.yml
```

runs the script with `--check-report`. CI fails if the canonical proof/roadmap changes in a way that changes the deterministic report without intentionally regenerating and reviewing the report.

## Final lock

```text
STAGE13_13D=COMPLETE_DETERMINISTIC_FINAL_CONSISTENCY_AUDIT
AUDIT_STATUS=PASS
CANONICAL_CONSTANTS_REPRODUCED=true
CHAMBER_SUM_REPRODUCED=true
DIRECTION_VECTOR_REPRODUCED=true
JQ_BRIDGE_REPRODUCED=true
FINITE_FACTOR_TWO_BRIDGE_REPRODUCED=true
INERT_UNIT_ACCEPTANCE_REPRODUCED=true
INERT_LOCAL_MULTIPLIER_REPRODUCED=true
STALE_SUPERSEDED_FORMULAS_IN_CANONICAL_FILES=0
THEOREM_CHANGED=false
R03_MUTATED=false
NEXT=13-13e
```
