# Stage14-t25 — odd local minimality and partial large-prime routing on the rank branch

## Purpose

Stage14-t24 closed the torsion energy and reduced the remaining t-track obstruction to

\[
Q_{\rm rank}(B)=\sum_{\alpha,\beta}\left(A^{\rm rank}_{\alpha,\beta}(B)\right)^2.
\]

Every rank-active reduced direction carries a physical non-torsion point on the explicit `[-1]` 2-cover of

\[
E_{D,C}:Y^2=X\left(X^2+(4D^2-2C^2)X+C^4\right),
\]

with

\[
D-C=h\alpha r^2,\qquad D+C=h\beta u^2.
\]

The q3 literature pass identified Pierre Le Boudec's 2018 congruent-number argument as the preferred transfer architecture: isolate a large prime factor, force it through a complete 2-descent, impose the physical height window, then count the surviving covering configurations.

Stage14-t25 performs the first exact transfer test on the t24 cover. It proves the odd local minimal-discriminant/conductor statement, derives two exact sum-of-two-squares identities, and shows precisely which large primes are already forced into the covering variables.

The transfer is useful but incomplete: the elementary rational cover routes the `3 mod 4` part of `ru`, while the remaining `1 mod 4` and `C` columns require Gaussian and dual-isogeny bookkeeping. Therefore t25 does **not** claim the rank second-moment power saving.

## 1. Odd local minimality of the integral 4-torsion model

Write

\[
A=4D^2-2C^2.
\]

For

\[
E_{D,C}:Y^2=X^3+AX^2+C^4X,
\]

the standard invariants give

\[
\boxed{c_4=16(16D^4-16D^2C^2+C^4)}
\]

and

\[
\boxed{\Delta=256C^8D^2(D^2-C^2)}.
\]

Let `ell` be an odd prime dividing `C D(D^2-C^2)`. Since `(D,C)=1`, the reduction of `c4/16` is:

- if `ell|C`, then `16D^4`;
- if `ell|D`, then `C^4`;
- if `ell|(D^2-C^2)`, then again `C^4`.

Each is nonzero modulo `ell`. Hence

\[
\boxed{v_\ell(c_4)=0}
\]

for every odd bad prime. The displayed integral model is therefore minimal at `ell`, and its reduction is multiplicative. Consequently

\[
\boxed{
N_{\rm odd}=\operatorname{rad}\!\left(CD(D^2-C^2)\right).
}
\]

Moreover

\[
v_\ell(\Delta_{\min})=
\begin{cases}
8v_\ell(C),&\ell|C,\\
2v_\ell(D),&\ell|D,\\
v_\ell(D^2-C^2),&\ell|(D^2-C^2).
\end{cases}
\]

The prime `2` is deliberately left unresolved in t25; no global conductor formula including its 2-adic exponent is asserted.

## 2. The physical `[-1]` cover in primitive variables

Write the physical Kummer parameter in lowest terms as

\[
z=-\left(\frac pq\right)^2,
\qquad p>q>0,
\qquad (p,q)=1.
\]

Clearing denominators in the t24 cover gives an integer `W` satisfying

\[
\boxed{
W^2=(4D^2-2C^2)p^2q^2-C^2(p^4+q^4).
}
\]

There are two exact rearrangements:

\[
\boxed{
W^2+C^2(p^2+q^2)^2=(2Dpq)^2
}
\tag{25.1}
\]

and

\[
\boxed{
W^2+C^2(p^2-q^2)^2=4(D^2-C^2)p^2q^2.
}
\tag{25.2}
\]

These are the local large-prime routing identities.

## 3. Odd prime divisors of `D` must split in `Q(i)`

Let `ell` be an odd prime divisor of `D`. Reducing (25.1) modulo `ell` gives

\[
W^2+C^2(p^2+q^2)^2\equiv0\pmod\ell.
\]

Because `ell` cannot divide `C`, if `ell=3 mod 4` then `-1` is a quadratic nonresidue and a sum of two squares can vanish only when both summands vanish. Thus

\[
p^2+q^2\equiv0\pmod\ell,
\]

which for `ell=3 mod 4` forces `ell|p,q`, contradicting `(p,q)=1`.

Therefore every physical rank-active direction satisfies

\[
\boxed{
ell|D,\ \ell\text{ odd}\Longrightarrow\ell\equiv1\pmod4.}
\]

This is a theorem-level arithmetic restriction on the active reduced directions, not merely a frozen-range observation.

## 4. `3 mod 4` primes in `D^2-C^2` are forced into `p^2-q^2`

Now let `ell=3 mod 4` divide `D^2-C^2`. Since the t20 kernel `alpha beta` contains only `2` and primes `1 mod 4`, every such `ell` comes from the square part `r^2u^2`. Hence

\[
v_\ell(D^2-C^2)=2v_\ell(ru).
\]

Apply the standard `ell=3 mod 4` valuation property to the sum of two squares in (25.2). Since `ell` divides neither `C` nor `pq`,

\[
v_\ell\left(W^2+C^2(p^2-q^2)^2\right)
=2\min\{v_\ell(W),v_\ell(p^2-q^2)\}.
\]

The right-hand side of (25.2) has valuation `2v_ell(ru)`. Therefore

\[
\boxed{
ell^{v_\ell(ru)}\mid W}
\]

and

\[
\boxed{
ell^{v_\ell(ru)}\mid p^2-q^2.}
\]

Since `(p,q)=1` and `ell` is odd, exactly one of `p-q` and `p+q` is divisible by `ell`. Define

\[
R_3(ru)=\prod_{\ell\equiv3(4)}\ell^{v_\ell(ru)}.
\]

Then every physical orientation satisfies the compact forcing law

\[
\boxed{
R_3(ru)\mid W,
\qquad
R_3(ru)\mid p^2-q^2.
}
\]

This is the exact Stage14 analogue of the first large-prime allocation step in the Le Boudec architecture.

## 5. What happens to `1 mod 4` large primes

For primes `ell=1 mod 4`, the previous integer argument cannot force both terms of a sum of squares to vanish. Instead the exact identities factor in the Gaussian integers:

\[
\boxed{
(W+iC(p^2+q^2))(W-iC(p^2+q^2))=(2Dpq)^2,
}
\]

\[
\boxed{
(W+iC(p^2-q^2))(W-iC(p^2-q^2))=4(D^2-C^2)p^2q^2.
}
\]

Thus a large split prime can still be routed, but only after its two Gaussian prime factors and the gcd of the conjugate factors are controlled. That allocation is not automatic from the rational cover alone.

The odd primes of `C` are even less visible in (25.1)--(25.2): modulo an odd prime of `C`, the cover only gives

\[
W^2\equiv(2Dpq)^2.
\]

So a complete four-column large-prime transfer requires the dual 2-isogeny/descent state in addition to the Gaussian allocation.

## 6. Exact transfer boundary

The q3 Le Boudec handoff asked for:

1. a usable large prime;
2. exact descent-state forcing;
3. physical-height constraints on the covering variables;
4. a count with fixed power saving.

Stage14-t25 completes items 1--2 only on the `3 mod 4` part of the square factors `r,u`.

For a fixed split partition `(alpha,beta)`, the remaining moving columns are

\[
r,\quad u,\quad C=\frac h2(\beta u^2-\alpha r^2),\quad D=\frac h2(\beta u^2+\alpha r^2).
\]

The current cover gives:

- `3 mod 4` prime in `D`: impossible;
- `3 mod 4` prime in `r,u`: forced into `p-q` or `p+q` with half the discriminant valuation;
- `1 mod 4` prime in `D,r,u`: Gaussian allocation still needed;
- odd prime in `C`: dual-isogeny routing still needed.

Therefore the direct Le Boudec transfer test is **partially successful but not yet a full power-saving theorem**.

## 7. Exact remaining rank pair count

For same-partition collision energy, a pair of rank-active directions is determined by

\[
(r_1,u_1),(r_2,u_2)
\]

with the same `(alpha,beta)`, together with primitive cover variables

\[
(p_j,q_j,W_j),\qquad j=1,2,
\]

satisfying

\[
W_j^2=(4D_j^2-2C_j^2)p_j^2q_j^2-C_j^2(p_j^4+q_j^4)
\]

and

\[
R_3(r_ju_j)\mid p_j^2-q_j^2.
\]

Hence `Q_rank` is now an explicit same-kernel pair count with a named large-prime divisor constraint. The missing theorem is a uniform power-saving count after completing the Gaussian/dual allocation.

## 8. Finite audit

The dedicated standard-library audit regenerates the exact Stage14 graph through `B=2,000,000` and verifies:

- all 356 frozen rank-active edges;
- all 712 physical orientations;
- odd local minimality at every odd prime in `C D(D^2-C^2)`;
- absence of odd `3 mod 4` prime divisors of `D`;
- the exact `R_3(ru)|W` and `R_3(ru)|(p^2-q^2)` forcing law;
- the two Gaussian norm identities.

The distribution of the `3 mod 4` part of `ru` is recorded only as finite diagnostic evidence. It is not promoted to an asymptotic statement.

## Boundary

```text
STAGE14_T25=COMPLETE_ODD_LOCAL_MINIMALITY_AND_PARTIAL_LARGE_PRIME_ROUTING
ODD_DISPLAYED_MODEL_MINIMAL_MULTIPLICATIVE=true
ODD_CONDUCTOR_RADICAL_EXPLICIT=true
ALL_ODD_D_PRIMES_1MOD4_ON_PHYSICAL_RANK_BRANCH=true
RU_3MOD4_PART_FORCED_INTO_P2_MINUS_Q2=true
LE_BOUDEC_LARGE_PRIME_TRANSFER_PARTIAL=true
LE_BOUDEC_TRANSFER_FULL_POWER_SAVING_PROVED=false
GAUSSIAN_OR_DUAL_DESCENT_REQUIRED=true
RANK_ACTIVE_SECOND_MOMENT_POWER_SAVING_PROVED=false
Q_ACTIVE_DIRECTION_POWER_SAVING_PROVED=false
Q_SPLIT_POWER_SAVING_PROVED=false
Q_EDGE_O_B_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t26 complete the large-prime routing: Gaussian gcd/allocation for 1 mod 4 primes and dual-isogeny descent for the C-column, then formulate the same-partition pair count
```

## References used for routing

- Pierre Le Boudec, *Height of rational points on congruent number elliptic curves*, 2018, arXiv:1802.07136. The imported ingredient is the proof architecture: restrict to integers with a large prime factor, then exploit that factor through complete 2-descent before counting small points.
- Stage14-q3 and q8 literature-routing records in this repository.
