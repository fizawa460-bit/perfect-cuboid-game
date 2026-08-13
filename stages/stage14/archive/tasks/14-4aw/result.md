# Stage14-4aw — auxiliary-state bulk transfer and endpoint ledger

## Result

Stage14-4av proved fixed-power cancellation for the bare linear reciprocal block on balanced interior dyadic ranges. Merged Stage14-s5i then proved that primitive/opposite-parity Euclid incidence with the full state moduli has the rank-one form

\[
W_R(q_A,\ldots,q_E)
=\frac4{\pi^2}XY\,
\lambda_L(q_A)\lambda_L(q_B)\lambda_L(q_C)\lambda_L(q_D)\lambda_E(q_E)
+\Delta_R(q_A,\ldots,q_E),
\]

where

\[
\lambda_L(p)=\frac1{p+1},
\qquad
\lambda_E(p)=
\begin{cases}
2/(p+1),&p\equiv1\pmod4,\\
0,&p\equiv3\pmod4.
\end{cases}
\]

for odd primes, extended multiplicatively to squarefree state pieces.

The purpose of 14-4aw is to insert this result into the main 14-4 chain and determine exactly what survives after the growing auxiliary state and dyadic endpoints are summed.

## 1. Growing auxiliary state does not obstruct the bulk

Fix all complementary selected/unselected/Q2 state pieces except one reciprocal edge `u,v`. Because the odd state pieces in the five Euclid columns have disjoint prime support and the `lambda` factors are multiplicative, the bulk coefficient is

\[
\Gamma(\text{frozen state})\,\alpha(u)\beta(v),
\]

with one-variable coefficients only. Hence the merged s5h quadratic-large-sieve estimate applies to the bulk exactly as in 14-4av.

Therefore

```text
GROWING_AUXILIARY_STATE_INCIDENCE_COUPLING
```

is **not** a bulk obstruction. It survives only through the discrepancy `Delta_R` and through endpoint/sparse ranges where the bulk estimate itself gives no fixed power.

## 2. Primitive Möbius discrepancy imported from s5i

For a Möbius cutoff `D`, merged s5i gives

\[
\Delta_R=\Delta_{\le D}+\Delta_{>D},
\]

with

\[
\Delta_{\le D}
\ll \rho(Q)\left(\frac{X+Y}{Q}\log(2D)+D\right),
\]

and

\[
\Delta_{>D}
\ll \frac{XY}{D}+(X+Y)\log(2M)+M.
\]

After balancing,

\[
\boxed{
\Delta_R\ll_\varepsilon
Q^\varepsilon\left((X+Y)\log(2M)+\sqrt{QXY}+Q\right).}
\]

On a balanced geometric box `X~Y~L`, if

\[
Q\le L^{2-2\kappa},
\]

then every fixed-state discrepancy satisfies

\[
\Delta_R\ll L^{2-\kappa+o(1)}.
\]

This is a **pointwise** saving only. Summing over the moving divisor/state matrix requires dispersion.

## 3. Interior bulk sum

For a reciprocal dyadic block `u~U`, `v~V`, 14-4av gives schematically

\[
B^{\rm bulk}(U,V)
\ll L^2 (UV)^\varepsilon
\sqrt{\frac1U+\frac1V}.
\]

If

\[
L^\kappa\le U,V\le L^{1-\kappa},
\]

then

\[
B^{\rm bulk}(U,V)\ll L^{2-\kappa/2+o(1)}.
\]

There are only `O((log L)^2)` dyadic `(U,V)` blocks, so the complete interior bulk sum remains

\[
\boxed{
E_{\rm bulk,int}(L;\kappa)
\ll L^{2-\kappa/2+o(1)}.}
\]

Thus the auxiliary-state bulk is genuinely summable with a fixed power saving on the interior range.

## 4. Microscopic endpoint sum

Suppose `U<=V` and `U<L^kappa`. The same separable estimate gives

\[
B^{\rm bulk}(U,V)
\ll L^{2+o(1)}U^{-1/2}.
\]

Summing over dyadic `U<L^kappa` gives a bounded geometric series dominated by the smallest block. Consequently

\[
\boxed{
E_{\rm bulk,micro}(L;\kappa)\ll L^{2+o(1)}.}
\]

This is important: the microscopic endpoint ranges can be **summed without a power loss**, but they do **not** inherit a fixed power saving. When `U=1`, the reciprocal character degenerates to the constant character, so a uniform off-diagonal saving cannot be demanded from the quadratic large sieve alone.

Hence microscopic endpoints are now isolated as a genuine lower-dimensional/diagonal-type obstruction rather than an uncontrolled number of blocks.

## 5. Sparse large-state modulus

The second endpoint is not a small reciprocal side but a large complete frozen state modulus. When

\[
Q>L^{2-2\kappa},
\]

the s5i pointwise discrepancy can be as large as the scale needed for the local error budget. Near `Q~XY~L^2`, the `sqrt(QXY)` and `Q` terms are both of order `L^2`.

Thus these blocks require divisor switching/complementary divisors or an independent sparse-incidence estimate. The number of dyadic modulus ranges is logarithmic, but their mass is not closed by counting ranges alone.

## 6. Exact dispersion target

For a fixed frozen structural state define

\[
\mathfrak D(U,V)
=\sum_{u\asymp U}\sum_{v\asymp V}
|\Delta(u,v)|^2.
\]

The trivial Cauchy--Schwarz transfer is

\[
\left|\sum_{u,v}\Delta(u,v)\left(\frac uv\right)\right|
\le (UV)^{1/2}\mathfrak D(U,V)^{1/2}.
\]

Therefore a sufficient fixed-power target for an `L^{2-eta}` reciprocal error is

\[
\boxed{
\mathfrak D(U,V)
\ll \frac{L^{4-2\eta+o(1)}}{UV}.}
\]

A sharper structured dispersion estimate may do better, but this is a clean sufficient contract. Merged s5i does not prove it.

## 7. Main-track local boundary

Combining 14-4au, 14-4av, and merged s5i now gives

```text
local support expansion
  -> rank-one primitive-Mobius bulk + Delta
  -> interior bulk: fixed-power saving and dyadic summation proved
  -> microscopic bulk: summable, but only trivial L^(2+o(1)) scale
  -> Delta: pointwise medium saving, L2 dispersion missing
  -> sparse Q: switching bound missing.
```

So the first remaining local object is sharpened to

```text
DISCREPANCY_L2_PLUS_MICROSCOPIC_DIAGONAL_PLUS_SPARSE_SWITCHING.
```

Until those three pieces are controlled, 14-4as cannot receive an explicit nontrivial pair `(rho_loc,E_loc)`.

## Boundary

```text
STAGE14_4AW=AUXILIARY_STATE_BULK_TRANSFERRED_AND_ENDPOINT_LEDGER_QUANTIFIED
S5I_RANK_ONE_BULK_IMPORTED=true
GROWING_AUXILIARY_STATE_COUPLING_IN_BULK=false
INTERIOR_AUXILIARY_BULK_POWER_SAVING_SUMMED=true
MICROSCOPIC_BULK_DYADIC_SUMMED=true
MICROSCOPIC_BULK_FIXED_POWER_SAVING=false
MEDIUM_MODULUS_POINTWISE_DISCREPANCY_POWER_SAVING=true
DISCREPANCY_L2_TARGET_EXPLICIT=true
DISCREPANCY_SECOND_MOMENT_PROVED=false
SPARSE_LARGE_MODULUS_BLOCKS_CLOSED=false
MICROSCOPIC_DIAGONAL_CLOSED=false
EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED=false
EXPLICIT_E_LOC_PROVED=false
POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false
POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

No pointwise discrepancy bound is promoted to a dispersion theorem. No microscopic constant-mode cancellation or sparse divisor-switching theorem is claimed.

```text
NEXT=Stage14-4ax attack the discrepancy L2 target on balanced/medium blocks and close either the microscopic diagonal or sparse large-modulus regime by divisor switching, exposing whichever obstruction survives first
```
