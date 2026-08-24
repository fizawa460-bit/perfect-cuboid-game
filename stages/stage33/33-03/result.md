# Stage33-03 — hostile-audited BR0B exact prefix

```text
STAGE33_UNIT=33-03
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
BR0B=OPEN
BR0B_ALL_PRIMARY_CLASSES_ACCOUNTED=false
OPEN_ALGEBRAIC_Q_DEFINED_CLASS_INVENTORY_COMPLETE=false
KERNELS_COKERNELS_TORSION_EXACT=false
UNRESOLVED_UNKNOWN_IN_SCOPE=1
AUDIT_VERDICT=PASS_EXACT_PREFIX_REJECT_PREMATURE_BR0B_CLOSURE_ON_ABSOLUTE_EXTENSION_CLASS
```

## Audited exact data

The following production outputs from workflow `32703426900` / artifact `9511501245`
(zip SHA256 `09e311369d0c02f0d8322b3543163b11454a81183d6a6aa46d688f26f68136ff`)
are accepted.

```text
U_D = Z^14 with trivial absolute G_Q action
Pic(Ubar) = Z^6 + (Z/2)^2

Pic(Ubar)_free V4 multiplicities:
  (+,+)=0
  (+,-)=3
  (-,+)=2
  (-,-)=1

H^2(Q,UPic(Ubar))_odd
  = Hom_cont(G_Q,Q/Z)_odd^14

H^2(V4,UPic(Ubar)) = (Z/2)^33
H^1(V4,UPic(Ubar)) = 0
rank_F2(d2_01) = 2
rank_F2(d2_11) = 2

H^3(G_Q,U_D) = 0
H^1(G_Q,Pic(Ubar))
  = Hom_cont(G_Q,(Z/2)^2) direct-sum (Z/2)^5
```

Milne, *Arithmetic Duality Theorems*, I.4 Cor.4.17 is accepted for
`H^3(G_Q,Z)=0`, hence the absolute right transgression has zero target.

The audit accepts the resulting exact filtration

```text
0
 -> X_Q^14 / <KAPPA_1,KAPPA_2>
 -> H^2(G_Q,UPic(Ubar))
 -> Hom_cont(G_Q,(Z/2)^2) direct-sum (Z/2)^5
 -> 0
```

with `X_Q=Hom_cont(G_Q,Q/Z)` and the two exact visible-V4 quadratic
relations from `d2-01-image.json`.

## Hostile-audit correction

The generated `br0b-all-primary-inventory.json` also states

```text
filtration_extension_split_claimed=false
```

so the middle absolute hypercohomology group has not yet been determined
as an abelian group. The unresolved extension can change primary orders
of lifts from the right filtration. Therefore it is not yet valid to set

```text
KERNELS_COKERNELS_TORSION_EXACT=true
OPEN_ALGEBRAIC_Q_DEFINED_CLASS_INVENTORY_COMPLETE=true
BR0B_ALL_PRIMARY_CLASSES_ACCOUNTED=true
BR0B=DISCHARGED
UNRESOLVED_UNKNOWN_IN_SCOPE=0
```

under the frozen Stage33-03 closure contract.

## Exact residual

```text
RESIDUAL_KERNEL=R33-BR0B-ABSOLUTE-HYPERCOHOMOLOGY-EXTENSION-CLASS
LEAF_ID=L33-03-COMPUTE-ABSOLUTE-H2-UPIC-EXTENSION-CLASS-AND-PRIMARY-ORDERS
CLASS=2
NEW_THEOREM_REQUIRED=false
```

The next production leaf must compute the absolute extension class (or
prove a splitting strong enough to determine the full group) and certify
the primary order of the right-filtration lifts.

```text
THEOREM_CREDIT=Milne_H3_VANISHING_ONLY
ENDPOINT_CREDIT=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
33-06_RELEASED=false
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```
