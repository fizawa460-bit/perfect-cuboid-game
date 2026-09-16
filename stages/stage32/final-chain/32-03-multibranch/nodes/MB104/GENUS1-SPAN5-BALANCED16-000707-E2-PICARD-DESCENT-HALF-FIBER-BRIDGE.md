# Stage32 MB104 — `000707000f0f` e=2 Picard-descent half-fiber bridge

Status: **RETAINED EXACT LATTICE BRIDGE / TWO CANONICAL MOD-2 CORRECTIONS / GEOMETRIC BRIDGE CONDITIONAL ON PACKET ADAPTER / NO CLOSURE / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

The preceding exact Picard/2 verifier proved that the descent condition for

```text
D' = 7l H + sum_(j in Sigma) (x_j-8l) E_j
```

forces every one of the fourteen supported allocations `x_j` to be even.  It also found that `H` maps to zero after quotienting by the sixteen absent exceptional classes.  This note identifies the latter statement exactly and relates its only ambiguity to the already-retained residual half-fiber character.

## 1. The two canonical absent packets

For the selected absent stabilizer type, let

```text
E_a = sum_(j=16)^23 E_j,
E_b = sum_(j=40)^47 E_j.
```

The exact lattice calculation below singles out these two numerical packets.  The prior geometric half-fiber leaf supplies abstract eight-node sets `T_a,T_b` on reduced bad-fiber components `Q_a,Q_b`, with relation

```text
2(Q_a-Q_b) = sum_(p in T_b)E_p-sum_(p in T_a)E_p  (HF)
```

in `Pic(S)`.  The retained chain does not yet contain an executable node-label/fibration adapter proving that the ordered numerical packets `(16..23,40..47)` are the ordered geometric packets `(T_a,T_b)` for one displayed fibration.  Every use of `(HF)` with `E_a,E_b` below is therefore conditional on

```text
PACKET: E_a=sum_(p in T_a)E_p and E_b=sum_(p in T_b)E_p,
```

up to simultaneous interchange of `a,b`.

## 2. Exact retained-lattice computation

Using the saturated retained Picard64 marking—not displayed ambient coefficients—the verifier proves

```text
H-E_a in 2 Pic(S),
H-E_b in 2 Pic(S).                              (DIV2)
```

Define the two integral classes

```text
L_a=(H-E_a)/2,
L_b=(H-E_b)/2.
```

The sixteen absent exceptional classes have rank `15` modulo two.  The unique relation is the sum of all sixteen classes, and the two solutions of

```text
H = sum c_j E_j  in Pic(S)/2Pic(S)
```

are exactly

```text
c_j=1 on {16,...,23}, 0 otherwise,
c_j=1 on {40,...,47}, 0 otherwise.
```

Thus the earlier statement “`H` vanishes in the absent quotient” has precisely two **mod-two correction supports**, represented canonically by the two displayed numerical packets.  This does not say that all integral lifts form a two-element set: adding twice an integral absent divisor changes an integral representative without changing its mod-two support.

## 3. Half-lifts of the descent class

Because all supported `x_j` are even, both

```text
M_a=(D'-l E_a)/2,
M_b=(D'-l E_b)/2
```

are integral Picard classes.  Their unconditional exact lattice relation is

```text
2(M_a-M_b)=l(E_b-E_a).                         (LATTICE-BRIDGE)
```

Conditional on `(PACKET)`, their difference is

```text
M_a-M_b
 = l(E_b-E_a)/2
 = l(Q_a-Q_b)                                  (BRIDGE)
```

by `(HF)`.  Put `Delta=Q_a-Q_b`.  The two canonical representatives then obey

```text
M_a-M_b=l Delta.
```

This is a conditional bridge to the retained residual character

```text
eta = O_E(Delta|_E) in Pic^0(E)[2].
```

After restriction to a hypothetical normalization `E`,

```text
O_E((M_a-M_b)|_E)=eta^l.                       (RESTRICT)
```

Hence, conditional on `(PACKET)`:

- in the active `e=2` case, `eta=0`, so the two half-lifts have the same restriction;
- in the `e=4` case, an odd `l` makes the two restrictions differ by the nonzero residual character;
- for even `l`, this particular two-choice comparison cannot distinguish `e=2` from `e=4`.

## 4. Singular-carrier consequence

Let `C` be the hypothetical singular carrier and `nu:E->C` its normalization.  The retained half-branch class is

```text
L_abs=Delta+sum_(p in T_a)E_p.
```

The carrier is disjoint from every absent exceptional curve, so `O_C(Delta|_C) ~= O_C(L_abs|_C)`.  In the `e=2` case this residual line bundle is the generalized-Jacobian gluing class

```text
kappa in Ker(Pic(C)[2] -> Pic(E)[2]).
```

Consequently, conditional on `(PACKET)`,

```text
O_C((M_a-M_b)|_C) ~= kappa^l.                 (SINGULAR-BRIDGE)
```

For odd `l` the ratio of the two canonical half-lifts on `C` is exactly `kappa`; for even `l` it is trivial.  Pullback to `E` kills `kappa`, explaining why normalization-only Picard or Abel--Jacobi calculations cannot evaluate a conductor loop.

## Route consequence

The Picard/2 correction support is no longer an unspecified `15`-dimensional absent span: it has the two canonical numerical representatives `M_a,M_b`.  Conditional on `(PACKET)`, their geometric difference is

```text
M_a  <->  M_b=M_a-l Delta.
```

The normalization restriction difference is `eta^l`, but normalization forgets the load-bearing gluing class `kappa`.  The useful next calculation is instead a descent/linearization comparison on the **singular carrier** for odd `l`, or directly the retained one-coordinate conductor evaluator.  Both require branch-specific conductor data.  Repeating a blind mod-4 descent is not justified.

This bridge does not evaluate an individual conductor pair.  It narrows the global obstruction feeding that evaluation to the same single residual half-fiber class already controlling the conductor sheet.

## Firewalls

- No second Picard descent or mod-4 divisibility is assumed.
- No numerical packet is unconditionally identified with an ordered geometric half-fiber packet.
- No claim that all integral lifts form a two-element set.
- No individual conductor loop is assigned `0` or `gamma_Q`.
- No weighted-cut upper bound is proved.
- No `e=2`, `e=4`, or `000707000f0f` closure is claimed.
- No MAIN, receiver, effectivity, theorem, endpoint, or Perfect-Cuboid credit changes.
- No heavy compute and no merge authorization.
