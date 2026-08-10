# Stage14-t58 — toroidal reconstruction masks and radial-cell energy transfer

## Purpose

Merged Stage14-t57 reduces the dominant fixed-`U` invisible packet to the exact rank-one toroidal Kummer/Mellin correlation

\[
\sum_{p\ne q}|\langle b_{U,pq},K_{pq}\rangle|^2
\ll R_U P^2 B^{o(1)},
\]

with

\[
K_p(t,x)=A_p(x/t)A_p(tx),\qquad A_p(z)=\chi_p(z^2-1).
\]

The only unresolved gate after t57 is the actual physical selector. Stage14-t58 asks whether the interval/reconstruction/canonical/divisor masks can be transferred into the toroidal packet with only `B^{o(1)}` coefficient-energy cost, or whether a new polynomial mask-correlation obstruction remains.

The answer is favorable at the support-energy level: the cross-angular physical chamber becomes exactly separated in the toroidal variables, all other masks are one-side or radial, and each fixed radial `(ell,delta)` cell has only divisor-bounded angular multiplicity. The full physical support is **not** a Cartesian product, so this does not prove the required second moment. It removes the mask-energy adapter and isolates one sharper analytic theorem.

No global Stage14 power saving is claimed.

---

## 1. Physical reconstruction chamber becomes toroidally separated

Write, on the positive physical chart,

\[
t=\frac ab,\qquad x=\frac pq,
\]

and use the t57 ratio/product variables

\[
u=\frac{x}{t},\qquad v=tx.
\]

The physical reconstruction inequalities in the frozen/live parameterization are

\[
a q<b p,\qquad a p<b q.
\]

Since `a,b,p,q>0`, these are exactly

\[
t<x,\qquad tx<1.
\]

Hence

\[
\boxed{t<x<1/t\iff u>1\ \text{and}\ 0<v<1.}
\tag{58.1}
\]

Thus the only explicit cross-angular interval condition factors as

\[
\boxed{{\bf1}_{\rm chamber}(u,v)
={\bf1}_{u>1}{\bf1}_{0<v<1}.}
\tag{58.2}
\]

The inverse square relations are also exact:

\[
\boxed{t^2=v/u,\qquad x^2=uv.}
\tag{58.3}
\]

The square-root compatibility is not an extra uncontrolled mode condition. In t57 the nonzero Mellin modes arise from pairs `(eta,xi)` and the induced toroidal characters have exponent combinations corresponding to `xi eta^{-1}` and `eta xi`; the evenness of `A_p` already removes the incompatible odd modes.

The deterministic audit verifies (58.1)--(58.3) on all 560 reciprocal frozen states.

```text
PHYSICAL_INTERVAL_TOROIDAL_SEPARATION_PROVED=true
TOROIDAL_INVERSE_SQUARE_COMPATIBILITY_PROVED=true
```

---

## 2. Classification of the remaining physical masks

After fixing primitive `U`, finite `epsilon`, divisor-fan `k`, and the invisible branch, the other masks have a simpler ownership structure.

### Canonical prime

The canonical Gaussian prime `pi` and its rational norm `ell=N(pi)` are selected from the direction data `a+ib=pi U`. Therefore the largest-prime/canonical condition depends on the `pi`/direction side only; it does not inspect `V`.

```text
CANONICAL_MASK_PI_SIDE_ONLY=true
```

### Primitive cover variable

Primitivity/orientation of `V` is a `V`-side condition. It can be retained as a bounded zero-one coefficient mask.

### Invisible branch

On the invisible branch,

\[
N(V)=n=k\delta
\]

and the defining condition is

\[
\ell\nmid N(V).
\]

Thus

\[
\boxed{\ell\nmid k\delta}
\tag{58.4}
\]

is a radial norm-index condition; it carries no new angular coupling.

```text
INVISIBLE_BRANCH_MASK_RADIAL_ONLY=true
```

### Physical size/hyperbola

The exact reconstruction budget is

\[
\boxed{\frac{\varepsilon\ell N(U)\delta}{2}\le B.}
\tag{58.5}
\]

For fixed `U` and `epsilon`, this is the sharp two-variable radial product cutoff

\[
\ell\delta\le Y_U,
\qquad
Y_U=\frac{2B}{\varepsilon N(U)}.
\tag{58.6}
\]

Stage14-tH2 already freezes the correct policy: retain the sharp product cutoff, use exact hyperbola identities/dyadic blocks, and never replace it by a Cartesian box for a signed character sum without an error term.

```text
SHARP_HYPERBOLA_MASK_RADIAL_ONLY=true
SHARP_HYPERBOLA_RECTANGULARIZED_WITHOUT_ERROR=false
```

### Auxiliary bad-prime and finite branch masks

These remain bounded zero-one masks. By the tH4 coefficient theorem they do not increase source `L2` energy. This is an energy statement only; it does not manufacture cancellation.

---

## 3. Radial cells have only `B^{o(1)}` angular multiplicity

Fix

```text
primitive U,
epsilon,
k,
ell=N(pi),
delta,
invisible branch.
```

Call this a radial cell. Its angular freedom comes from:

1. Gaussian representatives of the canonical split prime `pi`, with `N(pi)=ell`;
2. primitive Gaussian representatives `V` with
   \[
   N(V)=k\delta;
   \]
3. a finite branch/orientation label.

For a split rational prime `ell`,

\[
r_2(\ell)=8.
\]

For the cover norm,

\[
r_2(k\delta)\le4\tau(k\delta)=(k\delta)^{o(1)}.
\]

Therefore the physical angular multiplicity of one radial cell satisfies

\[
\boxed{M_{U,\varepsilon,k}(\ell,\delta)\ll \tau(k\delta)=B^{o(1)}.}
\tag{58.7}
\]

This is uniform in the critical fixed-`U` family.

The frozen reciprocal invisible family has

```text
states                         419
radial cells                   408
cell multiplicity 1            397
cell multiplicity 2             11
max frozen cell                  2
radial-cell collision energy   441
```

These finite numbers are diagnostics only; the asymptotic theorem is (58.7).

---

## 4. Weighted support-energy transfer is near-linear

Let `C` run over radial cells and let `w_s` be arbitrary coefficients carrying all bounded physical masks. Let `phi_s` be any unit-modulus auxiliary/Mellin phase, possibly depending on the active modulus/mode. For each cell define

\[
A_C=\sum_{s\in C}w_s\phi_s.
\]

Cellwise Cauchy gives

\[
|A_C|^2
\le |C|\sum_{s\in C}|w_s|^2.
\]

Using (58.7) and summing over cells,

\[
\boxed{
\sum_C|A_C|^2
\ll B^{o(1)}\sum_s|w_s|^2.
}
\tag{58.8}
\]

Crucially, no Cauchy is taken over the **number of radial cells**. The only loss is the maximum cell multiplicity, which is divisor-bounded. This is exactly the quantifier-safe support-energy transfer that toolbox-as/t57 left open.

Merged tH4 already proves bounded masks/phases are `L2`-safe, and merged tH5 proves exact paired Gaussian coefficient collisions cost only `B^{o(1)}`. Equation (58.8) is the fixed-`U` radial specialization compatible with those roadworks.

Therefore

```text
FIXED_U_PHYSICAL_SELECTOR_SUPPORT_ENERGY_TRANSFER_PROVED=true
PHYSICAL_RADIAL_CELL_MULTIPLICITY_B_O1=true
```

This statement does **not** say the selector is equidistributed modulo the auxiliary primes. It says only that its physical masks and lift multiplicities no longer create a polynomial coefficient-energy obstruction before the analytic second moment is applied.

---

## 5. Why this still does not make the selector Cartesian

The chamber itself factors in `(u,v)`, but the actual arithmetic support does not become one product set.

A frozen invisible fixed-`U` fiber with unit key `U=(-1,0)` contains the three toroidal points

\[
(15/8,1/30),\qquad
(40/3,1/30),\qquad
(15/8,2/15),
\]

but not

\[
(40/3,2/15).
\]

Thus one `2x2` support rectangle has the exact pattern

```text
1 1
1 0
```

(up to row/column ordering). A single Cartesian-product selector would have rectangular support and cannot realize this pattern.

```text
FULL_PHYSICAL_SELECTOR_SINGLE_CARTESIAN_PRODUCT=false
```

So t58 does not tensorize `pi` and `V`, does not apply separate one-variable estimates as if the selector were a product, and does not revive the t54 Latin-square error.

---

## 6. New minimal analytic receiver

After (58.1)--(58.8), the physical-mask adapter is no longer the obstruction. What remains is a same-modulus two-coordinate second moment on a sharp canonical-prime/`delta` hyperbola with only `B^{o(1)}` angular fibers.

Define

```text
SharedUCanonicalPrimeDeltaToroidalSecondMoment
```

as the uniform theorem which, for fixed primitive `U`, finite `epsilon`, divisor-fan `k`, and invisible branch, controls

\[
\boxed{
\sum_{p\ne q}
\left|
\sum_{\substack{\ell\delta\le Y_U\\
\ell\ \mathrm{canonical\ split\ prime}}}
\sum_{s\in C_U(\ell,\delta)}
 w_s\,K_{pq}(t_s,x_s)
\right|^2
\ll
P^2 B^{o(1)}\sum_s|w_s|^2.
}
\tag{58.9}
\]

Here:

- the sharp `ell*delta` cutoff is retained;
- every cell has `B^{o(1)}` angular lifts;
- `K_{pq}` is the exact t57 rank-one toroidal kernel;
- all canonical, branch, primitive, interval, reconstruction and bad-prime masks are already encoded in the `L2`-safe coefficients;
- the same physical state is used at both auxiliary primes;
- independent `pi/V` modulus tensorization is forbidden.

If (58.9) is proved, then t57 gives `SharedUPhysicalToroidalMellinCorrelation`, t56 gives invisible SUBD, and tH15 gives near-linear invisible fixed-`U` squareclass energy.

The theorem (58.9) is strictly narrower than the t57 receiver: mask decomposition and support-energy transfer are now proved inputs rather than theorem obligations.

```text
SHARED_U_CANONICAL_PRIME_DELTA_TOROIDAL_SECOND_MOMENT_PROVED=false
SHARED_U_PHYSICAL_TOROIDAL_MELLIN_CORRELATION_PROVED=false
```

---

## 7. Mixed branch remains separate

Nothing in t58 addresses the invisible/visible mixed shared-`U` block. Its centered dispersion remains a separate explicit obligation. Frozen multiplicity is not an asymptotic negligibility theorem.

```text
SHARED_U_MIXED_BRANCH_DISPERSION_PROVED=false
```

---

## 8. tH decision

Stage14-t58 creates a new concrete support-stage trigger.

At t57 the residual was still the broad receiver-specific phrase “physical toroidal Mellin correlation”, so a new H-line would have duplicated existing infrastructure. After t58, all mask/lift obligations are removed and the missing analytic object is the sharply specified same-modulus theorem (58.9) on a canonical-prime/`delta` sharp hyperbola.

Merged tH4 explicitly leaves

```text
SAME_MODULUS_JOINT_SECOND_MOMENT_THEOREM_PROVED=false
```

and t58 now supplies the exact packet on which such a theorem is needed. Therefore a parallel support line is justified:

```text
TH16_NEEDED=true
```

### Requested tH16 task

`Stage14-tH16` should independently attack

```text
SharedUCanonicalPrimeDeltaToroidalSecondMoment
```

by testing same-modulus multiplicative/trace large-sieve, Gaussian/rational-slope reciprocity, prime-`delta` hyperbolic bilinear, and spectral large-sieve routes against the exact t58 packet. It must preserve the common auxiliary modulus, sharp `ell*delta` cutoff, centered two-prime assembly, and `B^{o(1)}` angular-cell coefficient energy. It should either prove a usable theorem/adapter or return a precise conductor/energy failure boundary.

The live t route need not wait:

```text
T_ROUTE_BLOCKED_WAITING_FOR_TH16=false
```

Stage14-t59 may directly exploit arithmetic of the canonical-prime/`delta` packet in parallel.

---

## Locked boundary

```text
STAGE14_T58=COMPLETE_TOROIDAL_RECONSTRUCTION_MASK_SEPARATION_AND_RADIAL_CELL_ENERGY_TRANSFER
MERGED_T57_IMPORTED=true
PHYSICAL_INTERVAL_TOROIDAL_SEPARATION_PROVED=true
TOROIDAL_INVERSE_SQUARE_COMPATIBILITY_PROVED=true
CANONICAL_MASK_PI_SIDE_ONLY=true
INVISIBLE_BRANCH_MASK_RADIAL_ONLY=true
SHARP_HYPERBOLA_MASK_RADIAL_ONLY=true
PHYSICAL_RADIAL_CELL_MULTIPLICITY_B_O1=true
FIXED_U_PHYSICAL_SELECTOR_SUPPORT_ENERGY_TRANSFER_PROVED=true
FULL_PHYSICAL_SELECTOR_SINGLE_CARTESIAN_PRODUCT=false
SHARED_U_CANONICAL_PRIME_DELTA_TOROIDAL_SECOND_MOMENT_PROVED=false
SHARED_U_PHYSICAL_TOROIDAL_MELLIN_CORRELATION_PROVED=false
SHARED_U_CENTERED_PROJECTIVE_SELECTOR_DISPERSION_PROVED=false
SHARED_U_MIXED_BRANCH_DISPERSION_PROVED=false
SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED=false
GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false
GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
TH16_NEEDED=true
TH16_REQUESTED_OBJECT=SharedUCanonicalPrimeDeltaToroidalSecondMoment
T_ROUTE_BLOCKED_WAITING_FOR_TH16=false
NEXT=Stage14-t59 attack SharedUCanonicalPrimeDeltaToroidalSecondMoment on the sharp ell*delta hyperbola; run Stage14-tH16 in parallel
```
