# Stage14-t60 — polar Kummer factorization and one-side fourth-moment reduction

## Purpose

Merged Stage14-t59 reduces the dominant fixed-`U` invisible physical selector to only `B^{o(1)}` energy-balanced orthogonal rectangle families

\[
\mathcal R=\{A_j\times B_j\}_j,
\]

with pairwise-disjoint row projections `A_j`, pairwise-disjoint column projections `B_j`, and

\[
\Bigl(\sum_j |A_j|^2\Bigr)
\Bigl(\sum_j |B_j|^2\Bigr)
\le 2\Bigl(\sum_j |A_j||B_j|\Bigr)^2.
\tag{60.1}
\]

The remaining receiver is

```text
SharedUEnergyBalancedOrthogonalRectangleSecondMoment.
```

Merged Stage14-tH16 independently showed that two tempting direct routes do not close it:

1. quadratic reciprocity followed by a quadratic large sieve is circular because its coefficient energy is the unresolved fixed-`U` squareclass energy;
2. plain Cauchy over the full two-coordinate Mellin character universe loses the full same-modulus character-space factor.

Stage14-t60 keeps the exact t57 Mellin coefficient **matrix** intact instead of replacing it by entrywise absolute values.  A finite-dimensional polar/SVD factorization splits that matrix optimally between the row and column coordinates.  This proves that the t59 two-coordinate rectangle theorem follows from two explicit **one-side coefficient-weighted fourth moments**, both still averaged over the same auxiliary prime pair `(p,q)`.

This is a noncircular reduction only.  The two one-side fourth moments are not proved here, and no global Stage14 power saving is claimed.

---

## 1. Aggregate the t57 Mellin packet as a coefficient matrix

For one good split auxiliary prime `r`, put

\[
n_r=r-1,
\qquad
A_r(z)=\chi_r(z^2-1).
\]

Let

\[
\widehat A_r(\eta)
=\sum_{z\in\mathbf F_r^\times}A_r(z)\overline{\eta(z)}.
\]

Merged t57 gives

\[
K_r(t,x)
=\frac1{n_r^2}
\sum_{\eta,\xi}
\widehat A_r(\eta)\widehat A_r(\xi)
(\xi\eta^{-1})(t)(\eta\xi)(x).
\tag{60.2}
\]

Write

\[
\alpha=\xi\eta^{-1},
\qquad
\beta=\eta\xi.
\]

Several ordered pairs `(eta,xi)` may give the same `(alpha,beta)`.  Therefore define the **aggregated one-prime coefficient matrix**

\[
\boxed{
C_r(\alpha,\beta)
=\frac1{n_r^2}
\sum_{\substack{\eta,\xi:\\\xi\eta^{-1}=\alpha\\\eta\xi=\beta}}
\widehat A_r(\eta)\widehat A_r(\xi).
}
\tag{60.3}
\]

Then

\[
\boxed{
K_r(t,x)=\sum_{\alpha,\beta}
C_r(\alpha,\beta)\alpha(t)\beta(x).
}
\tag{60.4}
\]

For `r == 1 mod 4`, t57 evenness kills all odd local modes.  On the surviving even-mode subgroup, the map

\[
(\eta,\xi)\mapsto(\alpha,\beta)
\]

has fiber size at most `2`: its kernel is given by

\[
\eta=\xi,\qquad \eta^2=1.
\]

Hence aggregation costs only an absolute constant in spectral `L2`:

\[
\boxed{
\|C_r\|_{HS}^2
\le 2
\left(\frac{r-3}{r-1}\right)^2
\le2.
}
\tag{60.5}
\]

The deterministic audit reconstructs (60.4) on every nonzero `(t,x)` for the split test primes and verifies the exact fiber bound `<=2`.

---

## 2. Two-prime coefficient matrix is a tensor product, with the modulus still shared

For distinct good split primes `p,q`, CRT gives

\[
K_{pq}(t,x)=K_p(t,x)K_q(t,x).
\]

Let a row character at modulus `pq` be the ordered pair

\[
\boldsymbol\alpha=(\alpha_p,\alpha_q)
\]

and similarly

\[
\boldsymbol\beta=(\beta_p,\beta_q).
\]

Then

\[
\boxed{
C_{pq}=C_p\otimes C_q
}
\tag{60.6}
\]

and

\[
K_{pq}(t,x)
=\sum_{\boldsymbol\alpha,\boldsymbol\beta}
C_{pq}(\boldsymbol\alpha,\boldsymbol\beta)
\boldsymbol\alpha(t)\boldsymbol\beta(x).
\tag{60.7}
\]

The Hilbert--Schmidt energy satisfies

\[
\boxed{
\|C_{pq}\|_{HS}^2
=\|C_p\|_{HS}^2\|C_q\|_{HS}^2
\le4.
}
\tag{60.8}
\]

This does **not** create independent auxiliary moduli.  The single ordered pair `(p,q)` indexes one coefficient matrix `C_{pq}` and both coordinate character systems simultaneously.

```text
SHARED_AUXILIARY_MODULUS_PRESERVED=true
INDEPENDENT_PI_V_MODULUS_TENSORIZATION_ALLOWED=false
```

---

## 3. Rectangle trace is a matrix bilinear form

Fix one t59 energy-balanced orthogonal rectangle family

\[
\mathcal R=\{A_j\times B_j\}_j.
\]

For one auxiliary pair `(p,q)`, define the row and column Fourier sums

\[
X_j(\boldsymbol\alpha)
=\sum_{\pi\in A_j}\boldsymbol\alpha(t(\pi)),
\tag{60.9}
\]

and

\[
Y_j(\boldsymbol\beta)
=\sum_{V\in B_j}\boldsymbol\beta(x(V)).
\tag{60.10}
\]

The physical unit-weight rectangle trace is exactly

\[
\begin{aligned}
T_{\mathcal R}(p,q)
&=\sum_j\sum_{\pi\in A_j}\sum_{V\in B_j}
K_{pq}(t(\pi),x(V))\\
&=\sum_j
\sum_{\boldsymbol\alpha,\boldsymbol\beta}
C_{pq}(\boldsymbol\alpha,\boldsymbol\beta)
X_j(\boldsymbol\alpha)Y_j(\boldsymbol\beta).
\end{aligned}
\tag{60.11}
\]

Thus the two-coordinate analytic problem is encoded in one finite matrix `C_{pq}` rather than in an entrywise list of Mellin modes.

The raw physical trace is a sufficient object: merged t55 already controls the constant-density mean term, so a target-scale second moment for the raw physical trace gives the centered selector target by

\[
|G-M|^2\le2|G|^2+2|M|^2.
\tag{60.12}
\]

No centered-weight factorization is being assumed.

---

## 4. Polar factorization keeps spectral cancellation that entrywise Cauchy destroys

Take a singular-value decomposition

\[
C_{pq}=U_{pq}\Sigma_{pq}V_{pq}^*.
\]

Define the two half matrices

\[
L_{pq}=U_{pq}\Sigma_{pq}^{1/2},
\qquad
R_{pq}=V_{pq}\Sigma_{pq}^{1/2}.
\tag{60.13}
\]

Then

\[
\boxed{C_{pq}=L_{pq}R_{pq}^*.}
\tag{60.14}
\]

For every rectangle `j` and singular-mode index `h`, put

\[
\mathcal X_{j,h}(p,q)
=\sum_{\boldsymbol\alpha}
X_j(\boldsymbol\alpha)L_{pq}(\boldsymbol\alpha,h),
\tag{60.15}
\]

\[
\mathcal Y_{j,h}(p,q)
=\sum_{\boldsymbol\beta}
Y_j(\boldsymbol\beta)\overline{R_{pq}(\boldsymbol\beta,h)}.
\tag{60.16}
\]

Then (60.11) becomes

\[
\boxed{
T_{\mathcal R}(p,q)
=\sum_{j,h}
\mathcal X_{j,h}(p,q)
\mathcal Y_{j,h}(p,q).
}
\tag{60.17}
\]

Cauchy is now taken only after the signed/complex Mellin matrix has been aggregated and polar-factorized:

\[
\boxed{
|T_{\mathcal R}(p,q)|^2
\le
\mathcal E_A(p,q)\mathcal E_B(p,q),
}
\tag{60.18}
\]

where

\[
\mathcal E_A(p,q)
=\sum_{j,h}|\mathcal X_{j,h}(p,q)|^2,
\tag{60.19}
\]

\[
\mathcal E_B(p,q)
=\sum_{j,h}|\mathcal Y_{j,h}(p,q)|^2.
\tag{60.20}
\]

Equivalently,

\[
\mathcal E_A
=\sum_j
\langle X_j,(C_{pq}C_{pq}^*)^{1/2}X_j\rangle,
\tag{60.21}
\]

\[
\mathcal E_B
=\sum_j
\langle Y_j,(C_{pq}^*C_{pq})^{1/2}Y_j\rangle.
\tag{60.22}
\]

This is the exact polar form.  It does **not** replace `C_{pq}` by `|C_{pq}|` entrywise.  Consequently the cancellation already encoded in the Kummer Mellin coefficients is retained.

This is precisely the point at which tH16's naive full-mode Cauchy is improved: tH16 summed the complete character-pair universe after discarding the matrix geometry, whereas (60.18) uses the optimal Hilbert-space split of the actual coefficient matrix.

No estimate is claimed yet for (60.19)--(60.22).

---

## 5. Average over the same auxiliary prime pairs

Summing (60.18) over the same ordered distinct split-prime pairs and applying Cauchy only in that common pair index gives

\[
\boxed{
\sum_{p\ne q}|T_{\mathcal R}(p,q)|^2
\le
\left(\sum_{p\ne q}\mathcal E_A(p,q)^2\right)^{1/2}
\left(\sum_{p\ne q}\mathcal E_B(p,q)^2\right)^{1/2}.
}
\tag{60.23}
\]

The two factors are one-coordinate objects, but they are **not** evaluated on independent prime families.  Both are indexed by exactly the same `(p,q)` amplifier set.

This produces two new one-side contracts.

### Canonical-prime side

```text
CanonicalPrimePolarKummerFourthMoment
```

is the estimate

\[
\boxed{
\sum_{p\ne q}\mathcal E_A(p,q)^2
\ll
P^2
\left(\sum_j |A_j|^2\right)
B^{o(1)}.
}
\tag{60.24}
\]

### Primitive-cover side

```text
PrimitiveCoverPolarKummerFourthMoment
```

is

\[
\boxed{
\sum_{p\ne q}\mathcal E_B(p,q)^2
\ll
P^2
\left(\sum_j |B_j|^2\right)
B^{o(1)}.
}
\tag{60.25}
\]

These are genuine fourth moments because `mathcal E_A` and `mathcal E_B` are already quadratic spectral energies.

They are strictly narrower than tH16's `SameModulusToroidalKummerLargeSieve`: each sees only one physical coordinate after the exact coefficient matrix has been split, while the shared auxiliary pair remains common at the outer average.

---

## 6. The two one-side moments close the t59 receiver with no rectangle-count loss

Assume (60.24) and (60.25).  Then (60.23) gives

\[
\sum_{p\ne q}|T_{\mathcal R}(p,q)|^2
\ll
P^2
\left[
\left(\sum_j|A_j|^2\right)
\left(\sum_j|B_j|^2\right)
\right]^{1/2}
B^{o(1)}.
\tag{60.26}
\]

By the exact t59 aspect-ratio energy balance (60.1),

\[
\boxed{
\sum_{p\ne q}|T_{\mathcal R}(p,q)|^2
\ll
P^2
\left(\sum_j|A_j||B_j|\right)
B^{o(1)}.
}
\tag{60.27}
\]

This is exactly `SharedUEnergyBalancedOrthogonalRectangleSecondMoment` for one t59 family.

There are only `B^{o(1)}` t59 families, so legal polylogarithmic recombination then yields the t58 canonical-prime/`delta` toroidal second moment, followed by the already-proved t57/t56/tH15 implication chain.

The number of rectangles inside a family never appears as a Cauchy factor.

```text
POLAR_ONE_SIDE_FOURTH_MOMENT_PAIR_IMPLIES_T59_RECEIVER=true
RECTANGLE_COUNT_CAUCHY_FACTOR_USED=false
```

---

## 7. What t60 does not prove

Neither (60.24) nor (60.25) follows from plain character orthogonality.

Indeed the one-side quadratic energy still contains the complete same-modulus character family hidden inside the positive operators

\[
(C_{pq}C_{pq}^*)^{1/2},
\qquad
(C_{pq}^*C_{pq})^{1/2}.
\]

Replacing either positive operator by the identity recovers the ordinary full-character Parseval loss identified by tH16.  Thus

```text
NAIVE_ONE_SIDE_FULL_CHARACTER_ORTHOGONALITY_CLOSES_60_24=false
NAIVE_ONE_SIDE_FULL_CHARACTER_ORTHOGONALITY_CLOSES_60_25=false
```

Likewise, projecting first to the rational squarefree kernel `D_s` and using the tH16 quadratic frame again produces the unresolved squareclass coefficient energy and is still circular.

```text
QUADRATIC_SQUARECLASS_PRECOLLAPSE_ALLOWED=false
E4_COEFFICIENT_ENERGY_USED=false
```

The new reduction is therefore not a hidden proof of SMTKLS.  Its value is that the missing theorem is no longer intrinsically two-coordinate: it is a matched pair of one-coordinate fourth moments for the exact Kummer polar weights.

---

## 8. Relation to tH16 routes

Merged tH16 left two proof strategies:

```text
SameModulusToroidalKummerLargeSieve (SMTKLS)
ToroidalHyperbolicJacobiBridge (THJB)
```

Stage14-t60 changes their role.

- A proof of SMTKLS certainly implies the t59 receiver directly, but t60 shows that full SMTKLS is stronger than necessary for the rectangle packet.
- THJB remains a possible way to prove either one-side polar fourth moment after an additional arithmetic transform, but the hyperbola geometry itself has already been eliminated exactly by t59.
- The receiver-level obstruction is now the pair (60.24)--(60.25), not the broad phrase `SMTKLS or THJB`.

Thus tH16 is **consumed** as an applicability/failure audit.

---

## 9. tH decision

No Stage14-tH17 is needed at t60.

The new step is exact finite-dimensional linear algebra applied to the already-certified t57 coefficient packet and the already-merged t59 rectangle geometry.  It does not introduce a new external theorem source or a new support convention that requires an independent H-line.

The next live stage should attack the two one-side moments directly.  If t61 finds that one side requires a genuinely new theorem family not covered by tH3/tH4/tH16, that will be the correct trigger for tH17.

```text
TH16_CONSUMED=true
TH17_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH=false
```

---

## Locked boundary

```text
STAGE14_T60=COMPLETE_POLAR_KUMMER_ONE_SIDE_FOURTH_MOMENT_REDUCTION
MERGED_T59_IMPORTED=true
MERGED_TH16_IMPORTED=true
ONE_PRIME_AGGREGATED_MELLIN_COEFFICIENT_MATRIX_DEFINED=true
ONE_PRIME_MODE_MAP_FIBER_MAX=2
ONE_PRIME_AGGREGATED_MATRIX_HS2_LE_2=true
TWO_PRIME_COEFFICIENT_MATRIX_TENSOR_IDENTITY=true
TWO_PRIME_AGGREGATED_MATRIX_HS2_LE_4=true
POLAR_KUMMER_HALF_PACKET_FACTORIZATION_PROVED=true
SAME_AUXILIARY_PAIR_OUTER_AVERAGE_PRESERVED=true
INDEPENDENT_PI_V_MODULUS_TENSORIZATION_ALLOWED=false
CANONICAL_PRIME_POLAR_KUMMER_FOURTH_MOMENT_PROVED=false
PRIMITIVE_COVER_POLAR_KUMMER_FOURTH_MOMENT_PROVED=false
POLAR_ONE_SIDE_FOURTH_MOMENT_PAIR_IMPLIES_T59_RECEIVER=true
SHARED_U_ENERGY_BALANCED_ORTHOGONAL_RECTANGLE_SECOND_MOMENT_PROVED=false
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
TH16_CONSUMED=true
TH17_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH=false
NEXT=Stage14-t61 attack CanonicalPrimePolarKummerFourthMoment and PrimitiveCoverPolarKummerFourthMoment; first test whether one side is already covered by a tH4-compatible one-variable large-sieve/fourth-moment upgrade
```
