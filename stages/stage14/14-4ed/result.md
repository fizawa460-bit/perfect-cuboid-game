# Stage14-4ed — Cayley row / post-column filter collapse

## Status

`COMPLETE_ROW_POST_COLUMN_FILTER_COLLAPSE_ON_SECOND_RECIPROCAL_DIVISOR_CANDIDATES`

Consumes batch-local `Stage14-4ec` and merged `Stage14-X13`, `Stage14-s7-42`, `Stage14-s7-46`, `Stage14-4ea`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. X13 quantifier-order lock

Merged X13 proves in the reverse reciprocal order that after `(U,V,M)` are fixed, the second reciprocal difference-of-squares equation gives only `B^o(1)` candidates `(c,d,p,q)`, and the first reciprocal equation then gives only `B^o(1)` candidates for the remaining signed quotients.

At that point the Cayley row congruences

```text
N == M  (mod C_-),
N == -M (mod C_+)
```

are applied only to the already divisor-many candidate values of `N`. X13 explicitly proves that the row lift is a filter, not a new polynomial support variable.

Stage14-4ec has placed the current reciprocal conditional receiver in exactly this order: canonical allocation incidence first, then one `W_2` difference-of-squares divisor pair.

## 2. No second polynomial density factor from row/post-column reconstruction

For a fixed canonical allocation incidence and allowed `B^o(1)` decoration, let `Cand_2(w)` be the divisor-many second-reciprocal candidate set from 4ec.

The full post-column acceptance is

```text
R_full(w)=1
```

iff at least one candidate in `Cand_2(w)` passes the Cayley row congruences and all remaining post-column reverse-reconstruction masks.

Because

```text
|Cand_2(w)|=B^o(1),
```

and X13 reconstructs the row/signed-quotient data from each candidate with `B^o(1)` multiplicity, the row/post-column layer does not create another polynomial support coordinate.

```text
CAYLEY_ROW_IS_FILTER_AFTER_SECOND_RECIPROCAL_FACTORIZATION=true
POST_COLUMN_RECONSTRUCTION_MULTIPLICITY=Bo1
ROW_POST_COLUMN_INDEPENDENT_POLYNOMIAL_SUPPORT=false
ROW_POST_COLUMN_RECHARGE_ALLOWED=false
```

This does not assert that every divisor candidate is physical. Existence may still be arithmetically sparse; it is simply one Boolean filter on the same finite candidate family.

## 3. Canonical reciprocal divisor-filter predicate

Absorb parity, divisibility, dyadic, squarefree/coprime, Cayley-row and post-column tests into one charged-once predicate

```text
R_div(w)=1
```

iff there exists a positive factorization

```text
F_2^- F_2^+ = W_2(w)
```

whose induced reciprocal tuple passes all physical filters.

Then the current two-factor mainline receiver is legally rewritten as

```text
mu_G = mu_can * mu_div,
```

where `mu_div` is the conditional density of `R_div=1` on the canonical allocation-bearing slope family. This is the same nested Boolean cardinality ratio as `mu_recip`; only its arithmetic representation has been made explicit.

```text
RECIPROCAL_CONDITIONAL_RENAMED_AS_EXPLICIT_DIVISOR_FILTER_DENSITY=true
CANONICAL_ALLOCATION_DIVISOR_FILTER_DENSITY_CHAIN_EXACT=true
INDEPENDENCE_ASSUMED=false
```

## 4. Next

Stage14-4ee should test whether generic divisor-count or balanced-window information can itself force `mu_div` to be fixed-power small. If not, the obstruction becomes an averaged divisor-filter density for the arithmetic family `W_2(w)`.

## Boundary

```text
STAGE14_4ED=COMPLETE_ROW_POST_COLUMN_FILTER_COLLAPSE_ON_SECOND_RECIPROCAL_DIVISOR_CANDIDATES
CAYLEY_ROW_IS_FILTER_AFTER_SECOND_RECIPROCAL_FACTORIZATION=true
POST_COLUMN_RECONSTRUCTION_MULTIPLICITY=Bo1
ROW_POST_COLUMN_INDEPENDENT_POLYNOMIAL_SUPPORT=false
RECIPROCAL_CONDITIONAL_RENAMED_AS_EXPLICIT_DIVISOR_FILTER_DENSITY=true
CANONICAL_ALLOCATION_DIVISOR_FILTER_DENSITY_CHAIN_EXACT=true
DIVISOR_FILTER_FIXED_POWER_DEFICIT_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=false
NEXT=Stage14-4ee
```
