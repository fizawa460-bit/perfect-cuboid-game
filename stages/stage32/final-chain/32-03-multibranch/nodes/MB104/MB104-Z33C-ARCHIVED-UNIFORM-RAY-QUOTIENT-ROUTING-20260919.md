# MB104 Z33C — archived uniform-ray quotient routing — 2026-09-19

Status: **PARALLEL ROUTING REDUCTION / NO NEW CREDIT**

## Purpose

This checkpoint is a top-down Z-lane routing note. It does not follow the current P6 frontier and
does not promote any archived result beyond its original scope.

The current Z33A finite orbit scan lists surviving ambient hyperplane orbits at incidences
24,20,19,16,15,14 after the simple-contact test. That list is useful for the arbitrary span-five
equality sector, but it should not be mistaken for the unresolved population of the older
**uniform P5 Picard ray**

```text
D_l = 7l H - 4l sum_(p in Sigma) E_p.
```

## Archived exact quotient

At archive head

```text
ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11
```

the source-locked known-conic verifier proves, for the displayed uniform ray:

```text
incidence 24: closed by fixed components
incidence 20: closed by fixed components
incidence 19: closed by fixed components
incidence 15: closed by known conics
incidence 14: all five ambient orbits closed by known conics
incidence 16: reduced to balanced hard core only
```

The remaining uniform-ray support population is exactly four Aut(S) orbits:

```text
0000770000ff   orbit 48
00007b0000ff   orbit 48
000707000f0f   orbit 768
00070b000f0f   orbit 768
```

Total: `1632` supports.

The first two come from the incidence-16 size-3 ambient orbit; the last two from the
incidence-16 size-24 ambient orbit.

## Interaction with current Z33A

Z33A adds useful local information to the incidence-16 ambient classes:

```text
I16-O3:
  every supported branch is diagonal;
  with m=1 this forces (A,B)=(1,1).

I16-O24:
  exactly one fixed non-diagonal landing bin survives at every node.
```

Therefore, in **uniform-ray semantics**, the legal unresolved Z target is not the full Z33A
survivor table. It is only the four balanced incidence-16 support orbits above, now augmented
by the newer Z33 equality/simple-contact data.

This prevents unnecessary deep dives into incidence 24/20/19/15/14 when the intended object is
the uniform P5 ray.

## Important scope firewall

The archived known-conic quotient does **not** close arbitrary unequal exceptional
coefficients. Z33/Z33A are broader than the archived uniform ray in that respect.

Hence:

```text
uniform-ray unresolved Z population = four balanced incidence-16 support orbits
arbitrary unequal span-five population = not reduced to those four by this adapter alone
```

No inference from the first line to the second is permitted.

## Recommended shallow order

For the Z lane, before rebuilding any general-m Hilbert machinery:

1. test the two size-48 balanced support orbits under the new I16-O3 all-diagonal condition;
2. test the two size-768 balanced support orbits under the new I16-O24 one-fixed-bin condition;
3. consume their already-retained zero-pairing elliptic-quartic profiles;
4. only if all four survive, return to Z32R/BTVA primitive Hilbert growth.

This keeps the lane finite-first and avoids another long descent into local conductor or
general-m machinery before the four exact hard-core orbits are exhausted.

## Source locks

Archived:
- `GENUS1-SPAN5-KNOWN-CONIC-BALANCED-QUOTIENT.md`
  blob `1dfafccb9559c98ccf71cc4b98449d784941d48f`;
- certificate
  blob `f63d08b9005762a02935a727f35e6581ae52aaab`.

Current:
- Z33A note blob `2483de9c5c4da33e331f0b5b75ceb96f7304411d`;
- Z33A certificate blob `fc66b5df676660798417e11f194b68e950f3bc98`.

## Firewalls

```text
new_mathematical_closure=false
arbitrary_unequal_picard_classes_closed=false
whole_span5_closed=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
