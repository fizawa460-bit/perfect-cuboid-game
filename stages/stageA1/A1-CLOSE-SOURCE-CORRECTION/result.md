# StageA1 closure — invalid upstream source correction

## Closure reason

StageA1 is closed because the A1-3 audit changed the published Bremner–Elsholtz–Ulas equation-(6) anchor coefficient from `-18` to `-8`. That correction was wrong.

The published equation (6) uses

```text
c^8 - 18 c^4 d^4 + d^8.
```

The StageA1 A1-3 through A1-14 chain instead propagated the auxiliary `-8` version.

Independent source recheck established:

- the arXiv v1 equation-(6) source uses `-18`;
- at `(c,d,G,H)=(3,1,7,1)`, the published `-18` formulas give all eight Hilbert-cube subset sums as exact squares;
- replacing only that coefficient by `-8` breaks seven of the eight square conditions;
- the published `-18` anchor yields

```text
4k(k-1)u^2-(k^4-18k^2+1)u-16k^2(k-1)=0,
D18(k)=k^8-36k^6+256k^5-186k^4+256k^3-36k^2+1,
Y^2=z^4-40z^2+256z-112.
```

This differs from the StageA1 auxiliary quartic

```text
Y^2=z^4-20z^2+256z-412.
```

Therefore A1-3 through A1-14 are not valid restrictions on the published equation-(6) family.

## Quarantine of downstream results

The internal arithmetic on the auxiliary `-8` curve is not deleted. In particular, the A1-12 384-class sieve, A1-13 256-class refinement, and A1-14 deeper 7-adic refinement may remain mathematically meaningful for that auxiliary curve.

They MUST NOT be cited as consequences for:

- the published equation-(6) Hilbert-cube family;
- arbitrary perfect cuboids;
- perfect-cuboid existence or nonexistence.

They are historical auxiliary-curve computations only.

## Handoff

The correct restart is a new StageA2 line beginning at `A2-3`, from the published `-18` source with no inherited `-8` algebra.

A2-3 must require, in this order:

1. source PDF coefficient check;
2. independent transcription of equation (6);
3. exact numerical sanity check on a nondegenerate source parameter point;
4. symbolic anchor derivation from `-18`;
5. only then quotient/rational-point work.

```text
STAGE_A1_STATUS=CLOSED_INVALID_UPSTREAM_SOURCE_CORRECTION
INVALID_FROM=A1-3
INVALID_THROUGH=A1-14
AUXILIARY_MINUS8_ARITHMETIC_PRESERVED=true
AUXILIARY_MINUS8_RESULTS_APPLY_TO_PUBLISHED_EQUATION6=false
A1_12_384_APPLIES_TO_PUBLISHED_EQUATION6=false
PERFECT_CUBOID_FOUND=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT_STAGE=StageA2
NEXT_TASK=A2-3_PUBLISHED_MINUS18_RESTART
```
