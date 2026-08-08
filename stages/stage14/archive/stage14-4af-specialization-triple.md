# Stage14-4af — Pythagorean-base specialization and triple-subtraction geometry

## Purpose

Stage14-4ae showed that the raw-pair problem is controlled by rational points on

\[
E_t:\quad Y^2=X(X-1)(X+t^2),
\]

with a physical second-face parameter `q=u/v` whose natural cutoff is

\[
v\asymp\sqrt{Bg/S_1}.
\]

It also proved geometric generic Mordell--Weil rank zero over the full `t`-line. Stage14, however, samples only **Pythagorean** base values `t=X_1/S_1`, and exactly-two requires removing the triple-face locus. Stage14-4af closes those two structural gaps.

The conclusions are:

1. the Pythagorean degree-two base change is a K3 elliptic surface whose geometric generic Mordell--Weil rank is still `0`;
2. on every genuine Pythagorean base, the rational torsion is exactly `Z/2 x Z/4`;
3. every rational 4-torsion point maps to the degenerate boundary `q=+/-1`, and no rational 8-torsion exists;
4. therefore every **physical** Stage14 raw-pair point is non-torsion and forces a positive-rank specialization;
5. for each fixed first face, imposing the third integral face produces a smooth genus-5 fiber product, hence only finitely many rational triple points on that fixed base;
6. neither the rank-jump frequency nor a uniform genus-5 rational-point bound is yet available, so the true growth order and `T=o(sqrt(B))` remain open.

No `sqrt(B)` asymptotic is claimed here.

---

## 1. Pythagorean restriction is a nontrivial base change

A genuine first face satisfies

\[
S_1^2+X_1^2=H_1^2.
\]

Put

\[
t=\frac{X_1}{S_1},\qquad h=\frac{H_1}{S_1},
\]

so

\[
h^2=1+t^2.
\]

The rational Pythagorean base can be parametrized by

\[
u=\frac{X_1}{H_1+S_1}\in\mathbf Q,
\]

with

\[
\boxed{
 t=\frac{2u}{1-u^2},
 \qquad
 h=\frac{1+u^2}{1-u^2}.
}
\]

Thus Stage14 does not sample arbitrary rational `t`; it samples a degree-two base change of the elliptic surface from Stage14-4ae.

This matters because generic rank zero on the `t`-line does not automatically imply generic rank zero after a finite base change. Stage14-4af checks that issue explicitly.

---

## 2. The Pythagorean pullback is a K3 surface with generic rank zero

The Stage14-4ae elliptic surface has geometric singular fibers

```text
t=0        I4
t=+i       I2
t=-i       I2
t=infinity I4
```

under

\[
t=\frac{2u}{1-u^2}.
\]

The map has degree `2` and branches over `t=+/-i`. Therefore:

- the `I4` fiber at `t=0` has two unramified preimages `u=0,infinity`;
- the `I4` fiber at `t=infinity` has two unramified preimages `u=+1,-1`;
- each ramified `I2` fiber at `t=+i,-i` pulls back to `I4` at `u=+i,-i`.

Hence the Pythagorean-base elliptic surface has

\[
\boxed{I_4^6}
\]

as its geometric singular-fiber configuration.

The Euler number is

\[
6\cdot4=24,
\]

so the pullback is an elliptic K3 surface.

The trivial lattice has rank

\[
2+6(4-1)=20.
\]

A K3 surface has geometric Picard rank at most `20`. Since the trivial lattice already has rank `20`, the Neron--Severi rank is exactly `20`, and Shioda--Tate gives

\[
\boxed{
\operatorname{rank}E(\overline{\mathbf Q}(u))
=20-2-18=0.
}
\]

Thus the generic-rank-zero conclusion survives the **actual Pythagorean base restriction** used by Stage14.

There is no hidden non-torsion section that appears merely because the first face was constrained to be Pythagorean.

---

## 3. Rational torsion on a genuine Pythagorean fiber

Fix a genuine Pythagorean base. Then

\[
E_t:\quad Y^2=X(X-1)(X+t^2)
\]

has rational full 2-torsion

\[
(0,0),\qquad(1,0),\qquad(-t^2,0).
\]

Because

\[
h^2=1+t^2
\]

is rational, `(1,0)` has rational halves. Explicitly the points with

\[
X=1\pm h
\]

and the corresponding signs of `Y` have exact order `4`.

The Stage14-4ae inverse coordinate is

\[
q=\frac{X}{sY},
\qquad s=\frac{S_1}{H_1}=\frac1h.
\]

For the order-4 points this gives

\[
\boxed{q=+1\text{ or }q=-1.}
\]

These are precisely the degenerate rational-circle boundary charts with `S_2=0`. They are not physical Stage14 second faces, which require

\[
0<q<1.
\]

So the rational 4-torsion contributes no genuine raw-pair incidence.

---

## 4. No rational 8-torsion on a genuine Pythagorean base

The curve already contains `Z/2 x Z/4`. By Mazur's torsion theorem, the only possible larger rational torsion group containing it is `Z/2 x Z/8`.

An order-8 point would halve one of the rational order-4 points. For the positive half of `(1,0)`, the standard 2-divisibility criterion on a full-2-torsion curve forces both

\[
h
\quad\text{and}\quad
h+1
\]

to be rational squares. Since

\[
t^2=(h-1)(h+1)
\]

is already a square, this would also force `h-1` to be a rational square. Hence

\[
h-1,\quad h,\quad h+1
\]

would be three rational squares in arithmetic progression with common difference `1`.

That is equivalent to a rational right triangle of area `1`, which is impossible by Fermat's right-triangle theorem (equivalently, `1` is not a congruent number).

The negative order-4 branch has negative `X=1-h`, so it cannot satisfy the rational square condition required for divisibility by `2`.

Therefore

\[
\boxed{
E_t(\mathbf Q)_{tors}\cong\mathbf Z/2\mathbf Z\times\mathbf Z/4\mathbf Z
}
\]

for every genuine Pythagorean base.

Consequently:

\[
\boxed{
\text{every physical Stage14 raw-pair point is non-torsion.}
}
\]

Since the Pythagorean-base generic rank is zero, every physical raw-pair incidence occurs on a genuine **positive-rank specialization**.

This removes the `extra torsion` alternative left open in Stage14-4ae.

---

## 5. What the raw-pair problem has become

The global raw-pair count is now a pure small-nontorsion-point specialization problem.

For the Pythagorean base parameter `u`, the generic Mordell--Weil rank is zero. A base value contributes only when the specialized fiber acquires positive rank and contains a non-torsion point whose physical `q`-height is sufficiently small:

\[
H(q)=v\ll\sqrt{Bg/S_1}.
\]

Thus the missing quantitative input is not simply an average rank theorem. It is a bound for the distribution of **rank-jump fibers with a first sufficiently small non-torsion point**, together with the gcd/lcm constraints.

In particular, root-number parity or positive-rank density alone would still be insufficient: a positive-rank fiber whose first non-torsion point is too high contributes nothing below the physical cutoff.

---

## 6. Triple condition as a second quartic

Exactly-two requires subtracting the triple population. Fix the first-face slope

\[
t=t_1.
\]

The integer-space-diagonal condition is the Stage14-4ad quartic

\[
\boxed{
W^2=q^4+2Aq^2+1,
\qquad
A=\frac{1-t^2}{1+t^2}.
}
\]

The third-face condition is

\[
t^2+t_2^2\in(\mathbf Q^\times)^2.
\]

Using

\[
t_2=\frac{2q}{1-q^2},
\]

this becomes another Jacobi quartic

\[
\boxed{
R^2=q^4+2Cq^2+1,
\qquad
C=\frac{2}{t^2}-1.
}
\]

For a genuine Pythagorean `t`, `t!=1`, and both quartics are nonsingular.

Moreover

\[
\boxed{
A-C=-\frac{2}{t^2(1+t^2)}\ne0.
}
\]

Thus their four simple branch points in the `q`-line are disjoint.

---

## 7. Fixed-base triple fiber has genus 5

Adjoin both square roots to `Q(q)`:

\[
W^2=q^4+2Aq^2+1,
\qquad
R^2=q^4+2Cq^2+1.
\]

Because the two branch sets are disjoint, the resulting connected fiber product is a degree-4 `(Z/2)^2` cover of `P^1_q` with eight branch points. Above each branch point there are two ramified points of index `2`, so the total ramification contribution is

\[
8\cdot2=16.
\]

Riemann--Hurwitz gives

\[
2g-2=4(-2)+16=8,
\]

hence

\[
\boxed{g=5.}
\]

Therefore the triple/perfect-cuboid locus on **each fixed first-face fiber** is a smooth genus-5 curve.

By Faltings' theorem, each such fixed genus-5 curve has only finitely many rational points.

This is a genuine strengthening of the triple gate: the triple set is not merely an elliptic subcondition on a fixed base; it is a higher-genus intersection.

However this is only fiberwise finiteness. Stage14 currently has no uniform rational-point bound as the first-face base varies. In particular, Stage14-4af does **not** prove

\[
T(B)=O(1),\qquad T(B)=o(\sqrt B),
\]

or perfect-cuboid nonexistence.

---

## 8. Deterministic finite audit

The Stage14-4af audit uses the exact face-pair bijection at `B=10000`.

It records

```text
oriented primitive face data        3186
raw pair incidences                   25
exactly-two direction              (9,11,5)
triple                                  0
distinct first-face fibers with hits  23
q-denominator range                  5..57
```

The 25 raw hits lie on 23 first-face fibers: two fibers contribute two hits and the other 21 contribute one each.

For every one of the 3,186 oriented first faces it verifies the Pythagorean base-change formulas and the rational 4-torsion boundary. For every physical raw hit it verifies `0<q<1` and checks that `8P` is not the identity.

The script and frozen JSON report are

```text
stages/stage14/scripts/14-4/specialization_triple_audit.py
stages/stage14/data/14-4/specialization_triple_audit.json
```

and the report is intended to regenerate exactly from the script.

The finite audit is validation only; it is not evidence for a limiting rank-jump density.

---

## 9. Literature boundary

Nearby arithmetic geometry exists and should be treated as reusable method rather than as a Stage14 theorem.

- Halbeisen--Hungerbuehler, *Pairing Pythagorean Pairs* (JNT 233, 2022) studies related full-2-torsion elliptic curves attached to Pythagorean pairs and connects positive rank with double-pythapotent conditions.
- Jonathan R. Love, *Root numbers of a family of elliptic curves and two applications* (Indagationes Mathematicae 35, 2024) studies the adjacent family `y^2=x(x+1)(x+t^2)` and products of rational-right-triangle slopes.

Neither result is imported as a rank-jump frequency theorem for the signed Stage14 family with its lcm/physical height.

```text
LITERATURE_STATUS=ADJACENT_RESULT_AND_REUSABLE_METHOD
NOVELTY_BY_SEARCH_ABSENCE=false
```

---

## 10. Stage14-4af decision

```text
STAGE14_4AF=COMPLETE

PYTHAGOREAN_BASE_CHANGE_K3=true
PYTHAGOREAN_BASE_FIBERS=I4_X6
PYTHAGOREAN_BASE_GENERIC_MW_RANK=0

TORSION_EXACT_Z2xZ4_ON_GENUINE_BASES=true
RATIONAL_4_TORSION_PHYSICAL=false
RATIONAL_8_TORSION_EXISTS=false
PHYSICAL_RAW_PAIR_IMPLIES_POSITIVE_RANK_SPECIALIZATION=true

TRIPLE_FIXED_BASE_GENUS=5
TRIPLE_FIXED_BASE_RATIONAL_POINTS_FINITE=true
UNIFORM_TRIPLE_POINT_BOUND_PROVED=false
T_O_SQRT_B_PROVED=false

SQRT_B_STRUCTURAL_HEIGHT_SOURCE_IDENTIFIED=true
SQRT_B_FINITE_CANDIDATE_SURVIVES=true
SQRT_B_ASYMPTOTIC_CLAIM=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
LEADING_CONSTANT_IDENTIFIED=false

NEXT=Stage14-4ag quantitative rank-jump/small-point counting with uniform triple control
```

The remaining growth-order problem is now sharply separated into two quantitative tasks:

1. count Pythagorean base specializations that acquire a sufficiently small non-torsion point;
2. control the moving genus-5 triple fibers strongly enough to transfer any raw-pair law to exactly-two.
