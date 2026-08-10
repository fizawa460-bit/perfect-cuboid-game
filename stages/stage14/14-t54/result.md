# Stage14-t54 — shared-U divisor fan and bipartite squareclass-energy reduction

## Purpose

Stage14-t53 split the post-residue distinct-`ell` cross-good LD2 principal family into

- 6 shared-`U` blocks,
- 1 shared-`V` block,
- 5 genuinely `U/V`-transverse blocks.

Stage14-t54 attacks the largest stratum, `SharedUCanonicalPrimePrincipalIncidence`, and asks whether fixing the primitive Gaussian direction cofactor `U` reduces the principal problem to a one-dimensional moving canonical-prime sum.

It does not.  Fixing `U` fixes `m=N(U)`, but the cover cofactor `V`, the hyperbola denominator `delta`, and the common-refinement packet remain live.  What can be removed exactly is the divisor fan.

No global principal-collision power saving is claimed.

## 1. Exact fixed-U divisor fan

For every physical state,

\[
N(U)=m,\qquad N(V)=n=k\delta,
\]

with

\[
k=\gcd(n,\varepsilon m),\qquad k\mid \varepsilon m.
\]

Set

\[
h=\frac{\varepsilon m}{k}.
\]

Then

\[
\boxed{n=k\delta,\qquad k\mid\varepsilon m,\qquad hk=\varepsilon m.}
\]

Hence after fixing primitive `U` and the finite `epsilon` split, the variables `k,h` range over only divisor choices of `epsilon*m`, costing `B^{o(1)}`.  This is the exact divisor fan.

However `V` still satisfies only

\[
N(V)=k\delta,
\]

so both `delta` and the primitive Gaussian representation `V` remain moving.

## 2. Frozen shared-U audit

The six post-residue shared-`U` principal blocks have

```text
same epsilon        6 / 6
same branch         5 / 6
same k              4 / 6
same h              4 / 6
same delta          0 / 6
same V unit-orbit   0 / 6
```

Thus the shared-`U` phenomenon is not a disguised fixed-`V` packet.

Across the whole reciprocal-quotient frozen family:

```text
distinct U unit-orbits             4
max states in one U fiber        276
max distinct V in one U fiber     16
max distinct delta in one U fiber  8
U fibers with principal excess      2
max principal excess in one U fiber 10
```

These are finite diagnostics only.

## 3. Two one-variable receivers exist, but do not globalize

There are already strong one-variable inputs on both coordinate axes.

1. Fix `pi`.  Then the direction `pi U` is fixed, so the t36 fixed-direction squareclass-energy mechanism controls the cover variable.
2. Fix `V` and the branch.  Then t38 writes the moving-`pi` squareclass equation as a smooth genus-one quartic.  The same bounded-height twist mechanism applies to a fixed represented squareclass.

The physical shared-`U` family is therefore naturally a bipartite array with coordinates

\[
(\pi,V).
\]

But row- and column-wise squareclass multiplicity bounds do not imply a near-linear global squareclass energy.

A Latin-square countermodel makes this quantifier failure exact: on an `N x N` array color `(i,j)` by `i+j mod N`.  Every row and column sees each color once, yet each color occurs `N` times globally, so

\[
E=N^3=N\cdot H.
\]

For the frozen guard `N=32`,

```text
states                    1024
row color max                1
column color max             1
global color energy      32768
near-linear target        1024
failure factor              32
```

Therefore t36 plus t38 cannot be combined by a formal Cauchy/globalization step to close the shared-`U` principal problem.

## 4. Required receiver

Define, for one fixed primitive `U` fiber,

\[
r_U(\kappa)=\#\{s:\ U_s\sim U,\ [\widetilde F_s]=\kappa\},
\]

and

\[
E_U=\sum_\kappa r_U(\kappa)^2.
\]

After the `B^{o(1)}` splits in `epsilon`, branch, and divisor-fan data, the required theorem is

\[
\boxed{E_U\ll R_U B^{o(1)}}
\]

uniformly in the critical strip, where `R_U` is the physical population of the fixed-`U` fiber.

We call this receiver

```text
SharedUBipartiteSquareclassEnergy
```

Its state space must retain

- fixed primitive `U`,
- `k | epsilon*N(U)`,
- moving canonical Gaussian prime `pi`,
- moving primitive `V` with `N(V)=k delta`,
- branch/orientation,
- interval and reconstruction masks,
- the hyperbola/divisor coupling.

The receiver must be noncircular: collapsing state pairs first to a product squareclass or cross-kernel is not allowed if it reintroduces the unresolved global fourth energy.

## 5. tH decision

Stage14-t54 satisfies a concrete support-stage trigger.

The residual object is genuinely two-dimensional after all exact divisor reductions, and is not supplied by t36, t38, or the fixed-common-core receivers tH12/tH13/tH14.  The one-variable bounds provably do not globalize.

Therefore:

```text
TH15_NEEDED=true
```

Stage14-tH15 should investigate a fixed-`U`, moving-`(pi,V)` bipartite squareclass-energy/dispersion theorem, or produce a precise impossibility/failure boundary that Stage14-t55 can consume.

## Boundary

```text
STAGE14_T54=COMPLETE_SHARED_U_DIVISOR_FAN_AND_BIPARTITE_ENERGY_REDUCTION
FIXED_U_DIVISOR_FAN_PROVED=true
FIXED_U_REDUCES_TO_ONE_DIMENSIONAL_CANONICAL_PRIME_SUM=false
ONE_VARIABLE_FIBER_BOUNDS_GLOBALIZE=false
SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_REQUIRED=true
SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED=false
SHARED_U_CANONICAL_PRIME_PRINCIPAL_INCIDENCE_PROVED=false
UV_TRANSVERSE_CROSS_GOOD_LD2_KUMMER_INCIDENCE_PROVED=false
GENERIC_CROSS_GOOD_LD2_KUMMER_PRINCIPAL_INCIDENCE_PROVED=false
GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false
GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
TH15_NEEDED=true
NEXT=Stage14-t55 attack SharedUBipartiteSquareclassEnergy directly; consume tH15 if available, preserving the fixed-U divisor fan and avoiding premature cross-kernel collapse
```
