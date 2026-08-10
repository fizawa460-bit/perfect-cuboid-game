# Physical compact class reduction

```yaml
ID: TB-LEMMA-physical-compact-class-reduction
TYPE: LEMMA
STATUS: CURRENT
TITLE: Physical torsion translate is a nonzero compact Kummer class with four tau packets
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-05
SOURCE_PR: 356
SOURCE_MERGE_SHA: c2273d0388b48f8fb51d9dc69d8977efbc83db37
SOURCE_FILES:
  - stages/stage14/14-s6-05/result.md
```

## INPUT

The compact translate `Q0=P_phys+(0,0)` from `TB-FORMULA-compact-t0-torsion-translation`.

## OUTPUT

`Q0` lies on the nonidentity real component, hence

```text
Q0 notin 2E(R),
Q0 notin 2E(Q).
```

Its factor signs are forced to `(--+)`. The physical majorant needs exactly four sign/2-adic packets:

```text
(-1,-1,1), (-2,-2,1), (-2,-1,2), (-1,-2,2).
```

Writing `d0=-e0,d1=-e1,d2=e2` gives the positive-definite equations

```text
e2*u2^2+e0*u0^2=X^2D^2,
e2*u2^2+e1*u1^2=H^2D^2,
```

and therefore `|u_i|<=BD` on the physical cutoff.

## VARIABLE DICTIONARY

- `e_i=|d_i|` in the physical compact sign chamber.
- `D` here is the reduced denominator of the selected compact point in this lemma; use the selector-specific names `D_-` or `D_+` once half-angle routing is introduced.

## USED BY

- Removing the noncompact `+++` chamber from the physical upper majorant.
- Replacing maximal halving by a canonical physical representative.
- Archimedean coordinate control before arithmetic routing.

## DO NOT USE FOR

- Do not conclude that every abstract locally admissible packet has this sign chamber.
- Do not promote `|u_i|<=BD` to a packet-count saving without a transfer theorem.

## PROVENANCE NOTES

Merged Stage14-s6-05 uses the real component group and exact torsion translation. No external theorem is needed.