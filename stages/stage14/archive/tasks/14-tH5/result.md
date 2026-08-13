# Stage14-tH5 — exact Gaussian-pair coefficient collision energy

## Purpose

Stage14-tH4 proved that masks, bounded smooth cutoffs, Mellin phases, divisor lifts and Gaussian representation multiplicities do not consume a fixed exponent before a large-sieve theorem is called.  One piece was intentionally left open:

```text
FULL_COEFFICIENT_COLLISION_ENERGY_PROVED=false.
```

Stage14-tH5 closes that specific roadworks gap for the **exact paired Gaussian coefficient map**.  The key point is that tH2 already exposed the shared factor

\[
N(U)=hr,\qquad N(V)=gh\delta,
\qquad g\mid\varepsilon,
\qquad (h,\varepsilon/g)=1,
\qquad hr\delta\le Y.
\]

Once both Gaussian coordinates are retained, all source collisions are controlled by the possible common divisors `h` of the two norm indices.  This gives an exact divisor formula for every coefficient fiber and a near-linear collision-energy bound.

This stage does **not** claim a same-modulus residue-collision theorem.  Distinct exact pairs may still become congruent modulo an auxiliary Gaussian prime; that is a different dispersion problem.

No future live `t` result is required.

---

## 1. Exact paired norm map

Fix one finite state `(epsilon,g)` and write

\[
c=\varepsilon/g.
\]

For a transformed tH2 source tuple `(h,r,delta)`, define

\[
\boxed{m=hr,\qquad n=gh\delta.}
\tag{H5.1}
\]

Thus a Gaussian representative pair satisfies

\[
N(U)=m,\qquad N(V)=n.
\]

Suppose `(m,n)` is fixed and comes from at least one source tuple.  Then any preimage must have

\[
h\mid m,
\qquad
h\mid n/g.
\]

Hence

\[
\boxed{h\mid \gcd(m,n/g).}
\tag{H5.2}
\]

Moreover

\[
r=m/h,
\qquad
\delta=n/(gh)
\]

are then forced.

So **the only collision freedom left after both norms are fixed is the shared factor `h`**.

---

## 2. Exact coefficient-fiber multiplicity formula

The tH2 coprimality and physical budget impose

\[
(h,c)=1
\]

and

\[
hr\delta
=
\frac{mn}{gh}
\le Y.
\]

Therefore the exact number of tH2 source tuples mapping to `(m,n)` is

\[
\boxed{
\nu_{\varepsilon,g,Y}(m,n)
=
\#\left\{
 h\mid\gcd(m,n/g):
 (h,\varepsilon/g)=1,
 mn\le ghY
\right\}.
}
\tag{H5.3}
\]

Here the set is empty unless `g|n`.

In particular,

\[
\boxed{
\nu_{\varepsilon,g,Y}(m,n)
\le
\tau\!\left(\gcd(m,n/g)\right)
\le
\tau_{\max}(Y).
}
\tag{H5.4}
\]

Indeed every source tuple has `m=hr<=Y` and `n/g=h delta<=Y`, so the gcd in (H5.4) is at most `Y`.

Thus

\[
\boxed{\nu_{\varepsilon,g,Y}(m,n)=Y^{o(1)}}
\tag{H5.5}
\]

uniformly in the exact paired norm index.

```text
EXACT_SHARED_H_FIBER_FORMULA_PROVED=true
EXACT_PAIRED_NORM_COLLISION_MULTIPLICITY_LE_TAU_MAX=true
```

---

## 3. Exact Gaussian element pairs have the same collision multiplicity

Now retain actual Gaussian elements rather than only their norms.

Fix

\[
(U,V)\in\mathbf Z[i]^2,
\qquad
N(U)=m,
\qquad
N(V)=n.
\]

Once `(U,V)` is fixed, the possible tH2 arithmetic preimages are still exactly the `h` counted by (H5.3).  Choosing a particular Gaussian representation does not create any new factorisation freedom.

Hence

\[
\boxed{
\nu(U,V)
=
\nu_{\varepsilon,g,Y}(N(U),N(V)).
}
\tag{H5.6}
\]

The four Gaussian units only create a bounded-size orbit if one later passes between exact elements and unit classes.  If unit classes are used, expanding both coordinates back to exact elements costs at most `4*4=16`, an absolute constant.

Conjugation is **not** silently quotiented: tH1/tH3 preserve Gaussian orientation.

```text
EXACT_GAUSSIAN_PAIR_COLLISION_MULTIPLICITY=DIVISOR_BOUNDED
UNIT_ORBIT_EXPANSION_COST_AT_MOST=16
GAUSSIAN_CONJUGATION_COLLAPSED=false
```

---

## 4. Weighted coefficient-energy theorem

Let the source coefficient be

\[
w(h,r,\delta,U,V)
\]

on one fixed finite state `(epsilon,g)` and one legal tH2 block/domain.

Collapse all arithmetic preimages to the exact Gaussian pair:

\[
\boxed{
A(U,V)
=
\sum_{\substack{h,r,\delta:\\N(U)=hr\\N(V)=gh\delta}}
 w(h,r,\delta,U,V).
}
\tag{H5.7}
\]

For each fixed `(U,V)`, Cauchy gives

\[
|A(U,V)|^2
\le
\nu(U,V)
\sum_{s\mapsto(U,V)}|w(s)|^2.
\]

Using (H5.4) and summing over exact pairs,

\[
\boxed{
\sum_{U,V}|A(U,V)|^2
\le
\tau_{\max}(Y)
\sum_{h,r,\delta,U,V}|w(h,r,\delta,U,V)|^2.
}
\tag{H5.8}
\]

Therefore the complete exact-pair coefficient collapse costs only

\[
\boxed{Y^{o(1)}}.
\tag{H5.9}
\]

This is the coefficient-energy statement missing from tH4.

All bounded masks, smooth weights and unit-modulus phases from tH4 may be inserted before the collapse; they only decrease or preserve the source `L2` energy.

```text
FULL_EXACT_GAUSSIAN_PAIR_COEFFICIENT_COLLISION_ENERGY_PROVED=true
EXACT_PAIR_COLLAPSE_FIXED_POWER_LOSS=false
```

---

## 5. Unweighted collision energy is near-linear

For unit source weights, let

\[
\mathcal S
=
\{(h,r,\delta,U,V)\}
\]

and let

\[
E_{\rm exact}
=
\#\{(s,s')\in\mathcal S^2:
(U(s),V(s))=(U(s'),V(s'))\}.
\]

Then

\[
E_{\rm exact}
=
\sum_{U,V}\nu(U,V)^2.
\]

Since `nu<=tau_max(Y)`, while

\[
\sum_{U,V}\nu(U,V)=|\mathcal S|,
\]

we obtain

\[
\boxed{
E_{\rm exact}
\le
\tau_{\max}(Y)|\mathcal S|
=
Y^{o(1)}|\mathcal S|.
}
\tag{H5.10}
\]

Thus exact coefficient collisions have **near-linear energy**, not quadratic energy.

---

## 6. Finite-state aggregation is harmless

The tH2/tH3 state set contains only finitely many `(epsilon,g)` possibilities.  The cleanest downstream interface is to retain those labels until after the analytic theorem.

If a later theorem chooses to discard the labels first, Cauchy across the finite state set costs only an absolute constant depending on the frozen state family.

Therefore finite local/canonical state aggregation cannot consume a fixed power of `B`.

```text
FINITE_STATE_LABELS_RETAINABLE=true
FINITE_STATE_AGGREGATION_FIXED_POWER_LOSS=false
```

---

## 7. Why keeping both Gaussian coordinates matters

The paired result above is substantially stronger than a one-coordinate collapse.

If only `U` is retained, then fixing

\[
N(U)=m
\]

still allows the cover variable `delta` to range up to roughly

\[
Y/m,
\]

with corresponding variation in `V`.  That fiber can have polynomial size.

Thus tH5 does **not** claim

```text
U-only coefficient collision energy = B^o(1) times source energy.
```

The safe object is the exact pair `(U,V)` — precisely the paired object which tH3 required for same-modulus analysis.

```text
ONE_COORDINATE_PROJECTION_COLLISION_ENERGY_PROVED=false
PAIR_RETENTION_ESSENTIAL=true
```

---

## 8. Exact-pair collisions versus residue collisions

There are now two different collision notions and they must not be conflated.

### Exact coefficient collision — CLOSED here

```text
(U,V) = (U',V')
```

or equality up to a bounded unit-orbit convention.

This collision multiplicity is divisor-bounded by (H5.4).

### Same-modulus residue collision — NOT closed here

For an auxiliary Gaussian prime `varpi`, a joint character second moment may identify distinct pairs satisfying

\[
U\equiv uU'\pmod\varpi,
\qquad
V\equiv vV'\pmod\varpi,
\qquad u,v\in\mu_4.
\]

That is a modulus-dependent dispersion kernel.  tH5 does not turn such congruence into exact equality and does not claim a new same-modulus large-sieve theorem.

The practical consequence is valuable nevertheless: a future same-modulus theorem may now take the exact paired coefficients `A(U,V)` as input with a **proved subpolynomial coefficient-energy overhead**.  No hidden arithmetic collision factor remains before the residue-dispersion step.

```text
SAME_MODULUS_RESIDUE_COLLISION_ENERGY_PROVED=false
SAME_MODULUS_JOINT_SECOND_MOMENT_THEOREM_PROVED=false
```

---

## 9. Interface to a future joint theorem

A future same-modulus estimate may now start from

\[
M_{\mathfrak q}(\xi,\zeta)
=
\sum_{U,V}
A(U,V)\xi(U)\zeta(V)
\]

with the guaranteed coefficient budget

\[
\boxed{
\|A\|_2^2
\le
B^{o(1)}\|w\|_2^2.
}
\tag{H5.11}
\]

Combining tH3--tH5 gives the stable roadworks chain

```text
tH2 exact divisor-coupled hyperbola
  -> tH3 shared-modulus character/conductor packet
  -> tH4 weighted L2-safe transfer
  -> tH5 exact Gaussian-pair collision energy
  -> future same-modulus joint second moment / dispersion theorem.
```

No future t-stage identity is required for this chain.

---

## 10. Deterministic audit

The dedicated audit uses

```text
epsilon in {1,2,3,4,6,8,12}
Y = 128
```

and enumerates every transformed tH2 tuple.

Frozen totals:

```text
source transformed tuples                    33257
retained (epsilon,g,m,n) coefficient fibers  28955
maximum exact fiber multiplicity                 5
maximum tau(n), n<=128                          16
exact fiber-formula failures                      0
```

Fiber multiplicity histogram:

```text
multiplicity 1   25351 fibers
multiplicity 2    3043
multiplicity 3     431
multiplicity 4     123
multiplicity 5       7
```

For unit weights on norm pairs,

```text
exact norm-pair collision energy             43545
source tuple count                            33257
```

which is consistent with the theorem `E <= tau_max(Y)*|S|`.

Expanding every norm pair by its exact ordered signed two-square representations gives

```text
Gaussian source lifts                       357568
distinct exact Gaussian pair labels         314064
exact Gaussian-pair collision energy        460064
collision/source ratio            1.286647574727045
```

The collision multiplicity is unchanged because the representation pair itself is retained.

For deterministic signed source weights,

```text
source L2 energy                             366056
collapsed exact-pair L2 energy               395576
energy ratio                     1.0806433988242237
fiberwise Cauchy violations                       0
```

These finite computations audit the exact formulas; the asymptotic statement is the divisor bound (H5.4)--(H5.10).

---

## Proof boundary

```text
STAGE14_TH5=COMPLETE_EXACT_GAUSSIAN_PAIR_COEFFICIENT_COLLISION_ENERGY
TH_REQUIRES_FUTURE_T_RESULT=false
EXACT_SHARED_H_FIBER_FORMULA_PROVED=true
EXACT_PAIRED_NORM_COLLISION_MULTIPLICITY_LE_TAU_MAX=true
EXACT_GAUSSIAN_PAIR_COLLISION_MULTIPLICITY=DIVISOR_BOUNDED
FULL_EXACT_GAUSSIAN_PAIR_COEFFICIENT_COLLISION_ENERGY_PROVED=true
EXACT_PAIR_COLLAPSE_FIXED_POWER_LOSS=false
EXACT_PAIR_COLLISION_ENERGY=SOURCE_MASS*B^o(1)
UNIT_ORBIT_EXPANSION_COST_AT_MOST=16
PAIR_RETENTION_ESSENTIAL=true
ONE_COORDINATE_PROJECTION_COLLISION_ENERGY_PROVED=false
SAME_MODULUS_RESIDUE_COLLISION_ENERGY_PROVED=false
SAME_MODULUS_JOINT_SECOND_MOMENT_THEOREM_PROVED=false
NORM_INDEX_HYPERBOLIC_CORRELATION_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-tH6
```
