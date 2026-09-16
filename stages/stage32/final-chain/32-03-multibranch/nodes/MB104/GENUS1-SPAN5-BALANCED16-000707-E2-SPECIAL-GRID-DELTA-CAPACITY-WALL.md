# Stage32 MB104 — `000707000f0f` e=2 special-grid delta-capacity wall

Status: **RETAINED EXACT NEGATIVE ROUTING RESULT / ORDINARY MULTIBRANCH DELTA LOWER BOUND IS AUTOMATICALLY WITHIN THE GENUS BUDGET / TANGENCY DATA STILL REQUIRED / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

The retained joint-pair leaf gives a birational normalization map

```text
Psi:E -> C subset R x R = P1 x P1
```

with

```text
[C]=(28l,28l),
g(E)=1.
```

The retained low-bidegree leaf gives sixteen exact residual special points with branch masses

```text
A+,A-,...,H+,H-
```

and total mass `112l`. This note tests the most direct next use of the singularity delta budget: sum the universal lower bound `binomial(r,2)` at those sixteen points and compare it with the total normalization defect of `C`.

## 1. Total delta budget of the bidegree curve

For a reduced curve of bidegree `(n,n)` on `P1 x P1`,

```text
p_a(C)=(n-1)^2.
```

Here `n=28l` and the normalization has genus one, so

```text
delta(C)=p_a(C)-1
        =n^2-2n
        =784l^2-56l.                            (TOTAL-DELTA)
```

For any reduced curve singularity with `r` normalization branches,

```text
delta_p
 = sum_i delta(branch_i) + sum_(i<j) I(branch_i,branch_j)
 >= binomial(r,2).                              (BRANCH-DELTA)
```

Thus, if `w(P)` is the branch mass at one of the sixteen special points,

```text
delta_special
 >= S_special := sum_P binomial(w(P),2).        (SPECIAL-LOWER)
```

A contradiction from this route would require `S_special > delta(C)`.

## 2. Saturation already bounds the branch-mass square energy

For either zero-quartic block, the eight special masses occur in four complementary pairs with fixed pair totals

```text
16l, 16l, 16l, 8l.
```

The retained saturated coordinate fibre chooses one member from each complementary pair and has total mass exactly

```text
28l.
```

Write the chosen four masses as

```text
y1,y2,y3,y4
```

with

```text
0<=y1,y2,y3<=16l,
0<=y4<=8l,
y1+y2+y3+y4=28l.
```

The sum of squares of all eight masses in the block is

```text
B
 = y1^2+(16l-y1)^2
 + y2^2+(16l-y2)^2
 + y3^2+(16l-y3)^2
 + y4^2+(8l-y4)^2.
```

Scaling by `l`, this is a convex quadratic on a bounded slice. Its maximum is attained at a vertex. Exact enumeration of the vertices gives

```text
B <= 736 l^2.                                   (BLOCK-SQ)
```

For example, after scaling `l=1`, a maximizing vertex is

```text
(y1,y2,y3,y4)=(0,16,12,0),
B=736.
```

The Q0 and Q1 blocks have the same complementary-pair profile and the same `28l` saturation. Therefore

```text
sum_(16 special P) w(P)^2 <= 1472 l^2.          (SQ)
```

This uses only the already-retained saturation and branch bounds; none of the newer irreducible `(1,1)/(1,2)/(2,1)` Bezout inequalities is needed.

## 3. The naive delta lower bound can never exhaust the genus budget

Since

```text
sum_P w(P)=112l,
```

we have

```text
S_special
 = (sum_P w(P)^2 - 112l)/2
 <= 736l^2-56l.                                 (SPECIAL-CAP)
```

Comparing with `(TOTAL-DELTA)`,

```text
delta(C) - S_special
 >= (784l^2-56l)-(736l^2-56l)
 = 48l^2.                                       (HEADROOM)
```

Hence the ordinary-multiple-point lower bound at the sixteen special grid points is **always at least `48l^2` short of contradiction** once the retained saturation equations hold.

Equivalently, in the thin-shell variables `l=2m` and

```text
Q=sum_j b_j^2,
X=b0*b2+b1*b3+b8*b10+b9*b11+b24*b26+b32*b34,
```

the delta-budget necessary condition is

```text
Q+2X <= 368m^2,
```

whereas the saturation square bound already gives the stronger universal inequality

```text
Q+2X <= 320m^2.                                 (REDUNDANT)
```

So the naive special-grid delta test is strictly redundant.

## 4. Exact check on the current formal survivor

For the retained low-bidegree survivor

```text
m=5, l=10,
b=(-16,-20,-20,4, 1,18,-19,20, -20,-20,-20, -20,-19,19)
```

in the retained node order, exact evaluation gives

```text
Q=4480,
X=601,
Q+2X=5682,
320m^2=8000,
368m^2=9200.
```

Its sixteen branch masses are

```text
(8,152,48,112,0,160,0,80,44,116,156,4,78,82,2,78),
```

so

```text
S_special=63768,
delta(C)=77840,
delta(C)-S_special=14072.
```

The survivor therefore also passes this delta test with substantial slack. This remains formal allocation data only; no geometric realization is asserted.

## Routing consequence

Do **not** continue the route

```text
special-point branch multiplicities
 -> use only delta_p >= binomial(r_p,2)
 -> expect to exhaust the genus-one bidegree delta budget.
```

The exact saturation package prevents that lower bound from reaching the total delta budget.

A genuinely stronger singularity route would need information beyond branch count, for example:

- forced tangent coincidences giving `I(branch_i,branch_j)>1`;
- singular individual branches with positive intrinsic delta;
- a source-locked relation forcing additional non-special singularities;
- monodromy/Nielsen data or the actual conductor-loop `0` versus `gamma_Q` comparison.

The active leaf and its current conductor-loop obligation remain unchanged.

## Firewalls

- `(BRANCH-DELTA)` is only a lower bound; this note does not upper-bound the actual special-point delta.
- The `48l^2` headroom rules out only the branch-count-only delta attack.
- No tangency multiplicity is inferred from residual-grid coincidence.
- No conductor loop is evaluated.
- No branch allocation is claimed geometrically realizable.
- No weighted-cut upper bound or e=2 closure is claimed.
- `e=4`, `000707000f0f`, MB104, span5, finite-window, receiver, effectivity, theorem, endpoint and Perfect-Cuboid credit remain open/zero.
- No heavy compute is armed.
- No merge or rebase authorization.
