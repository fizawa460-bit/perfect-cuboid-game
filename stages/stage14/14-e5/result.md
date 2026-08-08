# Stage14-e5 — space-diagonal filter comparison

> STATUS: `STAGE14_E5_COMPLETE_SPACE_FILTER_COMPARISON`
>
> TRACK: front-side ambient control population versus main integer-space-diagonal Stage14 population
>
> INPUT: Stage14-e4 directional ambient theorem + frozen Stage13 R03 pair-overlap theorem + main Stage14-4af structural reduction
>
> IMPORTANT: this stage does **not** prove the true main Stage14 growth order and does **not** prove a main-track limiting direction vector.

## 1. Two populations on the same shared-edge geometry

Normalize a primitive two-face object by its shared edge `e`:

\[
(e,x,y)=L(1,t_1,t_2),
\qquad 0<t_1<t_2,
\]

with both `t_i` positive rational Pythagorean slopes.

The Stage14-e exactly-two ambient family requires

\[
1+t_1^2\in(\mathbf Q^\times)^2,
\qquad
1+t_2^2\in(\mathbf Q^\times)^2,
\]

and excludes

\[
t_1^2+t_2^2\in(\mathbf Q^\times)^2,
\]

but imposes no rationality/integrality condition on

\[
D_{\mathbf R}=L\sqrt{1+t_1^2+t_2^2}.
\]

The main Stage14 population is the subpopulation for which additionally

\[
\boxed{1+t_1^2+t_2^2\in(\mathbf Q^\times)^2,}
\]

which is equivalent, after primitive integral scaling, to an integer space diagonal.

Thus

\[
\boxed{N_q^{(2)}(B)\subset E_q(B)}
\]

for each shared-edge chamber `q=a,b,c`, and

\[
\boxed{N_2(B)\subset E_2(B).}
\]

The chamber dictionaries agree exactly:

```text
a: 1<t1<t2     shared smallest edge
b: t1<1<t2     shared middle edge
c: t1<t2<1     shared largest edge
```

## 2. Frozen ambient main terms

Stage14-e4 proves that there is one common positive arithmetic factor `Lambda_E` such that

\[
\boxed{
E_q(B)\sim \Lambda_E M_q B(\log B)^5,
\qquad q\in\{a,b,c\},
}
\]

where

\[
\begin{aligned}
M_a&=0.7295086229844189\ldots,\\
M_b&=0.6753521849589658\ldots,\\
M_c&=0.3139356465617057\ldots,
\end{aligned}
\]

and

\[
M=M_a+M_b+M_c=1.7187964545050902\ldots.
\]

Therefore

\[
\boxed{E_2(B)\sim\Lambda_E M B(\log B)^5.}
\]

The ambient direction vector is

\[
\boxed{
(p_a,p_b,p_c)=
(0.4244299091217717\ldots,
0.3929215604260869\ldots,
0.1826485304521414\ldots).
}
\]

## 3. The space-diagonal condition is geometrically thin

On the ambient torus, adding a rational space diagonal introduces the cover

\[
z^2=1+t_1^2+t_2^2.
\]

The function `1+t1^2+t2^2` is not a square in the geometric function field. After normalization/resolution this is a genuine generically degree-two cover, so the space-square locus is a Type-II thin subset of the ambient toric surface.

Consequently the general thin-set/equidistribution machinery already predicts zero leading density inside the `B(log B)^5` ambient family.

However Stage14 has a much sharper arithmetic input than this qualitative thinness statement.

## 4. R03 upgrades thinness by two full logarithmic powers

The frozen Stage13 R03 theorem gives every raw pair overlap

\[
O_{qr}(B)=o(B(\log B)^3),
\]

and

\[
T(B)=o(B(\log B)^3).
\]

The exactly-two main directions are

\[
N_a^{(2)}=O_{ab,ac}-T,
\]

\[
N_b^{(2)}=O_{ab,bc}-T,
\]

\[
N_c^{(2)}=O_{ac,bc}-T.
\]

Since all counts are nonnegative,

\[
0\le N_a^{(2)}\le O_{ab,ac},
\qquad
0\le N_b^{(2)}\le O_{ab,bc},
\qquad
0\le N_c^{(2)}\le O_{ac,bc}.
\]

Hence separately in every direction,

\[
\boxed{
N_q^{(2)}(B)=o(B(\log B)^3),
\qquad q=a,b,c.
}
\]

This directionwise conclusion is stronger than merely quoting the total relation

\[
N_2(B)=o(B(\log B)^3).
\]

## 5. Main comparison theorem: filter survival is `o(log^-2)`

Define the directionwise survival fractions

\[
S_q(B)=\frac{N_q^{(2)}(B)}{E_q(B)}.
\]

Using the positive e4 main terms,

\[
E_q(B)\sim \Lambda_E M_qB(\log B)^5,
\qquad M_q>0,
\]

and the R03 numerator bounds,

\[
N_q^{(2)}(B)=o(B(\log B)^3),
\]

we obtain

\[
\boxed{
S_q(B)=o((\log B)^{-2}),
\qquad q=a,b,c.
}
\]

Likewise, with

\[
S(B)=\frac{N_2(B)}{E_2(B)},
\]

we have

\[
\boxed{
S(B)=o((\log B)^{-2}).
}
\]

This is the first rigorous quantitative answer to the question for which the e-track was created:

> after two integral faces are already present, requiring the space diagonal to be integral selects a subset whose survival fraction is smaller than `1/(log B)^2` by a little-o factor, both globally and in each shared-edge chamber.

This does **not** identify the true main-track power of `B`. The finite `sqrt(B)` clue remains a clue only.

## 6. Exact decomposition of directional bias

Define the finite direction proportions

\[
p_q^E(B)=\frac{E_q(B)}{E_2(B)},
\qquad
p_q^N(B)=\frac{N_q^{(2)}(B)}{N_2(B)},
\]

when `N_2(B)>0`.

Then identically,

\[
\boxed{
p_q^N(B)=p_q^E(B)\frac{S_q(B)}{S(B)}.
}
\]

This separates the problem into two pieces:

1. ambient geometry, already solved by e4:
   \[
   p_q^E(B)\to p_q;
   \]
2. space-filter bias:
   \[
   \frac{S_q(B)}{S(B)}.
   \]

Therefore the space-diagonal filter is asymptotically direction-neutral **if and only if**

\[
\boxed{
\frac{S_a(B)}{S(B)},
\frac{S_b(B)}{S(B)},
\frac{S_c(B)}{S(B)}\to1.
}
\]

Under that condition the main direction vector would equal the ambient vector

\[
(0.4244299091\ldots,
0.3929215604\ldots,
0.1826485305\ldots).
\]

No such neutrality theorem is currently proved.

More generally, if limits

\[
\beta_q=\lim_{B\to\infty}\frac{S_q(B)}{S(B)}
\]

exist, then any main direction limit must satisfy

\[
\boxed{p_q^N=p_q\beta_q,}
\qquad
\boxed{\sum_qp_q\beta_q=1.}
\]

This is the comparison contract that future main Stage14 stages can fill in without reopening e1--e4.

## 7. Main-track structural interpretation from Stage14-4af

The e-track ambient population is toric and abundant. The main space-square filter is not behaving like an independent coin flip.

Main Stage14-4af shows that after the actual Pythagorean base change the relevant elliptic K3 surface has geometric generic Mordell-Weil rank zero. Its rational torsion is exactly

\[
\mathbf Z/2\times\mathbf Z/4,
\]

and all rational torsion maps to the nonphysical boundary `q=+/-1`.

Therefore every physical main-track hit must occur on a **positive-rank specialization** and must contain a non-torsion point small enough for the physical cutoff

\[
v\ll\sqrt{Bg/S_1}.
\]

This explains why e5 does not model the filter as direction-neutral random square probability. The unresolved numerator is a moving-base small-point rank-jump problem with gcd/lcm coupling and R03 local restrictions.

The fixed-base triple/perfect-cuboid intersection has genus five, but Stage14-4af proves only fiberwise finiteness, not a uniform moving-base bound. e5 therefore makes no perfect-cuboid nonexistence claim.

## 8. Finite same-cutoff diagnostic — not an asymptotic input

At `B=10,000`, the exact main Stage14 audit gives

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(9,11,5),
\qquad N_2=25.
\]

The exact ambient e2 census at the same cutoff gives

\[
(E_a,E_b,E_c)=(12{,}464,18{,}198,11{,}004),
\qquad E_2=41{,}666.
\]

Thus the finite survival fractions are

\[
\begin{aligned}
S_a(10^4)&=0.0007220795892\ldots,\\
S_b(10^4)&=0.0006044620288\ldots,\\
S_c(10^4)&=0.0004543802254\ldots,\\
S(10^4)&=0.0006000096002\ldots.
\end{aligned}
\]

The corresponding finite bias factors `S_q/S` are approximately

\[
(1.20345,1.00742,0.75729).
\]

These values use only 25 main-track objects and are **not** evidence for limiting bias.

At the larger frozen main cutoff `B=2,000,000`, the main finite direction vector is

\[
\frac1{356}(142,134,80)
=(0.3988764\ldots,0.3764045\ldots,0.2247191\ldots).
\]

It is visually closer to the ambient theoretical vector than the tiny `B=10^4` sample, but this remains finite evidence only. No direction-neutrality inference is authorized.

## 9. Literature boundary

The e5 literature refresh records:

```text
PESCHMANN_2026_SPACE_BLOCKERS=ADJACENT_RESULT_PLUS_REUSABLE_METHOD
ELLIPTIC_K3_RANK_JUMP_LITERATURE=ADJACENT_RESULT_PLUS_REUSABLE_CONTEXT
AMBIENT_TORIC_HEIGHT_THEOREMS=REUSABLE_METHOD_THEOREM_INPUT
DIRECT_STAGE14_E5_FILTER_SURVIVAL_THEOREM=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
DIRECT_STAGE14_E5_DIRECTION_BIAS_THEOREM=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
NOVELTY_BY_SEARCH_ABSENCE=false
```

The `o(log^-2)` comparison is not a new general theorem about thin sets; it is a direct consequence of the repository's frozen e4 denominator theorem and R03 numerator theorem.

## 10. What e5 closes and what remains open

Stage14-e was created as a control population with the space-diagonal condition removed. That control experiment is now complete:

- e1 defined and bijected the ambient family;
- e2 measured it finitely;
- e3 identified its true `B(log B)^5` order;
- e4 proved its directionwise main terms;
- e5 quantifies how strongly the main space-square filter thins it and isolates the remaining directional-bias variable.

The e-track does **not** need to invent a main-track exponent. That remains Stage14-4's job.

Current lock:

```text
STAGE14_E5=COMPLETE_SPACE_FILTER_COMPARISON
AMBIENT_MAIN_TERM=B_LOG5
MAIN_STAGE14_IMPORTED_UPPER_SCALE=o(B_LOG3)
TOTAL_SPACE_FILTER_SURVIVAL=o(LOG^-2)
DIRECTIONWISE_SPACE_FILTER_SURVIVAL=o(LOG^-2)
SPACE_SQUARE_LOCUS=THIN_TYPE_II
DIRECTION_NEUTRALITY_PROVED=false
MAIN_TRUE_GROWTH_ORDER_PROVED=false
MAIN_DIRECTION_LIMIT_PROVED=false
E_TRACK_CONTROL_EXPERIMENT=COMPLETE
NEXT_E_ACTION=WAIT_FOR_MAIN_STAGE14_QUANTITATIVE_GROWTH_OR_DIRECTION_RESULT
```
