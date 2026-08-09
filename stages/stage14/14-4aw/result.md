# Stage14-4aw — auxiliary-state modulus freezing and discrepancy boundary

## Result

Stage14-4av proved a fixed-power saving for the **bare** reciprocal Euclid-incidence block on balanced intermediate dyadic ranges. The remaining question was whether the growing complementary descent state destroys this separability.

It does not destroy the **bulk**. After the complete state modulus is frozen, primitive Möbius inversion leaves a rank-one product of one-column local densities. The unresolved mass is confined to the finite-box/Möbius discrepancy and sparse dyadic endpoints.

Write

```text
A=m,
B=n,
C=m-n,
D=m+n,
E=m^2+n^2.
```

Let the odd squarefree state moduli in the five pairwise-disjoint columns be

```text
q_A,q_B,q_C,q_D,q_E,
Q=q_A q_B q_C q_D q_E.
```

All assertions below are on a rectangular Euclid box of side lengths `X,Y`, with primitive and opposite-parity pairs.

## Exact local primitive factors

For an odd prime `p`, the primitive residue population modulo `p` has size `p^2-1`.

For each linear column `A,B,C,D`, the condition `p|L(m,n)` is one nonzero line through the origin, hence contributes `p-1` primitive residues. Its conditional primitive density is therefore

\[
\lambda_L(p)=\frac{p-1}{p^2-1}=\frac1{p+1}.
\]

For `E=m^2+n^2`, there is no primitive root when `p=3 mod 4`; when `p=1 mod 4`, the zero set is two nonzero isotropic lines and has `2(p-1)` primitive residues. Hence

\[
\lambda_E(p)=
\begin{cases}
2/(p+1),&p\equiv1\pmod4,\\
0,&p\equiv3\pmod4.
\end{cases}
\]

Extend multiplicatively to odd squarefree moduli. Because each odd prime belongs to exactly one Euclid column, CRT introduces no cross-column local factor.

The baseline density of primitive opposite-parity integer pairs is

\[
\frac4{\pi^2}.
\]

## Primitive Möbius rank-one bulk

Let `W_R(q_A,...,q_E)` count primitive opposite-parity pairs in the box satisfying the five divisibility conditions. Then

\[
\boxed{
W_R(q_A,\ldots,q_E)
=
\frac4{\pi^2}XY
\lambda_L(q_A)\lambda_L(q_B)\lambda_L(q_C)\lambda_L(q_D)\lambda_E(q_E)
+\Delta_R(q_A,\ldots,q_E).}
\]

This formula is obtained by first imposing the local primitive residue conditions at primes dividing `2Q`, then applying Möbius inversion only to common divisors coprime to `2Q`.

The key consequence for 14-4av is that **state splitting preserves rank one**. If one column modulus is split into coprime selected/unselected/auxiliary pieces, multiplicativity gives

\[
\lambda(q_1q_2)=\lambda(q_1)\lambda(q_2).
\]

Thus after all complementary state variables are frozen, a reciprocal edge with free pieces `u,v` has bulk coefficient

\[
\Gamma(\text{frozen state})\,\alpha(u)\beta(v),
\]

where `alpha,beta` contain only one-variable local densities and one-variable residue characters. The s5h quadratic-large-sieve estimate therefore applies to the bulk exactly as in the separable 14-4av block.

So the 14-4av obstruction

```text
GROWING_AUXILIARY_STATE_INCIDENCE_COUPLING
```

is removed from the bulk term.

## Explicit Möbius discrepancy decomposition

Choose `D>=1`. For the Möbius sum with `(d,2Q)=1`, split at `d=D`:

\[
\Delta_R=\Delta_{\le D}+\Delta_{>D}.
\]

Writing `rho(Q)` for the number of admissible primitive residue classes modulo the odd state modulus, elementary rectangular lattice counting gives

\[
\Delta_{\le D}
\ll
\rho(Q)\left(\frac{X+Y}{Q}\log(2D)+D\right),
\]

while discarding the state congruences in the large-common-divisor tail gives

\[
\Delta_{>D}
\ll
\frac{XY}{D}+(X+Y)\log(2M)+M,
\]

with `M` the ambient coordinate scale.

Using `rho(Q)<=Q^{1+o(1)}` and balancing the `rho(Q)D` and `XY/D` terms yields the safe pointwise summary

\[
\boxed{
\Delta_R
\ll_\varepsilon
Q^\varepsilon\left((X+Y)\log(2M)+\sqrt{QXY}+Q\right).}
\]

This is a pointwise bound. It is **not** yet the dispersion estimate needed to sum all reciprocal state blocks.

## Medium-modulus interpretation

On balanced boxes `X~Y~L`, suppose the complete frozen state modulus obeys

\[
Q\le L^{2-2\kappa}.
\]

Then the pointwise discrepancy bound is

\[
\Delta_R\ll L^{2-\kappa+o(1)}.
\]

Thus every fixed state has a power-saving discrepancy in this medium-modulus regime. But the full local expansion sums over many moving moduli, so a pointwise estimate cannot be summed trivially. The missing theorem is an `L^2`/dispersion estimate for the matrix

\[
\Delta(u,v;\text{frozen state}).
\]

A sufficient contract is a bound of the form

\[
\sum_{u\asymp U}\sum_{v\asymp V}
|\Delta(u,v)|^2
\ll L^{4-2\eta_{\rm disp}+o(1)}
\]

with normalization strong enough that Cauchy--Schwarz plus the quadratic large sieve produces a summable reciprocal error.

No such uniform bound is claimed here.

## Dyadic endpoint ledger

The dyadic decomposition now has three analytically distinct ranges.

1. **Balanced/medium reciprocal blocks**: `L^kappa <= U,V <= L^(1-kappa)` and complete state modulus below `L^(2-2kappa)`. The rank-one bulk has the 14-4av fixed-power saving; only the discrepancy dispersion remains.
2. **Microscopic-side blocks**: `min(U,V)<L^kappa`. The separable large-sieve gain can deteriorate to no fixed power as a side approaches `1`. These are lower-dimensional/endpoint modes and require a separate switching or recursive treatment.
3. **Sparse large-modulus blocks**: complete state modulus `Q>L^(2-2kappa)` (in particular near or above the geometric area `XY`). The pointwise Möbius discrepancy is comparable with the bulk scale, so divisor switching/complementary divisors are required.

There are only `O((log L)^2)` dyadic `(U,V)` ranges for each frozen structural case. Therefore summing a **proved uniform block bound** across dyadic ranges costs only `L^o(1)`. This counts the endpoint ranges but does not manufacture a missing bound for their mass.

## What 14-4aw closes

The full local analytic chain is now

```text
full local state expansion
  -> freeze complementary state moduli
  -> rank-one primitive-Mobius bulk + Delta
  -> quadratic-large-sieve saving on rank-one medium bulk
  -> [missing] L2 dispersion for Delta
  -> [missing] sparse/microscopic endpoint switching.
```

Accordingly, the first unresolved local object is no longer an arbitrary auxiliary-state coefficient matrix. It is

```text
DISCREPANCY_L2_AND_SPARSE_ENDPOINT_CONTROL.
```

The parallel Draft s5i computation independently reaches the same rank-one-bulk/discrepancy split; 14-4aw does not depend on that Draft being merged.

## Boundary

```text
STAGE14_4AW=AUXILIARY_STATE_BULK_FACTORIZED_AND_DISCREPANCY_ENDPOINT_BOUNDARY_ISOLATED
LINEAR_PRIMITIVE_LOCAL_FACTOR_EXACT=true
NORM_PRIMITIVE_LOCAL_FACTOR_EXACT=true
PRIMITIVE_OPPOSITE_PARITY_BASE_DENSITY=4/pi^2
PRIMITIVE_MOBIUS_RANK_ONE_BULK=true
STATE_SPLIT_PRESERVES_BULK_SEPARABILITY=true
GROWING_AUXILIARY_STATE_COUPLING_IN_BULK=false
MOBIUS_TRUNCATION_DISCREPANCY_DECOMPOSITION=true
MEDIUM_MODULUS_POINTWISE_DISCREPANCY_POWER_SAVING=true
DISCREPANCY_SECOND_MOMENT_PROVED=false
MICROSCOPIC_ENDPOINT_BLOCKS_CLOSED=false
SPARSE_LARGE_MODULUS_BLOCKS_CLOSED=false
EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED=false
EXPLICIT_E_LOC_PROVED=false
POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false
POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

No pointwise discrepancy estimate is promoted to an `L2` theorem. No endpoint switching theorem, complete local retainer exponent, or square-root asymptotic is claimed.

```text
NEXT=Stage14-4ax prove an L2 dispersion bound for the primitive-Mobius discrepancy on balanced/medium blocks and close the microscopic/sparse endpoint ranges by divisor switching or isolate a persistent diagonal
```
