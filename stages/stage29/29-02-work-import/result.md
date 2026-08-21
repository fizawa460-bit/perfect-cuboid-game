# Stage29-02 Work import — audited independent foundation intake

```text
TASK_ID=Stage29-02-work-import
ROLE=INDEPENDENT_EXTERNAL_RESEARCH_INTAKE
SOURCE=perfect_cuboid_stage29_foundations_report.md
SOURCE_DATE=2026-08-21
STATUS=AUDITED_PASS_AFTER_BOUNDED_REPAIR
WORK_FINDINGS_ARE_NOT_SELF_CERTIFYING=true
PERFECT_CUBOID_CONCLUSION=NONE
```

This package imports an independent Work literature audit into the already-audited Stage29-02/02a/02b foundation layer. Fresh Stage29 audit was performed against the load-bearing primary sources; the authoritative details are in `audit.md`.

## W29-A — audited finite unibranch low-genus lock

Freitag--Salvati Manni Theorem 3.1 gives, for an integral curve on the box/cuboid surface whose normalization map is bijective,

```text
d <= 176 + 16g,
```

where `g` is the normalization genus and `d` is the projective/canonical degree. Hence, using the already-audited even-degree endpoint constraint,

```text
g=0 -> even d<=176
g=1 -> even d<=192.
```

The theorem/application lock formerly proposed as `29-02c-LG1` is therefore satisfied by this audit. The next step is the genuinely separate finite Picard-lattice/effectivity computation:

```text
29-02c-LG2=PICARD_176_192_FINITE_ENUMERATION.
```

Firewalls: bijective normalization/unibranch is required; multibranch-at-node curves remain open; lattice classes still need effectivity and physical-chamber tests; isolated rational points are not excluded.

## W29-B — audited Beauville structural route

Beauville's cuboid specialization supplies a distinct smooth irregular cover with

```text
q=4, pg=7, K^2=32,
canonical map degree=2,
canonical quotient=four-quadric cuboid surface with 48 nodes.
```

It also carries an etale `(Z/2)^2` tower and an Albanese map to an abelian fourfold. This is not the Stage29 joint V4 cover over `Bl_4(P1xP1)`. Its arithmetic value depends on field-of-definition, Q-descent and twist control.

```text
29-02d=BEAUVILLE_IRREGULAR_COVER_Q_DESCENT
R29-BEAU1=PhysicalOpenBeauvilleDoubleCoverQDescentAndTwistLedger
R29-BEAU2=LocallySolubleBeauvilleTwistsToAlbaneseTorsors
```

No rational endpoint point is assumed to lift to the untwisted cover over `Q`.

## W29-C — audited exact modular Q-descent receiver

The useful modular object is the exact `M(4,8)` / conjugate-self 8-congruence condition with level-4 data and Q-descent, not ordinary 8-congruence. Fisher-style abundance of ordinary 8-congruent pairs is retained as a firewall against a naive modular/Hecke obstruction.

```text
29-02g=MODULI_M4_8_Q_DESCENT
R29-MOD1=ConjugateSelf8CongruenceWithLevel4QDescent
NAIVE_ORDINARY_8_CONGRUENCE_OBSTRUCTION=RED
```

## W29-D — Brauer route, repaired scope

Testa--Stoll Theorem 10 does prove for the smooth proper minimal cuboid surface `S`

```text
Br_1(S)/im Br(Q)=0.
```

Thus the proper surface has no nonconstant algebraic Brauer class. The Work intake overreached by treating this as closure of the algebraic Brauer route on the **physical open**. Removing the degenerate/boundary divisors can create additional algebraic Brauer classes through residues, so `Br_1(U)` for the physical open `U` is not computed by Theorem 10 alone.

The retained suffix is therefore:

```text
29-02f=PHYSICAL_OPEN_BOUNDARY_AND_TRANSCENDENTAL_BRAUER_AUDIT
R29-BR0=PhysicalOpenBoundaryBrauerResidueAudit
R29-BR1=TranscendentalBrauerIntegralLatticeOddPrimeAudit
R29-BR2=TranscendentalBrauerPrime2AndEvaluationAudit
```

Horie--Yamauchi rational semisimplified l-adic/L-function data are input only; they do not determine integral torsion, extension classes or Brauer evaluations.

## Recent nonexistence screen

Fresh audit confirms that Yelle arXiv:2602.00239v2 is explicitly exploratory and does not claim a definitive impossibility theorem. Peschmann's unconditional result covers 1,072 explicit master-tuple fibers with `max(m,n)<=100`, not arbitrary endpoint coverage.

The detailed Work critique of the Jonathan Reed formalization was **not independently source-locked** in this audit. It remains provenance-only until an exact public repository/archive is locked and checked.

```text
RECENT_GLOBAL_NONEXISTENCE_PROOF_ACCEPTED=false
YELLE_V2_GLOBAL_PROOF=false_CONFIRMED
PESCHMANN_GLOBAL_COVERAGE=false_CONFIRMED
REED_DETAILED_CRITIQUE_AUDITED=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Audited routing

No imported route requires reopening Stage16--28. All accepted routes are Stage29-native and materially distinct from the frozen Stage27/28 gates.

```text
29-02c-LG1  SATISFIED_BY_PR1292_AUDIT
29-02c-LG2  PICARD_176_192_FINITE_ENUMERATION
29-02d      BEAUVILLE_IRREGULAR_COVER_Q_DESCENT
29-02e      EXISTING_V4_CHARACTER_NEWFORM_ROUTE_CONTINUES
29-02f      PHYSICAL_OPEN_BOUNDARY_AND_TRANSCENDENTAL_BRAUER_AUDIT
29-02g      MODULI_M4_8_Q_DESCENT
```

`29-03 FOUNDATION_BACKFLOW_DECISION` remains after the relevant 29-02 suffix work.

```text
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPAIR
NEW_EXTERNAL_INPUT_FOUND=true
OLD_GATE_REPLAY=false
BACKFLOW_TO_STAGE16_28=false
KEEP_STAGE29_NATIVE=true
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=29-02c-LG2
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
