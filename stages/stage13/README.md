# Stage13 — active structural analysis

Current state:

```text
STAGE13_1=COMPLETE
STAGE13_2=COMPLETE
STAGE13_3=ACTIVE
STAGE13_3A=COMPLETE
STAGE13_3B=COMPLETE
STAGE13_3C=COMPLETE
STAGE13_3D=COMPLETE
STAGE13_3E=COMPLETE
NEXT=Stage13-3f
```

## Active organization

```text
stages/stage13/roadmap.md
stages/stage13/policy.md
stages/stage13/initial/definition.md
stages/stage13/initial/structural-decomposition.md
stages/stage13/main.md
stages/stage13/scripts/13-3/raw_incidence.py
stages/stage13/scripts/13-3/geometric_chamber.py
stages/stage13/scripts/13-3/parity_2adic.py
stages/stage13/scripts/13-3/representation_fiber.py
stages/stage13/scripts/13-3/representation_density.py
stages/stage13/data/13-3/raw_incidence_report.json
stages/stage13/data/13-3/geometric_chamber_report.json
stages/stage13/data/13-3/parity_2adic_report.json
stages/stage13/data/13-3/representation_fiber_report.json
stages/stage13/data/13-3/representation_density_report.json
```

`main.md` is the canonical living mathematical source. The completed Stage13-1/2 initial files remain as provenance; active mathematics is edited in `main.md`.

Stage13-3a established by complete finite enumeration that the near `2:1:1` shape is already present in raw face incidences before the exactly-one overlap sieve.

Stage13-3b isolated the canonical size-order / archimedean mechanism. On `0<a<b<c`, the exact one-face real-density weights satisfy `w_ab>w_ac>w_bc`; their chamber integrals give a `bc`-normalized geometric ratio about `2.4317:1.1158:1`, stronger than the observed raw `2.0660:1.0607:1`.

Stage13-3c audited parity and the prime `2`. Every primitive raw-incidence object has exactly one odd edge, odd space diagonal, and both even edges divisible by `4`. This admissibility condition is permutation-symmetric across the three one-face varieties, so a standalone `p=2` local factor cannot create a directional bias. Finite OE/EE parity types do couple with canonical order and visibly flatten the aggregate vector, but they do not by themselves close the gap to the observed ratio.

Stage13-3d resolved the Stage12 representation/fiber bridge exactly. For a canonical raw face incidence, the Stage12 ordered distinguished-face construction has exactly two records, one for each order of the two face legs; if full orientation is retained, each supported fiber has size `1`. Hence `C_prim(B)=2*(A_ab(B)+A_ac(B)+A_bc(B))`, direction by direction and separately in the OE/EE strata. Combining this exact bridge with the frozen Stage12 theorem gives the total raw-incidence asymptotic `A_ab+A_ac+A_bc ~ kappa/(24*pi) B(log B)^3`.

Stage13-3e then tested the remaining representation-density effect. For an outer shell `(p,z,d)`, let `R_prim` be the number of primitive face representations supported on that shell. At `B=100000`, the incidence-weighted means are about `4.88, 5.79, 5.93` in `ab,ac,bc`; thus `ab` lies on systematically poorer shells. Reweighting each shell to total weight one changes the `bc`-normalized ratio from `2.0660:1.0607:1` to about `2.3819:1.0610:1`, moving the finite vector about `80.8%` of the way from the raw data back toward the Stage13-3b archimedean vector in normalized-proportion `L1` distance. Pure `G(p)` deweighting alone gives a substantial but smaller correction. This is a finite diagnostic, not a categorywise asymptotic theorem.

The next mathematical step is Stage13-3f: test cutoff / boundary stability and synthesize the leading-`2` mechanism before moving to Stage13-4.

## File rule

Stage13 uses one living mathematical source. Corrections go directly into `main.md`; Git/PR history records earlier versions.

Stage13-specific support assets should use the stage/task in the path, with short functional filenames:

```text
stages/stage13/scripts/13-3/<purpose>.py
stages/stage13/data/13-3/<purpose>.json
```

Do not repeat long `stage13_...` suffixes in filenames when the directory already supplies that context.

Generated external-review bundles are created only on demand.
