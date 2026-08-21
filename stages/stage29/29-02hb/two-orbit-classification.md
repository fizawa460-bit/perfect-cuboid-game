# Geometric and arithmetic orbit classification of Campedelli kernels

The exact kernel enumeration produces ten rank-3 subgroups of the six-dimensional sign deck group.

## Geometric / Q(i) classification

The audited arrangement automorphism group

```text
Aut_P2(D) ~= S4, order 24
```

acts on the ten kernels with orbit sizes

```text
8 + 2.
```

All 24 arrangement projectivities lift to the full sign cover over `Q(i)` by the audited Stage29-02ha squareclass calculation. Therefore `8+2` is a valid geometric / `Q(i)` orbit classification.

Representative of the geometric size-8 orbit:

```text
A1 001
A2 010
A3 011
B3 100
B2 110
B1 111
C  101
```

with upstairs `F2^7` kernel basis

```text
1000110
0100011
0010101
0001111
```

Representative of the geometric size-2 orbit:

```text
A1 001
A2 010
A3 100
B3 101
B2 110
B1 011
C  111
```

with upstairs kernel basis

```text
1000101
0100111
0010011
0001110
```

Each upstairs kernel has rank four and contains the all-ones projective-sign relation; modulo that relation it is rank three in `Gamma`.

## Q-arithmetic classification: the S4 collapse is not valid

Fresh adversarial audit applies the already-audited Stage29-02ha field-of-definition split. Only the coordinate-permutation subgroup

```text
S3 <= S4, order 6
```

lifts to the full sign cover over `Q`; the remaining arrangement symmetries require `Q(i)`.

Re-running the ten-kernel action under this certified Q-defined subgroup gives

```text
Q-symmetry orbit sizes = 6 + 2 + 2.
```

More precisely, the geometric size-8 orbit splits into Q-symmetry orbits of sizes `6+2`, while the geometric size-2 orbit remains size `2`.

Therefore the submission phrase “two quotient types matter first arithmetically” was too aggressive. The audited arithmetic route must keep **three certified Q-symmetry representatives** unless a separate Q-isomorphism theorem identifies more of them.

```text
R29-CAMP0A=DISCHARGED_EXACT_10_KERNEL_COUNT
R29-CAMP0B=DISCHARGED_GEOMETRIC_QI_ORBITS_8_PLUS_2
R29-CAMP0C=DISCHARGED_CERTIFIED_Q_SYMMETRY_ORBITS_6_PLUS_2_PLUS_2
EXACT_Q_ISOMORPHISM_CLASS_COUNT_PROVED=false
```

The last firewall is intentional: a Q-isomorphism between two quotient surfaces need not a priori lift to the full endpoint surface, so `6+2+2` is certified as the orbit decomposition under the known Q-defined endpoint symmetry, not promoted to an abstract classification of all Q-isomorphism classes.
