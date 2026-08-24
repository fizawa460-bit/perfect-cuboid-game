# Stage33-03 hostile audit — BR0B absolute-Galois UPic / Gersten

```text
STAGE33_UNIT=33-03
PR=1361
AUDITED_FUNCTIONAL_HEAD=1d12fbc74db876c704889a9d11f89165a8e5eaa9
WORKFLOW_RUN=32703426900
WORKFLOW_CONCLUSION=success
ARTIFACT_ID=9511501245
ARTIFACT_ZIP_SHA256=09e311369d0c02f0d8322b3543163b11454a81183d6a6aa46d688f26f68136ff
AUDIT_VERDICT=PASS_EXACT_PREFIX_REJECT_PREMATURE_BR0B_CLOSURE_ON_ABSOLUTE_EXTENSION_CLASS
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
BR0B=OPEN
STAGE33_PROGRESS=2/11
```

## Accepted exact prefix

The audit independently checked the uploaded certificate hashes, the integral V4 actions, and the relevant cohomological reductions.

Accepted facts:

- `U_D = ker(Div_D -> Pic(Sbar)) ~= Z^14`, with trivial absolute `G_Q` action because the source-locked action factors through `Gal(Q(i,sqrt(2))/Q)=V4` and both generators act identically on the unit lattice.
- `Pic(Ubar) ~= Z^6 + (Z/2)^2`; the free V4 character multiplicities are `(+,+)=0,(+,-)=3,(-,+)=2,(-,-)=1`, and the full `(Z/2)^2` torsion is fixed.
- The Stage32 primitive Picard basis bridge is unimodular with determinant `-1`.
- The odd-primary contribution is retained, not discarded: `H^2(Q,UPic(Ubar))_odd ~= Hom_cont(G_Q,Q/Z)_odd^14`.
- Finite V4 hypercohomology is exact: `H^2(V4,UPic(Ubar)) ~= (Z/2)^33` and `H^1(V4,UPic(Ubar))=0`.
- The finite transgression ranks are exactly `(rank d2_01, rank d2_11)=(2,2)`.
- The two `d2_01` image vectors are independent over `F2`.
- Milne, *Arithmetic Duality Theorems*, I.4 Cor.4.17 gives `H^3(G_Q,Z)=0`; hence `H^3(G_Q,U_D)=0` and the absolute `d2_11` target is zero.
- Independent integral recomputation of the free part gives `H^1(V4,Z^6) ~= (Z/2)^5`, so `H^1(G_Q,Pic(Ubar)) ~= Hom_cont(G_Q,(Z/2)^2) direct-sum (Z/2)^5`.

The resulting spectral-sequence filtration is therefore accepted as exact:

```text
0
 -> X_Q^14 / <KAPPA_1,KAPPA_2>
 -> H^2(G_Q,UPic(Ubar))
 -> Hom_cont(G_Q,(Z/2)^2) direct-sum (Z/2)^5
 -> 0,
```

where `X_Q = Hom_cont(G_Q,Q/Z)` and the two visible quadratic `KAPPA` relations are source-locked by `d2-01-image.json`.

## Closure claim rejected

The final generated inventory simultaneously records

```text
filtration_extension_split_claimed=false
```

while asserting

```text
KERNELS_COKERNELS_TORSION_EXACT=true
OPEN_ALGEBRAIC_Q_DEFINED_CLASS_INVENTORY_COMPLETE=true
BR0B_ALL_PRIMARY_CLASSES_ACCOUNTED=true
BR0B=DISCHARGED
UNRESOLVED_UNKNOWN_IN_SCOPE=0
```

Those assertions cannot all be true under the frozen Stage33-03 closure contract.

Knowing the two associated graded pieces and both edge differentials does not determine the middle abelian group. The unresolved extension can change the primary order of lifts from the right filtration; in particular an order-two graded class need not have an order-two lift. Therefore the absolute `H^2(G_Q,UPic(Ubar))` group law/torsion inventory, and consequently the complete Q-defined BR0B class inventory required downstream, are not yet exact.

The finite V4 extension was computed exactly; the unresolved object is specifically the **absolute** extension involving the infinite character families.

## Exact residual

```text
RESIDUAL_KERNEL=R33-BR0B-ABSOLUTE-HYPERCOHOMOLOGY-EXTENSION-CLASS
LEAF_ID=L33-03-COMPUTE-ABSOLUTE-H2-UPIC-EXTENSION-CLASS-AND-PRIMARY-ORDERS
CLASS=2
NEW_THEOREM_REQUIRED=false
```

Required next output:

1. compute the absolute extension class of the accepted filtration, or prove a canonical/abstract splitting sufficient to determine the group;
2. determine the primary order of every parametric family/lift, including the right-filtration quadratic families and the five finite free-part `H^1` classes;
3. only then set `KERNELS_COKERNELS_TORSION_EXACT=true`, `OPEN_ALGEBRAIC_Q_DEFINED_CLASS_INVENTORY_COMPLETE=true`, `BR0B_ALL_PRIMARY_CLASSES_ACCOUNTED=true`, and `BR0B=DISCHARGED`.

## Firewalls

```text
THEOREM_CREDIT=Milne_H3_VANISHING_ONLY
ENDPOINT_CREDIT=false
BRAUER_MANIN_OBSTRUCTION_CLAIM=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
33-06_RELEASED=false
```

This PR is safe to merge as an exact audited checkpoint after the repo-local state repair, but it does **not** close Stage33-03 and must not release Stage33-06.
