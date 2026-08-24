# Stage33-05 CI evidence

The old `L_{c,E}=9` pilot and the old norm-level pure-Jac `x-alpha` row interpretation are superseded.  The authoritative chain now includes the exact five-function lift, the true section-pair `x-alpha` repair, the corrected full-pair Galois action, an explicit geometric quotient basis, and the first finite-presentation descent connecting computation.

Latest authoritative CI before this evidence-only commit:

```text
HEAD_SHA=43f4f7907830f63045839d1c2d15ba12cad3e96e
WORKFLOW_RUN=32711169972
WORKFLOW_NUMBER=45
CONCLUSION=success
ARTIFACT_ID=9514128076
ARTIFACT_ZIP_SHA256=568b68ff0f5070b4c84efecaf3651199b862548fed3cd175c641c998da68cbf1
ARTIFACT_NAME=stage33-05-k3-branch-preflight
```

The successful workflow reruns the complete Stage33-05 exact chain and certifies

```text
branch components                         = 2 smooth (2,2) genus-one curves over Q(i)
intersection nodes                        = 8, all transverse
Jac(B)[2] dim                             = 4
dual graph b1                             = 7
special even-e fiber count                = 8
L_E=L_{c,E} dim                           = 5
im(x-alpha) dim                           = 3
Br(K_cbar)[2] dim                         = 2
full explicit L_{c,E} basis               = materialized
true x-alpha pair repair                  = exact
J1 in im(x-alpha)                         = exact
x-alpha graph projection rank             = 2
seven-graph-line search                   = retired
explicit geometric Brauer quotient basis  = J2,q1
full-pair Galois action                    = exact
geometric Br[2] quotient action            = identity
geometric G_Q-invariant dimension          = 2
CV-presentation delta(J2)                 = 0
CV-presentation delta(q1)                 = ct -> J1 != 0
J2 fixed LcE lift                         = yes
q1 fixed LcE lift                         = no
J2 sqrt(2)-free Q(i) generic function      = materialized
```

Authoritative `x-alpha` state in basis `[J1,J2,q1,q2,q3]`:

```text
s=1                    -> graph q1+q2
s=t                    -> graph q1+q2+q3
s=-i*(t-i)/(t+i)       -> graph q1+q2
xalpha(-i*(t-i)/(t+i)) + xalpha(1) = J1

im(x-alpha)
 = span_F2 {
     J1,
     b*J2+q1+q2,
     d*J2+q1+q2+q3
   }, b,d in F2.
```

For every `b,d`, `[J2,q1]` is a basis of the two-dimensional quotient.  The old seven-line residual search and the old pure-Jac section rows are not load-bearing.

The corrected full-pair action is

```text
tau = cc = identity
ct(q1)=q1+J1
ct(q2)=q2+J1
ct(q3)=q3
ct(J1)=J1
ct(J2)=J2
```

and therefore induces identity on the geometric quotient because `J1` is a relation.

The first descent front-end is the connecting map of

```text
0 -> R=im(x-alpha) -> L_{c,E} -> Br(K_cbar)[2] -> 0.
```

It gives

```text
delta(J2)=0
delta(q1)=ct -> J1 != 0.
```

This connecting class is **not** promoted to the Hochschild--Serre `d2`.  In particular the repository does not yet claim that `q1` fails arithmetic descent.

For `J2`, the checker also certifies the squareclass identity

```text
2*(t^2+z-3)/(t^2-2*t-1)
```

as a `sqrt(2)`-free `Q(i)`-defined generic normalization function representing the geometric `J2` class.  Arithmetic unramifiedness over `Q(i)` and `Q(i)/Q` descent are still open.

Still open:

```text
J2_ARITHMETIC_QI_RESIDUES_CERTIFIED=false
J2_QI_OVER_Q_DESCENT_CERTIFIED=false
Q1_J1_RELATION_NS_LIFT_MATERIALIZED=false
Q1_HOCHSCHILD_SERRE_D2_CERTIFIED=false
DESCENT_OBSTRUCTION_ACCOUNTED=false
Q_DEFINED_ARITHMETIC_REPRESENTATIVES_MATERIALIZED=false
Q_RELEVANT_SURVIVING_DIM=NOT_YET_CERTIFIED
UNIT_STATUS=RUNNING
```

This file update is evidence-only.  Its own follow-up workflow run should be checked separately; the mathematical certificate content above is tied to successful run `32711169972` on `43f4f7907830f63045839d1c2d15ba12cad3e96e`.
