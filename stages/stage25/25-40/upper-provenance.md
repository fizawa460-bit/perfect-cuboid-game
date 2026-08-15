# Stage25-40 upper provenance lattice

## Legal quantitative routes

Let `E(B)=N2(B)/M1(B)`.

### Direct endpoint

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon},\qquad
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B
\]

gives

\[
E(B)\ll_\varepsilon B^{-3/2+\varepsilon}(\log B)^{-1}.
\]

### Path A

\[
E=\frac{M_2}{M_1}\frac{N_2}{M_2}
\]

with scales

\[
B^{-1}(\log B)^4\times B^{-1/2+\varepsilon}(\log B)^{-5}
=
B^{-3/2+\varepsilon}(\log B)^{-1}.
\]

### Path B

\[
E=\frac{N_1}{M_1}\frac{N_2}{N_1}
\]

with scales

\[
B^{-1}(\log B)^2\times B^{-1/2+\varepsilon}(\log B)^{-3}
=
B^{-3/2+\varepsilon}(\log B)^{-1}.
\]

All three are the same endpoint upper in different coordinates.

## Legal qualitative routes

The Stage24 thin cover gives `N2=o(B(log B)^5)`, hence

\[
E=o(B^{-1}(\log B)^4).
\]

The Stage24 fixed-prime sieve gives `N2/M2=o(1)`; composing with Stage22 through the exact Path A identity again gives

\[
E=o(B^{-1}(\log B)^4).
\]

These are independent qualitative zero-density explanations but are quantitatively weaker than the half-power upper.

## Localized fixed-curve route

Stage24-40 proves each fixed physical rational curve has target contribution `O(B^(2/5+o(1)))`; the same holds for a genuinely fixed finite collection. Therefore its Stage25 endpoint contribution satisfies

\[
E_{\rm fixed\ finite}(B)
=O(B^{-8/5+o(1)}(\log B)^{-1}).
\]

No growing-family summation is certified.

## Invalid products

```text
INVALID_1=(N1/M1)*(M2/M1)
REASON_1=no intermediate cancellation; disjoint target counts and common denominator

INVALID_2=(half_power_target_upper)*(local_sieve_density_factor)
REASON_2=alternative proofs for the same target set; no independence theorem

INVALID_3=(half_power_target_upper)*(thin_cover_little_o)
REASON_3=alternative upper mechanisms, not nested independent filters

INVALID_4=(Path_A_upper)*(Path_B_upper)
REASON_4=two coordinate decompositions of the same endpoint ratio

INVALID_5=Stage21_log_squared_interaction * Stage25_endpoint_upper
REASON_5=Stage21 interaction is already contained in Path B coordinates and cannot be recharged
```

## Bottleneck statement

The present global upper power is inherited from the target numerator theorem. The Stage25 source asymptotic is sharp enough for division; its denominator is not the unresolved component. A global improvement requires a new whole-target theorem or a genuinely new direct source-target incidence theorem.

```text
UPPER_PROVENANCE_LATTICE=COMPLETE
DOUBLE_CHARGE_FIREWALL=PASS
STRICT_SUB_SQRT_TARGET_INPUT_AVAILABLE=false
STAGE25_SPECIFIC_DIRECT_UPPER_RECEIVER_AVAILABLE_IN_IMPORTED_LATTICE=false
```
