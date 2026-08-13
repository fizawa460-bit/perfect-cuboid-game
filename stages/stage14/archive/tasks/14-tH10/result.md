# Stage14-tH10 — squareclass fiber / autocorrelation incidence toolbox

## Purpose

Stage14-tH9 rewrote the one-Cauchy cross-kernel problem on the rational squareclass group.  If a state `j` has squareclass

\[
\sigma_j=\operatorname{sqf}(|F_j|),
\]

then

\[
\kappa_{ij}=\sigma_i\oplus\sigma_j,
\]

and the pair coefficient is the squareclass autocorrelation

\[
A(\kappa)=\sum_s W(s)\overline{W(s\oplus\kappa)}.
\]

The principal collision and fourth energy are therefore

\[
A_1=A(1),\qquad E_4=\sum_\kappa |A(\kappa)|^2.
\]

Merged Stage14-t41 then showed that near-linear row energy and near-linear reverse-column energy do **not** imply a near-linear global `A1`: a genuinely mixed off-fiber collision survives on a Kummer-type surface.  It also showed that controlling `A1` alone is insufficient for `E4`.

Stage14-tH10 does not retry the t41 geometry.  It builds a reusable receiver for whatever generic/exceptional, transverse/isogenous, canonical-prime, or common-core decomposition a later live `t` stage proves.

No future `t42` result is required.

---

## 1. Squareclass counts and exact autocorrelation identities

For the counting version, let

\[
r(s)=\#\{j:\sigma_j=s\},\qquad H=\sum_s r(s).
\]

Write

\[
c(\kappa)=\sum_s r(s)r(s\oplus\kappa).
\]

Then

\[
\boxed{c(1)=A_1=\sum_s r(s)^2}
\tag{10.1}
\]

and

\[
\boxed{\sum_\kappa c(\kappa)=H^2.}
\tag{10.2}
\]

The fourth energy is

\[
\boxed{E_4=\sum_\kappa c(\kappa)^2.}
\tag{10.3}
\]

For complex coefficients the same algebra holds with `r` replaced by `W` and conjugation inserted.  The nonnegative counting formulation is singled out below when an inequality uses positivity.

---

## 2. Exact partition receiver for the principal energy

Let `P` be any partition of the state set into cells `C`.  Define

\[
r_C(s)=\#\{j\in C:\sigma_j=s\}.
\]

The local same-cell squareclass energy is

\[
L_P=\sum_C\sum_s r_C(s)^2.
\tag{10.4}
\]

The ordered off-cell squareclass incidence is

\[
I_P^{\rm off}
=\sum_{C\ne C'}\sum_s r_C(s)r_{C'}(s).
\tag{10.5}
\]

Expanding the global square gives the exact identity

\[
\boxed{A_1=L_P+I_P^{\rm off}.}
\tag{10.6}
\]

This is the correct interface for t41-type geometry.

It prevents the invalid shortcut

```text
row local energy is near-linear
column local energy is near-linear
therefore global A1 is near-linear
```

because neither local theorem controls the cross-cell term in (10.6).

### Generic / exceptional receiver

If ordered cell pairs are split into generic and exceptional sets,

\[
I_P^{\rm off}=I_{\rm gen}+I_{\rm exc},
\]

then

\[
\boxed{A_1=L_P+I_{\rm gen}+I_{\rm exc}.}
\tag{10.7}
\]

A later live stage may therefore prove different theorems for transverse generic packet pairs and exceptional/isogenous packet pairs without changing the energy bookkeeping.

---

## 3. Frozen t41 application of the partition receiver

For the merged t41 frozen population,

```text
H                         = 1120
A1                        = 2368
same-direction energy     = 2240
off-direction collisions  = 128
```

and indeed

\[
\boxed{2368=2240+128.}
\tag{10.8}
\]

Thus the direction partition already isolates the exact unresolved principal-energy contribution into 128 frozen ordered collisions.

This finite count is diagnostic only.  Stage14-tH10 does not promote `128` to an asymptotic bound.

The t41 geometry says that the corresponding asymptotic off-fiber condition is represented, after fixing a packet pair, by a Kummer-type surface birational to

\[
(E_\gamma\times E_{\gamma'})/\{\pm1\}.
\]

Therefore the receiver in (10.7) deliberately accepts an external mixed-incidence theorem rather than pretending that a one-dimensional genus-one bound controls the whole surface.

---

## 4. Why two local-energy directions are not enough

There is an exact combinatorial countermodel.

Take `H` states, put every state in its own row cell and its own column cell, but give every state the same squareclass.

Then both row and column local energies equal `H`, while

\[
A_1=H^2.
\]

Hence

\[
\boxed{\text{two-sided local near-linearity does not imply global near-linearity}.}
\tag{10.9}
\]

This stress test is part of the dedicated audit.

---

## 5. Uniform nonprincipal autocorrelation receiver for E4

Because squareclass translation is a permutation, Cauchy gives

\[
c(\kappa)
=\sum_s r(s)r(s\oplus\kappa)
\le \sum_s r(s)^2=A_1.
\]

Together with (10.2),

\[
A_1^2\le E_4\le A_1H^2,
\]

recovering the t41 universal bounds.

But tH10 records a sharper positive-counting receiver.

Let

\[
R_{\rm non}=\max_{\kappa\ne1}c(\kappa),
\qquad
S_{\rm non}=H^2-A_1.
\]

Then

\[
\boxed{
E_4
\le
A_1^2+R_{\rm non}(H^2-A_1).
}
\tag{10.10}
\]

Proof: for nonprincipal kernels, `c(k)^2 <= R_non c(k)` and their total mass is `H^2-A1`.

This exposes a clean sufficient route:

```text
A1 near-linear
AND every nonprincipal squareclass difference has subpolynomial multiplicity
=> E4 near-quadratic.
```

However tH10 does not assume the required uniform expansion theorem is true for Stage14.

---

## 6. Heavy/light receiver — uniform expansion is not necessary

Uniform control of every nonprincipal kernel may be too strong.  Fix a threshold `T>=0` and define

\[
\mathcal H_T=\{\kappa\ne1:c(\kappa)>T\},
\]

with heavy mass

\[
M_T=\sum_{\kappa\in\mathcal H_T}c(\kappa).
\]

Then

\[
\sum_{\substack{\kappa\ne1\\c(\kappa)\le T}}c(\kappa)^2
\le T(H^2-A_1-M_T),
\]

while the heavy part is at most `R_non M_T`.  Therefore

\[
\boxed{
E_4
\le
A_1^2
+T(H^2-A_1)
+(R_{\rm non}-T)M_T.
}
\tag{10.11}
\]

This is an important second receiver.

A later theorem does **not** need to prove `R_non=B^o(1)` if it can instead show that the kernels with large multiplicity carry sufficiently little total pair mass.

This is suited to a generic/exceptional split:

- generic transverse pairs should feed the light term;
- exceptional/isogenous or common-core pairs may feed the heavy mass `M_T`;
- an incidence theorem only has to make the heavy contribution small enough.

---

## 7. Fiber-multiplicity × support-expansion factorization

Let

\[
M=\max_s r(s),
\]

and let `S={s:r(s)>0}` be the occupied squareclass support.

For a nonprincipal difference `kappa`, define the unweighted support-difference multiplicity

\[
d_S(\kappa)
=\#\{s\in S:s\oplus\kappa\in S\}.
\]

Then

\[
c(\kappa)
=\sum_{s\in S\cap(S\oplus\kappa)}r(s)r(s\oplus\kappa)
\le M^2d_S(\kappa).
\]

Hence with

\[
D_{\rm non}=\max_{\kappa\ne1}d_S(\kappa),
\]

we have

\[
\boxed{R_{\rm non}\le M^2D_{\rm non}.}
\tag{10.12}
\]

This separates two mathematically different tasks:

1. **fiber control**: no squareclass itself carries too many physical states;
2. **support expansion**: the occupied squareclass set has few representations of each nontrivial difference.

A theorem may attack either factor using different geometry.

Combining (10.10) and (10.12),

\[
\boxed{
E_4
\le
A_1^2
+M^2D_{\rm non}(H^2-A_1).
}
\tag{10.13}
\]

Again, this is a receiver, not a claim that `D_non` is already small in Stage14.

---

## 8. Exponent ledger

Suppose a later application has the scale

\[
H\le B^{h+o(1)}.
\]

### Principal receiver

If

\[
L_P\le B^{\lambda+o(1)},
\qquad
I_{\rm gen}\le B^{g+o(1)},
\qquad
I_{\rm exc}\le B^{e+o(1)},
\]

then

\[
\boxed{
A_1\le B^{a+o(1)},
\qquad a=\max(\lambda,g,e).
}
\tag{10.14}
\]

### Uniform E4 receiver

If also

\[
R_{\rm non}\le B^{r+o(1)},
\]

then (10.10) gives

\[
\boxed{
E_4\le B^{q+o(1)},
\qquad q=\max(2a,r+2h).
}
\tag{10.15}
\]

### Heavy/light E4 receiver

If

\[
T\le B^{t+o(1)},
\quad
R_{\rm non}\le B^{r+o(1)},
\quad
M_T\le B^{m+o(1)},
\]

then

\[
\boxed{
q\le\max(2a,t+2h,r+m).
}
\tag{10.16}
\]

Thus near-quadratic fourth energy `q<=2h` can be obtained by the more flexible conditions

```text
a <= h,
t <= 0,
r + m <= 2h,
```

up to `o(1)` terms.

This explicitly allows a polynomially large worst nonprincipal kernel if the total mass of such heavy kernels is correspondingly sparse.

---

## 9. How a later t stage should hand results to tH10

A receiving stage should provide a record of the form

```text
SquareclassFiberEnergyPacket
  population_scale H
  chosen_partition P
  local_energy_bound L_P
  off_pair_split:
    generic incidence bound I_gen
    exceptional incidence bound I_exc
  squareclass_fiber_bound M
  support_difference_bound D_non            [optional]
  nonprincipal_kernel_bound R_non            [optional]
  heavy_threshold T                          [optional]
  heavy_pair_mass M_T                        [optional]
```

Not every optional field is needed.  Either the uniform route (10.10) or the heavy/light route (10.11) may be used.

The adapter then outputs an `A1` exponent and an `E4` exponent without altering the underlying live proof.

---

## 10. What tH10 does not prove

Stage14-tH10 does **not** prove:

- a global bound for the off-direction Kummer surface;
- a generic-transverse / exceptional-isogenous classification;
- `R_non=B^o(1)`;
- `D_non=B^o(1)`;
- a power-saving bound for `A1`;
- a power-saving bound for `E4`;
- the critical-square-root-strip saving;
- `A_{1,1}` power saving;
- `T=o(sqrt(B))`;
- perfect-cuboid nonexistence.

Its output is the exact reusable bookkeeping needed once any of those geometric/analytic inputs become available.

---

## Frozen t41 regression

```text
H                                      1120
A1                                     2368
same-direction local energy            2240
off-direction ordered collisions        128
E4                                 21193216
largest nonprincipal kernel              160
A1^2                                5607424
nonprincipal E4                     15585792
```

The uniform nonprincipal receiver gives the valid but non-sharp frozen bound

\[
E_4\le
2368^2+160(1120^2-2368)
=205932544.
\]

The point is not numerical sharpness.  It is that the exact missing input is now named: either reduce the nonprincipal maximum or prove a sparse-heavy-mass theorem.

---

## Boundary

```text
STAGE14_TH10=COMPLETE_SQUARECLASS_FIBER_AND_AUTOCORRELATION_INCIDENCE_TOOLBOX
TH_REQUIRES_FUTURE_T_RESULT=false
T41_KUMMER_ENERGY_BOUNDARY_IMPORTED=true
PRINCIPAL_PARTITION_IDENTITY_PROVED=true
TWO_SIDED_LOCAL_ENERGY_SHORTCUT_REJECTED=true
GENERIC_EXCEPTIONAL_OFF_FIBER_RECEIVER_DEFINED=true
UNIFORM_NONPRINCIPAL_E4_RECEIVER_PROVED=true
HEAVY_LIGHT_NONPRINCIPAL_E4_RECEIVER_PROVED=true
FIBER_TIMES_SUPPORT_EXPANSION_BOUND_PROVED=true
PRINCIPAL_AND_FOURTH_EXPONENT_LEDGER_PROVED=true
GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false
GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-tH11 build generic/exceptional Kummer-pair and heavy-kernel classification receivers if still independently useful; otherwise stress-test/PARK this second tH cycle
```
