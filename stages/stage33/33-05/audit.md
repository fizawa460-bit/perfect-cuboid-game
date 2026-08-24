# Stage33-05 hostile audit — PR #1358

Verdict: `PASS_AFTER_INDEPENDENT_Q_SURVIVAL_AND_HS_D2_VERIFICATION`.

Audited functional head: `1e6452d2a3df9c9e054d454173b4f923d6f1d343`.

Authoritative final-head production evidence:

- workflow `32712707329` (`Stage33-05 K3 branch/Galois preflight`) — `success`;
- artifact `9514868333` — `stage33-05-k3-branch-preflight`;
- artifact ZIP SHA256 `410950d087fa5898af6b11ac7f163effe88773164a3dd569c366863a78e705bd`.

The audit downloaded that artifact and independently recomputed every stored `canonical_sha256` field. All canonical hashes matched. The older run/artifact recorded in the pre-audit result (`32712441163` / `9514610852`) is superseded as audit authority by the final-head run above.

## Accepted exact geometric prefix

The Creutz--Viray finite presentation is accepted with

```text
L_E = L_{c,E} dimension = 5
im(x-alpha) dimension   = 3
Br(K_cbar)[2] dimension = 2.
```

The exact 5D basis is `[J1,J2,q1,q2,q3]`.  The true pair-valued `x-alpha` repair gives

```text
im(x-alpha)=span_F2{
  J1,
  b*J2+q1+q2,
  d*J2+q1+q2+q3
},  b,d in F2.
```

The audit independently checked all four `(b,d)` choices.  In every case the relation space has rank 3 and `[J2,q1]` completes it to rank 5, so `[J2,q1]` is an exact quotient basis independent of the unresolved presentation coefficients.

The corrected full-pair action is

```text
tau = identity,
cc  = identity,
ct(q1)=q1+J1,
ct(q2)=q2+J1,
ct(q3)=q3,
ct(J1)=J1,
ct(J2)=J2.
```

Since `J1` lies in `im(x-alpha)`, the induced action on the 2D geometric Brauer quotient is identity.  Thus

```text
Br(K_cbar)[2]^G_Q dimension = 2
basis = [J2,q1].
```

## J2 arithmetic descent accepted

The audit independently recomputed the resultant norm of the Q-defined branch-algebra representative

```text
ell_J2 = 4*(alpha^2*t^2+t^4-4*t^2+2)
         /((t^2-1)*(t^2-2*t-1))
```

and obtained exactly

```text
Norm_{L/Q(t)}(ell_J2)
 = 1024/(t^2-2*t-1)^4
 = (32/(t^2-2*t-1)^2)^2.
```

On the normalization `z^2=t^4-6t^2+1`, the identity

```text
(t^2+z-3)(t^2-z-3)=8
```

and the simple ramification of the two roots of `t^2-2*t-1` give the recorded even divisor

```text
4*infinity_minus - 2*P1 - 2*P2.
```

This satisfies the Creutz--Viray vertical residue criterion (Prop. 3.1 / Cor. 3.2); their Prop. 3.4 then removes the exceptional `(-2)`-curve residues over the simple branch singularities.  The Q-defined corestriction quaternion algebra therefore gives an explicit unramified arithmetic representative of the nonzero geometric class `J2`.

Hence

```text
J2_Q_DESCENT_CERTIFIED=true.
```

## q1 Hochschild--Serre obstruction accepted

The presentation defect is exact:

```text
ct(q1)-q1=J1.
```

The relation is lifted integrally in `Pic(K_cbar)` by

```text
D = Cb + E_P0,
```

with `ct(D)=D`.  The Q(i)-defined branch conic `Cb`, the exceptional component `E_P0`, and the rational test conic

```text
T : A1=0, A2+B3=0, A3-B2=0
```

are source-locked to the Testa--Stoll geometry.  Direct tangent-space calculation gives

```text
Cb.T=1,
E_P0.T=0,
D.T=1.
```

For `C2=<ct>`, any cyclic norm `(1+ct)E` pairs evenly with the `ct`-invariant `T`.  Therefore `D` is not a norm and

```text
[D] != 0 in H^2(C2,Pic)=Pic^ct/(1+ct)Pic.
```

The audit also checked the formal bridge used by the production leaf.  Kummer gives

```text
0 -> Pic/2 -> H^2_et(K_cbar,mu_2) -> Br(K_cbar)[2] -> 0
```

because the K3 Picard lattice is torsion-free.  Creutz--Viray's Galois-equivariant `gamma` construction and their explicit divisor/corestriction cocycle comparison (hyperelliptic-curve paper, Remark 3.1, Proposition 3.2, Lemmas 3.4--3.5) identify the `x-alpha` presentation relation with the corresponding Picard/Kummer defect.  For the normalized C2 lift `J(ct)=D`,

```text
(dJ)(ct,ct)=2D,
Bockstein(J1)(ct,ct)=D.
```

Naturality of Kummer and Hochschild--Serre therefore gives

```text
d2(q1)|_<ct> = [D] != 0,
```

so `q1` cannot descend to `Br(K_c)`.

## Exact Q-survival

The invariant geometric space is exactly 2D with basis `[J2,q1]`.  `J2` descends explicitly and `q1` has nonzero `d2`; by linearity `q1+J2` has the same nonzero obstruction.  Hence

```text
ker(d2 | Br(K_cbar)[2]^G_Q) = span_F2{J2}
Q_RELEVANT_SURVIVING_DIM_EXACT = 1
Q_SURVIVING_GEOMETRIC_BR2_BASIS = [J2].
```

The unique surviving 1D subspace has an explicit Q-defined arithmetic representative, so the Stage33-05 closure contract is completely satisfied.

## Accepted audited state

```text
K3_GEOMETRIC_BR2_DIM=2
QI_OVER_Q_ACTION_MATRIX_EXACT=true
INVARIANT_DESCENDED_SUBSPACE_EXACT=true
DESCENT_OBSTRUCTION_ACCOUNTED=true
Q_RELEVANT_SURVIVING_DIM_EXACT=true
ALL_SURVIVING_K3_CLASSES_HAVE_EXPLICIT_ARITHMETIC_REPRESENTATIVES=true
UNRESOLVED_UNKNOWN_IN_SCOPE=0
HOSTILE_AUDIT=PASS
UNIT_STATUS=CLOSED
UNIT_CLOSED=true
DOWNSTREAM_RELEASED=true
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

This closes only Stage33-05.  It does not release Stage33-07 by itself because `33-03`, `33-04`, and `33-06` are independent prerequisites under the frozen DAG.  No route-color, Brauer--Manin obstruction, endpoint theorem, or Perfect Cuboid existence/nonexistence credit is granted here.
