# Stage33-03 hostile re-audit — BR0B absolute-Galois UPic / Gersten

```text
STAGE33_UNIT=33-03
PR=1361
PRODUCTION_HEAD=cc6c383b9a8ee3f6c04f649385db535feb2d055d
PRODUCTION_WORKFLOW_RUN=32709285338
PRODUCTION_WORKFLOW_CONCLUSION=success
PRODUCTION_ARTIFACT_ID=9513603089
PRODUCTION_ARTIFACT_ZIP_SHA256=cf95be77ae227227f8f2f2b478a54a4c38d82cc242d6c4a293d63490eb533c07
FOCUSED_AUDIT_WORKFLOW_RUN=32711989526
FOCUSED_AUDIT_ARTIFACT_ID=9514467883
FOCUSED_AUDIT_ARTIFACT_ZIP_SHA256=130698786259ad140ff86d0bff506a40a68227ee31ef3762a4b20ad7b1e12ace
AUDIT_VERDICT=PASS_AFTER_DIRECT_FREE_D2_11_MATERIALIZATION_AND_ABSOLUTE_EXTENSION_CLASS_VERIFICATION
UNIT_STATUS=CLOSED
UNIT_CLOSED=true
BR0B=DISCHARGED
UNRESOLVED_UNKNOWN_IN_SCOPE=0
STAGE33_PROGRESS=3/11
33-06_RELEASED=false
```

## Previously accepted prefix

The prior hostile audit remains authoritative for the exact prefix:

- `U_D ~= Z^14` with trivial absolute `G_Q` action;
- `Pic(Ubar) ~= Z^6 direct-sum (Z/2)^2`;
- odd-primary contribution `Hom_cont(G_Q,Q/Z)_odd^14` retained exactly;
- `H^2(V4,UPic) ~= (Z/2)^33` and `H^1(V4,UPic)=0`;
- finite transgression ranks `(rank d2_01,rank d2_11)=(2,2)`;
- `H^3(G_Q,U_D)=0` by Milne, *Arithmetic Duality Theorems*, I.4 Cor.4.17;
- `H^1(G_Q,Pic(Ubar)) = Hom_cont(G_Q,(Z/2)^2) direct-sum (Z/2)^5`.

Hence the exact filtration is

```text
0
 -> A = X_Q^14/<KAPPA_1,KAPPA_2>
 -> Br_a(U)=H^2(G_Q,UPic(Ubar))
 -> Hom_cont(G_Q,(Z/2)^2) direct-sum (Z/2)^5
 -> 0,
X_Q=Hom_cont(G_Q,Q/Z).
```

The previous audit correctly refused closure because the middle extension class and the primary orders of right-filtration lifts had not yet been determined.

## Absolute extension class

The repair materializes the two torsion Postnikov classes as

```text
lambda_1 = v_1*chi_-1,
lambda_2 = v_2*chi_-1,
```

with independent `v_1,v_2 in (F2)^14`, recovered from the exact `d2_01` images through the injective integral Bockstein. For

```text
alpha=(alpha_1,alpha_2) in Hom_cont(G_Q,(Z/2)^2),
```

the hidden doubling map is

```text
delta(alpha_1,alpha_2)
 = [v_1*alpha_1 + v_2*alpha_2] in A/2A.
```

Using `H^3(G_Q,Z)=0`, the coefficient Bockstein identifies the quadratic cup-square with the class in `X_Q/2X_Q`; the Serre cyclic-quartic criterion is used only as an arithmetic adapter for the resulting squareclass condition. No splitting of the filtration is asserted.

For every nonzero quadratic-family right class, the minimal lift order is exactly

```text
2 if delta=0,
4 if delta!=0,
```

and no such lift has order above four.

## Hostile check of the five free H1 classes

The production proof originally argued that the five `H^1(V4,Pic(Ubar)_free)` classes have `d2_11=0` because the torsion contribution already has rank two and the total `d2_11` rank is two. That rank argument alone is insufficient: a nonzero free-side image could lie inside the same two-dimensional target image.

The hostile re-audit therefore did not accept that inference. It added an independent direct chain-level verifier using the exact Smith complex and source-locked Picard action. A first verifier run failed only because the historical JSON field names follow the tensor-resolution block order `ct` then `cc`; the corrected adapter was checked against all five cocycle relations before rerun.

Focused run `32711989526` then computed every free-side transgression directly. The exact certificate is

```text
audit-free-d2-11-direct.json
canonical_sha256=90113c462f5cf028fd8d0ef29a21ab57ca4e01840082f94a47284cba109c12d6
```

and gives

```text
PICU-FREE-H1-1: d2_11 = 0 in (Z/2)^14
PICU-FREE-H1-2: d2_11 = 0 in (Z/2)^14
PICU-FREE-H1-3: d2_11 = 0 in (Z/2)^14
PICU-FREE-H1-4: d2_11 = 0 in (Z/2)^14
PICU-FREE-H1-5: d2_11 = 0 in (Z/2)^14
free_d2_11_image_rank = 0
torsion_d2_11_image_rank = 2
combined_direct_d2_11_image_rank = 2
```

The combined direct rank exactly matches the independently audited total rank. Therefore all five finite free classes do have order-two finite lifts in `H^2(V4,UPic)=(Z/2)^33`, and their inflated absolute lifts have order two.

## Closure decision

With the direct free-side check replacing the invalid rank-only inference, the extension class and all primary lift orders required by Stage33-03 are exact parametrically. The following closure gates are accepted:

```text
EXPLICIT_GALOIS_ACTION_CERTIFIED=true
UPIC_GERSTEN_MAPS_CERTIFIED=true
KERNELS_COKERNELS_TORSION_EXACT=true
UNIT_KERNEL_ABSOLUTE_GALOIS_INFLATION_CHARACTER_TERMS_EXACT=true
NO_UNJUSTIFIED_TWO_PRIMARY_RESTRICTION=true
QBAR_TO_Q_DESCENT_ADAPTER_CERTIFIED=true
OPEN_ALGEBRAIC_Q_DEFINED_CLASS_INVENTORY_COMPLETE=true
BR0B_ALL_PRIMARY_CLASSES_ACCOUNTED=true
BR0B=DISCHARGED
UNRESOLVED_UNKNOWN_IN_SCOPE=0
HOSTILE_AUDIT=PASS
```

Therefore `Stage33-03` is **CLOSED**.

## Firewalls and DAG state

This closure gives no endpoint theorem and no Perfect Cuboid existence/nonexistence result. `Stage33-06` is **not** released by this branch alone because its other prerequisite, `Stage33-04`, is an independent unit and is not CLOSED in the authoritative merged state consumed here.

```text
THEOREM_CREDIT=Milne_H3_VANISHING_AND_SERRE_ADAPTER_ONLY
ENDPOINT_CREDIT=false
BRAUER_MANIN_OBSTRUCTION_CLAIM=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
MERGE_ALLOWED=true
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```
