# Stage14 — exactly-two integral-face population

Stage14 studies the next layer above Stage13: primitive canonical cuboids with integer space diagonal and exactly two integral face diagonals.

## Current state

```text
STAGE14_1A=COMPLETE
STAGE14_1B=COMPLETE
STAGE14_1C=COMPLETE
STAGE14_1=COMPLETE
NEXT=Stage14-2
```

The canonical mathematical source is

```text
stages/stage14/main.md
```

and the active roadmap is

```text
stages/stage14/roadmap.md
```

## Counting convention

Use

\[
0<a<b<c,
\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,
\qquad d\le B.
\]

The three exactly-two directions are

```text
ab+ac only  <-> shared edge a <-> smallest edge shared
ab+bc only  <-> shared edge b <-> middle edge shared
ac+bc only  <-> shared edge c <-> largest edge shared
```

Write

\[
N_a^{(2)}=N_{ab,ac}^{(2)},
\qquad
N_b^{(2)}=N_{ab,bc}^{(2)},
\qquad
N_c^{(2)}=N_{ac,bc}^{(2)}.
\]

Stage14 also retains the raw pair-overlap vector

\[
\mathbf O=(O_{ab,ac},O_{ab,bc},O_{ac,bc})
\]

and the triple population `T(B)`. Exactly,

\[
\mathbf N_2^{\rm dir}=\mathbf O-T(1,1,1).
\]

Thus no perfect-cuboid nonexistence assumption is built into the counting convention.

## Stage13 interface

Stage14-1b identifies the raw pair and triple objects exactly with the Stage13 overlap ledger; there is no conversion multiplicity because both stages use the same primitive canonical ambient population and cutoff.

The inherited Stage13 finite seed table covers `B=1000` through `B=100000`. At the largest inherited cutoff,

```text
B=100000
O_ab_ac = 33
O_ab_bc = 33
O_ac_bc = 23
T       = 0

N_a^(2), N_b^(2), N_c^(2) = (33,33,23)
N_2 = 89
```

with the exact total checksum

\[
168208-168030=178=2\cdot89+3\cdot0.
\]

Stage13-7 also supplies the inherited ceiling

\[
N_a^{(2)},N_b^{(2)},N_c^{(2)},N_2=o(B(\log B)^3).
\]

This does not determine the true two-face scale; that remains the main Stage14-4 problem.

Machine-readable interface ledger:

```text
stages/stage14/data/14-1/stage13_pair_interface.json
```

## Enumeration contract

Stage14-1c fixes the Stage14-2 finite-counting contract.

```text
exact integer square tests only
canonical sort and dedup by (a,b,c,d)
recompute all three face flags after dedup
retain raw pair, triple and exactly-two ledgers
reproduce all seven inherited rows exactly
produce at least one verified cutoff above B=100000
never assume or silently discard T=0
```

Preferred extension ladder:

```text
200000 -> 500000 -> 1000000 -> 2000000
```

as computationally feasible. Correctness is not relaxed to reach a larger cutoff.

If `T(B)>0`, the enumerator must preserve full witness data

```text
a,b,c,d,d_ab,d_ac,d_bc
```

and trigger exact independent/manual verification.

The machine-readable enumeration/output specification is

```text
stages/stage14/data/14-1/enumeration_output_spec.json
```

The finite enumerator itself is independent of Stage13 proof review. If a Stage13 review changes only an asymptotic justification, Stage14 counting is unaffected. If it changes the ambient object or inherited seed numbers, Stage14-1b is re-audited before Stage14-2 publication.

## Main questions

Stage14 asks two quantitative questions simultaneously:

1. how fast does the total exactly-two population `N_2(B)` grow?
2. how do the three size directions `a/b/c` divide that population as `B` grows?

The first finite stages will enumerate and diagnose the population before any limiting law is assumed.

## Planned sequence

```text
14-1  definition / interface / counting specification   [complete]
14-2  complete finite enumeration                       [next]
14-3  finite directional-ratio evolution
14-4  true total growth order
14-5  directionwise asymptotic structure
```

The difficult analytic tasks `14-4` and `14-5` may use two-letter substages beginning at `aa`; this is only an organizational convention.
