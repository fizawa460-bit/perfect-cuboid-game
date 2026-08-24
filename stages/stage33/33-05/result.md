# Stage33-05 — K3 Br[2] Q(i)/Q descent production state

```text
STAGE33_UNIT=33-05
UNIT_STATUS=READY_FOR_AUDIT
MAIN_PRODUCTION_COMPLETE=true
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
K3_GEOMETRIC_BR2_DIM=2
LCE_DIMENSION=5
XALPHA_IMAGE_DIMENSION=3
COMMON_NORMALIZATION_EXACT=true
FULL_EXPLICIT_LCE_BASIS_MATERIALIZED=true
TRUE_XALPHA_PAIR_REPAIR_EXACT=true
J1_IN_XALPHA_IMAGE_EXACT=true
XALPHA_GRAPH_PROJECTION_RANK=2
XALPHA_IMAGE_SPANNED_EXACTLY=true
SEVEN_GRAPH_LINE_SEARCH_RETIRED=true
BRAUER_QUOTIENT_DIMENSION=2
EXPLICIT_GEOMETRIC_BRAUER_QUOTIENT_BASIS=J2,q1
FULL_PAIR_GALOIS_ACTION_EXACT=true
GEOMETRIC_BR2_GALOIS_ACTION=IDENTITY
GEOMETRIC_BR2_GQ_INVARIANT_DIMENSION=2
CV_PRESENTATION_CONNECTING_COCYCLE_EXACT=true
J2_Q_DESCENT_CERTIFIED=true
Q1_NS_LIFT_MATERIALIZED=true
Q1_HOCHSCHILD_SERRE_D2_CERTIFIED=true
Q1_Q_DESCENT=false
DESCENT_OBSTRUCTION_ACCOUNTED=true
Q_DEFINED_ARITHMETIC_REPRESENTATIVES_MATERIALIZED=true
Q_RELEVANT_SURVIVING_DIM_CERTIFIED=true
Q_RELEVANT_SURVIVING_DIM=1
Q_SURVIVING_GEOMETRIC_BR2_BASIS=J2
HOSTILE_AUDIT=PENDING
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Exact geometric presentation

The corrected Creutz--Viray computation is frozen at

```text
Jac(B)[2] dimension       = 4
dual graph b1             = 7
raw generator dimension   = 12
K*L^2 relation dimension  = 7
L_E=L_{c,E} dimension     = 5
im(x-alpha) dimension     = 3
Br(K_cbar)[2] dimension   = 2.
```

The common normalization is

```text
z^2=t^4-6t^2+1,
s_plus =  i*(1-t^2+z)/(2*t),
s_minus = -i*(1-t^2+z)/(2*t),
```

and the exact `L_{c,E}` basis is `[J1,J2,q1,q2,q3]`, with graph classes

```text
q1=e1+e3,
q2=e1+e5,
q3=e1+e7.
```

The old `xalpha_split_section_rows.py` pure-Jac interpretation is superseded and retained only as a norm-level regression.  For the true pair class `(f-s_plus,f-s_minus)`, exact node incidences give

```text
s=1                    -> graph q1+q2,
s=t                    -> graph q1+q2+q3,
s=-i*(t-i)/(t+i)       -> graph q1+q2,
```

and an explicit square witness proves

```text
xalpha(-i*(t-i)/(t+i)) + xalpha(1) = J1.
```

Thus

```text
im(x-alpha)
 = span_F2 {
     J1,
     b*J2+q1+q2,
     d*J2+q1+q2+q3
   }, b,d in F2,
```

and `[J2,q1]` is a quotient basis for every `b,d`.

## Correct full-pair Galois action

The single-component half-point mixing is not the full action on `L=k(B+) x k(B-)`.  The corrected pair action is

```text
tau = identity,
cc  = identity,
ct(q1)=q1+J1,
ct(q2)=q2+J1,
ct(q3)=q3,
ct(J1)=J1,
ct(J2)=J2.
```

Since `J1` is an `x-alpha` relation, the induced action on `Br(K_cbar)[2]` is identity. Therefore

```text
Br(K_cbar)[2] ~= (F2)^2,
Br(K_cbar)[2]^G_Q ~= (F2)^2,
```

with geometric invariant basis `[J2,q1]`.

## J2 descends to Q

The first descent filter gives `delta(J2)=0`.  Hilbert--90 removes the auxiliary `sqrt(2)` from the normalization representative:

```text
ell_z = 2*(t^2+z-3)/(t^2-2*t-1).
```

Eliminating `z` in the Q-defined quartic branch algebra

```text
L=Q(t)[alpha]/(
  t^2*(1-alpha^2)^2 + alpha^2*(1-t^2)^2
)
```

gives the Q-rational function

```text
ell_J2 =
4*(alpha^2*t^2+t^4-4*t^2+2)
 / ((t^2-1)*(t^2-2*t-1)).
```

The exact resultant computation gives

```text
Norm_{L/Q(t)}(ell_J2)
 = 1024/(t^2-2*t-1)^4
 = (32/(t^2-2*t-1)^2)^2.
```

On `z^2=t^4-6t^2+1`, the divisor is

```text
4*infinity_minus - 2*P1 - 2*P2,
```

so every branch valuation is even.  The horizontal norm condition and the Creutz--Viray simple-node exceptional-curve condition therefore hold.  A Q-defined unramified representative is materialized as the corresponding corestriction quaternion algebra

```text
Cor_{L(C)/Q(t)(C)}((ell_J2,s-alpha)_2).
```

Hence `J2` is a nontrivial geometric class that genuinely descends to `Br(K_c)`.

## q1 has nonzero Hochschild--Serre d2

The CV-presentation connecting calculation gives

```text
ct(q1)-q1 = J1.
```

The relation has now been lifted integrally to the Neron--Severi group.  Under the Stage29 ruled map,

```text
s=-i*(t-i)/(t+i)
```

closes to the branch conic

```text
Cb : i*A1+B1 = i*A2+B2 = i*A3+B3 = 0,
```

while the chosen `s=1` section contracts to the singular point

```text
P0=[0:1:0:-1:0:1].
```

On the minimal resolution an integral lift of `J1` is therefore

```text
D = Cb + E_P0.
```

Both components are fixed by `ct`.  With the `ct`-invariant nonbranch conic

```text
T : A1=0, A2+B3=0, A3-B2=0,
```

exact tangent-space computation gives

```text
Cb.T=1,
E_P0.T=0,
D.T=1.
```

If `D=(1+ct)E` were a cyclic norm, invariance of `T` would force `D.T=2(E.T)`, contradiction.  Hence

```text
[D] != 0 in H^2(<ct>,Pic(K_cbar))
          = Pic(K_cbar)^ct / (1+ct)Pic(K_cbar).
```

The remaining compatibility is now closed by the Kummer/Leray cochain chase.  Since a K3 Picard group is torsion-free, Kummer gives

```text
0 -> Pic/2 -> H^2_et(K_cbar,mu_2) -> Br(K_cbar)[2] -> 0.
```

Creutz--Viray's `gamma` is the explicit corestriction/cup-product lift, and their divisor/Brauer cocycle calculation identifies its Galois defect with the corresponding Picard defect.  Thus the presentation defect `J1` is exactly the Kummer `Pic/2` defect of `q1`.

For `C2=<ct>`, lift the normalized defect by `J(ct)=D`. Then

```text
(dJ)(ct,ct)=ct(D)+D=2D,
Bockstein(J1)(ct,ct)=D.
```

Naturality of the Kummer and Leray/Hochschild--Serre sequences identifies this Bockstein with `d2(q1)|_<ct>`. Since `[D]` is nonzero,

```text
d2(q1)|_<ct> != 0,
d2(q1) != 0,
q1 does not descend to Br(K_c).
```

## Exact Q-survival dimension

The invariant geometric space is two-dimensional with basis `[J2,q1]`.  `J2` has an explicit Q-defined unramified representative, while `q1` has nonzero `d2`.  By linearity, `q1+J2` has the same nonzero obstruction. Therefore

```text
ker(d2 on Br(K_cbar)[2]^G_Q) = span_F2{J2},
Q_RELEVANT_SURVIVING_DIM = 1.
```

This is a Stage33-05 K3 two-primary arithmetic-descent result only.  It grants no endpoint, route-color, Brauer--Manin obstruction, or perfect-cuboid existence/nonexistence credit by itself.

## Authoritative execution

```text
xalpha repair checker       = xalpha_pair_galois_repair.py
descent frontend checker    = descent_presentation_cocycle.py
J2 arithmetic checker       = j2_arithmetic_descent.py
q1 NS parity checker        = q1_ns_lift_parity.py
q1 HS d2 checker            = q1_hs_d2_bockstein.py
workflow_run                = 32712441163
workflow_number             = 55
workflow_conclusion         = success
artifact_id                 = 9514610852
artifact_sha256             = 075f4ec28170e62f86a895f9c65028a8daaa1516c5b2a2dba8298d710ebb5d3e
```

## Production disposition

```text
ALL_STAGE33_05_DESCENT_UNKNOWNS_RESOLVED=true
MAIN_PRODUCTION_COMPLETE=true
HOSTILE_AUDIT=PENDING
UNIT_STATUS=READY_FOR_AUDIT
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
NEXT_EXPECTED_COMMAND=Stage33-audit
```
