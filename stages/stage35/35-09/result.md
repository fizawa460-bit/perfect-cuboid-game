# Stage35 35-09 — decision certificate

```text
UNIT=35-09_DECISION_CERTIFICATE_OR_PARK
CLASSIFICATION=CLASS3_RETAINED_WITH_SHARPER_MINIMAL_THEOREM
AUDIT_STATUS=REPAIR_AFTER_HOSTILE_AUDIT_5100964131_NOT_STAGE_CLOSE
TARGET=T35-R3-PHYS-EMPTY
R29_FIB2_CLOSED=false
J12_PARAMETRIC_CLOSED=false
STAGE35_CLOSED=false
NEW_THEOREM_CREDIT=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

Stage35 materially shrinks the Stage29 moving-fiber wall but does not solve it.

The retained receiver can be attacked through one exact `Q`-defined full-endpoint genus-5 fibration

```text
TS-S-R3-Q1
t=(e+d)/z in Q, t>1.
```

Every physical endpoint enters this family, the point-level inverse reconstruction is exact, and every rational physical parameter gives a smooth fiber. The family is a diagonal intersection of three quadrics with five explicit elliptic quotient Jacobians over `Q(t)`.

The minimum remaining theorem is now only

```text
T35-R3-PHYS-EMPTY:
for every rational t>1, U_t(Q)=empty.
```

Existing source-locked fixed-fiber covering/elliptic-Chabauty methods and generic `Q(t)` Mordell--Weil/section methods do not supply the missing quantifier: they do not exclude rational points appearing only after specialization. Stage35 makes no global literature-absence claim. The negative result is only that the source-locked material checked in 35-06 contains no applicable uniform closure theorem. Broad external literature is not declared exhausted.

No exact globally exhaustive reduction to finitely many fibers was obtained from the current exact inputs, so `S34-W02` remains locked and bounded fiber computation remains non-credit-bearing.

Hostile audit `5100964131` accepted the central selected-route mathematics but required four bounded repairs: correct the 35-08 cubic-RHS-versus-Weierstrass discriminant terminology, add one lightweight aggregate 35-01--35-09 verifier wired to PR CI, update the PR body to the current research surface, and bound the literature-negative claim. These repairs do not promote receiver or theorem credit.

The re-audit execution authority is `stages/stage35/verify_stage35_35_01_to_09.py` through `.github/workflows/stage35-35-01-to-09-audit.yml` at the exact PR head.
