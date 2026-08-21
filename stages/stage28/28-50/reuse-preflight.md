# Stage28-50 repository-wide reuse preflight

```text
DISCOVERY_CHECKPOINT=Stage28-50
PARENT_ROADMAP=docs/stage16-29-population-roadmap.md
COMPARISON=Stage19 -> Stage20
REPO_REUSE_PREFLIGHT=PASS
REUSE_SCOPE=ROADMAP,ARSENAL,STRUCTURE_RADAR,STAGES,PRS,LATEST_CONSTRUCTION_LITERATURE
NEW_RESEARCH_JUSTIFIED=true
```

## Canonical role

The roadmap defines checkpoint50 as the strongest certified lower-bound / construction ledger.  Stage28 is a matched comparison, not a literal subset transition, so construction floors may be compared only as floors or as explicitly named subfamilies; lower bounds alone may not order the full source and target populations.

## Audited source interfaces reused

### Stage19 / N2

Current lower:

\[
N_2(B)\gg B^{1/4}.
\]

Reused provenance includes Stage25 reentry PR #1003 and Stage27 lower reentry PR #1031.  The latter audits the known R501/R502 families as saturated two-dimensional families with physical height exponent eight and progress gate `kappa/h>1/4` for any genuine improvement.

### Stage20 / M3

Current pre-checkpoint50 lower:

\[
M_3(B)\gg_\varepsilon B^{1/3-\varepsilon}.
\]

Reused provenance is Stage26 checkpoint60 PR #1019.  It already proves:

- generalized Saunderson validity for every primitive Pythagorean input;
- primitive outputs;
- `>>T^2` primitive opposite-parity Euclid inputs with `r,s<=T`;
- physical height `R<72T^6`;
- `w^3` occurs as a physical face diagonal.

The old proof used `r_2(w^2)=B^o(1)` only to control output multiplicity.  This is therefore the exact place where a new inverse-map argument can strengthen the lower theorem without changing the construction.

## Prior routes explicitly not re-opened

- Stage27 R501/R502 fiber/gcd re-estimation: already saturated at `1/4`.
- Stage27 r8-r10 low-height / Saunderson / Peschmann square-lift routes: no `N2` lower above `1/4` survived audit.
- Stage20 historical one-parameter Saunderson `B^(1/6)` floor: superseded.
- finite effective exponents and finite databases: diagnostic only.
- perfect-cuboid intersection counting: off-stage endpoint and forbidden.

## Current external rematch

Checked current construction-side sources through August 2026:

- Peschmann, arXiv:2605.00573, Mordell-Weil Euler-brick generator;
- Peschmann, arXiv:2604.09328 and arXiv:2604.28072, master-tuple/fiber structure;
- Himane, arXiv:2405.13061, primitive Euler-brick generator.

No source supplies a matched primitive/canonical Euclidean-height power lower exceeding `1/3` for `M3`, or exceeding `1/4` for `N2`.  Peschmann's MW generator has rigorous output correctness and very large finite production but no uniform bounded-height count theorem of the required strength.

```text
STRONGER_PRIOR_M3_LOWER_FOUND=false
STRONGER_PRIOR_N2_LOWER_FOUND=false
FINITE_DATABASE_AS_ASYMPTOTIC_THEOREM=false
NOVELTY_BY_SEARCH_ABSENCE=false
```

## New route selected

The highest-leverage unexhausted internal route is the generalized Saunderson **physical inverse map**:

```text
chosen cube face diagonal -> w
opposite edge -> C=4uvw -> uv
(u^2+v^2=w^2, uv fixed) -> {u,v}
```

Because an output has only three faces, this targets an absolute fiber bound `<=3`.  It is materially new relative to Stage26's divisor-fiber proof and, if audited, removes the epsilon from the current one-third target lower.

```text
NEW_ROUTE=L1_GENERAL_SAUNDERSON_BOUNDED_FIBER
MATERIALLY_DISTINCT_FROM_PRIOR_STAGE26_PROOF=true
EXPECTED_STRENGTH=M3(B)>>B^(1/3)
AUDIT_REQUIRED=true
```
