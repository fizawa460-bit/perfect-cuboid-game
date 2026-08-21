# Stage29-02g — exact defect-orbit checkpoint

```text
SCRIPT=stages/stage29/29-02g/defect_orbits.py
ARITHMETIC=EXACT_F2_MATRIX_ENUMERATION
STATUS=PASS
```

Output:

```text
trace_zero_matrices=8
SL2_F2_order=6
orbit size=1 type=zero representative=((0, 0), (0, 0))
orbit size=1 type=identity representative=((1, 0), (0, 1))
orbit size=3 type=nonzero_det0 representative=((0, 0), (1, 0))
orbit size=3 type=det1_nonidentity representative=((0, 1), (1, 0))
orbit_sizes=1,1,3,3
PASS
```

This is a finite group-theory regression only. It does not enumerate endpoint rational points.
