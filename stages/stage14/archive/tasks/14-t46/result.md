# Stage14-t46 — twist-translation conductor energy and base quadratic-character operator

## Purpose

Stage14-t45 reduced the fixed-partner generic cross-good Kummer condition to a genuine one-dimensional quadratic character

\[
\chi_{D_{\tau,y}}(\ell_x),
\qquad
D_{\tau,y}=D(\operatorname{sqf}(\tau F_y)),
\]

but observed 544 moving conductors for every frozen heavy twist.  Stage14-t46 asks whether those conductors are genuinely new as `tau` varies, and whether their multiplicity/energy can be expressed in already-known squareclass data.

The answer is yes: the apparent many-conductor family is a twist-translation of one fixed squareclass spectrum.

---

## 1. Exact twist-translation lemma

Write

\[
\kappa_y=\operatorname{sqf}(|F_y|)\in \mathbf Q^\times/\mathbf Q^{\times2}
\]

using the positive squarefree representative.  For fixed squareclass twist `tau`, define

\[
\kappa_{\tau,y}=\operatorname{sqf}(\tau\kappa_y).
\]

Multiplication by `tau` is an involution:

\[
\boxed{
\kappa_y\mapsto \tau\kappa_y,
\qquad
\tau(\tau\kappa_y)=\kappa_y.
}
\tag{46.1}
\]

The positive fundamental-discriminant map

\[
D(k)=
\begin{cases}
k,&k\equiv1\pmod4,\\4k,&\text{otherwise}
\end{cases}
\]

is injective on positive squarefree `k`.  Therefore for every fixed `tau`, the multiset

\[
\{D_{\tau,y}:y\}
\]

has exactly the same multiplicity profile as the original squareclass multiset

\[
\{\kappa_y:y\}.
\]

Consequently, if

\[
r(\kappa)=\#\{y:\kappa_y=\kappa\},
\qquad
A_1=\sum_\kappa r(\kappa)^2,
\]

then exactly

\[
\boxed{
\sum_D m_\tau(D)^2=A_1
}
\tag{46.2}
\]

for every `tau`, where `m_tau(D)` is the multiplicity of translated conductor `D`.

This removes the t45 interpretation that each twist brings an unrelated new 544-conductor family.

---

## 2. Principal conductor slice is already a squareclass fiber

The translated character is principal exactly when

\[
D_{\tau,y}=1.
\]

Because `D(k)=1` iff `k=1`, this is equivalent to

\[
\tau\kappa_y=1
\quad\Longleftrightarrow\quad
\kappa_y=\tau.
\]

Hence

\[
\boxed{
m_\tau(1)=r(\tau).}
\tag{46.3}
\]

So the principal-conductor piece required by t45/tH13 is not a new exceptional family.  It is exactly the existing target squareclass fiber.

---

## 3. Twist dependence factors out as a row character

For an odd good canonical prime `ell` with

\[
\ell\nmid 2\tau\kappa,
\]

we have

\[
\chi_{D(\tau\kappa)}(\ell)
=
\left(\frac{\tau\kappa}{\ell}\right)
=
\left(\frac{\tau}{\ell}\right)
\left(\frac{\kappa}{\ell}\right).
\]

Therefore

\[
\boxed{
\chi_{D(\tau\kappa)}(\ell)
=
\chi_\tau(\ell)\chi_{D(\kappa)}(\ell).
}
\tag{46.4}
\]

The factor `chi_tau(ell)` depends only on the row/canonical prime.  Thus every twist uses the same base matrix

\[
M(\ell,\kappa)=\chi_{D(\kappa)}(\ell)
\]

up to multiplication of rows by signs and removal of the `O(1)` `tau`-bad canonical-prime rows already isolated in t44.

This is the main structural reduction of t46:

\[
\boxed{
\text{many moving conductors}
\longrightarrow
\text{one twist-independent quadratic-character operator}.
}
\tag{46.5}
\]

---

## 4. Weighted coefficient-energy form

Aggregate arbitrary state coefficients by canonical prime and squareclass:

\[
A_\ell=\sum_{x:\ell_x=\ell}a_x,
\qquad
B_\kappa=\sum_{y:\kappa_y=\kappa}b_y.
\]

Then the rectangular character core is

\[
\boxed{
S_\tau
=
\sum_\ell A_\ell\chi_\tau(\ell)
\sum_\kappa B_\kappa\chi_{D(\kappa)}(\ell).
}
\tag{46.6}
\]

Define

\[
E_\ell=\sum_\ell|A_\ell|^2,
\qquad
E_\kappa=\sum_\kappa|B_\kappa|^2.
\]

For unit state weights, `E_kappa=A1` exactly.  This is the correct tH13 coefficient ledger: the conductor side pays squareclass energy, not the raw number of state-pairs.

A standard quadratic-large-sieve interface has the schematic shape

\[
\boxed{
|S_\tau|^2
\ll
E_\kappa(K+Q)E_\ell(KQ)^\varepsilon,
}
\tag{46.7}
\]

where `Q` is the canonical-prime range and `K` is the largest base squareclass conductor.

Independently of any arithmetic cancellation, the finite support gives the elementary Frobenius bound

\[
\boxed{
|S_\tau|^2
\le
|\mathcal K|\,|\mathcal L|\,E_\kappa E_\ell.
}
\tag{46.8}
\]

The two bounds expose the next issue cleanly: the classical large sieve sees the **diameter** `K`, while the elementary sparse bound sees only the **cardinality** but gives no cancellation.

---

## 5. Conductor exponent improves, but not enough

From the t40 physical bound

\[
|F|\le256B^4,
\]

we have

\[
\kappa\le256B^4,
\qquad
D(\kappa)\le2^{10}B^4.
\]

Thus after factoring out `tau`, the moving conductor may always be taken in the fixed base range

\[
\boxed{K\le2^{10}B^4.}
\tag{46.9}
\]

This removes the much larger naive translated conductor `D(tau*kappa)` from the analytic modulus.

However in the critical strip

\[
Q=B^{1/2+o(1)},
\qquad
K=B^{4+o(1)},
\]

so the standard max-range large sieve still carries a square-root cost

\[
(K+Q)^{1/2}=B^{2+o(1)}.
\]

Therefore t46 does **not** close the critical strip.  A cardinality/energy-sensitive sparse operator estimate, conductor compression, or a different centered dispersion is still needed.

---

## 6. Frozen audit

Reciprocal quotient:

```text
states                               560
distinct squareclasses               544
A1                                   592
max squareclass multiplicity           2

distinct canonical ell                87
canonical-ell unit energy            7184
max states / canonical ell             29
```

For every top-8 heavy twist:

```text
translated distinct conductors        544
translated conductor energy           592
translated max multiplicity             2
```

Thus the `544` reported in t45 is exactly invariant under twist translation.

The exact translation involution was checked 4480 times, and the character factorization (46.4) was checked 378232 times.

The frozen base matrix has 87 distinct `ell` rows and 544 squareclass columns.  Row squared norms lie in `[540,544]`; the largest off-diagonal row correlation is `81`, attained for `(ell1,ell2)=(229,461)` in this sample.  This is diagnostic only and is **not** promoted to an asymptotic spectral estimate.

Top heavy twists also satisfy

```text
tau     c(tau)   r(tau)=principal conductor multiplicity
91        40       1
209       38       1
286       34       0
34034     34       0
41        32       1
329       32       0
4641      32       0
11        30       1
```

---

## 7. The detector baseline remains separate

Stage14-t45 already proved that two endogenous local tests give

\[
\frac{(1+\chi_x)(1+\chi_y)}4
\]

with constant term `1/4`.  Even perfect cancellation for the t46 operator does not delete that positive baseline by itself.

Therefore t46 records two independent remaining requirements:

1. a sharper estimate for the twist-independent sparse squareclass-character operator;
2. a growing family of square tests or a centered dispersion mechanism that removes/absorbs the `1/4` baseline.

---

## 8. tH decision

**Stage14-tH13 is still needed.**  Its task is now sharper than in t45:

- do not treat the 544 conductors as arbitrary;
- use the exact twist-translation and the coefficient energy `E_kappa`;
- build a twist-uniform sparse squareclass quadratic-character operator receiver;
- compare max-range quadratic large sieve with cardinality/energy-sensitive alternatives;
- retain canonical-prime selector weights and the t44 `O(1)` tau-bad slices;
- state the critical-strip exponent ledger and countermodels if sparse support cannot improve the classical range term.

---

## Boundary

```text
STAGE14_T46=COMPLETE_TWIST_TRANSLATION_CONDUCTOR_ENERGY_AND_BASE_OPERATOR_REDUCTION
MOVING_CONDUCTOR_FAMILY_IS_TWIST_TRANSLATED_SQUARECLASS_SPECTRUM=true
TRANSLATED_CONDUCTOR_MULTIPLICITY_ENERGY_EQUALS_A1=true
PRINCIPAL_CONDUCTOR_SLICE_EQUALS_R_TAU=true
TWIST_DEPENDENCE_FACTORS_AS_ROW_CHARACTER=true
ALL_TWISTS_SHARE_BASE_QUADRATIC_CHARACTER_OPERATOR=true
SAFE_BASE_CONDUCTOR_BOUND=2^10*B^4
STANDARD_QUADRATIC_LARGE_SIEVE_INTERFACE_VALID=true
STANDARD_MAX_RANGE_LARGE_SIEVE_CLOSES_CRITICAL_STRIP=false
SPARSE_CARDINALITY_ENERGY_LARGE_SIEVE_PROVED=false
TWO_LOCAL_FILTER_CONSTANT_TERM_REMOVED=false
GENERIC_CROSS_GOOD_KUMMER_INCIDENCE_BOUND_PROVED=false
GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false
GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
CANONICAL_PRIME_SUM_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
TH13_NEEDED=true
NEXT=Stage14-t47 attack the twist-independent sparse squareclass character operator and the 1/4 detector baseline; use tH13 if available for a cardinality/energy-sensitive adapter
```
