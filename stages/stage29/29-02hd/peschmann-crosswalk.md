# Peschmann 2026 crosswalk — candidate adapter, not independent foundation

SOURCE=arXiv:2604.09328
STATUS=RESEARCH_INPUT_REQUIRES_EXACT_ADAPTER_AUDIT

## What the preprint does

The preprint chooses two Euclidean/Pythagorean parameter pairs and constructs edges for which two face-diagonal conditions are automatic. The perfect-cuboid condition then becomes simultaneous squareness of the two remaining quantities: the third face diagonal and the space diagonal. It further reorganizes those quartic conditions into a one-parameter genus-3 hyperelliptic family with elliptic quotients.

## Existing Stage29 crosswalk

Stage28/29 already has an audited common two-face host with two residual square completions:

```text
base = common two-face toric host Y
residual square #1 = third-face completion
residual square #2 = space-diagonal completion
joint endpoint = V4 / bidouble cover tracking both
```

The Peschmann construction has the same condition pattern:

```text
two Pythagorean faces built in
+ third-face square
+ space-diagonal square
```

Therefore the correct pre-audit routing is

```text
PESCHMANN_2026_RELATION_TO_F2=LIKELY_EXPLICIT_CHART_OR_FIBRATION
INDEPENDENT_FOUNDATION=false_PENDING_EXACT_CROSSWALK
HIGH_VALUE_ADAPTER_CANDIDATE=true
```

## What must be proved before importing it

A future adapter should establish, with exact rational maps and exceptional loci:
1. the birational map from the Euclid-pair parameter space to the canonical Stage28 two-face host;
2. which Peschmann quartic is the Stage20 third-face square root and which is the Stage19/28 space square root;
3. the physical height/canonical-order/primitivity firewall;
4. whether the genus-3 curves are fibers/slices of the joint V4 cover or a further quotient;
5. exact coverage and exceptional/degenerate loci.

## Firewall

No Peschmann computation or descent result is imported into the certified Stage16–20 population theorems here.

```text
BACKFLOW_TO_STAGE16_28=false
POPULATION_TRANSFER=false
HEIGHT_TRANSFER=false
PRIMITIVITY_TRANSFER=false
ASYMPTOTIC_TRANSFER=false
GLOBAL_ENDPOINT_CONCLUSION=false
```
