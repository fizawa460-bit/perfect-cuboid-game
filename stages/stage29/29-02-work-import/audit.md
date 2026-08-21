# Stage29-02 Work import — fresh audit

```text
AUDITED_PR=1292
AUDITED_SUBMISSION_HEAD=d548795f95b9c008098f07b2c86cb46ba7439a65
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPAIR
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
PERFECT_CUBOID_CONCLUSION=NONE
```

## Scope

Fresh audit checked the four imported research routes against primary sources where available, rematched them to the merged Stage29-02/02a/02b foundation layer, and audited the recent nonexistence ledger. The Work report is treated as research input, not self-certifying evidence.

## W29-A — Freitag--Salvati Manni low-genus degree lock

Primary source: E. Freitag and R. Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), Theorem 3.1.

Theorem 3.1 states exactly that for a curve `C` on the box variety whose normalization map is bijective, with normalization genus `g` and projective degree `d`,

```text
d <= 176 + 16g.
```

The same source identifies this degree with intersection against the canonical divisor on the desingularization. Testa--Stoll independently cite the same theorem for unibranch curves on the cuboid surface and explicitly record the rational bound `d<=176`.

Together with the audited parity result that all endpoint curve degrees are even:

```text
g=0 -> even d<=176
g=1 -> even d<=192.
```

The hypothesis is strong: bijective normalization means the curve is globally unibranch; multibranch behaviour at a node is not covered. The theorem does not exclude isolated rational points.

Because `K^2>0`, the orthogonal complement of `K` in the Picard lattice is negative definite; for fixed genus and bounded `K.C=d`, adjunction fixes `C^2`, so only finitely many lattice vectors occur in each bounded degree range. This makes a finite Picard-lattice enumeration a legitimate next step, but effectivity and physical-chamber admissibility still require proof.

```text
W29_A_AUDIT=PASS
FSM_THEOREM_3_1_AUDIT=PASS_EXACT
29_02C_LG1_STATUS=SATISFIED_BY_THIS_AUDIT
NEXT_LOW_GENUS_TASK=29-02c-LG2
MULTIBRANCH_RESIDUAL_OPEN=true
```

## W29-B — Beauville irregular cover / Albanese route

Primary source: A. Beauville, *A tale of two surfaces*, Proposition 1 and remarks in the cuboid specialization.

For the specialized genus-5 curves giving the cuboid surface, Beauville constructs a smooth surface `X=(C x C')/Gamma`, `Gamma~(Z/2)^2`, with

```text
q(X)=4
pg(X)=7
K_X^2=32.
```

Its canonical map has degree two and its quotient is exactly the four-quadric cuboid surface with 48 nodes after the displayed linear change of variables. Beauville also gives a `(Z/2)^2`-etale tower over a product of genus-2 curves and identifies the induced map to an abelian fourfold as the Albanese map.

This is genuinely different from the Stage29 joint V4 cover over `Bl_4(P1xP1)`. The geometric theorem is over the appropriate algebraic closure/complex setting; arithmetic use over `Q` requires a field-of-definition, descent and twist ledger. A rational endpoint point cannot simply be assumed to lift to the untwisted cover over `Q`.

```text
W29_B_AUDIT=PASS_AS_STRUCTURAL_ROUTE
BEAUVILLE_Q_DESCENT_SOLVED=false
29_02D_REQUIRED=true
```

## W29-C — modular `M(4,8)` / exact Q-descent

Freitag--Salvati Manni identify the finite box variety with the `M(4,8)` moduli problem after the required cyclotomic base field and describe pairs of elliptic curves with level-4 data and a compatible symplectic 8-torsion isomorphism. Testa--Stoll Section 4 gives the exact `Q`-form: a rational cuboid-surface point corresponds to an elliptic curve over `Q(i)` together with the conjugate-self 8-torsion isomorphism and specified action on the level-4 basis.

Fisher's explicit 8-congruence surfaces show why ordinary 8-congruence alone is not an endpoint obstruction. The live receiver is therefore the exact conjugate-self/level-4 descent condition, with cusps and stabilizers tracked.

```text
W29_C_AUDIT=PASS_AS_RECEIVER
29_02G_REQUIRED=true
NAIVE_ORDINARY_8_CONGRUENCE_OBSTRUCTION=RED
```

## W29-D — Brauer route; bounded repair

Testa--Stoll Theorem 10 is exact:

```text
Br_1(S)/im Br(Q)=0
```

for the smooth minimal projective surface `S`; equivalently the algebraic part of `Br(S)` contributes no nonconstant class, and the paper explicitly notes no algebraic Brauer--Manin obstruction to weak approximation on `S`.

The Work import overreached by saying that **only** the transcendental Brauer quotient remains for the physical endpoint. The physical nondegenerate locus is an open subset `U` of `S`. Removing boundary divisors can create additional algebraic Brauer classes through residue data, so Theorem 10 for proper `S` does not by itself compute `Br_1(U)`.

Therefore 29-02f is retained but repaired to start with the open-boundary residue question before the transcendental calculation:

```text
R29-BR0=PhysicalOpenBoundaryBrauerResidueAudit
R29-BR1=TranscendentalBrauerIntegralLatticeOddPrimeAudit
R29-BR2=TranscendentalBrauerPrime2AndEvaluationAudit
```

Horie--Yamauchi rational semisimplified l-adic/L-function information is useful input but does not determine integral torsion, extension classes or evaluation maps.

```text
W29_D_AUDIT=PASS_AFTER_SCOPE_REPAIR
PROPER_S_ALGEBRAIC_BRAUER_NONCONSTANT=ABSENT
PHYSICAL_OPEN_ALGEBRAIC_BRAUER_CLOSED=false
29_02F_REQUIRED=true
```

## Recent nonexistence screen

Yelle arXiv:2602.00239v2 was checked directly. The current v2 explicitly says the paper is exploratory and is **not** claiming a definitive impossibility result; it analyzes selected gluing strategies and ends with an open question. Hence it is not a global perfect-cuboid nonexistence theorem.

Peschmann arXiv:2604.28072 was checked directly. Its unconditional result is exactly on `1,072` explicit master-tuple fibers with `max(m,n)<=100`; it is not a uniform endpoint theorem.

The Work report's Jonathan Reed formalization critique was not independently source-locked in this audit. Its detailed RED rationale remains provenance-only and must not be cited as a repo-certified audit result until the exact public repository/archive is source-locked.

```text
YELLE_V2_GLOBAL_NONEXISTENCE=REJECTED_CONFIRMED
PESCHMANN_1072_FIBERS_GLOBAL_COVERAGE=false_CONFIRMED
REED_DETAILED_CRITIQUE_AUDITED=false
RECENT_GLOBAL_NONEXISTENCE_THEOREM_ACCEPTED=false
```

## Routing verdict

All accepted routes are Stage29-native. None supplies a reason to reopen Stage16--28. The low-genus theorem lock itself is complete in this audit, so the active extension queue is

```text
29-02c-LG2  PICARD_176_192_FINITE_ENUMERATION
29-02d      BEAUVILLE_IRREGULAR_COVER_Q_DESCENT
29-02e      EXISTING_V4/NEWFORM/CROSS-QUOTIENT_ROUTE
29-02f      BOUNDARY_PLUS_TRANSCENDENTAL_BRAUER_AUDIT
29-02g      MODULI_M4_8_Q_DESCENT
```

The queue represents materially distinct theorem/geometric hosts, not renamed Stage27/28 gates. `29-03 FOUNDATION_BACKFLOW_DECISION` remains after the relevant 29-02 suffix work rather than before it.

```text
NEW_EXTERNAL_INPUT_AUDIT=PASS
OLD_GATE_REPLAY=false
BACKFLOW_TO_STAGE16_28=false
KEEP_STAGE29_NATIVE=true
29_03_MUST_WAIT_FOR_RELEVANT_29_02_SUFFIXES=true
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=29-02c-LG2
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```