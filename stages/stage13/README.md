# Stage13 — active structural analysis

Current state:

```text
STAGE13_1=COMPLETE
STAGE13_2=COMPLETE
STAGE13_3=COMPLETE_AT_STRUCTURAL_DIAGNOSTIC_LEVEL
STAGE13_3A=COMPLETE
STAGE13_3B=COMPLETE
STAGE13_3C=COMPLETE
STAGE13_3D=COMPLETE
STAGE13_3E=COMPLETE
STAGE13_3F=COMPLETE
STAGE13_4=ACTIVE
STAGE13_4A=COMPLETE
STAGE13_4B=COMPLETE
NEXT=Stage13-4c
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
stages/stage13/scripts/13-3/boundary_stability.py
stages/stage13/data/13-3/raw_incidence_report.json
stages/stage13/data/13-3/geometric_chamber_report.json
stages/stage13/data/13-3/parity_2adic_report.json
stages/stage13/data/13-3/representation_fiber_report.json
stages/stage13/data/13-3/representation_density_report.json
stages/stage13/data/13-3/boundary_stability_report.json
stages/stage13/scripts/13-4/ac_bc_gap.py
stages/stage13/scripts/13-4/ac_bc_cancellation.py
stages/stage13/data/13-4/ac_bc_gap_report.json
stages/stage13/data/13-4/ac_bc_cancellation_report.json
```

`main.md` is the canonical living mathematical source. The completed Stage13-1/2 initial files remain as provenance; active mathematics is edited in `main.md`.

Stage13-3a established by complete finite enumeration that the near `2:1:1` shape is already present in raw face incidences before the exactly-one overlap sieve.

Stage13-3b isolated the canonical size-order / archimedean mechanism. On `0<a<b<c`, the exact one-face real-density weights satisfy `w_ab>w_ac>w_bc`; their chamber integrals give a `bc`-normalized geometric ratio about `2.4317:1.1158:1`, stronger than the observed raw `2.0660:1.0607:1`.

Stage13-3c audited parity and the prime `2`. Every primitive raw-incidence object has exactly one odd edge, odd space diagonal, and both even edges divisible by `4`. This admissibility condition is permutation-symmetric across the three one-face varieties, so a standalone `p=2` local factor cannot create a directional bias. Finite OE/EE parity types do couple with canonical order and visibly flatten the aggregate vector, but they do not by themselves close the gap to the observed ratio.

Stage13-3d resolved the Stage12 representation/fiber bridge exactly. For a canonical raw face incidence, the Stage12 ordered distinguished-face construction has exactly two records, one for each order of the two face legs; if full orientation is retained, each supported fiber has size `1`. Hence `C_prim(B)=2*(A_ab(B)+A_ac(B)+A_bc(B))`, direction by direction and separately in the OE/EE strata. Combining this exact bridge with the frozen Stage12 theorem gives the total raw-incidence asymptotic `A_ab+A_ac+A_bc ~ kappa/(24*pi) B(log B)^3`.

Stage13-3e tested representation density. At `B=100000`, `ab` incidences lie on systematically poorer primitive representation shells than `ac/bc`. Equalizing shell weight moves the ratio from raw `2.0660:1.0607:1` to about `2.3819:1.0610:1`, strongly back toward the Stage13-3b archimedean vector `2.4317:1.1158:1`. Pure `G(p)` deweighting gives a substantial but smaller correction. This is finite structural evidence, not a categorywise asymptotic theorem.

Stage13-3f checked cutoff/boundary stability and closed the leading-two structural diagnostic. In the outer half of the largest search, `50000<d<=100000`, there are `94,209` raw incidences, about `56.0%` of the full `B=100000` incidence mass, yet the band ratio is `2.0651:1.0569:1`, essentially the same as the cumulative `2.0660:1.0607:1`; the normalized proportion vectors differ by only about `0.00126` in `L1`. From `B=50000` to `100000`, the raw, shell-neutral and pure-`G` diagnostics all move only slightly. Thus the largest observed cutoff boundary does not generate a competing leading ratio.

The Stage13-3 structural synthesis is therefore: canonical archimedean geometry creates the leading `ab` excess; arithmetic representation density materially flattens it toward the observed near-`2`; overlap, standalone prime-2 admissibility, projection fiber multiplicity and the largest observed cutoff boundary do not generate the leading effect. This closes Stage13-3 only at the structural finite-diagnostic level. No separate directional asymptotic constants and no limiting `2:1:1` theorem are claimed.

Stage13-4a started the two-near-`1` analysis. At `B=100000`, raw `ac/bc=1.0607458`, exact-one `1.0608294`, and the outer-half band `1.0569241`; the closeness is therefore not created by the exactly-one sieve or the largest cutoff boundary. Supported shell-neutralization also leaves aggregate `ac/bc` near `1.061`, while pure `G(p)` deweighting moves it to about `1.002`.

Stage13-4b resolves the immediate 4a ambiguity at the finite structural level. The near equality after pure-`G` deweighting is a cancellation, not an exact `ac<->bc` symmetry: at `B=100000`, the pure-`G` OE contribution has `ac/bc=0.95422` and weighted gap `-254.28`, while EE has `ac/bc=1.04547` and gap `+277.86`; their sum leaves only `+23.58`, giving aggregate `1.00202`. The same sign split persists in the outer half (`OE=0.95636`, `EE=1.05368`, aggregate `1.00685`). It is not stable at all smaller cutoffs, so the near equality cannot yet be promoted to a limiting law. Geometric subregions also cross from `bc`-heavy to `ac`-heavy under pure-`G` weighting: about `0.9156`, `0.9835`, `1.0417`, `1.0924` as `g=w_ac/w_bc` increases. Thus no universal local common factor equalizes `ac` and `bc`. Finally, the exact identity `1/R_prim=(R_all/R_prim)(1/R_all)` shows that primitive-support correction favors `ac`: its `G`-weighted mean factor is about `1.246` for `ac` versus `1.177` for `bc`, pushing the nearly cancelled pure-`G` vector back toward the observed `ac>bc` gap.

The next mathematical step is Stage13-4c: test whether the OE/EE and geometric cancellation has a stable scaling law as `B` grows, or whether the two near-`1` components remain a finite balance with no single asymptotic symmetry yet visible.

## File rule

Stage13 uses one living mathematical source. Corrections go directly into `main.md`; Git/PR history records earlier versions.

Stage13-specific support assets should use the stage/task in the path, with short functional filenames:

```text
stages/stage13/scripts/13-<task>/<purpose>.py
stages/stage13/data/13-<task>/<purpose>.json
```

Do not repeat long `stage13_...` suffixes in filenames when the directory already supplies that context.

Generated external-review bundles are created only on demand.
