# Stage31 — EXT-E-INTEGRAL-CERTIFICATION roadmap

Status: ROADMAP_SUBMISSION_PENDING_AUDIT

## Objective

Stage31 attacks the post-Stage29 Class-2 kernel

```text
K16-C2-EXT-E-INTEGRAL-CERTIFICATION
child: R29-EXT-CHANG-E
parent route: J12-PARAMETRIC
```

Frozen Stage29 wall:

```text
explicit integrality-preserving quartic-to-elliptic maps
+
source-locked complete IntegralPoints / elliptic-logarithm certificate
+
audited pullback and cuboid reconstruction
```

The goal is to decide the exact prime-parameter Sophie--Germain thin subfamily claim from Paper E. Completion is **thin-family closure only**. It does not prove global perfect-cuboid existence or nonexistence.

Target close state, if the external claim survives exact reconstruction:

```text
QUARTIC_ELLIPTIC_BIRATIONAL_MAP=VERIFIED
INTEGRALITY_TRANSFER=VERIFIED
MORDELL_WEIL_BASIS=VERIFIED_AND_SATURATED
COMPLETE_INTEGRAL_POINT_CERTIFICATE=VERIFIED
QUARTIC_INTEGRAL_POINTS=COMPLETE
PULLBACK_RECONSTRUCTION=COMPLETE
PRIME_SOPHIE_GERMAIN_SUBFAMILY_EXCLUSION=VERIFIED
R29_EXT_CHANG_E=DISCHARGED_INTEGRAL_CERTIFICATION
K16_C2_EXT_E_INTEGRAL_CERTIFICATION=CLOSED
```

A negative result is also valid: if the claimed point set, map, integrality implication, or family reduction is false, Stage31 must record the exact counterexample and reclassify the receiver rather than repair the source claim by assumption.

## Frozen audited starting facts

Do not grant more credit than Stage29 already audited.

Internal source authority:

```text
stages/stage29/29-13/external-source-audit.md
stages/stage29/29-13/theorem-dependency-ledger.json
stages/stage29/29-15/open-receiver-triage.json
stages/stage29/29-16/active-kernel-ledger.json
```

Stage29 verified the following inputs:

```text
C_anom: 20 Z^2 = Y^4 + 8Y^3 + 18Y^2 - 8Y + 1
E_anom: y^2 = x^3 - 275x + 1750
Cremona label: 800a3
LMFDB label: 800.d2
rank(E(Q)) = 1
torsion(E(Q)) = Z/2
external database reports elliptic integral-point count = 7
```

Stage29 explicitly did **not** certify the Paper-E closure because:

```text
1. no load-bearing explicit quartic <-> elliptic map was supplied;
2. no rigorous integrality implication was proved;
3. the committed point search was bounded, not a complete IntegralPoints proof;
4. the height-difference constant in 04_height_completeness.gp was sampled;
5. no complete pullback/reconstruction ledger was supplied.
```

Therefore neither `elliptic integral-point count = 7` nor the paper's claimed quartic list may be used as completeness credit before Stage31 certifies the transfer and enumeration.

## External source lock

Primary external repository:

```text
weiqi-kids/perfect-cuboid-problem
```

Roadmap source snapshot:

```text
commit = bd3018b896c8ac15b56cadc382af1477dca9e97a
paper-e/paper.tex blob = 1ff42f5a657ab9edafcfd6060f015a19e4322a83
paper-e/scripts/01_identity_and_reduction.gp blob = a117cf78176d6818d6dca99388e827bcc1e2269e
paper-e/scripts/02_curve_rank_label.gp blob = b0c30169a920ef7ab6ba7040875ab8d99de5aa18
paper-e/scripts/03_integral_points.gp blob = 80a113d42641e474de01c1cbe1b15c06a9744892
paper-e/scripts/04_height_completeness.gp blob = ba372d9c0a4f6fad2884ad192f5f64f85244396a
```

Every execution must use this pinned snapshot unless a deliberate source-refresh record is created. Later edits to the external repository receive no automatic theorem credit.

## Operating model: one-shot first, split only on a real wall

Stage31 is intentionally **not** pre-split into many small tasks.

The geometry is unusually concentrated:

```text
one thin prime subfamily
-> one genus-one quartic
-> one rank-one elliptic curve
-> one complete integral-point enumeration
-> one finite reconstruction ledger
```

Therefore the primary execution unit is an XL full-closure attempt.

User-facing commands:

```text
Stage31-main-batch
Stage31-audit
```

No third command is required.

`Stage31-main-batch` must first attempt `31-01-XL`. If all hard close conditions are met, it jumps directly to final hostile audit. It may activate fallback units `31-02` through `31-05` **only if** the one-shot attempt exposes a precise unresolved Class-2/tool/CAS leaf. The controller must name that leaf exactly; vague timeout-based splitting is forbidden.

Stage31 execution must not begin until Stage30 has passed its final audit and its final Stage30 PR is merged. The Stage31 roadmap may be reviewed/merged earlier because it does not alter Stage30 state.

---

## Stage31-00 — ROADMAP_AND_SOURCE_LOCK

Size: S
Owner: ChatGPT

Purpose: freeze the exact receiver, external snapshot, allowed conclusions, and fail-closed rules.

Hard close condition:

```text
R29_EXT_CHANG_E_WALL_FROZEN=true
EXTERNAL_PAPER_E_COMMIT_PINNED=true
THIN_FAMILY_ONLY_FIREWALL=true
STAGE30_FINAL_CLOSE_REQUIRED_BEFORE_EXECUTION=true
```

---

## Stage31-01-XL — FULL_CLOSURE_ATTEMPT

Size: XL
Owner: ChatGPT, using exact CAS/code where needed

This is the preferred path. Execute the complete repair contract in one research unit.

### A. Reconstruct the family reduction

Fresh-check the load-bearing Paper-E reduction from prime `p` to the two Sophie--Germain branches and the common quartic.

Required exact checks include:

```text
Case II: q = (p^2 + 2p - 1)/2
Case I:  q = (p^2 - 2p - 1)/2
Case I <-> Case II quartic involution Y -> -Y
C_anom: 20 Z^2 = Y^4+8Y^3+18Y^2-8Y+1
```

Do not silently broaden this to composite `p` or to all Case-B candidates.

### B. Construct explicit birational maps

Produce exact rational formulas

```text
phi: C_anom --> E_anom
psi: E_anom --> C_anom
```

with:

- exact coefficients over Q;
- exceptional/undefined loci listed;
- symbolic verification that the maps land on the stated curves;
- symbolic verification of both compositions on the common dense open;
- exact treatment of the chosen base point and points at infinity.

Using only `ellfromeqn`/Jacobian identification without formulas is insufficient.

### C. Prove the legal integrality transfer

For every integral quartic point relevant to the prime family, prove exactly what arithmetic condition its elliptic image satisfies.

Preferred outcome:

```text
C_anom(Z) -> E_anom(Z)
```

If the actual map gives denominators, Stage31 must not pretend they disappear. Instead derive an explicit finite denominator/S-integral condition and enumerate that exact set. Acceptable alternatives include:

```text
C_anom(Z) -> E_anom(Z[1/S]) with explicit finite S and denominator classes
```

provided the subsequent completeness certificate covers that exact target and the pullback is exhaustive.

Hard rule:

```text
ELLIPTIC_INTEGRAL_POINTS_AUTOMATICALLY_CLOSE_QUARTIC=false
```

until the transfer theorem is proved.

### D. Certify the Mordell--Weil input

A complete integral-point proof requires a certified Mordell--Weil basis, not merely a rank statement or a generator found by search.

Verify/source-lock at least:

```text
rank = 1
torsion = Z/2
candidate free generator P = (-15,50) or corrected basis
T = (10,0)
full saturation / index certificate for the free generator
```

If the quoted generator is not proved to generate the full free part, replace it and record the exact index.

### E. Produce a complete integral-point certificate

Use a proof-capable exact method whose theorem/algorithm and software behavior are source-locked. Preferred routes:

1. Magma/Sage `IntegralPoints` or an equivalent implementation of a proven elliptic-logarithm/Cremona--Prickett--Siksek style algorithm;
2. a direct fully documented elliptic-logarithm/Baker reduction with reproducible bounds and exhaustive final enumeration;
3. a direct integral-points routine on the genus-one quartic, if its completeness theorem and exact model transfer are independently source-locked.

Required reproducibility surface:

```text
software name/version
exact curve/model
Mordell-Weil basis and saturation certificate
algorithm/theorem locator
all parameters/options
initial and reduced bounds
complete raw output or machine-readable certificate
independent finite checker of every returned point
```

Forbidden as completeness proof:

```text
bounded ellratpoints search
sampled height constants
"database says 7" without algorithmic certificate
unproved BSD/GRH assumptions
```

### F. Pull back every certified arithmetic point

Map every certified elliptic/S-integral point back through `psi`, including exceptional points, and determine the exact integral quartic set.

The paper claims

```text
(Y,Z) = (-1,+/-1), (1,+/-1), (11,+/-37)
```

but Stage31 must derive this list rather than assume it.

For every surviving quartic point record:

```text
branch I/II
p
q
prime condition
positivity/nondegeneracy
gcd/parity hypotheses
edges a,b,c
three face-square tests
space-square test
```

The claimed nondegenerate point `(p,q)=(11,71)` must be independently reconstructed and its failing third-face value checked by exact integer square-root arithmetic.

### G. Final certificate and independent checker

Produce at least:

```text
stages/stage31/31-01/source-lock.json
stages/stage31/31-01/birational-map.json
stages/stage31/31-01/integrality-transfer.md
stages/stage31/31-01/mordell-weil-certificate.json
stages/stage31/31-01/integral-points-certificate.json
stages/stage31/31-01/reconstruction-ledger.json
stages/stage31/31-01/result.md
stages/stage31/31-01/verify_stage31.py
```

Prefer an independent verifier that rebuilds the curve equations, map identities, returned point list, and cuboid square tests rather than simply calling the construction code.

### 31-01 direct-close conditions

All must hold:

```text
BIRATIONAL_MAP_EXPLICIT_AND_INVERTIBLE_ON_STATED_OPEN=true
EXCEPTIONAL_LOCUS_COMPLETE=true
INTEGRALITY_TRANSFER_PROVED=true
MW_BASIS_COMPLETE_AND_SATURATED=true
INTEGRAL_POINT_ALGORITHM_SOURCE_LOCKED=true
INTEGRAL_POINT_COMPLETENESS_CERTIFIED=true
QUARTIC_PULLBACK_EXHAUSTIVE=true
CUBOID_RECONSTRUCTION_EXHAUSTIVE=true
HIDDEN_CLASS1_PENDING_COUNT=0
```

If these hold, `Stage31-main-batch` skips fallback units and sets:

```text
NEXT_EXPECTED_COMMAND=Stage31-audit
```

---

# Fallback decomposition — activated only if 31-01-XL cannot legally close

These are not mandatory sequential stages. Only the unresolved leaf(s) are activated.

## Stage31-02 — BIRATIONAL_MAP_AND_INTEGRALITY_TRANSFER

Size: M/L

Use if map construction or denominator control is the first real wall.

Goal:

```text
explicit C <-> E map
+
complete exceptional locus
+
legal integral/S-integral transfer theorem
```

Exit either by closing the leaf or by exposing a strictly smaller exact arithmetic target.

## Stage31-03 — MW_BASIS_AND_COMPLETE_INTEGRALPOINTS

Size: L/XL

Use if the only remaining wall is the complete arithmetic enumeration.

Goal:

```text
certified MW basis/index/saturation
+
proof-capable IntegralPoints/elliptic-log certificate
+
complete target point set
```

A missing installed CAS is Class 2/tool infrastructure, not a mathematical theorem wall. Record an exact runnable certificate task rather than reclassifying it as Class 3.

## Stage31-04 — PULLBACK_AND_CUBOID_RECONSTRUCTION

Size: M

Use if the arithmetic point set is certified but the quartic/family reconstruction is not yet exhaustively audited.

Goal:

```text
all exceptional and ordinary pullbacks classified
prime-family branch ledger complete
all candidate square tests exact
```

## Stage31-05 — FINAL_CERTIFICATE_REPAIR

Size: S/M

Use only for reproducibility/certificate integration after the mathematics is already complete. This stage may not hide a mathematical gap behind a manifest.

---

## Stage31-06 — FINAL_HOSTILE_AUDIT_AND_CLOSE

Size: M/L
Owner: ChatGPT

Fresh audit must independently attack the entire load-bearing chain.

PASS is forbidden unless:

```text
SOURCE_SNAPSHOT_AMBIGUITY_COUNT=0
BIRATIONAL_FORMULA_UNVERIFIED_COUNT=0
EXCEPTIONAL_POINT_UNCLASSIFIED_COUNT=0
INTEGRALITY_GAP_COUNT=0
MW_INDEX_AMBIGUITY_COUNT=0
HEURISTIC_HEIGHT_BOUND_COUNT=0
UNPROVED_ANALYTIC_ASSUMPTION_COUNT=0
INTEGRAL_POINT_COMPLETENESS_GAP_COUNT=0
PULLBACK_MISSING_POINT_COUNT=0
CUBOID_RECONSTRUCTION_UNVERIFIED_COUNT=0
HIDDEN_CLASS1_PENDING_COUNT=0
```

Permitted final outcomes:

```text
A. CLOSED_CERTIFIED: Paper-E prime thin-family exclusion independently certified.
B. SOURCE_CLAIM_FALSE: an explicit counterexample/gap invalidates the claimed closure.
C. SMALLER_CLASS2: a strictly smaller exact CAS/model/certificate leaf remains.
D. CLASS3_EXPOSED: a genuinely new theorem is proven necessary after all finite work is exhausted.
```

Outcome C/D must identify the first missing statement exactly. "IntegralPoints unavailable" alone is not Class 3.

## Research-OS consequence

If outcome A closes the kernel, the post-Stage30 active portfolio loses one Class-2 kernel:

```text
K16-C2-EXT-E-INTEGRAL-CERTIFICATION -> CLOSED
```

This does not change `J12-PARAMETRIC` to GREEN merely by closing one thin family. The family is not a global parameterization of all endpoint candidates.

## Endpoint claim firewall

Always:

```text
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
THIN_FAMILY_CLOSURE_IMPLIES_GLOBAL_ENDPOINT_EMPTY=false
```
