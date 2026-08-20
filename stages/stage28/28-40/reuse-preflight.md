# Stage28-40 repository-wide reuse preflight

```text
TASK_ID=Stage28-40
CHECKPOINT=40
PARENT_ROADMAP=docs/stage16-29-population-roadmap.md
COMPARISON=Stage19 -> Stage20
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,STRUCTURE_RADAR,STAGES,STAGE14_15_ATTACK_MAP,PRS,LITERATURE
STRONGEST_KNOWN_CHECK=PASS_FOR_CURRENT_UPPER_SURFACE
NEW_RESEARCH_JUSTIFIED=YES_DIRECT_BRIDGE_UPPER_AND_CAUSAL_LOCAL_COMPARISON
```

## Exact receiver

Stage28 compares the matched common-host shares

\[
\Sigma_{19}(B)=N_2(B)/H_{\ge2}(B),\qquad
\Phi_{20}(B)=M_3(B)/H_{\ge2}(B),
\]

with

\[
H_{\ge2}=M_2+M_3,\qquad
\mathcal R_{28}(B)=\frac{M_3(B)}{N_2(B)}=\frac{\Phi_{20}(B)}{\Sigma_{19}(B)}.
\]

The endpoint populations remain disjoint exact-face strata. `R28` is a population-size bridge ratio, not a survival probability.

## Reused project interfaces

Accepted:

- Stage19 / `SR-STR-145`: on the exactly-two shared-edge host, the space-square condition has split-prime acceptance
  \[
  \rho_p=\frac{p^4+4p^3+22p^2+4p+1}{(p+1)^2(p^2+6p+1)},
  \qquad 1-\rho_p=4/p+O(p^{-2}),
  \]
  while inert odd primes have acceptance `1`; this proves qualitative zero density with fixed finite prime sets and does **not** supply growing-modulus uniformity.
- Stage20 / `SR-STR-147`: the third-face local blocker on the matched two-face toric host has
  \[
  \delta_p=\frac{2(p-\chi_4(p))}{p^2+6p+1}=2/p+O(p^{-2}),
  \]
  with fixed-finite-set product law. Stage14-e11 separately supplies a growing-prime dimension-two Selberg sieve for this third-face system.
- `S26-W02`: `H_ge2=M2+M3`, `P=M2+3M3`, `Phi->0`, `Theta->0`, and `M3/M2->0`; incidence multiplicity is not probability.
- `S26-W03`: for fixed `0<eta<1/46`,
  \[
  M_3(B)\ll_\eta B(\log B)^{5-\eta}.
  \]
- Stage27 / `AR-006`: `N2(B)<<_epsilon B^(1/2+epsilon)` and the strict reattack did not improve the exponent.
- Stage27 / `S25-W01`: `N2(B)>>B^(1/4)`; Stage27 lower reattacks did not improve the exponent.
- Stage14/15 deep-review queue: moving-curve/Kummer/support routes require a new same-measure uniform theorem; reconstructed-graph and Pell/dispersion routes are frozen absent materially new input.
- StructureRadar literature batch17: Kummer and quartic-del-Pezzo literature checked there does not furnish the exact moving physical-height bridge theorem.

## Fresh literature rematch for checkpoint40

The current external rematch checked materially distinct upper-side species:

1. Glas--Hochfilzer, *Rational points on del Pezzo surfaces of low degree* (arXiv:2401.04759), Theorem 1.3: a degree-4 or degree-5 del Pezzo surface with a conic bundle has an effective `B^(1+epsilon)` rational-point upper bound. This is a fixed-variety anti-canonical-height theorem and does not improve the project Stage20 bound `B(log B)^(5-eta)` on the exact physical Euler population.
2. Peschmann, *Quartic reductions and elliptic obstructions for perfect Euler bricks* (arXiv:2604.09328): genus-3/elliptic obstruction machinery for the perfect-cuboid intersection; it explicitly does not solve the global problem and is not an `M3` counting upper theorem.
3. Peschmann, *A torsion-intersection proof ... on 1,072 explicit master-tuple fibers* (arXiv:2604.28072): unconditional fiberwise exclusions and a structural parametrization result, but no whole-family `M3/N2` counting inequality.
4. Peschmann, *Exponent-one blockers and a Mordell-Weil construction of Euler bricks* (arXiv:2605.00573): large verified construction/obstruction data and Mordell--Weil generation, but no primitive-canonical bounded-height asymptotic or bridge upper theorem.
5. Huerlimann's primitive-cuboid asymptotic counts the ambient equation `x^2+y^2+z^2=t^2`; it is not the Euler three-face population and is rejected as a population mismatch.

```text
DIRECT_STRONGER_M3_UPPER_FOUND=false
DIRECT_STRONGER_N2_LOWER_FOUND=false
DIRECT_PUBLISHED_M3_OVER_N2_BRIDGE_FOUND=false
LITERATURE_TRANSFER_WITHOUT_ADAPTER=false
```

## Why new Stage28 research is still justified

Checkpoint40 is not another Stage27 `N2` exponent attack. The genuinely new Stage28 receiver is a **relative same-host comparison** between the space-square and third-face completion mechanisms. It can in principle improve `M3/N2` without determining either individual true exponent.

The main-batch therefore opens only this relative receiver and does not reopen frozen Stage27 routes.