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
STAGE13_4=COMPLETE_AT_STRUCTURAL_FINITE_DIAGNOSTIC_LEVEL
STAGE13_4A=COMPLETE
STAGE13_4B=COMPLETE
STAGE13_4C=COMPLETE
NEXT=Stage13-5
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
stages/stage13/scripts/13-4/ac_bc_scaling.py
stages/stage13/data/13-4/ac_bc_gap_report.json
stages/stage13/data/13-4/ac_bc_cancellation_report.json
stages/stage13/data/13-4/ac_bc_scaling_report.json
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

Stage13-4b showed that the pure-`G` near equality is a cancellation, not an exact `ac<->bc` symmetry. At `B=100000`, pure-`G` OE has `ac/bc=0.95422` and weighted gap about `-254.28`, while EE has `ac/bc=1.04547` and gap about `+277.86`; the residual total gap is only about `+23.58`. Low-`g` geometric regions are `bc`-heavy and high-`g` regions are `ac`-heavy. Primitive support then tilts the balance back toward `ac`.

Stage13-4c scales that cancellation and closes Stage13-4 at the structural finite-diagnostic level. The exact finite decomposition

```text
r_raw(B) = r_G(B) * F_prim(B) * F_shell(B)
```

separates pure-`G`, primitive-support and supported-shell effects. For `B>=10000`, the primitive-support factor is unusually stable, ranging only from about `1.05872` to `1.06499`, while the pure-`G` ratio ranges from about `0.95316` to `1.00202`. At `B=100000`,

```text
1.0607458 = 1.0020209 * 1.0588757 * 0.9997457.
```

Thus the observed `ac/bc` gap is, at the largest cutoff, almost exactly a near-one pure-`G` cancellation multiplied by a roughly `1.059` primitive-support tilt, with supported-shell restoration nearly neutral. The fresh outer half independently reproduces the mechanism: pure-`G` OE is `0.95636`, EE is `1.05368`, aggregate `1.00685`, and the fixed geometric bins run monotonically from about `0.9087, 0.9729, 1.0605, 1.1176`. However the cancellation is not stable at all smaller bounds or annuli, so no exact or asymptotic secondary balance law is claimed.

The Stage13-4 structural synthesis is therefore: the two near-`1` components do not arise from one exact symmetry. At late audited scales, parity and geometric subregions contribute opposite signed gaps that cancel strongly; a comparatively stable primitive-support correction supplies the residual `ac>bc` tilt. This is a finite structural explanation only.

The next mathematical step is Stage13-5: define a quantitative deviation from `(1/2,1/4,1/4)` before classifying its structural sources.

## File rule

Stage13 uses one living mathematical source. Corrections go directly into `main.md`; Git/PR history records earlier versions.

Stage13-specific support assets should use the stage/task in the path, with short functional filenames:

```text
stages/stage13/scripts/13-<task>/<purpose>.py
stages/stage13/data/13-<task>/<purpose>.json
```

Do not repeat long `stage13_...` suffixes in filenames when the directory already supplies that context.

Generated external-review bundles are created only on demand.
