# Stage29-15 — bounded execution: seven-line Brauer incidence precursor

This is the finite combinatorial part of the post-audit Ford input. It does **not** identify the endpoint physical-open Brauer group.

## Arrangement

Use the seven projective lines

```text
Lx   : x=0
Ly   : y=0
Lz   : z=0
Lxy  : x+y=0
Lxz  : x+z=0
Lyz  : y+z=0
Ls   : x+y+z=0
```

All pairwise intersections collapse to exactly nine geometric intersection points.

### Six triple points

```text
[0:0:1]    : Lx, Ly, Lxy
[0:1:0]    : Lx, Lz, Lxz
[1:0:0]    : Ly, Lz, Lyz
[0:1:-1]   : Lx, Lyz, Ls
[1:0:-1]   : Ly, Lxz, Ls
[1:-1:0]   : Lz, Lxy, Ls
```

### Three ordinary double points

```text
[1:-1:-1]  : Lxy, Lxz
[1:-1:1]   : Lxy, Lyz
[1:1:-1]   : Lxz, Lyz
```

No fourth line passes through any listed triple point, and there are no further intersection points.

## Incidence graph

Take the bipartite incidence graph with

```text
7 line vertices
9 intersection-point vertices
```

so

```text
V = 16.
```

The six triple points contribute `6*3=18` incidence edges and the three double points contribute `3*2=6`, hence

```text
E = 24.
```

The graph is connected (for example the three coordinate lines are joined through the coordinate triple points, each sum line meets them, and `Ls` meets three mixed triples). Therefore

```text
b1 = E - V + 1 = 24 - 16 + 1 = 9.
```

The exact checker is `verify_brauer_line9.py`.

## Receiver disposition

Conditional on renewed audit source-locking the exact Ford line-arrangement theorem in the form reported by the external Work search, this gives the geometric precursor

```text
R29-BR-LINE9=EXECUTED_FINITE_INCIDENCE_PRECURSOR
FORD_INCIDENCE_B1=9
GEOMETRIC_SYMBOL_SPACE_DIM_F2=9   # source-theorem promotion pending renewed audit
```

Firewalls:

```text
BR_P2BAR_MINUS_D_EQUALS_ENDPOINT_BRAUER=false
GALOIS_DESCENT_DONE=false
MULTIQUADRATIC_COVER_RESIDUES_DONE=false
EXCEPTIONAL_DIVISOR_RESIDUES_DONE=false
PHYSICAL_72_BOUNDARY_ADAPTER_DONE=false
LOCAL_EVALUATION_DONE=false
BRAUER_MANIN_OBSTRUCTION_PROVED=false
```

Thus this execution supplies a finite exact input to `R29-BR0G/R29-BR2A`; it does not discharge either parent receiver.
