# MB104 Z49 — size48 explicit plumbing: finite index-one root ambiguity — 2026-09-19

Status: **PRE-AUDIT EXACT FINITE PLUMBING REDUCTION / NEW ADAPTER / NO CREDIT**

## Target

Work on one connected size-48 nonrational exceptional fiber

```text
D = Q_1 union B union Q_2
```

with dual graph

```text
Q_1(-4,g=1) -- B(-2,g=0) -- Q_2(-4,g=1).
```

Retained Z48 input:

```text
Q_i ~= E_1728,
N_(Q_i/S) ~= O_{Q_i}(-4p_i),
B ~= P^1,
N_(B/S) ~= O_{P^1}(-2),
```

and the two attachments are the exact retained transverse marked points.

The purpose of Z49 is to determine what plumbing/root data remain after those exact component
neighborhoods and the index-three discrepancy are fixed.

## 1. Exact discrepancy vector

Write

```text
K_S = phi^* K_Y + a_1 Q_1 + a_B B + a_2 Q_2.
```

Adjunction gives

```text
K_S.Q_i = 4,
K_S.B = 0.
```

The intersection matrix is

```text
[-4  1  0]
[ 1 -2  1]
[ 0  1 -4].
```

Since `phi^*K_Y` has zero intersection with each contracted component, symmetry gives
`a_1=a_2=x`, `a_B=y), and

```text
-4x+y=4,
2x-2y=0.
```

Hence

```text
a_1=a_B=a_2=-4/3.                              (DISCREPANCY)
```

Equivalently, on a sufficiently small plumbing neighborhood `N(D)`,

```text
phi^*(3K_Y) = 3K_S + 4D.                       (3K-PLUMB)
```

Thus the divisorial/meridian exponent of the index-one cyclic cover is fixed on all three
components.  There is no freedom to change those exponents without changing the exact
Q-Gorenstein canonical class.

## 2. Ordinary edge plumbing scalars are not moduli

Fix the linearized component neighborhoods from Z48.

Near the edge `Q_1--B`, choose coordinates

```text
(z_1,u_1) on Tot(N_{Q_1/S}),
(w_0,v_0) on Tot(N_{B/S}),
```

with zero sections `u_1=0`, `v_0=0` and marked attachment coordinates `z_1=0`, `w_0=0`.

A standard transverse plumbing has the form, up to units,

```text
z_1 = alpha_1 v_0,
u_1 = beta_1 w_0,
alpha_1,beta_1 in C^*.
```

The same holds at the second edge with nonzero scalars `alpha_2,beta_2`.

Fiber multiplication in each line bundle is a `C^*` automorphism, and the bridge
`P^1` has a `C^*` automorphism fixing its two marked endpoints.  Because the dual graph is a
tree, these component rescalings can be chosen successively from an end vertex and absorb every
edge scalar.

Therefore:

```text
continuous C^* edge-plumbing modulus = none.    (TREE-SCALAR)
```

This statement concerns scalar plumbing parameters after the component neighborhoods and marked
points are fixed.  It does not infer the analytic germ from the weighted graph alone.

## 3. The remaining canonical-root ambiguity is finite

Let the local Cartier generator of `3K_Y` be fixed.  By (3K-PLUMB), the associated
index-one cover has fixed meridian character around each irreducible component of `D`.

After fixing these meridian characters, two candidate order-three canonical root data on the
exceptional divisor can differ only by a degree-zero three-torsion line bundle on `D`.

The generalized Jacobian normalization sequence for a nodal curve gives

```text
1 -> (C^*)^{b_1(Gamma_D)}
  -> Pic^0(D)
  -> Pic^0(Q_1) x Pic^0(B) x Pic^0(Q_2)
  -> 1.
```

Here `Gamma_D` is a tree, so `b_1(Gamma_D)=0`, and `Pic^0(P^1)=0`.  Hence

```text
Pic^0(D) ~= Pic^0(Q_1) x Pic^0(Q_2).
```

Both elliptic components have `j=1728`, therefore over `C`

```text
Pic^0(Q_i)[3] ~= Q_i[3] ~= (Z/3Z)^2.
```

Consequently

```text
Pic^0(D)[3]
 ~= Q_1[3] x Q_2[3]
 ~= (Z/3Z)^4,
# Pic^0(D)[3] = 3^4 = 81.                    (ROOT-81)
```

Thus the residual root ambiguity is finite: at most 81 three-torsion classes.

## 4. No new torsion choices appear on finite formal thickenings

For every nilpotent thickening `D subset D_n`, the small etale sites of `D` and `D_n`
are equivalent.  In characteristic zero, `mu_3` is finite etale.

Therefore restriction induces

```text
H^1_et(D_n,mu_3) ~= H^1_et(D,mu_3).
```

Hence higher formal neighborhoods do not create new discrete `mu_3)-torsor choices.

Combined with Z48's negative-neighborhood linearization, this means the canonical-cover root
ambiguity visible to the formal plumbing is already bounded by the same 81 classes.

This does **not** claim that all 81 classes extend to the actual contracted germ.  The actual
candidate set is a subset of these 81 classes.

## 5. Explicit finite follow-up

Choose the marked point `p_i` as origin on each `Q_i`.  Then the candidate root twists are

```text
tau = (tau_1,tau_2),
tau_i in Q_i[3].
```

Each factor has nine points.  Since `j=1728`, one may pass to a Weierstrass model
`y^2=x^3-x`; its nonzero three-torsion x-coordinates satisfy the division polynomial

```text
psi_3(x)=3x^4-6x^2-1.
```

Therefore Z49 replaces an uncontrolled analytic-root family by a bounded exact task:

```text
<=81 canonical-root twist classes.
```

The next exact adapter should compute which class is realized by the actual cuboid plumbing.
The required source datum is now precise:

```text
the transition character of the canonical line bundle along a symplectic basis
of H_1(Q_1,Z) and H_1(Q_2,Z),
equivalently the two E[3] root classes.
```

Those characters can in principle be extracted from explicit local defining equations / a
trivializing rational 3-canonical form on the Z48 quartic neighborhoods.

## 6. What is and is not closed

Closed by Z49:

```text
continuous edge scalar plumbing moduli,
unbounded formal mu_3 root ambiguity.
```

Still open:

```text
which of the <=81 torsion classes is the actual cuboid canonical root,
whether different torsion classes yield distinct contracted analytic germs,
an explicit index-one cover equation,
local symmetric-Euler/Chern correction.
```

This is a finite replacement receiver for the **canonical-root ambiguity only**.  It is not yet a
finite replacement receiver for the entire MB104 carrier problem.

## External theorem anchors

- Standard generalized-Jacobian normalization sequence for a nodal curve; for a tree dual graph
  the torus factor is trivial.
- Invariance of finite etale covers under nilpotent thickenings; applied to `mu_3)-torsors.
- Patrick Popescu-Pampu, *Numerically Gorenstein surface singularities are homeomorphic to
  Gorenstein ones*: Q-Gorenstein/index data can be encoded by plumbing meromorphic canonical
  forms.  Z49 uses this only as conceptual support for canonical-form plumbing, not as an
  analytic-type classification theorem.

## Firewalls

```text
size48_discrepancy_vector_exact=true
edge_scalar_modulus_remaining=false
canonical_root_candidate_upper_bound=81
higher_formal_mu3_choices_added=false
actual_root_class_identified=false
connected_germ_classified=false
canonical_cover_equation_known=false
local_symmetric_euler_computed=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
