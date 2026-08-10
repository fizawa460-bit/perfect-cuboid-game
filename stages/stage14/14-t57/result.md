# Stage14-t57 — rank-one Kummer / Mellin adapter and selector-correlation boundary

## Purpose

Merged Stage14-t56 reduces the dominant fixed-`U` invisible/invisible packet to

\[
\sum_{p\ne q}
\left|\langle b_{U,pq},K_{pq}\rangle\right|^2
\ll R_U P^2 B^{o(1)}.
\tag{57.1}
\]

Toolbox-as split a possible external trace-function route into three gates:

1. one-field trace/sheaf certification;
2. physical-selector support/energy transfer;
3. two-prime zero-fixed-loss reassembly.

Stage14-t57 attacks these gates directly.  The main new point is that the t55 projective kernel is much more special than a generic high-rank trace sheaf: on the split affine torus it is an exact rank-one Kummer ratio/product kernel with an all-order Mellin expansion of bounded spectral L2 energy.  This closes the algebraic kernel certificate and the kernel-side CRT bookkeeping, but it also shows why the cited generic high-rank bilinear theorems are not direct imports.  The only genuinely live part is the correlation of the actual physical selector with this rank-one toroidal spectrum.

No global principal-energy or `T=o(sqrt(B))` claim is made.

## 1. Exact split-prime ratio/product factorization

Let `p == 1 (mod 4)` be a good auxiliary prime and put

\[
A_p(z)=\chi_p(z^2-1),\qquad z\in\mathbf F_p^\times.
\tag{57.2}
\]

On the affine chart of the t55 kernel write

\[
t=A/B,\qquad x=P/Q,
\]

with `t,x != 0`.  Since `chi_p(-1)=1`,

\[
\begin{aligned}
K_p(t,x)
&=\chi_p\bigl((x^2-t^2)(1-t^2x^2)\bigr)\\
&=A_p(x/t)A_p(tx).
\end{aligned}
\tag{57.3}
\]

This is an identity including the zero values at the four Kummer divisors.

Equivalently, away from the two Cayley poles,

\[
r=\frac{x-t}{1+tx},\qquad
s=\frac{x+t}{1-tx},
\]

satisfy

\[
\frac{x^2-t^2}{1-t^2x^2}=rs,
\tag{57.4}
\]

and the original quartic differs from `rs` by the square `(1-t^2x^2)^2`.  Thus the t55 squareclass is an exact rank-one Kummer product after a birational change of the two projective coordinates.

The branch divisor is the union

```text
x=t, x=-t, tx=1, tx=-1.
```

Hence its algebraic complexity is absolutely bounded, uniformly in the fixed primitive `U`.  Multiplication by fixed `U` only applies the already-proved t55 `PGL2` reparameterization on the first projective coordinate for good primes `p not dividing N(U)`.

## 2. All-order multiplicative Mellin expansion

Let `G=F_p^*`, `n=p-1`, and for every multiplicative character `eta` of `G` define

\[
\widehat A_p(\eta)
=\sum_{z\in G} A_p(z)\overline{\eta(z)}.
\tag{57.5}
\]

Fourier inversion gives

\[
A_p(z)=\frac1n\sum_\eta \widehat A_p(\eta)\eta(z).
\tag{57.6}
\]

Substitution into (57.3) yields the exact two-coordinate Mellin packet

\[
\boxed{
K_p(t,x)
=\frac1{n^2}\sum_{\eta,\xi}
\widehat A_p(\eta)\widehat A_p(\xi)
(\xi\eta^{-1})(t)(\eta\xi)(x).
}
\tag{57.7}
\]

Because `A_p(-z)=A_p(z)`,

\[
\widehat A_p(\eta)=0
\quad\text{whenever}\quad \eta(-1)=-1.
\tag{57.8}
\]

The sheaf behind each coefficient in (57.5) is a tame rank-one Kummer sheaf with singular support contained in `{0,+1,-1,infinity}`.  For all non-exceptional character modes the usual rank-one Weil bound is `O(sqrt(p))`; the finitely simpler modes satisfy the same safe `O(sqrt(p))` bound directly.  No conductor grows with `B` or with the fixed `U`.

Most importantly, Parseval is exact:

\[
\sum_\eta |\widehat A_p(\eta)|^2
=n\sum_{z\in G}|A_p(z)|^2
=n(p-3).
\tag{57.9}
\]

Therefore the normalized two-coordinate coefficient packet

\[
c_p(\eta,\xi)
=\frac{\widehat A_p(\eta)\widehat A_p(\xi)}{n^2}
\]

has

\[
\boxed{
\sum_{\eta,\xi}|c_p(\eta,\xi)|^2
=\left(\frac{p-3}{p-1}\right)^2
\le1.
}
\tag{57.10}
\]

Thus the complete t55 kernel has an exact all-order rank-one Mellin packet with **O(1) spectral L2 energy**.  This is stronger structural information than merely knowing the total complete trace.

## 3. One-field sheaf gate: algebraic certificate closed, direct theorem import still invalid

Equation (57.3) certifies the one-field algebraic object: it is a bounded-complexity rank-one Kummer sheaf on the two-dimensional torus/projective surface, with a finite explicit exceptional divisor.  Accordingly

```text
FIXED_U_ONE_FIELD_RANK1_KUMMER_CERTIFICATE_PROVED=true
FIXED_U_ALL_ORDER_MELLIN_PACKET_PROVED=true
```

However this does **not** turn Ping Xi's theorem into a direct import.  The theorem shortlisted in toolbox-as is formulated for bilinear forms with a one-variable trace kernel such as `K(mn)` coming from a bountiful sheaf; bountiful sheaves have rank at least two.  The Stage14 kernel is rank one and genuinely bivariate before the coordinate-mixing ratio/product transform.

A newer source also does not remove this mismatch automatically.  Fouvry--Kowalski--Michel--Sawin, *Bilinear forms with trace functions*, arXiv:2511.09459v3 (11 Mar 2026), proves powerful type-I/II estimates for gallant sheaves with monomial kernels `K(m^b n^c)`.  Its main gallant class again has rank at least two.  Section 9.11 explains how their method can sometimes treat rank-one Kummer/Artin--Schreier trace functions, but requires a separate application-specific classification of the diagonal parameter varieties.  It does not state a ready-made theorem for the present bivariate ratio/product kernel with the Stage14 physical incidence selector.

Therefore

```text
PING_XI_DIRECT_IMPORT_VALID=false
FKMS_2026_DIRECT_IMPORT_VALID=false
```

remains the correct theorem-import boundary.

## 4. Two-prime kernel reassembly has zero fixed-power spectral cost

For distinct split primes `p,q`, CRT gives

\[
K_{pq}=K_pK_q
\]

on the corresponding product residue box.  Applying (57.7) independently at `p` and `q`, the spectral coefficient packet is the tensor product

\[
c_{pq}=c_p\otimes c_q.
\]

Hence by (57.10)

\[
\boxed{
\|c_{pq}\|_2^2
=\|c_p\|_2^2\|c_q\|_2^2
\le1.
}
\tag{57.11}
\]

Thus CRT itself, all-order mode expansion, and the passage from one split prime to two distinct split primes create **no fixed `B^omega` loss**.  This agrees with the finite-CRT active-support philosophy already frozen in tH3.

This closes the kernel-side content of toolbox-as gate 3.  It does not close the physical two-prime dispersion, because the same integral state selector is evaluated at both primes.

```text
TWO_PRIME_KERNEL_SPECTRAL_REASSEMBLY_FIXED_POWER_LOSS=0
FULL_TWO_PRIME_PHYSICAL_DISPERSION_PROVED=false
```

## 5. Why bounded spectral energy does not prove sparse-selector cancellation

Let `nu_{U,p}` be the physical residue multiplicity after all fixed-`U` labels are retained.  Inserting (57.7) gives

\[
\langle \nu_{U,p},K_p\rangle
=\sum_{\eta,\xi}c_p(\eta,\xi)
\widehat\nu_{U,p}(\xi\eta^{-1},\eta\xi).
\tag{57.12}
\]

Although `||c_p||_2<=1`, plain Cauchy against the complete character basis is not enough: Parseval for the sparse selector returns its residue-collision energy multiplied by the size of the complete spectral universe.  This reproduces, rather than removes, the selector obstruction.

Equivalently, an arbitrary selector can concentrate on one sign of the Kummer kernel.  The rank-one factorization therefore sharpens the t55/tH15 lesson:

> the algebraic kernel is no longer the obstruction; cancellation must come from arithmetic non-correlation of the **actual physical selector** with the toroidal Mellin modes.

The tH4/tH5 roadworks remain useful bookkeeping: divisor lifts, Gaussian representation multiplicity, bounded masks, smooth/Mellin weights, conductor bands and exact Gaussian-pair coefficient collisions cost only `B^{o(1)}` when a valid base analytic estimate is available.  But their safety statements do not prove the missing same-modulus selector correlation theorem.

## 6. Minimal remaining receiver

The three toolbox-as gates now collapse to one analytic object.

Define

```text
SharedUPhysicalToroidalMellinCorrelation
```

as the uniform estimate which, for every fixed primitive `U`, legal divisor-fan/branch refinement and distinct split auxiliary pair `p,q`, controls the physical centered incidence selector after the exact Mellin packet (57.7), while retaining

```text
moving canonical pi
moving primitive V
moving delta
N(V)=k*delta
hyperbola cutoff
canonical-prime selector
interval/reconstruction masks
branch/orientation
bad-prime masks
same physical state across p and q
```

and gives after auxiliary-pair averaging

\[
\boxed{
\sum_{p\ne q}
|\langle b_{U,pq},K_{pq}\rangle|^2
\ll R_UP^2B^{o(1)}.
}
\tag{57.13}
\]

The name is intentionally narrower than a generic trace-bilinear theorem: (57.7) has already removed uncertainty about the algebraic kernel and (57.11) has removed kernel-side two-prime assembly cost.  What remains is physical support correlation.

No pair-to-squareclass collapse, `E4` coefficient energy, independent `U/V` modulus tensorization, or blockwise absolute recombination is allowed.

## 7. Mixed branch

The single frozen invisible/visible shared-`U` block remains separate.  Nothing in the rank-one invisible factorization proves its asymptotic negligibility or its own centered dispersion.  The mixed branch is therefore still an explicit second obligation after the dominant invisible receiver is closed.

## 8. tH decision

No `tH16` is needed.

The new algebraic question encountered by t57 is resolved inside t57 by the exact Kummer/Mellin factorization.  The remaining object is the same receiver-specific physical selector correlation already identified by tH4/tH15/toolbox-as, now in a narrower spectral form.  A new H-line would duplicate infrastructure rather than solve a new ambiguity.

## Locked boundary

```text
STAGE14_T57=COMPLETE_RANK1_KUMMER_MELLIN_ADAPTER_AND_PHYSICAL_SELECTOR_CORRELATION_BOUNDARY
FIXED_U_ONE_FIELD_RANK1_KUMMER_CERTIFICATE_PROVED=true
FIXED_U_ALL_ORDER_MELLIN_PACKET_PROVED=true
FIXED_U_MELLIN_PACKET_L2_ENERGY_LE_ONE=true
PING_XI_DIRECT_IMPORT_VALID=false
FKMS_2026_DIRECT_IMPORT_VALID=false
TWO_PRIME_KERNEL_SPECTRAL_REASSEMBLY_FIXED_POWER_LOSS=0
FIXED_U_PHYSICAL_SELECTOR_SUPPORT_ENERGY_TRANSFER_PROVED=false
SHARED_U_PHYSICAL_TOROIDAL_MELLIN_CORRELATION_PROVED=false
SHARED_U_CENTERED_PROJECTIVE_SELECTOR_DISPERSION_PROVED=false
SHARED_U_MIXED_BRANCH_SEPARATE=true
SHARED_U_MIXED_BRANCH_DISPERSION_PROVED=false
SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED=false
GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false
GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
TH16_NEEDED=false
NEXT=Stage14-t58 attack SharedUPhysicalToroidalMellinCorrelation using the exact rank-one packet; first test whether the physical reconstruction masks admit a bounded-energy separated/toroidal decomposition, otherwise freeze that mask correlation as the sole invisible obstruction
```
