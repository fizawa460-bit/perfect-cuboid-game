# Stage14-numα11-diag5 — family / same-diagonal dependence diagnostic

## Result

This stage tests whether the late B500m shell-direction movement is mainly an artifact of dependent candidate groups rather than a direction-law effect.

The exact source remains the merged `3495`-row B500m exactly-two census. No new census is performed.

### Same space diagonal multiplicity

There are `3325` distinct space diagonals among the `3495` objects. Only `166` diagonals repeat: `162` carry two objects and `4` carry three. Thus `336/3495` objects lie on repeated diagonals and the maximum multiplicity is only `3`.

Raw cumulative direction ratios:

```text
(a,b,c) = (0.3931330, 0.3922747, 0.2145923)
```

After giving every distinct `d` total weight one:

```text
(a,b,c) = (0.3924812, 0.3937845, 0.2137343)
```

So repeated-diagonal weighting has almost no effect on the cumulative 2:2:1-like pattern.

For the previously highlighted `(300m,400m]` versus `(400m,500m]` contrast, the raw L2 direction shift is `0.1223201`. Equal weighting per `d` gives `0.1239583`, slightly larger rather than smaller.

### Primitive-face overlap graph clusters

Using the exact Stage14 primitive-face graph as an operational dependency proxy gives:

```text
vertices             = 5082
edges                = 3495
connected components = 1703
largest component    = 95 edges
```

Most components are tiny (`1191` are isolated one-edge components), although a small number of larger connected families exist.

Equal weighting per connected component changes the cumulative direction ratios to

```text
(a,b,c) = (0.3780926, 0.3858789, 0.2360284)
```

but does **not** remove the late-shell movement. Its L2 shift becomes `0.1410303`, larger than the raw value.

Progressively removing the largest connected components also fails to collapse the late shift:

```text
raw                      0.1223201
remove largest 1         0.1185070
remove largest 2         0.1130240
remove largest 5         0.1183247
```

Therefore the visible 300–500m direction jump is not driven by one or a few giant graph components under this exact proxy.

## Interpretation

The two simplest dependence explanations tested by diag5 fail:

1. several candidates sharing the same space diagonal do not create the observed shell movement;
2. a few large primitive-face graph families do not create it either.

This does **not** prove object independence, and a graph connected component is not asserted to be a true parametric family. It only removes two concrete finite-data confounders.

The next useful diagnostic is therefore not finer shell slicing. It is a matched Stage13/Stage14 comparison: place exactly-one and exactly-two populations under the same cutoff, shell and direction conventions and ask where the Stage13 direction law changes on passage to the second face.

```text
STAGE14_NUM_ALPHA11_DIAG5=SAME_DIAGONAL_AND_GRAPH_CLUSTER_DEPENDENCE_DIAGNOSTIC_COMPLETE
SOURCE_B500M_ROWS=3495
DISTINCT_SPACE_DIAGONALS=3325
REPEATED_SPACE_DIAGONALS=166
MAX_OBJECTS_PER_SPACE_DIAGONAL=3
PRIMITIVE_FACE_GRAPH_COMPONENTS=1703
MAX_COMPONENT_EDGES=95
RAW_LATE_SHIFT_L2=0.12232012942880242
EQUAL_D_LATE_SHIFT_L2=0.1239582638610805
EQUAL_COMPONENT_LATE_SHIFT_L2=0.14103029428645789
SAME_DIAGONAL_MULTIPLICITY_MATERIALLY_REDUCES_LATE_SHIFT=false
GRAPH_COMPONENT_EQUAL_WEIGHT_MATERIALLY_REDUCES_LATE_SHIFT=false
FEW_LARGEST_COMPONENTS_DRIVE_LATE_SHIFT=false
IID_ARITHMETIC_OBJECTS_CLAIM=false
ASYMPTOTIC_CLAIM=false
NEXT=Stage14-num-alpha11-diag6 matched Stage13 exactly-one versus Stage14 exactly-two comparison
```
