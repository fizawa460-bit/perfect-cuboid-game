# MB104 Z49 — canonical-cover discriminant character from explicit plumbing — 2026-09-19

Status: **PRE-AUDIT EXACT TOPOLOGICAL/CLASS-GROUP COVER REDUCTION / NO CREDIT**

## Purpose

Z48 replaces the arbitrary-analytic-germ input by explicit marked negative elliptic plumbing data.
Z49 asks for the first invariant of the degree-three canonical index-one cover that can be obtained
without yet knowing the complete analytic multiplication table.

The answer is the local discriminant/class-group character.

## 1. Size-48 Q-E-Q component

In basis (Q1,E,Q2), the exceptional intersection matrix is

```
M48 =
[-4  1  0
  1 -2  1
  0  1 -4].
```

Its determinant is `-24`.

The gcd of all matrix entries is one and the gcd of all 2x2 minors is one, so the Smith form is

```
diag(1,1,24).
```

Hence the discriminant group of the lattice is cyclic:

```
A48 = L48^*/L48 ~= Z/24.
```

The canonical pairing vector is

```
(K.Q1,K.E,K.Q2)=(4,0,4).
```

Solving `M48 a = (4,0,4)^T` gives

```
a=(-4/3,-4/3,-4/3).
```

Modulo the integral lattice this class has exact order three.

Therefore the canonical index-three class is the unique order-three subgroup direction in the cyclic
discriminant group `Z/24`.  Up to deck-generator inversion, the associated degree-three topological
canonical-cover character is unique.

The fractional discrepancy on each of Q1,E,Q2 is `2/3`; equivalently every component meridian
has the same nonzero character in `Z/3`, up to simultaneous inversion.

## 2. Size-768 connected component

In basis (A,B,E_A,E_B),

```
M768 =
[-4  2  1  0
  2 -4  0  1
  1  0 -2  0
  0  1  0 -2].
```

Its determinant is `33`.

The gcds of the 1x1, 2x2 and 3x3 minors are all one, hence

```
SNF(M768)=diag(1,1,1,33),
A768 ~= Z/33.
```

The canonical discrepancy vector is

```
a=(-8/3,-8/3,-4/3,-4/3).
```

Again its class has exact order three.

Thus the canonical degree-three cover direction is unique in the cyclic discriminant group
`Z/33`, up to inversion of the deck generator.

The fractional discrepancy characters split as

```
A,B       : 1/3 mod Z,
E_A,E_B   : 2/3 mod Z,
```

again only up to simultaneous `1 <-> 2` deck inversion.

## 3. Consequence

Z43 previously retained only

```
degree-three canonical cover exists.
```

Z48+Z49 now retain

```
- explicit negative elliptic component neighborhoods,
- explicit marked plumbing graph,
- cyclic discriminant group,
- exact order-three canonical class,
- unique degree-three discriminant-cover direction,
- componentwise meridian character pattern.
```

So the next analytic problem is no longer to choose an arbitrary index-three cover.  It is to realize
the **unique lattice/topological canonical cover** on the explicit plumbing and determine its
holomorphic gluing/multiplication.

## 4. What is not yet proved

The lattice discriminant group is not automatically the full analytic local divisor class group, and
topological uniqueness of the order-three cover does not by itself produce:

```
a hypersurface equation,
a complete-intersection equation,
the canonical algebra multiplication,
local Chern/Euler coefficients.
```

Those remain analytic questions.

No quotient/lc/klt identification is made.

## 5. Next leaf

```
MB104-Z49B-SIZE48-PLUMBING-INDEX3-HOLOMORPHIC-LIFT
```

Use size-48 first.

The input is now exceptionally rigid:

```
E1,E2: j=1728,
N_Ei=O(-4p_i),
bridge: P1(-2),
one transverse marked attachment on each elliptic component,
canonical meridian character: nonzero and equal on all three components.
```

Target: write local plumbing transition functions and determine whether the unique topological
Z/3 cover has a unique holomorphic lift.  If a modulus remains, identify it as an explicit C* or
Pic^0 parameter and test whether the cuboid equations fix it.

## Firewalls

```
canonical_discriminant_character_exact=true
topological_degree3_cover_direction_unique=true
analytic_holomorphic_lift_unique=false
canonical_cover_equation_known=false
local_euler_reopened=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
