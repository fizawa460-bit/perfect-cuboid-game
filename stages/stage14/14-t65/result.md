# Stage14-t65 — Cayley divisor locks and exact cross-ratio fiber rigidity

## Purpose

Merged Stage14-t64 replaces the dominant fixed-`U` invisible squareclass geometry by the exact cross-ratio

\[
s=R=\frac{X-T}{1-TX},\qquad T=t^2,\quad X=x^2,
\]

with `0<s<1`, and shows that equal squareclass is the condition that two exact `s` values differ by a rational square.

Stage14-t65 asks whether the moving exact parameter `s` is itself arithmetically rigid once the fixed-`U` norm/divisor fan and the sharp invisible hyperbola are restored.

The answer is two-part:

1. **yes for an exact `s` fiber**: fixing `s` forces the radial variables `(ell,delta)` into divisor sets, so the physical lift is `B^{o(1)}` by merged t58;
2. **no for an entire squareclass by this argument alone**: `s=kappa(u/v)^2` retains a moving primitive square-scale `(u,v)`. The remaining obstruction is a two-sided quadratic divisor incidence for this square scale.

No new Stage14 power saving is claimed.

---

## 1. Fixed-U invisible norm skeleton

Fix a legal dominant invisible packet with primitive `U`, `epsilon`, and divisor-fan choice `k,h`. Write

\[
N(U)=m,\qquad N(V)=n=k\delta,\qquad hk=\varepsilon m.
\tag{65.1}
\]

For the canonical Gaussian prime `pi`,

\[
a^2+b^2=\ell m,
\tag{65.2}
\]

while in the invisible branch

\[
p^2+q^2=k\delta,
\qquad \ell\nmid k\delta.
\tag{65.3}
\]

Merged t37 gives the exact coprimality

\[
\gcd(\delta,h)=1.
\tag{65.4}
\]

The sharp physical size condition remains

\[
\varepsilon\ell m\delta/2\le B.
\tag{65.5}
\]

All canonical-prime, primitive-cover, chamber, reconstruction and branch masks remain attached.

---

## 2. Exact Cayley factorization by radial variables

For

\[
A=b^2p^2-a^2q^2,\qquad
B_0=b^2q^2-a^2p^2,
\]

t64 has `s=A/B_0`. Hence

\[
\frac{1+s}{1-s}=\frac{A+B_0}{B_0-A}.
\]

The sum and difference factor exactly:

\[
A+B_0=(b^2-a^2)(p^2+q^2),
\tag{65.6}
\]

\[
B_0-A=(a^2+b^2)(q^2-p^2).
\tag{65.7}
\]

Put

\[
D_\pi=b^2-a^2>0,\qquad D_V=q^2-p^2>0.
\]

Using (65.1)--(65.3), the Cayley coordinate of the exact cross-ratio is

\[
\boxed{
C(s):=\frac{1+s}{1-s}
=\frac{k\delta D_\pi}{\ell m D_V}
=\frac{\varepsilon\delta D_\pi}{\ell h D_V}.
}
\tag{65.8}
\]

Thus `k` cancels completely. The live radial variables occur on opposite sides: `delta` in the numerator and `ell*h` in the denominator.

```text
CAYLEY_RADIAL_FACTOR_IDENTITY_PROVED=true
K_CANCELS_FROM_CAYLEY_RADIAL_IDENTITY=true
```

---

## 3. Odd-part noncancellation

The primitive pairs satisfy

\[
\gcd(p,q)=\gcd(a,b)=1.
\]

Therefore

\[
\gcd(p^2+q^2,q^2-p^2)\mid2,
\tag{65.9}
\]

and

\[
\gcd(a^2+b^2,b^2-a^2)\mid2.
\tag{65.10}
\]

Since `delta | p^2+q^2`, (65.9) gives

\[
\gcd(\delta,D_V)_{\rm odd}=1.
\tag{65.11}
\]

Since the invisible condition gives `ell ∤ k delta`, in particular

\[
\gcd(\ell,\delta)=1.
\tag{65.12}
\]

Together with merged t37 `gcd(delta,h)=1`,

\[
\gcd(\delta,\ell hD_V)_{\rm odd}=1.
\tag{65.13}
\]

For the opposite side, every odd prime of `h` divides `m` because `hk=epsilon*m`; hence the odd part of `ell*h` divides the odd support of `ell*m=a^2+b^2`. Equation (65.10) therefore gives

\[
\gcd(\ell h,D_\pi)_{\rm odd}=1.
\tag{65.14}
\]

Combining (65.4), (65.12), and (65.14),

\[
\gcd(\ell h,\varepsilon\delta D_\pi)_{\rm odd}=1.
\tag{65.15}
\]

Now write the reduced positive rational number

\[
C(s)=\frac{N_s}{D_s},\qquad \gcd(N_s,D_s)=1.
\tag{65.16}
\]

Equations (65.8), (65.13), and (65.15) imply the exact divisor locks

\[
\boxed{\operatorname{odd}(\delta)\mid N_s,}
\tag{65.17}
\]

\[
\boxed{\operatorname{odd}(\ell h)\mid D_s.}
\tag{65.18}
\]

Only bounded 2-adic ambiguity remains; for primitive sums of two squares it is harmless `B^{o(1)}` bookkeeping.

```text
ODD_DELTA_SURVIVES_REDUCED_CAYLEY_NUMERATOR=true
ODD_ELL_H_SURVIVES_REDUCED_CAYLEY_DENOMINATOR=true
CAYLEY_RADIAL_CROSS_CANCELLATION_FIXED_POWER=false
```

---

## 4. Exact cross-ratio fiber is divisor-many

Fix `U,epsilon,k,h` and an exact rational `s in (0,1)`. Then `N_s,D_s` in (65.16) are fixed integers of polynomial height in the Stage14 range.

By (65.17), `delta` has only divisor-many odd choices from `N_s`; by (65.18), the odd prime `ell` is forced into the divisor support of `D_s` after the fixed `h` is retained. The 2-adic choices are bounded.

Hence

\[
\#\{(\ell,\delta):\text{legal radial data for fixed }s\}=B^{o(1)}.
\tag{65.19}
\]

Merged t58 proves that a fixed invisible radial cell

\[
(U,\varepsilon,k,\ell,\delta)
\]

has physical angular lift multiplicity `B^{o(1)}`. Therefore

\[
\boxed{
\#\{\text{physical invisible states with fixed }(U,\varepsilon,k,s)\}
\le B^{o(1)}.
}
\tag{65.20}
\]

Define

```text
SharedUExactCrossRatioFiberMultiplicity.
```

It is proved at t65.

This is strictly stronger than the finite observation that exact cross-ratio values are usually unique: the proof is uniform and uses the exact divisor locks plus t58 radial-cell multiplicity.

```text
SHARED_U_EXACT_CROSS_RATIO_FIBER_MULTIPLICITY=Bo1
SHARED_U_EXACT_CROSS_RATIO_FIBER_MULTIPLICITY_PROVED=true
```

---

## 5. What remains inside one squareclass

Let `kappa` be the positive squarefree representative of a squareclass. Since `s>0`, write uniquely up to sign

\[
s=\kappa\left(\frac uv\right)^2,
\qquad \gcd(u,v)=1,
\qquad v^2>\kappa u^2>0.
\tag{65.21}
\]

Then

\[
\boxed{
C(s)=\frac{v^2+\kappa u^2}{v^2-\kappa u^2}.
}
\tag{65.22}
\]

Set

\[
g_\kappa(u,v)=\gcd(v^2+\kappa u^2,v^2-\kappa u^2).
\tag{65.23}
\]

If an odd prime `r` divides both factors and `r∤kappa`, then `r|u` and `r|v`, impossible. Since `kappa` is squarefree, any odd common divisor is supported on `kappa`. Hence

\[
\boxed{g_\kappa(u,v)\mid 2\kappa.}
\tag{65.24}
\]

After reducing (65.22), the physical divisor locks become

\[
\boxed{
\operatorname{odd}(\delta)
\mid
\frac{v^2+\kappa u^2}{g_\kappa(u,v)},
}
\tag{65.25}
\]

\[
\boxed{
\operatorname{odd}(\ell h)
\mid
\frac{v^2-\kappa u^2}{g_\kappa(u,v)}.
}
\tag{65.26}
\]

Thus all moving cancellation between the two Cayley factors is confined to the fixed squareclass support `2*kappa`; there is no new unrestricted moving gcd.

This is the genuine residual arithmetic object.

---

## 6. New minimal square-scale receiver

Because exact `s` fibers cost only `B^{o(1)}`, the dominant invisible fixed-`U` squareclass problem no longer needs a uniform point bound on the Jacobi quartic for each exact parameter.

It reduces to controlling how many primitive square scales `(u,v)` from (65.21) can occur in one physical squareclass while satisfying simultaneously

```text
odd(delta) | (v^2+kappa*u^2)/g_kappa
odd(ell*h) | (v^2-kappa*u^2)/g_kappa
ell*delta <= Y_U
canonical-prime mask on ell
primitive V / reconstruction masks
```

with `g_kappa | 2*kappa`.

Define

```text
SharedUCayleySquareScaleDivisorIncidence
```

for this physical primitive `(u,v)` incidence. Proving its near-linear square-ratio energy would imply `SharedUTransverseJacobiSquareLiftIncidence`, and hence the dominant invisible part of the t63/tH15 receiver.

```text
SHARED_U_CAYLEY_SQUARE_SCALE_DIVISOR_INCIDENCE_PROVED=false
SHARED_U_TRANSVERSE_JACOBI_SQUARE_LIFT_INCIDENCE_PROVED=false
```

---

## 7. Why fixed exact-s rigidity does not yet close squareclass energy

Equation (65.20) controls repeated states with the **same exact rational** `s`. Equal squareclass permits

\[
s_2/s_1\in\mathbf Q^{*2},
\]

so different primitive `(u,v)` values can still lie in the same class `kappa`.

Therefore it is invalid to infer

```text
exact-s fiber B^o
=> squareclass fiber B^o.
```

The finite family indeed contains same-squareclass pairs with distinct exact cross-ratios, already locked by t64.

Likewise a quadratic large sieve after deduplicating by `kappa` remains circular: its coefficient energy is exactly the square-scale energy now isolated in (65.21)--(65.26).

---

## 8. tH decision

`tH18` is **not needed yet**.

The t64 Jacobi/K3-shaped obstruction has been reduced internally to elementary two-sided quadratic divisibility with a fixed gcd defect `g_kappa | 2*kappa`. A generic uniform Jacobi-quartic theorem would now be stronger than necessary.

Stage14-t66 should first split the two quadratic factors in (65.25)--(65.26) prime-by-prime, exploit `gcd(delta,ell*h)=1`, and test whether the sharp product budget `ell*delta<=Y_U` plus the opposite-sign factors gives a divisor/CRT parameterization of `(u,v)`.

If t66 still leaves a genuine average theorem for primitive solutions of the simultaneous `v^2 ± kappa u^2` divisibility system, that precise theorem is the correct trigger for `tH18`.

```text
TH18_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH=false
```

---

## Locked boundary

```text
STAGE14_T65=COMPLETE_CAYLEY_RADIAL_DIVISOR_LOCK_AND_EXACT_S_FIBER_RIGIDITY
MERGED_T64_IMPORTED=true
MERGED_T58_RADIAL_CELL_BOUND_IMPORTED=true
MERGED_T37_GCD_DELTA_H_IMPORTED=true
CAYLEY_RADIAL_FACTOR_IDENTITY_PROVED=true
K_CANCELS_FROM_CAYLEY_RADIAL_IDENTITY=true
ODD_DELTA_SURVIVES_REDUCED_CAYLEY_NUMERATOR=true
ODD_ELL_H_SURVIVES_REDUCED_CAYLEY_DENOMINATOR=true
SHARED_U_EXACT_CROSS_RATIO_FIBER_MULTIPLICITY=Bo1
SHARED_U_EXACT_CROSS_RATIO_FIBER_MULTIPLICITY_PROVED=true
SQUARECLASS_SCALE_PARAMETERIZATION_PROVED=true
CAYLEY_PLUS_MINUS_GCD_DIVIDES_2KAPPA=true
CAYLEY_SQUARE_SCALE_TWO_SIDED_DIVISOR_LOCK_PROVED=true
SHARED_U_CAYLEY_SQUARE_SCALE_DIVISOR_INCIDENCE_PROVED=false
SHARED_U_TRANSVERSE_JACOBI_SQUARE_LIFT_INCIDENCE_PROVED=false
SHARED_U_TRANSVERSE_VERTICAL_KUMMER_DISPERSION_PROVED=false
SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED=false
SHARED_U_MIXED_BRANCH_DISPERSION_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
TH18_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH=false
NEXT=Stage14-t66
```
