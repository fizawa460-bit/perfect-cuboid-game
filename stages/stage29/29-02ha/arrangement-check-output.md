# Stage29-02ha — exact arrangement / symmetry audit output

The committed `arrangement_check.py` now performs the original incidence calculation plus the fresh audit of projective realizability, cover-lift fields, and node fields of definition using exact rational arithmetic only.

```text
t3=6
t2=3
triple_points=
  (0, 0, 1) ['A1', 'A2', 'B3']
  (0, 1, -1) ['A1', 'B1', 'C']
  (0, 1, 0) ['A1', 'A3', 'B2']
  (1, -1, 0) ['A3', 'B3', 'C']
  (1, 0, -1) ['A2', 'B2', 'C']
  (1, 0, 0) ['A2', 'A3', 'B1']
double_points=
  (1, -1, -1) ['B2', 'B3']
  (1, -1, 1) ['B1', 'B3']
  (1, 1, -1) ['B1', 'B2']
projective_arrangement_aut_order=24
projective_arrangement_aut_group=S4
Q_liftable_base_aut_order=6
Q_liftable_base_aut_group=S3
Q_line_orbits=[3:{A1,A2,A3}, 3:{B1,B2,B3}, 1:{C}]
Q(i)_liftable_base_aut_order=24
Q(i)_line_orbits=[4:{A1,A2,A3,C}, 3:{B1,B2,B3}]
sign_deck_order=64
geometric_sign_semidirect_order=64*24=1536
Q_defined_sign_semidirect_order=64*6=384
node_field_split=24_Q_plus_24_strict_Q(i)
odd_characteristic_projective_complement_count=(p-3)^2
PASS
```

The key audit distinction is now exact. All 24 incidence automorphisms are genuine `PGL_3(Q)` automorphisms of the **base arrangement**, but only the six coordinate-permutation transformations have a common rational squareclass multiplier on all seven branch forms and hence lift to the cuboid sign cover over `Q`. For the other eighteen transformations the only multiplier obstruction is `-1`, so all 24 lift over `Q(i)`.

This recovers the arithmetic orbit split

```text
Q:     3 + 3 + 1
Q(i):  4 + 3
```

and the source-locked full geometric automorphism order `1536=64*24` from the sign-cover model itself.

The same exact squareclass calculation at the six triple fibers gives three fibers with eight `Q`-defined nodes each and three fibers with eight nodes requiring `i`, hence the independently known split `24/Q + 24/Q(i)`.

```text
ARRANGEMENT_EXACT_CHECK=PASS
PROJECTIVE_S4_REALIZATION=PASS
Q_LIFT_SUBGROUP=S3
QI_LIFT_GROUP=S4
R29_KUM2A_ARITHMETIC_ORBIT_SCOPE=PASS
NODE_FIELD_SPLIT_AUDIT=PASS
```
