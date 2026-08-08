# Stage14 — primitive canonical exactly-two-face population

> **STATUS:** `STAGE14_1_COMPLETE_14_2_NEXT`
>
> **TRACK:** integer-space-diagonal / two-integral-face layer
>
> **CANONICAL_WORKING_FILE:** `stages/stage14/main.md`

Stage14 studies primitive canonical cuboids with integer space diagonal and **exactly two** integral face diagonals. The first objective is to count the three possible canonical two-face directions as the cutoff grows, then determine their growth scale and directional structure.

## §1. Stage14-1 — counting convention

### §1.1 Ambient object

For `B >= 1`, consider positive integer quadruples

\[
(a,b,c,d)\in\mathbf Z_{>0}^4
\]

satisfying

\[
0<a<b<c,
\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,
\qquad d\le B.
\]

Thus Stage14 keeps the same canonical order, primitive normalization and integer-space-diagonal cutoff as the Stage13 space-diagonal-first track.

Define the three face-square indicators

\[
I_{ab}=\mathbf 1_{a^2+b^2=\square},
\qquad
I_{ac}=\mathbf 1_{a^2+c^2=\square},
\qquad
I_{bc}=\mathbf 1_{b^2+c^2=\square}.
\]

### §1.2 The three raw pair populations

Before excluding three-face objects, define

\[
O_{ab,ac}(B)=\sum I_{ab}I_{ac},
\]

\[
O_{ab,bc}(B)=\sum I_{ab}I_{bc},
\]

\[
O_{ac,bc}(B)=\sum I_{ac}I_{bc},
\]

where the sums run over the ambient primitive canonical population above.

These are **at-least-the-specified-two-face** counts. A cuboid with all three integral face diagonals contributes once to each of the three raw pair populations.

Define the triple-overlap population

\[
T(B)=\sum I_{ab}I_{ac}I_{bc}.
\]

Inside the integer-space-diagonal ambient population, `T(B)` is precisely the primitive canonical perfect-cuboid population under the cutoff. Stage14 does not assume that `T(B)=0`.

### §1.3 Exactly-two directional populations

The primary Stage14 objects are the three **exactly-two** populations:

\[
\boxed{
N^{(2)}_{ab,ac}(B)=O_{ab,ac}(B)-T(B),
}
\]

\[
\boxed{
N^{(2)}_{ab,bc}(B)=O_{ab,bc}(B)-T(B),
}
\]

\[
\boxed{
N^{(2)}_{ac,bc}(B)=O_{ac,bc}(B)-T(B).
}
\]

Equivalently, the category conditions are

```text
ab+ac only:
  a^2+b^2 = square
  a^2+c^2 = square
  b^2+c^2 != square

ab+bc only:
  a^2+b^2 = square
  b^2+c^2 = square
  a^2+c^2 != square

ac+bc only:
  a^2+c^2 = square
  b^2+c^2 = square
  a^2+b^2 != square
```

The total exactly-two population is

\[
\boxed{
N_2(B)=N^{(2)}_{ab,ac}(B)+N^{(2)}_{ab,bc}(B)+N^{(2)}_{ac,bc}(B).
}
\]

Since the triple population is subtracted from each raw pair,

\[
\boxed{
N_2(B)=O_{ab,ac}+O_{ab,bc}+O_{ac,bc}-3T.
}
\]

### §1.4 Canonical direction = shared-edge size

Each two-face category has a unique shared canonical edge:

| exactly-two faces | shared edge | size-direction label |
|---|---|---|
| `ab + ac` | `a` | smallest-edge shared |
| `ab + bc` | `b` | middle-edge shared |
| `ac + bc` | `c` | largest-edge shared |

Accordingly Stage14 may use the shorter aliases

\[
\boxed{
N_a^{(2)}:=N^{(2)}_{ab,ac},
\qquad
N_b^{(2)}:=N^{(2)}_{ab,bc},
\qquad
N_c^{(2)}:=N^{(2)}_{ac,bc}.
}
\]

Both notations are retained in canonical documents: the face-pair notation records the literal square conditions, while the `a/b/c` notation records the geometric size direction.

There is a second equivalent size interpretation. Because `0<a<b<c`, the three face diagonals satisfy

\[
d_{ab}<d_{ac}<d_{bc}.
\]

Thus:

```text
ab+ac  = the two smaller face diagonals are integral
ab+bc  = the smallest and largest face diagonals are integral
ac+bc  = the two larger face diagonals are integral
```

### §1.5 Raw-pair and exactly-two ledgers are both retained

Stage14 will record both

\[
\mathbf O(B)=
(O_{ab,ac},O_{ab,bc},O_{ac,bc})
\]

and

\[
\mathbf N_2^{\rm dir}(B)=
(N_a^{(2)},N_b^{(2)},N_c^{(2)}).
\]

The raw pair vector is useful because it connects directly to the pair-overlap quantities already introduced in the one-face investigation. The exactly-two vector is the primary Stage14 population because it partitions the two-face layer without counting a three-face object in all three directions.

The exact relation is always

\[
\boxed{
\mathbf N_2^{\rm dir}(B)=\mathbf O(B)-T(B)(1,1,1).
}
\]

Therefore the raw and exactly-two **direction differences** are identical at every cutoff:

\[
N_a^{(2)}-N_b^{(2)}=O_{ab,ac}-O_{ab,bc},
\]

and cyclically. However their normalized ratios need not be identical if `T(B)>0`, so the two ledgers must not be silently identified.

### §1.6 What Stage14 will measure

For increasing cutoffs `B`, the finite stage will record at least:

```text
O_ab_ac(B), O_ab_bc(B), O_ac_bc(B)
T(B)
N_a^(2)(B), N_b^(2)(B), N_c^(2)(B)
N_2(B)
```

and directional diagnostics such as

\[
N_a^{(2)}:N_b^{(2)}:N_c^{(2)}
\]

plus normalized proportions

\[
P_q^{(2)}(B)=\frac{N_q^{(2)}(B)}{N_2(B)}.
\]

No growth law, limiting ratio, monotonicity, or perfect-cuboid existence/nonexistence statement is assumed at Stage14-1a.

### §1.7 Stage14 task split

The planned high-level sequence is

```text
14-1  definition / interface / counting specification
14-2  complete finite enumeration
14-3  finite directional-ratio evolution
14-4  true total growth order
14-5  directionwise asymptotic structure
```

Tasks `14-1` through `14-3` use ordinary letter substages as needed. Because `14-4` and `14-5` are expected to contain the difficult analytic work, their fine-grained substages may begin at `aa` rather than consuming the short letter namespace first.

This naming choice is organizational only and has no mathematical content.

### §1.8 Locked decision — 14-1a

```text
STAGE14_1A=COMPLETE
AMBIENT_SPACE_DIAGONAL_INTEGRAL=true
CANONICAL_ORDER=0<a<b<c
PRIMITIVE=gcd(a,b,c)=1
CUTOFF=d<=B
PRIMARY_POPULATION=exactly_two_integral_faces
RAW_PAIR_LEDGER_RETAINED=true
TRIPLE_POPULATION_RETAINED=true
PERFECT_CUBOID_NONEXISTENCE_ASSUMED=false
DIRECTION_a=ab+ac_smallest_edge_shared
DIRECTION_b=ab+bc_middle_edge_shared
DIRECTION_c=ac+bc_largest_edge_shared
NEXT=Stage14-1b Stage13 pair-overlap interface and inherited checksum
```

### §1.9 Stage14-1b — Stage13 pair-overlap interface

Stage14 does not introduce a new pair-count object. Its raw pair populations are exactly the pair-overlap quantities already counted in Stage13 under the same ambient convention:

\[
\boxed{
O_{ab,ac}^{(14)}(B)=O_{ab,ac}^{(13)}(B),
\quad
O_{ab,bc}^{(14)}(B)=O_{ab,bc}^{(13)}(B),
\quad
O_{ac,bc}^{(14)}(B)=O_{ac,bc}^{(13)}(B).
}
\]

Likewise the Stage14 triple population is the same Stage13 triple overlap,

\[
\boxed{T^{(14)}(B)=T^{(13)}(B).}
\]

There is no conversion multiplicity: both stages use primitive canonical objects with `0<a<b<c`, integer space diagonal, and the same cutoff `d<=B`. The only change of viewpoint is that Stage13 treated these quantities as overlap corrections to the one-face population, whereas Stage14 promotes them to the raw objects of interest.

The machine-readable interface ledger is

```text
stages/stage14/data/14-1/stage13_pair_interface.json
```

#### §1.9.1 Inherited finite seed table

The complete Stage13-3a enumeration already recorded the following pair/triple values:

| B | O_ab,ac | O_ab,bc | O_ac,bc | T | exactly-two vector (a,b,c) | N_2 |
|---:|---:|---:|---:|---:|---|---:|
| 1,000 | 2 | 0 | 0 | 0 | (2,0,0) | 2 |
| 2,000 | 2 | 2 | 1 | 0 | (2,2,1) | 5 |
| 5,000 | 6 | 6 | 3 | 0 | (6,6,3) | 15 |
| 10,000 | 9 | 11 | 5 | 0 | (9,11,5) | 25 |
| 20,000 | 16 | 16 | 10 | 0 | (16,16,10) | 42 |
| 50,000 | 24 | 24 | 14 | 0 | (24,24,14) | 62 |
| 100,000 | 33 | 33 | 23 | 0 | (33,33,23) | 89 |

These rows are inherited seed data, not a substitute for Stage14-2. Stage14-2 will independently reproduce the historical range where practical and extend the finite enumeration to larger cutoffs.

No conclusion is drawn from the fact that `T=0` in these audited rows; perfect-cuboid nonexistence is not assumed.

#### §1.9.2 B=100000 end-to-end checksum

At `B=100000`, Stage13 gives

\[
(A_{ab},A_{ac},A_{bc})=(84212,43236,40760)
\]

and

\[
(N_{ab},N_{ac},N_{bc})=(84146,43180,40704).
\]

Together with

\[
(O_{ab,ac},O_{ab,bc},O_{ac,bc})=(33,33,23),
\qquad T=0,
\]

the directional inclusion-exclusion checks are

\[
84212-84146=66=33+33-0,
\]

\[
43236-43180=56=33+23-0,
\]

\[
40760-40704=56=33+23-0.
\]

The Stage14 exactly-two vector is therefore exactly

\[
\boxed{
\mathbf N_2^{\rm dir}(100000)=(33,33,23),
\qquad N_2(100000)=89.
}
\]

At total-incidence level,

\[
168208-168030=178=2\cdot89+3\cdot0.
\]

The coefficient `2` here is not the Stage12 orientation factor: it is simply that an exactly-two-face object contributes two raw face incidences and zero exactly-one incidences. A three-face object would contribute three raw incidences, giving the exact identity

\[
\boxed{
A_{ab}+A_{ac}+A_{bc}-N_1=2N_2+3T.
}
\]

#### §1.9.3 Inherited asymptotic ceiling

Stage13-7jf/7jg proves, at the existing project theorem-application standard,

\[
O_{ab,ac}(B),\ O_{ab,bc}(B),\ O_{ac,bc}(B),\ T(B)
=o(B(\log B)^3).
\]

Because

\[
N_a^{(2)}=O_{ab,ac}-T,
\quad
N_b^{(2)}=O_{ab,bc}-T,
\quad
N_c^{(2)}=O_{ac,bc}-T,
\]

Stage14 immediately inherits

\[
\boxed{
N_a^{(2)}(B),\ N_b^{(2)}(B),\ N_c^{(2)}(B),\ N_2(B)
=o(B(\log B)^3).
}
\]

This is only an **upper-scale separation from the Stage13 one-face main term**. It does not identify the true two-face scale, exponent, logarithmic power, directional constants, or limiting ratio. Those remain open, with the true total order assigned to Stage14-4 and directionwise asymptotics to Stage14-5.

The inherited overlap theorem also does not imply `T(B)=0`; density zero relative to the one-face main term is not nonexistence.

### §1.10 Locked decision — 14-1b

```text
STAGE14_1A=COMPLETE
STAGE14_1B=COMPLETE
STAGE13_PAIR_INTERFACE=CLOSED
PAIR_OBJECT_CONVERSION_MULTIPLICITY=1
INHERITED_FINITE_SEED_DATA=true
B100000_EXACTLY_TWO_VECTOR=(33,33,23)
B100000_EXACTLY_TWO_TOTAL=89
INHERITED_PAIR_OVERLAP_BOUND=o(B(log B)^3)
INHERITED_TRIPLE_BOUND=o(B(log B)^3)
INHERITED_EXACTLY_TWO_BOUND=o(B(log B)^3)
TRUE_TWO_FACE_GROWTH_ORDER_IDENTIFIED=false
PERFECT_CUBOID_NONEXISTENCE_ASSUMED=false
NEXT=Stage14-1c enumeration/output specification
```

### §1.11 Stage14-1c — enumeration and output contract

Stage14-1c fixes what a Stage14-2 finite enumeration must count, validate and emit. It deliberately does **not** choose a growth model. The finite enumerator is a measurement instrument; asymptotic interpretation belongs to Stages14-3 through 14-5.

The machine-readable contract is

```text
stages/stage14/data/14-1/enumeration_output_spec.json
```

#### §1.11.1 Exact arithmetic and canonicalization

Every reported object must satisfy, using exact integer arithmetic,

\[
0<a<b<c,
\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,
\qquad d\le B.
\]

All face-square decisions must use an integer square test such as

```text
isqrt(n)^2 == n
```

or an equivalent exact test. Floating-point square decisions are forbidden.

Candidate records must be canonically sorted before counting and deduplicated by

```text
(a,b,c,d).
```

After deduplication, all three face flags `ab/ac/bc` are recomputed directly. The final category is determined only by those recomputed flags, not by the path that generated the candidate.

#### §1.11.2 Historical reproduction gate

Before any extended Stage14-2 table is accepted, the production enumerator must reproduce exactly all seven inherited rows

```text
B = 1000, 2000, 5000, 10000, 20000, 50000, 100000.
```

The expected values live in

```text
stages/stage14/data/14-1/stage13_pair_interface.json
```

and are treated as checksums. They are not used to manufacture the new counts.

If the production implementation is optimized, a logically independent or literal implementation should also be compared on feasible smaller cutoffs. Agreement is exact integer equality, not approximate numerical agreement.

#### §1.11.3 Extension ladder

Stage14-2 must produce at least one verified cutoff strictly above the inherited `B=100000` ceiling. The preferred extension ladder is

```text
200000
500000
1000000
2000000
```

as computationally feasible. The same cutoff must be used for all three directions. The highest reached cutoff is an implementation/performance fact, not a mathematical assumption; correctness checks are never relaxed merely to reach a larger `B`.

#### §1.11.4 Required output row

For each reported cutoff, retain at least

```text
B
O_ab_ac, O_ab_bc, O_ac_bc
T
N_a^(2), N_b^(2), N_c^(2)
N_2
P_a^(2), P_b^(2), P_c^(2)
a common normalized directional ratio when defined
candidate/dedup diagnostics
validation flags
```

The normalized proportions are

\[
P_q^{(2)}(B)=\frac{N_q^{(2)}(B)}{N_2(B)}
\]

when `N_2(B)>0`. A ratio whose chosen denominator is zero is recorded as null/undefined rather than forced numerically.

Stage14-2 may emit additional neutral diagnostics, but no fitted exponent, logarithmic power or limiting ratio is part of the required counting schema. Such fits belong to later analysis.

#### §1.11.5 Exact row identities

Every output row must satisfy

\[
N_a^{(2)}=O_{ab,ac}-T,
\]

\[
N_b^{(2)}=O_{ab,bc}-T,
\]

\[
N_c^{(2)}=O_{ac,bc}-T,
\]

and

\[
\boxed{
N_2=O_{ab,ac}+O_{ab,bc}+O_{ac,bc}-3T.
}
\]

Equivalently,

\[
O_{ab,ac}+O_{ab,bc}+O_{ac,bc}=N_2+3T.
\]

For historical cutoffs the row must additionally agree exactly with the locked Stage14-1b checksum table.

#### §1.11.6 Triple witness rule

No enumerator may assume `T=0` or silently discard three-face objects.

If any reported cutoff has

\[
T(B)>0,
\]

then the output must set a dedicated perfect-cuboid-candidate flag and persist witness records containing at least

```text
a,b,c,d,d_ab,d_ac,d_bc
```

for the triple objects. All seven defining square identities must then be recomputed with exact integer arithmetic, and the witness must be flagged for independent/manual verification.

Thus a hypothetical perfect cuboid is treated as data to preserve, not as an exceptional record to filter away.

#### §1.11.7 Stage13 review sensitivity

The Stage14-2 finite enumeration is logically independent of any later review correction to the Stage13 analytic proof. Stage13 seed rows are checksum targets only; new Stage14 rows are produced from the Stage14 enumerator itself.

If Stage13 review changes only the justification or status of an inherited asymptotic theorem, the Stage14-1c enumeration contract remains unchanged and the dependency tag can be updated separately.

If a Stage13 review instead changes the ambient counting definition or one of the inherited finite checksum values, Stage14-1b must be reopened/re-audited before Stage14-2 results are published. This prevents proof-review churn from silently changing the finite counting object.

#### §1.11.8 Stage boundary

The work division is now fixed:

```text
Stage14-2  validated finite population table
Stage14-3  finite directional-ratio evolution
Stage14-4  true total growth order
Stage14-5  directionwise asymptotic structure
```

No candidate asymptotic model is baked into the Stage14-2 enumerator.

### §1.12 Locked decision — 14-1c / Stage14-1 completion

```text
STAGE14_1A=COMPLETE
STAGE14_1B=COMPLETE
STAGE14_1C=COMPLETE
STAGE14_1=COMPLETE
ENUMERATION_CONTRACT_LOCKED=true
OUTPUT_SCHEMA_LOCKED=true
EXACT_INTEGER_SQUARE_TEST_REQUIRED=true
CANONICAL_DEDUP_KEY=(a,b,c,d)
HISTORICAL_REPRODUCTION_REQUIRED=true
HISTORICAL_ROWS_REQUIRED=7
EXTENSION_ABOVE_B100000_REQUIRED=true
TRIPLE_WITNESS_RETENTION_REQUIRED=true
GROWTH_MODEL_BAKED_INTO_ENUMERATOR=false
STAGE13_PROOF_REVIEW_CAN_CHANGE_ENUMERATION_CONTRACT=false_unless_object_or_seed_data_change
PERFECT_CUBOID_NONEXISTENCE_ASSUMED=false
NEXT=Stage14-2 complete finite enumeration
```
