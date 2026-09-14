# Stage32 LGS-MB-02 — retained local-defect route archaeology

Status: `REPO_ARCHAEOLOGY_COMPLETE_NO_EXISTING_POPULATION_COMPLETE_DEFECT_BOUND`

This note is a no-recompute inspection of retained Stage32 source notes relevant to the new LGS/MB blocker.

## Reconnected frontier

LGS is reconnected only on `R29-LG2-MB` through MB101/MB102. The remaining blocker is:

`LGS_MB_MISSING_EXHAUSTIVE_LOCAL_DEFECT_RANGE_AND_DELTA_OFF_CONTROL`.

The question here is whether retained Stage32 work already supplies that missing information. It does not.

## Retained route archaeology

### post1648AN — exact feasibility wall

Source blob: `512fcc70afb1acf16956fd4b7a2b9b935a052150`.

AN proves that exceptional mass / node-preimage / multibranch counts plus a scalar genus-defect requirement are not contradictory by themselves. Minimal branches may land at distinct nonzero exceptional parameters and contribute zero exceptional-locus delta, while a large required genus defect can be placed at a smooth ambient point analytically. This is the direct anti-loop warning for LGS: MB101 counts cannot be promoted to delta bounds.

### post1648AO — special-fibre Hurwitz budget

Source blob: `242088adab5c86292154a6de9bc3563ba73b4f43`.

AO forces strong V6-specific normalization-branch and multibranch-node lower bounds from the two factor fibrations, but explicitly does not force exceptional landing collisions or convert global defect into exceptional defect.

### post1648AP — factor-pair conductor demand

Source blob: `f9a64fbfff0eabffbfa884cb43c5e4e62644a8c5`.

AP proves a V6-specific birational factor-pair image and an exact conductor-length demand. It identifies a concrete conductor obligation but does not upper-bound it or exclude its realization.

### post1648AR — two-factor slack / minimal-branch bound

Source blob: `da9b6ba755b8bd43d5b342d5540053caeb218f57`.

AR forces at least 186 V6 node branches to be the FSM-minimal local type. Their actual nonzero landing parameters remain unconstrained, so the large count is not a collision theorem.

### post1648AS — residual inertia / tangent preflight

Source blob: `cca79a4978c0cd5ea288ccba12ddafc9a5e3ffe5`.

AS identifies the exact local involution `lambda -> -lambda`, but proves that finite landing sets need not contain opposite pairs. The retained class/action data do not determine member-level landings or first jets. AS explicitly leaves two possible escapes: member-level landing/jet constraints or an independent global bound separating exceptional and off-exceptional contributions.

### post1648AT — quotient/blowup/conductor split

Source blob: `59849336b9e49610c00709b58989d17b9df1c6a7`.

AT exactly factors the V6 conductor demand into quotient and blowdown pieces. The factorization explains the required conductor rather than showing it is too large. The missing input remains member-level landing/jet information or an independent global singularity restriction.

### post1648AU — universal cusp-weight Bezout wall

Source blob: `c149dfe6c2bbbd4cb9614bfda441cf22d29c3a79`.

AU proves that the exact retained cusp multiplicities cannot by themselves force an auxiliary component by weighted Bezout, even allowing arbitrary cusp multiplicities. It explicitly requires genuinely stronger tangent/higher-jet relations or an independent global singularity inequality.

### Arsenal S34-W03

Source blob: `1d5275321f42768a6414d4610ac912c63be43f96`.

`S34-W03` is a formal receiver-intersection method: close a receiver by proving `B ∩ K` empty without classifying all of `B`. It does not supply the missing exact `K`, local-defect range, or `Delta_off` bound for LGS. Therefore it is a routing pattern, not the missing theorem.

## Deduplicated conclusion

The retained Stage32 archive already exhausts the following as stand-alone LGS closures:

- scalar exceptional mass / branch-count budgets;
- factor Hurwitz budgets without member-level landing information;
- cusp multiplicity alone;
- conductor accounting identities without an independent upper bound;
- residual involution action without actual landing/jet data;
- weighted Bezout using only the retained cusp multiplicities.

They must not be repeated as if MB101/102 newly made them sufficient.

## Live nonduplicate directions

Only two non-MB104 directions remain justified by this archaeology:

1. `POPULATION_WIDE_TANGENT_JET_OR_LANDING_CONSTRAINT` — a source-valid theorem/adapter forcing or bounding coincidences/intersections among allowed branches on the attacked `R29-LG2-MB` population.
2. `POPULATION_WIDE_GLOBAL_SINGULARITY_OR_DELTA_OFF_BOUND` — an independent inequality/theorem bounding intrinsic branch delta and/or off-exceptional `Delta_off` strongly enough to combine with MB102.

The third historical direction, global conductor/factor-cover gluing, overlaps the currently retained MB104 mission and is excluded from this re-entry PR by ownership firewall.

## Next bounded unit

`LGS_MB_03_EXTERNAL_THEOREM_AND_SOURCE_DISCOVERY_FOR_JET_OR_DELTA_OFF_BOUND`

Search authoritative sources and retained Arsenal only for the two nonduplicate directions above. A theorem name without exact hypotheses/object/population adapter is not progress.

No heavy compute, receiver exclusion, MAIN authority mutation, or merge credit follows from this archaeology.
