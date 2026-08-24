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
TWO_PRIMARY_TRANSGRESSION_COMPLETE=false
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## 1. Exact V4 action on the unit lattice

The pinned Testa--Stoll source gives the two generators of

```text
Gal(Q(i,sqrt(2))/Q) ~= V4.
```

Using the hostile-audited Stage33-02 kernel

```text
U_D = ker(Div_D -> Pic(Sbar)) ~= Z^14,
```

CI run `32687868403` induces the exact integral action.  Both Galois generators act trivially:

```text
unit character traces:
  id  = 14
  cc  = 14
  ct  = 14
  cct = 14

V4 character multiplicities:
  (+,+) = 14
  (+,-) = 0
  (-,+) = 0
  (-,-) = 0
```

Since the action on the compactification complex factors through this pinned V4, the full absolute-Galois action on `U_D` is trivial.

## 2. Exact rational action on Pic(Ubar)

Stage33-02 gives

```text
Pic(U_Qbar) ~= Z^6 + Z/2 + Z/2.
```

The basis-invariant rational character is obtained from the exact sequence

```text
0 -> U_D -> Div_D -> Pic(Sbar) -> Pic(Ubar) -> 0.
```

The free rank-six quotient has

```text
character traces:
  id  =  6
  cc  =  0
  ct  = -2
  cct = -4

V4 character multiplicities:
  (+,+) = 0
  (+,-) = 3
  (-,+) = 2
  (-,-) = 1.
```

In particular the free part has no trivial rational character.

## 3. Complete odd-primary BR0B contribution

The UPic truncation long exact sequence is used only prime-by-prime.  At every odd prime:

- `Pic(Ubar)^G` has no odd-primary contribution because the free part has no trivial character and the only torsion is `(Z/2)^2`;
- `H^1(Q,Pic(Ubar))_odd=0`: the free action factors through the order-four group V4, while the torsion is 2-primary;
- `U_D ~= Z^14` is a trivial absolute-Galois lattice.

Therefore the odd-primary open-algebraic Brauer contribution is exactly

```text
H^2(Q,UPic(Ubar))_odd
 ~= H^2(Q,Z^14)_odd
 ~= Hom_cont(G_Q,Q/Z)_odd^14.
```

This is a complete parametric description, not a finite enumeration.  It is also the reason Stage33 must not silently drop open-algebraic odd-primary classes.

```text
ODD_PRIMARY_BR0B_PARAMETRICALLY_COMPLETE=true
ODD_PRIMARY_BR0B=Hom_cont(G_Q,Q/Z)_odd^14
```

## 4. Integral Pic(Ubar) action and basis firewall closure

A first pilot correctly detected that the internal Magma `Pic` basis and the audited Stage32 primitive Picard basis are not the same basis.  No cross-basis equality was used.

Run `32688060998` closes this adapter exactly.  The same 64 source-locked known curves are used to build the change-of-basis matrix, and Magma certifies

```text
primitive-to-source Picard basis determinant = -1.
```

Thus the bridge is genuinely in `GL_64(Z)`.  Transport through the exact Stage33-02 Smith coordinates gives the full mixed integral V4 action on

```text
Pic(Ubar) = (Z/2)^2 + Z^6.
```

Both elements of the `(Z/2)^2` torsion subgroup are fixed by both V4 generators:

```text
TORSION_JOINT_FIXED_DIM_F2 = 2
TORSION_JOINT_FIXED_SUBGROUP_ORDER = 4.
```

The mixed actions square to the identity and commute exactly.

Evidence:

```text
workflow_run = 32688060998
workflow_conclusion = success
picu_integral_action_sha256 = 6f5e90aca65a0a9600937d56d265dcf17c0f3877ee2dc7b5a60b28283b682231
artifact_id = 9506357506
artifact_zip_sha256 = 673dafc9f69175a24be387c75d8128f306a9dc8ef9c90ba9cce902848d107859
odd_primary_closure_sha256 = 37621477597da5502673ca618054d255459f5d8ee777c0c20b8de758af0561be
```

## 5. Remaining exact leaf

All representation/module ambiguity has now been removed.  The remaining all-primary wall is the two-primary extension/transgression in the UPic complex:

```text
LEAF_ID=L33-03-TWO-PRIMARY-UPIC-TRANSGRESSION
CLASS=2
NEW_THEOREM_REQUIRED=false
```

The next computation must use the actual two-term equivariant complex, not merely the cohomology groups, because the connecting/transgression map may change the 2-primary answer.

```text
UNRESOLVED_UNKNOWN_IN_SCOPE>0
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```
