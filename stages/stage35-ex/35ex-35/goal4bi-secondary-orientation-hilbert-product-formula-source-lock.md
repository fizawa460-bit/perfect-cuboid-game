# Stage35-EX Goal4BI source lock — rational Hilbert product formula cannot see the secondary Gaussian orientation bits

Scope: continue exact Goal4BH after exact-head verification. Audited authority remains V74 / Goal4AK. Goal4BI tests whether the primewise `mu_2` orientation bits `sigma_i(ell)` can be closed by an ordinary rational Hilbert-symbol product formula, including the real and 2-adic places.

The answer is structurally negative: every reservoir prime splits in `Q(i)`, so the rational local field `Q_ell` already contains `sqrt(-1)`. The orientation bit distinguishes the two split Gaussian primes, while rational quadratic Hilbert symbols forget that distinction. A new global symbol over `Q(i)` would be required.

## 1. Input from Goal4BH

For a secondary reservoir prime `ell|s_a`, Goal4BH has

```text
p_a=(ell,i-iota_a),
bar(p_a)=(ell,i+iota_a),

iota_a^2=-1 mod ell,

sigma_a=-1 <=> p_a divides Omega_a,
sigma_a=+1 <=> bar(p_a) divides Omega_a.             (BI-orient)
```

Thus `sigma_a` records which of the two primes of `Z[i]` above the rational prime `ell` is selected by the reduced space Gaussian square root. Cyclic analogues hold.

## 2. Every reservoir prime is split over Q(i)

Goal4BE proves

```text
ell|s_a*s_b*s_c => ell=1 mod 4.                      (BI-split-prime)
```

Hence

```text
-1 in Q_ell^{*2},
Q(i) tensor_Q Q_ell ~= Q_ell x Q_ell.                (BI-split)
```

The two factors correspond exactly to the two embeddings

```text
i -> +iota_i(ell),
i -> -iota_i(ell),                                    (BI-two-emb)
```

or equivalently to `p_i` and `bar(p_i)`.

The Goal4BH sign `sigma_i(ell)` is therefore a **split-prime orientation datum**. It is not the value of the local quadratic character associated with `Q_ell(i)/Q_ell`, because that quadratic algebra is already split.

## 3. Rational Hilbert symbols with -1 are identically trivial at reservoir primes

For every `t in Q_ell^*`,

```text
(-1,t)_ell=1                                         (BI-H1)
```

because the first Hilbert-symbol entry is a square.

Consequently no product formula based on local symbols

```text
(-1,t_v)_v
```

can distinguish the two alternatives in `(BI-orient)` at any reservoir prime.

This remains true if `t` is chosen from the rational reservoirs, Kummer representatives, face norms, or space norms: the loss occurs in the first slot before any such choice matters.

## 4. Rational norms also forget the orientation

Goal4BF has

```text
s_a=Sigma_a*bar(Sigma_a),
N(Sigma_a)=s_a,                                      (BI-norm)
```

and cyclically. Passing from the Gaussian divisor `Sigma_a` to its rational norm identifies the two conjugate choices. Likewise

```text
N(p_a)=N(bar(p_a))=ell.                              (BI-prime-norm)
```

Therefore every invariant factoring only through rational norms or rational squareclasses loses the exact datum measured by `sigma_i`.

This explains why Goal4AU/BE can produce rational rank-two squareclass/Jacobi shadows while Goal4BF/BG/BH still retain an oriented phase gauge.

## 5. Why the real and 2-adic places do not repair this by themselves

A rational Hilbert reciprocity formula has the form

```text
product_v (r,s)_v=1                                  (BI-product)
```

for one **fixed global pair** `r,s in Q^*`.

The finite reservoir contributions needed for Goal4BH are not values of a known fixed rational pair: at every reservoir prime they distinguish `p_i` from `bar(p_i)`, which rationalization has already collapsed.

The real place can contribute a sign only from the signs of the rational global pair. It cannot reconstruct which split Gaussian prime was chosen at an odd `ell`.

At `2`, `Q_2(i)/Q_2` is non-split, but a 2-adic correction can constrain reservoir orientations only after a single global class over `Q(i)` (or an equivalent global cohomological symbol) has been identified. No such class is present in Goal4BF–Goal4BH.

Thus adding `v=infinity` and `v=2` to a rational product formula does not restore information that was discarded at the split odd primes.

## 6. Correct global level for a possible next obstruction

To retain `sigma_i`, one must stay over the Gaussian field and use data that distinguishes prime ideals:

```text
p_i != bar(p_i).                                      (BI-Gaussian)
```

A viable global reciprocity step would therefore require a **single source-derived global Gaussian symbol**, for example a fixed pair

```text
(alpha,beta) in Q(i)^* x Q(i)^*
```

whose local quadratic Hilbert symbols or equivalent `K_2`/quartic residue character evaluations recover the Goal4BH orientation bits at all relevant prime ideals.

Goal4BF supplies oriented prime ideals and quartic residue phases. Goal4BG supplies face/space Gaussian square roots. Goal4BH identifies the local matching bits. But no retained source identity currently assembles them into one global Gaussian pair or one idele-class character.

Therefore ordinary Hilbert reciprocity over `Q` is fail-closed, while a genuinely Gaussian global-symbol adapter remains untested.

## 7. Verdict

Certified provisionally:

```text
RESERVOIR_PRIMES_SPLIT_IN_QI=true;
SIGMA_IS_SPLIT_PRIME_ORIENTATION=true;
RATIONAL_HILBERT_MINUS_ONE_SYMBOL_TRIVIAL_AT_RESERVOIRS=true;
RATIONAL_NORM_FORGETS_SIGMA=true;
REAL_AND_TWO_ADIC_CORRECTIONS_ALONE_INSUFFICIENT=true;
RATIONAL_HILBERT_PRODUCT_ROUTE_FAIL_CLOSED=true;
GLOBAL_GAUSSIAN_SYMBOL_CONSTRUCTED=false;
BRANCH_PRUNING=false.
```

Not certified:

```text
Gaussian K2 obstruction;
quartic global product contradiction;
universal sigma product;
any h_i=1;
any d_i=1;
E1;
Stage35 closure;
Perfect Cuboid existence/nonexistence.
```

Next unit:

```text
35EX-35_GOAL4BJ_GLOBAL_GAUSSIAN_K2_OR_QUARTIC_CHARACTER_ADAPTER_PREFLIGHT
```

Question: use the source-canonical `Theta_**`, `Psi_*`, and `Sigma_i` to construct one global Gaussian `K_2` symbol / Hecke-character datum whose local evaluations recover the Goal4BH `sigma_i`; if no such source-derived global pair exists, fail-close this reciprocity branch.

No merge. No hostile-audit credit. MAIN-STATE remains V74 / Goal4AK.
