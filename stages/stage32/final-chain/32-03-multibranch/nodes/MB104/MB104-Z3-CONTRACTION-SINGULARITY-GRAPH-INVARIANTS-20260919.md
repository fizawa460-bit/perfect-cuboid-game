# MB104 Z3 — exact contraction-graph invariants after semiampleness — 2026-09-19

Status: **PARALLEL PRE-AUDIT EXACT GRAPH-INVARIANT CHECKPOINT / NO CREDIT**

## Purpose

Assume the pre-audit Z3 Birkar gate: the balanced primitive ray P is semiample and defines a
birational contraction whose exceptional locus is exactly Null(P).

Compute the connected exceptional graphs and their basic numerical invariants.  This determines
what sort of singularities a Z2/Z12 continuation would actually face.

## 1. Isolated unsupported exceptional curves

Every unsupported exceptional curve not attached to a zero elliptic quartic is a single

```text
E ~= P1,  E^2=-2,  K.E=0.
```

Its contraction is the usual A1 numerical configuration.

Each surviving balanced support has 32 such isolated curves after removing the two unsupported
exceptionals participating in the nontrivial quartic-containing components.

## 2. Size-48 support orbits

For either

```text
0000770000ff
00007b0000ff
```

the four zero elliptic quartics and the two repeated omitted exceptionals form two disjoint
connected trees, each with graph

```text
Q_1(-4,g=1) -- E(-2,g=0) -- Q_2(-4,g=1).
```

The intersection matrix is

```text
[-4  1  0
  1 -2  1
  0  1 -4]
```

with determinant -24 and is negative definite.

The reduced cycle

```text
Z=Q_1+E+Q_2
```

satisfies

```text
Z.Q_1=-3,
Z.E=0,
Z.Q_2=-3,
```

so it is already the fundamental positive anti-nef cycle.

Its invariants are

```text
Z^2=-6,
K.Z=8,
p_a(Z)=1+(Z^2+K.Z)/2=2.
```

Thus this connected contraction is not a simple elliptic exceptional graph (whose fundamental
cycle has arithmetic genus one).

### Numerical discrepancy vector

If the contracted singularity is Q-Gorenstein, writing

```text
K_S = phi^* K_Y + a_1 Q_1 + a_E E + a_2 Q_2
```

and intersecting with the exceptional curves gives uniquely

```text
a_1=a_E=a_2=-4/3.
```

Hence any Q-Gorenstein realization has discrepancies below -1 and is not log canonical.

There are two such connected singular points per size-48 support orbit.

## 3. Surviving size-768 orbit

For

```text
000707000f0f
```

the two zero elliptic quartics A,B meet transversely at two smooth points.  Each has one
unsupported exceptional (-2)-curve attached as a leaf.

The connected graph has intersection data

```text
A^2=B^2=-4,
A.B=2,
A.E_A=1,
B.E_B=1,
E_A^2=E_B^2=-2,
```

and no other intersections.

In basis (A,B,E_A,E_B), the matrix is

```text
[-4  2  1  0
  2 -4  0  1
  1  0 -2  0
  0  1  0 -2]
```

with determinant 33 and is negative definite.

The reduced cycle

```text
Z=A+B+E_A+E_B
```

has

```text
Z.A=Z.B=Z.E_A=Z.E_B=-1,
```

so it is the fundamental anti-nef cycle.

Its invariants are

```text
Z^2=-4,
K.Z=8,
p_a(Z)=1+(Z^2+K.Z)/2=3.
```

### Numerical discrepancy vector

Under the same Q-Gorenstein conditional interpretation,

```text
a_A=a_B=-8/3,
a_EA=a_EB=-4/3.
```

Again the singularity would be strictly worse than log canonical.

There is one such connected nonrational contraction point, plus 32 isolated A1 configurations.

## 4. Canonical-square checksum

The discrepancy-square contribution of the nonrational connected exceptional locus is

```text
-64/3
```

for either support type:

- size48: two tree components, each contributes -32/3;
- size768: the single four-component graph contributes -64/3.

Thus, conditionally when K_Y is Q-Cartier,

```text
K_Y^2 = K_S^2 - (discrepancy exceptional part)^2
      = 16 + 64/3
      = 112/3.
```

The equality across the two support types is a useful consistency checksum, not a closure theorem.

## 5. Consequence for Z12/Z2 routing

The actual P-contraction does **not** replace the zero quartics by isolated simple-elliptic (-4)
singularities.

The full connected exceptional graphs have fundamental genera 2 or 3 and, in any Q-Gorenstein
interpretation, discrepancies below -1.

Therefore:

- log-canonical extension theorems cannot simply be imported to the full P-contraction;
- the earlier one-quartic epsilon_4 thought experiment remains only a local auxiliary contraction,
  not the exact global semiampleness contraction;
- any symmetric-differential local-Euler calculation should use these complete graphs if it is meant
  to describe the actual contracted model.

## Firewalls

```text
Q_Gorenstein_of_contracted_model_not_proved=true
discrepancy_values_are_conditional_on_Q_Gorenstein=true
P_contraction_exists_pre_audit=true
surviving_orbits_excluded=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
