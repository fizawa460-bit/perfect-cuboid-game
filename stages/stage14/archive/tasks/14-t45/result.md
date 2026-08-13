# Stage14-t45 — two-canonical local character and many-conductor boundary

## Purpose

Stage14-t44 reduced the heavy nonprincipal obstruction almost entirely to the genuinely generic, distinct-canonical-prime, cross-good twisted-Kummer family. Stage14-tH12 then supplied a strict certificate for when a fixed-core or fixed-partner specialization may legitimately be exported as a one-dimensional quadratic-character problem.

Stage14-t45 tests that certificate on the live t44 family.

The result is two-sided:

1. a **genuine one-dimensional quadratic prime character is exposed** after fixing the partner state (or equivalently freezing the phase conductor);
2. the two endogenous canonical primes of a pair supply only two local square tests, whose positivity detector has a fixed constant term `1/4`; and once the partner moves, the quadratic conductor moves through a large sparse family.

Thus the next obstruction is no longer “can a character be found?” It is a **many-conductor aggregation / large-sieve problem**.

No global Kummer-incidence power saving, `A_{1,1}` saving, or `T=o(sqrt(B))` claim is made.

---

## 1. Imported exact support routing

For a reciprocal-quotiented state `s`, write

\[
\ell_s=\text{canonical prime},\qquad F_s>0,
\]

and let

\[
v_s=v_{\ell_s}(F_s)\in\{0,2\}
\]

by t44. Define the own-prime normalized value

\[
\boxed{F_s^{\sharp}=F_s/\ell_s^{v_s}.}
\tag{45.1}
\]

Then `ell_s` does not divide `F_s^sharp`.

For a generic distinct-prime cross-good pair `(x,y)`, t44 gives

\[
\ell_x\nmid F_y,\qquad \ell_y\nmid F_x.
\tag{45.2}
\]

For a fixed nonprincipal target twist `tau`, the t44 bad-prime routing also removes the cases

\[
\ell_x\mid\tau\quad\text{or}\quad \ell_y\mid\tau
\]

from the generic good slice.

---

## 2. Exact two endogenous local square conditions

If

\[
[F_xF_y]=\tau,
\]

then

\[
\tau F_xF_y
\]

is a rational square. Dividing by the even own-prime powers does not alter its squareclass. Therefore every generic good target pair satisfies

\[
\boxed{
\chi_{\ell_x}(\tau F_x^{\sharp}F_y)=1,
\qquad
\chi_{\ell_y}(\tau F_xF_y^{\sharp})=1.
}
\tag{45.3}
\]

Equivalently, with the known own-state signs

\[
s_x=\chi_{\ell_x}(F_x^{\sharp}),\qquad
s_y=\chi_{\ell_y}(F_y^{\sharp}),
\]

we have

\[
\boxed{
\chi_{\ell_x}(\tau F_y)=s_x,
\qquad
\chi_{\ell_y}(\tau F_x)=s_y.
}
\tag{45.4}
\]

These are exact necessary conditions, not heuristics.

### Own-state sign sanity check

The frozen quotient gives

```text
invisible, v_ell(F)=0: 419 states, self sign always +1
visible,   v_ell(F)=2: 141 states, self sign can be +/-1
```

The invisible `+1` behavior is consistent with the t39 natural-modulus identity applied after commutativity of Gaussian multiplication: each `Psi` factor contributes the same unit sign and the product squares it away. No asymptotic theorem is claimed from this finite sign table.

---

## 3. Fixed partner gives a genuine quadratic Dirichlet character

Fix `tau` and the right state `y`. Put

\[
d_{\tau,y}=\operatorname{sqf}(\tau F_y)
=\operatorname{sqf}(\tau\,\sigma_y),
\]

where `sigma_y=sqf(F_y)`, and define the positive fundamental discriminant

\[
\boxed{
D_{\tau,y}=\begin{cases}
d_{\tau,y},&d_{\tau,y}\equiv1\pmod4,\\
4d_{\tau,y},&d_{\tau,y}\not\equiv1\pmod4.
\end{cases}}
\tag{45.5}
\]

For every odd cross-good canonical prime `ell_x` not dividing `tau F_y`, the square factors in `tau F_y` disappear in the Legendre symbol and the factor `4` is a square. Hence exactly

\[
\boxed{
\chi_{\ell_x}(\tau F_y)
=\chi_{D_{\tau,y}}(\ell_x).
}
\tag{45.6}
\]

Thus (45.4) becomes

\[
\boxed{
\chi_{D_{\tau,y}}(\ell_x)=s_x.
}
\tag{45.7}
\]

For fixed `y`, this is a genuine one-dimensional quadratic prime-character specialization of the tH12 receiver. The phase conductor is independent of the moving `ell_x`.

The deterministic audit verifies (45.6) on `2,442,672` generic-good `(target tau, x, y)` triples from the top eight heavy twists.

This closes the **existence-of-character** question for that specialization.

---

## 4. Why two endogenous primes do not by themselves save a power

For a good integer `N`, two local tests give the positivity majorant

\[
1_{N=\square}
\le
\frac{1+\chi_{\ell_x}(N)}2
\frac{1+\chi_{\ell_y}(N)}2.
\]

Expanding,

\[
\boxed{
1_{N=\square}
\le
\frac14\bigl(
1+\chi_{\ell_x}(N)+\chi_{\ell_y}(N)
+\chi_{\ell_x}(N)\chi_{\ell_y}(N)
\bigr).
}
\tag{45.8}
\]

The constant term is `1/4`.

Therefore, using only positivity / absolute values, a bounded number of endogenous local tests changes the count by at most a constant factor and cannot change a `B`-exponent. A power saving requires genuine cancellation in one or more nonconstant character terms, or a growing family of moduli.

The frozen top-heavy data matches this exactly. The generic distinct-prime cross-good candidate pool has

```text
305,334 ordered pairs.
```

For the top eight heavy twists, the two-local-pass counts are

```text
tau        exact pairs     two-local-pass      pass density
91              40              76,690          0.25117
209             38              77,616          0.25420
286             34              75,486          0.24722
34034           34              76,136          0.24935
41              32              78,054          0.25563
329             32              76,124          0.24931
4641            32              75,592          0.24757
11              30              75,994          0.24889
```

So the two endogenous tests behave almost exactly like two independent quadratic bits: useful as a correct local receiver, but nowhere near the observed exact multiplicities.

---

## 5. tH12 common-core route is not automatically one-dimensional

The tH12 common core is

\[
C=(\varepsilon,\delta,h,\mathrm{branch}).
\]

Fixing `C` does **not** freeze the equal-norm core `t`, the Gaussian orientation/cofactor data, or the canonical prime. Hence a fixed common-core cell is not automatically a one-variable prime sum.

Frozen quotient census:

```text
states                              560
common-core blocks                   37
canonical-prime blocks               87
joint (core,ell) blocks             530
descended cofactor packet blocks     56
max states in one common core        86
max distinct t in one common core     2
max distinct ell in one common core  73
max common cores for one ell         27
```

This is a finite diagnostic, while the logical point is exact: tH12's residual-dimension certificate must still be proved after any proposed freeze.

---

## 6. The actual new obstruction: many moving conductors

Equation (45.7) is one-dimensional only when `y` is fixed. Once `y` moves, the conductor

\[
D_{\tau,y}
\]

moves with it.

For each of the frozen top eight heavy twists, the generic cross-good family already contains

\[
\boxed{544\text{ distinct fixed-partner conductors}.}
\tag{45.9}
\]

Thus summing a separate one-dimensional estimate for every partner block would reproduce the tH12 many-block quantifier problem.

The correct analytic object is a sparse many-conductor family of the schematic form

\[
\boxed{
\mathcal B_\tau
=
\sum_x\sum_y
 a_x b_y\,
\chi_{D_{\tau,y}}(\ell_x),
}
\tag{45.10}
\]

with all of the following retained:

- canonical-prime selector weights on `ell_x`;
- tH12 common disjoint refinement;
- t44 `O(1)` bad/exposed canonical-prime routing;
- principal-conductor blocks split separately;
- physical packet coefficients / multiplicities;
- potentially the symmetric second leg with `x` and `y` interchanged.

This is the exact point where a quadratic large sieve / dispersion adapter is needed. A theorem depending only on a single fixed conductor does not close (45.10).

---

## 7. tH13 trigger

Stage14-tH12 said to reopen only if a live `t` stage found a concrete certified prime/core specialization that needed a sharper adapter.

Stage14-t45 now supplies exactly that trigger:

- fixed-partner quadratic prime character: **certified**;
- blockwise character existence: **closed**;
- global aggregation over the moving conductor family: **open**.

Therefore `Stage14-tH13` should be opened in parallel with the next live `t` step.

Requested tH13 roadwork:

1. build a reusable sparse many-conductor quadratic-character / large-sieve receiver for
   \[
   \sum_{x,y}a_xb_y\chi_{D_y}(\ell_x);
   \]
2. retain canonical-prime selector weights instead of replacing them by all primes without proof;
3. support tH12 common refinements and coefficient-energy bookkeeping;
4. use t44 to remove/charge the `O(1)` large bad primes per twist/block;
5. split principal conductors explicitly;
6. test reciprocity/duality, rational quadratic large sieve, norm-induced Gaussian-Hecke large sieve, and same-modulus dispersion;
7. state the usable bound in terms of **sparse conductor count/energy** if possible, and determine whether a bound depending on the maximum conductor alone is too weak in the critical strip;
8. include countermodels if sparse cardinality cannot replace conductor range in the available theorem.

Do not assume a t45 power saving: none has been proved.

---

## 8. Boundary

```text
STAGE14_T45=COMPLETE_TWO_CANONICAL_LOCAL_CHARACTER_AND_MANY_CONDUCTOR_BARRIER
TH12_PRIME_CHARACTER_SPECIALIZATION_FOUND=true
FIXED_PARTNER_QUADRATIC_CHARACTER_CERTIFIED=true
FIXED_COMMON_CORE_ALONE_ONE_DIMENSIONAL=false
TWO_ENDOGENOUS_CANONICAL_LOCAL_FILTERS_EXACT=true
TWO_ENDOGENOUS_CANONICAL_LOCAL_FILTERS_POWER_SAVING=false
TWO_LOCAL_FILTER_CONSTANT_TERM=1/4
MANY_CONDUCTOR_AGGREGATION_REQUIRED=true
TH13_REOPEN_TRIGGER=true
GENERIC_CROSS_GOOD_KUMMER_INCIDENCE_BOUND_PROVED=false
GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false
GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
CANONICAL_PRIME_SUM_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t46 attack the sparse many-conductor quadratic-character aggregate; in parallel Stage14-tH13 build the reusable multi-conductor large-sieve/dispersion adapter triggered here
```
