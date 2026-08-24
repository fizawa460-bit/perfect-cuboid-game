# Stage33-05 — K3 Br[2] Q(i)/Q action and descent

```text
STAGE33_UNIT=33-05
UNIT_STATUS=CLOSED
UNIT_CLOSED=true
DOWNSTREAM_RELEASED=true
HOSTILE_AUDIT=PASS_AFTER_INDEPENDENT_Q_SURVIVAL_AND_HS_D2_VERIFICATION
K3_GEOMETRIC_BR2_DIM=2
QI_OVER_Q_ACTION_MATRIX_EXACT=true
INVARIANT_DESCENDED_SUBSPACE_EXACT=true
DESCENT_OBSTRUCTION_ACCOUNTED=true
Q_RELEVANT_SURVIVING_DIM_EXACT=true
Q_RELEVANT_SURVIVING_DIM=1
ALL_SURVIVING_K3_CLASSES_HAVE_EXPLICIT_ARITHMETIC_REPRESENTATIVES=true
UNRESOLVED_UNKNOWN_IN_SCOPE=0
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Exact geometric presentation

The corrected Creutz--Viray finite presentation is

```text
Jac(B)[2] dimension       = 4
dual graph b1             = 7
L_E=L_{c,E} dimension     = 5
im(x-alpha) dimension     = 3
Br(K_cbar)[2] dimension   = 2.
```

The exact 5D presentation basis is `[J1,J2,q1,q2,q3]`.  The true pair-valued `x-alpha` calculation gives

```text
im(x-alpha)=span_F2{
  J1,
  b*J2+q1+q2,
  d*J2+q1+q2+q3
}, b,d in F2.
```

For all four choices of `(b,d)`, `[J2,q1]` is an exact quotient basis.  The corrected full-pair action is

```text
tau = identity,
cc  = identity,
ct(q1)=q1+J1,
ct(q2)=q2+J1,
ct(q3)=q3,
ct(J1)=J1,
ct(J2)=J2.
```

Because `J1` is an `x-alpha` relation, the induced action on `Br(K_cbar)[2]` is identity.  Therefore

```text
Br(K_cbar)[2]^G_Q ~= (F2)^2
basis = [J2,q1].
```

## Exact arithmetic descent

### J2 survives

A Q-defined branch-algebra representative is

```text
ell_J2 = 4*(alpha^2*t^2+t^4-4*t^2+2)
         /((t^2-1)*(t^2-2*t-1)).
```

The exact resultant norm is

```text
Norm_{L/Q(t)}(ell_J2)
 = 1024/(t^2-2*t-1)^4
 = (32/(t^2-2*t-1)^2)^2.
```

On `z^2=t^4-6t^2+1` its divisor is

```text
4*infinity_minus - 2*P1 - 2*P2,
```

so the vertical residue conditions are even.  Creutz--Viray Prop. 3.1 / Cor. 3.2 and Prop. 3.4 then certify the corresponding Q-defined corestriction quaternion algebra as unramified on the K3 resolution.  Thus

```text
J2_Q_DESCENT_CERTIFIED=true.
```

### q1 does not survive

The exact presentation defect is

```text
ct(q1)-q1=J1.
```

An integral `ct`-invariant NS lift of `J1` is

```text
D = Cb + E_P0.
```

For the `ct`-invariant test conic

```text
T : A1=0, A2+B3=0, A3-B2=0,
```

exact tangent/intersection computation gives

```text
Cb.T=1,
E_P0.T=0,
D.T=1.
```

Therefore `D` is not a cyclic norm in `Pic(K_cbar)` and

```text
[D] != 0 in H^2(<ct>,Pic).
```

Kummer gives

```text
0 -> Pic/2 -> H^2_et(K_cbar,mu_2) -> Br(K_cbar)[2] -> 0.
```

Creutz--Viray's Galois-equivariant corestriction/divisor cocycle comparison identifies the `x-alpha` defect with the Picard/Kummer defect.  With normalized lift `J(ct)=D`,

```text
(dJ)(ct,ct)=2D,
Bockstein(J1)(ct,ct)=D,
```

hence

```text
d2(q1)|_<ct>=[D] != 0,
q1_Q_DESCENT=false.
```

By linearity `q1+J2` has the same nonzero obstruction.  Consequently

```text
ker(d2 | Br(K_cbar)[2]^G_Q)=span_F2{J2}
Q_RELEVANT_SURVIVING_DIM=1
Q_SURVIVING_GEOMETRIC_BR2_BASIS=[J2].
```

The unique surviving K3 class has an explicit Q-defined arithmetic representative.

## Hostile audit evidence

Final functional head audited:

```text
1e6452d2a3df9c9e054d454173b4f923d6f1d343
```

Authoritative execution:

```text
workflow_run     = 32712707329
workflow_number  = 59
conclusion       = success
artifact_id      = 9514868333
artifact_sha256  = 410950d087fa5898af6b11ac7f163effe88773164a3dd569c366863a78e705bd
```

The artifact ZIP digest was independently recomputed and matched.  Every stored canonical SHA256 in the artifact was independently recomputed and matched.  The audit also independently checked all four `(b,d)` quotient cases and recomputed the J2 resultant norm.

Repo authority:

```text
stages/stage33/33-05/audit.md
stages/stage33/33-05/audit-state.json
stages/stage33/33-05/handoff.json
```

## Disposition

```text
CLOSURE_CRITERIA_TOTAL=8
CLOSURE_CRITERIA_SATISFIED=8
UNRESOLVED_UNKNOWN_IN_SCOPE=0
UNIT_STATUS=CLOSED
UNIT_CLOSED=true
DOWNSTREAM_RELEASED=true
```

This closes only the Stage33-05 K3 arithmetic-descent branch.  Stage33-07 remains locked until its independent prerequisites `33-03`, `33-04`, and `33-06` are also CLOSED.  No endpoint theorem, route-color change, Brauer--Manin obstruction, or Perfect Cuboid existence/nonexistence credit is granted by this unit alone.
