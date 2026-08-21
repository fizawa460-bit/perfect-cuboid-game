# Two `S4`-orbits of Campedelli quotient kernels

The exact kernel enumeration produces ten rank-3 subgroups of the six-dimensional sign deck group. The audited arrangement automorphism group `Aut_P2(D) ~= S4` acts on this ten-element set with orbit sizes

```text
8 + 2.
```

This is stronger than merely counting 1680 admissible labelings: target `GL(3,F2)` has already been divided out, so each of the ten objects is a distinct kernel subgroup.

## Orbit I — size 8

Representative branch labels:

```text
A1 001
A2 010
A3 011
B3 100
B2 110
B1 111
C  101
```

An upstairs `F2^7` kernel basis is

```text
1000110
0100011
0010101
0001111
```

Modulo the all-ones projective relation this is rank three in `Gamma`.

Orbit stabilizer order under the 24-element arrangement group:

```text
24/8 = 3.
```

## Orbit II — size 2

Representative branch labels:

```text
A1 001
A2 010
A3 100
B3 101
B2 110
B1 011
C  111
```

An upstairs kernel basis is

```text
1000101
0100111
0010011
0001110
```

Modulo the all-ones relation this is rank three in `Gamma`.

Orbit stabilizer order:

```text
24/2 = 12.
```

## Interpretation

The size-2 orbit has substantially more arrangement symmetry than the generic size-8 orbit. This may make it the better first arithmetic target, but no rational-point advantage is asserted merely from the larger stabilizer.

Fresh audit should verify:

```text
R29-CAMP0A = exact 10-kernel count
R29-CAMP0B = exact 8+2 S4 orbit decomposition
R29-CAMP0C = Q-lift status of the orbit symmetries
```

If the size-2 representative admits an especially simple Q-model or involution quotient, route it first into `R29-CAMP2/3`.
