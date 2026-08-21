# Peschmann 2026 crosswalk — high-value unresolved adapter candidate

SOURCES=`arXiv:2604.09328`, `arXiv:2604.28072`
STATUS=AUDITED_RESEARCH_INPUT_EXACT_STAGE29_CROSSWALK_OPEN

## What the 2026 route actually supplies

The companion papers use two Euclidean/Pythagorean parameter pairs so that two face-diagonal conditions are automatic. The remaining perfect-cuboid conditions are simultaneous squareness of the third face diagonal and the space diagonal, reorganized through a genus-3 family with elliptic quotients.

The later paper `arXiv:2604.28072` additionally gives:

- a structural classification placing primitive Euler bricks in the standard `(a,b,m,n)` parametrization up to scaling;
- a torsion/rank-zero exclusion criterion on the elliptic quotients;
- an unconditional exclusion on 1,072 explicit master-tuple fibers with `max(m,n)<=100`.

These are source-level research inputs only. They are not imported as Stage29 certified global or population results here.

## Relation to the audited Stage28/29 host

Stage28/29 already has the condition architecture

```text
common two-face host
+ third-face square completion
+ space-diagonal square completion
= joint V4 endpoint cover.
```

Peschmann has the same residual two-square pattern. That makes an F2 crosswalk highly plausible, but pattern equality is not an exact rational-map proof.

Therefore the adversarial audit records

```text
PESCHMANN_PROVEN_F2_ADAPTER=false
PESCHMANN_INDEPENDENCE_RESOLVED=false
PESCHMANN_NEW_FOUNDATION_PROMOTED=false
PESCHMANN_ROUTING=HIGH_VALUE_GLOBAL_PARAMETRIZATION_FIBRATION_CANDIDATE
```

The broad-screen stop does **not** mean Peschmann was proved non-independent. It means no ninth independent foundation was certified by this pass.

## Receiver

```text
R29-PESCH1 = EuclidPairToStage28TwoFaceHostAndJointV4ExactCrosswalk
```

A future discharge must establish exact rational maps, exceptional loci, which quartic is which residual square completion, the genus-3 fiber/quotient relation, and coverage.

## Population / finite-family firewall

The 1,072-fiber exclusion is finite-family arithmetic in Peschmann coordinates. It does not automatically imply anything about Stage16–20 cutoff populations, heights, primitivity, canonical ordering, or asymptotic density.

```text
BACKFLOW_TO_STAGE16_28=false
POPULATION_TRANSFER=false
HEIGHT_TRANSFER=false
PRIMITIVITY_TRANSFER=false
CANONICAL_ORDER_TRANSFER=false
ASYMPTOTIC_TRANSFER=false
GLOBAL_ENDPOINT_CONCLUSION=false
```
