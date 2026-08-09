# Denominator selectors: D, D_min, D_T

```yaml
ID: TB-DICTIONARY-denominator-selectors
TYPE: DICTIONARY
STATUS: CURRENT
TITLE: Generic, least-packet, and physical compact denominator selectors
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-05
SOURCE_PR: 356
SOURCE_MERGE_SHA: c2273d0388b48f8fb51d9dc69d8977efbc83db37
SOURCE_FILES:
  - stages/stage14/14-s6-05/result.md
  - stages/stage14/14-4bj/result.md
```

## INPUT

- The merged post-local witness framework of Stage14-4bg/s6-01.
- When using `D_T`, an actual physical point `P_phys` and its compact torsion translate `Q=P_phys+(0,0)`.

## OUTPUT

There are three distinct denominator objects.

```text
D
= denominator square-root of one chosen rational witness:
  Z=A/D^2, gcd(A,D)=1.

D_min(F,sigma;B)
= least D among the bounded-height global representatives admitted for an abstract packet `(F,sigma)`.

D_T(P_phys)
= denominator square-root of the canonical compact physical representative
  Q=P_phys+(0,0).
```

For the packet containing the canonical physical translate,

```text
D_min <= D_T.
```

The exact s6-05 involution gives, if the original physical point is

```text
Z_P=A_P/D_P^2,
gcd(A_P,D_P)=1,
```

then

```text
D_T^2=A_P/gcd(A_P,S^2X^2).
```

`D_min` remains a valid abstract packet statistic, but `D_T` is the stronger physical selector because it preserves invertible physical reconstruction and later acquires direct second-face/half-angle identities.

## VARIABLE DICTIONARY

- `D` = denominator square-root attached to a particular rational witness.
- `D_min` = minimum `D` over a bounded-height representative set for one abstract packet.
- `D_T` = denominator square-root after translating a genuine physical point by `T0=(0,0)` to the compact real component.
- `D_P` = denominator square-root of the original physical point before torsion translation.
- `A_P` = numerator of the original physical `Z_P` coordinate.

## USED BY

- Main route after Stage14-4bj when discussing packet-level denominator gates.
- s route from Stage14-s6-05 onward when using the canonical physical compact representative.
- Any cross-route note comparing abstract packet existence with physical reconstruction.

## DO NOT USE FOR

- Do not replace `D_min` by `D_T` on an arbitrary locally soluble or globally soluble packet that has no known physical point.
- Do not infer `D_T=D_min`; only `D_min<=D_T` is justified for the packet containing the selected physical translate.
- Do not import later `D_T|X2` or half-angle formulas into generic `D` or `D_min` statements.
- Do not identify the symbol `D` here with the s5 D-column `m+n`.

## PROVENANCE NOTES

- Stage14-4bj, PR #355, merge `7ab3c21cc07714b24edfa1a36425b4beaeb2a6e7`, defines `D_min` as the abstract packet-level statistic.
- Stage14-s6-05 proves that physical hits admit the canonical compact torsion translate and upgrades the preferred physical selector to `D_T` without invalidating `D_min`.
- Stage14-s6-06 later gives stronger formulas for the same `D_T`; those are packaged in a separate dictionary card.
