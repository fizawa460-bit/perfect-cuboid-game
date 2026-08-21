# Stage29-02a — repo / Arsenal reuse preflight

Stage29 requires reuse-first and anti-loop checks before calling a route new.

## Repo search

Targeted repository searches were performed for:

```text
arXiv 1009.0388
Michael Stoll / Damiano Testa + cuboid
surface parametrizing cuboids
general type cuboid surface
X(8) cuboid
Picard rank 64
15 elliptic fibrations Euler brick K3
```

No direct existing Stage/StructureRadar artifact carrying the Testa--Stoll full-surface low-degree theorem package was found by these searches.

The repo already contains adjacent but different geometry:

- Stage20 / Stage14-e8: Euler-brick K3 as the third-face double cover of the two-face toric base;
- Stage28: common physical polarization and fixed-curve spectrum on the two marginal K3 covers;
- StageA2: family-specific cover/descent closure;
- StructureRadar `SR-STR-163`, `SR-STR-223`: low-genus / moving-fiber structural and theorem-gate species.

None of these is the full endpoint canonical-surface classification through projective degree 6.

## Novelty verdict

```text
DIRECT_PRIOR_REPO_COPY_FOUND=false
NEW_TO_REPO_WEAPON_CANDIDATE=true
NEW_TO_MATHEMATICS=false
SOURCE_IS_EXISTING_EXTERNAL_THEOREM=true
OLD_GATE_REPLAY=false
```

The claim is only that this is a newly imported **repo weapon**, not a novel mathematical theorem.

## Selection firewall

- Do not replace Stage28 `M_face` degree by endpoint canonical degree without `R29-K1`.
- Do not infer endpoint point-finiteness from general type.
- Do not use the low-degree classification as a whole-population count.
- Do not call the Testa--Stoll Euler K3 globally identical to Stage20 `X_face` until the explicit birational/polarization adapter is audited.
