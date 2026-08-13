# Stage14-t73 — kappa=1 linear factorization, fixed denominator tags, and uniform fixed-norm fibers

## Purpose

Merged Stage14-t72 leaves the fixed-`U` small-squareclass branch in the exact form

\[
\eta P_+=\alpha r^2+\beta t^2,
\qquad
\eta P_-=\beta t^2-\alpha r^2,
\qquad
\alpha\beta=\kappa,
\]

with denominator tag

\[
\beta=\gcd(\kappa,v).
\]

Stage14-t73 removes three apparent obstructions before any further analytic theorem is requested:

1. `kappa=1` is an elementary coprime difference-of-squares factorization, not a Pell orbit;
2. denominator-tag conditioning costs only `B^{o(1)}`, and fixed tag pairs determine the t72 CRT sign uniquely;
3. for fixed `(kappa,beta,P_-)`, the real-quadratic norm fiber in a polynomial physical height box is uniformly `B^{o(1)}` with no class-number loss.

The completed parallel tH19 audit is consumed here. Its negative result is consistent with t73: the remaining obstruction is not fixed-norm Pell multiplicity, but the average over **moving canonical-largest-prime norm values** while retaining the sharp physical filters.

No additional whole-family power saving is claimed.

---

## 1. Exact tagged normal form

Write

\[
s=\kappa(u/v)^2,
\qquad (u,v)=1,
\]

and put

\[
\beta=\gcd(\kappa,v),
\qquad
\alpha=\kappa/\beta,
\qquad
v=\beta w.
\]

Let

\[
G=\gcd(v^2+\kappa u^2,v^2-\kappa u^2).
\]

Merged t66 proves

\[
G\in\{\beta,2\beta\}.
\]

Set

\[
\eta=G/\beta\in\{1,2\}.
\]

Then the reduced Cayley pair is exactly

\[
\boxed{
P_+=\frac{\beta w^2+\alpha u^2}{\eta},
\qquad
P_-=\frac{\beta w^2-\alpha u^2}{\eta}.
}
\tag{73.1}
\]

With

\[
x=\beta w,\qquad y=u,
\]

this is

\[
\boxed{x^2-\kappa y^2=\beta\eta P_-}
\tag{73.2}
\]

and

\[
\boxed{x^2+\kappa y^2=\beta\eta P_+.}
\tag{73.3}
\]

Thus the t72 signed split is completely determined by the divisor tag `beta`; it is not an independent combinatorial datum.

```text
TAGGED_NORMAL_FORM_PROVED=true
TAGGED_NORM_EQUATION_PROVED=true
```

---

## 2. `kappa=1` is a coprime linear-factor problem

If `kappa=1`, then `alpha=beta=1` and `eta=G in {1,2}`. Define

\[
L_-=(v-u)/\eta,
\qquad
L_+=(v+u)/\eta.
\]

Because `(u,v)=1`, `eta=1` in the opposite-parity case and `eta=2` in the odd/odd case. Hence

\[
\boxed{(L_-,L_+)=1}
\tag{73.4}
\]

and

\[
\boxed{P_-=\eta L_-L_+.}
\tag{73.5}
\]

Conversely, after fixing `eta` and an admissible ordered coprime factorization

\[
P_-/\eta=L_-L_+,
\]

one recovers

\[
\boxed{
 u=\frac{\eta(L_+-L_-)}2,
 \qquad
 v=\frac{\eta(L_++L_-)}2.
}
\tag{73.6}
\]

Therefore

\[
\boxed{
\#\{(u,v):\kappa=1,\ P_-=D\}\ll\tau(D).
}
\tag{73.7}
\]

Merged t65 then gives only `O(1)` physical lifts for each exact `(U,s)`.

The physical boundary also retains

\[
\ell=\operatorname{LPF}_{\rm odd}(P_+P_-),
\qquad
v_\ell(P_-)=1,
\qquad
2\,\operatorname{odd}(P_-/\ell)<\ell.
\]

Since the odd parts of `L_-` and `L_+` are coprime, the odd canonical prime `ell` divides exactly one linear factor. Thus the `kappa=1` residual problem is a moving canonical-prime-tagged factor-value problem, not a real-quadratic unit orbit.

```text
KAPPA_ONE_PELL_ORBIT_EXISTS=false
KAPPA_ONE_COPRIME_LINEAR_FACTORIZATION_PROVED=true
KAPPA_ONE_CANONICAL_ELL_UNIQUE_LINEAR_FACTOR_TAG=true
KAPPA_ONE_FIXED_DENOMINATOR_VALUE_FIBER=Bo1
```

The frozen physical sample contains zero `kappa=1` states; this is diagnostic only and is not promoted to branch emptiness.

---

## 3. Fixed denominator tags determine the t72 orientation

Since `kappa` is squarefree and `beta|kappa`,

\[
\#\{\beta:\beta|\kappa\}=\tau(\kappa)=2^{\omega(\kappa)}=B^{o(1)}.
\tag{73.8}
\]

For a pair of states, conditioning on `(beta_i,beta_j)` therefore costs only `B^{o(1)}`.

Let

\[
K=\operatorname{odd}(\kappa),
\qquad
d_i=(K,\beta_i),
\qquad
d_j=(K,\beta_j),
\qquad
g=(d_i,d_j).
\]

Merged t72 gives

\[
\boxed{
K_{\rm switch}=\frac{d_i d_j}{g^2},
\qquad
K_{\rm agree}=K/K_{\rm switch}.
}
\tag{73.9}
\]

Because `K` is squarefree, `K_switch` is exactly the symmetric-difference support of the two denominator tags. Every odd prime of `K` therefore has a predetermined sign once the tags are fixed:

```text
same tag side      -> +1 / agreement
different tag side -> -1 / switch
```

Hence the CRT sign of t72 has multiplicity exactly

\[
\boxed{1}
\tag{73.10}
\]

for fixed tags. The earlier `2^{omega(K)}` is only the cost of summing over all tag patterns.

If `beta_i=beta_j`, then

\[
K_{\rm switch}=1,
\qquad
K_{\rm agree}=K.
\tag{73.11}
\]

Moreover (73.1) gives the exact same-tag identity

\[
\boxed{
\eta_i\eta_j
(P_{+,j}P_{-,i}-P_{+,i}P_{-,j})
=2\kappa
(u_j^2w_i^2-u_i^2w_j^2).
}
\tag{73.12}
\]

Thus same-tag agreement divisibility is coefficient-forced and must not be charged a second time as an independent root-coordinate modulus.

```text
DENOMINATOR_TAG_CONDITIONING_COST=Bo1
PAIR_DENOMINATOR_TAG_CONDITIONING_COST=Bo1
TAG_SWITCH_EQUALS_ODD_SUPPORT_SYMMETRIC_DIFFERENCE=true
FIXED_TAG_CAYLEY_ROOTLINE_ORIENTATION_MULTIPLICITY=1
SAME_TAG_KSWITCH_ONE=true
SAME_TAG_KAPPA_AGREEMENT_DIVISIBILITY_COEFFICIENT_FORCED=true
```

---

## 4. Uniform fixed-norm fiber has no class-number loss

For `kappa>1`, fix

\[
n=\beta\eta P_->0
\]

and consider

\[
x^2-\kappa y^2=n.
\tag{73.13}
\]

Let `K_kappa=Q(sqrt(kappa))` with maximal order `O_K`. Every integral solution gives

\[
z=x+y\sqrt\kappa\in O_K,
\qquad N(z)=n.
\]

Then

\[
(z)(\bar z)=(n),
\]

so `(z)` is an integral ideal divisor of `(n)`.

If `n=prod p^{e_p}`, each rational prime contributes at most two prime ideals, hence

\[
\boxed{
\#\{\text{ideal divisors of }(n)\}\le\tau(n)^2.
}
\tag{73.14}
\]

No class-number factor appears: the principal ideals coming from actual solutions are merely a subset of these ideal divisors.

For one fixed principal ideal, all generators differ by units. A real-quadratic fundamental unit satisfies the uniform degree-two lower bound

\[
\varepsilon_\kappa\ge\frac{1+\sqrt5}{2}.
\tag{73.15}
\]

Inside any polynomial physical height box `H=B^{O(1)}`, the allowable unit exponents therefore form an interval of length `O(log B)`. Consequently

\[
\boxed{
R_\kappa(n;H)
\ll \tau(n)^2(1+\log H)
=B^{o(1)}
}
\tag{73.16}
\]

uniformly in moving squarefree `kappa>1`.

For `kappa=1`, (73.5) gives the stronger divisor bound directly. Therefore

\[
\boxed{
\#\{\text{square scales with fixed }(U,\kappa,\beta,P_-)\}
=B^{o(1)}.
}
\tag{73.17}
\]

```text
UNIFORM_FIXED_NORM_REAL_QUADRATIC_ELEMENT_COUNT=Bo1
FIXED_KAPPA_BETA_PMINUS_SQUARE_SCALE_FIBER=Bo1
CLASS_NUMBER_FIXED_NORM_COST=0
UNIT_ORBIT_FIXED_NORM_COST=Bo1
REGULATOR_FIXED_POWER_LOSS=0
```

This is stronger than merely assuming that a moving class-number/regulator average is harmless: the fixed-norm count bypasses class-number averaging completely.

---

## 5. Consumption of completed tH19

The supplied parallel audit completed with

```text
STAGE14_TH19=COMPLETE_INDEPENDENT_PELL_SMOOTH_ENERGY_AUDIT
PRIMITIVE_DIVISOR_LUCAS_PELL_APPLICABLE_PARTIALLY=true
PRIMITIVE_DIVISOR_FORCES_CANONICAL_LPF=false
PRIMITIVE_DIVISOR_FORCES_V_ELL_ONE=false
PRIMITIVE_DIVISOR_FORCES_2C_LT_ELL=false
FIXED_S_SUNIT_SMOOTH_THEOREMS_AVAILABLE=true
MOVING_KAPPA_MOVING_S_UNIFORM_QUANTITATIVE_SAVING_AVAILABLE=false
PELL_UNIT_ORBIT_COST=Bo1_COMPATIBLE
MOVING_CLASS_NUMBER_REGULATOR_UNIFORM_AVERAGE_SUFFICIENTLY_STRONG=false
SHARP_ELL_DELTA_HYPERBOLA_MUST_BE_RETAINED=true
DISTINGUISHED_LARGEST_PRIME_FILTER_MUST_BE_RETAINED=true
EXPONENT_ONE_FILTER_MUST_BE_RETAINED=true
SMOOTH_COMPANION_FILTER_MUST_BE_RETAINED=true
OFF_THE_SHELF_UNIFORM_FIXED_POWER_SAVING_PROVED=false
```

This is fully consistent with t73.

- `PELL_UNIT_ORBIT_COST=Bo1_COMPATIBLE` is upgraded here to the uniform fixed-norm theorem (73.16).
- the weak moving class-number/regulator average is no longer a fixed-norm obstruction because no class-number factor is used;
- primitive-divisor technology remains only a possible ingredient for the moving-value average;
- tH19 correctly shows that primitive divisors alone do not force `ell=LPF`, `v_ell=1`, or `2c<ell`.

Hence the pre-t73 receiver

```text
SmallOddKappaCanonicalLargestPrimePellSmoothEnergy
```

is not minimal after t73.

```text
TH19_CONSUMED=true
TH19_FIXED_NORM_PELL_ORBIT_SUBPROBLEM_SUPERSEDED=true
TH19_CLASS_NUMBER_FIXED_NORM_SUBPROBLEM_SUPERSEDED=true
TH19_KAPPA_ONE_PELL_SUBPROBLEM_SUPERSEDED=true
```

---

## 6. Minimal live receiver: moving norm values

The argument above does **not** sum over the moving negative Cayley value

\[
P_-=\ell\,c\,2^{e_2},
\qquad
c=\operatorname{odd}(h)R_V,
\qquad
2c<\ell,
\]

nor over the coupled positive value

\[
\operatorname{odd}(P_+)
=\operatorname{odd}(\delta)R_\pi,
\]

with the sharp radial hyperbola

\[
\ell\delta\le Y_U.
\]

Thus the live fixed-`U` receiver is

```text
SharedUSmallOddKappaFixedTagMovingCanonicalNormValueEnergy
```

with mandatory retained filters

```text
ell = LPF_odd(P+*P-)
v_ell(P-)=1
2*odd(P-/ell)<ell
odd(P-)/ell=odd(h)*R_V
odd(P+)=odd(delta)*R_pi
ell*delta<=Y_U
fixed U
fixed kappa band
fixed denominator tag beta
```

The `kappa=1` specialization is

```text
SharedUKappaOneMovingCanonicalLinearFactorValueEnergy.
```

Neither moving-value energy is proved near-linear here.

---

## 7. tH decision after completed tH19

`tH19` is complete and consumed. A new auxiliary audit is justified because t73 changed the theorem target from Pell-orbit multiplicity to a tagged binary-quadratic **value-distribution** problem.

```text
TH20_NEEDED=true
TH20_REQUESTED_OBJECT=SmallOddKappaFixedTagMovingCanonicalLargestPrimeSmoothNormValueSieve
```

`tH20` should independently test only the following:

1. largest-prime-factor / beta-sieve / dispersion technology for
   `beta*w^2-alpha*u^2` with `alpha*beta=kappa` squarefree and `(kappa,beta)` conditioned;
2. simultaneous retention of the positive companion `beta*w^2+alpha*u^2`;
3. distinguished `ell=LPF_odd(P+P-)`, exponent one, and `2c<ell`;
4. the exact smooth companion `c=odd(h)R_V` and positive factor `odd(delta)R_pi`;
5. the sharp `ell*delta<=Y_U` average;
6. whether averaging over moving `(kappa,beta)` and moving physical norm values yields any uniform power saving.

Do **not** reopen fixed-norm Pell orbit counting, class-number/regulator averaging, denominator-tag enumeration, or generic Legendre-only large sieve.

The t-route does not wait for tH20.

```text
TH19_CONSUMED=true
TH20_NEEDED=true
TH20_REQUESTED_OBJECT=SmallOddKappaFixedTagMovingCanonicalLargestPrimeSmoothNormValueSieve
T_ROUTE_BLOCKED_WAITING_FOR_TH20=false
```

---

## 8. Frozen audit

```text
reciprocal states                                560
invisible states                                 419
tagged normal-form checks                        419
canonical largest-prime filter checks            419
private fixed-tag orientation checks               5
same-denominator-tag private pairs                 1
kappa=1 exhaustive factorization checks         1965
fixed-norm small-box regression checks           3240
max frozen fixed (kappa,beta,Pminus) multiplicity   1
kappa=1 frozen physical states                      0
```

The last two values are diagnostic only; neither is used as an asymptotic theorem input.

---

## 9. Shared exponent and next step

Current merged whole-family exponent remains

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8
```

Stage14-t73 proves no additional whole-family saving.

Stage14-t74 should attack the moving negative norm value directly: split by which prime-ideal / linear orientation hosts canonical `ell`, then combine `2c<ell` with the angular formula for `R_V`, the positive companion, and the sharp `ell*delta` hyperbola.

---

## Locked boundary

```text
STAGE14_T73=COMPLETE_KAPPA_ONE_LINEAR_FACTORIZATION_FIXED_TAG_CONDITIONING_AND_UNIFORM_FIXED_NORM_FIBER_REDUCTION
MERGED_T72_IMPORTED=true
TAGGED_NORMAL_FORM_PROVED=true
KAPPA_ONE_PELL_ORBIT_EXISTS=false
KAPPA_ONE_COPRIME_LINEAR_FACTORIZATION_PROVED=true
KAPPA_ONE_CANONICAL_ELL_UNIQUE_LINEAR_FACTOR_TAG=true
KAPPA_ONE_FIXED_DENOMINATOR_VALUE_FIBER=Bo1
DENOMINATOR_TAG_CONDITIONING_COST=Bo1
PAIR_DENOMINATOR_TAG_CONDITIONING_COST=Bo1
TAG_SWITCH_EQUALS_ODD_SUPPORT_SYMMETRIC_DIFFERENCE=true
FIXED_TAG_CAYLEY_ROOTLINE_ORIENTATION_MULTIPLICITY=1
SAME_TAG_KSWITCH_ONE=true
SAME_TAG_KAPPA_AGREEMENT_DIVISIBILITY_COEFFICIENT_FORCED=true
UNIFORM_FIXED_NORM_REAL_QUADRATIC_ELEMENT_COUNT=Bo1
FIXED_KAPPA_BETA_PMINUS_SQUARE_SCALE_FIBER=Bo1
CLASS_NUMBER_FIXED_NORM_COST=0
UNIT_ORBIT_FIXED_NORM_COST=Bo1
REGULATOR_FIXED_POWER_LOSS=0
TH19_CONSUMED=true
TH19_FIXED_NORM_PELL_ORBIT_SUBPROBLEM_SUPERSEDED=true
SHARED_U_KAPPA_ONE_MOVING_CANONICAL_LINEAR_FACTOR_VALUE_ENERGY_PROVED=false
SHARED_U_SMALL_ODD_KAPPA_FIXED_TAG_MOVING_CANONICAL_NORM_VALUE_ENERGY_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8
T73_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
TH20_NEEDED=true
TH20_REQUESTED_OBJECT=SmallOddKappaFixedTagMovingCanonicalLargestPrimeSmoothNormValueSieve
T_ROUTE_BLOCKED_WAITING_FOR_TH20=false
NEXT=Stage14-t74
```
