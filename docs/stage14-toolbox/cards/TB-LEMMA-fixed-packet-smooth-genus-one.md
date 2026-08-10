# Smooth genus-one complete intersection

```yaml
ID: TB-LEMMA-fixed-packet-smooth-genus-one
TYPE: LEMMA
STATUS: CURRENT
TITLE: Every nonzero fixed witness packet is a smooth genus-one curve
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-02
SOURCE_PR: 348
SOURCE_MERGE_SHA: 1338ee0170a6d92c26a9dd4fa21c886a8125d6db
SOURCE_FILES:
  - stages/stage14/14-s6-02/result.md
```

## INPUT

The fixed curve `C_sigma={Q1=Q2=0}` from `TB-FORMULA-fixed-packet-two-quadrics`, with nonzero `d0,d1,d2,S,X,H` and `S^2+X^2=H^2`.

## OUTPUT

The gradients are

```text
grad Q1=(2d0u0,-2d1u1,0,-2S^2D),
grad Q2=(-2d0u0,0,2d2u2,-2X^2D).
```

Linear dependence of the two gradients at a common zero forces successively `u2=0`, `u1=0`, and then

```text
d0*u0^2=S^2*D^2,
-d0*u0^2=X^2*D^2,
```

so `H^2D^2=0`, hence all projective coordinates vanish, impossible. Thus `C_sigma` is smooth.

A smooth complete intersection of two quadrics in `P^3` has degree four and trivial canonical class by adjunction, hence

```text
2g-2=0,
g=1.
```

Therefore

```text
C_sigma = smooth genus-one curve of degree 4.
```

## VARIABLE DICTIONARY

- `g` = geometric genus of `C_sigma`.
- `degree 4` = projective degree of the complete intersection `(2,2)`.

## USED BY

- Genus-one point-count/determinant-method eligibility checks per packet.
- Excluding hidden singular curve components in the witness relaxation.
- Comparing the witness model with alternative genus-one presentations.

## DO NOT USE FOR

- Smooth genus one does not imply a rational point exists.
- A genus-one curve is not automatically an elliptic curve until a rational base point is chosen.
- Per-packet geometry does not by itself improve the moving packet-count exponent.

## PROVENANCE NOTES

Merged PR #348 gives the direct Jacobian proof and adjunction step. Merged PR #347 records the same conclusion independently on the main track.