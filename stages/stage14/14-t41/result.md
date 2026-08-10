# Stage14-t41 — two-sided global squareclass incidence and the Kummer energy barrier

## Purpose

Stage14-t40 converted the external auxiliary variable, after one Cauchy step, into a genuine quadratic Dirichlet / norm-induced quadratic Hecke character.  What remained was no longer a character-theoretic obstruction but two global energies:

\[
A_1=\sum_\kappa r(\kappa)^2,
\qquad
E_4=\sum_D |A_D|^2.
\]

Stage14-t41 asks whether the two already-proved one-sided genus-one estimates can control these global quantities:

- t36: fixed direction, moving cover slope;
- t37: fixed cover slope, moving direction;
- t38: fixed descended packet, moving canonical Gaussian prime.

The answer is mixed.  These estimates explain almost all frozen principal collisions, but **two-sided local energy bounds do not logically imply a global near-linear energy bound**.  The genuine off-fiber collision locus is a two-dimensional Kummer-type surface, not another genus-one curve.  Likewise, even a hypothetical near-linear `A1` does not by itself imply the near-quadratic fourth energy required by t40.

Thus t41 identifies the next genuinely new input: a mixed transversality / squareclass-expansion theorem for the off-fiber Kummer incidences, preserving the canonical-prime and physical packet constraints.

No critical-strip, `A_{1,1}`, or `T=o(sqrt(B))` conclusion is claimed here.

## 1. Row and column energies already proved

For a fixed direction `d=(a,b)`, let `r_{d,kappa}` be the number of physical cover states in squareclass `kappa`.  Stage14-t36 gives

\[
\boxed{
\sum_\kappa r_{d,\kappa}^2\le J_d B^{o(1)}.
}
\tag{41.1}
\]

Summing over directions,

\[
\sum_d\sum_\kappa r_{d,\kappa}^2\le H B^{o(1)},
\tag{41.2}
\]

where `H` is the ambient number of states in the range under discussion.

In the reverse orientation, Stage14-t37 gives for each fixed cover state `v`

\[
\boxed{
\sum_\kappa r_{v,\kappa}^2\le K_v B^{o(1)}
}
\tag{41.3}
\]

and hence

\[
\sum_v\sum_\kappa r_{v,\kappa}^2\le H B^{o(1)}.
\tag{41.4}
\]

These are strong local incidence statements in both directions.

## 2. Why two-sided local energy is not enough

The global principal energy is

\[
A_1=\sum_\kappa\left(\sum_{d,v}1_{[F(d,v)]=\kappa}\right)^2.
\tag{41.5}
\]

Equations (41.2) and (41.4) do **not** imply `A1<=H B^{o(1)}`.

A purely combinatorial countermodel is a perfect matching with `H` edges, all carrying one common color.  Every row and every column contains one edge, so both row and column collision energies are exactly `H`; nevertheless the global color multiplicity is `H`, giving

\[
A_1=H^2.
\]

Therefore a new *mixed* incidence statement is necessary.  Reusing t36 and t37 separately cannot close t40.

## 3. Exact off-fiber geometry

Fix two descended t38 packets `gamma,gamma'`.  Their moving-prime squareclass factors can be represented by separable quartics

\[
f_\gamma(x),\qquad f_{\gamma'}(y),
\]

where `x,y` are the corresponding Gaussian-prime slope coordinates.

Equality of squareclasses is equivalent to the existence of `Y` such that

\[
\boxed{
Y^2=f_\gamma(x)f_{\gamma'}(y).
}
\tag{41.6}
\]

Introduce the two genus-one curves

\[
E_\gamma:\ u^2=f_\gamma(x),
\qquad
E_{\gamma'}:\ v^2=f_{\gamma'}(y).
\tag{41.7}
\]

Then

\[
(x,u;y,v)\longmapsto (x,y,Y=uv)
\]

identifies (41.6) birationally with the quotient

\[
\boxed{
(E_\gamma\times E_{\gamma'})/\{(u,v)\sim(-u,-v)\}.
}
\tag{41.8}
\]

After resolving the quotient singularities this is a Kummer-type surface.

This explains the exact logical boundary.  Freezing `y` gives the t36/t38 genus-one fiber; freezing `x` gives the reverse t37 genus-one fiber.  But with both variables moving the collision locus is a surface.  Bounded-height control on each elliptic fiber does not by itself imply a subpolynomial bound for all points on the surface.

## 4. Principal-energy decomposition

Write

\[
A_1=A_{\rm same\ direction}+A_{\rm off\ direction}.
\tag{41.9}
\]

The first term is already covered by t36 and is `H B^{o(1)}`.  The second term is the genuine Kummer-surface incidence term from (41.6).

The frozen `B=10000` audit is especially suggestive:

```text
H                                      1120
global A1                              2368
same-direction energy                  2240
off-direction ordered collisions        128
```

Thus only `128/2368` of the observed principal energy lies outside the already-understood direction fibers.  This is a diagnostic, not an asymptotic proof.

The audit further decomposes these 128 collisions by exact `F`, canonical `ell`, cover slope, common-core packet, descended packet, and Gaussian cofactor identities.  The generated JSON is the frozen source of truth for the exact counts.

## 5. Fourth energy is a separate expansion problem

Let `r(kappa)` denote global squareclass multiplicity and define the squareclass convolution

\[
c(t)=\sum_\kappa r(\kappa)r(\kappa t).
\tag{41.10}
\]

Then

\[
E_4=\sum_t c(t)^2,
\qquad
c(1)=A_1,
\qquad
\sum_t c(t)=H^2.
\tag{41.11}
\]

By Cauchy,

\[
c(t)\le A_1
\]

for every `t`.  Hence the universal bounds are

\[
\boxed{
A_1^2\le E_4\le A_1H^2.
}
\tag{41.12}
\]

The lower bound is just the principal cross-kernel contribution.  The upper bound shows why proving only

\[
A_1\le H B^{o(1)}
\]

would still be insufficient: it would give merely `E4<=H^3 B^{o(1)}`, whereas t40 needs substantially stronger nonprincipal squareclass expansion.

So t41 splits the remaining task into two genuinely distinct statements:

1. **principal transversality:** control off-fiber same-squareclass Kummer incidences;
2. **nonprincipal expansion:** show that the cross-kernel convolution is sufficiently flat to force near-quadratic fourth energy.

## 6. Frozen fourth-energy diagnostics

For the frozen 1120-state packet family, t40 gave

\[
A_1=2368,
\qquad
E_4=21,193,216.
\]

Therefore

\[
A_1/H\approx2.11,
\qquad
E_4/H^2\approx16.9.
\]

The principal contribution to `E4` is

\[
A_1^2=5,607,424,
\]

so most of the fourth energy is nonprincipal.  This confirms that the fourth-energy problem is not merely a restatement of the principal collision problem.

Again, these are finite diagnostics only.

## 7. What t42 must add

The next useful theorem cannot be another repetition of a one-variable elliptic bounded-height estimate.  It must exploit structure that couples the two fibrations.

The most promising split is:

- isolate packet pairs for which the two genus-one factors in (41.7) are isogenous or share an exceptional algebraic relation;
- prove a transverse bound for the generic non-isogenous packet pairs, using the canonical-largest-prime/common-core restrictions;
- simultaneously prove product-set expansion for the squareclass multiset so that nonprincipal `c(t)` cannot concentrate.

The frozen off-direction collisions provide the concrete exception list against which such a split can be audited.

## Locked boundary

```text
STAGE14_T41=COMPLETE_TWO_SIDED_INCIDENCE_AUDIT_AND_KUMMER_ENERGY_BARRIER
T36_ROW_ENERGY_REUSED=true
T37_REVERSE_COLUMN_ENERGY_REUSED=true
TWO_SIDED_LOCAL_ENERGY_IMPLIES_GLOBAL_NEAR_LINEAR=false
OFF_FIBER_COLLISION_SURFACE_KUMMER_TYPE=true
A1_DECOMPOSED_INTO_LOCAL_PLUS_OFF_FIBER=true
GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false
E4_LOWER_BOUND_A1_SQUARED=true
E4_UPPER_BOUND_A1_H_SQUARED=true
GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
CANONICAL_PRIME_SUM_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t42 isolate the off-direction Kummer incidence mechanism using canonical-prime/common-core constraints; split generic transverse packet pairs from exceptional/isogenous pairs and control nonprincipal squareclass convolution
```
