# Physical-open / arrangement-open firewall

## Two different algebraic opens

Let

```text
D_all = {x y z (x+y)(x+z)(y+z)(x+y+z)=0}.
```

The non-Fano arrangement complement is

```text
B_arr=P2\D_all.
```

Its inverse image in the endpoint resolution is the unbranched congruence-cover open.

Stage29-02f's physical algebraic open is instead defined by the nonzero side condition

```text
a1*a2*a3 != 0.
```

Over `Qbar`, this does not delete every face-diagonal-zero or space-diagonal-zero divisor, so these two opens are not equal as algebraic varieties.

## Rational-point containment

For a rational nondegenerate box, if a rational face diagonal vanished then a sum of two rational squares would be zero, forcing the corresponding sides to vanish. Similarly a rational space diagonal cannot vanish for nonzero rational sides. Hence

```text
U_phys(Q) subset U_arr(Q)
```

for the actual endpoint candidate locus (indeed equality on the nondegenerate rational endpoint locus after the redundant diagonal-nonzero conditions are added).

Thus proving `U_arr(Q)=empty` would be a valid endpoint obstruction. But a Brauer group or boundary computation on `U_arr` cannot simply be substituted for the Stage29-02f computation on `U_phys` without an open-immersion/residue adapter.

## Receivers

```text
R29-NF-PHYS1 = ArrangementOpenToPhysicalRationalLocusContainment
R29-NF-PHYS2 = ArrangementBoundaryResiduesToPhysicalBoundaryResidues
```

The first is elementary candidate-level arithmetic; the second remains open and is potentially useful for `R29-BR0G/R29-BR2A/B`.
