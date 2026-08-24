# Stage33-03 absolute hypercohomology extension class

This note resolves

```text
R33-BR0B-ABSOLUTE-HYPERCOHOMOLOGY-EXTENSION-CLASS
L33-03-COMPUTE-ABSOLUTE-H2-UPIC-EXTENSION-CLASS-AND-PRIMARY-ORDERS
```

without asserting that the filtration splits.

## 1. Audited input

Write

```text
U = U_D = Z^14
T = Pic(Ubar)_tors = (Z/2)^2
F = Pic(Ubar)_free = Z^6
X_Q = Hom_cont(G_Q,Q/Z)
A = X_Q^14/<KAPPA_1,KAPPA_2>.
```

The audited inputs are

```text
H^3(G_Q,U)=0,
H^1(G_Q,Pic(Ubar))=Hom_cont(G_Q,T) direct-sum (Z/2)^5,
0 -> A -> H^2(G_Q,UPic(Ubar)) -> H^1(G_Q,Pic(Ubar)) -> 0,
```

with exact independent `d2_01` images `KAPPA_1,KAPPA_2`.

## 2. Torsion Postnikov classes

For a trivial `Z/2` summand of `T` and Z-free trivial `U`, change of rings gives

```text
Ext^2_{Z[G_Q]}(Z/2,U)=H^1(G_Q,U/2U).
```

Since `H^1(G_Q,U)=0`, the integral Bockstein

```text
H^1(G_Q,U/2U) -> H^2(G_Q,U)[2]
```

is injective. Hence the exact `KAPPA` images determine the two torsion Postnikov classes uniquely:

```text
lambda_1=v_1*chi_-1,
lambda_2=v_2*chi_-1,
```

with independent `v_1,v_2 in (F2)^14`.

## 3. Hidden extension / doubling map

For `alpha=(alpha_1,alpha_2) in H^1(G_Q,T)`, Yoneda composition gives

```text
delta(alpha)
 = [alpha_1 cup lambda_1 + alpha_2 cup lambda_2]
 in H^2(G_Q,U/2U)/<red(KAPPA_1),red(KAPPA_2)>.
```

Milne, *Arithmetic Duality Theorems*, I.4 Cor.4.17 gives `H^3(G_Q,U)=0`, so the target is exactly `A/2A`.

For a quadratic character `alpha`, the Bockstein for

```text
0 -> Z/2 -> Z/4 -> Z/2 -> 0
```

is `alpha -> alpha cup alpha`, and the standard identity gives

```text
alpha cup alpha = alpha cup chi_-1.
```

Therefore

```text
delta(alpha_1,alpha_2)
 = [v_1*alpha_1+v_2*alpha_2] in A/2A.
```

This determines the extension class itself; no splitting is claimed.

## 4. Quadratic-family primary orders

For every nonzero right-filtration quadratic class,

```text
minimal lift order = 2 if delta=0,
minimal lift order = 4 if delta!=0.
```

No such lift has order above four. Independence of `v_1,v_2` gives

```text
[alpha_j] in span_F2([chi_-1]) inside X_Q/2X_Q, j=1,2
```

as the exact `delta=0` criterion. For `alpha_j=chi_d`, Serre, *Topics in Galois Theory*, Ch.1 sec.1.2 Thm.1.2.4 supplies the cyclic-quartic/sum-of-two-squares arithmetic adapter; equivalently `(d,-1)` is `0` or `(-1,-1)` in `Br(Q)[2]`.

## 5. Five finite free classes — hostile direct verification

The production draft initially reasoned that the torsion contribution already has rank two and the total finite `rank(d2_11)=2`, so the five `H^1(V4,F)` classes must map to zero. That rank inference is not valid by itself because a nonzero free-side image could lie in the same two-dimensional target subspace.

The hostile audit therefore computes these five transgressions individually from the exact Smith complex and source-locked Picard action. The tensor-product periodic resolution stores its H1 blocks in the order `ct` then `cc`; the corrected audit adapter explicitly respects that convention.

Focused verifier:

```text
workflow_run=32711989526
artifact_id=9514467883
artifact_zip_sha256=130698786259ad140ff86d0bff506a40a68227ee31ef3762a4b20ad7b1e12ace
audit-free-d2-11-direct.json canonical_sha256=
90113c462f5cf028fd8d0ef29a21ab57ca4e01840082f94a47284cba109c12d6
```

It gives

```text
PICU-FREE-H1-1 -> 0 in H^3(V4,U)
PICU-FREE-H1-2 -> 0 in H^3(V4,U)
PICU-FREE-H1-3 -> 0 in H^3(V4,U)
PICU-FREE-H1-4 -> 0 in H^3(V4,U)
PICU-FREE-H1-5 -> 0 in H^3(V4,U)
free image rank = 0
torsion image rank = 2
combined direct image rank = 2
```

The combined rank agrees with the independently audited total finite rank. Since `H^2(V4,UPic)=(Z/2)^33`, all five free classes have finite order-two lifts, and their inflated absolute lifts have order two.

## 6. Audited closure state

The extension class and the primary orders are now exact parametrically:

```text
FILTRATION_EXTENSION_SPLIT_CLAIMED=false
FILTRATION_EXTENSION_CLASS_EXACT=true
KERNELS_COKERNELS_TORSION_EXACT=true
OPEN_ALGEBRAIC_Q_DEFINED_CLASS_INVENTORY_COMPLETE=true
BR0B_ALL_PRIMARY_CLASSES_ACCOUNTED=true
BR0B=DISCHARGED
UNRESOLVED_UNKNOWN_IN_SCOPE=0
HOSTILE_AUDIT=PASS_AFTER_DIRECT_FREE_D2_11_MATERIALIZATION_AND_ABSOLUTE_EXTENSION_CLASS_VERIFICATION
UNIT_STATUS=CLOSED
UNIT_CLOSED=true
```

Stage33-06 is not released by this unit alone because Stage33-04 is also a required prerequisite.
