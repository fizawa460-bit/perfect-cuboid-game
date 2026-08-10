# Full odd leg radicals as exact incidence moduli

```yaml
ID: TB-LEMMA-full-leg-radical-modulus
TYPE: LEMMA
STATUS: CURRENT
TITLE: Full odd radicals of S, X, H are exact witness congruence moduli
SCOPE: BOTH
SOURCE_STAGE: Stage14-4bi-S
SOURCE_PR: 352
SOURCE_MERGE_SHA: a40878e2efdf17b2f151a9cf15849c001908c3a4
SOURCE_FILES:
  - stages/stage14/14-4bi-S/result.md
  - stages/stage14/14-4bi-L/result.md
```

## INPUT

The normalized edge equations from an exact signed kernel packet, with

```text
a | rad_odd(S)
b | rad_odd(X)
c | rad_odd(H).
```

Define

```text
R_S=rad_odd(S)
R_X=rad_odd(X)
R_H=rad_odd(H).
```

## OUTPUT

The full leg radicals divide the normalized right sides:

```text
R_S | a*(S/a)^2
R_X | b*(X/b)^2
R_H | c*(H/c)^2.
```

Hence every exact witness satisfies

```text
tau0*b*u0^2 == tau1*c*u1^2 (mod R_S)
tau2*c*u2^2 == tau0*a*u0^2 (mod R_X)
tau2*b*u2^2 == tau1*a*u1^2 (mod R_H).
```

The coefficients are units modulo the corresponding radical.

In particular, the usable incidence modulus can remain large even when

```text
a=b=c=1.
```

## VARIABLE DICTIONARY

- `R_S,R_X,R_H` = full odd radicals of the three primitive Pythagorean legs.
- `a,b,c` = selected odd squarefree kernel edges; generally proper divisors of the corresponding full radicals.

## USED BY

- Full-radical witness-lattice bounds.
- Removing `small selected kernel` as an intrinsic modulus obstruction.
- Radical-rich/radical-poor partitioning.

## DO NOT USE FOR

- Do not identify `R_S` with `a`, `R_X` with `b`, or `R_H` with `c` unless equality is separately known.
- Do not infer global point existence from the congruences.
- Do not infer a packet-count saving directly from the modulus size.

## PROVENANCE NOTES

Merged PR #352 strengthens merged PR #349 from selected edge kernels to the entire odd radicals of the Pythagorean legs.