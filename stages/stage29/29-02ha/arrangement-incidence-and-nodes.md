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

**geometric** points above it. Therefore

\[
6\times8=48
\]

geometric `A1` singularities occur on `Sbar`.

At a transverse double intersection, the local model is simply `u^2=r, v^2=s`, which is smooth after using `u,v` as local coordinates; these points do not create endpoint singularities.

## Arithmetic field split of the 48 nodes

The field of definition is visible directly from the four nonzero branch values at each triple point.

At

```text
[0:0:1], [0:1:0], [1:0:0]
```

the nonzero values have one common rational squareclass. Hence all eight nodes above each of these three base points are `Q`-defined:

```text
3 * 8 = 24 Q-defined nodes.
```

At

```text
[0:1:-1], [1:0:-1], [1:-1:0]
```

the nonzero values have squareclasses `1` and `-1`. The fibers therefore require `sqrt(-1)` and all eight nodes over each triple point are defined over `Q(i)` but not over `Q`:

```text
3 * 8 = 24 strictly Q(i)-defined nodes.
```

Thus the seven-line cover independently recovers the previously audited exceptional-node Galois split

```text
24/Q + 24/Q(i).
```

The committed `arrangement_check.py` verifies this squareclass calculation exactly.

```text
R29-KUM0A=SevenLineIncidenceLedger
STATUS=PASS_AUDITED_EXACT
R29-KUM0B=SixTriplePointsTimesEightEquals48A1
STATUS=PASS_AUDITED_EXACT_LOCAL_MODEL
NODE_FIELD_SPLIT=24_Q_PLUS_24_STRICT_QI
NODE_FIELD_SPLIT_AUDIT=PASS
```
