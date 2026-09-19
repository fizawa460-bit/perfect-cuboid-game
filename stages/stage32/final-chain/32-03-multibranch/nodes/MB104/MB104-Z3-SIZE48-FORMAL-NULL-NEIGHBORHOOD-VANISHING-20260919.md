# MB104 Z3 — size-48 formal null-neighborhood vanishing — 2026-09-19

Status: **PARALLEL EXACT FORMAL-PICARD NO-GO / NO CREDIT**

## Scope

This is a Z1--Z30 re-audit continuation, specifically Z3 (complete null-locus / stable-base / cone direction).

It does not follow the active Z34/Z35 route.  It uses the exact Z33G null-union geometry for the two surviving size-48 balanced support orbits:

```text
0000770000ff
00007b0000ff
```

Z33G proves that their four zero-pairing elliptic quartics are pairwise disjoint and are joined only by the repeated omitted exceptional curves into two tree components

```text
Q_1 -- E -- Q_2.
```

There is no dual-graph cycle.

## One connected tree component

Let

```text
U = Q_1 + E + Q_2
```

on the smooth cuboid resolution.

Retained intersection data:

```text
Q_j^2 = -4,
E^2   = -2,
Q_1.E = Q_2.E = 1,
Q_1.Q_2 = 0.
```

Therefore

```text
U.Q_j = -3,
U.E   = 0.
```

For every integer n>=1,

```text
L_n := O_U(-nU)
```

has component degrees

```text
deg(L_n|Q_j)=3n,
deg(L_n|E)=0.
```

Each Q_j is elliptic, so

```text
H^1(Q_j,L_n|Q_j)=0
```

because 3n>0.  Also E~=P1 and

```text
H^1(E,O_E)=0.
```

## Normalization sequence

Normalize the nodal tree U.  For L_n the standard exact sequence is

```text
0 -> L_n
  -> L_n|Q_1 direct_sum L_n|E direct_sum L_n|Q_2
  -> k_{p_1} direct_sum k_{p_2}
  -> 0.
```

The evaluation map on H^0 is surjective:

- a degree-3n line bundle on an elliptic curve is globally generated for n>=1;
- hence the Q_1 section value at p_1 can be chosen arbitrarily;
- independently the Q_2 section value at p_2 can be chosen arbitrarily.

Thus the two node discrepancies can be prescribed independently, regardless of the constant section on E.

Consequently

```text
H^1(U,O_U(-nU)) = 0
```

for every n>=1.

The full size-48 null union is the disjoint union of two such trees, so the same vanishing holds on the complete retained null union.

## Formal Picard consequence

Because U is a Cartier divisor on the smooth surface,

```text
I_U^n/I_U^(n+1) ~= O_U(-nU).
```

For successive infinitesimal neighborhoods, the units sequence gives the Picard transition kernel from the additive group

```text
H^1(U,O_U(-nU)).
```

The vanishing above therefore shows that

```text
Pic((n+1)U) -> Pic(nU)
```

has zero infinitesimal kernel for every n>=1.  Since H^2 of a coherent sheaf on the curve U vanishes, the transition is in fact an isomorphism at each step.

Z33E/Z33G already give

```text
O_U(P) ~= O_U.
```

Hence the ambient line bundle class O(P) restricts trivially to every finite infinitesimal neighborhood nU:

```text
O_{nU}(P) ~= O_{nU}
```

for all n>=1, and likewise for every multiple lP.

## Interpretation

For the two size-48 balanced support orbits, the null-locus line-bundle route is exhausted not only at ordinary Pic^0 level but at every finite formal-neighborhood order.

Therefore no exclusion of these two orbits can come from:

```text
componentwise restriction,
tree gluing,
first-normal restriction,
higher finite formal Picard gluing.
```

A future Z3 attack on the size-48 orbits must use information outside formal restriction of O(lP) to the retained null trees--for example a genuinely global effective-cone contraction theorem or a new null component creating a cycle.

This does not construct a carrier and does not close the orbits.

## Z3 routing consequence

The current formal-null-locus split is now:

```text
00070b000f0f (768): excluded by non-torsion Pic0 cycle holonomy.
000707000f0f (768): ordinary cycle holonomy trivial; first/higher normal cycle data remain the only formal-gluing possibility.
0000770000ff (48): all finite formal Picard neighborhood obstructions vanish.
00007b0000ff (48): all finite formal Picard neighborhood obstructions vanish.
```

Thus any further formal-gluing effort should be concentrated only on the surviving size-768 orbit.

## Source locks

- Z33G note blob `14c1661c5a3b1975474c1f983ed08b29c2150731`;
- Z33G certificate blob `62374fbb19092a2a4a5630fb86b37ddb4924ca29`;
- Z33E note blob `57fa113b33ed827fd8b5d619b232ec16cdf85a8c`.

## Firewalls

```text
size48_orbits_excluded=false
formal_picard_obstruction_size48=false
surviving_768_first_normal_obstruction_computed=false
remaining_balanced_support_count=864
whole_uniform_ray_closed=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
