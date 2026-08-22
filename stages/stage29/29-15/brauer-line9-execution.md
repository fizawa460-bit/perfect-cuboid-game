# Stage29-15 — audited bounded execution: seven-line geometric Brauer complement

This is the finite combinatorial and source-certified Ford part of the post-Work input. It does **not** identify the endpoint physical-open Brauer group.

## 1. Arrangement

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

No fourth line passes through any listed triple point, and there are no further intersection points. The exact checker is `verify_brauer_line9.py`.

## 2. Incidence graph

Take the bipartite incidence graph with

```text
7 line vertices
9 intersection-point vertices
```

so

```text
V=16.
```

The six triple points contribute `6*3=18` incidence edges and the three double points contribute `3*2=6`, hence

```text
E=24.
```

The graph is connected. Therefore

```text
b1=E-V+1=24-16+1=9.
```

Independent renewed audit reproduces all nine points, their multiplicities, connectivity and `b1=9`.

## 3. Ford source lock

Primary source:

Timothy J. Ford, *The Brauer Group of an Affine Double Plane Associated to a Hyperelliptic Curve*, Comm. Algebra 45 (2017), 1416--1442, DOI `10.1080/00927872.2016.1175608`, Theorem 1.1 and the line-arrangement discussion immediately following it.

Ford takes one projective component as the line at infinity and the remaining components as affine curves. Over an algebraically closed field, for the coordinate ring obtained by deleting those curves, Theorem 1.1 identifies the `d`-torsion Brauer group with `H_1(Gamma,Z/d)`. In the line-arrangement case the symbol generators are subject exactly to the concurrence relations described there.

For the present seven-line projective divisor choose any one component as the line at infinity. The other six are affine lines, all hypotheses hold over `Qbar`, and with `d=2` the computed graph gives

```text
Br(P2_Qbar - D)[2] ~= H1(Gamma,Z/2) ~= (Z/2)^9.
```

Thus the source-theorem promotion that was provisional in the Work input is now audited.

```text
R29-BR-LINE9=DISCHARGED_SOURCE_CERTIFIED_GEOMETRIC_ARRANGEMENT_COMPLEMENT_BR2
FORD_INCIDENCE_B1=9
GEOMETRIC_ARRANGEMENT_COMPLEMENT_BR2_DIM_F2=9
```

## 4. Firewalls

This theorem is for the **base arrangement complement**. It is not the Brauer group of the endpoint multiquadratic cover or its physical open.

```text
BR_P2BAR_MINUS_D_EQUALS_ENDPOINT_BRAUER=false
GALOIS_DESCENT_DONE=false
MULTIQUADRATIC_COVER_RESIDUES_DONE=false
EXCEPTIONAL_DIVISOR_RESIDUES_DONE=false
PHYSICAL_72_BOUNDARY_ADAPTER_DONE=false
LOCAL_EVALUATION_DONE=false
BRAUER_MANIN_OBSTRUCTION_PROVED=false
```

The exact `(Z/2)^9` result is therefore a finite geometric input to `R29-BR0G/R29-BR2A`, not a discharge of either receiver and not an endpoint nonexistence result.
