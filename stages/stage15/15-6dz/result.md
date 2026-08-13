# Stage15-6dz — fixed-modulus congruence-refined count on the same physical measure

Base: Stage15-6dy. The exact one-prime acceptance set `E_p` and its charged local density `rho_p` are now known. This stage proves the fixed-finite-prime refinement before any ordered-limit or growing-prime argument.

Let
\[
\mathcal A(B)
\]
be the primitive physical shared-edge incidence population used in Stage15-2b, with the exact anticanonical height `R<=B` and one chosen real direction chamber if desired. Stage15-2b proves
\[
\mathcal A(B)\sim C_A B(\log B)^5.
\]
Every exactly-two box contributes one incidence, while every triple-face box contributes three.

## 1. One fixed prime

Fix one good split prime `p=1 mod 4`. The p-adic acceptance set
\[
\mathcal E_p=\{v_p(A)\equiv v_p(B)\pmod2\}
\]
is an open union of valuation annuli away from the zero divisors. Its boundary is contained in the four strict Gaussian divisors and their intersections, which have p-adic measure zero.

Stage15-2b already imports Huang's Manin--Peyre equidistribution for the same smooth split toric surface `Y`, the same anticanonical height, and adelic neighbourhood restrictions. Approximating `E_p` from inside and outside by finite unions of residue tubes therefore gives the fixed-local asymptotic
\[
\boxed{
\mathcal A_p(B)
=\rho_p C_A B(\log B)^5+o_p(B(\log B)^5),
}
\]
where `rho_p` is the exact local Tamagawa acceptance density from 6dy.

There is no hidden completion measure: the local condition is imposed directly on the unique toric/reconstructed representative of each physical incidence.

For `p=3 mod 4`, `rho_p=1`, so the same statement is tautological and supplies no thinning.

## 2. Exactly-two subtraction remains lower order

Let `M_3(B)` be the triple-face population. Stage15-2b proves
\[
M_3(B)=o(B(\log B)^5)
\]
by the geometrically integral thin cover. Imposing any fixed finite local acceptance condition can only delete triple-face points, so
\[
M_{3,p}(B)\le M_3(B)=o(B(\log B)^5).
\]
Using the exact incidence identity
\[
\mathcal A_p(B)=M_{2,p}(B)+3M_{3,p}(B),
\]
we obtain
\[
\boxed{
M_{2,p}(B)=\rho_p C_{M_2}B(\log B)^5+o_p(B(\log B)^5).
}
\]
Thus the fixed-prime refinement is on the **exact Stage15 ambient exactly-two measure**, not merely an unrestricted parameter box.

The same argument applies direction by direction because the direction choice is an archimedean chamber and the finite p-adic factor is unchanged.

## 3. Fixed finite prime set and CRT tensor

Now fix a finite set `S` of good split primes before sending `B` to infinity. Put
\[
\mathcal E_S=\bigcap_{p\in S}\mathcal E_p.
\]
The local conditions live at distinct finite places. The adelic Tamagawa measure factors, so the exact finite-set acceptance density is
\[
\boxed{\rho_S=\prod_{p\in S}\rho_p.}
\]
Huang equidistribution for the corresponding fixed adelic neighbourhood gives
\[
\boxed{
M_{2,S}(B)
=C_{M_2}\rho_S B(\log B)^5
+o_S(B(\log B)^5).
}
\]
Here `o_S` is allowed to depend on the **fixed** prime set. No uniformity in `max S`, `|S|`, or the product modulus is claimed.

This is the exact fixed-modulus congruence-refined count required before invoking any AR-035-style ordered limit.

## 4. Survivor domination

Every integral-space-diagonal survivor satisfies the valuation-parity condition at every prime. Therefore for every fixed finite split-prime set `S`,
\[
N_2(B)\le M_{2,S}(B).
\]
Dividing by the ambient asymptotic gives
\[
\boxed{
\limsup_{B\to\infty}\frac{N_2(B)}{M_2(B)}
\le \prod_{p\in S}\rho_p.
}
\]
This implication uses neither Stage15-5 nor the earlier Stage15-6 character/Pell/complementary receivers.

## 5. Boundary and error ledger

There are two lower-order terms and both are non-effective at the currently certified interface:

1. **adelic equidistribution boundary/error:** `o_S(B(log B)^5)` for each fixed local set;
2. **exactly-two subtraction:** at most `3M_3(B)=o(B(log B)^5)`.

Hence the combined refined error is
\[
\boxed{o_S(B(\log B)^5).}
\]
No rate uniform in `S` is proved. In particular this stage does **not** allow a modulus or prime set to grow with `B`.

## 6. Cell, core, and completion audit

- Cell normalization is only a reconstruction of the unique toric point; local density is computed before summing cell labels.
- States with `p|H` remain in the toric p-adic measure and were already included by the exceptional-divisor parity analysis of 6dy.
- If the common local parity is zero, `p\nmid k`; if it is one, `p|k` and `k>1`.
- The `k=1` factor-gap and `k>1` Pell completion descriptions are postfilters/reparametrizations of survivors and are not charged in this ambient refined count.
- `kg^2|Delta` remains available on survivors but is not multiplied into the local acceptance probability.
- `R<=B`, primitive/canonical masks and the exactly-two subtraction are unchanged.

```text
STAGE15_6_SUBSTAGE=6dz
STAGE15_6DZ_FIXED_PRIME_REFINED_ASYMPTOTIC=true
STAGE15_6DZ_ACTUAL_LOCAL_DENSITY_FROM_6DY=true
STAGE15_6DZ_FIXED_FINITE_SET_TENSOR=true
STAGE15_6DZ_FINITE_SET_DENSITY=PRODUCT_RHO_P
STAGE15_6DZ_EXACTLY_TWO_REFINEMENT=true
STAGE15_6DZ_REFINED_ERROR=o_S(B*log(B)^5)
STAGE15_6DZ_ERROR_UNIFORM_IN_S=false
STAGE15_6DZ_SURVIVOR_DOMINATION=true
STAGE15_6DZ_GROWING_MODULUS_USED=false
STAGE15_6DZ_EXIT=AR035_ORDERED_LIMIT_TEST_READY
```
