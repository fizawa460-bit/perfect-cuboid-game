# Stage14-e1 — two-face ambient control population

> STATUS: `STAGE14_E1_COMPLETE_DEFINITION_BIJECTION_AND_FINITE_AUDIT`
>
> TRACK: front-side control population
>
> INTEGER SPACE DIAGONAL CONDITION: deliberately removed
>
> LITERATURE POLICY: mandatory collision audit before later theorem/novelty claims

## 1. Ambient counting convention

Count positive integer triples `(e,x,y)` with

\[
x<y,\qquad \gcd(e,x,y)=1,
\]

such that the two faces sharing `e` are Pythagorean:

\[
e^2+x^2=u^2,\qquad e^2+y^2=v^2.
\]

Define the ordinary real Euclidean space diagonal only as a height

\[
\boxed{D_{\mathbf R}=\sqrt{e^2+x^2+y^2}}
\]

and impose

\[
D_{\mathbf R}\le B.
\]

There is **no** requirement that `D_R` be rational or integral.

The raw ambient population permits the remaining face diagonal to be integral. The exactly-two ambient population excludes it:

\[
x^2+y^2\ne \square.
\]

Directions are purely the chamber position of `e`:

```text
a: e < x < y
b: x < e < y
c: x < y < e
```

Write the exactly-two ambient directional counts as

\[
E_a(B),\qquad E_b(B),\qquad E_c(B),
\]

and

\[
E_2(B)=E_a(B)+E_b(B)+E_c(B).
\]

These are control-population counts, not the main Stage14 `N_q^(2)` counts.

---

## 2. Oriented primitive face data and minimal gluing

Let

\[
F_i=(S_i,X_i,H_i),\qquad S_i^2+X_i^2=H_i^2,
\]

be oriented primitive Pythagorean face data, where `S_i` is the leg designated to become the shared edge. Thus

\[
\gcd(S_i,X_i)=\gcd(S_i,H_i)=\gcd(X_i,H_i)=1.
\]

For two data `F_1,F_2`, set

\[
g=(S_1,S_2),\qquad \alpha=S_1/g,\qquad \beta=S_2/g.
\]

The common-edge scale equation

\[
k_1S_1=k_2S_2
\]

has the complete positive solution

\[
k_1=t\beta,\qquad k_2=t\alpha.
\]

Therefore the glued edges are

\[
e=tg\alpha\beta,\qquad x=t\beta X_1,\qquad y=t\alpha X_2.
\]

Exactly as in Stage14-4ab, the minimal triple

\[
e_0=g\alpha\beta,\qquad x_0=\beta X_1,\qquad y_0=\alpha X_2
\]

satisfies

\[
\gcd(e_0,x_0,y_0)=1.
\]

Hence

\[
\boxed{\gcd(e,x,y)=t}.
\]

Primitive ambient objects force

\[
\boxed{t=1}.
\]

Crucially, this proof never uses a rational or integral space diagonal. Therefore after deleting the main Stage14 square condition the same exact minimal gluing survives:

\[
\boxed{
\begin{aligned}
e&=\operatorname{lcm}(S_1,S_2)=g\alpha\beta,\\
x&=\beta X_1,\\
y&=\alpha X_2.
\end{aligned}}
\]

With the convention `x<y`, a fixed raw ambient incidence has parameter-fiber multiplicity exactly one.

---

## 3. Rational-slope height identity

Define

\[
t_1=X_1/S_1,\qquad t_2=X_2/S_2,
\]

and

\[
L=\operatorname{lcm}(S_1,S_2).
\]

Since

\[
x=L t_1,\qquad y=L t_2,\qquad e=L,
\]

we obtain the exact vector identity

\[
\boxed{(e,x,y)=L(1,t_1,t_2)}.
\]

Therefore

\[
\boxed{
D_{\mathbf R}
=L\sqrt{1+t_1^2+t_2^2}.
}
\]

This height formula is common to all three directions. The direction label is only one of

```text
a: 1<t1<t2
b: t1<1<t2
c: t1<t2<1.
```

The main Stage14 integer-space-diagonal filter is now visibly the extra rational-square condition

\[
1+t_1^2+t_2^2\in(\mathbf Q^\times)^2.
\]

Stage14-e intentionally does not impose it.

---

## 4. Two independent finite enumerators

The deterministic audit implements two materially different routes.

### Route A — edge first

Enumerate primitive positive edge triples `(e,x,y)` under the real height, test

\[
e^2+x^2=\square,\qquad e^2+y^2=\square,
\]

and classify by the position of `e`.

### Route B — face pair first

Enumerate oriented primitive Pythagorean face data, glue them by the exact lcm formula above, normalize the order by `x<y`, and apply the same real-height cutoff.

These routes have different production logic. Equality of their resulting object sets is therefore a nontrivial audit of the ambient bijection.

---

## 5. Finite audit

For every audited cutoff through `B=2000`, the two routes produce exactly the same set of primitive raw ambient incidences, and the face-pair route has maximum fiber multiplicity one.

```text
B       raw total   exactly-two total    (Ea,Eb,Ec) exactly-two   third-face-square incidences
50             16                  16      (3,10,3)                  0
100            56                  56      (12,29,15)                0
200           172                 172      (39,75,58)                0
500           695                 689      (170,323,196)             6
1000         1853                1838      (500,833,505)            15
2000         4833                4812      (1342,2136,1334)         21
```

At `B=2000`, the raw directional vector is

\[
(1349,2143,1341),
\]

while excluding the third-face-square incidences gives

\[
\boxed{(E_a,E_b,E_c)=(1342,2136,1334)}.
\]

The audit also records seven distinct ambient Euler-brick objects by `B=2000`; each contributes three shared-edge raw incidences, giving the 21 third-face-square incidences above.

These finite values are diagnostics only. No growth exponent, asymptotic constant or limiting direction vector is inferred in Stage14-e1.

Canonical audit artifacts:

```text
stages/stage14/scripts/14-e1/ambient_audit.py
stages/stage14/data/14-e1/ambient_audit.json
```

---

## 6. Literature collision policy

Because this control population sits near rational-cuboid, Euler-brick and nearly-perfect-cuboid research, Stage14-e adopts a literature-first rule.

The initial verified seed is

```text
stages/stage14/14-e1/literature-seed.md
```

and currently covers classical rational cuboids, algebraic-surface treatments, nearly-perfect/rational parametrizations, recent search algorithms, and 2026 quartic/elliptic Euler-brick work.

The initial search status is

```text
NO_EXACT_COLLISION_FOUND_IN_CURRENT_SEARCH
```

for the specific target

```text
primitive shared-edge two-face ambient family
+ no rational/integer space-diagonal condition
+ real Euclidean height cutoff
+ total and directionwise asymptotic counting
```

This wording is intentionally weaker than a novelty claim. Before any later e-track theorem is promoted, the search must be refreshed and the nearest prior result classified as exact collision, adjacent result, reusable method, or no collision found in the current search.

---

## 7. Stage14-e1 decision

Stage14-e1 establishes the control population and the coordinate system needed for a genuinely different front-side attack.

```text
STAGE14_E1=COMPLETE_DEFINITION_BIJECTION_AND_FINITE_AUDIT
ROADMAP_CREATED_BEFORE_E1_IMPLEMENTATION=true
INTEGER_SPACE_DIAGONAL_CONDITION_REMOVED=true
REAL_SPACE_DIAGONAL_HEIGHT_ONLY=true
TWO_FACE_MINIMAL_GLUING_BIJECTION=true
FACE_PAIR_FIBER_MULTIPLICITY_ONE=true
EDGE_FIRST_FACE_PAIR_FIRST_SET_EQUALITY=true
FINITE_AUDIT_MAX_B=2000
ASYMPTOTIC_CLAIM_MADE=false
LITERATURE_COLLISION_AUDIT_REQUIRED=true
INITIAL_LITERATURE_SEED_CREATED=true
NOVELTY_BY_SEARCH_ABSENCE=false
NEXT_E_TASK=Stage14-e2 finite ambient reconnaissance plus refreshed literature audit
```
