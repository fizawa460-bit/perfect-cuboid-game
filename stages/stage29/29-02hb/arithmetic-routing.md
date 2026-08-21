# Audited arithmetic routing for the Campedelli quotients

## 1. One-way rational-point transfer is exact

Every coordinate sign involution is defined over `Q`, and every enumerated kernel `H` is a subgroup of that constant rational deck group. The quotient maps

```text
Sbar -> Cbar_H
S    -> C_H
```

are therefore Q-defined.

On the physical endpoint open the action is free and the resolutions are irrelevant, so

```text
U_endpoint(Q) -> C_H(Q)
```

for every admissible kernel. Consequently

```text
C_H(Q)=empty
```

for **one** audited quotient is sufficient to exclude physical endpoint rational points.

The converse is false: a rational quotient point need not lift rationally upstairs.

## 2. The submission's two-type arithmetic collapse is rejected

Geometrically, and over `Q(i)`, the ten kernels form two `S4` orbits of sizes

```text
8 + 2.
```

That is not the Q-arithmetic classification. Stage29-02ha already proves that only the coordinate-permutation subgroup

```text
S3 <= S4
```

lifts to the full sign cover over `Q`. The exact kernel checker gives the induced certified Q-symmetry decomposition

```text
6 + 2 + 2.
```

Thus arithmetic work may be reduced from ten kernels to **three certified Q-symmetry representatives**, not two.

The count of abstract Q-isomorphism classes of the quotient surfaces is not proved: in principle two quotients in different endpoint-symmetry orbits could be Q-isomorphic by a map that does not lift to the endpoint. The route therefore records only the reduction actually certified.

```text
GEOMETRIC_QI_KERNEL_TYPES=2
CERTIFIED_Q_SYMMETRY_TYPES=3
EXACT_Q_ISOMORPHISM_CLASS_COUNT_PROVED=false
```

## 3. H-torsor lifting

For the etale degree-8 quotient

```text
H ~= (Z/2)^3,
```

the geometric fiber above a rational quotient point is an `H`-torsor, with class in

```text
H^1(Q,H).
```

Without ramification conditions this set is infinite. A finite twist list requires a separate Selmer/ramification argument.

Corrected receiver:

```text
R29-CAMP2=ArithmeticHTorsorDescentForThreeCertifiedQSymmetryRepresentatives
```

Required payload:

1. explicit Q-model for one representative in each certified `6+2+2` orbit;
2. exact physical-open image and deleted boundary;
3. Q-form/twist ledger relative to literature models;
4. ramification set for the H-torsor classes;
5. local solubility filters;
6. finite Selmer-style twist set if provable;
7. exact lift criterion back to the full sign cover.

## 4. Involution quotients: geometric classification is not Q-rationality

A classical Campedelli surface has seven nontrivial deck involutions, all Q-defined for these quotient Q-forms because `Gamma/H` is a constant `(Z/2)^3` group.

The literature gives geometric possibilities for the desingularized involution quotients, including rational and Enriques cases. Those words are geometric/birational unless a field is explicitly specified. In particular,

```text
geometrically rational != Q-rational
geometric Enriques classification != explicit Q-model
```

without additional descent.

Receiver:

```text
R29-CAMP3=SevenCampedelliInvolutionQuotientsWithQFormAndRationalVsEnriquesLedger
```

No rational parametrization or rational-point implication is imported from the geometric classification.

## 5. Brauer compatibility

For the Campedelli quotient, `pg=q=0`, `K^2=2`, and geometric fundamental group `(Z/2)^3`. This makes a 2-primary descent/Brauer analysis natural, but nothing from the endpoint Brauer computation automatically pushes down or pulls back as a complete obstruction.

```text
R29-CAMP4=CampedelliBrauerAndTwoPrimaryDescentCompatibilityWith29_02f
BRAUER_MANIN_OBSTRUCTION_PROVED=false
```

## 6. Population-stage firewall

The Campedelli quotient is useful for endpoint rational-point existence because it is a Q-defined pointwise quotient. It does **not** identify the earlier population stages or preserve their counting contracts.

No statement is made that

```text
M1, N1, M2, N2, M3
```

are counts on Campedelli quotients, nor that `R<=B`, primitivity, canonical ordering, or exact-face multiplicity descends without distortion.

```text
STAGE16_20_POPULATION_CORRESPONDENCE_CLAIM=false
POPULATION_ASYMPTOTIC_TRANSFER=false
HEIGHT_TRANSFER=false
PRIMITIVITY_TRANSFER=false
OLD_GATE_REPLAY=false
BACKFLOW_TO_STAGE16_28=false
```
