# Stage14-tH4 — weighted Mellin / Hecke large-sieve transfer toolbox

## Purpose

Stage14-tH3 produced a canonical `GaussianSpectralHyperbolaPacket` which preserves

- arbitrary local Mellin character order;
- exact Gaussian/ray-class conductor data;
- the `mu_4`-trivial fast path with no ramified `(1+i)` conductor;
- tH2 divisor-coupled hyperbola coordinates;
- the fact that `U` and `V` may use the same auxiliary Gaussian prime modulus.

Stage14-tH4 builds the reusable **weighted transfer layer** between that packet and any later one-variable or same-modulus large-sieve / dispersion theorem.

The problem solved here is not the base large sieve itself.  The problem is to prove that the extra weights which actually occur in Stage14 — Mellin spectral coefficients, smooth cutoffs, phase twists, good-prime masks, divisor lifts, conductor bands and dyadic decompositions — do not silently consume a fixed power.

The output is deliberately theorem-agnostic.  If a later analytic theorem supplies a second-moment bound with constant `Delta`, tH4 tells exactly how much of `Delta` survives after all roadworks weights are inserted.

No future live `t` result is required.

---

## 1. Abstract base second-moment interface

Let `F(Q)` be any finite family of Gaussian residue/ray-class characters, or any other spectral family indexed by conductors in one tH3 conductor band.  Assume an analytic theorem gives

\[
\boxed{
\sum_{\chi\in F(Q)}
\left|\sum_z a_z\chi(z)\right|^2
\le
\Delta(Z,Q)\sum_z|a_z|^2.
}
\tag{H4.1}
\]

The precise formula for `Delta` is **not** part of tH4.

Examples include a Gaussian additive/multiplicative large sieve with `Delta=Z+Q^2`, but tH4 does not need to import or reprove that theorem.

The contract is simply

```text
analytic input  = second moment Delta * coefficient L2 energy
roadworks task  = track every extra weight before the analytic theorem is called.
```

---

## 2. Coefficient masks, smooth cutoffs and Mellin phases are L2-safe

Let

\[
b_z=a_z\,M_z\,W_z\,e^{i\phi_z},
\]

where

```text
M_z in {0,1},
|W_z| <= 1,
phi_z real.
```

Then pointwise

\[
|b_z|\le|a_z|,
\]

and therefore

\[
\boxed{
\sum_z|b_z|^2\le\sum_z|a_z|^2.
}
\tag{H4.2}
\]

Thus all of the following are free at the polynomial-exponent level:

- tH3 good-prime masks such as `gcd(Q_rat,g*h*r*delta)=1`;
- bounded smooth dyadic cutoffs;
- unit-modulus Mellin twists `N(z)^{it}`;
- fixed Gaussian unit/orientation phases;
- visibility labels implemented by zero-one restriction.

Consequently (H4.1) remains valid with `a_z` replaced by any such weighted `b_z` with the **same** `Delta`.

```text
GOOD_PRIME_MASK_L2_COST=1
BOUNDED_SMOOTH_WEIGHT_L2_COST<=1
UNIT_MODULUS_MELLIN_PHASE_L2_COST=1
```

---

## 3. Spectral packet aggregation costs exactly its L2 energy

For one modulus group, let `theta` denote the allowed local/all-order character modes and let

\[
M_\theta=\sum_z a_z\theta(z).
\]

Suppose the Stage14 local trace or Mellin decomposition provides coefficients `c_theta`.  Put

\[
E_{\rm spec}=\sum_\theta|c_\theta|^2.
\]

Then Cauchy gives the exact Hilbert-space inequality

\[
\boxed{
\left|\sum_\theta c_\theta M_\theta\right|^2
\le
E_{\rm spec}
\sum_\theta|M_\theta|^2.
}
\tag{H4.3}
\]

Hence any base second-moment theorem for the full character family immediately transfers to a weighted Mellin packet at the multiplicative cost `E_spec`.

In particular, if

\[
E_{\rm spec}=O(1),
\]

then the spectral aggregation costs no fixed power.

The same statement applies to a two-coordinate packet at one **shared** tH3 modulus group:

\[
\boxed{
\left|
\sum_{\xi,\zeta}
C(\xi,\zeta)M(\xi,\zeta)
\right|^2
\le
\left(\sum_{\xi,\zeta}|C(\xi,\zeta)|^2\right)
\left(\sum_{\xi,\zeta}|M(\xi,\zeta)|^2\right).
}
\tag{H4.4}
\]

Crucially, (H4.4) does **not** replace the shared modulus by independent `U` and `V` moduli.

```text
SPECTRAL_PACKET_COST=EXACT_L2_ENERGY
BOUNDED_SPECTRAL_ENERGY_FIXED_POWER_LOSS=false
SHARED_MODULUS_PACKET_CAUCHY_PRESERVES_MODULUS_GROUP=true
```

---

## 4. Divisor lift from tH2 costs at most one divisor function

The tH2 norm engine uses

\[
N(U)=hr,
\qquad (h,c)=1
\]

for a fixed finite state `c=epsilon/g`.

Let `w(h,r)` be arbitrary complex weights supported on `hr<=Y`, and define the norm-collapsed coefficient

\[
A_c(n)
=
\sum_{\substack{hr=n\\(h,c)=1}}w(h,r).
\]

Let

\[
\mu_c(n)
=
\#\{h\mid n:(h,c)=1\}.
\]

Then

\[
\mu_c(n)\le\tau(n).
\]

By Cauchy on each norm fiber,

\[
|A_c(n)|^2
\le
\mu_c(n)
\sum_{\substack{hr=n\\(h,c)=1}}|w(h,r)|^2.
\]

Summing over `n<=Y`,

\[
\boxed{
\sum_{n\le Y}|A_c(n)|^2
\le
\tau_{\max}(Y)
\sum_{\substack{hr\le Y\\(h,c)=1}}|w(h,r)|^2,
}
\tag{H4.5}
\]

where

\[
\tau_{\max}(Y)=\max_{n\le Y}\tau(n)=Y^{o(1)}.
\]

Thus collapsing the exact tH2 factorisation into one Gaussian norm index costs only `Y^o(1)`.

The same argument applies to `N(V)=gh\delta` after the fixed finite state `g` is removed: the nonconstant factorisation multiplicity is again divisor-bounded.

```text
DIVISOR_LIFT_L2_COST=tau_max(Y)
DIVISOR_LIFT_FIXED_POWER_LOSS=false
```

This is a coefficient-norm statement only.  Correlations between **both** norm coordinates are reserved for tH5.

---

## 5. Gaussian representation lift is also subpolynomial at the multiplicity level

For a positive integer `n`, the number of integral Gaussian elements of norm `n` satisfies

\[
r_2(n)\le4\tau(n).
\]

If one first constructs a norm coefficient `A(n)` and then distributes it among Gaussian representatives with bounded per-representative weights, the representation multiplicity contributes at most another divisor factor.

At the polynomial-exponent level,

\[
\boxed{
r_2(n)=n^{o(1)}.}
\tag{H4.6}
\]

Therefore the combination

```text
divisor lift -> Gaussian norm -> Gaussian representatives
```

has no fixed-power multiplicity cost.

This does **not** prove that two different hyperbola tuples cannot land on the same spectral coefficient after all Stage14 labels are imposed.  That collision/energy problem remains the planned tH5 task.

```text
GAUSSIAN_REPRESENTATION_LIFT_FIXED_POWER_LOSS=false
FULL_COEFFICIENT_COLLISION_ENERGY_PROVED=false
```

---

## 6. Conductor bands and dyadic blocks cost only polylogarithms

Let the joint tH3 modulus envelope satisfy

\[
N\mathfrak q\le Q_{\max}.
\]

Partition conductors into dyadic bands

\[
Q\le N\mathfrak q<2Q.
\]

There are

\[
O(\log(2Q_{\max}))
\]

such bands.

Likewise tH2 supplies dyadic hyperbola blocks `(H,R,D)` with only polylogarithmically many active blocks.

If

\[
S=\sum_{j=1}^{J}S_j,
\]

then

\[
\boxed{
|S|^2\le J\sum_{j=1}^{J}|S_j|^2.
}
\tag{H4.7}
\]

Thus summing the final amplitude over `J=(log B)^{O(1)}` roadworks pieces costs only `B^{o(1)}`.

No dyadic partition may be silently charged as a fixed exponent.

```text
CONDUCTOR_BAND_COUNT=polylogarithmic
HYPERBOLA_BLOCK_COUNT=polylogarithmic
BLOCK_RECOMBINATION_FIXED_POWER_LOSS=false
```

---

## 7. Smooth Mellin/Perron decomposition has an explicit kernel budget

Suppose a smooth cutoff is represented by a Mellin integral

\[
W(x)
=
\frac1{2\pi}
\int_{\mathbf R}
\widehat W(t)x^{-it}\,dt
\]

on the chosen vertical line, and define

\[
K_W
=
\frac1{2\pi}
\int_{\mathbf R}|\widehat W(t)|\,dt.
\]

Since `x^{-it}` has modulus one, any uniform second-moment estimate for the twisted coefficient sequence transfers by Minkowski/Cauchy with at most

\[
\boxed{K_W^2}
\tag{H4.8}
\]

in squared norm.

Thus tH4 does **not** declare smooth Mellin inversion free.  It exposes the exact analytic budget which a later stage must bound.

For a fixed smooth partition with derivative norms independent of `B`, one expects `K_W=O(1)`; if a later stage chooses a `B`-dependent sharp approximation, its growth must be recorded explicitly.

```text
MELLIN_KERNEL_COST=K_W^2
SHARP_TO_SMOOTH_COST_HIDDEN=false
```

---

## 8. Weighted one-variable large-sieve transfer theorem

Combining sections 2--7 gives the reusable theorem.

Assume the base family satisfies (H4.1).  Let the actual coefficient sequence be produced from a tH2 divisor lift, followed by

- bounded masks/smooth weights;
- unit-modulus phases;
- Gaussian representation expansion;
- one conductor band and one dyadic block;
- a Mellin packet with spectral energy `E_spec`.

Then for every `eta>0`,

\[
\boxed{
\sum_{\chi\in F(Q)}
\left|
\sum_z a_z^{\rm road}\chi(z)
\right|^2
\ll_{\eta}
\Delta(Z,Q)
\,E_{\rm spec}
\,K_W^2
\,Y^{\eta}
\sum_{h,r}|w(h,r)|^2.
}
\tag{H4.9}
\]

After recombining polylogarithmically many bands/blocks, the factor remains `B^{o(1)}` provided

```text
E_spec = B^o(1),
K_W    = B^o(1).
```

So **all standard roadworks weights are compatible with any base large-sieve saving**.  They do not erase a fixed positive exponent.

```text
WEIGHTED_ONE_VARIABLE_LARGE_SIEVE_TRANSFER_PROVED=true
ROADWORK_WEIGHT_OVERHEAD=B^o(1)_UNDER_BOUNDED_SPECTRAL_AND_MELLIN_BUDGETS
BASE_LARGE_SIEVE_THEOREM_REPROVED=false
```

---

## 9. Same-modulus two-coordinate safety rule

For a tH3 packet with one shared auxiliary modulus `q`, define

\[
M_q(\xi,\zeta)
=
\sum_{(U,V)\in\mathcal H}
a_{U,V}\xi(U)\zeta(V).
\]

The legal weighted reduction is (H4.4):

\[
|T_q|^2
\le E_q
\sum_{\xi,\zeta}|M_q(\xi,\zeta)|^2.
\]

The illegal reduction is

```text
same q on U and V
  -> introduce independent q_U and q_V
  -> tensorise two one-variable large sieves.
```

That operation destroys the same-modulus collision information which tH3 was designed to preserve.

Therefore tH4 freezes the theorem boundary:

> one-variable weighted transfer is closed; same-modulus **joint** second-moment saving must come from a theorem which keeps the common modulus common.

```text
INDEPENDENT_UV_MODULUS_TENSORIZATION_ALLOWED=false
SAME_MODULUS_JOINT_SECOND_MOMENT_THEOREM_PROVED=false
```

---

## 10. Canonical weighted theorem record

Later stages should expose analytic inputs and costs using

```text
WeightedGaussianSieveBlock:
  packet: GaussianSpectralHyperbolaPacket   # tH3

  base_second_moment:
    family
    conductor_band_Q
    norm_length_Z
    Delta_Z_Q

  coefficient_budget:
    source_l2_energy
    divisor_lift_factor <= tau_max
    gaussian_representation_factor <= 4*tau_max
    mask_sup_norm <= 1
    smooth_weight_sup_norm <= 1
    phase_modulus = 1

  spectral_budget:
    E_spec = sum |c_theta|^2

  mellin_budget:
    K_W = L1 norm of Mellin kernel

  assembly_budget:
    conductor_band_count
    hyperbola_block_count

  modulus_policy:
    shared_modulus_group_preserved = true
    independent_uv_tensorization = false
```

A claimed power saving is valid only after every field above is assigned a proved `B^{o(1)}` or better budget.

---

## 11. Deterministic audit

The dedicated tH4 audit checks the transfer algebra independently of the live `t` route.

### Divisor lift

For

```text
Y = 512,
c in {1,2,3,4,6,8,12},
w(h,r)=(-1)^(h+r)*(1+((h+2r) mod 3)),
```

it checks every pair `hr<=Y,(h,c)=1`.

Frozen totals:

```text
source (h,r) pairs                         13705
source L2 energy                           62770
collapsed norm L2 energy                  237956
max divisor-fiber multiplicity                24
Cauchy fiber violations                         0
max observed lift/source energy ratio   4.366268762557617
```

The theoretical bound is `24 * source energy`; the observed ratio is far below it.

### Bounded mask / smooth / phase layer

For a deterministic length-512 coefficient sequence:

```text
unweighted L2 energy                        12308
weighted energy numerator / 64             65502 / 64
L2 monotonicity violations                      0
```

The weight combines a coprimality mask, a bounded rational smooth factor and a sign phase.

### Spectral Cauchy

For

```text
p in {5,13,17,29,37,41,53,61}
```

and deterministic one- and two-coordinate `mu4`-mode vectors:

```text
one-coordinate modes checked                   62
same-modulus ordered mode pairs checked       650
maximum local H_p                              15
spectral Cauchy violations                       0
```

### Assembly

At `Y=512`, the audit finds `220` raw dyadic triples `(H,R,D)` satisfying `HRD<=Y`.  This is finite verification of the block generator; the asymptotic statement remains polylogarithmic.

---

## 12. Interaction with the live t route

Stage14-tH4 requires only merged tH3.

The current live t route has already advanced beyond the one-variable all-character obstruction and is attacking shorter endpoint arithmetic.  That does not make tH4 obsolete: the weighted transfer layer is reusable whenever the live route introduces

- a new smooth cutoff;
- another divisor decomposition;
- a conductor partition;
- a new Mellin packet;
- or a coefficient sequence which must be passed into a pre-existing large-sieve theorem.

If no future live step needs this tool immediately, tH4 simply remains frozen road infrastructure rather than becoming a waiting stage.

---

## Proof boundary

```text
STAGE14_TH4=COMPLETE_WEIGHTED_MELLIN_HECKE_LARGE_SIEVE_TRANSFER_TOOLBOX
TH_REQUIRES_FUTURE_T_RESULT=false
COEFFICIENT_MASKS_L2_SAFE=true
UNIT_MODULUS_PHASES_L2_SAFE=true
SPECTRAL_PACKET_COST_EXACT_L2_ENERGY=true
DIVISOR_LIFT_L2_COST=tau_max(Y)
DIVISOR_LIFT_FIXED_POWER_LOSS=false
GAUSSIAN_REPRESENTATION_LIFT_FIXED_POWER_LOSS=false
CONDUCTOR_BAND_COUNT=polylogarithmic
HYPERBOLA_BLOCK_COUNT=polylogarithmic
MELLIN_KERNEL_COST_EXPLICIT=true
WEIGHTED_ONE_VARIABLE_LARGE_SIEVE_TRANSFER_PROVED=true
SHARED_MODULUS_PACKET_CAUCHY_PRESERVES_MODULUS_GROUP=true
INDEPENDENT_UV_MODULUS_TENSORIZATION_ALLOWED=false
SAME_MODULUS_JOINT_SECOND_MOMENT_THEOREM_PROVED=false
FULL_COEFFICIENT_COLLISION_ENERGY_PROVED=false
NORM_INDEX_HYPERBOLIC_CORRELATION_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-tH5
```
