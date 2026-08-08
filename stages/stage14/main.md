# Stage14 — primitive canonical exactly-two-face population

> **STATUS:** `STAGE14_2_COMPLETE_14_3_NEXT_14_4_PAUSED`
>
> **TRACK:** integer-space-diagonal / two-integral-face layer
>
> **CANONICAL_WORKING_FILE:** `stages/stage14/main.md`

Stage14 studies primitive canonical cuboids with integer space diagonal and **exactly two** integral face diagonals. The finite census is now independently audited through `B=2,000,000`. Stage14 proceeds through finite directional diagnostics in Stage14-3, then stops before asymptotic work until the one-face / Stage13 proof review is settled.

## §1. Locked counting convention

For `B>=1`, consider

\[
(a,b,c,d)\in\mathbf Z_{>0}^4
\]

with

\[
0<a<b<c,
\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,
\qquad d\le B.
\]

Define exact face-square indicators

\[
I_{ab}=\mathbf 1_{a^2+b^2=\square},\qquad
I_{ac}=\mathbf 1_{a^2+c^2=\square},\qquad
I_{bc}=\mathbf 1_{b^2+c^2=\square}.
\]

The raw pair populations are

\[
O_{ab,ac}=\sum I_{ab}I_{ac},\qquad
O_{ab,bc}=\sum I_{ab}I_{bc},\qquad
O_{ac,bc}=\sum I_{ac}I_{bc},
\]

and the triple population is

\[
T=\sum I_{ab}I_{ac}I_{bc}.
\]

No perfect-cuboid nonexistence assumption is made. A triple object is retained as data and must preserve the witness

```text
a,b,c,d,d_ab,d_ac,d_bc
```

for independent exact verification.

### §1.1 Exactly-two directions

The primary Stage14 populations are

\[
N_a^{(2)}:=N_{ab,ac}^{(2)}=O_{ab,ac}-T,
\]

\[
N_b^{(2)}:=N_{ab,bc}^{(2)}=O_{ab,bc}-T,
\]

\[
N_c^{(2)}:=N_{ac,bc}^{(2)}=O_{ac,bc}-T.
\]

Thus

```text
a-direction = ab+ac only = smallest shared edge
b-direction = ab+bc only = middle shared edge
c-direction = ac+bc only = largest shared edge
```

and

\[
\boxed{
N_2=N_a^{(2)}+N_b^{(2)}+N_c^{(2)}
=O_{ab,ac}+O_{ab,bc}+O_{ac,bc}-3T.
}
\]

Because `0<a<b<c`, the face diagonals satisfy

\[
d_{ab}<d_{ac}<d_{bc},
\]

so the same three classes may also be read as

```text
ab+ac = two smaller face diagonals integral
ab+bc = smallest and largest face diagonals integral
ac+bc = two larger face diagonals integral
```

### §1.2 Enumeration contract

All finite enumeration uses exact integer arithmetic.

```text
integer square tests only
canonical sort before counting
primitive gcd(a,b,c)=1
canonical dedup key=(a,b,c,d)
recompute all three face flags after dedup
retain raw pair, triple and exactly-two ledgers
never assume T=0
```

The machine-readable contract remains

```text
stages/stage14/data/14-1/enumeration_output_spec.json
```

Historical Stage13 values were used only as initial checksum targets. Stage14 now reproduces them independently.

### §1.3 Stage13 analytic quarantine

Stage13 is under independent external proof review. A previously recorded Stage13-derived statement

\[
N_2(B)=o(B(\log B)^3)
\]

is therefore **not an input to current Stage14 conclusions**. Its proof status will be revisited only after the Stage13 review is resolved.

Current Stage14 finite results satisfy

```text
STAGE13_CODE_IMPORTED=false
STAGE13_ASYMPTOTIC_RESULT_USED=false
```

The counting definition itself is independent of that analytic review.

## §2. Stage14-2 — finite census

### §2.1 Production route

The Stage14 production census is

```text
stages/stage14/scripts/14-2/two_face_census.py
```

It generates a distinguished integral face

\[
x^2+y^2=p^2
\]

and then glues

\[
p^2+z^2=d^2.
\]

After canonicalization and deduplication, all three face-square flags are recomputed directly from `(a,b,c)`.

Stage14-2a reproduced the historical seven cutoff rows exactly. Stage14-2b extended the same exact census through the full preferred ladder up to `B=2,000,000`.

### §2.2 Independent audit route

Stage14-2c adds

```text
stages/stage14/scripts/14-2/shared_leg_crosscheck.py
```

which uses a materially different generation order:

```text
generate integer Pythagorean faces
join two faces sharing one leg
form the two-face candidate first
then test a^2+b^2+c^2=d^2
canonicalize / primitive-filter / deduplicate
recompute all three face flags
```

Thus the production route begins with `face -> space diagonal`, while the audit route begins with `two faces sharing an edge -> space diagonal`.

The two routes agree exactly at all 11 audited cutoffs.

### §2.3 Frozen finite population table

| B | N_a^(2) | N_b^(2) | N_c^(2) | N_2 | T | c-normalized ratio |
|---:|---:|---:|---:|---:|---:|---|
| 1,000 | 2 | 0 | 0 | 2 | 0 | undefined |
| 2,000 | 2 | 2 | 1 | 5 | 0 | `2 : 2 : 1` |
| 5,000 | 6 | 6 | 3 | 15 | 0 | `2 : 2 : 1` |
| 10,000 | 9 | 11 | 5 | 25 | 0 | `1.8 : 2.2 : 1` |
| 20,000 | 16 | 16 | 10 | 42 | 0 | `1.6 : 1.6 : 1` |
| 50,000 | 24 | 24 | 14 | 62 | 0 | `1.714286 : 1.714286 : 1` |
| 100,000 | 33 | 33 | 23 | 89 | 0 | `1.434783 : 1.434783 : 1` |
| 200,000 | 42 | 50 | 24 | 116 | 0 | `1.75 : 2.083333 : 1` |
| 500,000 | 70 | 78 | 40 | 188 | 0 | `1.75 : 1.95 : 1` |
| 1,000,000 | 98 | 101 | 56 | 255 | 0 | `1.75 : 1.803571 : 1` |
| 2,000,000 | 142 | 134 | 80 | 356 | 0 | `1.775 : 1.675 : 1` |

All row identities pass exactly in both generation routes.

At the largest audited cutoff,

\[
\boxed{
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),
\qquad N_2=356,
\qquad T=0.
}
\]

No triple object was found through `B=2,000,000`. This is only a finite search result and does not imply perfect-cuboid nonexistence.

### §2.4 Finite leader reversal

The finite directional ordering is not stable on the audited range. In particular,

```text
B=200k   b > a > c
B=500k   b > a > c
B=1m     b > a > c
B=2m     a > b > c
```

Hence monotone convergence of the directional ratios is not assumed. Stage14-3 must treat the observed reversal as data to explain rather than noise to suppress.

### §2.5 Frozen artifacts

```text
stages/stage14/data/14-2/historical_reproduction_report.json
stages/stage14/data/14-2/extended_census_report.json
stages/stage14/data/14-2/shared_leg_crosscheck_report.json
stages/stage14/data/14-2/final_census_audit.json
stages/stage14/archive/stage14-2a-historical-reproduction.md
stages/stage14/archive/stage14-2b-extended-census.md
stages/stage14/archive/stage14-2c-census-closure.md
```

### §2.6 Locked decision — Stage14-2 completion

```text
STAGE14_2A=COMPLETE
STAGE14_2B=COMPLETE
STAGE14_2C=COMPLETE
STAGE14_2=COMPLETE
FINITE_CENSUS_FROZEN=true
INDEPENDENT_GENERATION_ROUTES=2
ALL_11_ROWS_MATCH=true
MAX_VERIFIED_B=2000000
PERFECT_CUBOID_WITNESS_FOUND=false
FINITE_LEADER_REVERSAL_OBSERVED=true
STAGE13_ANALYTIC_DEPENDENCY_USED=false
```

## §3. Next task — Stage14-3 only

Stage14-3 studies only finite directional behavior over the frozen 11-row census:

\[
N_a^{(2)}:N_b^{(2)}:N_c^{(2)}
\]

and

\[
P_q^{(2)}(B)=\frac{N_q^{(2)}(B)}{N_2(B)}.
\]

It may compute finite differences, local effective slopes, candidate fits, ratio trajectories and comparison diagnostics. These are empirical diagnostics only; Stage14-3 must not declare a growth exponent, limiting directional vector or monotonicity theorem from this finite range.

The purpose is to return with a finite-data map of what any later proof must explain.

## §4. Stop line

Current research policy is

```text
Stage14-3  finite directional diagnostics        NEXT / ALLOWED
Stage14-4  true total growth order               PAUSED
Stage14-5  directionwise asymptotic structure    PAUSED
```

Stage14-4 and Stage14-5 resume only after the one-face / Stage13 proof review clarifies which structural results are reliable enough to serve as a proof-level starting point.

```text
NEXT=Stage14-3 finite directional-ratio analysis
STOP_AFTER_STAGE14_3=true
STAGE14_4_STATUS=PAUSED_PENDING_ONE_FACE_REVIEW
STAGE14_5_STATUS=PAUSED_PENDING_ONE_FACE_REVIEW
```
