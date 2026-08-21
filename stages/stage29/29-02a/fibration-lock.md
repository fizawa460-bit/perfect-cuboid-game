# Stage29-02a — fibration lock

Testa--Stoll provides a second endpoint-specific weapon beyond the low-degree curve classification: explicit fibrations on both the full surface and its Euler-brick K3 quotient.

## Full endpoint surface

From the rank-3 and rank-4 quadrics containing the cuboid surface, the source constructs exactly `28` fibrations whose generic fibers are smooth canonically embedded curves of genus `5` and projective degree `8`.

Theorem 16 further states that any integral curve on the full cuboid surface spanning a `P^4` is degree `8` and is a fiber of one of these 28 fibrations; such a curve is either a smooth canonical genus-5 fiber or one of the described genus-3 hyperelliptic singular fibers.

Thus the first canonical degree not excluded by the positive-chamber degree-<=6 filter is not featureless: an important minimal-degree class is organized into explicit genus-5 fibrations.

## Euler-brick K3 quotient

For the long-diagonal-sign quotient `K_c`, the source obtains `15` elliptic fibrations from its rank-3/rank-4 quadrics.

This is potentially relevant to the Stage28/Stage29 moving-fibre route after the exact K3/polarization adapter `R29-K1` is established.

## New receiver species

```text
R29-FIB1=PhysicalRationalPointsOnPublishedGenus5EndpointFibrations
R29-FIB2=Stage20PhysicalHeightOnPublishedKcEllipticFibrations
```

Questions for later work:

- Which of the 28 full-surface fibrations are defined over `Q` versus only after a splitting field?
- Does the positive physical chamber meet their generic real locus?
- What is the induced physical height on a fiber and its base?
- Can any fiber quotient reduce to genus 1/2/3 in a way compatible with StageA2-style descent?
- Which of the 15 `K_c` elliptic fibrations correspond to previously used Stage20 moving fibres, and which are genuinely unused?

## Firewall

A fibration by curves of genus at least 2 does not by itself imply that the union of rational points over varying fibers is finite or sparse with a certified physical-height exponent.  Likewise an elliptic fibration requires rank and height control before it yields a counting theorem.

```text
GENUS5_FIBRATION_IMPLIES_GLOBAL_POINT_FINITE=false
ELLIPTIC_FIBRATION_IMPLIES_UNIFORM_RANK_CONTROL=false
NEW_COUNTING_EXPONENT=false
```
