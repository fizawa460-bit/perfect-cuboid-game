# Stage29-02a — global endpoint surface literature lock

```text
TASK_ID=Stage29-02a
ROLE=GLOBAL_ENDPOINT_SURFACE_LITERATURE_LOCK
STATUS=RESEARCH_IN_PROGRESS
PARENT=Stage29-02
PERFECT_CUBOID_CONCLUSION=NONE
```

This subroute exists because the full endpoint surface is not merely a new Stage29 construction: there is strong published/preprint algebraic-geometry work directly on the same rational-box surface.  The goal is to lock those results into the repo with exact applicability and firewalls.

## Primary source lock

Damiano Testa and Michael Stoll, `Curves on the surface of cuboids`, Mathematics of Computation, DOI `10.1090/mcom/4238` (accepted 2026; open preprint arXiv:1009.0388 / author PDF `Cuboidi.pdf`).

Their surface `Sbar` in `P^6` is defined by the three face-diagonal equations and the long-diagonal equation, hence is the same projective rational-box/perfect-cuboid endpoint model as Stage29 F1 after a coordinate relabeling.

The source proves / records the following load-bearing facts:

1. `Sbar` is a geometrically integral complete intersection of multidegree `(2,2,2,2)` in `P^6`.
2. `Sbar` has exactly 48 isolated `A1` singularities.
3. For the minimal desingularization `S`, the canonical divisor is big and nef, `K_S^2=16`, and `S` is a minimal surface of general type; `Sbar` is its canonical model.
4. `Aut(S)=Aut(Sbar)` is explicitly determined and has order `1536` over the stated geometric setting; the source also determines the geometric Picard group, of rank `64`.
5. All integral curves of degree at most `6` are completely classified.
6. In particular there are no integral curves of degree `6` on `Sbar`.
7. All conics are among the known set; there are no smooth rational curves of degree `4`; degree-4 arithmetic-genus-one curves are among the known curves.
8. Any rational curve on `Sbar` other than a conic satisfies the stronger exceptional-divisor incidence bound stated in their Lemma 21; any genus-one curve satisfies the corresponding lower incidence bound.

## Immediate Stage29 consequence

This creates a new downstream weapon species that was not present in the Stage16--28 population arsenal:

```text
S29-W01_CANDIDATE=FULL_ENDPOINT_CANONICAL_SURFACE_GEOMETRY
S29-W02_CANDIDATE=FULL_ENDPOINT_LOW_DEGREE_CURVE_CLASSIFICATION_THROUGH_6
```

The low-degree theorem is strictly stronger than merely observing that Stage20 has a degree-six Saunderson curve on the *Euler/K3 marginal* surface.  It says that on the **full perfect-cuboid endpoint surface** there is no integral degree-six curve at all.  These are different surfaces and no contradiction occurs.

This gives a useful endpoint firewall:

```text
STAGE20_K3_HAS_PHYSICAL_M_DEGREE6_SAUNDERSON=true
FULL_ENDPOINT_SURFACE_HAS_INTEGRAL_PROJECTIVE_DEGREE6_CURVE=false
CROSS_SURFACE_DEGREE_IDENTIFICATION_FORBIDDEN=true
```

It also suggests a concrete transfer question for later Stage29 work: if a candidate endpoint family coming from Stage19/20/joint-cover geometry maps to a curve on the canonical endpoint surface, what is its canonical projective degree and does the degree-<=6 classification exclude it?

## What is NOT proved

- General type does not imply finiteness of rational points unconditionally.
- The absence of integral curves of degree 6 does not imply absence of perfect cuboids.
- The known low-degree classification does not rule out rational points lying on higher-degree curves or outside low-genus curves.
- Stage20 physical `M_face`-degree and canonical `P^6` degree on the endpoint surface are not identified without a proved adapter.
- No family-specific StageA2 exclusion is promoted to the whole endpoint.

```text
PERFECT_CUBOID_EXISTENCE_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
LOW_DEGREE_CURVE_THEOREM_IS_ENDPOINT_STRUCTURE_NOT_GLOBAL_POINT_CLOSURE=true
```

## Next checks before submission

1. lock exact theorem/proof locators for the complete-intersection/general-type and low-degree statements;
2. determine which of the known degree-2/4 curves are degenerate for the positive perfect-cuboid chamber;
3. determine whether the paper's quotient K3 is directly identifiable with any Stage20/Stage28 K3 or only related at a different quotient level;
4. extract any fibration / low-genus constraints that can become an exact Stage29 receiver;
5. search repo/StructureRadar for prior unnoticed provenance before calling these weapons new-to-repo.
