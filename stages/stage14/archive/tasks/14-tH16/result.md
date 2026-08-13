# Stage14-tH16 — same-modulus / reciprocity / hyperbolic audit for the canonical-prime–delta toroidal second moment

## Purpose

Merged Stage14-t58 isolates the dominant fixed-`U` invisible packet as

```text
SharedUCanonicalPrimeDeltaToroidalSecondMoment
```

with target

\[
\sum_{p\ne q}
\left|
\sum_{\substack{\ell\delta\le Y_U\\
\ell\ \mathrm{canonical\ split\ prime}}}
\sum_{s\in C_U(\ell,\delta)}
 w_s K_{pq}(t_s,x_s)
\right|^2
\ll P^2 B^{o(1)}\sum_s|w_s|^2,
\tag{H16.1}
\]

where

\[
K_p(t,x)=A_p(x/t)A_p(tx),\qquad A_p(z)=\chi_p(z^2-1),
\tag{H16.2}
\]

and every radial `(ell,delta)` cell has only `B^{o(1)}` angular lifts. The sharp hyperbola `ell*delta<=Y_U`, fixed primitive `U`, `epsilon`, divisor-fan `k`, moving canonical Gaussian prime `pi`, moving primitive Gaussian `V`, and the same physical state at both auxiliary primes are retained.

Stage14-tH16 independently tests three possible known-method routes:

1. same-modulus multiplicative / Hecke large sieve;
2. Gaussian or rational quadratic reciprocity;
3. Jacobi-symbol bilinear estimates on hyperbolic regions.

The result is a precise **non-import boundary**. No currently certified theorem closes (H16.1) directly. Two useful exact reductions are nevertheless proved:

- a reciprocity projection to the already-merged tH14-R2 quadratic product-row frame;
- a Mellin-side same-modulus spectral collision identity showing exactly why generic full-character Cauchy is too expensive.

No Stage14 power saving is claimed.

---

## 1. Imported exact packet

The legal packet inherits from t57/t58:

```text
fixed primitive U
fixed epsilon
fixed divisor-fan k | epsilon*N(U)
sharp ell*delta <= Y_U
moving canonical split prime ell=N(pi)
moving oriented Gaussian prime pi
moving primitive V with N(V)=k*delta
moving delta
invisible branch
canonical / interval / reconstruction / primitive masks
B^o(1) angular multiplicity per (ell,delta) radial cell
same auxiliary modulus acting on both toroidal coordinates
distinct auxiliary split primes p,q
```

The exact ratio/product variables are

\[
u=x/t,\qquad v=tx,
\]

and t58 proves that the physical chamber is exactly

\[
u>1,\qquad 0<v<1.
\]

The full selector is not a Cartesian product, so independent `pi`/`V` tensorisation remains forbidden.

---

## 2. Two exact representations of the same kernel

The audit starts from a structural dichotomy.

### 2.1 Mellin representation: coefficient-safe, theorem-missing

For one split good auxiliary prime `p`, t57 proves

\[
K_p(t,x)
=\frac1{(p-1)^2}
\sum_{\eta,\xi}
\widehat A_p(\eta)\widehat A_p(\xi)
(\xi\eta^{-1})(t)(\eta\xi)(x),
\tag{H16.3}
\]

with normalized spectral energy

\[
\sum_{\eta,\xi}
\left|\frac{\widehat A_p(\eta)\widehat A_p(\xi)}{(p-1)^2}\right|^2
\le1.
\tag{H16.4}
\]

This keeps the actual physical state coefficients and does **not** collapse squareclasses. It is therefore the non-circular representation.

But the mode family consists of two multiplicative characters over the **same** residue field/modulus, with character orders varying through the full even spectrum. Existing tH4 supplies weighted transfer once a base same-modulus theorem exists; it explicitly does not prove that base theorem.

### 2.2 Quadratic reciprocity representation: theorem-available, energy-circular

Write projective coordinates

\[
t=A/B,\qquad x=P/Q
\]

in coprime integral form. Define

\[
\Delta_s
=(B^2P^2-A^2Q^2)(B^2Q^2-A^2P^2).
\tag{H16.5}
\]

For every good split auxiliary prime `r`, denominators are squares and

\[
\boxed{K_r(t_s,x_s)=\left(\frac{\Delta_s}{r}\right).}
\tag{H16.6}
\]

Let

\[
D_s=\operatorname{funddisc}(\operatorname{sqf}(\Delta_s)).
\]

After the finite 2-adic/sign refinement already used in tH13/tH14, and since the auxiliary primes are split rational primes, quadratic reciprocity gives

\[
\boxed{K_r(t_s,x_s)=\chi_{D_s}(r)}
\tag{H16.7}
\]

on the good slice. Hence

\[
K_{pq}(s)=\chi_{D_s}(pq).
\tag{H16.8}
\]

This is an exact legal reciprocity projection. However, if

\[
C_D=\sum_{s:D_s=D}w_s,
\]

then

\[
\sum_s w_sK_{pq}(s)=\sum_D C_D\chi_D(pq),
\tag{H16.9}
\]

and the coefficient energy is

\[
E_D=\sum_D|C_D|^2.
\tag{H16.10}
\]

For unit physical weights, (H16.10) is exactly the fixed-`U` weighted squareclass-fiber energy whose near-linearity is the live goal. Thus reciprocity gives the right *character family* only by moving the unresolved principal energy into the coefficient norm.

This is not an `E4` pair collapse; it is a one-state squareclass quotient. It is still circular for proving the same fixed-`U` squareclass energy.

---

## 3. Quadratic / Hecke large sieve: exact reusable adapter and exact failure

Merged tH14-R2 already proves the product-row quadratic frame

\[
\sum_{p\ne q}
\left|\sum_D C_D\chi_D(pq)\right|^2
\ll B^{o(1)}(K+L^2)E_D,
\tag{H16.11}
\]

where `|D|<=K` and `p,q~L`.

Therefore tH16 does **not** need a new quadratic large-sieve theorem. The reciprocity route from (H16.6) to (H16.11) is valid.

If

\[
K\le B^{d+o(1)},\qquad L=B^{\rho+o(1)},
\]

then the conductor-range cost is absorbed at the target prime-pair scale when

\[
2\rho\ge d.
\tag{H16.12}
\]

But even in that favorable regime (H16.11) becomes only

\[
\ll P^2 E_D B^{o(1)},
\]

not

\[
\ll P^2\sum_s|w_s|^2B^{o(1)}.
\]

The missing input is precisely

\[
E_D\ll B^{o(1)}\sum_s|w_s|^2.
\tag{H16.13}
\]

For physical unit weights, (H16.13) is the Shared-U squareclass-energy theorem itself.

Hence:

```text
QUADRATIC_RECIPROCITY_PROJECTION_PROVED=true
TH14_R2_PRODUCT_ROW_QUADRATIC_LARGE_SIEVE_IMPORT_VALID=true
QUADRATIC_LARGE_SIEVE_CLOSES_T58_TARGET=false
QUADRATIC_LARGE_SIEVE_FAILURE=unknown weighted squareclass-fiber energy E_D
```

Goldmakher–Louvel's quadratic large sieve over number fields is compatible with a certified quadratic Hecke-family reduction, but it has the same coefficient-energy issue: it does not distinguish two physical states carrying the same quadratic character.

---

## 4. Same-modulus Mellin large sieve: why the obvious full-mode argument loses a power

The safe t57 representation (H16.3) avoids squareclass collapse, so one may try to sum over all multiplicative mode pairs and use character orthogonality.

For one prime `p`, a generic mode sum has the form

\[
S_p(\alpha,\beta)
=\sum_s a_s\alpha(t_s)\beta(x_s),
\tag{H16.14}
\]

with `alpha,beta` characters modulo the **same** prime `p`.

Summing over the full character-pair basis gives the exact residue-collision identity

\[
\sum_{\alpha,\beta}|S_p(\alpha,\beta)|^2
=(p-1)^2
\sum_{\rho}
\left|\sum_{s:(t_s,x_s)\equiv\rho\bmod p}a_s\right|^2.
\tag{H16.15}
\]

Even if the residue map is injective, (H16.15) has size

\[
\asymp p^2\sum_s|a_s|^2.
\tag{H16.16}
\]

Because the normalized Kummer coefficient vector in (H16.3) has `L2` norm only `O(1)`, plain Cauchy against the full mode basis retains the `p^2` factor. For two primes the tensor mode universe has size `~p^2q^2`, producing a fixed-power overhead on the `L^4` scale before the auxiliary-pair average.

Thus the missing theorem is not ordinary character orthogonality and not an unrestricted two-coordinate multiplicative large sieve. It must exploit the special Kummer coefficient packet **and** the actual canonical-prime/`delta` physical incidence simultaneously.

Baier–Bansal's Gaussian sparse-moduli large sieve concerns additive fractions with Gaussian moduli satisfying distribution hypotheses. It does not directly supply (H16.1), whose kernel is multiplicative, bivariate, same-modulus, and evaluated on a sharp physical hyperbola.

Hence:

```text
FULL_MODE_ORTHOGONALITY_CLOSES_TARGET=false
NAIVE_SAME_MODULUS_MELLIN_CAUCHY_FIXED_POWER_LOSS=L^4_per_two_prime_packet
GAUSSIAN_ADDITIVE_SPARSE_MODULI_LARGE_SIEVE_DIRECT_IMPORT_VALID=false
```

---

## 5. Reciprocity in the Gaussian variables does not produce a separated FI/Jacobi kernel

A stronger hope is to move the quadratic symbol from the external auxiliary prime onto one of the physical Gaussian variables and obtain a separated symbol such as

\[
\alpha(\pi)\beta(V)\left(\frac{V}{\pi}\right)_{\mathbf Z[i]}
\]

or a rational radial Jacobi symbol

\[
\alpha(\ell)\beta(\delta)\left(\frac{d(\delta)}{\ell}\right).
\]

The current exact kernel does not admit either identity.

The t57 factorization

\[
K_p(t,x)=A_p(x/t)A_p(tx)
\]

mixes the canonical direction slope and the `V` slope in both factors. Fixing `U` only turns its action into a fixed projective reparameterization; it does not separate the two moving variables.

This is the same separation failure already audited in t39/tH15 for the Friedlander–Iwaniec Gaussian-symbol route. The toroidal change of variables makes the local Kummer geometry transparent but does not manufacture a Gaussian residue symbol between `pi` and `V`.

Therefore:

```text
DIRECT_GAUSSIAN_RECIPROCITY_SEPARATION_PROVED=false
DIRECT_FI_GAUSSIAN_SYMBOL_IMPORT_VALID=false
```

A future proof may still construct a **multi-term bounded-energy reciprocity decomposition**, but that is a new theorem, not a consequence of quadratic reciprocity alone.

---

## 6. Hyperbolic Jacobi bilinear theorem: geometry matches, kernel does not

The sharp radial support

\[
\ell\delta\le Y_U
\]

has exactly the geometric shape treated by hyperbolic bilinear methods. Cameron Wilson's theorem studies sums over

\[
nm\le T
\]

with kernel

\[
\left(\frac{n}{m}\right),
\]

for odd squarefree variables, with additional care required near the coordinate axes.

The t58 packet satisfies only the **region** part of that template:

- `ell` is a prime, hence squarefree;
- `delta` is not known to be squarefree;
- the toroidal kernel depends on angular representatives `pi,V`, not only on radial norms `ell,delta`;
- its quadratic modulus is the external auxiliary prime `p` (or `pq`), not the canonical prime `ell`;
- small-`delta` axis packets are present and cannot be discarded without a separate estimate.

Thus no exact identity of the form

\[
K_{pq}(t_s,x_s)
=a_{pq}(\ell_s)b_{pq}(\delta_s)
\left(\frac{d(\delta_s)}{\ell_s}\right)
\tag{H16.17}
\]

has been proved.

Wilson's hyperbolic machinery cannot be imported until such a kernel bridge and the `delta` squarepart/axis coefficient-energy ledger are certified.

```text
HYPERBOLIC_REGION_GEOMETRY_COMPATIBLE=true
HYPERBOLIC_JACOBI_KERNEL_IDENTITY_PROVED=false
DELTA_SQUAREFREE_REQUIRED_BY_DIRECT_WILSON_IMPORT=true
DELTA_SQUAREFREE_ON_PHYSICAL_PACKET=false
AXIS_PACKET_SEPARATE_CONTROL_REQUIRED=true
WILSON_HYPERBOLIC_BILINEAR_DIRECT_IMPORT_VALID=false
```

---

## 7. Exact new adapter contracts

The independent audit leaves two possible non-circular future routes.

### Route A — SameModulusToroidalKummerLargeSieve (SMTKLS)

A direct theorem may work in the original physical coefficient space:

> For every fixed `U,epsilon,k` physical packet on `ell*delta<=Y_U`, with t58 `B^{o(1)}` radial-cell energy and t57 Kummer packet, prove
>
> \[
> \sum_{p\ne q}|\sum_s w_sK_p(s)K_q(s)|^2
> \ll P^2B^{o(1)}\sum_s|w_s|^2.
> \tag{H16.18}
> \]
>
> The proof must use the special Kummer spectral coefficients rather than full-mode Cauchy and must keep the same modulus on both toroidal coordinates.

This is essentially the minimal same-modulus theorem requested by t58, now with the failure mechanism (H16.15) explicitly excluded.

### Route B — ToroidalHyperbolicJacobiBridge (THJB)

To legally use Wilson/Heath-Brown hyperbolic Jacobi technology, it is sufficient to prove a decomposition, on every dyadic physical hyperbola packet,

\[
K_{pq}(s)
=\sum_{\nu} c_{\nu,pq}
 a_{\nu,pq}(\pi_s)
 b_{\nu,pq}(V_s)
 \left(\frac{d_{\nu}(\delta_s)}{\ell_s}\right)
 +\mathcal E_{pq}(s),
\tag{H16.19}
\]

such that

```text
sum_nu |c_nu,pq|^2 <= B^o(1)
|a_nu,pq|, |b_nu,pq| <= 1
d_nu(delta) is odd squarefree on the routed main slice
delta-squarepart lift has B^o(1) coefficient-energy cost
small-axis and exceptional mass is already target-scale
sum_{p!=q}|sum_s w_s E_pq(s)|^2 <= P^2 B^o(1) sum_s|w_s|^2
```

Only after (H16.19) is proved is the hyperbolic Jacobi theorem a candidate receiver. No such bridge is currently certified.

A Gaussian analogue replacing the rational Jacobi symbol by a separated Gaussian quadratic residue symbol is equally acceptable, provided its coefficient separation and ray-class conductor are proved with `B^{o(1)}` energy cost.

---

## 8. Impossibility guard: coefficient-energy roadworks alone cannot prove the theorem

Suppose `r` distinct physical states lie in distinct radial/residue cells but have the same nonzero squareclass. Then for every good auxiliary pair `(p,q)`,

\[
K_{pq}(s_1)=\cdots=K_{pq}(s_r).
\]

With unit weights,

\[
\sum_s|w_s|^2=r,
\]

but

\[
\sum_{p\ne q}\left|\sum_{j=1}^r K_{pq}(s_j)\right|^2
=P(P-1)r^2.
\tag{H16.20}
\]

Thus t58's `B^{o(1)}` radial-cell multiplicity and t57's bounded Mellin spectral energy are not, by themselves, sufficient to prove (H16.1). A successful theorem must use genuine arithmetic non-correlation of the physical canonical-prime/`delta` incidence.

This also explains why reciprocity plus a quadratic large sieve cannot avoid the squareclass coefficient energy: identical squareclasses are literally identical character rows.

---

## 9. Critical exponent ledger

Write

\[
N(U)=B^{u+o(1)}.
\]

Then

\[
Y_U=\frac{2B}{\varepsilon N(U)}=B^{1-u+o(1)}.
\tag{H16.21}
\]

On the critical canonical-prime strip

\[
\ell=B^{1/2+o(1)},
\]

so

\[
\delta\le B^{1/2-u+o(1)}.
\tag{H16.22}
\]

Let the auxiliary scale be

\[
p,q\asymp L=B^{\rho+o(1)},\qquad P=B^{\rho+o(1)}.
\]

The desired fixed-`U` second moment has exponent

\[
2\rho+e_w,
\]

where

\[
\sum_s|w_s|^2=B^{e_w+o(1)}.
\]

For the reciprocity/QLS route, if the discriminant range is `K=B^{d+o(1)}`, the conductor cost is harmless only when

\[
2\rho\ge d.
\]

Even then the exponent is controlled by `E_D`, not by `e_w`; the missing squareclass-energy exponent is not removed.

For the naive full Mellin-mode Cauchy route, a two-prime packet pays an extra `L^4=B^{4\rho}` spectral-universe factor in the worst safe orthogonality bound, so it is not a zero-fixed-loss receiver.

Any successful SMTKLS/THJB route must have fixed-power loss

\[
\boxed{\omega=0.}
\tag{H16.23}
\]

relative to `P^2 sum|w|^2`.

---

## 10. Direct handoff to Stage14-t59 / t60

Downstream may import the following.

```text
SharedUCanonicalPrimeDeltaToroidalSecondMomentAudit:
  exact_kernel:
    K_p(t,x) = A_p(x/t) A_p(tx)
    mellin_packet_L2_energy <= 1
    same_modulus_on_t_and_x = true

  reciprocity:
    Delta_s = (B^2 P^2-A^2 Q^2)(B^2 Q^2-A^2 P^2)
    K_r(s) = (Delta_s/r) = chi_Ds(r) on the good refined slice
    tH14_R2_product_row_QLS = valid
    coefficient_energy_after_D_collapse = unresolved fixed-U squareclass energy
    closes_target = false

  same_modulus_large_sieve:
    full_mode_orthogonality = exact residue-collision identity
    naive_mode_Cauchy = loses L^4 per two-prime packet
    known_direct_zero-loss_theorem = none certified

  hyperbolic_bilinear:
    ell*delta hyperbola = compatible geometry
    exact Jacobi kernel in (ell,delta) = not proved
    delta squarefree = not guaranteed
    small-delta axis = separate obligation
    Wilson direct import = false

  acceptable_new_theorems:
    SameModulusToroidalKummerLargeSieve = H16.18
    ToroidalHyperbolicJacobiBridge = H16.19

  forbidden:
    pair_to_cross_kernel_before_cancellation = true
    E4_as_coefficient_energy = true
    squareclass_energy_assumed_near_linear = true
    independent_pi_V_modulus_tensorization = true
    complete_or_full_mode_orthogonality_implies_physical_selector_cancellation = true
```

The preferred next attack is arithmetic: either prove the direct same-modulus Kummer frame (H16.18), or exhibit a separated reciprocity/Jacobi decomposition of the actual toroidal kernel satisfying (H16.19). Re-running generic quadratic large sieve after squareclass collapse is not progress.

---

## Literature audit

Primary sources used only to test theorem hypotheses:

- L. Goldmakher and B. Louvel, *A quadratic large sieve inequality over number fields*, arXiv:1112.1642. Quadratic Hecke-family large sieve; applicable after a legal quadratic-character reduction, but it does not remove coefficient collisions among identical characters.
- S. Baier and A. Bansal, *Large sieve with sparse sets of moduli for Z[i]*, arXiv:1811.07300. Gaussian additive large sieve with distribution hypotheses on sparse moduli; not a direct multiplicative toroidal receiver.
- C. Wilson, *General Bilinear Forms In The Jacobi Symbol Over Hyperbolic Regions*, arXiv:2208.14909. Hyperbolic `nm<=T` Jacobi-symbol cancellation for odd squarefree variables, with axis restrictions; region geometry is relevant but the t58 kernel identity is absent.
- J. Friedlander and H. Iwaniec, *The polynomial X^2+Y^4 captures its primes*, arXiv:math/9811185 / Ann. of Math. 148 (1998). Gaussian spin/Jacobi-symbol machinery remains an orientation point; the Stage14 fixed-`U` toroidal kernel has no certified separated FI-symbol identity.

No literature result is promoted to a proof of (H16.1).

---

## Locked boundary

```text
STAGE14_TH16=COMPLETE_CANONICAL_PRIME_DELTA_TOROIDAL_SECOND_MOMENT_APPLICABILITY_AUDIT
MERGED_T57_IMPORTED=true
MERGED_T58_IMPORTED=true
MERGED_TH14_R2_IMPORTED=true
T58_RADIAL_CELL_ENERGY_TRANSFER_USED=true
T57_MELLIN_PACKET_L2_ENERGY_USED=true
QUADRATIC_RECIPROCITY_PROJECTION_PROVED=true
TH14_R2_PRODUCT_ROW_QUADRATIC_LARGE_SIEVE_IMPORT_VALID=true
QUADRATIC_LARGE_SIEVE_CLOSES_T58_TARGET=false
QUADRATIC_LARGE_SIEVE_FAILURE_IS_SQUARECLASS_COEFFICIENT_ENERGY=true
FULL_MODE_ORTHOGONALITY_IDENTITY_PROVED=true
NAIVE_SAME_MODULUS_MELLIN_CAUCHY_CLOSES_TARGET=false
GAUSSIAN_ADDITIVE_SPARSE_MODULI_LARGE_SIEVE_DIRECT_IMPORT_VALID=false
DIRECT_GAUSSIAN_RECIPROCITY_SEPARATION_PROVED=false
DIRECT_FI_GAUSSIAN_SYMBOL_IMPORT_VALID=false
HYPERBOLIC_REGION_GEOMETRY_COMPATIBLE=true
HYPERBOLIC_JACOBI_KERNEL_IDENTITY_PROVED=false
DELTA_SQUAREFREE_ON_PHYSICAL_PACKET=false
WILSON_HYPERBOLIC_BILINEAR_DIRECT_IMPORT_VALID=false
SAME_MODULUS_TOROIDAL_KUMMER_LARGE_SIEVE_DEFINED=true
SAME_MODULUS_TOROIDAL_KUMMER_LARGE_SIEVE_PROVED=false
TOROIDAL_HYPERBOLIC_JACOBI_BRIDGE_DEFINED=true
TOROIDAL_HYPERBOLIC_JACOBI_BRIDGE_PROVED=false
PAIR_COLLAPSE_BEFORE_PHYSICAL_CANCELLATION_ALLOWED=false
E4_COEFFICIENT_ENERGY_USED=false
SHARED_U_CANONICAL_PRIME_DELTA_TOROIDAL_SECOND_MOMENT_PROVED=false
SHARED_U_PHYSICAL_TOROIDAL_MELLIN_CORRELATION_PROVED=false
SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED=false
GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
MINIMAL_REMAINING_OBSTRUCTION=SameModulusToroidalKummerLargeSieve_or_ToroidalHyperbolicJacobiBridge
NEXT=Stage14-t59 consume the tH16 no-import boundary; attack the actual canonical-prime/delta arithmetic rather than repeating quadratic large sieve after squareclass collapse
```
