# Stage32 MB104 — `000707000f0f` e=2 Picard-descent half-fiber bridge

Status: **RETAINED EXACT LATTICE BRIDGE / TWO MOD-2 CORRECTIONS IDENTIFIED WITH THE TWO ABSENT HALF-FIBERS / NO CLOSURE / NO CREDIT**

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

## 1. The two absent packets

For the selected absent stabilizer type, let

```text
E_a = sum_(j=16)^23 E_j,
E_b = sum_(j=40)^47 E_j.
```

These are the two eight-node packets on the reduced bad-fiber components `Q_a,Q_b`.  The retained half-fiber relation is

```text
2(Q_a-Q_b) = E_b-E_a                         (HF)
```

in `Pic(S)`.

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

Thus the earlier statement “`H` vanishes in the absent quotient” has precisely two lifts, and they are the two geometric absent packets rather than arbitrary exceptional combinations.

## 3. Half-lifts of the descent class

Because all supported `x_j` are even, both

```text
M_a=(D'-l E_a)/2,
M_b=(D'-l E_b)/2
```

are integral Picard classes.  Their difference is

```text
M_a-M_b
 = l(E_b-E_a)/2
 = l(Q_a-Q_b)                                  (BRIDGE)
```

by `(HF)`.  Put `Delta=Q_a-Q_b`.  Then the entire ambiguity in lifting the exact Picard/2 descent condition is

```text
{M_a,M_b}, with M_a-M_b=l Delta.
```

This is an exact bridge to the retained residual character

```text
eta = O_E(Delta|_E) in Pic^0(E)[2].
```

After restriction to a hypothetical normalization `E`,

```text
O_E((M_a-M_b)|_E)=eta^l.                       (RESTRICT)
```

Hence:

- in the active `e=2` case, `eta=0`, so the two half-lifts have the same restriction;
- in the `e=4` case, an odd `l` makes the two restrictions differ by the nonzero residual character;
- for even `l`, this particular two-choice comparison cannot distinguish `e=2` from `e=4`.

## Route consequence

The Picard/2 descent ambiguity is no longer an unspecified `15`-dimensional absent span.  It is the geometric two-choice torsor

```text
M_a  <->  M_b=M_a-l Delta,
```

whose restriction difference is exactly `eta^l`.  A next exact calculation may therefore evaluate either half-lift on the normalization and recover the other automatically.  Repeating a blind mod-4 descent is not justified: a second divisibility statement would require new geometry beyond `(DIV2)`.

This bridge does not evaluate an individual conductor pair.  It narrows the global obstruction feeding that evaluation to the same single residual half-fiber class already controlling the conductor sheet.

## Firewalls

- No second Picard descent or mod-4 divisibility is assumed.
- No individual conductor loop is assigned `0` or `gamma_Q`.
- No weighted-cut upper bound is proved.
- No `e=2`, `e=4`, or `000707000f0f` closure is claimed.
- No MAIN, receiver, effectivity, theorem, endpoint, or Perfect-Cuboid credit changes.
- No heavy compute and no merge authorization.
