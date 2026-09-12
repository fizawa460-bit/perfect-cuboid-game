# Stage32 MB104 — balanced16 zero-quartic stabilizer/union reduction

Status: **RETAINED EXACT SYMMETRY REDUCTION / FIXEDNESS ALL-OR-NONE PER SUPPORT ORBIT / BALANCED16 OPEN / MB104 INCOMPLETE / NO CREDIT**

## Scope

Work only with the displayed uniform genus-one support-span-five ray

```text
D_l = 7l H - 4l sum_{i in Sigma} E_i, |Sigma|=14, l>=1,
```

on the four balanced incidence-16 support orbits. The previous leaves prove that every zero-pairing retained elliptic quartic `Q` satisfies

```text
D_l.Q=0,
O_Q(D_l) ~= O_Q,
```

but do not decide whether the restriction map to `Q` is zero or nonzero.

## Exact support stabilizers

Using the retained order-1536 node action of `Aut(S)`, let `G_Sigma` be the stabilizer of the canonical support `Sigma`. Exact finite replay gives:

```text
support mask       support orbit   |G_Sigma|   zero quartics   orbit on zero quartics
0000770000ff           48              32            4                  4
00007b0000ff           48              32            4                  4
000707000f0f          768               2            2                  2
00070b000f0f          768               2            2                  2
```

Thus in every case `G_Sigma` acts transitively on the complete set of zero-pairing elliptic quartics.

The unique omitted box node on each zero quartic also has only one stabilizer orbit after duplicates are removed:

```text
0000770000ff: omitted nodes {27,31}
00007b0000ff: omitted nodes {26,31}
000707000f0f: omitted nodes {27,35}
00070b000f0f: omitted nodes {26,35}
```

The two omitted nodes are exchanged by the support stabilizer in every representative.

## Node-incidence shape of the zero-quartic union

For the two size-48 support orbits the four zero quartics are exactly the four retained genus-one quartics in the `b1=0` family. Their box-node supports have pairwise overlap sizes

```text
0 or 4,
```

with overlap graph the four-cycle/K2,2 pattern. The two opposite pairs have disjoint box-node supports.

For the two size-768 support orbits there are exactly two zero quartics and their box-node supports are disjoint.

This is a statement about box-node incidence only. It does **not** identify the complete intersection scheme of the strict transforms on the resolution; smooth intersection points away from box nodes remain a separate gluing input.

## Fixed-component consequence

The divisor class `D_l` is invariant under `G_Sigma`. Therefore `G_Sigma` acts linearly on `H^0(S,O(D_l))` and carries the restriction map for one zero quartic to the restriction map for any other zero quartic in its stabilizer orbit.

Because the zero quartics form one stabilizer orbit, their fixed-component status is all-or-none:

```text
one zero quartic is fixed in |D_l|
<=> every zero quartic is fixed in |D_l|.
```

Equivalently, since each target `H^0(Q,O_Q)` is one-dimensional,

```text
rank(H^0(D_l)->H^0(Q,O_Q))
```

is simultaneously `0` for all zero quartics or simultaneously `1` for all zero quartics of the representative support.

This removes the possibility of a mixed fixed/nonfixed zero-quartic configuration.

## Consequence for the next leaf

The remaining decision is genuinely a **union/gluing** problem. It is enough to decide whether the restriction to the complete zero-quartic orbit is identically zero or has nonzero restriction on every component. The next useful computation is therefore:

1. determine the strict-transform intersection scheme of the zero quartics, including smooth intersections away from box nodes;
2. compute the gluing conditions for the componentwise constants in `O_Q(D_l) ~= O_Q`;
3. combine those conditions with the exceptional landing/first-jet data;
4. if necessary, test explicit degree-`7l` global interpolation on the canonical model.

No restriction-map rank is decided here. Balanced16, whole span5 and MB104 remain open; no receiver/theorem/endpoint/Perfect-Cuboid credit and no merge authorization.
