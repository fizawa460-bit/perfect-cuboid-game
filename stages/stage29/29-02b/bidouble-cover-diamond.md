# Stage29-02b — bidouble-cover quotient diamond

```text
ROLE=JOINT_V4_QUOTIENT_DIAGRAM
STATUS=DERIVED_PENDING_FRESH_AUDIT
```

Let

```text
Y=Bl_4(P1xP1),
K=Qbar(Y),
f=t1^2+t2^2,
g=1+t1^2+t2^2.
```

Stage28 certifies that `K(sqrt(f))` and `K(sqrt(g))` are distinct quadratic extensions.  Hence

```text
K_joint=K(sqrt(f),sqrt(g))
```

has generic Galois group `V4=(Z/2)^2` and exactly three nontrivial quadratic subfields.

The quotient diamond is therefore

```text
                         X_joint
                      /     |      \
                     /      |       \
               X_face    X_cross    X_sp
                     \      |       /
                      \     |      /
                           Y
```

with function fields

```text
X_face  : K(sqrt(f))
X_sp    : K(sqrt(g))
X_cross : K(sqrt(fg)).
```

The first two quotients are the Stage20 third-face K3 cover and Stage19 space-completion K3 cover.  The third quotient is new to Stage29 and records the product squareclass.

## Endpoint meaning

`X_joint` is not a fourth unrelated construction.  On the dense two-face chart it is birational to the full perfect-cuboid endpoint surface: the two square roots reconstruct the third face diagonal and the long diagonal.

Thus the three intermediate quotients have distinct meanings:

- `X_face`: forget the long-diagonal square root;
- `X_sp`: forget the third-face square root;
- `X_cross`: retain only the product squareclass of the two missing completion predicates.

The cross quotient is therefore the geometric carrier of the local cross character

```text
chi(fg)=chi(f)chi(g),
```

which is exactly the extra term in the simultaneous local square-indicator expansion.

## Involution bookkeeping

Let `sigma_f` change the sign of `sqrt(f)` and `sigma_g` change the sign of `sqrt(g)`.  Then

```text
X_joint/<sigma_f>           = X_sp,
X_joint/<sigma_g>           = X_face,
X_joint/<sigma_f sigma_g>   = X_cross.
```

Physical positive cuboids choose signs after passing to the real positive chamber.  These algebraic involutions are not physical multiplicity factors.

```text
V4_QUOTIENT_DIAMOND_EXACT=true
CROSS_QUOTIENT_NEW_STAGE29_OBJECT=true
ALGEBRAIC_SIGN_ORBITS_ARE_PHYSICAL_MULTIPLICITY=false
```
