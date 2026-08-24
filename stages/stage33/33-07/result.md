# Stage33-07 — BR2A integration — REOPENED / BLOCKED_NEW_KERNEL

Stage33-08 hostile audit #1375 found a theorem-scope regression in the global-Q residue-lift step used by the original Stage33-07 closure.

Current effective state:

```text
STAGE33_UNIT=33-07
UNIT_STATUS=BLOCKED_NEW_KERNEL
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
BR2A=BLOCKED_NEW_KERNEL
UNRESOLVED_UNKNOWN_IN_SCOPE=1
NEW_KERNEL_ID=R33-BR0G-BR2A-GLOBAL-RESIDUE-LIFT-ARITHMETIC-HS-DESCENT
STAGE33_PROGRESS_EFFECTIVE=6/11
STAGE33_08_RELEASED=false
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```

Historical audit verdict
`PASS_AFTER_J2_PROPER_TRANSCENDENTAL_ENDPOINT_SURVIVAL_AND_EXACT_BR0B_BR0G_GLOBAL_INTEGRATION`
is retained as provenance, but its global BR0G Q-lift/inventory credit is superseded by the Stage33-08 hostile re-audit.

## What remains exact

The regression does **not** affect:

```text
BR0B all-primary inventory and full boundary injection
J2 Q-defined exact order 2
J2 endpoint pullback nonzero
J2 proper/unramified/transcendental
J2 Q2 evaluation nonconstant with values 0 and 1/2
seven-line endpoint contribution = 0
Stage33-04 BR0G boundary-residue presentation
```

The Stage33-04 finite ramified object

```text
(Z/2)^49 direct_sum (Z/4)^12
```

remains an exact **boundary residue module**.

## What is no longer promoted

Panin--Zainoulline Theorem 1.1 is semi-local and does not by itself prove global surjectivity of compatible residues on the whole projective surface. Therefore the following Stage33-07 claims are pending repair:

```text
complete Q-defined global BR0G class inventory
Q-defined global lifts of the constant-character complement
Q-defined global lifts of the R17/O12 finite residue directions
noncanonical finite Gersten splitting over Q
global direct-sum presentation of those lifts
full duplicate quotient involving the unknown global lifts
```

The cuboid minimal resolution is simply connected, so the global geometric residue-lift obstruction over Qbar vanishes. The remaining kernel is arithmetic descent to Q, where the proper geometric Brauer module is nonzero (transcendental l-adic rank 14).

## Closure accounting

The Stage33-07 contract requires a complete relevant Q-defined class list. That gate is currently false, so the unit is not CLOSED. A conservative current count retains only the clearly unaffected closure gates:

```text
CLOSURE_CRITERIA_TOTAL=14
CLOSURE_CRITERIA_SATISFIED_CONSERVATIVE=4
```

The exact repair target is

```text
L33-07-REPAIR-COMPUTE-ARITHMETIC-HS-DESCENT-OF-BR0G-RESIDUE-LIFTS
```

No Brauer--Manin emptiness, endpoint emptiness, or Perfect Cuboid existence/nonexistence conclusion follows from this reopened state.
