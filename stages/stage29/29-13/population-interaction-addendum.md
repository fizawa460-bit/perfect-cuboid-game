# Stage29-13 audit addendum — Saunderson non-endpoint population lower theorem

## Status

```text
STATUS=AUDITED_POSITIVE_REPAIR
SOURCE_FAMILY_RECEIVER=R29-EXT-CHANG-A
POPULATION_CONSUMER=J12-POP-INTERACTION
TARGETED_BACKFLOW_REQUIRED=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## 1. Audited Stage28 lower family

Stage28-50-r2, independently audited in `stages/stage28/28-50-r2/audit.md`, counts a primitive opposite-parity two-parameter Saunderson family on the cone

```text
1/8 <= s/r <= 4/5
```

with an injective primitive/canonical physical output map and exact physical-height bound

```text
R <= 8 r^6.
```

The audited cone count is

```text
#C(T)=27/(20*pi^2)*T^2+O(T log T),
```

hence

\[
M_3(B)\ge \left(\frac{27}{40\pi^2}+o(1)\right)B^{1/3}
\]

and

\[
\liminf_{B\to\infty}\frac{M_3(B)}{B^{1/3}}\ge\frac{27}{40\pi^2}.
\]

Every object counted by this lower construction is a nondegenerate primitive canonical Saunderson Euler brick.

## 2. New Stage29-13 input

Fresh Stage29-13 audit independently reconstructs the full Saunderson-family endpoint exclusion:

```text
R29-EXT-CHANG-A=DISCHARGED_INDEPENDENTLY_RECONSTRUCTED
NO_NONDEGENERATE_PERFECT_CUBOID_IN_SAUNDERSON_FAMILY=true.
```

The family formula is the same classical Saunderson construction used by the Stage28 lower theorem, up to harmless edge signs/permutation before the frozen primitive/canonical normalization. Consequently every Stage28-50-r2 lower-family object lies in

```text
M3 \ P.
```

No cutoff, primitivity, canonical-order, or multiplicity conversion is needed: those were already audited in the Stage28 construction, while the Stage29-13 exclusion is pointwise on the entire nondegenerate Saunderson family.

## 3. New theorem

Therefore the Stage28 lower count transfers verbatim to the non-endpoint Euler population:

\[
\boxed{
M_3(B)-P(B)\ge
\left(\frac{27}{40\pi^2}+o(1)\right)B^{1/3}
}
\]

and in particular

\[
\boxed{
\liminf_{B\to\infty}
\frac{M_3(B)-P(B)}{B^{1/3}}
\ge \frac{27}{40\pi^2}>0.
}
\]

Receiver:

```text
R29-POP-SAUND-NONENDPOINT=DISCHARGED_EXPLICIT_NONENDPOINT_M3_LOWER
```

## 4. Firewalls

This theorem does **not** imply

```text
P(B)=0,
P(B)/M3(B)->0,
M3(B)~const*B^(1/3),
or any upper bound for M3(B)-P(B).
```

The reason is that the true growth scale of the full `M3` population remains unknown; the Saunderson family is only an explicit lower subfamily.

This is not a repair to a false Stage28 theorem and therefore does not require old-stage backflow. It is a new Stage29 interaction consequence obtained by combining the audited Stage28 counting theorem with the newly certified Stage29-13 family exclusion.
