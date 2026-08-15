# Stage25-40 — upper-bound provenance and no-fake-product firewall

EVIDENCE_LEVEL=PROVED_FROM_AUDITED_INTERFACES
CHECKPOINT=40
STATUS=PROVED_SUBMITTED_FOR_FRESH_AUDIT
STAGE=Stage25
TRANSITION=Stage16->Stage19

## 1. Objective

Checkpoint40 determines exactly where the current upper bound for the Stage25 endpoint ratio comes from, which alternative routes are genuinely equivalent, which weaker zero-density routes remain informative, and which tempting products are mathematically invalid.

Stage25 compares the disjoint population sizes

\[
M_1(B)=\#\{\text{primitive canonical exactly-one-face, no space requirement, }R\le B\},
\]

and

\[
N_2(B)=\#\{\text{primitive canonical exactly-two-face + integral space, }R\le B\}.
\]

The ratio `N2/M1` is not objectwise survival.

## 2. Quantitative global upper

The audited source asymptotic is

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B.
\]

The audited Stage24 target-side whole-family theorem remains

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

Therefore

\[
\boxed{
\frac{N_2(B)}{M_1(B)}
\ll_\varepsilon
B^{-3/2+\varepsilon}(\log B)^{-1}
}.
\]

This is the current quantitative Stage25 upper inherited from the target numerator theorem. Stage24-40 proved no strict whole-family sub-square-root improvement, so Stage25 does not silently strengthen it.

```text
GLOBAL_ENDPOINT_UPPER=B^(-3/2+epsilon)(log B)^(-1)
UPPER_PROVENANCE=STAGE24_TARGET_HALF_POWER_DIVIDED_BY_STAGE21_SOURCE_ASYMPTOTIC
STRICTER_GLOBAL_UPPER_PROVED_AT_CHECKPOINT40=false
HALF_POWER_INTRINSIC_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
```

## 3. Path A and Path B are equivalent upper derivations

Path A is the exact count identity

\[
\frac{N_2}{M_1}=\frac{M_2}{M_1}\frac{N_2}{M_2}.
\]

Using Stage22 and Stage24,

\[
\frac{M_2}{M_1}\asymp B^{-1}(\log B)^4,
\qquad
\frac{N_2}{M_2}\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-5},
\]

gives the same

\[
B^{-3/2+\varepsilon}(\log B)^{-1}.
\]

Path B is the exact count identity

\[
\frac{N_2}{M_1}=\frac{N_1}{M_1}\frac{N_2}{N_1}.
\]

Using Stage21 and audited post-Stage24 Stage23,

\[
\frac{N_1}{M_1}\asymp B^{-1}(\log B)^2,
\qquad
\frac{N_2}{N_1}\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-3},
\]

again gives the same upper.

These products are legal because their intermediate counts cancel exactly. They are not probabilistic independence factorizations.

```text
DIRECT_UPPER_CHECK=PASS
PATH_A_UPPER_CHECK=PASS
PATH_B_UPPER_CHECK=PASS
THREE_WAY_UPPER_CONSISTENCY=PASS
```

## 4. Independent qualitative upper routes are weaker, not multiplicative bonuses

Stage24 has two independent qualitative zero-density mechanisms on the literal `M2 -> N2` transition.

### 4.1 Space-square thin cover

The geometrically integral degree-two thin-cover theorem gives

\[
N_2(B)=o(B(\log B)^5).
\]

Dividing by `M1(B)~cB^2 log B` gives

\[
\boxed{
\frac{N_2(B)}{M_1(B)}=o(B^{-1}(\log B)^4).
}
\]

### 4.2 Fixed-prime squareclass sieve

The fixed-prime sieve gives

\[
\frac{N_2(B)}{M_2(B)}\to0.
\]

Combining this with the exact identity and Stage22

\[
\frac{M_2}{M_1}\asymp B^{-1}(\log B)^4
\]

gives the same qualitative Stage25 consequence

\[
\boxed{
\frac{N_2(B)}{M_1(B)}=o(B^{-1}(\log B)^4).
}
\]

For any fixed `epsilon<1/2`, the quantitative half-power-derived upper is asymptotically stronger because

\[
\frac{B^{-3/2+\varepsilon}(\log B)^{-1}}
{B^{-1}(\log B)^4}
=
B^{-1/2+\varepsilon}(\log B)^{-5}\to0.
\]

The thin-cover and local-sieve routes are therefore independent explanations of zero density, not extra factors that can be multiplied onto the half-power theorem.

## 5. New localized fixed-curve consequence

Stage24-40 proves that the physical degree-four rational-curve square-root mechanism is absent and that every fixed physical rational curve has `M.C>=5`. Hence each fixed curve contributes at most

\[
O(B^{2/5+o(1)}),
\]

and every genuinely fixed finite collection has the same polynomial scale up to constants.

Dividing such a fixed-finite target contribution by Stage25's source asymptotic yields

\[
\boxed{
\frac{N_{2,\mathrm{fixed\ finite}}(B)}{M_1(B)}
=O\!\left(B^{-8/5+o(1)}(\log B)^{-1}\right).
}
\]

This is a valid Stage25-localized refinement. It is **not** a whole-family bound. Stage24 explicitly did not prove uniform implied constants or uniform `o(1)` over a number of curves growing with `B`.

```text
FIXED_FINITE_CURVE_ENDPOINT_UPPER=B^(-8/5+o(1))(log B)^(-1)
FIXED_FINITE_CURVE_REFINEMENT_PROVED=true
GROWING_CURVE_FAMILY_UNIFORM_SUMMATION_PROVED=false
GLOBAL_BOUND_UPGRADED_FROM_FIXED_CURVES=false
```

## 6. No-fake-product firewall

The following products are forbidden.

1. ` (N1/M1)*(M2/M1) ` is **not** `N2/M1`. Both factors start from the same denominator `M1`; there is no cancellation or intersection theorem. Its tempting scale `B^-2 (log B)^6` is not a Stage25 bound.
2. The Stage24 local-sieve zero-density factor cannot be multiplied onto the independent Stage14/19 half-power upper to manufacture an extra saving.
3. The Stage24 thin-cover little-o cannot be multiplied onto the half-power upper. They are alternative upper proofs for the same target set.
4. Path A and Path B are alternative exact decompositions of the same endpoint ratio; their upper estimates cannot be multiplied together.
5. Stage21's `(log B)^2` enhancement relative to the ambient space baseline is not an additional factor in Stage25's global upper.

```text
NO_FAKE_PRODUCT_SAVING_CHECK=PASS
STAGE24_LOCAL_SIEVE_MULTIPLIED_WITH_HALF_POWER=false
STAGE24_THIN_COVER_MULTIPLIED_WITH_HALF_POWER=false
PATH_A_AND_PATH_B_MULTIPLIED_TOGETHER=false
STAGE21_INTERACTION_FACTOR_RECHARGED=false
```

## 7. Upper bottleneck localization

Within the audited interfaces used by Stage25, improving the global endpoint power beyond the current `B^(-3/2+epsilon)` scale requires at least one genuinely new input of one of the following forms:

- a strict whole-family improvement to the target theorem `N2(B)<<B^(1/2+epsilon)`; or
- a new direct Stage25-specific theorem relating the disjoint `M1` source population to the `N2` target population more strongly than endpoint division.

Stage24-40 already localizes the unresolved target-side obstruction to a moving/collective near-maximal-occupancy / first-small-point / transverse-incidence regime. Checkpoint40 does not reopen that upstream program because no distinct Stage25-specific receiver is supplied by the current comparison lattice.

This is a provenance boundary, not a claim that exponent `1/2` is true or sharp.

## 8. Directional firewall from checkpoint30

Checkpoint30's fresh audit established that Stage21 order chambers and Stage23 shared-edge channels do not yet have a proved adapter. Checkpoint40 does not revive the rejected directional ratio theorem.

```text
DIRECTIONAL_SOURCE_CHANNEL_ADAPTER_PROVED=false
DIRECTIONAL_ENDPOINT_UPPER_REFINEMENT=OPEN_GATE_ADAPTER_REQUIRED
DIRECTIONAL_OVERCLAIM_REINTRODUCED=false
```

## 9. Finite-data boundary

Checkpoint20 finite counts and Stage24/Stage14 larger censuses remain regression and diagnostic evidence only. No empirical exponent is promoted here.

```text
FINITE_DATA_USED_AS_PROOF=false
FINITE_POWER_FIT_PROMOTED=false
```

## 10. Exit

```text
DISCOVERY_CHECKPOINT=Stage25-40
UPPER_BOUND_PROVENANCE_REQUIRED=SATISFIED
NO_FAKE_PRODUCT_SAVING_REQUIRED=SATISFIED
STAGE24_LOCAL_SIEVE_AND_THIN_COVER_NOT_MULTIPLIED=true
BOUNDED_NEW_ATTACK_OPENED=NONE
BOUNDED_NEW_ATTACK_REASON=no distinct Stage25-specific receiver beyond the audited target-side Stage24 upper gate
FIXED_FINITE_CURVE_REFINEMENT_PROVED=true
STRICTER_GLOBAL_UPPER_PROVED=false
FORMULA_SUBSTITUTION_ONLY=false
EXPLORATION_EVIDENCE_COMPLETE=true
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=40
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage25-audit
CODEX_REQUIRED=false
```
