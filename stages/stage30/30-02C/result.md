# Stage30-02C — Codex Task A exact finite action certificates

```text
TASK=Codex-A
SUBSTAGE=30-02C
SCOPE=FINITE_GROUP_ACTION_TABLES_ONLY
STATUS=READY_FOR_STAGE30_AUDIT
```

## Result

Task A completed with exact integer, rational, and modular arithmetic only.  It
materializes the two frozen concrete actions independently.  It does not
identify them and grants no `Q(i)/Q` descent credit.

### Arrangement action

The displayed dual matrices were applied directly to the seven frozen line
forms.  They recover exactly

```text
s_arr=(A1 A2)(B1 B2)
t_arr=(A1 A2 A3 C)(B1 B3).
```

Their permutation closure has order 24.  On the frozen action sets it is
transitive with

```text
Omega_arr_4 size=4, point-stabilizer order=6
Omega_arr_3 size=3, point-stabilizer order=8.
```

The subgroup preserving the rational-lift orbit split has order 6, consistently
with the frozen upstream `Q`-liftable coordinate-permutation subgroup.  All 24
arrangement elements and their seven-label images are recorded in
`action-tables.json`.

The chosen generators satisfy the concrete relations

```text
ord(s_arr)=2
ord(t_arr)=4
ord(s_arr*t_arr)=3.
```

These relations are reported as properties of the enumerated action, not as an
imported abstract presentation.

### Modular action

The construction enumerates all determinant-one matrices over `Z/4`:

```text
|SL2(Z/4)|=48.
```

Each projective class is normalized to the lexicographically smaller row-major
tuple among `M` and `-M modulo 4`.  The resulting quotient ledger has

```text
|PSL2(Z/4)|=24
<S_mod,T_mod>=PSL2(Z/4)
ord(S_mod)=2
ord(T_mod)=4
ord(S_mod*T_mod)=3.
```

Reduction modulo 2 is computed for every one of the 24 canonical classes.  Its
kernel is normal and has order 4.  Direct multiplication shows that it is a
Klein four group.  Therefore

```text
|Omega_mod_3|=|V_mod-{1}|=3.
```

Every 6-element subset of the concrete 24-element group was tested for the
subgroup, trivial-intersection, and product conditions.  Exactly four
complements satisfy

```text
|H|=6,
H intersect V_mod={1},
H*V_mod=G_mod.
```

Thus

```text
|Omega_mod_4|=4.
```

Conjugation by `S_mod,T_mod` on all three kernel points and all four complement
subgroups is written explicitly in `action-tables.json`.  Full-group orbits and
stabilizer element lists are written in `orbit-stabilizer.json`; the
orbit-stabilizer products are `3*8=24` and `4*6=24` on both sides.

## Independent checker

`verify_actions.py` does not call the construction script.  It independently:

1. recomputes the two arrangement generator permutations from the matrices and
   line forms;
2. regenerates their 24-element permutation closure;
3. re-enumerates `SL2(Z/4)` and the projective quotient;
4. re-enumerates all order-6 complements from 6-element subsets;
5. compares every certified generator action;
6. checks every listed orbit and stabilizer;
7. fails closed on missing/duplicate IDs, malformed action data, or any forbidden
   descent/existence claim.

Checker output:

```text
ARRANGEMENT_GENERATORS=PASS
ARRANGEMENT_GROUP_ORDER=24
ARRANGEMENT_4_PLUS_3_ACTION=PASS
MODULAR_PROJECTIVE_GROUP_ORDER=24
MODULAR_GENERATORS=PASS
MODULAR_REDUCTION_KERNEL_ORDER=4
MODULAR_OMEGA3_COUNT=3
MODULAR_OMEGA4_COUNT=4
MODULAR_ACTION_TABLES=PASS
ORBIT_STABILIZER_CERTIFICATE=PASS
TASK_A_Q_DESCENT_CREDIT=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Scope firewall

`D4` and the eight `K8` states are carried only as frozen labels.  `D4` is not
treated as an element of `G_mod`.  This result does not construct an
arrangement/modular identification, does not certify `Q(i)` equivariance, does
not derive a Galois cocycle, and does not eliminate any defect.  Those claims
remain downstream of the required Stage30 audits.

```text
CODEX_TASK=A
INPUT_SOURCE_LOCK_COMPLETE=true
EXACT_ARITHMETIC_ONLY=true
OBJECT_COVERAGE_COMPLETE=true
CHECKER_PRESENT=true
CHECKER_PASS=true
UNRESOLVED_ASSUMPTION_COUNT=0
NEW_THEOREM_ASSUMED=false
TASK_A_VERDICT=PASS_FINITE_ACTION_CERTIFICATE_READY_FOR_STAGE30_AUDIT
TASK_A_Q_DESCENT_CREDIT=false
QI_EQUIVARIANT_IDENTIFICATION_CLAIM=false
DEFECT_ELIMINATION_COUNT=0
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
