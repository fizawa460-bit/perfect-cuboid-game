# Stage14-t65 — Cayley divisor locks, canonical-prime recovery, and square-scale reduction

## Purpose

Merged Stage14-t64 replaces the dominant fixed-`U` invisible squareclass geometry by the exact cross-ratio

\[
s=R=\frac{X-T}{1-TX},\qquad T=t^2,\quad X=x^2,
\]

with `0<s<1`, and proves that equal squareclass is exactly the condition that two exact `s` values differ by a rational square.

Stage14-t65 restores the fixed-`U` norm skeleton and the sharp super-square-root physical budget. The outcome is stronger than a generic divisor bound:

1. the reduced Cayley denominator of an exact physical `s` contains the canonical prime `ell` with a cofactor strictly smaller than `ell/2`;
2. hence `ell` is the unique largest odd prime factor of that denominator;
3. fixed `(U,s)` has only `O(1)` invisible physical lifts;
4. after writing `s=kappa(u/v)^2`, the entire remaining squareclass problem is an elementary simultaneous divisibility problem for `v^2±kappa u^2`, with all common cancellation confined to the fixed support `2*kappa`.

No whole-family power saving is claimed.

---

## 1. Fixed-U invisible norm skeleton

Fix a legal dominant invisible packet with primitive `U`. Write

\[
N(U)=m,
\qquad
N(V)=n=k\delta,
\qquad
hk=\varepsilon m.
\tag{65.1}
\]

Merged t37 gives

\[
\boxed{\gcd(\delta,h)=1.}
\tag{65.2}
\]

The direction and cover norms are

\[
a^2+b^2=\ell m,
\qquad
p^2+q^2=k\delta,
\tag{65.3}
\]

and invisible means

\[
\ell\nmid k\delta.
\tag{65.4}
\]

The physical budget is

\[
\frac{\varepsilon\ell m\delta}{2}\le B,
\tag{65.5}
\]

while the branch under discussion is super-square-root,

\[
\ell^2>4B.
\tag{65.6}
\]

Combining (65.5)--(65.6),

\[
\boxed{\ell>2\varepsilon m\delta.}
\tag{65.7}
\]

In particular `ell>2m`, `ell>2n`, and `ell` is larger than every cofactor norm in this packet.

---

## 2. Exact Cayley radial identity

Put

\[
A=b^2p^2-a^2q^2,
\qquad
B_0=b^2q^2-a^2p^2,
\]

so t64 gives `s=A/B_0`. Define

\[
D_\pi=b^2-a^2>0,
\qquad
D_V=q^2-p^2>0.
\]

Then

\[
A+B_0=D_\pi(p^2+q^2),
\]

\[
B_0-A=(a^2+b^2)D_V.
\]

Therefore the Cayley coordinate

\[
C(s)=\frac{1+s}{1-s}
\]

satisfies the exact identity

\[
\boxed{
C(s)
=\frac{k\delta D_\pi}{\ell mD_V}
=\frac{\varepsilon\delta D_\pi}{\ell hD_V}.
}
\tag{65.8}
\]

The divisor-fan variable `k` cancels completely.

```text
CAYLEY_RADIAL_FACTOR_IDENTITY_PROVED=true
K_CANCELS_FROM_CAYLEY_RADIAL_IDENTITY=true
```

---

## 3. Odd-part reduction has only one moving cross-gcd

For an integer `z`, write `odd(z)` for its odd part. Primitive pairs give

\[
\gcd(a^2+b^2,b^2-a^2)\mid2,
\tag{65.9}
\]

\[
\gcd(p^2+q^2,q^2-p^2)\mid2.
\tag{65.10}
\]

Since `odd(h)` divides the odd support of `m`, (65.9) implies

\[
\gcd(\ell h,D_\pi)_{\rm odd}=1.
\tag{65.11}
\]

Since `delta|p^2+q^2`, (65.10) gives

\[
\gcd(\delta,D_V)_{\rm odd}=1.
\tag{65.12}
\]

Together with (65.2) and invisibility,

\[
\gcd(\delta,\ell hD_V)_{\rm odd}=1.
\tag{65.13}
\]

Thus the only unrestricted odd cancellation in (65.8) is

\[
g=\gcd(\operatorname{odd}(D_\pi),\operatorname{odd}(D_V)).
\tag{65.14}
\]

Write the reduced positive rational number as

\[
C(s)=\frac{N_s}{D_s},\qquad \gcd(N_s,D_s)=1.
\tag{65.15}
\]

Then exactly on odd parts,

\[
\boxed{
\operatorname{odd}(N_s)
=\operatorname{odd}(\delta)\,
\frac{\operatorname{odd}(D_\pi)}{g},
}
\tag{65.16}
\]

\[
\boxed{
\operatorname{odd}(D_s)
=\ell\,\operatorname{odd}(h)\,
\frac{\operatorname{odd}(D_V)}{g}.
}
\tag{65.17}
\]

In particular

\[
\operatorname{odd}(\delta)\mid N_s,
\qquad
\operatorname{odd}(\ell h)\mid D_s.
\tag{65.18}
\]

No polynomial cross-cancellation can remove `delta` from the Cayley numerator or `ell*h` from the Cayley denominator.

---

## 4. The canonical prime is recoverable from the exact cross-ratio

The cofactor of `ell` in (65.17) is

\[
c_s
:=\frac{\operatorname{odd}(D_s)}{\ell}
=\operatorname{odd}(h)\,
\frac{\operatorname{odd}(D_V)}{g}.
\tag{65.19}
\]

Since

\[
D_V=q^2-p^2<p^2+q^2=n=k\delta,
\]

we get

\[
c_s<hk\delta=\varepsilon m\delta.
\tag{65.20}
\]

Using (65.7),

\[
\boxed{2c_s<\ell.}
\tag{65.21}
\]

Therefore

\[
\boxed{
\ell=\operatorname{LPF}_{\rm odd}(D_s),
}
\tag{65.22}
\]

where `LPF_odd` denotes the largest odd prime factor. Moreover `ell` occurs in the reduced odd denominator with exponent one, because `ell>n>D_V` and `ell>h`.

This is stronger than saying `ell` is one divisor choice: the exact rational value `s` determines its canonical rational prime uniquely.

```text
CANONICAL_ELL_SURVIVES_REDUCED_CAYLEY_DENOMINATOR=true
CAYLEY_DENOMINATOR_ELL_COFACTOR_LT_ELL_OVER_2=true
CANONICAL_ELL_EQUALS_LARGEST_ODD_PRIME_FACTOR=true
```

---

## 5. Fixed `(U,s)` invisible fiber is uniformly finite

Fix primitive `U` and an exact rational `s in (0,1)`.

1. Equation (65.22) determines `ell` uniquely from `s`.
2. A rational prime `ell=1 mod 4` has only finitely many Gaussian prime associates of norm `ell` (at most eight signed/conjugate representations).
3. For each such `pi`, `a+ib=pi U` determines the direction slope `t=a/b` up to the already-finite unit/orientation conventions.
4. t64's Möbius identity
   \[
   x^2=\frac{t^2+s}{1+st^2}
   \]
   then determines the positive rational slope `x=p/q` uniquely if a physical square lift exists.
5. Primitive `(p,q)` is unique for a rational slope `x`.

Hence

\[
\boxed{
\#\{\text{dominant invisible physical states with fixed }(U,s)\}
=O(1).
}
\tag{65.23}
\]

The constant is only the finite Gaussian-unit / branch-normalization ambiguity and is independent of `B`.

This strengthens the preliminary `B^{o(1)}` exact-value fiber bound and does not require Cauchy over radial cells.

```text
SHARED_U_EXACT_CROSS_RATIO_FIBER_MULTIPLICITY=O(1)
SHARED_U_EXACT_CROSS_RATIO_FIBER_MULTIPLICITY_PROVED=true
```

---

## 6. Squareclass scale parameterization

Let `kappa` be the positive squarefree representative of the squareclass. Since `0<s<1`, write

\[
\boxed{
s=\kappa\left(\frac uv\right)^2,
\qquad
\gcd(u,v)=1,
\qquad
v^2>\kappa u^2>0.
}
\tag{65.24}
\]

Then

\[
\boxed{
C(s)=\frac{v^2+\kappa u^2}{v^2-\kappa u^2}.
}
\tag{65.25}
\]

Put

\[
g_\kappa(u,v)
=\gcd(v^2+\kappa u^2,v^2-\kappa u^2).
\tag{65.26}
\]

If an odd prime divides both factors, primitivity of `(u,v)` forces it to divide `kappa`; because `kappa` is squarefree its gcd valuation is one. The 2-adic part is bounded. Therefore

\[
\boxed{g_\kappa(u,v)\mid2\kappa.}
\tag{65.27}
\]

Consequently the reduced Cayley numerator and denominator are exactly

\[
N_s=\frac{v^2+\kappa u^2}{g_\kappa(u,v)},
\qquad
D_s=\frac{v^2-\kappa u^2}{g_\kappa(u,v)}.
\tag{65.28}
\]

All plus/minus cancellation is supported on the fixed squareclass datum `2*kappa`; there is no additional moving gcd.

---

## 7. Canonical-prime-tagged two-sided quadratic divisor system

Combining (65.18), (65.22), and (65.28), every dominant invisible state in squareclass `kappa` supplies a primitive pair `(u,v)` satisfying

\[
\boxed{
\operatorname{odd}(\delta)
\mid
\frac{v^2+\kappa u^2}{g_\kappa(u,v)},
}
\tag{65.29}
\]

\[
\boxed{
\operatorname{odd}(\ell h)
\mid
\frac{v^2-\kappa u^2}{g_\kappa(u,v)},
}
\tag{65.30}
\]

and, more sharply,

\[
\boxed{
\ell
=\operatorname{LPF}_{\rm odd}
\left(
\frac{v^2-\kappa u^2}{g_\kappa(u,v)}
\right),
}
\tag{65.31}
\]

with the remaining denominator cofactor `<ell/2`.

The sharp hyperbola remains

\[
\ell\delta\le Y_U:=\frac{2B}{\varepsilon m}.
\tag{65.32}
\]

Thus the live invisible principal problem is no longer a generic Jacobi/K3 point count. It is a primitive simultaneous quadratic divisor incidence with a recoverable canonical largest-prime tag.

Define

```text
SharedUCanonicalPrimeTaggedCayleySquareScaleIncidence.
```

Because fixed `(U,s)` fibers are `O(1)`, proving near-linear energy for this `(kappa,u,v)` incidence is sufficient for `SharedUTransverseJacobiSquareLiftIncidence` and hence for the dominant invisible part of t63/tH15 SUBD.

```text
CAYLEY_PLUS_MINUS_GCD_DIVIDES_2KAPPA=true
CAYLEY_SQUARE_SCALE_TWO_SIDED_DIVISOR_LOCK_PROVED=true
CANONICAL_PRIME_TAGGED_QUADRATIC_NORM_FORM_PROVED=true
SHARED_U_CANONICAL_PRIME_TAGGED_CAYLEY_SQUARE_SCALE_INCIDENCE_PROVED=false
```

---

## 8. Why exact-value rigidity does not close squareclass energy

Equation (65.23) controls repeated states having the same exact rational `s`. Equal squareclass only requires

\[
s_1/s_2\in\mathbf Q^{*2},
\]

so distinct primitive square scales `(u,v)` remain live in the same `kappa` class.

The frozen family contains such distinct exact cross-ratios inside one squareclass, so the implication

```text
exact-s fiber O(1)
=> squareclass fiber O(1)
```

is false as a logical shortcut.

Likewise, deduplicating the states by `kappa` before a quadratic large sieve recreates the unresolved squareclass coefficient energy. No `E4` coefficient collapse is used here.

---

## 9. tH decision

`tH18` is **not needed yet**.

The broad Jacobi/K3 obstruction has been reduced internally to the explicit simultaneous system (65.29)--(65.32), and the canonical prime is now an intrinsic largest-prime label of the negative quadratic factor. Before requesting a new theorem family, Stage14-t66 should use:

1. prime-by-prime splitting of `v^2+kappa u^2` and `v^2-kappa u^2`;
2. `g_kappa|2kappa`;
3. `gcd(delta,ell*h)=1`;
4. `ell=LPF_odd((v^2-kappa u^2)/g_kappa)`;
5. `ell*delta<=Y_U` and the strict cofactor `<ell/2`.

If t66 still leaves a genuine average theorem for primitive solutions of this simultaneous quadratic divisibility system, that exact theorem is the correct trigger for `tH18`.

```text
TH18_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH=false
```

---

## Locked boundary

```text
STAGE14_T65=COMPLETE_CAYLEY_CANONICAL_PRIME_RECOVERY_AND_SQUARE_SCALE_DIVISOR_REDUCTION
MERGED_T64_IMPORTED=true
MERGED_T37_GCD_DELTA_H_IMPORTED=true
CAYLEY_RADIAL_FACTOR_IDENTITY_PROVED=true
K_CANCELS_FROM_CAYLEY_RADIAL_IDENTITY=true
ODD_DELTA_SURVIVES_REDUCED_CAYLEY_NUMERATOR=true
ODD_ELL_H_SURVIVES_REDUCED_CAYLEY_DENOMINATOR=true
CAYLEY_DENOMINATOR_ELL_COFACTOR_LT_ELL_OVER_2=true
CANONICAL_ELL_EQUALS_LARGEST_ODD_PRIME_FACTOR=true
SHARED_U_EXACT_CROSS_RATIO_FIBER_MULTIPLICITY=O(1)
SHARED_U_EXACT_CROSS_RATIO_FIBER_MULTIPLICITY_PROVED=true
SQUARECLASS_SCALE_PARAMETERIZATION_PROVED=true
CAYLEY_PLUS_MINUS_GCD_DIVIDES_2KAPPA=true
CAYLEY_SQUARE_SCALE_TWO_SIDED_DIVISOR_LOCK_PROVED=true
CANONICAL_PRIME_TAGGED_QUADRATIC_NORM_FORM_PROVED=true
SHARED_U_CANONICAL_PRIME_TAGGED_CAYLEY_SQUARE_SCALE_INCIDENCE_PROVED=false
SHARED_U_TRANSVERSE_JACOBI_SQUARE_LIFT_INCIDENCE_PROVED=false
SHARED_U_TRANSVERSE_VERTICAL_KUMMER_DISPERSION_PROVED=false
SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED=false
SHARED_U_MIXED_BRANCH_DISPERSION_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
TH18_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH=false
NEXT=Stage14-t66
```
