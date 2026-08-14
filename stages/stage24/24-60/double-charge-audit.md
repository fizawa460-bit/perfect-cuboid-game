# Stage24-60 — double-charge audit

CHECKPOINT=60
ROLE=CONDITION_CHARGE_FIREWALL
STATUS=SUBMITTED_FOR_FRESH_AUDIT

## 1. What is genuinely new on the Stage24 arrow

Stage24 is the literal subset transition

\[
\mathcal A_2(B)=\mathcal B_2(B)\cap\{R\in\mathbf Z\}.
\]

For the Stage18 two-face source, space integrality is therefore genuinely new. In the paired Gaussian-norm coordinates frozen by Stage19,

\[
R\in\mathbf Z
\iff AB\in\mathbf Z^2
\iff \operatorname{sf}(A)=\operatorname{sf}(B).
\]

This squareclass equality may be charged once as the Stage24 transition predicate.

## 2. Stage16S is a comparator, not a multiplicative factor

Stage16S proves the ambient law

\[
N_S^{all}/U\sim c_S/B.
\]

This is the intrinsic control baseline. It is **not** an additional factor to multiply into the independent Stage14 half-power upper bound or into the Stage19 fixed-prime sieve.

Allowed use:

```text
compare (N2/M2) against (NSall/U)
```

Forbidden without a new theorem:

```text
N2/M2 <= or ~ (NSall/U) * (another independently derived saving)
```

No measure-preserving factorization of that type is known.

## 3. Stage21 logarithmic enhancement belongs to the one-face host

Stage21 proves

\[
(N_1/M_1)/(N_S^{all}/U)\asymp(\log B)^2.
\]

That enhancement is localized to the shared-`P` nested-Pythagorean bulk for the exactly-one-face source. It cannot be imported as a prefactor for the exactly-two Stage24 source.

```text
STAGE21_LOG2_TRANSFER_TO_STAGE24=false
REASON=DIFFERENT_CONDITIONED_SOURCE_MEASURE
```

## 4. Stage23 has already paid space

Stage23 starts at `N1`: every source object already has integral space diagonal. Its new event is an additional cross-leg Pythagorean face.

Therefore the Stage19 squareclass condition may be reused there as a target coordinate description, but may not be charged as a second thinning event.

```text
STAGE23_SPACE_ALREADY_IN_SOURCE=true
STAGE23_SQUARECLASS_NEW_COST=false
STAGE23_DOUBLE_CHARGE_CHECK=PASS
```

The post-Stage24-50 supersession changes the lower-status ledger only. It does not alter this causal firewall.

## 5. Stage22 horizontal ratio is not a conditional probability

Stage16 exactly-one and Stage18 exactly-two are adjacent disjoint face strata. Thus

\[
M_2/M_1
\]
is a matched count ratio, not the probability that an `M1` object survives by adding a face. The same caution applies to `N2/N1` in Stage23.

The identity

\[
\frac{N_2/M_2}{N_1/M_1}
=
\frac{N_2/N_1}{M_2/M_1}
\]
is valid algebraically, but it must not be narrated as multiplication of independent conditional probabilities.

## 6. Fixed-prime local sieve does not pay the half-power

Stage19's good split-prime acceptance has

\[
1-\rho_p=4/p+O(p^{-2}).
\]

The audited theorem takes a fixed finite prime set first, then `B->infinity`, then enlarges the set. It proves qualitative zero density.

Checkpoint40 further showed that even hypothetical polynomial prime windows for the same local tensor yield only logarithmic thinning. Hence the local sieve does **not** explain or pay for

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

```text
HALF_POWER_ATTRIBUTED_TO_LOCAL_SIEVE=false
LOCAL_SIEVE_QUALITATIVE_ZERO_DENSITY=true
LOCAL_SIEVE_FIXED_POWER_SAVING_PROVED=false
```

## 7. Thin-cover route is independent qualitative evidence, not another factor

Checkpoint30's space-square degree-two thin cover gives an independent proof that `N2/M2->0`. It does not supply an effective fixed power. It therefore cannot be multiplied with the squareclass sieve or the Stage14 upper bound to synthesize a stronger rate.

```text
INDEPENDENT_ZERO_DENSITY_PROOFS_MAY_BE_COMPARED=true
THEIR_SAVINGS_MAY_BE_MULTIPLIED=false
```

## 8. Checkpoint50 lower family is a lower witness, not bulk mass

The mixed-parity `C17` family proves

\[
N_2(B)\gg\sqrt{\log B}.
\]

It establishes infinitely many primitive exactly-two space-integral objects. It does not prove that this family has positive density inside `N2`, does not identify the true exponent, and does not provide a factor in any upper-bound decomposition.

The odd/odd zero-survival subfamily and mixed-parity infinite-survival subfamily prove arithmetic heterogeneity, not a global density formula.

## 9. Legal charge map

```text
AMBIENT_SPACE_BASELINE_STAGE16S=COMPARATOR_ONLY
STAGE21_SPACE_EVENT=CHARGED_ONCE_ON_M1_SOURCE
STAGE22_SECOND_FACE_EVENT=ADJACENT_STRATUM_COMPARISON_NOT_SUBSET_SURVIVAL
STAGE23_SECOND_FACE_EVENT=NEW_ON_ALREADY_SPACE_SOURCE
STAGE23_SPACE_EVENT=NOT_CHARGED_AGAIN
STAGE24_SPACE_SQUARECLASS_EVENT=NEW_AND_CHARGED_ONCE_ON_M2_SOURCE
STAGE24_LOCAL_SIEVE=QUALITATIVE_MECHANISM_ONLY
STAGE24_THIN_COVER=INDEPENDENT_QUALITATIVE_ROUTE_ONLY
STAGE14_HALF_POWER_UPPER=INHERITED_GLOBAL_UPPER_NOT_CAUSALLY_ASSIGNED
STAGE24_C17_FAMILY=LOWER_WITNESS_ONLY
DOUBLE_CHARGE_CHECK=PASS
```

No independence product, sharp exponent, or perfect-cuboid conclusion is asserted.
