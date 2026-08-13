# Stage14-t66 — primewise Cayley allocation and opposite-sign quadratic root lines

## Purpose

Merged Stage14-t65 R2 proves, for the dominant fixed-`U` invisible branch, that the exact cross-ratio

\[
s=\kappa(u/v)^2,
\qquad (u,v)=1,
\]

recovers the canonical prime from the reduced Cayley denominator and that a fixed `(U,s)` fiber has `O(1)` physical lifts.  The remaining principal problem is the square-scale incidence carried by

\[
C(s)=\frac{v^2+\kappa u^2}{v^2-\kappa u^2},
\]

with the physical radial divisors on opposite signs.

Stage14-t66 uses the prime allocation completely.  It proves that every odd physical radial prime is automatically coprime to the squareclass parameter, so the two-sided divisor system becomes an exact family of opposite-sign quadratic root lines:

\[
(v/u)^2\equiv-\kappa\pmod{\delta_{\rm odd}},
\qquad
(v/u)^2\equiv+\kappa\pmod{\ell h_{\rm odd}}.
\]

The CRT root multiplicity is only `B^{o(1)}` and therefore is not the remaining source of the `7/8` barrier.  What remains is the distribution of the *physical primitive lifts* on these moving root lines, with `ell` distinguished as the unique largest odd prime on the negative side.

This stage does not prove that distribution theorem and does not claim a new whole-family power saving.

---

## 1. Imported fixed-U data

Fix a legal dominant invisible packet and write

\[
N(U)=m,
\qquad N(V)=n=k\delta,
\qquad hk=\varepsilon m.
\tag{66.1}
\]

Merged t37/t65 give

\[
(\delta,h)=1,
\qquad \ell\nmid k\delta,
\qquad \ell>2\varepsilon m\delta,
\tag{66.2}
\]

and merged t65 R2 gives

\[
\ell=\operatorname{LPF}_{\rm odd}\!\left(
\operatorname{den} C(s)
\right)
\tag{66.3}
\]

with the remaining odd denominator cofactor strictly below `ell/2`.

Write

\[
G=\gcd(v^2+\kappa u^2,v^2-\kappa u^2),
\tag{66.4}
\]

and

\[
P_+=\frac{v^2+\kappa u^2}{G},
\qquad
P_-=\frac{v^2-\kappa u^2}{G}.
\tag{66.5}
\]

Then `(P_+,P_-)=1` and t65 proves

\[
\operatorname{odd}(\delta)\mid P_+,
\qquad
\ell\,\operatorname{odd}(h)\mid P_-.
\tag{66.6}
\]

---

## 2. Exact gcd defect

Let

\[
d=\gcd(\kappa,v).
\tag{66.7}
\]

Because `kappa` is squarefree and `(u,v)=1`, an odd prime `r` divides `G` iff `r|kappa` and `r|v`.  In that case its valuation in both raw factors is exactly one.  Hence

\[
\boxed{\operatorname{odd}(G)=\operatorname{odd}(d).}
\tag{66.8}
\]

The 2-adic part contributes at most one additional factor of two, so

\[
\boxed{G\in\{d,2d\}.}
\tag{66.9}
\]

whenever the displayed member is integral.  This sharpens the t65 statement `G|2kappa`.

Equivalently, if

\[
\kappa=d\kappa_0,
\qquad v=dv_0,
\qquad \eta=G/d\in\{1,2\},
\]

then

\[
\boxed{
P_+=\frac{d v_0^2+\kappa_0u^2}{\eta},
\qquad
P_-=\frac{d v_0^2-\kappa_0u^2}{\eta}.
}
\tag{66.10}
\]

No moving gcd remains between the two reduced factors.

```text
CAYLEY_GCD_ODD_PART_EQUALS_GCD_KAPPA_V=true
CAYLEY_GCD_DEFECT_IS_D_OR_2D=true
```

---

## 3. Odd physical radial moduli are coprime to kappa

The divisor locks (66.6) force a stronger fact.

Suppose an odd prime `r` divides both `delta` and `kappa`.

- If `r` does not divide `v`, then `v^2+kappa*u^2` is nonzero modulo `r`, so `r` cannot divide `P_+`.
- If `r|v`, then `r` occurs exactly once in the raw plus factor and exactly once in `G`, so it again does not divide `P_+`.

Both cases contradict `odd(delta)|P_+`.  Therefore

\[
\boxed{(\operatorname{odd}(\delta),\kappa)=1.}
\tag{66.11}
\]

The same argument on `P_-` gives

\[
\boxed{(\operatorname{odd}(h),\kappa)=1.}
\tag{66.12}
\]

For the canonical prime, t65 gives `ell>2m,2n`.  Since

\[
a^2+b^2=\ell m,
\]

we have `ell` not dividing `a` or `b`; modulo `ell`,

\[
a^2\equiv-b^2.
\]

For the t55 factors

\[
A=b^2p^2-a^2q^2,
\qquad B=b^2q^2-a^2p^2,
\]

this yields

\[
A\equiv B\equiv b^2(p^2+q^2)=b^2n\not\equiv0\pmod\ell.
\]

Thus `ell` does not divide the physical squareclass:

\[
\boxed{\ell\nmid\kappa.}
\tag{66.13}
\]

Combining (66.11)--(66.13),

\[
\boxed{
\gcd(\operatorname{odd}(\delta)\,\ell\,\operatorname{odd}(h),\kappa)=1.
}
\tag{66.14}
\]

```text
ODD_PHYSICAL_RADIAL_MODULUS_COPRIME_TO_KAPPA=true
CANONICAL_ELL_COPRIME_TO_KAPPA=true
```

---

## 4. Exact opposite-sign quadratic root lines

Put

\[
Q_+=\operatorname{odd}(\delta),
\qquad
Q_-=\ell\,\operatorname{odd}(h).
\tag{66.15}
\]

From `(delta,h)=1` and invisibility,

\[
\boxed{(Q_+,Q_-)=1.}
\tag{66.16}
\]

Equation (66.14), primitivity `(u,v)=1`, and (66.6) imply

\[
(u,Q_+Q_-)=1.
\tag{66.17}
\]

Therefore `z=v/u` is a legal unit residue modulo both physical moduli, and the divisor system is exactly

\[
\boxed{z^2\equiv-\kappa\pmod{Q_+},}
\tag{66.18}
\]

\[
\boxed{z^2\equiv+\kappa\pmod{Q_-}.}
\tag{66.19}
\]

For each odd prime power `r^e` dividing either modulus, the right-hand side is a unit.  A solvable quadratic congruence has exactly two roots modulo `r^e`.  Hence CRT gives exactly

\[
\boxed{2^{\omega(Q_+Q_-)}}
\tag{66.20}
\]

root lines for the fixed tuple `(kappa,Q_+,Q_-)`, and

\[
2^{\omega(Q_+Q_-)}\le\tau(Q_+Q_-)=B^{o(1)}.
\tag{66.21}
\]

Thus prime allocation and CRT reconstruction themselves have zero fixed-power cost.

```text
OPPOSITE_SIGN_QUADRATIC_ROOT_CONGRUENCES_PROVED=true
CRT_ROOT_LINE_MULTIPLICITY=Bo1
CRT_ROOT_LINE_FIXED_POWER_LOSS=false
```

---

## 5. All odd radial primes lie in one splitting set

Primitive Gaussian norms have no odd prime factor `3 mod 4`.  Therefore every odd prime dividing `delta`, `h`, or the canonical norm prime `ell` satisfies

\[
r\equiv1\pmod4.
\tag{66.22}
\]

For `r|Q_+`, (66.18) gives

\[
\left(\frac{-\kappa}{r}\right)=1.
\]

Since `r=1 mod 4`, this is equivalent to

\[
\left(\frac{\kappa}{r}\right)=1.
\]

For `r|Q_-`, the same conclusion follows directly from (66.19).  Hence

\[
\boxed{
\left(\frac{\kappa}{r}\right)=1
\quad\text{for every odd }r\mid Q_+Q_-.
}
\tag{66.23}
\]

Choose locally `tau_r^2=kappa` and `i_r^2=-1`.  Then the negative-side roots are

\[
z\equiv\pm\tau_r,
\]

while the positive-side roots are

\[
z\equiv\pm i_r\tau_r.
\]

Thus `Q_+` versus `Q_-` is not distinguished by a quadratic splitting character.  It is a finer **root orientation** differing by multiplication by a local square root of `-1`.

Equivalently every physical odd radial prime satisfies

\[
\boxed{z^4\equiv\kappa^2\pmod r.}
\tag{66.24}
\]

The side label tells which of the two quadratic factors vanishes.

```text
ALL_ODD_RADIAL_PRIMES_ARE_1_MOD_4=true
PLUS_AND_MINUS_HAVE_SAME_LEGENDRE_SPLITTING_CONDITION=true
PLUS_MINUS_DIFFER_BY_LOCAL_I_ROOT_ORIENTATION=true
```

---

## 6. Canonical largest-prime tag survives the root-line reduction

Merged t65 R2 gives

\[
\ell=\operatorname{LPF}_{\rm odd}(P_-),
\tag{66.25}
\]

and

\[
\frac{\operatorname{odd}(P_-)}{\ell}<\frac\ell2.
\tag{66.26}
\]

In particular `ell` occurs to exponent one in `P_-`; otherwise the cofactor would be at least `ell`.

Thus the negative root modulus has one distinguished prime component:

```text
ell : unique largest odd prime, exponent one,
all remaining negative cofactor < ell/2.
```

The sharp radial budget remains

\[
\ell\delta\le Y_U:=\frac{2B}{\varepsilon m}.
\tag{66.27}
\]

No enlargement to an arbitrary CRT modulus is permitted: the canonical largest-prime tag and the sharp `ell*delta` hyperbola remain part of the receiver.

```text
CANONICAL_ELL_ROOT_COMPONENT_EXPONENT_ONE=true
CANONICAL_LARGEST_PRIME_TAG_RETAINED=true
SHARP_ELL_DELTA_HYPERBOLA_RETAINED=true
```

---

## 7. Why ordinary quadratic-character large sieve is too coarse

At t65, deduplicating by squareclass before a quadratic large sieve was already circular.  Stage t66 gives a second, independent obstruction to a naive character-only treatment.

By (66.23), both physical sides satisfy the same Legendre condition

\[
(\kappa/r)=1.
\]

The information that a prime belongs to `Q_+` rather than `Q_-` is carried by the actual root orientation

\[
z^2=-\kappa
\quad\text{versus}\quad
z^2=+\kappa,
\]

not by the quadratic character of `kappa`.

Therefore replacing the root packet by Legendre-symbol support discards the exact side allocation that t65/t66 worked to preserve.  Such a replacement cannot by itself prove the physical incidence bound.

```text
LEGENDRE_SPLITTING_ALONE_DISTINGUISHES_RADIAL_SIDE=false
QUADRATIC_CHARACTER_ONLY_COLLAPSE_ALLOWED=false
```

---

## 8. The remaining theorem is a root-line distribution theorem

For fixed `U`, exact `s` fibers are already `O(1)` by t65.  After t66, every state in a fixed squareclass `kappa` is represented, at `B^{o(1)}` CRT cost, by a primitive rational point `(u,v)` on one of the opposite-sign root lines (66.18)--(66.19), subject to:

- canonical prime `ell=LPF_odd(P_-)`;
- the negative cofactor `<ell/2`;
- `ell*delta<=Y_U`;
- fixed divisor-fan `h,k`;
- primitive Gaussian `V`;
- canonical-prime, chamber and reconstruction masks.

Define the live receiver

```text
SharedUCanonicalPrimeTaggedOppositeSignQuadraticRootLineEnergy.
```

Its target is the same near-linear fixed-`U` squareclass energy required by tH15/t63, but the unresolved arithmetic is now localized to the distribution of physical primitive lifts among moving CRT root lines.  There is no remaining prime-allocation multiplicity or uncontrolled gcd adapter.

```text
SHARED_U_CANONICAL_PRIME_TAGGED_OPPOSITE_SIGN_QUADRATIC_ROOT_LINE_ENERGY_PROVED=false
SHARED_U_CANONICAL_PRIME_TAGGED_CAYLEY_SQUARE_SCALE_INCIDENCE_PROVED=false
SHARED_U_TRANSVERSE_JACOBI_SQUARE_LIFT_INCIDENCE_PROVED=false
SHARED_U_TRANSVERSE_VERTICAL_KUMMER_DISPERSION_PROVED=false
```

---

## 9. tH decision

At t66 a genuinely new theorem family is finally isolated, so **tH18 is needed**.

The requested independent object is

```text
CanonicalPrimeTaggedOppositeSignQuadraticRootLargeSieve
```

for the exact coefficient space above.  tH18 should test, without changing the physical quantifier order, whether any of the following can control the moving root-line lifts with zero fixed-power loss:

1. large sieve for roots of quadratic congruences / quadratic polynomials;
2. dispersion for simultaneous binary quadratic norm forms;
3. real-quadratic norm/Pell ideal factorization averaged over the distinguished prime `ell`;
4. Gaussian or biquadratic root-orientation large sieve retaining the local `i_r` side label;
5. largest-prime-factor sieve compatible with `ell=LPF_odd(P_-)` and `ell*delta<=Y_U`.

It must **not** replace the root orientations by the common Legendre condition `(kappa/r)=1`, and it must not pre-collapse states to squareclass coefficient energy.

The t route does not block waiting for tH18; t67 can continue internal arithmetic in parallel.

```text
TH18_NEEDED=true
TH18_REQUESTED_OBJECT=CanonicalPrimeTaggedOppositeSignQuadraticRootLargeSieve
T_ROUTE_BLOCKED_WAITING_FOR_TH18=false
```

---

## Locked boundary

```text
STAGE14_T66=COMPLETE_PRIMEWISE_CAYLEY_ALLOCATION_AND_OPPOSITE_SIGN_ROOT_LINE_REDUCTION
MERGED_T65_R2_IMPORTED=true
CAYLEY_GCD_ODD_PART_EQUALS_GCD_KAPPA_V=true
CAYLEY_GCD_DEFECT_IS_D_OR_2D=true
ODD_PHYSICAL_RADIAL_MODULUS_COPRIME_TO_KAPPA=true
CANONICAL_ELL_COPRIME_TO_KAPPA=true
OPPOSITE_SIGN_QUADRATIC_ROOT_CONGRUENCES_PROVED=true
CRT_ROOT_LINE_MULTIPLICITY=Bo1
CRT_ROOT_LINE_FIXED_POWER_LOSS=false
ALL_ODD_RADIAL_PRIMES_ARE_1_MOD_4=true
PLUS_AND_MINUS_HAVE_SAME_LEGENDRE_SPLITTING_CONDITION=true
PLUS_MINUS_DIFFER_BY_LOCAL_I_ROOT_ORIENTATION=true
CANONICAL_ELL_ROOT_COMPONENT_EXPONENT_ONE=true
CANONICAL_LARGEST_PRIME_TAG_RETAINED=true
SHARP_ELL_DELTA_HYPERBOLA_RETAINED=true
LEGENDRE_SPLITTING_ALONE_DISTINGUISHES_RADIAL_SIDE=false
QUADRATIC_CHARACTER_ONLY_COLLAPSE_ALLOWED=false
SHARED_U_CANONICAL_PRIME_TAGGED_OPPOSITE_SIGN_QUADRATIC_ROOT_LINE_ENERGY_PROVED=false
SHARED_U_CANONICAL_PRIME_TAGGED_CAYLEY_SQUARE_SCALE_INCIDENCE_PROVED=false
SHARED_U_TRANSVERSE_JACOBI_SQUARE_LIFT_INCIDENCE_PROVED=false
SHARED_U_TRANSVERSE_VERTICAL_KUMMER_DISPERSION_PROVED=false
SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED=false
SHARED_U_MIXED_BRANCH_DISPERSION_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
TH18_NEEDED=true
TH18_REQUESTED_OBJECT=CanonicalPrimeTaggedOppositeSignQuadraticRootLargeSieve
T_ROUTE_BLOCKED_WAITING_FOR_TH18=false
NEXT=Stage14-t67
```