# Stage14-t42 — reciprocal quotient and twisted-Kummer energy reduction

## Purpose

Stage14-t41 identified the global obstruction left after the one-variable genus-one estimates:

\[
A_1=\sum_\kappa r(\kappa)^2
\]

contains genuine off-direction Kummer incidences, while the fourth squareclass energy

\[
E_4=\sum_\tau c(\tau)^2
\]

also contains a large nonprincipal contribution.  Stage14-t42 makes two reductions.

1. It quotients the universal reciprocal symmetry `(p,q)<->(q,p)` before measuring the global energies.
2. It puts the principal and nonprincipal energies into one family of twisted Kummer surfaces and derives a sharper exact energy inequality.

The resulting analytic target is substantially narrower: after the reciprocal quotient it is enough to prove a near-linear aggregate bound for the principal off-direction incidence and a subpolynomial multiplicity bound for every fixed nonprincipal twist.

No such global transversality theorem is proved in t42.  Consequently no critical-strip, `A_{1,1}`, or `T=o(sqrt(B))` conclusion is claimed.

## 1. Exact reciprocal quotient

For the Stage14 quartic

\[
F_{a,b}(p,q)
=(b^2p^2-a^2q^2)(b^2q^2-a^2p^2),
\]

one has the exact symmetry

\[
\boxed{F_{a,b}(p,q)=F_{a,b}(q,p).}
\tag{42.1}
\]

The physical population used since t36 contains both orientations whenever `p!=q`.  Hence one may quotient by the involution

\[
(p,q)\longleftrightarrow(q,p)
\]

at bounded cost.  Write the quotient population as `S*` and its size as `H*`.

For the frozen `B=10000`, `a,b,p,q<=40` family, every orbit has exactly two states.  Therefore the frozen energies scale exactly as

\[
\boxed{
H=2H_*,\qquad A_1=4A_{1,*},\qquad E_4=16E_{4,*}.
}
\tag{42.2}
\]

This normalization removes the 560 reciprocal collisions which t36 had already classified completely.

## 2. Principal energy after quotient

The quotient contains

```text
H*                                  560
distinct squareclasses              544
multiplicity 1 squareclasses        528
multiplicity 2 squareclasses         16
A1*                                 592
A1* - H*                             32
```

Thus the entire non-diagonal principal excess is exactly

\[
\boxed{A_{1,*}-H_*=32=2\cdot16.}
\tag{42.3}
\]

Equivalently, the 128 ordered off-direction collisions found in t41 are exactly 16 unordered collision blocks after removing the two reciprocal orientations on each endpoint.

This is useful because the principal problem is no longer obscured by a universal symmetry: asymptotically the quantity that needs a new theorem is the number of genuinely off-direction edges in this quotient incidence graph.

## 3. Frozen transversality diagnostics

The 16 collision blocks are sparse on the direction side:

```text
distinct direction vertices          25
direction max degree                   2
degree 1 vertices                     18
degree 2 vertices                      7
```

The cover-side graph is less sparse:

```text
distinct cover vertices               13
cover max degree                        7
```

The packet coincidences among the 16 blocks are

```text
same Gaussian U orbit                   8
same Gaussian V orbit                   3
same visible/invisible branch          14
same common-core packet                 2
same unordered cover                    3
same canonical ell                      2
same exact F                            1
```

Hence most blocks are not repetitions inside one already-controlled t37/t38 packet.

These numbers are finite diagnostics only; bounded degree at the frozen cutoff is not an asymptotic theorem.

## 4. The simplest isomorphism exception is absent in the frozen blocks

For a fixed direction `(a,b)`, the t36 quartic has branch divisor

\[
\left\{\pm\frac ab,\ \pm\frac ba\right\}.
\]

A cross-ratio representative is

\[
\boxed{
\lambda_{a,b}
=\left(\frac{b^2-a^2}{b^2+a^2}\right)^2,
\qquad 0<\lambda_{a,b}<1.
}
\tag{42.4}
\]

The six cross-ratios in the `S_3` orbit are

\[
\lambda,\quad 1-\lambda,\quad \lambda^{-1},\quad
(1-\lambda)^{-1},\quad \frac{\lambda}{\lambda-1},\quad
\frac{\lambda-1}{\lambda}.
\]

When both representatives lie in `(0,1)`, equality of the unordered branch-divisor moduli reduces to

\[
\lambda'=\lambda
\quad\hbox{or}\quad
\lambda'=1-\lambda.
\tag{42.5}
\]

The audit checks this exactly with rational arithmetic.  Among the 16 frozen off-direction principal blocks,

\[
\boxed{
\#\{\text{PGL}_2\text{-equivalent t36 direction branch divisors}\}=0.
}
\tag{42.6}
\]

Therefore none of the observed blocks is explained by the most elementary mechanism in which the two t36 quartics have identical branch moduli.

This statement is deliberately narrow.  It does **not** prove that the more general descended t38 elliptic factors are never isogenous, nor does it classify all algebraic correspondences between packet curves.

## 5. Twisted Kummer unification

Let `gamma,gamma'` denote two packet/fiber labels and let their one-variable squareclass forms be represented by separable quartics

\[
f_\gamma(x),\qquad f_{\gamma'}(y).
\]

For a squareclass `tau`, consider

\[
\boxed{
K^{(\tau)}_{\gamma,\gamma'}:
Y^2=\tau f_\gamma(x)f_{\gamma'}(y).
}
\tag{42.7}
\]

As in t41, after passing to the two genus-one double covers this is a quadratic twist of the corresponding Kummer-type quotient.

The important point is that both global energies now have the same geometric source:

- `tau=1` gives same-squareclass collisions; after removing the reciprocal diagonal, its off-direction points are the principal incidence problem;
- `tau!=1` gives cross-squareclass pairs whose product squareclass is exactly `tau`.

Thus the principal and nonprincipal problems are not unrelated analytic leftovers.  They are two regimes of the same twisted-Kummer incidence family.

## 6. Exact refined fourth-energy inequality

On the reciprocal quotient let

\[
r(\kappa)=\#\{s:[F_s]=\kappa\}
\]

and define

\[
\boxed{
c(\tau)=\sum_\kappa r(\kappa)r(\kappa\tau).}
\tag{42.8}
\]

Equivalently, because the squareclass group has exponent two,

\[
c(\tau)
=\#\{(s,t):[F_sF_t]=\tau\}.
\tag{42.9}
\]

Then

\[
\sum_\tau c(\tau)=H^2,
\qquad
c(1)=A_1,
\tag{42.10}
\]

and

\[
\boxed{
E_4=A_1^2+\sum_{\tau\ne1}c(\tau)^2.
}
\tag{42.11}
\]

Put

\[
C_{\rm non}=\max_{\tau\ne1}c(\tau).
\]

Since

\[
\sum_{\tau\ne1}c(\tau)=H^2-A_1,
\]

we obtain the exact refinement

\[
\boxed{
E_4
\le
A_1^2+C_{\rm non}(H^2-A_1).
}
\tag{42.12}
\]

This is much sharper as an analytic interface than the t41 universal bound

\[
E_4\le A_1H^2.
\]

In particular, the following pair of estimates is sufficient:

\[
\boxed{
A_1\le H B^{o(1)},
\qquad
C_{\rm non}\le B^{o(1)}.
}
\tag{42.13}
\]

Indeed (42.12) then gives

\[
\boxed{E_4\le H^2B^{o(1)}.}
\tag{42.14}
\]

So one does not need to prove a fourth-moment theorem directly.  It suffices to control the principal twist in aggregate and every nonprincipal twist pointwise in its squareclass parameter.

## 7. Frozen nonprincipal expansion

On the 560-orbit frozen quotient,

```text
A1*                                 592
E4*                           1,324,576
principal contribution          350,464
nonprincipal contribution        974,112
max nonprincipal c(tau)               40
```

The most populated nonprincipal twists begin

```text
tau       c(tau)
91             40
209            38
286            34
34034          34
41             32
329            32
4641           32
11             30
```

The crude t41-style upper bound on the quotient is

\[
A_1H^2=185,651,200,
\]

whereas the observed fourth energy is only about `0.713%` of it.  Using only the observed `C_non=40`, (42.12) already improves the deterministic upper bound to

\[
12,870,784.
\]

Again, these are diagnostics rather than asymptotics; `C_non=40` at one cutoff is not a proof of `B^{o(1)}` multiplicity.

## 8. Exact remaining theorem

After t42 the missing input can be stated as one transversality theorem for (42.7), with different treatment of the principal diagonal.

### Principal twist

After quotienting the reciprocal symmetry, prove that the aggregate number of genuinely off-direction `tau=1` incidences is

\[
\ll H B^{o(1)}.
\]

Together with t36's already-controlled local direction fibers, this gives

\[
A_1\le H B^{o(1)}.
\]

### Nonprincipal twists

Uniformly for every `tau!=1`, prove

\[
\boxed{c(\tau)\le B^{o(1)}}
\]

after retaining the canonical-largest-prime, common-core, physical reconstruction, and branch/local-state restrictions.

The frozen branch-moduli audit suggests that the generic packet pairs are transverse rather than identical elliptic fibrations.  A proof must nevertheless isolate all exceptional low-degree correspondences or isogeny-type packet relations instead of assuming genericity.

This is the task passed to t43.

## Locked boundary

```text
STAGE14_T42=COMPLETE_RECIPROCAL_QUOTIENT_AND_TWISTED_KUMMER_ENERGY_REDUCTION
RECIPROCAL_DOUBLE_COVER_QUOTIENTED=true
FROZEN_RECIPROCAL_ORBITS=560
FROZEN_OFF_DIRECTION_PRINCIPAL_BLOCKS=16
FROZEN_DIRECTION_COLLISION_GRAPH_MAX_DEGREE=2
FROZEN_DIRECTION_BRANCH_PGL2_EQUIVALENT_BLOCKS=0
PRINCIPAL_AND_NONPRINCIPAL_UNIFIED_BY_TWISTED_KUMMER=true
REFINED_E4_BOUND=A1^2+C_non*(H^2-A1)
A1_NEAR_LINEAR_PLUS_CNON_SUBPOLY_IMPLIES_E4_NEAR_QUADRATIC=true
OFF_DIRECTION_PRINCIPAL_AGGREGATE_BOUND_PROVED=false
NONPRINCIPAL_TWIST_MULTIPLICITY_SUBPOLY_PROVED=false
GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false
GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
CANONICAL_PRIME_SUM_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t43 prove canonical-prime/common-core transversality for K^(tau): near-linear aggregate off-direction incidence for tau=1 after reciprocal quotient, and B^o(1) multiplicity for every tau!=1; isolate exceptional low-degree correspondences separately
```
