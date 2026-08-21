# Stage29-02 Work import — independent foundation audit

```text
TASK_ID=Stage29-02-work-import
ROLE=INDEPENDENT_EXTERNAL_RESEARCH_INTAKE
SOURCE=perfect_cuboid_stage29_foundations_report.md
SOURCE_DATE=2026-08-21
STATUS=SUBMITTED_PENDING_FRESH_STAGE29_AUDIT
WORK_FINDINGS_ARE_NOT_SELF_CERTIFYING=true
PERFECT_CUBOID_CONCLUSION=NONE
```

## Purpose

This package imports an independent Work literature audit performed after the audited Stage29-02 parent screening. It does **not** replay Stage27/StructureRadar analytic gates and does not count the already-known full endpoint surface, joint V4 cover, canonical/physical polarization adapter, or Horie--Yamauchi L-function as newly discovered foundations.

The Work report found no published theorem proving existence or nonexistence of a perfect cuboid. Its main value is four endpoint-native routes that were absent or underused in the inspected Stage29 branches.

All statements below are research inputs pending fresh Stage29 audit against the cited primary sources.

## W29-A — finite global low-genus degree lock

Primary input: Freitag--Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), Theorem 3.1.

Candidate theorem lock:

```text
If C is an integral curve on the box/cuboid surface whose normalization map is bijective,
with geometric genus g and canonical/projective degree d, then

d <= 176 + 16 g.
```

Therefore the unibranch low-genus search is finite:

```text
g=0 -> even d <= 176
g=1 -> even d <= 192
```

The proposed adapter combines this bound with the audited Testa--Stoll rank-64 Picard lattice and Bruin--Thomas--Varilly-Alvarado node-span constraints, turning the rational/elliptic carrier problem into a finite lattice enumeration.

This is materially stronger than the already-merged degree-<=6 endpoint classification.

Critical firewall:

```text
BIJECTIVE_NORMALIZATION_REQUIRED=true
MULTIBRANCH_AT_NODE_CASES_NOT_COVERED=true
EFFECTIVITY_NOT_IMPLIED_BY_LATTICE_CLASS_ALONE=true
ISOLATED_RATIONAL_POINTS_NOT_EXCLUDED=true
```

Verdict from Work: `HIGH_VALUE`.

Proposed suffixes:

```text
29-02c-LG1=UNIBRANCH_LOW_GENUS_GLOBAL_DEGREE_LOCK
29-02c-LG2=PICARD_176_192_FINITE_ENUMERATION
```

## W29-B — Beauville irregular double cover / Albanese descent

Primary input: Arnaud Beauville, *A tale of two surfaces*, arXiv:1303.1910, Proposition 1 and Remark 1.

Candidate structural lock:

- there is a smooth irregular surface `X_Beau=(C x C)/Gamma` related to the cuboid canonical surface by a degree-two quotient;
- `q=4`, `p_g=7`, `K^2=32`;
- the canonical quotient is the four-quadric cuboid surface with 48 nodes;
- the construction carries an etale V4 tower over a product of genus-2 curves and an Albanese map to an abelian fourfold.

This is **not** the Stage29 joint V4 cover over `Y=Bl_4(P1 x P1)`: the geometry and arithmetic direction of the cover are different.

Exact new receiver proposed by Work:

```text
R29-BEAU1=PhysicalOpenBeauvilleDoubleCoverQDescentAndTwistLedger
R29-BEAU2=LocallySolubleBeauvilleTwistsToAlbaneseTorsors
```

A rational endpoint point need not lift to the untwisted cover over `Q`; the covering cocycle and quadratic twists must be tracked explicitly. Ignoring twists is forbidden.

Verdict from Work: `HIGH_VALUE`, technically risky.

Proposed suffix:

```text
29-02d=BEAUVILLE_IRREGULAR_COVER_DESCENT
```

## W29-C — exact M(4,8) modular Q-descent

Primary inputs: Freitag--Salvati Manni Theorems 2.4 and 6.1--6.3; Testa--Stoll Section 4; Fisher, *Explicit moduli spaces for congruences of elliptic curves*.

The useful receiver is not generic `X(8)` modularity. It is the exact Q-descent condition: over `Q(i)`, an endpoint point gives elliptic data with level-4 structure and a compatible symplectic 8-torsion isomorphism; over `Q`, Testa--Stoll formulate the conjugate-self-congruence condition.

Fisher's abundance results for ordinary 8-congruent elliptic curves are a firewall against the naive claim that 8-congruence alone is restrictive enough.

```text
R29-MOD1=ConjugateSelf8CongruenceWithLevel4QDescent
NAIVE_HECKE_OR_8_CONGRUENCE_OBSTRUCTION=RED
```

Verdict from Work: `PROMISING` only with the exact Q-descent adapter.

Proposed suffix:

```text
29-02g=MODULI_M4_8_Q_DESCENT
```

## W29-D — transcendental Brauer completion

Primary inputs: Testa--Stoll Theorem 10; Horie--Yamauchi arXiv:2512.22520v3.

Work reports that Testa--Stoll proves

```text
Br_1(S)/im Br(Q)=0.
```

Therefore another algebraic Brauer--Manin search is not a live route. The only potentially new Brauer receiver is the transcendental quotient, which would require integral Galois/cohomology information beyond the rational semisimplified L-function decomposition.

```text
ALGEBRAIC_BRAUER_ROUTE=RED_IF_THEOREM10_AUDITS
R29-BR1=TranscendentalBrauerIntegralLatticeOddPrimeAudit
R29-BR2=TranscendentalBrauerPrime2AndEvaluationAudit
```

The proposed use of Horie--Yamauchi is limited: L-function equality and rational l-adic constituents do not determine integral lattices, torsion, extension classes, or Brauer evaluation maps.

Verdict from Work: `PROMISING` / decisive audit of an obstruction class.

Proposed suffix:

```text
29-02f=TRANSCENDENTAL_BRAUER_AUDIT
```

## Existing routes not counted as new

The Work report explicitly does not count the following as new foundations:

- full four-quadric endpoint surface;
- joint V4 function field over the Stage28 two-face base;
- zero-loss canonical/physical polarization adapter;
- V4 character / cross-quotient L-function receiver already being developed in 29-02e;
- individual coordinate-sign K3 quotients or their elliptic fibrations;
- fiber-by-fiber Faltings/Chabauty without uniform base coverage;
- bare `X(8)xX(8)` modularity or Hecke-eigenvalue arguments;
- algebraic Brauer--Manin after Testa--Stoll Theorem 10;
- family-specific Saunderson/Peschmann closures without coverage.

## Hostile nonexistence screen

The report checked recent claims and found no endpoint-complete proof. The detailed ledger is in `nonexistence-claims-ledger.md`.

```text
RECENT_GLOBAL_NONEXISTENCE_PROOF_ACCEPTED=false
YELLE_2602_00239=RED_AS_GLOBAL_PROOF
PESCHMANN_FINITE_FIBERS=NOT_GLOBAL_COVERAGE
REED_FORMALIZATION=RED_AS_GLOBAL_PROOF
```

No result in this import changes the existing finite statement `P(B)=0` through the currently audited exact frontier into a global theorem.

## Priority proposed by Work

```text
1=29-02c-LG1 finite unibranch low-genus degree lock
2=29-02c-LG2 Picard 176/192 enumeration
3=29-02d Beauville irregular-cover Q descent
4=29-02f transcendental Brauer audit
5=29-02g exact M(4,8) Q descent
29-02e=continue existing V4/newform matching, not duplicate
```

This ordering is a research recommendation only. Fresh audit may reclassify or reject any route.

## Submission state

```text
NEW_EXTERNAL_INPUT_FOUND=true
NEW_FOUNDATION_CANDIDATES=2
DECISIVE_AUDIT_CANDIDATES=2
OLD_GATE_REPLAY=false
EARLIER_STAGE_BACKFLOW_RECOMMENDED=false
KEEP_STAGE29_NATIVE=true
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
ADVANCE_TO_29_03_BEFORE_ROUTE_AUDIT=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
NEXT_EXPECTED_COMMAND=Stage29-audit
```
