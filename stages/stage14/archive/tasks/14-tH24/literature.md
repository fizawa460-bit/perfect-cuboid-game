# Stage14-tH24 literature applicability note

Frozen object:

```text
FixedUPrimitiveBinaryNormSuperSqrtLargestPrimeShortCofactorVerticalDivisorSieve
```

Source snapshot: merged Stage14-t84 at `fa93c79084e05a2f1aa39eeb80b48f2e82f82113`.

This note is applicability-only. No source below is imported as a proof of the Stage14 receiver.

## 1. Half-dimensional sieve for quadratic forms

A directly relevant modern primary reference is:

- Elena Fuchs, Catherine Hsu, James Rickards, Damaris Schindler, Katherine E. Stange, *Primes represented by shifted quadratic forms: on primitivity and congruence classes*, arXiv:2504.20289.

The paper explicitly extends Iwaniec's half-dimensional sieve to primitive representations and congruence restrictions, and obtains prime-representation bounds of logarithmic density scale. This confirms that primitivity plus an arithmetic progression is compatible with half-dimensional sieve technology.

It does not directly match t84. The t84 vertical condition is on one coordinate

```text
D=d*j,
```

while the sieved object is the value

```text
N=T^2+D^2=ell*n
```

with a prescribed unique super-square-root largest prime, a moving short cofactor, and post-factorization physical masks. The theorem does not supply a fixed `B`-power saving for this weighted LPF/cofactor receiver.

Verdict:

```text
HALF_DIMENSIONAL_SIEVE_FORMALLY_RELEVANT=true
HALF_DIMENSIONAL_SIEVE_APPLICABLE=false
```

## 2. Prime values of binary quadratic forms with a thin variable

Peter Cho-Ho Lam, Damaris Schindler, Stanley Yao Xiao, *On prime values of binary quadratic forms with a thin variable*, arXiv:1809.10755, proves prime values for arbitrary primitive positive definite binary quadratic forms with one input restricted to a thin set, generalizing the Fouvry--Iwaniec `x^2+y^2` framework.

This is strong evidence that substantial thin-variable restrictions can coexist with primality of a binary quadratic form. But it treats the special case in which the whole form value is prime. The t84 set includes every

```text
N=ell*n,
1<=n<sqrt(B/h),
n=k*delta,
```

and needs an upper bound for the entire short-cofactor family. A theorem counting the `n=1` subset cannot upper-bound this larger set.

Verdict:

```text
BINARY_QUADRATIC_PRIME_VALUE_THEOREM_DIRECT_ADAPTER=false
```

## 3. Primitive binary quadratic form prime counts

Asif Zaman, *Primes represented by positive definite binary quadratic forms*, arXiv:1710.08914, gives upper bounds for primes represented by a fixed positive definite binary quadratic form and related almost-prime information.

Again, the prime-value variable is the form value itself. The t84 target is not a prime-value problem: its largest prime factor is prime while the form value has a variable split-prime cofactor. The fixed vertical coordinate divisor and reconstructed cover masks are absent from the theorem statement.

Verdict:

```text
BINARY_QUADRATIC_LARGE_PRIME_FACTOR_THEOREM_APPLICABLE=false
```

## 4. Friedlander--Iwaniec asymptotic sieve

John Friedlander and Henryk Iwaniec, *Asymptotic sieve for primes*, arXiv:math/9811186, develops an asymptotic sieve capable of breaking the parity barrier when a sequence satisfies an additional bilinear axiom. Its companion application, *The polynomial X^2+Y^4 captures its primes*, arXiv:math/9811185, verifies the needed structure for a specific thin polynomial sequence.

This is relevant as a methodological warning: parity-breaking prime detection is not supplied merely by a beta-sieve; it requires a sequence-specific bilinear input.

For t84, the required bilinear axiom would have to be verified for the Gaussian factorization

```text
T+iD=pi*W,
Im(pi*W)=d*j,
N(pi)=LPF(T^2+D^2),
N(W)=k*delta,
```

with all reconstructed-cover masks. That verification is exactly part of the remaining obstruction, not an off-the-shelf theorem.

Verdict:

```text
ASYMPTOTIC_SIEVE_DIRECT_ADAPTER=false
```

## 5. Gaussian primes in sectors

Bingrong Huang, Jianya Liu, Zeév Rudnick, *Gaussian primes in almost all narrow sectors*, arXiv:1903.04005, proves expected Gaussian-prime counts for almost all sufficiently narrow sectors.

The t84 problem is not a free sector count. The prime factor `pi` is coupled multiplicatively to `W`, its imaginary product coordinate is restricted by `d|D`, and `ell=N(pi)` also participates in the short-cofactor and physical hyperbola filters.

Verdict:

```text
GAUSSIAN_SECTOR_PRIME_THEOREM_APPLICABLE=false
```

## 6. Gaussian / number-field Bombieri--Vinogradov

Tanmay Khale, Cooper O'Kuhn, Apoorva Panidapu, Alec Sun, Shengtong Zhang, *A Bombieri-Vinogradov Theorem for primes in short intervals and small sectors*, arXiv:2008.09677, proves prime-norm distribution in short intervals, small sectors, and arithmetic progressions for Galois number fields. In the imaginary quadratic setting it is a genuine localized Gaussian-prime distribution theorem.

The theorem averages a prime ideal / rational prime variable in progressions. In the t84 receiver:

```text
ell=LPF(T^2+D^2)
```

is dependent on the lattice point, while the vertical condition after factorization is

```text
Im(pi*W)=d*j.
```

There is no free prime progression independent of the cofactor. The reconstructed balanced-cover, short ellipse, and `ell*delta` / sharp `ell*HRT` masks also remain coupled.

Verdict:

```text
GAUSSIAN_BV_BDH_APPLICABLE=false
```

## 7. Harman sieve and large moduli

Runbo Li, *Primes in arithmetic progressions to large moduli and refinements of Harman's sieve*, arXiv:2602.20917, develops Harman-sieve majorants/minorants with Bombieri--Vinogradov type mean values for structured large moduli.

This concerns distribution of the prime indicator in arithmetic progressions and exploits modulus averaging. The t84 frozen packet has only `B^o(1)` vertical divisor hosts for fixed `U`; its difficulty is not a missing average over many rational moduli. More importantly, the prime is the LPF of a binary norm and is multiplicatively coupled to the cofactor through a coordinate constraint.

Verdict:

```text
HARMAN_BUCHSTAB_APPLICABLE=false
```

## 8. Why Buchstab alone is not enough

The uniqueness condition

```text
ell^2>2N
```

makes a Buchstab split especially clean: once the large prime is chosen, the remaining cofactor is `n<ell/2`. But after the split the core sum is a Gaussian bilinear convolution with a vertical product-coordinate restriction. Standard Buchstab identities are exact combinatorial decompositions; they do not themselves yield cancellation.

A successful theorem adapter would need a Type-I/II or dispersion estimate that simultaneously sees:

```text
primitive (T,D),
D=d*j,
d|R*S,
N(pi)=ell,
N(W)=k*delta,
Im(pi*W)=D,
ell*delta<=Y_U,
reconstructed balanced cover and sharp hyperbolas.
```

No audited source supplies this full package.

## 9. Strict literature conclusion

The closest positive facts are:

1. half-dimensional sieve can handle primitive quadratic-form representations and congruence restrictions;
2. binary quadratic forms can take prime values even with a thin variable;
3. Gaussian primes have strong sector and Bombieri--Vinogradov distribution;
4. Harman/asymptotic sieve can break parity when a sequence-specific bilinear estimate is available.

The missing bridge is exactly the sequence-specific vertical Gaussian product dispersion with the short cofactor and reconstructed physical masks.

```text
OFF_THE_SHELF_FIXED_POWER_SAVING_PROVED=false
CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=0
MINIMAL_REMAINING_OBSTRUCTION=FixedUVerticalDivisorPrimitiveBinaryNormShortCofactorBuchstabDispersionWithReconstructedCoverMasks
```