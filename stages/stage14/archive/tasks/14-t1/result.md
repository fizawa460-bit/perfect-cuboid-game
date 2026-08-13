# Stage14-t1 — triple-gate baseline and theorem-gap closure

> STATUS: `STAGE14_T1_COMPLETE_BASELINE_AND_THEOREM_GAP`

Stage14-t1 isolates the triple/perfect-cuboid correction term before any quantitative attack.

## Locked counting interface

For primitive canonical Stage14 objects

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,\qquad a^2+b^2+c^2=d^2,\qquad d\le B,
\]

let `T(B)` count the objects for which all three face diagonals are integral. Then exactly

\[
\boxed{E(B)=N_2(B)+3T(B)}.
\]

Every triple object contributes to all three raw face-pair ledgers, hence the coefficient `3`.

## Fixed-base family

Fix the first Pythagorean face slope `t`. With the second-face rational-circle parameter `q`, the space-square and third-face-square conditions are

\[
W^2=q^4+2Aq^2+1,\qquad A=\frac{1-t^2}{1+t^2},
\]

and

\[
R^2=q^4+2Cq^2+1,\qquad C=\frac2{t^2}-1.
\]

The exact difference is

\[
\boxed{A-C=-\frac{2}{t^2(1+t^2)}}.
\]

For a genuine physical Pythagorean base, neither quartic has repeated roots and the two branch sets are disjoint. The connected `(Z/2)^2` fiber product is a degree-4 cover of `P^1_q` with eight simple branch values. Riemann--Hurwitz gives total ramification `16` and therefore

\[
\boxed{g=5}.
\]

The complex/projective exceptional base set is recorded as

```text
0, infinity, +1, -1, +i, -i.
```

A genuine positive primitive Pythagorean face does not hit these degeneracies: `t=0` is degenerate, `t=1` would require equal legs, and the remaining finite exceptional values are non-real.

## Physical height

For reduced `q=u/v`, `0<u<v`, the second primitive face has

\[
H_2=\frac{u^2+v^2}{\delta},\qquad \delta\in\{1,2\},
\]

so

\[
\frac{v^2}{2}<H_2<2v^2.
\]

The Stage14 physical cutoff satisfies the already-locked uniform sandwich

\[
\frac{S_1H_2}{\sqrt2\,g}<d<\frac{\sqrt3S_1H_2}{g},
\]

hence the moving-fiber denominator scale is

\[
\boxed{v\asymp\sqrt{Bg/S_1}}.
\]

This is the height interface t2 must preserve.

## Finite triple baseline

The frozen Stage14-2 audit used two materially different exact generation routes and checked all 11 cutoffs through

\[
B=2,000,000.
\]

They agree exactly, and

```text
T(B)=0
```

at every audited cutoff. In particular

```text
T(2,000,000)=0.
```

This is only a finite-range statement. It is **not** evidence sufficient to infer perfect-cuboid nonexistence or any asymptotic power saving.

## Literature boundary

The literature audit separates four levels:

- Faltings: fixed-fiber finiteness only;
- Browning--Heath-Brown--Salberger / Liu: unconditional determinant-method machinery potentially usable after a fixed-degree embedding and physical-height comparison are locked;
- Caporaso--Harris--Mazur: uniform fixed-genus cardinality belongs to a conditional Lang-type framework and is not imported;
- Peschmann 2026: directly adjacent perfect-cuboid quartic/genus-cover geometry, but no Stage14 bounded-height theorem for `T(B)`.

No determinant-method exponent is claimed in t1 because the required projective embedding, coefficient-height dependence, and moving-base summation have not yet been audited together.

## The exact remaining gap

The current unconditional chain is

```text
fixed physical Pythagorean base
-> smooth genus-5 fiber
-> finitely many rational triple points.
```

The missing step is a quantitative bound uniform enough in the moving base and compatible with the physical height to control the total sum over all bases.

The primary t2 target is

\[
T(B)=o(\sqrt B),
\]

with stronger target

\[
T(B)\ll B^{1/2-\delta+o(1)}
\]

for some `delta>0`.

```text
STAGE14_T1=COMPLETE_BASELINE_AND_THEOREM_GAP
TRIPLE_GATE_INTERFACE_LOCKED=true
TRIPLE_FIXED_BASE_GENUS=5
PHYSICAL_FIBERS_AVOID_GENERIC_DEGENERACY=true
FINITE_TRIPLE_CENSUS_MAX_B=2000000
FINITE_TRIPLE_COUNT_AT_MAX_B=0
FINITE_ZERO_IMPLIES_NONEXISTENCE=false
UNIFORM_MOVING_BASE_TRIPLE_BOUND_PROVED=false
T_O_SQRT_B_PROVED=false
NEXT=Stage14-t2 quantitative moving-family attack
```
