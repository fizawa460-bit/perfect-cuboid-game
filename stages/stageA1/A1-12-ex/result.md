# StageA1 A1-12-ex — second independent verification

## Verdict

`AUDIT_VERDICT=FAIL_SOURCE_COEFFICIENT_MISMATCH`

The A1-12 finite-field/Mordell–Weil computation is internally reproducible, but its attachment to the published Bremner–Elsholtz–Ulas equation-(6) family is not valid as currently recorded.

## 1. Published equation (6) uses -18, not -8

The arXiv source `2604.05459v1`, equation (6), has in the `a0` square factor

```text
c^8 - 18 c^4 d^4 + d^8.
```

The current StageA1 A1-3 chain instead replaced this by

```text
c^8 - 8 c^4 d^4 + d^8,
```

and all A1-4 through A1-13 reciprocal/quartic computations descend from that replacement.

This is not a harmless transcription choice. `verify_source_equation6.py` substitutes the exact nondegenerate parameter point

```text
(c,d,G,H)=(3,1,7,1)
```

into the published polynomial formulas. With coefficient `18`, all eight Hilbert-cube subset sums are exact integer squares. Replacing only the source coefficient by `8` leaves `a0` square but makes the other seven required subset sums nonsquares. Thus the `-8` replacement is not the published equation-(6) family.

## 2. Correct reciprocal curve from the published -18 coefficient

With

```text
x=c/d,
k=x^2,
r=G/H,
u=r-1/r,
```

the published anchor equation gives

```text
4 k(k-1)u^2
- (k^4-18k^2+1)u
- 16k^2(k-1)=0.
```

Its discriminant is

```text
D18(k)
 = k^8-36k^6+256k^5-186k^4+256k^3-36k^2+1.
```

For `z=k+1/k`, the reciprocal quotient is therefore

```text
Y^2 = z^4 - 40z^2 + 256z - 112.
```

This is not the A1-3/A1-12 quartic

```text
Y^2 = z^4 - 20z^2 + 256z - 412.
```

Hence the curve `6080.r1`, its multiplier `n`, and the 384 residue classes computed in A1-12 are not presently attached to the actual published equation-(6) anchor boundary.

## 3. What remains correct inside A1-12

The following computations were independently reproduced again and are internally correct for the A1-12 quartic/model:

- the birational map between `z^4-20z^2+256z-412` and `6080.r1`;
- official LMFDB data: minimal model `[0,1,0,95,703]`, rank 1, trivial torsion, generator `(3,32)`;
- all six finite-field orders and allowed classes;
- direct scan of all `3,416,490` residues;
- exactly `384` survivors;
- SHA-256 `63652cb8e25860ba40dba7ba5f99023a9a611525f7b2bd2465a79b95c268e874`.

The official LMFDB reliability statement for elliptic curves over `Q` makes the rank-one Mordell–Weil data rigorous at conductor 6080, so Sage execution is extra redundancy rather than the missing logical step.

But these facts now certify only the arithmetic of the **A1-12 auxiliary/wrong-source quartic**. They do not establish

```text
published equation-(6) candidate
  => n lies in the 384 A1-12 residue classes.
```

## 4. Required upstream repair

Before any further StageA1 conclusion is promoted, the chain must be rederived from the published `-18` coefficient. At minimum this invalidates the source attachment of A1-3 through A1-13 and requires a new exact descent beginning from

```text
Y^2=z^4-40z^2+256z-112.
```

A1-12/A1-13 should not be cited as restrictions on the published equation-(6) family until that rederivation is complete.

This does not prove or disprove a perfect cuboid. It is a source-attachment failure in the StageA1 side line.

```text
A1_12_EX_SECOND_CHECK=COMPLETE
A1_12_EX_SOURCE_PDF_COEFFICIENT=-18
A1_12_EX_PROJECT_CHAIN_COEFFICIENT=-8
A1_12_EX_SOURCE_ATTACHMENT_AUDIT=FAIL
A1_12_384_ARITHMETIC_INTERNAL_AUDIT=PASS
A1_12_384_APPLIES_TO_PUBLISHED_EQUATION6=NOT_PROVED_AND_CURRENT_DERIVATION_INVALID
CORRECT_PUBLISHED_RECIPROCAL_QUARTIC=Y^2=z^4-40z^2+256z-112
PERFECT_CUBOID_FOUND=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
```
