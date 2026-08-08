# Stage14 — primitive canonical exactly-two-face population

> **STATUS:** `STAGE14_1A_COUNTING_CONVENTION_LOCKED`
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

### §1.8 Locked decision

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
