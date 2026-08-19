# StructureRadar external-gate closure 29 — post-close triage

BATCH_ID=SR-BATCH-EXTERNAL_GATE_TRIAGE-29-R01
PHASE=EXTERNAL_GATE_CLOSURE
MODE=LIGHTWEIGHT_TRIAGE
EXTERNAL_GATE_COUNT_BEFORE=13
EXTERNAL_GATE_COUNT_AFTER=13
GATES_CLOSED=0

This batch implements the merged post-close policy before any repeated deep attack. It triages every remaining `EXTERNAL_GATE`, reuses merged prior work, and maps the gates to the current Stage27-19 / Stage27-20 barriers. No broad literature sweep is repeated and no Arsenal decision changes in this batch.

## Triage ledger

| card | class | Stage27 relevance | restart / blocker | priority |
|---|---|---|---|---|
| SR-STR-015 | PRIOR_DEEP_CLOSURE | Stage27-19 lower/family side; not the current fixed-R upper bottleneck | merged #1192 restart: `R504TwoFiberParityAlmostBelyiPrimitiveDegreeBound` | later deep attack |
| SR-STR-019 | PRIOR_DEEP_CLOSURE | HIGH for Stage27-20: exact nested-divisor/two-root MAIN receiver behind r302 | merged #1188 restart: `IndividualCellCommonParentNestedDivisorBilinearIncidenceEstimate`; every-cell form is stronger than the current exceptional-mass alternative | top-tier |
| SR-STR-021 | PRIOR_DEEP_CLOSURE | indirect fixed-U route only; MAIN measure adapter absent | merged #1188 restart: `ExceptionalZeroRepelledLogFreeZeroDensityForGaussianAngularRayCharacters` | lower |
| SR-STR-024 | PRIOR_DEEP_CLOSURE | HIGH adjacent to Stage27-20 conditioned filtered-tau3 / same-measure route | merged #1188 restart: `UniformFilteredQuotientCharacterVoronoiFunctionalEquationAdapter` | top-tier |
| SR-STR-162 | GENUINE_NEW_GATE | moving-family first-small-point frequency; not the current wall theorem | thin Pythagorean family frequency theorem still missing | later |
| SR-STR-167 | GENUINE_NEW_GATE | HIGH architecture match to Stage27-20 correlation | actual physical selector lacks bounded-complexity multiplicative/Hecke phase decomposition; pretentious structure alone is not a deficit | top-tier |
| SR-STR-168 | GENUINE_NEW_GATE | medium/high collision alternative for Stage27-20 | physical-mask-preserving norm-ratio pair correlation or polynomial-length Gaussian modulus/sample family missing | secondary |
| SR-STR-169 | GENUINE_NEW_GATE | HIGHEST direct match to Stage27-20 r302l | current theorem is exactly same-measure signed/arithmetic-host correlation; fixed-U/T-route forms cannot be cross-promoted to `H_phys^MAIN` | NEXT |
| SR-STR-170 | GENUINE_NEW_GATE | plausible Stage27-19 fixed-R outer-support/divisor-window route | reciprocal squareclass divisor-window transfer to charged physical measure missing | secondary Stage27-19 |
| SR-STR-171 | GENUINE_NEW_GATE | plausible Stage27-19 fixed-R shadow route | unitary-to-ordinary bounded-distortion plus window compatibility missing | secondary Stage27-19 |
| SR-STR-174 | GENUINE_NEW_GATE | HIGH for Stage27-20 q17-good/pushforward correlation | exact same-measure indicator-correlation lower bound on every principal cell missing; stronger than a weighted exceptional-mass alternative | top-tier |
| SR-STR-222 | PRIOR_DEEP_CLOSURE | fixed-U only; not directly MAIN | merged Thorner-Zaman partial upgrade leaves `RayClassToCanonicalSectorOrdinaryResidueAdapter`; safe Kai/Mitsui range already discharged | lower unless fixed-U reopens |
| SR-STR-223 | GENUINE_NEW_GATE | moving triple/fiber-product gate; not current Stage27-19/20 wall theorem | uniform moving-family compatible-small-point theorem missing | later |

## Stage27 priority decision

The current Stage27-20 checkpoint40 receiver is `UniformWallSlabMAINArithmeticHostCorrelationPowerDeficit` from audited r302j-l. Among the remaining StructureRadar gates, `SR-STR-169` is the closest receiver match because it already isolates the unresolved **same-measure signed selector correlation** architecture. However its archived fixed-U/T-route reductions do not identify their measure with the r302 MAIN physical host; audited r302d-f explicitly forbids that cross-measure promotion.

Therefore the next deep attack must be MAIN-native:

```text
NEXT_PRIORITY_STRUCTURE=SR-STR-169
NEXT_PRIORITY_RECEIVER=UniformWallSlabMAINArithmeticHostCorrelationPowerDeficit
REQUIRED_MEASURE=H_phys^MAIN
FIXED_U_OR_T_ROUTE_CROSS_PROMOTION=false
ALLOW_EXCEPTIONAL_MASS_ALTERNATIVE=true
```

`SR-STR-019`, `SR-STR-024`, `SR-STR-167`, and `SR-STR-174` remain top-tier supporting routes. In particular, the every-principal-cell forms in 019/174 are sufficient but stronger than r302's currently allowed weighted high-occupancy/exceptional-mass deficit, so the next attack should not unnecessarily require an every-cell theorem if a same-MAIN-measure exceptional-mass theorem can be proved.

## Stage27-19 note

The live Stage27-19 upper lane stops at fixed-R boundary factorization / outer-support counting. `SR-STR-170` and `SR-STR-171` are the closest remaining divisor-window/shadow architectures, but neither has the charged physical-measure transfer required for promotion. `SR-STR-015` is preserved at its deeper merged algebraic restart point and is not restarted now because it is not the immediate fixed-R upper bottleneck.

## Firewalls

- No `EXTERNAL_GATE` is closed by triage alone.
- No average-modulus, fixed-U, T-route, ambient, or different-measure result is promoted to the MAIN wall receiver without an exact adapter.
- Existing deep closure for 015/019/021/024 and the merged 222 partial upgrade are restart baselines; broad search is not repeated.
- `CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2`.
- `STRICT_SUBSQRT_POWER_SAVING_PROVED=false`.
- No perfect-cuboid existence/nonexistence claim is made.

```text
GATES_TRIAGED=13
GATES_CLOSED=0
REPO_RECONCILIATION_CLOSURES_AVAILABLE=0
PRIOR_DEEP_CLOSURE=5
GENUINE_NEW_GATE=8
NEXT_PRIORITY_STRUCTURE=SR-STR-169
NEXT_EXPECTED_COMMAND=StructureRadar-audit
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
```

VALIDATION_TRIGGER=CONNECTED_USER_EXACT_HEAD
