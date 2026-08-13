# Stage14-tH25 literature applicability note

Frozen target:

```text
FixedUFixedDiscriminantMinus4dSquaredFixedCofactorPrimeValueFormPhysicalSieve
```

Source snapshot:

```text
Stage14-t86
798191aa5071a344cf642a1be265f1ad8e373fd5
```

This note audits theorem applicability only. A cited theorem is not imported as a Stage14 proof unless an explicit variable/range adapter is established below.

## 1. Arithmetic object after t86

For fixed packet data and one fixed selector divisor `d`, t86 gives the primitive form

```text
F_{d,delta0,rho}(s,j)
 = delta0*s^2
   + 2*rho*d*s*j
   + ((rho^2+1)/delta0)*d^2*j^2,
```

with

```text
Disc(F)=-4*d^2,
F(s,j)=k0*ell,
ell prime,
rho^2=-1 mod delta0.
```

The order is

```text
O_d=Z+d*i*Z.
```

The associated invertible proper ideal can be written, up to sign convention,

```text
(delta0,d*(i-rho)).
```

Thus `(delta0,rho)` is a ring-class parameter. For odd squarefree `d>1`,

```text
h(-4*d^2)
 = (d/2) product_{p|d}(1-chi_4(p)/p)
 = d*B^o(1).
```

The unrestricted t86 form shape can represent the full proper class group. The physical Stage14 `delta0` range may be smaller, but no power-small class-family theorem is presently available.

This class-family issue is the central filter applied to every candidate theorem below.

---

## 2. Asif Zaman — primes represented by positive definite binary quadratic forms

Reference:

```text
Asif Zaman,
Primes represented by positive definite binary quadratic forms,
arXiv:1710.08914; Q. J. Math. 69 (2018), 1353-1386.
```

This is the closest direct single-form theorem.

For a primitive reduced positive-definite form of discriminant `-D`, Zaman proves an upper bound of the expected class-density shape

```text
pi_f(x) << x/(h(-D)*log x)
```

in explicit growing-discriminant ranges. Unconditionally, his general form-independent corollary applies for

```text
x >= D^(2+epsilon).
```

The sharper theorem uses the reduced leading coefficient `a` and, unconditionally, requires a range governed by

```text
(D^2/a)^(1+epsilon).
```

For t86,

```text
D=4*d^2,
x~ell.
```

So the generic unconditional condition is roughly

```text
ell >= d^(4+epsilon),
```

and even the favorable reduced-coefficient scale is not forced by the t86 inequalities.

The deterministic tH25 range witness explicitly satisfies all exponent-level target inequalities while having

```text
ell << d^3.
```

Therefore Zaman's theorem is not uniform over the frozen Stage14 range.

There is a second, independent obstruction. The theorem is a **single form class** bound. Its gain relative to the total split-prime scale is the class density

```text
1/h(-4*d^2)=d^-1*B^o(1).
```

The t86 family has not been proved to occupy power-fewer than `h(-4*d^2)` classes. Summing the single-class estimate over a full ring-class family can consume that gain exactly.

Verdict:

```text
ZAMAN_SINGLE_CLASS_THEOREM_RELEVANT=true
ZAMAN_TARGET_RANGE_UNIFORM=false
ZAMAN_CLASS_FAMILY_SUMMATION_SAVING_PROVED=false
GROWING_DISCRIMINANT_FORM_PRIME_THEOREM_APPLICABLE=false
```

---

## 3. Ditchen — Bombieri--Vinogradov / BDH for form classes

Reference:

```text
Jakob Ditchen,
On the average distribution of primes represented by binary quadratic forms,
arXiv:1312.1502.
```

Ditchen proves form-class analogues of Bombieri--Vinogradov and Barban--Davenport--Halberstam using a large sieve for complex ideal-class characters. In the stated theorems the averaging is over **negative fundamental discriminants** in long ranges. The representative theorem ranges include powers such as

```text
Q^(20/3+epsilon) <= X * log-loss
```

for the maximum-over-class Bombieri--Vinogradov statement, and

```text
Q^(3+epsilon) <= X * log-loss
```

for a mean-square statement over form classes.

Two mismatches are fatal for direct t86 use.

First, t86 has

```text
Disc=-4*d^2,
```

which is nonfundamental with a square conductor. Ditchen explicitly remarks that extending the argument to general nonfundamental discriminants becomes substantially more difficult because of the square factors and the functional-equation/class-character infrastructure.

Second, the theorem gains cancellation by averaging over discriminants / classes in a prescribed family. The Stage14 quantifier order is

```text
fixed U -> fixed selector d -> moving physical class labels.
```

There is no free fundamental-discriminant average to substitute for the theorem's `Q`-average.

Verdict:

```text
DITCHEN_CLASS_GROUP_LARGE_SIEVE_RELEVANT=true
DITCHEN_FUNDAMENTAL_DISCRIMINANT_HYPOTHESIS_MATCHES=false
DITCHEN_DISCRIMINANT_AVERAGE_AVAILABLE=false
RING_CLASS_LARGE_SIEVE_APPLICABLE=false
```

---

## 4. Thorner--Zaman — effective Chebotarev and prime form points

References:

```text
Jesse Thorner and Asif Zaman,
A Chebotarev variant of the Brun-Titchmarsh theorem and bounds for the Lang-Trotter conjectures,
arXiv:1606.09238.

Jesse Thorner and Asif Zaman,
A unified and improved Chebotarev density theorem,
arXiv:1803.02823; Algebra & Number Theory 13 (2019), 1039-1068.
```

These results provide strong unconditional prime-ideal bounds with conductor/discriminant uniformity. The latter paper also applies the Chebotarev machinery to lattice points `(u,v)` for which a primitive positive-definite binary quadratic form is prime, with additional roughness conditions on the coordinates.

This confirms that growing discriminants and some coordinate restrictions can coexist with strong prime theorems.

It does not solve the frozen t86 problem for three reasons:

1. a fixed Frobenius/form class is still the basic prime-density object;
2. the target does not prove that `(delta0,rho)` occupies a power-small family of ring classes;
3. the Stage14 reconstructed cover, vertical quotient, short ellipse and sharp hyperbola are not the rough-coordinate conditions in the Chebotarev application.

The fixed `k0` class translation does not help with item 2 because class multiplication is a bijection.

Verdict:

```text
CHEBOTAREV_SINGLE_CLASS_TECHNOLOGY_RELEVANT=true
CHEBOTAREV_PHYSICAL_CLASS_FAMILY_COMPRESSION_PROVED=false
RING_CLASS_PRIME_THEOREM_APPLICABLE=false
```

---

## 5. Gaussian-prime Bombieri--Vinogradov in short intervals and sectors

Reference:

```text
Tanmay Khale, Cooper O'Kuhn, Apoorva Panidapu, Alec Sun, Shengtong Zhang,
A Bombieri-Vinogradov Theorem for primes in short intervals and small sectors,
arXiv:2008.09677; J. Number Theory (2021).
```

This theorem works over a fixed Galois number field, counts prime ideals in short intervals and Hecke-character sectors, and proves Bombieri--Vinogradov distribution in arithmetic progressions.

For `Q(i)` it is relevant to the t86 factorization

```text
T+iD=gamma*a*pi'.
```

However, the Stage14 sequence is not a free Gaussian-prime progression. For fixed `gamma,a` it retains

```text
d | Im(gamma*a*pi'),
N(gamma)=delta0,
ell*delta0 and d*delta0^2 hyperbolas,
canonical direction,
reconstructed balanced-cover masks.
```

Then `gamma` itself ranges over the same `(delta0,rho)` ring-class data. Summing over `gamma` without a new class-family compression merely rewrites the full ring-class family. The cited BV theorem does not provide that compression.

Verdict:

```text
GAUSSIAN_BV_BDH_RELEVANT=true
GAUSSIAN_BV_BDH_APPLICABLE=false
GAUSSIAN_SHORT_COFACTOR_PRIME_BILINEAR_APPLICABLE=false
```

---

## 6. Fuchs--Hsu--Rickards--Schindler--Stange — primitivity and congruence

Reference:

```text
Elena Fuchs, Catherine Hsu, James Rickards,
Damaris Schindler, Katherine E. Stange,
Primes represented by shifted quadratic forms: on primitivity and congruence classes,
arXiv:2504.20289; Acta Arithmetica 222 (2026), 371-391.
```

This work extends Iwaniec-style sieve arguments to prime representations with primitivity and arithmetic-progression restrictions. It is useful evidence that the t86 condition

```text
gcd(s,d*j)=1
```

and congruence restrictions are not, by themselves, fatal to a sieve.

The result is not a uniform upper-bound theorem for a polynomial family of nonfundamental discriminants `-4d^2`, and its prime-density scale is logarithmic rather than the fixed `B`-power saving required here.

Verdict:

```text
PRIMITIVITY_CONGRUENCE_SIEVE_RELEVANT=true
PRIMITIVITY_CONGRUENCE_SIEVE_FIXED_POWER_ADAPTER=false
```

---

## 7. Fixed `k0` ideal composition

This part does not require a new external theorem.

For the odd part of `k0`, all physical primes are split in `Q(i)` and are prime to `d`. A primitive proper `O_d`-ideal of norm `k0*ell` factors into

```text
A_k * P_ell,
N(A_k)=oddpart(k0),
N(P_ell)=ell.
```

The local split orientations of `A_k` cost at most `2^omega(k0)=B^o(1)`. The one possible 2-primary factor is already an `O(1)` t86 branch.

Thus composition with `A_k^-1` is a valid class-label adapter:

```text
FIXED_K_IDEAL_COMPOSITION_ADAPTER_PROVED=true
FIXED_K_IDEAL_COMPOSITION_LOSS=Bo1.
```

But this is a translation on the class group, not a collapse:

```text
FIXED_K_COMPOSITION_REDUCES_CLASS_FAMILY=false.
```

It also does not preserve the literal t86 `(s,j)` box under a standard reduced-form coordinate map. Therefore it helps identify the prime class but does not complete a physical theorem adapter.

---

## 8. Class-family conclusion

The crucial distinction is

```text
one fixed t86 form class
```

versus

```text
all physically allowed (delta0,rho) classes at one conductor d.
```

For the order of conductor `d` in `Q(i)`,

```text
h(-4*d^2)=d*B^o(1).
```

The unrestricted t86 shape spans the full proper class group. The target's physical inequalities do not currently prove

```text
# physical ring classes <= d*B^(-fixed positive power)
```

or even

```text
# physical ring classes = B^o(1).
```

Therefore the expected `1/h` gain of a prime theorem cannot be charged before an internal class-family compression is established.

This is stronger and more specific than the tH24 obstruction. The remaining problem is no longer the moving cofactor or moving discriminant; it is the physical distribution of the root-lift class labels inside one growing ring class group.

---

## 9. Final applicability matrix

```text
RING_CLASS_PRIME_THEOREM_APPLICABLE=false
GROWING_DISCRIMINANT_FORM_PRIME_THEOREM_APPLICABLE=false
RING_CLASS_LARGE_SIEVE_APPLICABLE=false
GAUSSIAN_SHORT_COFACTOR_PRIME_BILINEAR_APPLICABLE=false
FIXED_K_IDEAL_COMPOSITION_ADAPTER_PROVED=true
FORM_CLASS_FAMILY_POWER_COST_CONTROLLED=false
OFF_THE_SHELF_FIXED_POWER_SAVING_PROVED=false
CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=0
```

Minimal remaining obstruction:

```text
FixedUPhysicalDeltaRootRingClassFamilyCompressionWithReconstructedCoverMasks
```

Preferred receiver:

```text
SharedUFixedSelectorRingClassCompressedFixedCofactorPrimeValuePhysicalEnergy
```

No further external theorem audit is minimal until the parent route determines whether the physical `(delta0,rho)` labels are power-compressed inside `Cl(-4d^2)`.
