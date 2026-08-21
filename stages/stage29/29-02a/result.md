# Stage29-02a — global endpoint surface literature lock

```text
TASK_ID=Stage29-02a
ROLE=GLOBAL_ENDPOINT_SURFACE_LITERATURE_LOCK
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PARENT=Stage29-02
PERFECT_CUBOID_CONCLUSION=NONE
```

## 1. Why this subroute exists

Stage29-02 found the full perfect-cuboid/rational-box surface as a new endpoint foundation.  Stage29-02a checks whether strong existing mathematics already exists on exactly that surface before Stage29 attempts to rediscover it.

The answer is yes.  The main source is:

Damiano Testa and Michael Stoll, `Curves on the surface of cuboids`, Mathematics of Computation, DOI `10.1090/mcom/4238` (accepted 2026; open preprint arXiv:1009.0388 / author PDF `Cuboidi.pdf`).

Their projective surface `Sbar` is the Stage29 F1 endpoint surface after coordinate renaming only.

## 2. Exact source theorem surface imported

The source proves / records the following load-bearing facts.

1. `Sbar` is a geometrically integral complete intersection of multidegree `(2,2,2,2)` in `P^6`.
2. `Sbar` has exactly `48` isolated `A1` singularities.
3. For the minimal desingularization `S`, `K_S^2=16`; the canonical divisor is big and nef; `S` is a minimal surface of general type and `Sbar` is its canonical model.
4. The geometric Picard group has rank `64`; the full automorphism group is explicitly determined and has order `1536` in the source's setting.
5. The source completely classifies the integral curves of projective/canonical degree at most `6`.
6. In particular, **there are no integral curves of degree `6` on `Sbar`**.
7. All conics are among the known set `G`; there are no smooth rational quartics; all arithmetic-genus-one quartics are among the known curves.
8. Any rational curve other than a conic satisfies the source's stronger exceptional-divisor incidence bound `C.E>=8`; any geometric-genus-one curve satisfies `C.E>=4`.
9. The full surface carries `28` explicit genus-5 fibrations whose generic fibers have canonical/projective degree `8`.

Exact theorem/proof locators and the coordinate adapter are recorded in `source-lock.md`.

## 3. New positive-physical-chamber consequence

Testa--Stoll Corollary 18 says that the known set `G` is exactly the set of integral curves of canonical degree at most `6` on the desingularization.  Definition 6 describes `G` explicitly:

- exceptional curves above singularities;
- conics in `a_j=0` or long diagonal `c=0`;
- genus-one curves in `b_j=0`;
- genus-one curves in `a_j=±a_{j+1}` or `a_j=± i c`.

The Stage29 positive nondegenerate physical chamber meets none of these as a positive rational-box family:

- `a_j=0` or `c=0` is degenerate;
- `b_j=0` forces a degenerate real face;
- `a_j=±a_{j+1}` with nonzero rational sides would require a rational face diagonal equal to `sqrt(2)|a_j|`;
- `a_j=± i c` has no positive real point;
- exceptional curves lie over the singular/degenerate locus.

Hence:

```text
POSITIVE_NONDEGENERATE_ENDPOINT_CURVE_DEGREE_LE_6=ABSENT
FIRST_POSSIBLE_CANONICAL_CURVE_DEGREE_FOR_PHYSICAL_FAMILY>=8
```

This is a curve-family carrier statement, **not** a nonexistence theorem for isolated rational points.  Full details are in `physical-chamber-filter.md`.

## 4. New downstream weapon species

```text
S29-W01_CANDIDATE=FULL_ENDPOINT_CANONICAL_SURFACE_GEOMETRY
S29-W02_CANDIDATE=FULL_ENDPOINT_LOW_DEGREE_CURVE_CLASSIFICATION_THROUGH_6
S29-W03_CANDIDATE=POSITIVE_CHAMBER_LOW_DEGREE_FAMILY_FILTER
S29-W04_CANDIDATE=FULL_ENDPOINT_GENUS5_FIBRATION_ATLAS
```

These are new-to-repo weapon candidates imported from existing mathematics; they are not claimed as new mathematical theorems.

A future endpoint family can now be tested by

```text
candidate family
 -> exact map to full cuboid surface
 -> canonical/projective degree + genus + node incidence
 -> Testa--Stoll low-degree/fibration filter
 -> if still alive, optional A2-style cover/descent
```

No saving is multiplied across these steps.

## 5. Relation to Stage20 / Stage28 K3

Testa--Stoll Section 6 quotients the full surface by the sign change of the long diagonal.  The singular quotient `Kbar_c` is exactly the three-face Euler-brick complete intersection in `P^5`; its minimal desingularization `K_c` is a K3 surface, and the source obtains `15` elliptic fibrations on it.

Stage20 / Stage14-e8 independently presents the Euler-brick locus as the third-face double cover

```text
X_face -> Y=Bl_4(P1xP1)
```

resolving to a K3 surface.  Thus `K_c` and Stage20 `X_face` describe the same Euler-brick moduli on dense nondegenerate opens, but the exact global birational/polarization adapter has not yet been written in the repo.

New exact receiver:

```text
R29-K1=Stage20ToricK3ToTestaStollEulerK3BirationalPolarizationAdapter
```

This receiver must identify the dense-open map, exceptional divisors, Stage28 `M_face` inside `Pic(K_c)`, height conversion, and the 15 published elliptic fibrations.  Until then, Testa--Stoll projective degree and Stage28 physical `M_face` degree remain distinct.

See `euler-k3-bridge.md`.

## 6. Fibration consequence

The full endpoint surface has 28 explicit genus-5 fibrations with generic projective degree-8 fibers.  This is especially relevant because degree 8 is the first canonical curve degree not removed by the positive-chamber degree-<=6 filter.

The Euler K3 quotient `K_c` has 15 elliptic fibrations.  These may give explicit models for the Stage28 future receiver

```text
UniformMovingEllipticFibreSquareLiftHeightCount
```

only after `R29-K1` proves the physical/polarization adapter.

See `fibration-lock.md`.

## 7. Repo / Arsenal anti-loop check

Targeted repository searches found no direct existing artifact carrying the Testa--Stoll full-endpoint package under the authors, arXiv id, `X(8)`, general-type surface, Picard-rank-64, or 15-elliptic-fibration descriptors.

Adjacent existing weapons remain distinct:

- Stage20 / Stage14-e8 Euler K3;
- Stage28 common physical polarization and marginal fixed-curve spectrum;
- StageA2 family-specific descent;
- StructureRadar low-genus/moving-fibre receiver species.

```text
DIRECT_PRIOR_REPO_COPY_FOUND=false
NEW_TO_REPO_WEAPON_CANDIDATE=true
NEW_TO_MATHEMATICS=false
OLD_GATE_REPLAY=false
```

See `reuse-preflight.md`.

## 8. What is NOT proved

- General type does not imply finiteness of rational points unconditionally.
- Degree-six curve absence does not imply absence of perfect cuboids.
- The low-degree classification does not rule out isolated rational points or higher-degree curve carriers.
- Stage20 physical `M_face` degree is not endpoint canonical degree without `R29-K1`.
- The Testa--Stoll `K_c` / Stage20 `X_face` global isomorphism is not yet asserted by this repo.
- The 28 genus-5 or 15 elliptic fibrations do not give a counting exponent without arithmetic/height control.

```text
PERFECT_CUBOID_EXISTENCE_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEW_POPULATION_EXPONENT=false
```

## 9. 29-02a verdict

Stage29-02a has found materially useful existing endpoint geometry and has reduced its reuse to explicit adapters rather than another broad literature search.

```text
GLOBAL_ENDPOINT_EXISTING_GEOMETRY_FOUND=true
LOW_DEGREE_ENDPOINT_FILTER_FOUND=true
POSITIVE_CHAMBER_DEGREE_LE_6_FAMILY_FILTER=true
EULER_K3_BRIDGE_FOUND=true
PUBLISHED_FULL_SURFACE_FIBRATIONS_FOUND=true
OLD_STAGE_REENTRY_REQUIRED=false
KEEP_STAGE29_NATIVE=true
FURTHER_BROAD_SEARCH_REQUIRED=false
NEXT_DEEP_RECEIVERS=R29-K1,R29-FIB1,R29-FIB2
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage29-audit
```
