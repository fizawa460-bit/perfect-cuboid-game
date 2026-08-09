# Stage14-toolbox-ae — local 2-descent and five-column interface

## Purpose

Turn the merged s5 local algebra into a reusable toolbox module for the live main/s routes. The local 2-descent system was already theorem-closed in s5f, but its inputs were scattered across s5b–s5f and its notation is easy to misuse after s6 later swapped the `S/X` orientation.

This stage adds no new Stage14 theorem. It packages the exact local system, closes the orientation adapter, and freezes a one-page end-to-end local admissibility recipe.

## Canonical interface

Orientation-free Euclid support columns:

```text
A=m
B=n
C=m-n
D=m+n
E=m^2+n^2.
```

Historical s5 local orientation:

```text
S=CD=m^2-n^2
X=2AB=2mn
H=E
A,B -> X -> selected label13
C,D -> S -> selected label12
E   -> H -> selected label23.
```

Later s6-01 global-witness orientation:

```text
S=2AB
X=CD
H=E
A,B -> S -> selected label12
C,D -> X -> selected label13
E   -> H -> selected label23.
```

The five columns are invariant; the local row must be dispatched from the actual oriented `S/X/H` role.

## Local covering coordinates

```text
z1=d1*u1^2
z2=d2*u2^2
z3=d3*u3^2
z1-z2=S^2
z3-z1=X^2
z3-z2=H^2
d1*d2*d3=square class.
```

Selected odd-prime labels:

```text
p|S -> 12
p|X -> 13
p|H -> 23.
```

## Odd local rows

Selected:

```text
S/12 : chi(a1*a2)=+1 and chi(a3)=+1
X/13 : chi(a1*a3)=+1 and chi(-a2)=+1
H/23 : chi(a2*a3)=+1 and chi(a1)=+1.
```

Compressed with the product-square unit relation:

```text
S/12 : chi(a3)=+1
X/13 : chi(a2)=+1 and chi(-1)=+1
H/23 : chi(a1)=+1.
```

Unselected:

```text
p|S : chi(d3)=+1
p|H : chi(d1)=+1
p|X : chi(d2)=+1 OR chi(-d2)=+1.
```

So an unselected X-prime at `p==3 mod4` is automatic, whereas a selected X-prime requires `p==1 mod4`.

## Q2 interface

Exact squareclass representatives:

```text
1,3,5,7,2,6,10,14.
```

Hilbert formula for `A=2^alpha u`, `B=2^beta v`:

```text
(A,B)_2=(-1)^[epsilon(u)epsilon(v)+alpha*omega(v)+beta*omega(u)]
```

with

```text
epsilon(u)=(u-1)/2 mod2
omega(u)=(u^2-1)/8 mod2.
```

The product-square constraint leaves 64 ordered states, but the Stage14 normalized covering has exactly eight Q2-soluble states:

```text
(1,1,1)
(3,7,5)
(5,1,5)
(7,7,1)
(2,1,2)
(6,7,10)
(10,1,10)
(14,7,2).
```

## Safe global handoff

Merged s6-01 proves that an actual global small-point witness refines to the same five Euclid columns and a finite 16-pattern sign/2 packet. Therefore the safe implication is

```text
physical hit
 -> global small-point witness
 -> globally soluble descent class
 -> locally admissible five-column character state.
```

No converse is supplied by the toolbox.

## New canonical cards

```text
TB-DICTIONARY-five-column-local-routing
TB-FORMULA-local-covering-coordinates
TB-RECIPE-odd-local-row-dispatch
TB-FORMULA-q2-hilbert-symbol
TB-LEMMA-q2-eight-state-covering-image
TB-RECIPE-full-local-character-check
TB-WARNING-local-global-and-orientation-boundary
```

## Boundary

```text
STAGE14_TOOLBOX_AE=COMPLETE_LOCAL_2_DESCENT_FIVE_COLUMN_INTERFACE
CANONICAL_NEW_CARD_COUNT=7
FIVE_COLUMN_ODD_PAIRWISE_COPRIME_REUSED=true
S5_S6_ORIENTATION_ADAPTER_FROZEN=true
SELECTED_ODD_ROW_DISPATCH_FROZEN=true
UNSELECTED_ODD_ROW_DISPATCH_FROZEN=true
Q2_HILBERT_FORMULA_FROZEN=true
Q2_COVERING_SOLUBLE_STATE_COUNT=8
FULL_LOCAL_CHARACTER_RECIPE_FROZEN=true
LOCAL_ADMISSIBLE_IMPLIES_GLOBAL_SOLUBLE=false
GLOBAL_SOLUBLE_IMPLIES_PHYSICAL_HIT=false
OPEN_PR_USED_AS_CANONICAL_SOURCE=false
TOOLBOX_OWNS_NEW_STAGE14_THEOREM=false
NEXT=Stage14-toolbox-af integral global-small-point witness formulas
```
