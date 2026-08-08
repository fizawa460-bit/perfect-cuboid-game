# Stage14-t roadmap — triple-gate side track

## Purpose

Stage14-t is the dedicated side track for quantitative control of the triple/perfect-cuboid correction term in the Stage14 exactly-two-face problem. It is separate from the main `14-4` Kummer/rank-jump track and from the `14-e` ambient control track.

For the locked primitive canonical Stage14 population,

\[
\boxed{E(B)=N_2(B)+3T(B)},
\]

where `T(B)` counts objects with all three integral face diagonals.

## 14-t1 — baseline and theorem gap

Status: [x] Complete.

Locked: fixed physical genus-5 fiber, physical height `v asymp sqrt(Bg/S1)`, exact finite triple census `T(B)=0` through `B=2,000,000` with no nonexistence inference, and the literature boundary for uniform moving-family bounds.

## 14-t2 — quantitative moving-family attack

Status: [x] Complete as a quantitative boundary; square-root target remains open.

Every triple object gives a unique Pythagorean chain

```text
(b,c,z),  b^2+c^2=z^2,
(a,z,d),  a^2+z^2=d^2,
z<d<=B.
```

For

\[
P(z)=\prod_{p\equiv1(4)}(2e_p+1),
\qquad \tau(z^2)=\prod_p(2e_p+1),
\]

the two representation counts satisfy

\[
A(z)=\frac{P(z)-1}{2},\qquad
L(z)\le\frac{\tau(z^2)-1}{2}.
\]

Thus

\[
T(B)\le\frac14\sum_{z\le B}f(z),
\qquad f(z)=P(z)\tau(z^2).
\]

The multiplicative Dirichlet series factors as

\[
\sum f(n)n^{-s}=\zeta(s)^6L(s,\chi_4)^3G(s),
\]

with residual odd-prime factors

```text
p = 1 mod 4: (1+6x+x^2)(1-x)^6
p = 3 mod 4: (1-x^2)^4
```

and `G` absolutely convergent near `s=1`. Selberg--Delange therefore gives the independent Stage14-native envelope

\[
\boxed{T(B)=O(B(\log B)^5).}
\]

This is explicit but does not improve the frozen Stage13 R03 theorem

\[
\boxed{T(B)=o(B(\log B)^3)}.
\]

The moving genus-5 determinant/family route also does not currently yield `o(sqrt(B))`: coefficient height, physical fiber height, base summation and possible low-degree exceptional strata remain coupled.

```text
STAGE14_T2=COMPLETE_QUANTITATIVE_BOUNDARY
PYTHAGOREAN_CHAIN_INJECTION_LOCKED=true
CHAIN_ENVELOPE=T(B)=O(B(log B)^5)
CHAIN_ENVELOPE_IMPROVES_R03=false
FROZEN_STRONGEST_GLOBAL_BOUND=T(B)=o(B(log B)^3)
T_O_SQRT_B_PROVED=false
```

## 14-t3 — exceptional fibers and low-degree subfamilies

Status: [>] Next.

Classify degenerations, lower-genus quotients, extra automorphisms and low-degree subfamilies capable of accumulating triple points. The immediate goal is to determine whether the generic genus-5 family contains rational/elliptic subcovers or special Pythagorean base strata whose bounded-height points could dominate `T(B)`, and to count each such stratum under the physical height.

## 14-t4 — Kummer-cover comparison

Status: [ ] Pending t3 and relevant merged `14-4` descendants.

Compare the moving genus-5 formulation with the relative degree-two third-square cover of the Stage14 Kummer surface, especially on low-degree physical rational curves found by the main track.

## 14-t5 — transfer theorem

Status: [ ] Pending a sufficient triple bound and a main-track raw-pair law.

Combine `N2(B)=E(B)-3T(B)` with the strongest proved estimates. If `E(B)` has a `sqrt(B)` leading law and `T(B)=o(sqrt(B))`, transfer that law to the exactly-two population.

## Scope boundary

Stage14-t is a population-counting track, not a finite-search proof of nonexistence.

```text
STAGE14_T_TRACK=ACTIVE
STAGE14_T1=COMPLETE_BASELINE_AND_THEOREM_GAP
STAGE14_T2=COMPLETE_QUANTITATIVE_BOUNDARY
PRIMARY_TARGET=T(B)=o(sqrt(B))
NEXT=Stage14-t3 exceptional fibers and low-degree subfamilies
```
