# Stage14 — exactly-two integral-face population

Stage14 studies the next layer above Stage13: primitive canonical cuboids with integer space diagonal and exactly two integral face diagonals.

## Current state

```text
STAGE14_1A=COMPLETE
NEXT=Stage14-1b
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

## Main questions

Stage14 asks two quantitative questions simultaneously:

1. how fast does the total exactly-two population `N_2(B)` grow?
2. how do the three size directions `a/b/c` divide that population as `B` grows?

The first finite stages will enumerate and diagnose the population before any limiting law is assumed.

## Planned sequence

```text
14-1  definition / interface / counting specification
14-2  complete finite enumeration
14-3  finite directional-ratio evolution
14-4  true total growth order
14-5  directionwise asymptotic structure
```

The difficult analytic tasks `14-4` and `14-5` may use two-letter substages beginning at `aa`; this is only an organizational convention.
