# Stage30-07 hostile audit

```text
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPRO_SCOPE_CLARIFICATION
```

The eight-defect transport was reconstructed independently from the frozen Stage29 K8 description and audited Stage30 source action.

## Mathematical verification

For

```text
A=[[a,b],[c,a]] in sl2(F2),
kappa(A)=I+4A mod 8,
```

the submitted adapter

```text
phi(A)=(a+b,a+c,a) in F2^3_(u,v,w)
```

is correct.  The basis derivation is compatible with the source X(8) action:

```text
E12 -> flip u,
E21 -> flip v,
I   -> flip {u,v,w}.
```

Fresh enumeration of all eight A and all residual SL2(F2) conjugates gives exactly the stored endpoint b-sign patterns.  The residual PSL2(Z/4) action factors through S3 and the ordinary orbit sizes are the four Hamming-weight layers

```text
1,3,3,1.
```

The submitted independent verifier checks all 24 x 8 equivariance pairs, all stabilizers, the frozen Task-A ID convention, and the stored eight rows.  No row mismatch was found.

## Marked arithmetic classes

The already-audited sigma action on K8 is trivial.  Since K8 is abelian, the marked twisted equivalence relation is equality.  Therefore the four ordinary S4 orbits do not collapse the marked arithmetic states:

```text
MARKED_Q_DESCENT_CLASS_COUNT=8
MARKED_CLASSES_ARE_SINGLETONS=true
DEFECT_ELIMINATION_COUNT=0
```

The Stage29 ordinary label `identity` is correctly disambiguated: it denotes A=I, hence kappa=5I mod 8, not the K8 group identity.

## Scope firewall

```text
K8_EQUALS_V_MOD=false
C_SIGMA_EQUALS_KAPPA=false
ORDINARY_S4_ORBIT_EQUALS_MARKED_ARITHMETIC_CLASS=false
PHYSICAL_ENDPOINT_EXCLUSION_PROVED=false
R29_KUM5_DISCHARGED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

30-07 transports and classifies all eight defects but eliminates none.  Stage30-08 must now state exactly what the completed action/cocycle/defect adapter says on the physical endpoint open and decide whether R29-KUM5 is discharged or leaves a smaller residual leaf.

## Bounded reproducibility-scope clarification

The prior 30-06C reproduction manifest SHA-pinned the mutable `stages/stage30/controller.json`.  Therefore its full manifest mode is a snapshot certificate of the 30-06C audited state and is expected to fail after later stages legitimately advance the controller.  This does not affect the 30-07 mathematics, whose verifier reconstructs its own finite data and does not call the 30-06C verifier.  Future final reproducibility should not treat mutable controller state as a permanent mathematical input hash.

```text
AUDIT_REQUIRED=false
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=30-08_PHYSICAL_ENDPOINT_ADAPTER
NEXT_EXPECTED_COMMAND=Stage30-main-batch
```
