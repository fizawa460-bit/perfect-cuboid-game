# Stage14-tH13 R2 — twist-uniform sparse squareclass quadratic-character operator

## Purpose

Merged Stage14-t46 sharpens the original tH13 problem.  The moving family is not an arbitrary set of 544 unrelated conductors.  If

\[
\kappa_y=\operatorname{sqf}(F_y),
\]

then for fixed twist `tau`

\[
\kappa_{\tau,y}=\tau\kappa_y\quad\text{in }\mathbf Q^\times/\mathbf Q^{\times2},
\]

and, on a good odd canonical prime `ell`,

\[
\chi_{D(\tau\kappa)}(\ell)
=\chi_\tau(\ell)\chi_{D(\kappa)}(\ell).
\]

Thus every twist uses the same base matrix

\[
M(\ell,\kappa)=\chi_{D(\kappa)}(\ell),
\]

with `tau` acting only by a row sign, apart from the t44 `O(1)` exposed bad canonical-prime rows.  This extension replaces the arbitrary-conductor viewpoint of the first tH13 receiver by a twist-uniform squareclass-operator receiver.

No Stage14-t46 power saving is assumed.  No critical-strip power saving is claimed here.

---

## 1. Common refinement and exact coefficient formation

Work on one tH12 common disjoint refinement block `R`.  Let

\[
\mathcal L_R(Q)=\{\ell:Q<\ell\le2Q\}
\]

be the active canonical-prime rows and let `K_R` be the active base squareclass support.  The actual canonical-prime selector is retained before any large-sieve step:

\[
A_\ell
=\sum_{x\in R:\,\ell_x=\ell}a_x w_R(x).
\tag{H13R2.1}
\]

Collapse the partner side by **base squareclass**, not by the translated conductor:

\[
B_\kappa
=\sum_{y\in R:\,\kappa_y=\kappa}b_y v_R(y).
\tag{H13R2.2}
\]

Define

\[
E_\ell=\sum_\ell|A_\ell|^2,
\qquad
E_\kappa=\sum_\kappa|B_\kappa|^2,
\tag{H13R2.3}
\]

and support cardinalities

\[
N_\ell=|\operatorname{supp}A|,
\qquad
N_\kappa=|\operatorname{supp}B|.
\tag{H13R2.4}
\]

For unit state weights on the frozen reciprocal quotient,

```text
N_kappa = 544
E_kappa = A1 = 592
N_ell   = 87
E_ell   = 7184
```

The equality `E_kappa=A1` is an exact consequence of the squareclass multiplicity profile, not an asymptotic estimate.

---

## 2. Exact twist-uniform operator reduction

Let

\[
M_R(\ell,\kappa)=\chi_{D(\kappa)}(\ell).
\tag{H13R2.5}
\]

For a fixed twist `tau`, delete the t44 bad rows

\[
\mathcal B_\tau
=\{\ell\in\mathcal L_R(Q):\ell\mid\tau\}.
\tag{H13R2.6}
\]

On the remaining rows, let

\[
(U_\tau f)(\ell)=\chi_\tau(\ell)f(\ell).
\tag{H13R2.7}
\]

Then `U_tau` is a diagonal unitary sign matrix.  The nonprincipal part is obtained by deleting the single base column `kappa=tau` when that column is present.  Hence

\[
M_{R,\tau}^{\rm np}
=P_{\mathcal L\setminus\mathcal B_\tau}
U_\tau M_R P_{\kappa\ne\tau}.
\tag{H13R2.8}
\]

Therefore, exactly,

\[
\boxed{
\|M_{R,\tau}^{\rm np}\|_{2\to2}
\le \|M_R\|_{2\to2}.
}
\tag{H13R2.9}
\]

This is the principal reusable improvement supplied by t46: **one base operator norm controls every twist**.  Twist translation does not create a new conductor family or a new spectral problem.

For the generic nonprincipal contribution,

\[
S_{R,\tau}^{\rm np}
=\sum_{\ell\notin\mathcal B_\tau}
A_\ell\chi_\tau(\ell)
\sum_{\kappa\ne\tau}B_\kappa\chi_{D(\kappa)}(\ell),
\]

so

\[
\boxed{
|S_{R,\tau}^{\rm np}|
\le E_\ell^{1/2}E_\kappa^{1/2}\Lambda_R,
\qquad
\Lambda_R:=\|M_R\|_{2\to2}.
}
\tag{H13R2.10}
\]

The bound is uniform in `tau`.

---

## 3. Principal column and t44 bad rows stay separate

### Principal translated conductor

`t46` proves

\[
D(\tau\kappa)=1\iff\kappa=\tau.
\]

Thus the principal translated conductor is the one base column `kappa=tau`.  On good rows its two character factors multiply to one, so

\[
\boxed{
S_{R,\tau}^{\rm pr}
=B_\tau^{(\kappa)}\sum_{\ell\notin\mathcal B_\tau}A_\ell,
}
\tag{H13R2.11}
\]

where `B_tau^(kappa)` means the coefficient (H13R2.2) of the base squareclass `tau`.  For unit weights it is exactly `r(tau)=m_tau(1)`.

There is no character cancellation in this slice.  The safe bound is

\[
|S_{R,\tau}^{\rm pr}|
\le |B_\tau^{(\kappa)}|N_\ell^{1/2}E_\ell^{1/2}.
\tag{H13R2.12}
\]

Any improvement must come from an independent bound for `r(tau)` / the principal squareclass fiber.

### t44 exposed bad rows

For fixed `tau`, t44 gives only `O(1)` super-square-root canonical primes dividing `tau` (safe explicit envelope `<=16+o(1)`).  Route those rows before using (H13R2.10).  With

\[
E_{\ell,\rm bad}=\sum_{\ell\in\mathcal B_\tau}|A_\ell|^2,
\]

a safe energy estimate is

\[
|S_{R,\tau}^{\rm bad}|
\le |\mathcal B_\tau|^{1/2}
E_{\ell,\rm bad}^{1/2}
N_\kappa^{1/2}E_\kappa^{1/2}.
\tag{H13R2.13}
\]

`O(1)` rows do not by themselves give a power saving; their coefficient mass still has to be bounded.

---

## 4. Standard max-range quadratic large sieve

Let

\[
D(\kappa)\ll K.
\]

Heath-Brown's quadratic large sieve, after the finite fundamental-discriminant / 2-adic refinement, gives the operator estimate

\[
\boxed{
\Lambda_R^2
\ll_\varepsilon (K+Q)(KQ)^\varepsilon.
}
\tag{H13R2.14}
\]

Consequently

\[
\boxed{
|S_{R,\tau}^{\rm np}|
\ll B^{o(1)}(K+Q)^{1/2}E_\ell^{1/2}E_\kappa^{1/2}.
}
\tag{H13R2.15}
\]

This is already twist-uniform.  The t46 conductor reduction is essential because `K` is now the **base** conductor range, not the much larger translated conductor range.

However, at the critical strip

\[
Q=B^{1/2+o(1)},
\qquad
K\le B^{4+o(1)},
\]

(H13R2.14) pays

\[
\Lambda_R\ll B^{2+o(1)}.
\tag{H13R2.16}
\]

So the standard max-range theorem still does not close the critical strip.

---

## 5. Reciprocity / dual large sieve

On the finitely refined good classes, quadratic reciprocity transposes the same matrix up to fixed local signs.  By Hilbert-space duality,

\[
\|M_R\|_{2\to2}=\|M_R^*\|_{2\to2}.
\]

Applying the quadratic large sieve after reciprocity gives the same `K+Q` envelope.  Therefore

```text
standard QLS             valid, twist-uniform, K+Q
reciprocity / dual QLS   valid, same operator norm, same K+Q
```

Duality is structurally useful but does not replace the conductor range `K` by `N_kappa`.

---

## 6. Cardinality-only bound and its exact limitation

Since every matrix entry has modulus at most one,

\[
\Lambda_R^2
\le \|M_R\|_{\rm HS}^2
\le N_\ell N_\kappa.
\tag{H13R2.17}
\]

Thus

\[
\boxed{
|S_{R,\tau}^{\rm np}|
\le (N_\ell N_\kappa)^{1/2}
E_\ell^{1/2}E_\kappa^{1/2}.
}
\tag{H13R2.18}
\]

This uses sparse support cardinality, but it is exactly the `L1 from L2` / Hilbert-Schmidt bound.  It contains no character cancellation.

### Countermodel: cardinality + minimal energy + simple factor structure still do not suffice

Fix any finite set `P` of odd row primes and put

\[
M_0=8\prod_{p\in P}p.
\]

By Dirichlet's theorem there are arbitrarily many distinct primes

\[
q_j\equiv1\pmod{M_0}.
\]

Take base squareclasses `kappa_j=q_j`.  Then each `kappa_j` is itself prime, the support has minimal unit-weight energy

\[
E_\kappa=N_\kappa,
\]

and for every `p in P`

\[
\chi_{D(\kappa_j)}(p)=1.
\]

The character matrix is the all-ones matrix, so

\[
\Lambda^2=N_\ell N_\kappa.
\tag{H13R2.19}
\]

Therefore none of the following, alone, can imply a sparse quadratic large-sieve gain:

- small support cardinality;
- minimal second energy `E_kappa=N_kappa`;
- squarefreeness;
- bounded / extremely simple prime-factor structure.

A universal replacement `K -> N_kappa` in Heath-Brown's bound is false without an additional anti-coherence/distribution hypothesis.

---

## 7. Known sparse-moduli large sieve: useful comparison, not the missing theorem

Baier's sparse-moduli large sieve is genuinely cardinality-sensitive only after a quantitative hypothesis that the modulus set is well distributed in short arithmetic progressions.  Its theorem is for additive fractions `a/q`, summing over the reduced residue classes for each selected modulus.

A primitive quadratic character may be Gauss-expanded.  For a dyadic base-conductor support `D(kappa)~K_0`, Cauchy in the Gauss variable gives the valid domination

\[
\sum_{\kappa}
\left|\sum_\ell A_\ell\chi_{D(\kappa)}(\ell)\right|^2
\le
\sum_{D\in\mathcal D}
\sum_{a\bmod |D|}^{*}
\left|\sum_\ell A_\ell e(a\ell/|D|)\right|^2.
\tag{H13R2.20}
\]

If Baier's progression-distribution hypothesis holds with parameter `X_AP>=1`, his sparse additive theorem gives schematically

\[
\Lambda_R^2
\ll
Q+K_0 X_{\rm AP}B^{o(1)}
\bigl(Q^{1/2}+N_\kappa\bigr).
\tag{H13R2.21}
\]

This is **not** a direct sparse quadratic-character theorem.  The Gauss/Cauchy passage pays for all reduced additive frequencies.

At the present critical endpoint `Q=B^(1/2+o(1))`, `K_0=B^(4+o(1))`, even the optimistic `X_AP=B^o(1)` version has a large-sieve constant of exponent at least `4+1/4`, hence is worse than the standard quadratic `K+Q` constant of exponent `4`.

So existing sparse-moduli technology does not solve the Stage14 operator merely because the base support is sparse.  It does identify a possible structural certificate — progression distribution — but a **one-character quadratic sparse theorem** or a different spectral argument is still required.

---

## 8. Exact squareclass-support spectral receiver

The t46 base operator has stronger structure than an arbitrary sparse modulus set.  Consider its row Gram matrix

\[
G_R=M_RM_R^*.
\]

Because each column is one quadratic character,

\[
\boxed{
G_R(\ell,\ell')
=\sum_{\kappa\in\mathcal K_R}
\chi_{D(\kappa)}(\ell\ell').
}
\tag{H13R2.22}
\]

This identity is exact, including zero character values.

For the diagonal,

\[
0\le G_R(\ell,\ell)\le N_\kappa.
\tag{H13R2.23}
\]

Define the squareclass-support two-row bias

\[
C_R(\ell,\ell')
:=\sum_{\kappa\in\mathcal K_R}
\chi_{D(\kappa)}(\ell\ell')
\quad(\ell\ne\ell').
\tag{H13R2.24}
\]

and

\[
\mathfrak R_1
:=\max_\ell\sum_{\ell'\ne\ell}|C_R(\ell,\ell')|,
\qquad
\mathfrak R_2
:=\sum_{\ell\ne\ell'}|C_R(\ell,\ell')|^2.
\tag{H13R2.25}
\]

Gershgorin and the Frobenius bound for the off-diagonal Gram matrix give

\[
\boxed{
\Lambda_R^2
\le
N_\kappa+\min\{\mathfrak R_1,\mathfrak R_2^{1/2}\}.
}
\tag{H13R2.26}
\]

This is an unconditional **receiver identity/bound**, not a cancellation theorem.  It isolates the exact missing arithmetic input: cancellation of the actual Stage14 squareclass support against the products of two canonical-prime row characters.

A direct sparse-operator theorem of the natural near-orthogonality size would be

\[
\boxed{
\Lambda_R^2
\ll B^{o(1)}(N_\ell+N_\kappa).
}
\tag{H13R2.27}
\]

for the actual Stage14 support.  Such a theorem would be cardinality-sensitive and twist-uniform.  It is **not** a consequence of known generic large-sieve theory or of `E_kappa` alone; (H13R2.19) is the obstruction.

### Frozen diagnostic only

`t46` records

```text
rows N_ell                       87
columns N_kappa                 544
row squared norms           540..544
max |off-diagonal row corr|      81
```

Hence the crude frozen Gershgorin consequence is

\[
\Lambda^2\le544+86\cdot81=7510.
\tag{H13R2.28}
\]

This is substantially below the Hilbert-Schmidt square `87*544=47328`, but it is only a finite `B=10000` diagnostic.  It is not promoted to an asymptotic theorem.

---

## 9. Coefficient-sensitive dispersion / product-squareclass receiver

The operator norm is uniform in all partner coefficients.  If the actual `B_kappa` coefficients have extra structure, expand before taking the operator norm:

\[
\|M_RB\|_2^2
=\sum_{\ell}
\left|\sum_\kappa B_\kappa\chi_{D(\kappa)}(\ell)\right|^2.
\tag{H13R2.29}
\]

The diagonal is at most

\[
N_\ell E_\kappa.
\tag{H13R2.30}
\]

For `kappa != kappa'`, the product of the two primitive quadratic characters is a (possibly imprimitive) quadratic character.  Define the weighted pair-character coefficients by grouping equal product characters:

\[
\Gamma_R(\psi)
=\sum_{\substack{\kappa\ne\kappa'\\
\chi_{D(\kappa)}\chi_{D(\kappa')}=\psi}}
B_\kappa\overline{B_{\kappa'}}
\tag{H13R2.31}
\]

and prime correlation

\[
P_R(\psi)=\sum_{\ell\in\mathcal L_R(Q)}\psi(\ell).
\tag{H13R2.32}
\]

Then exactly

\[
\boxed{
\|M_RB\|_2^2
\le N_\ell E_\kappa
+\left|\sum_{\psi\ne1}\Gamma_R(\psi)P_R(\psi)\right|.
}
\tag{H13R2.33}
\]

By Cauchy,

\[
\boxed{
\|M_RB\|_2^2
\le N_\ell E_\kappa
+E_\times^{1/2}H_\times^{1/2},
}
\tag{H13R2.34}
\]

where

\[
E_\times=\sum_{\psi\ne1}|\Gamma_R(\psi)|^2,
\qquad
H_\times=\sum_{\psi\in\operatorname{supp}\Gamma_R}|P_R(\psi)|^2.
\tag{H13R2.35}
\]

This is the coefficient-sensitive dispersion receiver.  For unit squareclass multiplicity coefficients it is the same squareclass-autocorrelation/fourth-energy phenomenon already isolated by tH9/tH10, now attached directly to the t46 base operator.

`t46` proves only `E_kappa=A1`; it does **not** prove a favorable asymptotic bound for `E_times` or `H_times`.  Therefore no power saving is inferred here.

---

## 10. What factor structure can actually buy

The conductor maximum `K` can be avoided only when one proves an additional statement about the actual Stage14 support.  Reusable sufficient inputs include:

1. **row-spectral anti-coherence:** a bound for `R1`, `R2`, or directly `||M_R||`;
2. **squareclass progression distribution:** uniform control of the base squareclasses / discriminants in the residue classes relevant to products `ell*ell'`;
3. **weighted product-character energy:** a favorable `E_times` together with a second moment for `P_R(psi)`;
4. **structural support decomposition:** a disjoint factorization into subfamilies on which one of the preceding certificates is provable.

What is not enough:

```text
squarefree conductor                         not enough
few prime factors                            not enough
small support cardinality                    not enough
E_kappa comparable to support cardinality    not enough
translation by tau                           only gives uniformity, not cancellation
```

The countermodel in section 6 already has prime squareclasses and minimal energy, so a vague `factor structure` assumption cannot replace an actual residue/spectral certificate.

---

## 11. Critical-strip exponent ledger

Use the notation requested by t46/t47:

\[
Q=B^{1/2+o(1)},
\qquad
K\le B^{4+o(1)}.
\]

Write

\[
N_\ell=B^{\alpha+o(1)},
\quad
N_\kappa=B^{\beta+o(1)},
\quad
E_\ell=B^{e_\ell+o(1)},
\quad
E_\kappa=B^{e_\kappa+o(1)}.
\tag{H13R2.36}
\]

### Standard / dual quadratic large sieve

\[
\boxed{
\operatorname{exp}|S|_{\rm QLS}
=\frac{e_\ell+e_\kappa+4}{2}.
}
\tag{H13R2.37}
\]

The reciprocity-dual orientation has the same exponent.

### Cardinality / Hilbert-Schmidt

\[
\boxed{
\operatorname{exp}|S|_{\rm HS}
=\frac{e_\ell+e_\kappa+\alpha+\beta}{2}.
}
\tag{H13R2.38}
\]

This can beat the max-range QLS numerically when the support is sparse, but it is exactly the trivial cardinality bound and contains zero cancellation.

### Spectral receiver

If

\[
\mathfrak R_1=B^{g_1+o(1)},
\qquad
\mathfrak R_2=B^{g_2+o(1)},
\]

then (H13R2.26) gives

\[
\lambda_{\rm spec}
=\max\{\beta,\min(g_1,g_2/2)\},
\]

and

\[
\boxed{
\operatorname{exp}|S|_{\rm spec}
=\frac{e_\ell+e_\kappa+\lambda_{\rm spec}}2.
}
\tag{H13R2.39}
\]

A near-orthogonality theorem (H13R2.27) would have

\[
\lambda_{\rm near}=\max(\alpha,\beta),
\]

hence save

\[
\frac{\min(\alpha,\beta)}2
\]

in the bilinear amplitude relative to Hilbert-Schmidt.

### Known sparse additive-moduli route after Gauss expansion

If the dyadic conductor scale is `B^4`, the Baier-type bound (H13R2.21) has large-sieve constant exponent

\[
4+x_{\rm AP}+\max(1/4,\beta),
\tag{H13R2.40}
\]

where `X_AP=B^(x_AP+o(1))` and `x_AP>=0`.  It is therefore not competitive with the standard quadratic exponent `4` at the critical endpoint.

### Weighted dispersion

Write

\[
E_\times=B^{e_\times+o(1)},
\qquad
H_\times=B^{h_\times+o(1)}.
\]

Then from (H13R2.34) and Cauchy in the prime coefficient,

\[
\boxed{
\operatorname{exp}|S|_{\rm disp}
=\frac{e_\ell+\max\{\alpha+e_\kappa,(e_\times+h_\times)/2\}}2.
}
\tag{H13R2.41}
\]

This is the correct ledger for a t47 product-character-energy attack.

---

## 12. The two-local `1/4` detector is a separate gate

The t45 positivity detector is

\[
1_{N=\square}
\le
\frac14(1+\chi_x(N)+\chi_y(N)+\chi_x(N)\chi_y(N)).
\tag{H13R2.42}
\]

Even a perfect bound for every nonconstant operator term leaves the constant contribution

\[
\frac14\times\text{ambient candidate mass}.
\]

Therefore

\[
\boxed{
\text{operator cancellation does not remove the fixed two-local constant term.}
}
\tag{H13R2.43}
\]

There are two valid ways for t47 to proceed:

1. **bypass the fixed positivity detector** and estimate the exact squareclass/twist convolution by a genuine squareclass operator/orthogonality theorem;
2. use a **growing auxiliary test family / square sieve**, where the diagonal constant term decays with the number of auxiliary tests and the operator receiver controls the resulting correlations.

Invalid transfer:

```text
two fixed endogenous local tests
+ cancellation in their nonconstant terms
=> power-saving square incidence
```

The implication is false because the `1/4` term remains.

---

## 13. Stage14-t47 receiver / theorem contract

The live t47 block may invoke tH13 R2 only after it supplies the following data on the **same common refinement**:

```text
SquareclassOperatorBlock:
  prime_scale_Q
  base_conductor_max_K
  canonical_coefficients A_ell including selector weight
  squareclass_coefficients B_kappa
  E_ell
  E_kappa
  N_ell
  N_kappa
  principal coefficient B_tau^(kappa)
  t44 bad-row set B_tau
```

It then has the unconditional receiver

\[
|S_{R,\tau}^{\rm np}|
\le E_\ell^{1/2}E_\kappa^{1/2}
\min\left\{
B^{o(1)}(K+Q)^{1/2},
(N_\ell N_\kappa)^{1/2},
\bigl(N_\kappa+\min(\mathfrak R_1,\mathfrak R_2^{1/2})\bigr)^{1/2}
\right\}.
\tag{H13R2.44}
\]

The third term is useful only after `R1/R2` are actually bounded; defining them is not a saving theorem.

### Preferred new theorem target

The cleanest t47 theorem target is the Stage14-specific sparse squareclass large sieve

\[
\boxed{
\sum_{\ell\in\mathcal L_R(Q)}
\left|\sum_{\kappa\in\mathcal K_R}b_\kappa
\chi_{D(\kappa)}(\ell)\right|^2
\ll B^{o(1)}(N_\ell+N_\kappa)
\sum_\kappa|b_\kappa|^2.
}
\tag{H13R2.45}
\]

for the **actual Stage14 squareclass support**, uniformly on the required common refinements.  This theorem is not known from cardinality alone; it must be proved from Stage14-specific residue/factor/spectral structure.

An alternative accepted contract is a coefficient-sensitive bound from (H13R2.34) strong enough to improve the ledger (H13R2.41).

Finally, t47 must separately state how it removes/bypasses the detector constant term (H13R2.42).

---

## 14. Failure boundary

The following claims remain false / unproved:

```text
544 frozen squareclasses imply asymptotic sparse LS saving                     false
E_kappa alone implies character anti-coherence                                 false
squarefree / few-factor base conductors imply anti-coherence                    false
reciprocity changes K+Q into cardinality range                                  false
known sparse additive-moduli LS directly supplies the desired quadratic bound   false
operator cancellation removes the two-local 1/4 constant                       false
Stage14-t46 power saving                                                         unproved
critical sqrt-ell strip power saving                                             unproved
```

What tH13 R2 **does** close is the adapter problem: all twists are reduced to one base squareclass operator, the exact energy inputs are identified, the standard/dual/sparse/spectral/dispersion routes are separated, and the precise missing theorem is exposed for Stage14-t47.

---

## 15. Boundary

```text
STAGE14_TH13_R2=COMPLETE_TWIST_UNIFORM_SPARSE_SQUARECLASS_OPERATOR_RECEIVER
MERGED_T46_TWIST_TRANSLATION_IMPORTED=true
ARBITRARY_544_CONDUCTOR_MODEL_SUPERSEDED=true
ALL_TWISTS_SHARE_ONE_BASE_OPERATOR=true
TWIST_ROW_SIGN_IS_UNITARY=true
PRINCIPAL_TRANSLATED_CONDUCTOR_COLUMN_SEPARATED=true
PRINCIPAL_MULTIPLICITY_UNIT_WEIGHTS=r(tau)
T44_TAU_BAD_CANONICAL_ROWS_RETAINED=true
CANONICAL_PRIME_SELECTOR_WEIGHT_PRESERVED=true
SQUARECLASS_ENERGY_E_KAPPA_EXPLICIT=true
CANONICAL_PRIME_ENERGY_E_ELL_EXPLICIT=true
STANDARD_MAX_RANGE_QUADRATIC_LS_RECEIVER=true
RECIPROCITY_DUAL_LS_RECEIVER=true
CARDINALITY_HILBERT_SCHMIDT_RECEIVER=true
KNOWN_SPARSE_ADDITIVE_MODULI_ROUTE_COMPARED=true
KNOWN_SPARSE_ADDITIVE_MODULI_ROUTE_CLOSES_CRITICAL_STRIP=false
SQUARECLASS_ROW_GRAM_IDENTITY_EXACT=true
SPECTRAL_R1_R2_RECEIVER=true
WEIGHTED_PRODUCT_CHARACTER_DISPERSION_RECEIVER=true
CARDINALITY_PLUS_E_KAPPA_ALONE_GIVES_CANCELLATION=false
SIMPLE_FACTOR_STRUCTURE_ALONE_GIVES_CANCELLATION=false
SPARSE_CARDINALITY_COUNTERMODEL_RETAINED=true
CRITICAL_Q_EXPONENT=1/2
SAFE_BASE_K_EXPONENT=4
STANDARD_QLS_OPERATOR_SQUARED_EXPONENT=4
STANDARD_QLS_AMPLITUDE_COST_EXPONENT=2
TWO_LOCAL_FILTER_CONSTANT_TERM=1/4
OPERATOR_CANCELLATION_REMOVES_TWO_LOCAL_CONSTANT_TERM=false
STAGE14_T46_POWER_SAVING_ASSUMED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
GENERIC_CROSS_GOOD_GLOBAL_POWER_SAVING_PROVED=false
NEXT=Stage14-t47 prove a Stage14-specific sparse squareclass spectral/dispersion theorem and separately remove or bypass the fixed two-local 1/4 detector baseline
```

## References

- D. R. Heath-Brown, *A mean value estimate for real character sums*, Acta Arith. 72 (1995), 235–275.
- L. Goldmakher and B. Louvel, *A quadratic large sieve inequality over number fields*, Math. Proc. Cambridge Philos. Soc. 154 (2013), 193–212.
- S. Baier, *On the large sieve with sparse sets of moduli*, arXiv:math/0512228 (2005).  The sparse improvement requires quantitative distribution of the modulus set in arithmetic progressions; it is not a cardinality-only theorem.
