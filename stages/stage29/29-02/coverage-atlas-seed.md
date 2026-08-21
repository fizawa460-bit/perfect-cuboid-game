# Stage29-02 — parametrization coverage atlas seed

```text
ROLE=F3_COVERAGE_SCREENING
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

The purpose of this seed is to prevent a recurring endpoint error: a parametrized family can be completely solved while still covering only a curve or thin subfamily of the relevant population.

| source/model | host | image dimension / generic degree | certified coverage statement | endpoint use |
|---|---|---|---|---|
| Stage18/19 shared-edge toric coordinates | exactly-two-face physical host | two-parameter toric host; physical reconstruction unique after frozen chamber | zero-loss for the exactly-two-face host interface used by Stage19 | valid base for adding space and/or third-face completion |
| Stage20 generalized Saunderson map | Stage20 third-face K3 | `P^1` image; generically degree 1 onto image | physical rational curve with `M_face.C=6` | strong explicit construction only; not dominant in full Euler population |
| StageA2 equation-(6) `-18` family | published anchored family | low-dimensional family reduced to two covers | family-specific nondegenerate rational points closed; `GENERAL_COVERAGE_PROVED=false` | method source only; no arbitrary-perfect-cuboid conclusion |
| Stage29 global endpoint model `S0` | perfect-cuboid endpoint | projective surface candidate cut by four quadrics | definition-level endpoint model; exact birational adapter to toric joint cover not yet certified | primary F1 receiver |
| Stage29 joint `(Z/2)^2` cover | common two-face base `Y` | generic degree 4 over `Y` | exact function-field compositum of the two distinct completion covers | primary F2 endpoint model; physical adapters still required |

## Mandatory fields for 29-08 expansion

Every future row must record at least:

```text
SOURCE_MODEL=
TARGET_HOST=
IMAGE_DIMENSION=
GENERIC_DEGREE=
HEIGHT_DISTORTION=
PHYSICAL_MULTIPLICITY=
EXCEPTIONAL_LOCUS=
DOMINANT_OR_THIN=
COVERAGE_PROVED=true/false
REVERSE_MAP_AVAILABLE=true/false
ENDPOINT_CLAIM_ALLOWED=
```

A family-specific rational-point closure may be globally useful only after its coverage row says why the image is large enough for the intended endpoint consequence.
