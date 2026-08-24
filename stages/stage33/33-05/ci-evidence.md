# Stage33-05 CI evidence

The old `L_{c,E}=9` pilot, the old norm-level pure-Jac `x-alpha` row interpretation, and the old single-component Galois matrices as a full-pair action are superseded.  The authoritative mathematical chain now includes the exact five-function lift, true section-pair `x-alpha`, corrected full-pair action, arithmetic descent of `J2`, the integral NS lift for the `q1` defect, and the Kummer/Hochschild--Serre Bockstein calculation.

Latest authoritative mathematical CI before the documentation/evidence ledger commits:

```text
HEAD_SHA=03e36312a0ac2d6841902b08045d919da7fe2df1
WORKFLOW_RUN=32712441163
WORKFLOW_NUMBER=55
CONCLUSION=success
ARTIFACT_ID=9514610852
ARTIFACT_ZIP_SHA256=075f4ec28170e62f86a895f9c65028a8daaa1516c5b2a2dba8298d710ebb5d3e
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
J2 Q-defined branch-algebra function       = materialized
J2 norm in Q(t)                            = exact square
J2 arithmetic residue checks              = pass
J2 Q-defined unramified CSA                = materialized
J2 Q descent                              = certified
q1 integral NS lift D                      = materialized
D invariant test pairing                   = 1 (odd)
D cyclic norm status                       = NO
[D] in H^2(<ct>,Pic)                       = nonzero
q1 Kummer defect                           = D mod 2
q1 HS d2 restricted to <ct>                = [D] != 0
q1 Q descent                              = rejected
Q-relevant surviving dimension             = 1 exact
surviving geometric Br[2] basis            = J2
```

## Authoritative x-alpha / Galois state

In basis `[J1,J2,q1,q2,q3]`,

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

For every `b,d`, `[J2,q1]` is a basis of the two-dimensional quotient.  The full-pair action is

```text
tau = cc = identity
ct(q1)=q1+J1
ct(q2)=q2+J1
ct(q3)=q3
ct(J1)=J1
ct(J2)=J2
```

and therefore induces the identity on the geometric quotient.

## J2 arithmetic certificate

The checker `j2_arithmetic_descent.py` eliminates `sqrt(2)` and realizes the geometric `J2` class in the Q-defined branch algebra

```text
L=Q(t)[alpha]/(t^2*(1-alpha^2)^2+alpha^2*(1-t^2)^2)
```

by

```text
ell_J2=
4*(alpha^2*t^2+t^4-4*t^2+2)
 / ((t^2-1)*(t^2-2*t-1)).
```

It verifies

```text
Norm_{L/Q(t)}(ell_J2)
 = 1024/(t^2-2*t-1)^4
 = (32/(t^2-2*t-1)^2)^2,
```

together with an even geometric divisor and the Creutz--Viray vertical/horizontal/simple-node residue conditions.  Hence the Q-defined corestriction quaternion algebra is unramified and maps geometrically to nonzero `J2`.

## q1 Hochschild--Serre certificate

The checker `q1_ns_lift_parity.py` closes the `J1` presentation relation to

```text
D=Cb+E_P0,
Cb : i*A1+B1=i*A2+B2=i*A3+B3=0,
P0=[0:1:0:-1:0:1].
```

For the invariant conic

```text
T : A1=0, A2+B3=0, A3-B2=0,
```

it verifies by tangent-space ranks that

```text
Cb.T=1,
E_P0.T=0,
D.T=1.
```

Thus `D` is not in `(1+ct)Pic`, so `[D]` is nonzero in `H^2(<ct>,Pic)`.

The final checker `q1_hs_d2_bockstein.py` imports all predecessor certificates and performs the normalized `C2` cochain calculation.  With Kummer defect `J1=D mod 2` and integral lift `J(ct)=D`,

```text
(dJ)(ct,ct)=2D,
Bockstein(J1)(ct,ct)=D.
```

The Kummer/Leray naturality and the Creutz--Viray explicit cup-product/divisor-cocycle compatibility identify this Bockstein with the restriction of the Hochschild--Serre differential.  Therefore

```text
d2(q1)|_<ct>=[D] != 0,
d2(q1) != 0,
q1 does not descend.
```

Since `J2` descends,

```text
ker(d2 | Br(K_cbar)[2]^G_Q)=span_F2{J2},
Q_RELEVANT_SURVIVING_DIM=1.
```

## Production disposition

```text
DESCENT_OBSTRUCTION_ACCOUNTED=true
Q_DEFINED_ARITHMETIC_REPRESENTATIVES_MATERIALIZED=true
Q_RELEVANT_SURVIVING_DIM_CERTIFIED=true
Q_RELEVANT_SURVIVING_DIM=1
UNRESOLVED_UNKNOWN_IN_SCOPE=0
MAIN_PRODUCTION_COMPLETE=true
HOSTILE_AUDIT=PENDING
UNIT_STATUS=READY_FOR_AUDIT
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
```

Later `result.md`, `source-reduction.md`, `source-lock.md`, and this ledger commit are documentation/evidence commits. They trigger regression workflows but do not supersede the mathematical certificate identity above unless a later mathematical checker changes.
