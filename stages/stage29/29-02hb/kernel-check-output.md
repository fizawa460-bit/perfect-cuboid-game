# Exact Campedelli-kernel enumeration checkpoint

```text
SCRIPT=stages/stage29/29-02hb/campedelli_kernel_check.py
ARITHMETIC=EXACT_F2
STATUS=PASS_ALL_ASSERTIONS
```

Output:

```text
raw_admissible_labelings=1680
GL3_F2_order=168
distinct_rank3_kernels=10
arrangement_aut_order=24
kernel_orbit_sizes=8,2
```

The ten kernels are labelings modulo target `GL(3,F2)`, so they are distinct rank-3 subgroups of the six-dimensional sign deck group rather than merely different names for the same quotient map.

Representative of the size-8 orbit:

```text
A1:001 A2:010 A3:011 B3:100 B2:110 B1:111 C:101
upstairs kernel basis in F2^7:
1000110
0100011
0010101
0001111
```

Representative of the size-2 orbit:

```text
A1:001 A2:010 A3:100 B3:101 B2:110 B1:011 C:111
upstairs kernel basis in F2^7:
1000101
0100111
0010011
0001110
```

Each upstairs kernel has dimension four and contains the all-ones projective-sign relation; modulo that relation it gives a rank-3 subgroup `H <= Gamma`.

The arrangement-incidence automorphism group is independently audited in Stage29-02ha as `S4` of order 24. Its action on these ten kernels has exactly two orbits, of sizes eight and two.
