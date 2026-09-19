# MB104 P6O — modular fixed-point branch-label adapter preflight wall — 2026-09-19

Status: **PRE-AUDIT BOUNDED EXTERNAL-SOURCE INTERFACE WALL / NO CREDIT**

## Target

P6N showed that the retained Stage32 48-node model identifies only the three inertia/stabilizer types. P6O checks the published modular/theta description for the missing factorwise map

```text
box node
  -> (individual branch value of C8/G in factor 1,
      individual branch value of C8/G in factor 2).
```

## Published source checked

E. Freitag and R. Salvati Manni, *Parametrization of the box variety by theta functions*, arXiv:1303.6495, especially Theorem 2.4, Proposition 2.5 and the surrounding Satake-boundary discussion.

The paper gives:

- `C8 = H*/Gamma[8]`;
- `Gamma[4]/Gamma[8] ~= (Z/2)^3`;
- the diagonal quotient model of the box variety;
- the 48 singular nodes as images of fixed points of this group;
- their images over the three diagonal cusps of `X(2) x X(2)`, represented by
  `(infinity,infinity), (0,0), (1,1)`;
- the theta parametrization identifying these three stabilizer types with the three zero coordinates `Z1,Z2,Z3`.

This is exactly the information already adapted by the retained node-stabilizer source note.

## Missing factorwise refinement

For P6N one needs a finer datum. Each of the three `X(2)` cusp types lifts to two branch values in the degree-eight single-factor quotient

```text
C8 -> C8/(Gamma[4]/Gamma[8]) ~= X(4) ~= P1.
```

The inspected published formulas do not provide a table matching the explicit Stage32 48-node coordinates/indexing to those two `X(4)` cusp values separately in each factor.

Proposition 2.5 identifies the three diagonal `X(2)` cusp fibres and the stabilizing group element, but does not refine the 48 singular nodes into the desired four cells per inertia type:

```text
(two X(4) branch values in factor 1)
  x
(two X(4) branch values in factor 2).
```

The Satake-boundary discussion likewise identifies boundary components and cusp incidence, but no exact Stage32 node-index -> ordered factor cusp-pair adapter is supplied.

Therefore constructing such a table would require a new modular cusp computation, not a shallow import of an already stated source fact.

## Disposition

```text
published modular identification of three inertia types = available,
factorwise six-branch-value node labels              = not directly available,
P6N 2x2 incidence restart                            = not authorized.
```

P6O is parked. No branch label is inferred from `c=0`, eight-node blocks, signs, or automorphism symmetry.

## Next invariant

Rotate away from cusp-label reconstruction. The retained exact two-factor result P6H gives two degree-`56l` pencils on the same elliptic normalization and in the same line bundle

```text
M1 ~= M2 = M.
```

The next shallow isolated-carrier gate is

```text
MB104-P6P-ELLIPTIC-TWO-PENCIL-WRONSKIAN-RIGIDITY-PREFLIGHT.
```

Target: determine whether two base-point-free `g^1_{56l}` inside the same `H^0(E,M)`, together with the retained typewise ramification constraints, can be forced into a finite or automorphism-related family by a source-complete Wronskian/ramification theorem. Stop immediately if the general Wronski map has positive-dimensional fibres or the retained constraints are only divisor-class data.

## Firewalls

```text
factorwise_branch_label_adapter_constructed=false
P6N_incidence_reopened=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
