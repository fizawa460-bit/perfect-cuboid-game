# Stage14-t50 — external bad-prime closure and selector-sensitive two-modulus boundary

## Purpose

Stage14-t49 reduced the principal squareclass collision problem to the external split-prime Frobenius mean square

\[
R_{\rm off}=\sum_{p\ne q\in\mathcal P}
\left|\sum_s\left(\frac{\widetilde F_s}{p}\right)
                 \left(\frac{\widetilde F_s}{q}\right)\right|^2,
\]

with the sufficient target

\[
R_{\rm off}\ll H P^2 B^{o(1)}.
\]

Stage14-t50 separates the auxiliary bad-prime contribution, identifies the good kernel with the existing tH8 physical Route-B dispersion object, and determines exactly what theorem is still missing between t32 complete angular cancellation and the physical sparse Gaussian selector.

## 1. External bad auxiliary primes are harmless at the t49 amplifier scale

For a physical state `s`, put all forbidden odd auxiliary-prime factors into a polynomial-size datum

\[
M_s=\ell_s\Delta_s m_s n_s\widetilde F_s
\]

(up to bounded fixed factors). On the physical family `|M_s|<=B^{C_0}` for an absolute constant `C_0`.

Take the external split-prime amplifier on

\[
p\asymp L=B^\rho,\qquad \rho>0\text{ fixed}.
\]

A fixed state is bad at only

\[
\omega_{p\asymp L}(M_s)\le C_0/\rho+o(1)=O_\rho(1)
\]

amplifier primes. If `B_p` denotes the number of states bad at `p`, then

\[
\sum_pB_p=O_\rho(H),
\qquad
\sum_pB_p^2\le H\sum_pB_p=O_\rho(H^2).
\]

Deleting the states bad at either endpoint changes a `(p,q)` character sum by at most `B_p+B_q`. Hence

\[
\boxed{
R_{\rm bad}
\le 4(P-1)\sum_pB_p^2
\ll_\rho H^2P.
}
\]

At the t49 amplifier scale `P>=H B^{-o(1)}` this gives

\[
\boxed{R_{\rm bad}\ll H P^2 B^{o(1)}.}
\]

Thus the auxiliary bad-prime aggregate is no longer an obstruction.

Frozen consistency: the t49 external 128-prime amplifier had max bad count `0`; the endogenous 87-prime set had max bad count `2`.

## 2. The good Frobenius kernel is exactly tH8 Route-B

After the canonical even square is removed on the visible branch,

\[
G_{p,q}
=
\sum_s\chi_p(\widetilde F_s)\chi_q(\widetilde F_s).
\]

This is exactly the physical-packet dispersion kernel `H_X(p,q)` standardized in Stage14-tH8. Therefore the t49 Frobenius amplifier is not a new algebraic object: it is the concrete two-auxiliary specialization of the already-audited Route-B dispersion identity.

Stage14-tH11 explicitly listed a

```text
genuinely multi-modulus post-dispersion packet
```

as a support-route reopen trigger. Stage14-t50 hits that trigger: two distinct split auxiliary primes `p,q` remain simultaneously active after dispersion.

## 3. Why the t32 complete bound does not yet prove the physical mean square

Stage14-t32 proved square-root cancellation for the **complete** split norm-circle angular correlation at fixed good auxiliary primes and fixed norm indices.

The physical Stage14 sum retains only sparse integral Gaussian representations satisfying the divisor-coupled hyperbola, canonical-prime selector, branch labels, interval constraints and reconstruction masks. A complete finite-field bound cannot by itself control such a selected subset.

The logical gap is real even in the simplest character model: modulo `13`,

\[
\sum_{x\in\mathbf F_{13}^*}\left(\frac{x}{13}\right)=0,
\]

but selecting only the six quadratic residues gives sum `6`.

Thus one needs a theorem about the **physical selector**, not another local Weil bound.

## 4. Existing roadworks remove every other fixed-power loss

Stage14-tH4 proves that masks, smooth weights, Mellin phases, divisor lifts and Gaussian representation lifts preserve a supplied base second-moment saving up to `B^{o(1)}`. It explicitly leaves the same-modulus joint second moment unproved.

Stage14-tH5 proves near-linear exact Gaussian-pair coefficient collision energy and again explicitly leaves same-modulus residue collision / joint second moment unproved.

Therefore the missing theorem can be isolated cleanly without reopening the divisor/hyperbola bookkeeping.

## 5. Minimal missing theorem contract

For the common disjoint refinement blocks `R`, define

\[
S_R(p,q)=
\sum_{\xi\in X_R}
 w_R(\xi)\,\chi_{pq}(\widetilde F(\xi)).
\]

The required base theorem is

\[
\boxed{
\sum_{p\ne q\in\mathcal P}
\left|\sum_R S_R(p,q)\right|^2
\ll
P^2\left(\sum_R\|w_R\|_2^2\right)B^{o(1)}.
}
\tag{50.1}
\]

It must preserve simultaneously:

- signed aggregation across common-refinement blocks;
- the shared `U/V` modulus group;
- the divisor-coupled hyperbola cutoff;
- canonical-prime and physical reconstruction selectors;
- two distinct split auxiliary primes `p,q`.

In the unweighted physical specialization, (50.1) is exactly

\[
R_{\rm good}\ll H P^2B^{o(1)}.
\]

The forbidden shortcut remains unchanged: collapsing ordered physical state pairs to cross-kernel coefficients before the physical/norm-index cancellation imports the unresolved fourth energy `E4`.

## 6. tH decision

**Stage14-tH14 is needed.**

This is not generic advance research: t50 has hit the explicit tH11 multi-modulus reopen trigger and the exact same-modulus joint-second-moment gap recorded by tH4/tH5.

The tH14 task should build a selector-sensitive two-auxiliary Gaussian second-moment receiver/certificate for (50.1), reusing t32 angular completion, tH4 weighted transfer and tH5 exact-pair energy without pair-collapse circularity.

## Frozen diagnostic inherited from t49

```text
H                                      560
external amplifier P                   128
external R_off                   9,007,456
R_off / [H*P*(P-1)]            0.9894649888
external max bad prime count              0
endogenous max bad prime count             2
```

The near-random frozen ratio is diagnostic only, not an asymptotic proof.

## Boundary

```text
STAGE14_T50=COMPLETE_BAD_AUXILIARY_BOUND_AND_SELECTOR_SENSITIVE_TWO_MODULUS_BOUNDARY
EXTERNAL_BAD_AUXILIARY_AGGREGATE_BOUND_PROVED=true
TH8_PHYSICAL_ROUTE_B_EQUALS_T49_FROBENIUS_KERNEL=true
TH11_MULTI_MODULUS_REOPEN_TRIGGER_HIT=true
T32_COMPLETE_ANGULAR_BOUND_DIRECTLY_CONTROLS_SPARSE_PHYSICAL_SELECTOR=false
SELECTOR_SENSITIVE_TWO_MODULUS_SECOND_MOMENT_REQUIRED=true
SELECTOR_SENSITIVE_TWO_MODULUS_SECOND_MOMENT_PROVED=false
GLOBAL_EXTERNAL_TWO_PRIME_MEAN_SQUARE_BOUND_PROVED=false
GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false
GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
TH14_NEEDED=true
NEXT=Stage14-t51 attack SelectorSensitiveTwoAuxiliaryGaussianSecondMoment on the critical family; consume Stage14-tH14 if available, while keeping t32 completion before pair collapse
```
