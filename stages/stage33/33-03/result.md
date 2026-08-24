# Stage33-03 — BR0B absolute-Galois UPic / Gersten final audited result

```text
STAGE33_UNIT=33-03
PR=1361
UNIT_STATUS=CLOSED
UNIT_CLOSED=true
DOWNSTREAM_RELEASED=false
BR0B=DISCHARGED
BR0B_ALL_PRIMARY_CLASSES_ACCOUNTED=true
OPEN_ALGEBRAIC_Q_DEFINED_CLASS_INVENTORY_COMPLETE=true
KERNELS_COKERNELS_TORSION_EXACT=true
UNRESOLVED_UNKNOWN_IN_SCOPE=0
HOSTILE_AUDIT=PASS_AFTER_DIRECT_FREE_D2_11_MATERIALIZATION_AND_ABSOLUTE_EXTENSION_CLASS_VERIFICATION
FILTRATION_EXTENSION_SPLIT_CLAIMED=false
FILTRATION_EXTENSION_CLASS_EXACT=true
STAGE33_PROGRESS=3/11
STAGE33_06_RELEASED=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Exact BR0B inventory

Let `X_Q=Hom_cont(G_Q,Q/Z)`. The audited compactification complex gives

```text
U_D ~= Z^14, with trivial absolute G_Q action,
Pic(Ubar) ~= Z^6 direct-sum (Z/2)^2.
```

The odd-primary part is retained parametrically as

```text
H^2(G_Q,UPic(Ubar))_odd ~= X_Q,odd^14.
```

The finite quotient calculations are exact:

```text
H^2(V4,UPic) = (Z/2)^33,
H^1(V4,UPic) = 0,
(rank d2_01, rank d2_11) = (2,2).
```

Milne, *Arithmetic Duality Theorems*, I.4 Cor.4.17 gives

```text
H^3(G_Q,U_D)=0,
```

and the absolute right filtration is

```text
H^1(G_Q,Pic(Ubar))
 = Hom_cont(G_Q,(Z/2)^2) direct-sum (Z/2)^5.
```

Thus the exact filtration is

```text
0
 -> A = X_Q^14/<KAPPA_1,KAPPA_2>
 -> Br_a(U)=H^2(G_Q,UPic(Ubar))
 -> Hom_cont(G_Q,(Z/2)^2) direct-sum (Z/2)^5
 -> 0.
```

## Exact hidden extension

The two torsion Postnikov classes are

```text
lambda_1=v_1*chi_-1,
lambda_2=v_2*chi_-1,
```

with independent

```text
v_1=[1,0,1,0,0,0,0,0,1,1,1,1,0,0]
v_2=[0,0,0,1,0,0,1,1,1,0,1,1,0,0].
```

For `alpha=(alpha_1,alpha_2) in Hom_cont(G_Q,(Z/2)^2)`, the absolute extension is represented by

```text
delta(alpha_1,alpha_2)
 = [v_1*alpha_1+v_2*alpha_2] in A/2A.
```

No split is asserted. For every nonzero quadratic-family right class, the exact minimal lift order is

```text
2 if delta=0,
4 if delta!=0,
```

with no order above four. Serre, *Topics in Galois Theory*, Ch.1 sec.1.2 Thm.1.2.4 is used only as the cyclic-quartic/squareclass adapter for the resulting criterion.

## Direct hostile verification of the five finite free classes

The production proof originally used a rank-only argument to assert that the five `H^1(V4,Pic(Ubar)_free)` classes have zero `d2_11`. Hostile audit rejected that inference as insufficient and computed the five images individually at chain level.

Focused verifier evidence:

```text
workflow_run=32711989526
artifact_id=9514467883
artifact_zip_sha256=130698786259ad140ff86d0bff506a40a68227ee31ef3762a4b20ad7b1e12ace
audit_free_d2_11_certificate_sha256=90113c462f5cf028fd8d0ef29a21ab57ca4e01840082f94a47284cba109c12d6
```

Exact result:

```text
free class 1: d2_11=0
free class 2: d2_11=0
free class 3: d2_11=0
free class 4: d2_11=0
free class 5: d2_11=0
free-side image rank=0
torsion-side image rank=2
combined direct image rank=2
```

Hence all five finite free classes have order-two absolute lifts. The direct combined rank agrees with the independently audited total finite rank.

## Closure

All eleven Stage33-03 closure criteria now pass. `R29-BR0B` is discharged and no unknown remains in the Stage33-03 scope.

Stage33 closed-unit progress becomes `3/11`. This does **not** release Stage33-06 yet: the DAG requires both `33-03` and `33-04` CLOSED, and this branch does not consume or promote the independent unmerged Stage33-04 state.

```text
THEOREM_CREDIT_SCOPE=Milne_H3_VANISHING_PLUS_SERRE_ADAPTER_ONLY
ENDPOINT_CREDIT=false
BRAUER_MANIN_OBSTRUCTION_CLAIM=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```
