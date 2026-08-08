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

The exact representation-factor majorant has Dirichlet series

\[
\sum f(n)n^{-s}=\zeta(s)^6L(s,\chi_4)^3G(s),
\]

with `G` absolutely convergent near `s=1`, hence

\[
\boxed{T(B)=O(B(\log B)^5)}.
\]

This independent Stage14-native envelope does not improve the frozen Stage13 theorem

\[
\boxed{T(B)=o(B(\log B)^3)}.
\]

```text
STAGE14_T2=COMPLETE_QUANTITATIVE_BOUNDARY
CHAIN_ENVELOPE=T(B)=O(B(log B)^5)
CHAIN_ENVELOPE_IMPROVES_R03=false
FROZEN_STRONGEST_GLOBAL_BOUND=T(B)=o(B(log B)^3)
T_O_SQRT_B_PROVED=false
```

## 14-t3 — Humbert-Edge structure and low-degree classification

Status: [x] Complete.

Put `s=t^2`, `A=(1-s)/(1+s)`, `C=2/s-1`. After homogenizing `q=Q/P` and setting

\[
U_0=P^2+Q^2,\qquad U_1=P^2-Q^2,\qquad U_2=2PQ,
\]

the triple fiber is the smooth complete intersection of three diagonal quadrics

\[
U_0^2-U_1^2-U_2^2=0,
\]

\[
2W^2-U_0^2-U_1^2-AU_2^2=0,
\]

\[
2R^2-U_0^2-U_1^2-CU_2^2=0.
\]

Thus every genuine physical fiber is a Humbert--Edge curve of type `4`, hence genus `5`, with sign group `(Z/2Z)^4`.

The five branch values of the quotient orbifold are

\[
\boxed{\infty,0,1,-1/s,1/(1-s)}.
\]

The singular branch-collision values are only `s=0,1,-1,infinity`, none of which is a genuine physical rational Pythagorean base. An exact audit of all 120 branch permutations shows that the remaining possible extra-symmetry loci are roots of

```text
s^2+1,
s^2+s+1,
s^2-s+1,
s^2+s-1,
s^2-s-1,
```

and none has a rational root. Therefore the physical rational family has no singular, lower-genus, or enlarged-automorphism exceptional stratum.

More importantly, the low-degree structure is universal: quotienting by each of the five coordinate involutions gives a smooth genus-one curve, and the refined Humbert--Edge decomposition gives

\[
\boxed{
J(C_t)\sim_{\mathbf Q}E_{U_0,t}\times E_{U_1,t}\times E_{U_2,t}\times E_{W,t}\times E_{R,t}.
}
\]

Hence

\[
\boxed{
\operatorname{rank}J(C_t)(\mathbf Q)=\sum_{i=1}^{5}\operatorname{rank}E_{i,t}(\mathbf Q).
}
\]

The t2 moving genus-5 rank problem is therefore an explicit moving five-elliptic-factor problem. The universal elliptic structure is not a thin exceptional set and cannot be discarded.

```text
STAGE14_T3=COMPLETE_HUMBERT_EDGE_AND_ELLIPTIC_SPLITTING
TRIPLE_FIBER_HUMBERT_EDGE_TYPE4=true
TRIPLE_FIBER_JACOBIAN_COMPLETELY_ELLIPTIC=true
ELLIPTIC_FACTOR_COUNT=5
PHYSICAL_SINGULAR_EXCEPTIONAL_STRATUM_EMPTY=true
PHYSICAL_RATIONAL_EXTRA_AUTOMORPHISM_STRATUM_EMPTY=true
UNIVERSAL_LOW_DEGREE_STRUCTURE_NOT_THIN=true
T_O_SQRT_B_PROVED=false
```

## 14-t4 — elliptic-factor rank/torsion audit and Kummer-cover comparison

Status: [>] Next.

Convert the five quotient factors to canonical Weierstrass models over the Pythagorean base, determine their generic torsion and rank behavior, and make the lift conditions back to the genus-5 fiber explicit. In particular:

- identify which factors coincide with or are isogenous to the Stage14 space/Kummer elliptic fibers already studied in `14-4`;
- search for rank-zero factors or torsion-intersection criteria that eliminate whole base strata;
- compare with recent perfect-cuboid elliptic-quotient/torsion-intersection methods;
- quantify the remaining positive-rank base population under the physical height.

The goal remains a bound strong enough to approach

\[
T(B)=o(\sqrt B).
\]

## 14-t5 — transfer theorem

Status: [ ] Pending a sufficient triple bound and a main-track raw-pair law.

Combine `N2(B)=E(B)-3T(B)` with the strongest proved estimates. If `E(B)` has a `sqrt(B)` leading law and `T(B)=o(sqrt(B))`, transfer that law to the exactly-two population.

## Scope boundary

Stage14-t is a population-counting track, not a finite-search proof of nonexistence.

```text
STAGE14_T_TRACK=ACTIVE
STAGE14_T1=COMPLETE_BASELINE_AND_THEOREM_GAP
STAGE14_T2=COMPLETE_QUANTITATIVE_BOUNDARY
STAGE14_T3=COMPLETE_HUMBERT_EDGE_AND_ELLIPTIC_SPLITTING
PRIMARY_TARGET=T(B)=o(sqrt(B))
NEXT=Stage14-t4 elliptic-factor rank/torsion audit and Kummer-cover comparison
```
