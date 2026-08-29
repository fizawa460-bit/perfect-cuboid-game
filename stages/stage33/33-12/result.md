# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_CLASS2_GO_NO_GO_FAILED_PENDING_BATCH4_CLASS3_ESCALATION_AUDIT_4_OF_5`

Stage33-12 remains open. Stage33-07 remains open. Stage33-13 is not released.

## Class-2 decision budget

This is MAIN **batch 3 / 4** under the committed common-standard-form go/no-go contract.

The fixed marked receiver remains

```text
T(Kc) ~= <4> direct_sum <8>
Br(Kc)[2] = Hom(T,Z/2)
[1,0] -> kernel minimum norm 8
[0,1] -> kernel minimum norm 4
[1,1] -> kernel minimum norm 12.
```

Batch 1 exhausted the four-contact pairing space. Batch 2 selected the named branch/admissible-cover orbit `(L,R)=(1,0)`. Batch 3 asks whether that named orbit can actually be promoted to the nontrivial genus-one K3 torsor `X_J2` or its index-two transcendental kernel using retained class-2 data.

## Scope correction: branch orbit is not yet the K3 special-Brauer lift

The batch-2 Weil/Kummer computation exactly selects the branch/admissible-cover orbit

```text
J2 -> (L,R)=(1,0).
```

It did **not** materialize any of the following:

```text
H^2(Kc,mu_2) special-Brauer lift,
PGL2 splitting modules and transition matrices,
relative-Picard local trivializations,
overlap divisor cocycle D_ij,
Brauer -> Sha Leray/Ogg-Shafarevich coordinate.
```

Those firewalls were already false in the controller and remain false. Therefore `(L,R)=(1,0)` cannot be promoted to the fixed marked `[1,0]` merely because the bit strings agree.

## Kc side is fully lattice-ready

Write

```text
r=(t^2-1)^2,
q=t^4-6*t^2+1=r-4t^2,
Kc: Y^2=X(X-r)(X-q).
```

Over `Q(i)(t)`, the change

```text
x=r-X,
y=iY
```

identifies the geometric fibration with Naskrecki's

```text
E2: y^2=x(x-r)(x-4t^2).
```

The exact discriminant is

```text
Delta=256*t^4*r^2*q^2.
```

The geometric fiber configuration is

```text
I4 at t=0,+1,-1,infinity,
I2 at the four simple roots of q.
```

Naskrecki's Table 2 / Lemmas 3.8 and 6.5 give geometric MW rank 2, height Gram `diag(1/2,1)`, and torsion `Z/2 + Z/4`. Hence

```text
root lattice = A3^4 + A1^4,
|disc(root)| = 4^4*2^4 = 4096,
|disc(NS)| = 4096*(1/2)/8^2 = 32,
rho = 20,
```

exactly matching the retained semantic PicK discriminant and `T(Kc)=<4>+<8>`. This is only a geometric lattice cross-check over the extension field; it grants no Q-marked coordinate. It does show that missing Kc singular-fiber/MW information is not the obstruction.

## Exact finite Hermite test: the obvious inverse family is Sha-trivial

Depress the cubic by `x=X-(r+q)/3`. For an even quartic

```text
w^2=a0*v^4+6*a2*v^2+a4
```

Hermite gives

```text
M=[[a0,0,a2+2x],
   [0,a2-x,0],
   [a2+2x,0,a4]].
```

There are three canonical choices of `a2`, one for each cubic branch component. Imposing both

```text
det(M)=4*X(X-r)(X-q)
```

and the retained component-cover fingerprint `[q,1,q]` forces the following squareclasses:

```text
middle C0: a0 squareclass 1
middle Cr: a0 squareclass q
middle Cq: a0 squareclass 1.
```

All three canonical even inverses are Sha-trivial:

- `C0` case: choose `a0=1`, so there is a rational point at infinity.
- `Cq` case: choose `a0=1`, so there is a rational point at infinity.
- `Cr` case: the forced canonical quartic is

```text
w^2=q*(v^4+1)+2*(t^2+1)^2*v^2,
```

and it has the explicit rational point

```text
v=1,
w=2*(t^2-1).
```

Thus the retained `[q,1,q]` component fingerprint, even after exact Hermite inversion in the canonical even subfamily, produces only zero Sha classes. This does not prove every non-even symmetric representation is trivial. It proves that a nontrivial named J2 requires exactly the missing global gluing/special-Brauer realization rather than another component-fingerprint refinement.

Certificate: `j2-class2-batch3-go-no-go.json`.
Verifier: `certify_j2_class2_batch3_go_no_go.py`.

## Post-orbit breadth audit

A fresh exhaustive/blind audit was run after the material receiver change in batch 2.

```text
PGL2/mu2 globalization       -> same missing global K3 lift
non-even Hermite/Recillas    -> same missing named lift
Wittenberg generic Kummer pair -> same Brauer-to-Sha coordinate gap
Twisted Mukai                -> needs the same named B-field lift
Pic/2 / q1 shortcut          -> Kummer extension class still missing
K3-level Shioda-Inose        -> class-3-level integral marked transport
```

No class-2 route remains that is both distinct and executable from retained finite data. This is **not** a mathematical impossibility claim.

## Batch-3 go/no-go verdict

```text
CLASS2_GO_NO_GO = NO_GO_AFTER_BATCH3
class-2 budget used = 3/4
class-3 promoted now = false
class-3 escalation audit pending = true
```

The exact missing interface is now frozen as:

```text
FUNCTORIAL INTEGRAL MARKED REALIZATION OF THE NAMED CV AZUMAYA/GERBE CLASS,
COMPATIBLE WITH Q-DESCENT,
INTO EITHER
  (1/2 T*)/T*
OR
  AN EXPLICIT TWISTED RELATIVE-PICARD K3 X_J2
WITH T(X_J2)=ker(J2) IN THE FIXED Kc MARKING.
```

Batch 4 is **not** another class-2 bridge search. It is a hostile audit of this no-go and the committed class-3 escalation conditions. If the no-go survives, Stage33-12 is promoted to class 3 under the user's four-batch contract.

## Firewalls

```text
Stage33-12 visible progress = 4/5
named branch orbit = (1,0)
branch orbit bits = marked Brauer bits = false
K3 mu2 special-Brauer lift materialized = false
J2 explicit torsor surface materialized = false
J2 marked Brauer functional materialized = false
J2 twisted transcendental kernel identified = false
Stage33-12 exact closure = false
Stage33-13 released = false
heavy actions authorized = false
theorem credit = false
receiver credit = false
endpoint credit = false
perfect cuboid existence/nonexistence claim = false
```
