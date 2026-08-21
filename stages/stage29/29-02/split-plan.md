# Stage29-02 split/deepening plan

Stage29-02 is a screening checkpoint, not a requirement to place every follow-up investigation in one PR.

The initial screening has found a materially new endpoint foundation: the global perfect-cuboid surface together with the joint `(Z/2)^2` completion cover and its cross quotient.  The follow-up work is therefore split into independently auditable subroutes.

```text
PARENT=Stage29-02_NEW_FOUNDATION_SCREENING
PARENT_PR=1286
ONE_PR_MUST_CONTAIN_ALL_DEEPENING=false
```

## 29-02a — GLOBAL_ENDPOINT_SURFACE_LITERATURE_LOCK

Purpose: import and applicability-audit the strongest known geometry of the full perfect-cuboid/rational-box surface itself, rather than treating F1 as a newly invented model.

Priority source: Testa--Stoll, `Curves on the surface of cuboids`, Mathematics of Computation, DOI `10.1090/mcom/4238`, accepted 2026; open preprint arXiv `1009.0388` / author PDF `Cuboidi.pdf`.

Questions:
- exact identification of the repo endpoint model with the published cuboid surface;
- complete-intersection and singularity type;
- canonical/general-type model and Picard/automorphism data;
- exact low-degree curve classification and endpoint implications;
- whether this yields a genuinely reusable Stage29 weapon rather than an existence/nonexistence claim.

## 29-02b — JOINT_V4_COVER_GEOMETRY_PREFLIGHT

Purpose: deepen F2 without prematurely doing full roadmap item 29-07.  Determine exact quotient diagram, branch intersections, normality/singularity issues, and what can already be certified about the cross quotient and joint cover before a full canonical-model analysis.

This subroute must distinguish exact function-field facts from unresolved resolution/Kodaira-type claims.

## 29-02c — LOW_GENUS_AND_COVERAGE_REUSE_SCREEN

Purpose: combine the full-surface low-genus restrictions with F3 coverage.  Test whether known conics/genus-one curves, fibrations, modular-product covers, symmetric-differential restrictions, and family-specific StageA2/Saunderson objects can be placed on one coverage atlas with exact endpoint firewalls.

## Stop rule

Each subroute is allowed to terminate independently at a real theorem/adapter boundary.  A new suffix is opened only for a materially distinct question; cosmetic subdivision is forbidden.

```text
OLD_GATE_REPLAY=false
AUDIT_EACH_SUBROUTE=true
TARGETED_BACKFLOW_ONLY_IF_NEW_RECEIVER=true
```
