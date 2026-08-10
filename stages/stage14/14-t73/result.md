# Stage14-t73 — kappa=1 linear factorization, fixed denominator tags, and uniform fixed-norm fibers

## Purpose

Merged Stage14-t72 reduces the live fixed-`U` small-squareclass branch to

\[
\eta P_+=\alpha r^2+\beta t^2,
\qquad
\eta P_-=\beta t^2-\alpha r^2,
\qquad
\alpha\beta=\kappa,
\]

with the exact denominator tag

\[
\beta=\gcd(\kappa,v).
\]

It then identifies the genuinely live analytic object as a canonical-largest-prime / smooth-companion Pell-norm energy.  Stage14-t73 separates the parts of that formulation which are actually harmless:

1. `kappa=1` is not a Pell-unit problem at all; it is an exact coprime difference-of-squares factorization;
2. denominator tags can be conditioned on at divisor-many cost, and once the two tags are fixed the t72 agree/switch orientation is unique rather than `2^omega(kappa)`-many;
3. for fixed `kappa`, fixed tag `beta`, and fixed negative norm value `P_-`, the number of integral norm representations in any polynomial physical height box is `B^o(1)` uniformly in the moving real quadratic field;
4. no class-number factor is needed, and the unit/regulator orbit contributes only logarithmically.

Therefore tH19 should no longer investigate fixed-norm Pell orbit multiplicity.  The remaining obstruction is the **average over moving physical norm values** `P_-` carrying the distinguished largest prime `ell` and the angular/radial smooth companion.

No additional whole-family power saving is claimed.

---

## 1. Exact normalized tagged form

Write the t65/t66 square scale as

\[
s=\kappa(u/v)^2,
\qquad \gcd(u,v)=1,
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

Merged t66 gives `G/beta in {1,2}`.  Define

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

Equivalently, with

\[
x=\beta w,\qquad y=u,
\]

one has

\[
\boxed{
x^2-\kappa y^2=\beta\eta P_-}
\tag{73.2}
\]

and

\[
\boxed{
x^2+\kappa y^2=\beta\eta P_+.}
\tag{73.3}
\]

Thus the t72 signed split contains no extra variable beyond the divisor tag `beta`.

```text
TAGGED_NORMAL_FORM_PROVED=true
TAGGED_NORM_EQUATION_PROVED=true
```

---

## 2. `kappa=1` degenerates to two coprime linear factors

If `kappa=1`, then `alpha=beta=1` and `eta=G in {1,2}`.  Put

\[
L_-=(v-u)/\eta,
\qquad
L_+=(v+u)/\eta.
\]

Because `(u,v)=1`, `eta=1` exactly in the opposite-parity case and `eta=2` exactly in the odd/odd case.  Hence

\[
\boxed{\gcd(L_-,L_+)=1}
\tag{73.4}
\]

and

\[
\boxed{P_-=\eta L_-L_+.}
\tag{73.5}
\]

Conversely, once `eta` and an admissible ordered coprime factorization

\[
P_-/\eta=L_-L_+
\]

are fixed,

\[
\boxed{
 u=\frac{\eta(L_+-L_-)}2,
 \qquad
 v=\frac{\eta(L_++L_-)}2
}
\tag{73.6}
\]

are recovered uniquely whenever the parity condition is legal.

Therefore, for fixed `P_-`, the number of primitive `kappa=1` square scales is divisor-many:

\[
\boxed{
\#\{(u,v):\kappa=1,\ P_-=D\}\ll \tau(D).
}
\tag{73.7}
\]

After merged t65's fixed `(U,s)` `O(1)` lift, the physical fixed-`(U,P_-)` fiber is also `B^{o(1)}`.

### Canonical prime becomes a unique linear-factor tag

The physical t69/t72 boundary retains

\[
\ell=\operatorname{LPF}_{\rm odd}(P_+P_-),
\quad
v_\ell(P_-)=1,
\quad
2\,\operatorname{odd}(P_-/\ell)<\ell.
\]

Since the odd parts of `L_-` and `L_+` are coprime, the odd canonical prime `ell` divides **exactly one** of the two linear factors.  Thus `kappa=1` has no real-quadratic unit orbit: its residual arithmetic is a moving canonical-prime-tagged difference-of-squares value problem.

```text
KAPPA_ONE_PELL_ORBIT_EXISTS=false
KAPPA_ONE_COPRIME_LINEAR_FACTORIZATION_PROVED=true
KAPPA_ONE_CANONICAL_ELL_UNIQUE_LINEAR_FACTOR_TAG=true
KAPPA_ONE_FIXED_DENOMINATOR_VALUE_FIBER=Bo1
```

The frozen 419-state audit happens to contain no `kappa=1` physical state.  This is recorded only as a regression fact and is **not** promoted to a theorem that the branch is empty.

---

## 3. Denominator-tag conditioning costs only `B^o(1)`

Because `kappa` is squarefree and `beta|kappa`,

\[
\#\{\beta:\beta\mid\kappa\}=\tau(\kappa)=2^{\omega(\kappa)}=B^{o(1)}.
\tag{73.8}
\]

For a pair of states in one squareclass, conditioning on `(beta_i,beta_j)` costs at most

\[
\tau(\kappa)^2=B^{o(1)}.
\tag{73.9}
\]

Let

\[
K=\operatorname{odd}(\kappa),
\qquad
d_i=\gcd(K,\beta_i),
\qquad
d_j=\gcd(K,\beta_j),
\]

and `g=gcd(d_i,d_j)`.  Then merged t72's switch modulus is

\[
\boxed{
K_{\rm switch}=\frac{d_i d_j}{g^2},
\qquad
K_{\rm agree}=K/K_{\rm switch}.
}
\tag{73.10}
\]

Since `K` is squarefree, `K_switch` is exactly the product of odd primes lying in the symmetric difference of the two denominator-tag supports.  Hence, once `(beta_i,beta_j)` are fixed, every odd prime of `K` has a predetermined sign:

```text
same tag side     -> +1 / agreement,
different tag side -> -1 / switch.
```

The CRT orientation of t72 is therefore **unique** for fixed tags.

\[
\boxed{
\text{fixed-tag orientation multiplicity}=1.
}
\tag{73.11}
\]

The previous `2^{omega(K)}` is only the total cost of summing over all possible tag patterns, already `B^{o(1)}`.

In particular, if `beta_i=beta_j`, then

\[
K_{\rm switch}=1,
\qquad K_{\rm agree}=K.
\tag{73.12}
\]

For equal full tags `beta`, (73.1) gives the exact identity

\[
\boxed{
\eta_i\eta_j
(P_{+,j}P_{-,i}-P_{+,i}P_{-,j})
=2\kappa
(u_j^2w_i^2-u_i^2w_j^2).
}
\tag{73.13}
\]

Thus the agreement divisibility by `K` in this diagonal-tag subclass is coefficient-forced.  It is a valid Cayley root-line restriction, but it must not be charged again as an independent root-coordinate modulus.

```text
DENOMINATOR_TAG_CONDITIONING_COST=Bo1
PAIR_DENOMINATOR_TAG_CONDITIONING_COST=Bo1
TAG_SWITCH_EQUALS_ODD_SUPPORT_SYMMETRIC_DIFFERENCE=true
FIXED_TAG_CAYLEY_ROOTLINE_ORIENTATION_MULTIPLICITY=1
SAME_TAG_KSWITCH_ONE=true
SAME_TAG_KAPPA_AGREEMENT_DIVISIBILITY_COEFFICIENT_FORCED=true
```

---

## 4. Uniform fixed-norm Pell fiber: no class-number loss

The remaining nondegenerate equation for `kappa>1` is

\[
x^2-\kappa y^2=n,
\qquad
n=\beta\eta P_->0.
\tag{73.14}
\]

A generic statement that this equation has infinitely many solutions is irrelevant: the physical problem has a polynomial height cutoff, and `n` is fixed in the fiber considered here.

Let `K_kappa=Q(sqrt(kappa))` and `O_K` be its maximal order.  For every integral solution

\[
z=x+y\sqrt\kappa\in O_K,
\qquad N(z)=n.
\]

Then

\[
(z)(\bar z)=(n),
\]

so the principal ideal `(z)` is an integral ideal divisor of `(n)`.

For `n=prod p^{e_p}`, each rational prime contributes at most two prime ideals; even in the ramified case the number of ideal-divisor exponents is bounded by `(e_p+1)^2`.  Therefore

\[
\#\{\text{ideal divisors of }(n)\}
\le \tau(n)^2.
\tag{73.15}
\]

No class-number factor occurs: principal ideals arising from solutions form only a subset of these ideal divisors.

For one fixed principal ideal, all generators differ by a real-quadratic unit.  If `epsilon_kappa>1` is the fundamental unit, the universal degree-two trace bound gives

\[
\epsilon_\kappa\ge\frac{1+\sqrt5}{2}.
\tag{73.16}
\]

Hence, inside any polynomial archimedean height box `H=B^{O(1)}`, the allowable unit exponents form an interval of length `O(log B)`.  Consequently

\[
\boxed{
R_\kappa(n;H)
\ll \tau(n)^2\,(1+\log H)
=B^{o(1)}
}
\tag{73.17}
\]

uniformly in the moving squarefree `kappa>1`.

For `kappa=1`, the same conclusion is stronger by (73.5): `R_1(n) <= 2 tau(n)`.

Applying (73.17) to `n=beta eta P_-` proves

\[
\boxed{
\#\{\text{physical square scales with fixed }(\kappa,\beta,P_-),U\}
=B^{o(1)}.
}
\tag{73.18}
\]

The fixed `U` lift from exact `s` then costs only `O(1)` per scale.

```text
UNIFORM_FIXED_NORM_REAL_QUADRATIC_ELEMENT_COUNT=Bo1
FIXED_KAPPA_BETA_PMINUS_SQUARE_SCALE_FIBER=Bo1
CLASS_NUMBER_FIXED_NORM_COST=0
UNIT_ORBIT_FIXED_NORM_COST=Bo1
REGULATOR_FIXED_POWER_LOSS=0
```

This removes the class-number / regulator / fixed-norm unit-orbit item from the tH19 obstruction list.

---

## 5. What remains: moving norm-value energy

The preceding argument does **not** sum over the moving negative Cayley value

\[
P_-=\ell\,c\,2^{e_2},
\qquad
c=\operatorname{odd}(h)R_V,
\qquad
2c<\ell.
\]

Nor does it use the coupled positive value

\[
\operatorname{odd}(P_+)
=\operatorname{odd}(\delta)R_\pi
\]

and the sharp radial hyperbola

\[
\ell\delta\le Y_U.
\]

Thus the minimal live nondegenerate receiver is no longer a generic Pell-orbit count.  It is

```text
SharedUSmallOddKappaFixedTagMovingCanonicalNormValueEnergy
```

which must average the divisor-many fixed-norm fibers over the physical moving values while retaining:

```text
ell = LPF_odd(P+*P-),
v_ell(P-)=1,
2*odd(P-/ell)<ell,
odd(P-)/ell=odd(h)*R_V,
odd(P+)=odd(delta)*R_pi,
ell*delta<=Y_U,
fixed U,
fixed kappa band,
fixed denominator tag beta.
```

The `kappa=1` specialization is the separate elementary receiver

```text
SharedUKappaOneMovingCanonicalLinearFactorValueEnergy.
```

No claim that either moving-value energy is already near-linear is made here.

---

## 6. tH19 decision

`tH19` remains useful, but its target is strictly narrower than in t72.

### Superseded tH19 subproblems

Do **not** spend tH19 effort on:

- fixed-norm Pell solution multiplicity;
- class-number factors;
- regulator lower bounds;
- the number of unit translates in a polynomial box;
- denominator-tag orientation enumeration;
- `kappa=1` Pell theory.

Stage14-t73 proves all of those cost only `B^{o(1)}` or degenerate to elementary factorization.

### Revised requested object

```text
SmallOddKappaMovingCanonicalLargestPrimeSmoothNormValueEnergy
```

The useful independent audit is now:

1. average over moving values of `beta*w^2-alpha*u^2` after `(kappa,beta)` are fixed;
2. preserve `ell=LPF_odd(P+P-)`, `v_ell(P-)=1`, and `2c<ell`;
3. preserve `c=odd(h)R_V`, `odd(P+)=odd(delta)R_pi`, and `ell*delta<=Y_U`;
4. test primitive-divisor / smooth-value / largest-prime-factor technology for this **moving norm-value family**, not for one Pell orbit;
5. determine whether averaging over moving `kappa` and moving physical norm values has a uniform power saving.

`t` does not wait for tH19.

```text
TH19_NEEDED=true
TH19_REQUESTED_OBJECT=SmallOddKappaMovingCanonicalLargestPrimeSmoothNormValueEnergy
TH19_FIXED_NORM_PELL_ORBIT_SUBPROBLEM_SUPERSEDED=true
TH19_KAPPA_ONE_PELL_SUBPROBLEM_SUPERSEDED=true
T_ROUTE_BLOCKED_WAITING_FOR_TH19=false
```

---

## 7. Shared exponent and next step

Merged s7-31/s7-32 and the current mainline still give

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8
```

Stage14-t73 proves no additional whole-family saving.

Stage14-t74 should attack the moving negative norm value itself: first split by which prime ideal / linear factor hosts the canonical `ell`, then combine the `2c<ell` largest-prime condition with the angular identities for `R_V` and the sharp `ell*delta` hyperbola.

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
SHARED_U_KAPPA_ONE_MOVING_CANONICAL_LINEAR_FACTOR_VALUE_ENERGY_PROVED=false
SHARED_U_SMALL_ODD_KAPPA_FIXED_TAG_MOVING_CANONICAL_NORM_VALUE_ENERGY_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8
T73_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
TH19_NEEDED=true
TH19_REQUESTED_OBJECT=SmallOddKappaMovingCanonicalLargestPrimeSmoothNormValueEnergy
TH19_FIXED_NORM_PELL_ORBIT_SUBPROBLEM_SUPERSEDED=true
T_ROUTE_BLOCKED_WAITING_FOR_TH19=false
NEXT=Stage14-t74
```
