# Stage29-02ha — exact arrangement regression output

The committed `arrangement_check.py` was independently re-derived with exact integer arithmetic before packaging.

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
incidence_automorphism_group_order=24
incidence_automorphism_group=S4 via faithful action on {A1,A2,A3,C}
line_orbits=[4:{A1,A2,A3,C}, 3:{B1,B2,B3}]
odd_characteristic_projective_complement_count=(p-3)^2
node_count=6*(64/8)=48
```

The `S4` statement is a statement about the **base line arrangement incidence symmetry**. It is not automatically a Q-defined automorphism group of the full cuboid cover: lifting the transformations that mix an `A_i` line with `C` requires auditing the square-root cocycle, and Testa–Stoll's extra geometric automorphism visibly involves `i`.

```text
ARRANGEMENT_EXACT_CHECK=PASS
FULL_Q_LIFT_OF_BASE_S4_NOT_CLAIMED=true
```
