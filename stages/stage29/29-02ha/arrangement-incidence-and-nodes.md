# Stage29-02ha — seven-line incidence and the 48 nodes

Label the branch lines

```text
A1: x=0
A2: y=0
A3: z=0
B3: x+y=0
B2: x+z=0
B1: y+z=0
C : x+y+z=0
```

Their projective intersection pattern over characteristic zero is

```text
t3 = 6 triple points
t2 = 3 double points
no point of multiplicity >=4.
```

The six triple points are

```text
[0:0:1]   A1 A2 B3
[0:1:0]   A1 A3 B2
[1:0:0]   A2 A3 B1
[0:1:-1]  A1 B1 C
[1:0:-1]  A2 B2 C
[1:-1:0]  A3 B3 C
```

and the three remaining double points are the pairwise intersections of `B1,B2,B3`:

```text
[1:-1:-1], [1:-1:1], [1:1:-1].
```

## Local singularity over a triple point

Near a triple point choose local branch equations `r=0`, `s=0`, `r+s=0`. The corresponding three square roots satisfy

\[
u^2=r,\qquad v^2=s,\qquad w^2=r+s,
\]

so after eliminating `r,s`,

\[
w^2=u^2+v^2.
\]

This is an ordinary quadratic cone, hence an `A1` rational double point in characteristic not two.

The three local inertia generators are independent in `G_sign`, giving inertia order `2^3=8`. Since the global degree is `64`, each base triple point has

\[
64/8=8
\]

points above it. Therefore

\[
6\times8=48
\]

`A1` singularities occur on `Sbar`.

At a transverse double intersection, the local model is simply `u^2=r, v^2=s`, which is smooth after using `u,v` as local coordinates; these points do not create endpoint singularities.

Thus the entire Testa–Stoll `48 A1` ledger is recovered from one finite line-arrangement calculation.

```text
R29-KUM0A=SevenLineIncidenceLedger
STATUS=PASS_CANDIDATE_EXACT
R29-KUM0B=SixTriplePointsTimesEightEquals48A1
STATUS=PASS_CANDIDATE_EXACT_LOCAL_MODEL
```
