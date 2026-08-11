# Stage14-tH26 literature and theorem-applicability audit

Frozen target: `stages/stage14/14-t90/th26-target.md` at merged Stage14-t90 snapshot `129a6a0625e46fb979e1ea757f2366d5e63c3b95`.

The applicability standard is strict: a theorem is marked applicable only if its hypotheses can be matched to the full frozen coefficient system and all physical masks with at most `B^o(1)` loss.  Logarithmic density gains do not count as a positive `B`-power exponent.

## 1. Selberg--Delange / split-prime support

Relevant modern reference:

- R. de la Bretèche and G. Tenenbaum, *Remarks on the Selberg--Delange method*, arXiv:2010.12929.

For a multiplicative indicator supported on a prime set of Dirichlet density `1/2`, Selberg--Delange technology produces logarithmic-scale density loss.  This is the correct qualitative model for integers all of whose odd prime factors are `1 mod 4`.

Applicability to tH26:

```text
SPLIT_PRIME_SUPPORT_AS_MULTIPLICATIVE_MAJORANT=true
SPLIT_PRIME_SUPPORT_FIXED_POWER_SAVING=false
PRINCIPAL_PHYSICAL_COEFFICIENT_EQUAL_TO_MULTIPLICATIVE_MAJORANT=false
```

The principal physical coefficient is smaller than the ambient split-prime representation majorant but is not proved to have an additional fixed-power density deficit.

## 2. Friedlander--Iwaniec--Mazur--Rubin spin technology

Reference:

- J. B. Friedlander, H. Iwaniec, B. Mazur, K. Rubin, *The spin of prime ideals*, arXiv:1110.6331.

This work develops bilinear cancellation for a specific non-Euler-product spin invariant on prime ideals.  It demonstrates that special Gaussian/number-field orientation symbols can admit power-saving bilinear treatment even when ordinary L-function methods do not directly apply.

Mismatch with tH26:

```text
c_U(gamma) identified as their spin=false
finite spin decomposition proved=false
required reciprocity/bilinear factorization proved=false
full four-cell/tag/projective masks packaged in Type-I/II form=false
```

Verdict:

```text
GAUSSIAN_SPIN_THEOREM_DIRECTLY_APPLICABLE=false
```

The reference is a candidate model for a future internal decomposition, not an adapter already available for the frozen coefficient.

## 3. Gaussian/number-field Bombieri--Vinogradov in short intervals and sectors

Reference:

- T. Khale, C. O'Kuhn, A. Panidapu, A. Sun, S. Zhang, *A Bombieri--Vinogradov Theorem for primes in short intervals and small sectors*, arXiv:2008.09677.

The theorem counts prime ideals with Hecke-character sector restrictions and establishes Bombieri--Vinogradov-type distribution in arithmetic progressions.

Mismatch with tH26:

```text
prime variable independent of cofactor in theorem=true
canonical LPF coupling ell=LPF(ell*delta0) in target=true
arbitrary physical cofactor coefficient accepted=false
principal positive cofactor representation term removed=false
full reconstructed physical masks included=false
```

Even a strong prime-side distribution theorem does not estimate

```text
sum_delta0 Sum_U,chi(delta0) * prime_error(X/delta0)
```

with a fixed power when `Sum_U,chi` has only a `B^o(1)` pointwise envelope and no theorem-compatible structure.

Verdict:

```text
GAUSSIAN_BV_BDH_DIRECTLY_APPLICABLE=false
```

## 4. Quadratic/Hecke large sieve over number fields

Reference:

- L. Goldmakher and B. Louvel, *A quadratic large sieve inequality over number fields*, arXiv:1112.1642.

This gives a genuine large-sieve framework for structured Hecke-character families over number fields.

Mismatch with tH26:

```text
endpoint projective character family size=B^o(1)
polynomial character-family length available=false
cofactor coefficient a Hecke character=false
cofactor coefficient quadratic Hecke family=false
```

There is no polynomial dual family whose orthogonality can be charged for a fixed-power gain.  Applying Cauchy plus a large sieve to a subpolynomial family does not by itself beat the frozen trivial packet scale by `B^{-delta}`.

Verdict:

```text
HECKE_LARGE_SIEVE_DIRECTLY_APPLICABLE=false
```

## 5. Bombieri--Vinogradov with Gaussian-prime-shaped moduli

Reference:

- K. Halupczok, *A Bombieri--Vinogradov Theorem with products of Gaussian primes as moduli*, arXiv:1607.07265.

This exploits special polynomial structure in a family of moduli.  The tH26 endpoint conductor is instead already fixed at `d=B^o(1)`, while the difficult moving object is the canonical-LPF/cofactor representation coefficient.  The theorem's source of averaging is therefore absent.

```text
HALUPCZOK_GAUSSIAN_MODULUS_BV_DIRECTLY_APPLICABLE=false
```

## 6. General prime-ideal Bombieri--Vinogradov / automorphic coefficients

Reference:

- Y. Jiang, G. Lü, J. Thorner, Z. Wang, *A Bombieri-Vinogradov theorem for higher rank groups*, arXiv:2104.02711.

This is powerful prime-ideal distribution technology for structured automorphic/Hecke coefficient sequences.  It does not permit an arbitrary physical Gaussian representation coefficient depending on the short cofactor, nor does it remove the principal term.

```text
GENERAL_PRIME_IDEAL_BV_DIRECTLY_APPLICABLE=false
```

## 7. Largest-prime / Buchstab decomposition

The identity

```text
Q=ell*delta0,
ell=LPF(Q),
v_ell(Q)=1
```

can be handled by a standard Buchstab/largest-prime decomposition.  This is bookkeeping, not cancellation.  The target permits polynomial cofactor length: at fixed-power scale, for instance,

```text
ell=B^(11/20),
delta0=B^(7/20),
Q=B^(9/10)
```

is compatible with the three principal size inequalities when `h*k0=B^o(1)`.

Thus no theorem may replace `delta0` by `B^o(1)` uniformly.

```text
CANONICAL_LPF_BUCHSTAB_DECOMPOSITION_FORMALLY_AVAILABLE=true
CANONICAL_LPF_SHORT_COFACTOR_UNIFORMITY_CONTROLLED=false
```

## 8. Principal versus nonprincipal character ledger

### Principal endpoint character

The contribution is positive.  Oscillatory theorems aimed only at `chi != 1` cannot delete it.  The ambient split-prime support has logarithmic, not fixed-power, sparsity.

```text
PRINCIPAL_REPRESENTATION_TERM_POWER_SPARSE=false
```

This is consistent with the separately merged sH50 lesson that a power-saving oscillatory remainder does not imply a whole-count saving while an unsaved principal density remains.  tH26 is nevertheless an independent frozen t90 certificate and does not import the sH50 mathematical receiver.

### Nonprincipal endpoint characters

Pure finite-conductor Hecke prime sums have cancellation technology.  The frozen target needs the stronger statement after multiplication by the nonmultiplicative cofactor representation weight and canonical-LPF coupling.  No audited theorem supplies that full adapter.

```text
PURE_NONPRINCIPAL_HEECKE_PRIME_SUM_CANCELLATION_KNOWN=true
NONPRINCIPAL_GAUSSIAN_CHARACTER_SAVING_AVAILABLE=false
```

## 9. Theorem matrix

```text
SELBERG_DELANGE_SPLIT_SUPPORT_RELEVANT=true
SELBERG_DELANGE_FIXED_POWER_GAIN=false
GAUSSIAN_SPIN_THEOREM_DIRECTLY_APPLICABLE=false
GAUSSIAN_BV_BDH_DIRECTLY_APPLICABLE=false
HECKE_LARGE_SIEVE_DIRECTLY_APPLICABLE=false
HALUPCZOK_GAUSSIAN_MODULUS_BV_DIRECTLY_APPLICABLE=false
GENERAL_PRIME_IDEAL_BV_DIRECTLY_APPLICABLE=false
CANONICAL_LPF_BUCHSTAB_DECOMPOSITION_FORMALLY_AVAILABLE=true
FULL_PHYSICAL_COEFFICIENT_DECOMPOSITION_THEOREM_READY=false
OFF_THE_SHELF_UNIFORM_FIXED_POWER_SAVING_PROVED=false
```

## 10. Exact missing theorem adapter

A positive theorem audit would require at least one of the following.

1. A proof that the principal physical representation coefficient occupies only `B^{-delta}` of the ambient split-prime semigroup on every physical dyadic range.
2. An exact `B^o(1)`-piece decomposition of the centered `c_U(gamma)` into multiplicative/Hecke/spin/trace/Type-I--II pieces with the primitive/four-cell/tag/projective masks retained.
3. A new bilinear theorem directly accepting the coupled largest-prime factorization and those physical Gaussian coefficients.

No such adapter was located or proved in the frozen t90 snapshot.
