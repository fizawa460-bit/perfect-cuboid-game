# Stage30-04 — finite Q(i)-level equivariant identification search

```text
STAGE=30
SUBSTAGE=30-04
OWNER=ChatGPT/main-batch
STATUS=SUBMITTED_PENDING_AUDIT
```

## Exact finite result

Starting from the audited Stage30-02C concrete actions, the search was recomputed from first principles rather than importing an abstract `S4` label.

Arrangement action sets:

```text
Omega_arr_4={A1,A2,A3,C}
Omega_arr_3={B1,B2,B3}
```

Modular action sets:

```text
Omega_mod_4={h0,h1,h2,h3}
Omega_mod_3={v0,v1,v2}
```

The modular sets are reconstructed from `PSL2(Z/4)` itself:

```text
V_mod=ker(PSL2(Z/4)->PSL2(F2)), |V_mod|=4
Omega_mod_3=V_mod-{1}
Omega_mod_4={the four order-6 complements of V_mod}
```

All `4! * 3! = 144` pairs of bijections were exhaustively tested. A pair survives exactly when transport through the faithful four-point action induces one modular group element for every arrangement group element and the same induced group identification is equivariant on the three-point action.

Exact output:

```text
EXHAUSTIVE_4x3_BIJECTION_SEARCH=PASS
SURVIVING_EQUIVARIANT_IDENTIFICATION_COUNT=24
C_IMAGE_MULTIPLICITIES=h0:6,h1:6,h2:6,h3:6
```

Thus the finite action problem closes, but it does **not** select a unique cuboid/modular identification. The 24 surviving identifications form the expected relabelling torsor at the finite-action level. In particular, the arrangement rational-liftable `S3` (the stabilizer of `C` in the four-point action) is sent to the stabilizer of `f(C)`; each of the four modular complement points occurs for exactly six candidates.

A generator-convention representative exists:

```text
qicand-22
s_arr -> S_mod
t_arr -> T_mod
A1,A2,A3,C -> h3,h2,h0,h1
B1,B2,B3   -> v0,v1,v2
```

This representative is a convention-level finite witness only. It is not promoted to the source-geometric `Q(i)` adapter merely because the generator labels match.

## Reclassification

```text
L30-QI-FINITE-EQUIVARIANT-SEARCH
  = CLASS1_DISCHARGED_EXHAUSTIVE_24_CANDIDATES

L30-COMMON-GEOMETRIC_OR_MODULI-ANCHOR
  = CLASS2_30-05
```

No new Class-3 theorem requirement is exposed by this finite search.

## Reproducibility

Committed artifacts:

```text
build_equivariant_candidates.py
equivariant-candidates.json
verify_equivariant_candidates.py
```

The independent verifier re-enumerates `SL2(Z/4)`, forms `PSL2(Z/4)`, recomputes `V_mod`, all four order-6 complements, both concrete permutation groups, and the complete 144-pair search. Local execution produced:

```text
EXHAUSTIVE_4x3_BIJECTION_SEARCH=PASS
SURVIVING_EQUIVARIANT_IDENTIFICATION_COUNT=24
C_IMAGE_MULTIPLICITIES=h0:6,h1:6,h2:6,h3:6
SOURCE_GEOMETRIC_ANCHOR_PROVED=false
```

## Firewalls

```text
FINITE_ACTION_EQUIVARIANCE=VERIFIED_SUBMISSION
SOURCE_GEOMETRIC_QI_ADAPTER_PROVED=false
QI_EQUIVARIANCE_VERIFIED=false
Q_GALOIS_COCYCLE_VERIFIED=false
Q_DESCENT_CREDIT=false
DEFECT_ELIMINATION_COUNT=0
R29_KUM5_DISCHARGED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

Stage30-05 must now supply an actual common cuboid/moduli geometric or moduli anchor over `Q(i)`. The finite `S4` actions alone cannot choose among the 24 candidates.

```text
AUDIT_REQUIRED=true
AUDIT_VERDICT=PENDING
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_ITEM_AFTER_AUDIT_PASS=30-05_COMMON_QI_GEOMETRIC_OR_MODULI_ANCHOR
NEXT_EXPECTED_COMMAND=Stage30-audit
```
