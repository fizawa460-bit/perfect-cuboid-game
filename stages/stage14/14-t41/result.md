# Stage14-t41 — two-sided global squareclass incidence and the Kummer energy barrier

## Purpose

Stage14-t40 converted the external auxiliary variable, after one Cauchy step, into a genuine quadratic Dirichlet / norm-induced quadratic Hecke character. What remained was no longer a character-theoretic obstruction but two global energies:

\[
A_1=\sum_\kappa r(\kappa)^2,
\qquad
E_4=\sum_D |A_D|^2.
\]

Stage14-t41 tests whether the one-sided genus-one estimates already proved in t36--t38 control these global energies when both sides move.

The conclusion is precise:

- the row and reverse-column energies are both near-linear;
- nevertheless these two local statements do not logically imply global near-linear `A1`;
- the genuine off-fiber same-squareclass locus is a two-dimensional Kummer-type surface;
- `E4` has an independent nonprincipal expansion problem, even if `A1` were near-linear.

No critical-strip, `A_{1,1}`, or `T=o(sqrt(B))` conclusion is claimed in t41.

## 1. Row and column energies already proved

For fixed direction `d=(a,b)`, t36 gives

\[
\boxed{
\sum_\kappa r_{d,\kappa}^2\le J_d B^{o(1)}.
}
\tag{41.1}
\]

Summing directions gives

\[
\sum_d\sum_\kappa r_{d,\kappa}^2\le H B^{o(1)}.
\tag{41.2}
\]

In the reverse orientation, t37 gives for each fixed cover state `v`

\[
\boxed{
\sum_\kappa r_{v,\kappa}^2\le K_v B^{o(1)},
}
\tag{41.3}
\]

and therefore

\[
\sum_v\sum_\kappa r_{v,\kappa}^2\le H B^{o(1)}.
\tag{41.4}
\]

These are strong local incidence statements in both fibrations.

## 2. Why two-sided local energy is not enough

The global principal energy is

\[
A_1=\sum_\kappa\left(\sum_{d,v}1_{[F(d,v)]=\kappa}\right)^2.
\tag{41.5}
\]

Equations (41.2)--(41.4) do **not** imply `A1<=H B^{o(1)}`.

A perfect matching with `H` edges, all carrying one common color, has row and column energies exactly `H`, but the global color multiplicity is `H`, hence `A1=H^2`.

So one genuinely mixed incidence theorem is necessary; t36 and t37 cannot simply be added together to close t40.

## 3. Exact off-fiber geometry

Fix two descended t38 packets `gamma,gamma'`. Their moving-prime squareclass factors are separable quartics

\[
f_\gamma(x),\qquad f_{\gamma'}(y).
\]

Equality of squareclasses is equivalent to

\[
\boxed{
Y^2=f_\gamma(x)f_{\gamma'}(y).
}
\tag{41.6}
\]

Introduce

\[
E_\gamma:\ u^2=f_\gamma(x),
\qquad
E_{\gamma'}:\ v^2=f_{\gamma'}(y).
\tag{41.7}
\]

Then

\[
(x,u;y,v)\mapsto(x,y,Y=uv)
\]

identifies (41.6) birationally with

\[
\boxed{
(E_\gamma\times E_{\gamma'})/\{(u,v)\sim(-u,-v)\}.
}
\tag{41.8}
\]

After resolving quotient singularities, this is Kummer-type. Freezing either variable recovers the genus-one fibers controlled in t36--t38; allowing both to move gives a surface. Thus the existing elliptic bounded-height results do not automatically bound the total off-fiber incidence set.

## 4. Principal-energy decomposition

Write

\[
\boxed{
A_1=A_{\rm same\ direction}+A_{\rm off\ direction}.
}
\tag{41.9}
\]

The first term is already controlled by t36. The second is the new Kummer-surface incidence term.

The frozen `B=10000` audit gives

```text
H                                      1120
global A1                              2368
same-direction energy                  2240
off-direction ordered collisions        128
```

Thus only 128 of 2368 principal ordered collisions lie outside the already-controlled direction fibers.

The 128 off-direction collisions are not mostly a trivial shared-packet effect:

```text
off-direction and different unordered cover   104
off-direction with same ell                     16
off-direction with same common-core packet      16
off-direction with same descended packet         8
off-direction with exact same F                  8
```

So 104/128 change both direction and unordered cover, while only 8/128 are already identical at the full descended-packet level. The remaining mechanism is genuinely mixed. These are finite diagnostics, not asymptotic estimates.

For reference, the frozen partition energies are

```text
direction             137 cells   energy 2240
ordered cover         216 cells   energy 1132
unordered cover       108 cells   energy 2264
canonical ell          87 cells   energy 2256
common-core packet     37 cells   energy 2256
descended packet      108 cells   energy 1128
```

## 5. Fourth energy is a separate expansion problem

Let `r(kappa)` be global squareclass multiplicity and define

\[
c(t)=\sum_\kappa r(\kappa)r(\kappa t).
\tag{41.10}
\]

Then

\[
E_4=\sum_t c(t)^2,
\qquad c(1)=A_1,
\qquad \sum_t c(t)=H^2.
\tag{41.11}
\]

Cauchy gives `c(t)<=A1`, hence

\[
\boxed{
A_1^2\le E_4\le A_1H^2.
}
\tag{41.12}
\]

Therefore even a proof of `A1<=H B^{o(1)}` would only imply the soft bound `E4<=H^3 B^{o(1)}`. The nonprincipal squareclass convolution needs its own expansion theorem.

## 6. Frozen fourth-energy diagnostics

For the 1120-state frozen family,

\[
A_1=2368,
\qquad
E_4=21,193,216.
\]

Thus

\[
A_1/H\approx2.114,
\qquad
E_4/H^2\approx16.895.
\]

The principal contribution is

\[
A_1^2=5,607,424,
\]

which is only about `26.46%` of `E4`; the nonprincipal contribution is

\[
15,585,792.
\]

The largest nonprincipal cross-kernel multiplicity is only `160` in the frozen family, versus the principal multiplicity `2368`. The leading nonprincipal kernels are

```text
91:160, 209:152, 286:136, 34034:136,
41:128, 329:128, 4641:128, 11:120
```

This is favorable finite behavior, but it is not an asymptotic flattening theorem.

## 7. What t42 must add

The next theorem must couple the two fibrations rather than repeat another one-variable elliptic estimate. The natural split is:

1. isolate packet pairs for which the two genus-one factors are isogenous or satisfy another exceptional algebraic relation;
2. prove a transverse incidence bound for generic packet pairs using the canonical-largest-prime and common-core restrictions;
3. simultaneously control nonprincipal squareclass convolution so that `E4` is near-quadratic rather than merely bounded by `A1 H^2`.

The frozen 128 off-direction collisions are now compactly classified and provide the audit target for that split.

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
