# Stage14-t67 — canonical root modulus collapse and private-prime cross-modulus reduction

## Purpose

Merged Stage14-t66 reduces the dominant fixed-`U` invisible squareclass problem to opposite-sign quadratic root lines

\[
z^2\equiv-\kappa\pmod{\operatorname{odd}(\delta)},\qquad
z^2\equiv+\kappa\pmod{\ell\operatorname{odd}(h)},
\]

with `z=v/u`, `hk=epsilon*m`, `gcd(delta,h)=1`, and the canonical prime `ell` distinguished on the negative side.

Stage14-t67 removes two pieces of apparent freedom that are still present in that formulation.

1. The two moving radial variables `(ell,delta)` are not an irreducible hyperbola for the root-line problem.  After fixing the divisor-fan packet `(U,epsilon,k,h)`, they combine into one canonical root modulus

   ```text
   M = ell * odd(h) * odd(delta).
   ```

   The prime `ell` is recoverable from `M` itself as its unique largest odd prime, so `M` recovers the odd radial data.

2. Same-`ell` principal collisions and the only possible cross-modulus contamination in which the smaller canonical prime divides the larger modulus are already near-linear by t36 plus divisor counting.  Consequently the unresolved receiver may be restricted to **private-canonical-prime cross-modulus pairs**.

No whole-family power saving is claimed.  The unconditional exponent remains `7/8`.

---

## 1. Fixed packet and imported t66 root system

Fix primitive `U`, `epsilon`, and one divisor-fan choice `(k,h)`:

\[
N(U)=m,\qquad N(V)=k\delta,\qquad hk=\varepsilon m.
\tag{67.1}
\]

The number of such `(epsilon,k,h)` refinements for a fixed `U` is `B^{o(1)}`, so this conditioning is legal.

Merged t37/t65/t66 give

\[
(\delta,h)=1,
\qquad
\ell\nmid k\delta,
\qquad
\ell>2\varepsilon m\delta,
\tag{67.2}
\]

and all odd primes in `delta`, `h`, or `ell` are `1 mod 4` and are coprime to the squareclass `kappa`.

Put

\[
D=\operatorname{odd}(\delta),
\qquad
H=\operatorname{odd}(h).
\tag{67.3}
\]

Then t66 gives

\[
(z,DH\ell)=1,
\tag{67.4}
\]

and

\[
z^2\equiv-\kappa\pmod D,
\qquad
z^2\equiv+\kappa\pmod{\ell H}.
\tag{67.5}
\]

The side label is retained; it is not replaced by the common Legendre condition `(kappa/r)=1`.

---

## 2. Collapse the radial hyperbola to one modulus

Define the **canonical root modulus**

\[
\boxed{M:=\ell H D.}
\tag{67.6}
\]

Because `(delta,h)=1`, invisibility, and `ell>h,delta`, the three odd factors in (67.6) are pairwise coprime in the required radial sense.

The sharp super-square-root inequality gives

\[
HD\le h\delta\le\varepsilon m\delta<\frac\ell2.
\tag{67.7}
\]

Therefore

\[
\boxed{\frac M\ell=HD<\frac\ell2.}
\tag{67.8}
\]

In particular:

\[
\boxed{\ell=\operatorname{LPF}_{\rm odd}(M),}
\tag{67.9}
\]

`ell` occurs in `M` to exponent one, and every other prime factor of `M` is strictly smaller than `ell`.

Since `H=odd(h)` is fixed in the packet, `M` then recovers

\[
\boxed{D=\frac{M}{\ell H}.}
\tag{67.10}
\]

The omitted 2-adic part of `delta` has only bounded multiplicity because `N(V)=k delta` is a primitive Gaussian norm.  Hence

```text
fixed (U,epsilon,k,h,M)
=> (ell,delta) has O(1) radial possibilities.
```

Thus the t66 two-modulus/hyperbola parameterization is losslessly replaced by one integer modulus `M`, up to bounded 2-primary decoration.

```text
CANONICAL_ROOT_MODULUS_DEFINED=true
CANONICAL_ELL_RECOVERED_FROM_ROOT_MODULUS=true
ODD_DELTA_RECOVERED_FROM_ROOT_MODULUS=true
RADIAL_HYPERBOLA_TO_SINGLE_MODULUS_LOSS=O1
```

---

## 3. Exact modulus band

The canonical prime remains super-square-root:

\[
\ell^2>4B.
\]

Since `M>=ell`,

\[
\boxed{M>2\sqrt B.}
\tag{67.11}
\]

On the other hand,

\[
M=\ell HD\le\ell h\delta
=\frac{\ell\varepsilon m\delta}{k}
\le\frac{2B}{k}.
\tag{67.12}
\]

Hence every physical canonical root modulus lies in the explicit band

\[
\boxed{2\sqrt B<M\le\frac{2B}{k}.}
\tag{67.13}
\]

In particular this branch is empty unless `k<sqrt(B)` up to the harmless endpoint convention.

The important point is that tH18 does not need to average over an unconstrained two-dimensional `(ell,delta)` hyperbola.  The physical moduli form a one-dimensional family with a distinguished dominant largest prime.

```text
CANONICAL_ROOT_MODULUS_SUPER_SQRT_BAND_PROVED=true
CANONICAL_ROOT_MODULUS_UPPER_BOUND=2B_over_k
```

---

## 4. Side allocation is intrinsic to M

For fixed `(h,k)` and a legal modulus `M`, let

\[
\ell(M)=\operatorname{LPF}_{\rm odd}(M),
\qquad
D(M)=\frac{M}{\ell(M)H}.
\tag{67.14}
\]

Then the t66 root packet is exactly

\[
\boxed{
\Omega_{\kappa,h}(M)
=\{\rho\in(\mathbf Z/M\mathbf Z)^*:
\rho^2\equiv+\kappa\pmod{\ell(M)H},\ 
\rho^2\equiv-\kappa\pmod{D(M)}\}.
}
\tag{67.15}
\]

Every prime-power factor is odd, coprime to `kappa`, and solvable with exactly two roots.  Therefore

\[
|\Omega_{\kappa,h}(M)|=2^{\omega(M)}\le\tau(M)=B^{o(1)}
\tag{67.16}
\]

on a nonempty physical packet.

The former `(Q_+,Q_-)` side allocation is no longer extra moving data: once `M` and fixed `h` are known, the positive side is `D(M)` and the negative side is `ell(M)H`.

```text
ROOT_SIDE_ALLOCATION_RECOVERED_FROM_M=true
ROOT_CLASSES_PER_M=Bo1
```

---

## 5. Fixed-M physical multiplicity is already subpolynomial

Merged t58 proves that a fixed invisible radial cell

\[
(U,\varepsilon,k,\ell,\delta)
\]

has physical angular lift multiplicity `B^{o(1)}`.

By Sections 2--3, fixed `(U,epsilon,k,h,M)` recovers `(ell,delta)` up to bounded 2-primary ambiguity.  Therefore

\[
\boxed{
R_{U,k,h}(M)
:=\#\{\text{physical invisible states with this }M\}
\le B^{o(1)}.
}
\tag{67.17}
\]

Consequently the entire same-modulus squareclass energy is automatically near-linear:

\[
\sum_M\sum_\kappa r_M(\kappa)^2
\le
\sum_M R_{U,k,h}(M)^2
\le
R_{U,k,h}B^{o(1)}.
\tag{67.18}
\]

This supersedes the interpretation that a difficult physical lift theorem is still needed *inside one CRT root modulus*.  The remaining obstruction is exclusively cross-modulus.

```text
FIXED_CANONICAL_ROOT_MODULUS_PHYSICAL_MULTIPLICITY=Bo1
SAME_ROOT_MODULUS_SQUARECLASS_ENERGY_NEAR_LINEAR=true
```

---

## 6. Same-canonical-prime energy is also already near-linear

Fix `ell` and `U`.  A rational prime `ell=1 mod 4` has only finitely many Gaussian prime associates, so `a+ib=pi U` produces only `O(1)` fixed directions after the canonical unit/orientation conventions.

For each such fixed direction, merged t36 proves

\[
E_{a,b}\le J_{a,b}B^{o(1)},
\tag{67.19}
\]

and, more pointwise, every fixed squareclass occurs only `B^{o(1)}` times in that direction fiber.

Taking the union of the `O(1)` directions and using Cauchy on the finitely many cross-direction terms gives

\[
\boxed{
E_{U,\ell}^{\rm sqclass}
\le R_{U,\ell}B^{o(1)}.
}
\tag{67.20}
\]

Hence same-`ell` principal collisions may be removed from the new receiver without asking tH18 to control them.

```text
SAME_CANONICAL_ELL_SQUARECLASS_ENERGY_NEAR_LINEAR=true
```

---

## 7. The nested-prime contamination graph is divisor-many

Write every canonical root modulus uniquely as

\[
M=\ell c,
\qquad
c=HD<\ell/2.
\tag{67.21}
\]

Consider two states in the same squareclass with distinct canonical primes, say

\[
\ell_1<\ell_2.
\]

The larger canonical prime can never divide the smaller modulus: since

\[
M_1=\ell_1c_1,
\qquad c_1<\ell_1/2<\ell_2,
\]

we have

\[
\ell_2\nmid M_1.
\tag{67.22}
\]

The only possible canonical-prime contamination is therefore

\[
\ell_1\mid M_2.
\]

Because `ell_1!=ell_2`, this is equivalent to

\[
\boxed{\ell_1\mid c_2.}
\tag{67.23}
\]

For a fixed larger state, `c_2` has only

\[
\omega(c_2)\le\tau(c_2)=B^{o(1)}
\]

possible smaller canonical prime divisors.  For each fixed such `ell_1` and the fixed squareclass of the larger state, Section 6 / t36 gives only `B^{o(1)}` physical states with that same `ell_1` and squareclass.

Thus the total ordered nested-prime principal incidence satisfies

\[
\boxed{I_{\rm nested}\le R_{U,k,h}B^{o(1)}.}
\tag{67.24}
\]

This removes the only case where a canonical prime of one state appears in the other state's root modulus.

```text
NESTED_CANONICAL_PRIME_INCIDENCE_NEAR_LINEAR=true
```

---

## 8. Exact remaining pair type: private canonical primes

After Sections 5--7, the unresolved principal pair may be assumed to satisfy

```text
same squareclass kappa,
M1 != M2,
ell1 != ell2,
ell1 does not divide M2,
ell2 does not divide M1.
```

Equivalently, each canonical largest prime is **private to its own root modulus**.

For such a pair, write

\[
M_i=\ell_i c_i,
\qquad c_i<\ell_i/2.
\]

Then

\[
\gcd(M_1,M_2)\mid\gcd(c_1,c_2),
\tag{67.25}
\]

so the common modulus contains neither distinguished canonical prime.  All common-prime interaction is confined to the two small cofactors.

Define the minimal remaining invisible receiver

```text
SharedUPrivateCanonicalPrimeRootModulusEnergy.
```

It asks for

\[
\boxed{
I_{\rm private}
\le R_{U,k,h}B^{o(1)}
}
\tag{67.26}
\]

for same-squareclass cross-modulus pairs with private canonical primes, retaining the exact root sets (67.15), the modulus band (67.13), and all primitive/canonical/reconstruction masks.

If (67.26) holds, then together with t36/t38/t58/t63 and the same-`ell`/nested reductions above, the dominant invisible fixed-`U` principal energy is near-linear.

```text
SHARED_U_PRIVATE_CANONICAL_PRIME_ROOT_MODULUS_ENERGY_PROVED=false
```

---

## 9. Consequence for tH18

`tH18` is still needed, but its requested theorem can now be made substantially narrower than the t66 formulation.

The preferred object is

```text
PrivateCanonicalPrimeOppositeSignRootModulusLargeSieve
```

on the exact family

```text
M = ell*c,
2*sqrt(B) < M <= 2B/k,
c < ell/2,
ell = LPF_odd(M),
ell exponent one,

rho^2 = +kappa mod ell*odd(h),
rho^2 = -kappa mod M/(ell*odd(h)).
```

and only for cross-modulus pairs satisfying

```text
ell1 not | M2,
ell2 not | M1.
```

The following are already handled internally and should **not** be charged again by tH18:

1. `(ell,delta)` hyperbola multiplicity;
2. CRT root count `2^omega(M)`;
3. fixed-`M` physical lift multiplicity;
4. same-`ell` squareclass energy;
5. nested canonical-prime divisibility pairs.

Useful theorem families to audit are therefore now limited to cross-modulus root-fraction large sieve / dispersion, polynomial-root spacing with a private largest-prime component, and biquadratic ideal/root-orientation methods that preserve the opposite-sign side allocation.

Do not collapse the two sides to `(kappa/r)=1`, and do not pre-collapse to squareclass coefficient energy.

```text
TH18_NEEDED=true
TH18_REQUESTED_OBJECT=PrivateCanonicalPrimeOppositeSignRootModulusLargeSieve
T_ROUTE_BLOCKED_WAITING_FOR_TH18=false
```

---

## 10. Next internal step

Stage14-t68 should attack a pair of private canonical root moduli directly.  The correct algebraic questions are:

1. what exact divisibility/resultant relation is forced on the cross-determinants of two roots of the same `kappa` packet;
2. whether private `ell_1,ell_2` can be charged to distinct cross-determinant factors;
3. whether the small common cofactor `gcd(c_1,c_2)` can be conditioned at `B^{o(1)}` cost;
4. whether, after that conditioning, the two canonical primes force a product divisor too large for the physical height window.

This can proceed in parallel with tH18.

---

## Locked boundary

```text
STAGE14_T67=COMPLETE_CANONICAL_ROOT_MODULUS_COLLAPSE_AND_PRIVATE_PRIME_REDUCTION
MERGED_T66_IMPORTED=true
CANONICAL_ROOT_MODULUS_DEFINED=true
CANONICAL_ROOT_MODULUS=M=ell*odd(h)*odd(delta)
CANONICAL_ELL_RECOVERED_FROM_ROOT_MODULUS=true
ODD_DELTA_RECOVERED_FROM_ROOT_MODULUS=true
RADIAL_HYPERBOLA_TO_SINGLE_MODULUS_LOSS=O1
ROOT_SIDE_ALLOCATION_RECOVERED_FROM_M=true
CANONICAL_ROOT_MODULUS_SUPER_SQRT_BAND_PROVED=true
FIXED_CANONICAL_ROOT_MODULUS_PHYSICAL_MULTIPLICITY=Bo1
SAME_ROOT_MODULUS_SQUARECLASS_ENERGY_NEAR_LINEAR=true
SAME_CANONICAL_ELL_SQUARECLASS_ENERGY_NEAR_LINEAR=true
NESTED_CANONICAL_PRIME_INCIDENCE_NEAR_LINEAR=true
PRIVATE_CANONICAL_PRIME_PAIR_REDUCTION_PROVED=true
SHARED_U_PRIVATE_CANONICAL_PRIME_ROOT_MODULUS_ENERGY_PROVED=false
SHARED_U_CANONICAL_PRIME_TAGGED_OPPOSITE_SIGN_QUADRATIC_ROOT_LINE_ENERGY_PROVED=false
SHARED_U_TRANSVERSE_VERTICAL_KUMMER_DISPERSION_PROVED=false
SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED=false
SHARED_U_MIXED_BRANCH_DISPERSION_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
TH18_NEEDED=true
TH18_REQUESTED_OBJECT=PrivateCanonicalPrimeOppositeSignRootModulusLargeSieve
T_ROUTE_BLOCKED_WAITING_FOR_TH18=false
NEXT=Stage14-t68
```
