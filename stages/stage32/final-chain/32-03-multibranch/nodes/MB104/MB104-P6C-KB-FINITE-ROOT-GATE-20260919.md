# MB104 P6C — Kb finite root gate — 2026-09-19

Status: **PRE-AUDIT EXACT FINITE GATE / W4 COORDINATE-QUOTIENT ROOT ARCHITECTURE CLOSED NEGATIVELY ON CURRENT P6 SURVIVOR / NO CREDIT**

## Input

Current hostile full-span support:

```
Sigma = 0000093f442e
```

P6B already closes all four Kc-type coordinate quotients and leaves only:

```
b1: possible negative root degree 2,
b2: possible negative root degree 2 or 3,
b3: possible negative root degree 2.
```

The retained Kb no-line proof removes degree 1.

## Quotient-node weights

For a coordinate-sign quotient, only box nodes with nonzero forgotten coordinate map to quotient singular points. Pair support nodes under the sign involution; the projected coefficient is the number of supported preimages in the pair.

The exact survivor weights are

```
b1: [2,2,1,1,1,1],       total 8
b2: [2,2,2,2,1,1,1,1],   total 12
b3: [2,1,1,1,1,1,1],     total 8
```

For a smooth curve meeting a quotient A1 point simply, the pushdown pairing has the form

```
P.R = 14 d - 4 W,
```

where `d` is the hyperplane degree and `W` is the weighted supported quotient-node incidence.

Thus

```
degree 2 negative => W >= 8,
degree 3 negative => W >= 11.
```

## Conics

An integral degree-two projective curve is a smooth plane conic. Therefore it spans a `P^2`, and at every quotient A1 point it meets, its strict transform has exceptional contact one.

Exact projective-rank enumeration of every subset whose weight is at least 8 gives:

```
b1: minimum vector rank = 5   -> projective span >= P4
b2: minimum vector rank = 4   -> projective span >= P3
b3: minimum vector rank = 6   -> projective span >= P5
```

A conic would require vector rank at most 3.

Therefore no Kb quotient has a negative degree-two root.

## The b2 cubic

Only `b2` permits degree three by the root-degree bound.

An integral degree-three curve spans either a plane or a `P^3`.

A plane cubic cannot lie on the singular Kb complete intersection: every defining quadric restricted to its plane would vanish on the integral cubic, hence vanish identically on the plane. The plane would then be a two-dimensional irreducible component of Kb, contradicting that this quotient is an integral K3 surface.

Therefore an integral degree-three curve on Kb is nondegenerate in `P^3`, hence a twisted cubic. It is smooth, so its contacts with quotient A1 nodes are simple.

For `b2`, exact enumeration of every quotient-node subset of weighted mass at least 11 gives

```
minimum vector rank = 6,
```

i.e. projective span at least `P^5`.

A twisted cubic spans `P^3`, vector rank at most 4.

Hence no negative degree-three root exists.

## W4 disposition on the current survivor

Combining P6B and P6C:

```
a1,a2,a3,c: no negative Kc root
b1,b2,b3:   no negative Kb root
```

So the **seven coordinate-sign quotient negative-root architecture** produces no fixed component for the current P6 survivor.

This is a clean negative closure of the revived W4 architecture on this support. It does not prove the survivor nef, and it does not close the broader K3/effective-cone direction.

## Next routing

Do not spend more cycles cataloguing low-degree test curves or coordinate-sign quotient roots.

The next P6 route must use a genuinely different packet-sensitive invariant. High-value retained options remain:

- W16-type branch/conductor/Cayley--Bacharach architecture, only if a valid P6 adapter exists;
- W26 cuboid-specific equisingular/T-smoothness;
- W6 coupled two-factor modular relation;
- a new global singularity/passport mechanism.

The next leaf should first test adapter availability, not assume the span-P5 residual-cover packet transfers to P6.

## Firewalls

```
finite_degree_window_proved=false
MB104_complete=false
R29_LG2_MB_discharged=false
receiver_credit=false
effectivity_final_milestone_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
