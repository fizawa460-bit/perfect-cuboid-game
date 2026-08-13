# Stage14-t51 — alias-free exact-pair diagonal and off-diagonal residue reduction

## Status

`COMPLETE_ALIAS_FREE_EXACT_PAIR_DIAGONAL_AND_OFFDIAGONAL_RESIDUE_REDUCTION`

Stage14-t50 reduced the remaining external split-prime Frobenius problem to a selector-sensitive two-auxiliary Gaussian second moment. Stage14-t51 separates its same-residue diagonal from the genuinely off-diagonal residue correlation.

## 1. Critical-strip coordinate bound

The live variables satisfy

```text
k = n/delta = gcd(n,eps*m) <= eps*m,
n <= eps*m*delta.
```

On the critical super-sqrt canonical-prime strip,

```text
eps*m*delta <= 2B/ell = O(B^(1/2)).
```

Hence

```text
N(U)=m = O(B^(1/2)),
N(V)=n = O(B^(1/2)),
```

and every Gaussian coordinate of `U,V` is `O(B^(1/4))`.

## 2. Alias-free auxiliary regime

Take distinct external split primes

```text
p,q ~ L=B^rho,
rho>1/8.
```

Then

```text
pq ~ B^(2rho) >> B^(1/4).
```

Inside one fixed common-refinement packet, equality of the oriented Gaussian pair `(U,V)` modulo `pq` therefore implies exact equality over the integers. Thus the same-modulus residue diagonal is not a new collision object in this regime: it is the exact oriented Gaussian-pair diagonal.

This no-alias statement is independent from the separate t49 amplifier-cardinality requirement `P>=H*B^-o(1)`. Any eventual global theorem must choose an auxiliary scale satisfying both conditions and be uniform on that chosen scale.

## 3. Route the diagonal to tH5

Stage14-tH5 already proves near-linear coefficient energy for exact Gaussian pairs:

```text
E_exact <= source_mass * B^o(1).
```

Retaining the common-refinement packet and the oriented pair `(U,V)` only refines the exact-pair labeling, so it does not create a larger collision fiber than the corresponding exact-pair roadworks packet.

Consequently, in the alias-free regime,

```text
E_res(pq) = E_exact <= H*B^o(1),
```

and after summing the two auxiliary primes,

```text
R_diag <= P^2 * H * B^o(1).
```

This is exactly the target scale required by t49/t50. The statement uses the asymptotic tH5 theorem; the frozen collision energy below is only a deterministic diagnostic.

## 4. Frozen deterministic alias audit

Reciprocal-quotient frozen family:

```text
states                              560
external split primes                16
prime pairs checked                 120
prime range                    2017..2269
minimum pq                    4,092,493
maximum |Gaussian coordinate|          7
exact-pair collision energy       14,242
maximum exact-pair multiplicity       66
residue-pair collision energy     14,242
alias failures                         0
```

All 120 external-prime pairs give exactly the same collision energy before and after reduction modulo `pq`.

The finite value `14,242` is not promoted to an asymptotic near-linear claim; near-linearity comes from merged tH5.

## 5. Remaining live object

After removing the exact/residue diagonal, the remaining theorem is strictly narrower than t50's original contract:

```text
OffDiagonalTwoAuxiliaryGaussianResidueDispersion
```

It must prove, after t32 angular completion and with signed common-refinement aggregation retained,

```text
R_off,res
  <= P^2 * (sum_R ||w_R||_2^2) * B^o(1).
```

For the physical unweighted family this becomes

```text
R_off,res <= H*P^2*B^o(1).
```

The proof must keep:

- signed aggregation across common-refinement blocks,
- the shared `U/V` modulus group,
- both distinct split auxiliary primes `p,q`,
- the divisor-coupled hyperbola selector,
- canonical-prime, branch, interval and reconstruction masks.

Collapsing ordered state pairs to cross-kernel coefficients before this cancellation remains forbidden because it imports the unresolved fourth energy `E4`.

## tH decision

**Stage14-tH14 is still needed. No Stage14-tH15 is needed.**

No separate new support object appeared in t51. The diagonal portion of tH14's requested two-auxiliary theorem is now closed by the `rho>1/8` no-alias regime plus tH5. tH14 should therefore focus on the genuinely off-diagonal residue/frequency correlation.

## Boundary

```text
STAGE14_T51=COMPLETE_ALIAS_FREE_EXACT_PAIR_DIAGONAL_AND_OFFDIAGONAL_RESIDUE_REDUCTION
CRITICAL_STRIP_GAUSSIAN_COORDINATE_BOUND_B_QUARTER=true
AUXILIARY_PRODUCT_NO_ALIAS_FOR_RHO_GT_ONE_EIGHTH=true
TWO_AUXILIARY_RESIDUE_DIAGONAL_NEAR_LINEAR=true
TH5_EXACT_PAIR_ENERGY_USED=true
OFFDIAGONAL_TWO_AUXILIARY_RESIDUE_DISPERSION_REQUIRED=true
OFFDIAGONAL_TWO_AUXILIARY_RESIDUE_DISPERSION_PROVED=false
GLOBAL_EXTERNAL_TWO_PRIME_MEAN_SQUARE_BOUND_PROVED=false
GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false
GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
TH14_STILL_NEEDED=true
TH15_NEEDED=false
NEXT=Stage14-t52 attack OffDiagonalTwoAuxiliaryGaussianResidueDispersion; consume tH14 if available and keep the rho>1/8 alias-free diagonal separated
```
