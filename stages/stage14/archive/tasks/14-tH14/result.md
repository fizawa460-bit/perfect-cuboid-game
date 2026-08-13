# Stage14-tH14 — selector-sensitive two-auxiliary Gaussian second-moment receiver

## Purpose

Merged Stage14-t50 hit the Stage14-tH11 reopen trigger

```text
genuinely multi-modulus post-dispersion packet
```

with two distinct split auxiliary primes `p,q`.  The live good-prime object is

\[
S_R(p,q)
 =\sum_{\xi\in X_R}
 w_R(\xi)\,\chi_{pq}(\widetilde F(\xi)),
\]

and the required global estimate is

\[
\boxed{
\sum_{p\ne q}
\left|\sum_R S_R(p,q)\right|^2
\ll
P^2\left(\sum_R\|w_R\|_2^2\right)B^{o(1)}.
}
\tag{H14.1}
\]

For unit physical weights this is exactly

\[
R_{\rm good}\ll H P^2B^{o(1)}.
\]

This stage constructs the non-circular receiver for (H14.1), proves the aggregate same-modulus residue-collision part that tH5 intentionally left open, and isolates the one remaining external analytic theorem: a nonresonant selector-sensitive completion / trace-family large-sieve theorem.

Stage14-t50's global mean-square power saving is **not** assumed.

The forbidden operation remains forbidden throughout:

```text
ordered physical state pair
  -> cross-kernel tau coefficient
  -> coefficient energy E4
```

before physical / norm-circle cancellation.  That is circular by merged t49.

---

## 1. Inputs and invariants that must survive

The receiver keeps all of the following until after the analytic estimate:

1. signed aggregation across the tH12 common-disjoint-refinement blocks `R`;
2. one shared `U/V` modulus group from tH3/tH4;
3. the exact divisor-coupled hyperbola from tH2;
4. canonical-prime selector weights;
5. interval, reconstruction and branch masks;
6. Gaussian orientation / unit-orbit labels;
7. two **distinct** split auxiliary rational primes `p,q`.

The reused roadworks are:

- t32: complete split-torus one- and two-prime angular cancellation;
- tH4: bounded masks, smooth cutoffs, Mellin phases and divisor/representation lifts are `L2`-safe once a base second-moment theorem is supplied;
- tH5: exact Gaussian-pair coefficient collision energy is near-linear;
- tH8: Route-B physical-packet dispersion identity;
- tH11: genuine multi-modulus packet is a reopen trigger;
- tH12/tH13: common refinement, signed aggregation and same-modulus discipline.

No independent `U` and `V` modulus tensorisation is introduced.

---

## 2. Lift first to the exact Gaussian-pair layer

On one legal tH2/tH4 hyperbola block, retain the exact Gaussian pair

\[
z=(R,U,V,\mathfrak s),
\]

where `mathfrak s` denotes the finite branch/orientation/reconstruction labels that are required by the physical selector.  Let

\[
A_z
\]

be the coefficient obtained after the legal tH4 weighted transfer and the tH5 exact arithmetic-fiber collapse.

The block label `R` is **not** discarded.  Thus signs from different common-refinement blocks remain in the final sum rather than being replaced by positive block masses.

Put

\[
E_A=\sum_z|A_z|^2.
\]

By tH5, together with the tH4 representation and assembly budgets,

\[
\boxed{
E_A
\ll
B^{o(1)}\sum_R\|w_R\|_2^2.
}
\tag{H14.2}
\]

For unit physical weights the exact-pair support mass and the exact-pair coefficient energy are both `H*B^{o(1)}` after all polylogarithmic / divisor representation refinements.

This is the correct coefficient space for tH14.  Collapsing further to the value `Ftilde`, to a squareclass, or to a cross-kernel is not allowed before the selector-sensitive theorem.

---

## 3. Two-prime trace matrix

For a good ordered pair of distinct split auxiliary primes `(p,q)`, write

\[
\Phi_{p,q}(z)
 =\chi_p(\widetilde F(z))\chi_q(\widetilde F(z))
 =\chi_{pq}(\widetilde F(z)).
\tag{H14.3}
\]

The signed common-refinement aggregate is

\[
T(p,q)=\sum_z A_z\Phi_{p,q}(z).
\tag{H14.4}
\]

The desired theorem is the operator estimate

\[
\boxed{
\sum_{p\ne q}|T(p,q)|^2
\ll P^2 E_A B^{o(1)}.
}
\tag{H14.5}
\]

Together with (H14.2), (H14.5) implies the t50 contract (H14.1).

The trivial estimate instead gives

\[
\sum_{p\ne q}|T(p,q)|^2
\le P^2\,N_Z\,E_A,
\tag{H14.6}
\]

where `N_Z` is the exact-pair support cardinality.  In the physical unit-weight case this is `H^2 P^2 B^{o(1)}` and misses the target by a full factor `H`.

Thus a genuine second-moment orthogonality statement is necessary.

---

## 4. Same-modulus residue collision: exact definition

Fix the oriented Gaussian prime ideals used by the split-prime normalization,

\[
\mathfrak p\mid p,
\qquad
\mathfrak q\mid q,
\qquad
\mathfrak m=\mathfrak p\mathfrak q.
\]

The local angular packet is unchanged if a Gaussian coordinate is multiplied by one of the four units.  Hence define a same-modulus collision of exact pairs `z=(U,V,...)` and `z'=(U',V',...)` by requiring, at both auxiliary prime ideals, unit-orbit congruences

\[
U\equiv u_rU'\pmod{\mathfrak r},
\qquad
V\equiv v_rV'\pmod{\mathfrak r},
\qquad
u_r,v_r\in\mu_4,
\qquad
\mathfrak r\in\{\mathfrak p,\mathfrak q\}.
\tag{H14.7}
\]

(The two primes may use different unit choices.)

Let `z ~_{p,q} z'` denote (H14.7), including the finite compatible branch/orientation labels required by the common refinement.

The residue-collision energy at `(p,q)` is

\[
\mathcal C_{p,q}(A)
 =\sum_{\rho}
 \left|\sum_{z:\operatorname{red}_{p,q}(z)=\rho}A_z\right|^2.
\tag{H14.8}
\]

This is the collision object tH5 explicitly did **not** bound.

---

## 5. New theorem: aggregate nonexact residue collisions are divisor-sparse

The key roadworks observation is that tH5 already retained both Gaussian coordinates.  This makes a nonexact residue collision visible through a fixed polynomial-size difference datum.

For two exact Gaussian pairs, define

\[
D_U(z,z')
 =\prod_{u\in\mu_4}N(U-uU'),
\qquad
D_V(z,z')
 =\prod_{v\in\mu_4}N(V-vV'),
\tag{H14.9}
\]

and

\[
\Delta(z,z')=\gcd\bigl(D_U(z,z'),D_V(z,z')\bigr).
\tag{H14.10}
\]

If `U` is unit-equivalent to `U'`, then `D_U=0`; the convention `gcd(0,n)=|n|` is used.  The only case `Delta=0` is when **both** coordinates are unit-equivalent, i.e. the exact `(U,V)` unit orbit agrees.  That orbit is the tH5 exact-pair diagonal, with bounded unit cost at most `16`.

Now suppose `z,z'` are not in the same exact unit orbit and `z~_{p,q}z'`.  For each rational auxiliary prime `r in {p,q}`, some unit choices in (H14.7) imply

\[
r\mid D_U(z,z'),
\qquad
r\mid D_V(z,z'),
\]

so

\[
\boxed{pq\mid\Delta(z,z').}
\tag{H14.11}
\]

All Stage14 Gaussian coordinates and labels in one physical block have polynomial size.  Therefore for some fixed absolute `C`,

\[
0<|\Delta(z,z')|\le B^C.
\tag{H14.12}
\]

Take the amplifier primes on a fixed dyadic scale

\[
p,q\asymp L=B^\rho,
\qquad \rho>0\text{ fixed}.
\]

A nonzero integer of size at most `B^C` has at most

\[
C/\rho+o(1)=O_\rho(1)
\]

prime divisors in this interval.  Hence a fixed nonexact pair `(z,z')` can satisfy (H14.7) for only

\[
\boxed{O_\rho(1)}
\tag{H14.13}
\]

ordered distinct auxiliary-prime pairs `(p,q)`.

This is the exact two-prime analogue of t50's bad-prime incidence count.

### Aggregate collision operator

Let

\[
K(z,z')
 =\#\{(p,q):p\ne q,\ z\sim_{p,q}z'\}.
\]

After exact unit-orbit canonicalisation,

```text
K(z,z) <= P(P-1),
K(z,z') = O_rho(1) for z != z'.
```

If `N_Z` is the exact-pair support cardinality, Schur's test gives

\[
\left\|K\right\|_{2\to2}
\ll P^2+N_ZB^{o(1)}.
\tag{H14.14}
\]

At the t49 amplifier scale

\[
P\ge H B^{-o(1)},
\]

and tH4/tH5 give

\[
N_Z\le H B^{o(1)}.
\]

Thus

\[
\boxed{
\sum_{p\ne q}\mathcal C_{p,q}(A)
\ll
P^2E_A B^{o(1)}.
}
\tag{H14.15}
\]

This closes the **aggregate same-modulus residue-collision energy** at exactly the scale needed by t50.

It is stronger than the tH5 exact collision theorem in one direction and weaker in another:

- tH5 controls exact pair fibers for one coefficient map;
- tH14 proves that nonexact pairs can collide modulo two large auxiliary primes only for `O(1)` prime pairs;
- neither theorem identifies distinct exact pairs with the same squareclass.

The latter distinction is essential to avoid circularity.

---

## 6. Large-product-modulus injectivity: optional stronger subrange

There is an additional elementary resonance-free regime.

Suppose one dyadic block has

\[
N(U),N(V)\le Y.
\]

For units `u,v`, a nonzero difference satisfies

\[
N(U-uU')\le4Y,
\qquad
N(V-vV')\le4Y.
\]

If

\[
pq>4Y,
\tag{H14.16}
\]

then divisibility by the product ideal `mathfrak p mathfrak q` forces each such congruence difference to vanish.  Hence the two-prime residue collision is an exact unit-orbit collision.

In the critical square-root-canonical-prime strip,

\[
\ell=B^{1/2+o(1)},
\qquad
Y=B/\ell=B^{1/2+o(1)}.
\]

Writing `p,q=B^{rho+o(1)}`, condition (H14.16) holds with a fixed margin whenever

\[
\boxed{\rho>1/4.}
\tag{H14.17}
\]

At `rho=1/4` the constants / `B^{o(1)}` widths matter, so no endpoint injectivity theorem is claimed.

This injective subrange is useful for t51, but it does **not** by itself prove the trace second moment: a sparse selector can remain highly coherent against the character even when every residue class contains at most one exact pair.

---

## 7. Why tH5 does not absorb the principal squareclass resonance

One must distinguish two resonances.

### A. same-modulus residue resonance

Distinct exact pairs happen to occupy the same local `U/V` unit-orbit residue class modulo `(p,q)`.

This aggregate is closed by (H14.15), using tH5 on the exact diagonal plus the new large-prime difference-divisor lemma off the diagonal.

### B. global character / squareclass resonance

Distinct exact pairs satisfy

\[
[\widetilde F(z)]=[\widetilde F(z')]
\]

in the rational squareclass group.  Then

\[
\Phi_{p,q}(z)=\Phi_{p,q}(z')
\]

for every good `(p,q)`.

Bounding how often this happens is precisely the principal-collision problem `A1` / its higher-energy variants.  Declaring this family to be an "exact-pair collision" would merely rename the problem and is forbidden.

Thus

```text
tH5 exact-pair energy absorbs residue-diagonal:        yes
tH14 divisor incidence absorbs nonexact residue clash: yes
tH5 absorbs equal-squareclass distinct exact pairs:    no
```

---

## 8. t32 completion: what it supplies and what is still missing

For fixed good norm indices, t32 proves complete split-torus correlation

\[
\left|C_{p,q}^{\rm comp}(m,n)\right|
\ll pq\,B^{o(1)}.
\tag{H14.18}
\]

The full two-coordinate split torus has size on the `p^2q^2` scale, so (H14.18) is the expected square-root complete scale.

However the physical coefficient is supported only on sparse integral Gaussian representatives satisfying the hyperbola and all physical masks.  Completion of a sparse subset requires more than the zero-frequency complete sum.

On one norm-index / branch cell let

\[
a_{p,q}(\omega)
 =\sum_{z:\operatorname{red}_{p,q}(z)=\omega}A_z
\]

on the complete angular residue fiber `Omega_{p,q}`.  Write

\[
a_{p,q}=\bar a_{p,q}+d_{p,q},
\]

where `bar a` is constant on the complete angular fiber with the same total mass.

Then

\[
\sum_\omega a_{p,q}(\omega)\Phi_{p,q}(\omega)
=
\bar a_{p,q}C_{p,q}^{\rm comp}
+
\sum_\omega d_{p,q}(\omega)\Phi_{p,q}(\omega).
\tag{H14.19}
\]

The first term is exactly the part t32 controls.  The second is the **selector discrepancy**.

The mod-13 countermodel from t50 shows that a complete character sum can vanish while a selected subset has maximal one-sign bias.  Therefore (H14.18) alone cannot control the second term in (H14.19).

---

## 9. Poisson / additive completion / lattice discrepancy audit

Three standard completion ideas were tested at the level of theorem shape.

### 9.1 Naive Fourier `L1` completion

If every additive Fourier transform of the complete angular trace enjoyed the same square-root bound as (H14.18), then Fourier inversion would bound the selector discrepancy by an `L1` norm of the selector Fourier transform.

For a genuinely sparse integral representation set, a delta-like selector already has Fourier `L1` mass on the full ambient-group scale.  Hence this route can lose the complete square-root gain and is not a uniform proof of (H14.5).

Conclusion:

```text
COMPLETE_TRACE_PLUS_SELECTOR_FOURIER_L1_IS_AUTOMATICALLY_SUFFICIENT=false
```

### 9.2 Gaussian additive large sieve

The Gaussian additive large sieve accepts arbitrary coefficient support for **linear additive phases**.  After a quadratic Gauss expansion of a character `chi(F(U,V))`, however, the additive phase is the nonlinear polynomial value `F(U,V)` and one also introduces all reduced additive frequencies.  Treating `U` and `V` by independent Gaussian large sieves would violate the shared-modulus rule.

Thus the existing additive theorem is useful as a possible internal step after a new linearisation, but is not the missing theorem itself.

### 9.3 Lattice discrepancy on norm circles

The physical selector is not a convex planar lattice box.  It is a sparse set of exact two-square representations on moving norm circles, coupled through

\[
N(U)=hr,
\qquad
N(V)=gh\delta,
\qquad
hr\delta\le Y,
\]

and then filtered by canonical / branch / reconstruction masks.

A pointwise equidistribution theorem for arbitrary fixed norm circles is therefore neither available from t32 nor logically sufficient.  The required statement must average over the divisor-coupled norm-index family and the two auxiliary primes simultaneously.

---

## 10. The exact missing external theorem

After (H14.15), the only missing analytic input can be stated without any `E4` coefficient.

### SelectorSensitiveGaussianCompletion (SSGC)

For every tH12 common-refinement family, every legal tH2 dyadic hyperbola block, and every exact-pair coefficient sequence `A_z` produced by tH4/tH5, with all canonical / interval / reconstruction / branch masks retained, define `T(p,q)` by (H14.4).

The theorem required by t51 is

\[
\boxed{
\sum_{p\ne q}
|T(p,q)|^2
\ll
B^{o(1)}
\left[
P^2E_A
+\sum_{p\ne q}\mathcal C_{p,q}^{\rm nonexact}(A)
\right].
}
\tag{H14.20}
\]

Equivalently, since tH14 proves the second term is `<=P^2 E_A B^{o(1)}`,

\[
\boxed{
\sum_{p\ne q}|T(p,q)|^2
\ll P^2E_AB^{o(1)}.
}
\tag{H14.21}
\]

The point of (H14.20), rather than simply restating the t50 target, is its **failure classification**:

- exact coefficient collisions are already paid by tH5;
- nonexact local residue collisions are already paid by (H14.15);
- the theorem's remaining content is cancellation of the nonresonant sparse integral selector against the t32 two-prime trace.

A proof may use Poisson summation, additive completion, a trace-function large sieve, lattice discrepancy, or a new hybrid argument, but it must deliver (H14.20) while preserving the shared modulus and signed block aggregation.

### Equivalent discrepancy formulation

Using (H14.19), it suffices to prove

\[
\boxed{
\sum_{p\ne q}
\left|
\sum_{\text{norm cells }c}
\sum_{\omega\in\Omega_c(p,q)}
 d_{c,p,q}(\omega)\Phi_{p,q}(\omega)
\right|^2
\ll P^2E_AB^{o(1)}.
}
\tag{H14.22}
\]

with the complete mean component separately controlled by t32 and the tH4/tH12 hyperbola assembly.

Equation (H14.22) is the exact **selector discrepancy theorem** that is absent from the current merged repository.

---

## 11. Why known generic large sieves do not already give SSGC

The following comparisons are safe.

### Heath-Brown / quadratic Hecke large sieve

If one collapses the exact-pair support to the integer or squareclass value `Ftilde(z)`, then the coefficient collision energy is no longer controlled by tH5.  In the principal/product-kernel expansion it is exactly the unresolved squareclass collision / `E4` type quantity exposed by t49.

Therefore a standard quadratic-character large sieve applied **after value collapse** is circular for the present purpose.

### Sparse Gaussian additive-moduli large sieve

Baier--Bansal type sparse-moduli Gaussian large sieves concern additive fractions `a/q` and require distribution information for the modulus set.  They do not directly supply (H14.22) for a nonlinear two-coordinate multiplicative trace on a divisor-coupled representation selector.

### Arbitrary-subset trace-function bilinear estimates

Known one-prime-field arbitrary-subset trace-function estimates require a trace-sheaf certificate and quantitative size / energy hypotheses.  The Stage14 object is simultaneously two-prime, composite-modulus, two-coordinate and shared-modulus, with a moving divisor-coupled support.  No direct theorem import is currently certified.

Thus

```text
KNOWN_GENERIC_LARGE_SIEVE_DIRECTLY_PROVES_SSGC=false
```

This is a theorem-hypothesis mismatch, not a claim that the existing literature cannot inspire a proof.

---

## 12. Countermodels and quantifier guards

### Guard A: arbitrary selector is false

If a selector is allowed to keep only points on which every active trace equals `+1`, then for `H` unit-weight points

\[
T(p,q)=H
\]

for every `(p,q)`, so

\[
\sum_{p\ne q}|T(p,q)|^2
\asymp P^2H^2,
\]

which violates the target `P^2H`.

A concrete algebraic instance is a selector supported on points for which `Ftilde` is a nonzero rational square at all good primes.  Hence SSGC cannot be a theorem for arbitrary masks; it must use the actual Stage14 Gaussian/hyperbola geometry.

### Guard B: complete cancellation is not subset cancellation

The t50 mod-13 example remains valid:

```text
complete Legendre sum = 0
selector = the six quadratic residues
selected sum = 6
```

### Guard C: no blockwise absolute recombination

The left side of (H14.1) contains

\[
\left|\sum_R S_R(p,q)\right|^2.
\]

Replacing it by

\[
\#R\sum_R|S_R(p,q)|^2
\]

is legal only if the resulting block-count factor is explicitly `B^{o(1)}` and does not destroy a signed cancellation supplied by the theorem.  The canonical tH14 contract therefore keeps the signed sum across `R` inside SSGC.

### Guard D: no pair-kernel pre-collapse

Expanding the square is allowed for identities and audits.  Aggregating the ordered exact-pair coefficients first by `tau=sqf(F(z)F(z'))` and then applying a coefficient-energy inequality is forbidden: its coefficient energy is the unresolved `E4`.

---

## 13. Critical square-root-strip exponent ledger

Write

\[
H=B^{h+o(1)},
\qquad
L=B^{\rho+o(1)},
\qquad
P=B^{\rho+o(1)},
\]

where the logarithmic prime density is absorbed into `B^{o(1)}`.

At the critical canonical-prime strip

\[
\ell=B^{1/2+o(1)},
\qquad
Y=B/\ell=B^{1/2+o(1)}.
\]

The t49 amplifier condition

\[
P\ge H B^{-o(1)}
\]

is the exponent condition

\[
\boxed{\rho\ge h.}
\tag{H14.23}
\]

### Target

\[
H P^2=B^{h+2\rho+o(1)}.
\tag{H14.24}
\]

### Trivial second moment

\[
H^2P^2=B^{2h+2\rho+o(1)},
\tag{H14.25}
\]

so the required mean-square saving is exactly one factor `H`, i.e. exponent `h`.

### Exact / residue collision contribution

By tH5 + (H14.15),

\[
\mathcal M_{\rm residue}
\ll B^{h+2\rho+o(1)},
\tag{H14.26}
\]

which is exactly on target and consumes no fixed exponent.

### Large-product injectivity threshold

Since `Y=B^{1/2+o(1)}`, per-modulus nonexact residue collisions disappear with a fixed margin when

\[
2\rho>1/2,
\qquad\text{i.e.}\qquad
\boxed{\rho>1/4.}
\tag{H14.27}
\]

This is optional because the aggregate divisor-incidence bound already closes residue collisions for every fixed `rho>0` under the amplifier-size hypothesis.

### SSGC loss ledger

If a future theorem proves only

\[
\sum_{p\ne q}|T(p,q)|^2
\ll P^2E_AB^{\omega+o(1)},
\]

then the physical bound is

\[
R_{\rm good}
\ll B^{h+2\rho+\omega+o(1)}.
\]

The t49 near-linear principal-collision target requires

\[
\boxed{\omega=0}
\]

at the fixed-power level.  Any positive fixed `omega` is a genuine remaining loss and must not be hidden in `B^{o(1)}`.

---

## 14. Direct receiver for Stage14-t51

Stage14-t51 may use the following record without reopening tH1--tH13.

```text
SelectorSensitiveTwoAuxiliaryGaussianSecondMoment:
  source:
    common_refinement_blocks = signed, not absolute-valued
    exact_gaussian_pair_labels = retained
    shared_UV_modulus_group = true
    divisor_coupled_hyperbola = retained
    canonical_selector = retained
    interval_reconstruction_branch_masks = retained

  auxiliary:
    p,q = distinct split rational primes
    p,q ~ B^rho
    bad-prime aggregate = closed by t50

  coefficient_energy:
    E_A <= B^o(1) * sum_R ||w_R||_2^2       # tH4+tH5

  residue_collision:
    exact unit-orbit diagonal = tH5
    nonexact pair supports O_rho(1) prime-pairs
    aggregate_collision <= P^2 E_A B^o(1)   # tH14

  complete_trace:
    t32 two-prime split-torus = O(p*q)

  missing_external_input:
    SelectorSensitiveGaussianCompletion / equation H14.20
    equivalently selector discrepancy equation H14.22

  forbidden:
    pair_to_tau_collapse_before_cancellation = true
    independent_UV_modulus_tensorization = true
    complete_sum_implies_sparse_selector_sum = true
    tH5_exact_pair_equals_squareclass_collision = true
```

If SSGC is proved, then immediately

\[
\sum_{p\ne q}\left|\sum_R S_R(p,q)\right|^2
\ll
P^2\left(\sum_R\|w_R\|_2^2\right)B^{o(1)},
\]

and in the physical unit-weight case

\[
R_{\rm good}\ll HP^2B^{o(1)}.
\]

Together with merged t50's bad-prime estimate, this supplies the full t49 Frobenius mean-square target.

---

## 15. Literature comparison used only as orientation

No external theorem is imported as a proof of SSGC.  The following are comparison points only:

- S. Baier and A. Bansal, *Large sieve with sparse sets of moduli for Z[i]*: Gaussian additive large sieve with sparse moduli, using distribution of moduli in arithmetic progressions and large-sieve/Poisson machinery.
- L. Goldmakher and B. Louvel, *A quadratic large sieve inequality over number fields*: quadratic Hecke-family large sieve and Poisson machinery; useful after a legal character-family reduction, but not after a circular `Ftilde`/squareclass coefficient collapse.
- P. Xi, *Bilinear forms with trace functions over arbitrary sets, and applications to Sato--Tate*: arbitrary-subset trace-function technology over one finite field under sheaf and size/energy hypotheses; not a direct certificate for the present two-prime shared-modulus Gaussian packet.

---

## Proof boundary

```text
STAGE14_TH14=COMPLETE_TWO_AUXILIARY_SELECTOR_RECEIVER_AND_RESIDUE_COLLISION_CLOSURE
T50_MULTI_MODULUS_REOPEN_TRIGGER_IMPORTED=true
SIGNED_COMMON_REFINEMENT_AGGREGATION_PRESERVED=true
SHARED_UV_MODULUS_GROUP_PRESERVED=true
DIVISOR_COUPLED_HYPERBOLA_PRESERVED=true
CANONICAL_SELECTOR_PRESERVED=true
INTERVAL_RECONSTRUCTION_BRANCH_MASKS_PRESERVED=true
DISTINCT_SPLIT_AUXILIARY_PRIMES_PRESERVED=true
EXACT_GAUSSIAN_PAIR_COEFFICIENT_ENERGY_IMPORTED=true
NONEXACT_RESIDUE_COLLISION_PRIME_PAIR_MULTIPLICITY=O_rho(1)
AGGREGATE_SAME_MODULUS_RESIDUE_COLLISION_ENERGY_PROVED=true
LARGE_PRODUCT_RESIDUE_INJECTIVITY_THRESHOLD_RHO_GT_1_4=true
TH5_ABSORBS_GLOBAL_SQUARECLASS_RESONANCE=false
T32_COMPLETE_ANGULAR_BOUND_DIRECTLY_CONTROLS_SPARSE_SELECTOR=false
NAIVE_POISSON_FOURIER_L1_COMPLETION_CLOSES_TARGET=false
GAUSSIAN_ADDITIVE_LARGE_SIEVE_DIRECTLY_CLOSES_TARGET=false
KNOWN_GENERIC_TRACE_LARGE_SIEVE_DIRECTLY_CERTIFIED=false
SELECTOR_SENSITIVE_GAUSSIAN_COMPLETION_THEOREM_DEFINED=true
SELECTOR_SENSITIVE_GAUSSIAN_COMPLETION_THEOREM_PROVED=false
SELECTOR_DISCREPANCY_THEOREM_H14_22_PROVED=false
PAIR_COLLAPSE_BEFORE_PHYSICAL_CANCELLATION_ALLOWED=false
T50_GLOBAL_MEAN_SQUARE_POWER_SAVING_ASSUMED=false
GLOBAL_EXTERNAL_TWO_PRIME_MEAN_SQUARE_BOUND_PROVED=false
GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false
GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t51 prove SelectorSensitiveGaussianCompletion (H14.20/H14.22) on the physical divisor-coupled Gaussian selector; residue collisions are no longer the obstruction
```
