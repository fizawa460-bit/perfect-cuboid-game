# Stage33-03 — BR0B UPic absolute-Galois production state

```text
STAGE33_UNIT=33-03
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
BR0B=OPEN
BR0B_ALL_PRIMARY_CLASSES_ACCOUNTED=false
UPIC_V4_INTEGRAL_ACTION_EXACT=true
UNIT_LATTICE_V4_ACTION_EXACT=true
PICU_INTEGRAL_V4_ACTION_EXACT=true
ODD_PRIMARY_BR0B_PARAMETRICALLY_COMPLETE=true
FINITE_V4_HYPERCOHOMOLOGY_EXACT=true
FINITE_V4_H2=(Z/2)^33
ABSOLUTE_TWO_PRIMARY_INFLATION_RESTRICTION_COMPLETE=false
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## 1. Exact V4 action and odd-primary closure

The pinned Testa--Stoll source gives

```text
Gal(Q(i,sqrt(2))/Q) ~= V4.
```

The hostile-audited Stage33-02 kernel is

```text
U_D = ker(Div_D -> Pic(Sbar)) ~= Z^14.
```

Both V4 generators act trivially on this rank-14 integral lattice.  The free rank-six part of

```text
Pic(Ubar) ~= Z^6 + (Z/2)^2
```

has rational V4 character multiplicities

```text
(+,+)=0, (+,-)=3, (-,+)=2, (-,-)=1,
```

and the full `(Z/2)^2` torsion subgroup is jointly fixed.

The Stage32 primitive Picard basis and the internal Testa--Stoll Picard basis are related by an exact unimodular change of basis with determinant `-1`, so no cross-basis identification is assumed.

For every odd prime the finite-quotient correction is 2-primary, while `U_D` is a trivial absolute-Galois lattice.  Hence

```text
H^2(Q,UPic(Ubar))_odd
 ~= Hom_cont(G_Q,Q/Z)_odd^14.
```

```text
ODD_PRIMARY_BR0B_PARAMETRICALLY_COMPLETE=true
ODD_PRIMARY_BR0B=Hom_cont(G_Q,Q/Z)_odd^14
```

## 2. Exact finite V4 hypercohomology, including the extension/transgression

Run `32688821421` computes the finite-quotient hypercohomology of the actual two-term complex

```text
UPic(Ubar) = [ Div_D -> Pic(Sbar) ]
```

instead of separately guessing the transgression.  The checker uses the tensor product of the standard two-periodic `C2` resolutions for

```text
V4 = C2 x C2,
```

totalizes the divisor module in degree `0` and the Picard module in degree `1`, verifies two consecutive total differentials compose to zero, and computes

```text
H^2(V4,UPic(Ubar)) = ker(d2)/im(d1)
```

by exact Smith normal form.

The result is

```text
FINITE_V4_H2_FREE_RANK = 0
FINITE_V4_H2_TORSION_INVARIANTS = [2 x 33]
H^2(V4,UPic(Ubar)) ~= (Z/2)^33.
```

This finite result includes the integral extension data of `[Div_D -> Pic]`; it is not a calculation performed only on `U_D` and `Pic(Ubar)` separately.

Evidence:

```text
workflow_run = 32688821421
workflow_conclusion = success
finite_v4_hypercohomology_sha256 = 82eabfe80fce8407198a8b2dd5277de352280866e73a38d272f160bc0a41ac2d
artifact_id = 9506608027
artifact_zip_sha256 = c49ec9282088962d09e059ba2878f26e71d32453afcf266daf1ee4132fa6e85b
picu_integral_action_sha256 = 6f5e90aca65a0a9600937d56d265dcf17c0f3877ee2dc7b5a60b28283b682231
odd_primary_closure_sha256 = 37621477597da5502673ca618054d255459f5d8ee777c0c20b8de758af0561be
```

## 3. Firewall: finite V4 is not yet the full absolute two-primary answer

The exact finite quotient

```text
H^2(V4,UPic(Ubar)) ~= (Z/2)^33
```

does **not** by itself identify

```text
H^2(G_Q,UPic(Ubar))[2^infinity].
```

Absolute-Galois inflation/restriction terms from the kernel of `G_Q -> V4`, especially the rank-14 trivial unit lattice and 2-primary coefficient terms, still have to be combined with the finite quotient exactly.

Therefore none of the following is claimed:

```text
BR0B_CLOSED=false
BR0B_ALL_PRIMARY_CLASSES_ACCOUNTED=false
Q_DEFINED_BRAUER_CLASS_COUNT_FROM_33_03=NOT_YET_CERTIFIED
BRAUER_MANIN_OBSTRUCTION_PROVED=false
```

## 4. Next exact leaf

```text
LEAF_ID=L33-03-ABSOLUTE-TWO-PRIMARY-INFLATION-RESTRICTION
CLASS=2
NEW_THEOREM_REQUIRED=false
INPUT_FINITE_V4_H2=(Z/2)^33
INPUT_UNIT_LATTICE=Z^14_TRIVIAL_GQ
INPUT_PICU=Z^6+(Z/2)^2
```

The next step is to compute the absolute two-primary inflation/restriction correction and combine it with the already-complete odd-primary description.  Only then can BR0B be closed or a smaller residual kernel be exposed.

```text
UNRESOLVED_UNKNOWN_IN_SCOPE>0
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```
