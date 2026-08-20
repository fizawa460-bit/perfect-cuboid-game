# Stage28-40 deep upper research ledger

```text
TASK_ID=Stage28-40
ROUTE_KIND=DEEP_BRIDGE_UPPER_ATTACK
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
TARGET=improve_or_localize_upper_control_of_R28=M3/N2
```

## Route U1 — independent endpoint bounds

The inherited endpoint bounds give the audited checkpoint30 corridor

\[
\mathcal R_{28}(B)=\frac{M_3(B)}{N_2(B)}
=o\!\left(B^{3/4}(\log B)^{5-\delta}\right)
\qquad(0<\delta<1/46).
\]

A strict numerical improvement from endpoint division would require either a stronger whole-family `M3` upper or a stronger whole-family `N2` lower. Repository-wide and current-literature rematches found neither. Reopening the already-exhausted Stage27 lower campaign without new input is forbidden.

```text
U1_NUMERIC_IMPROVEMENT=false
U1_REASON=no_stronger_compatible_endpoint_theorem
```

## Route U2 — same-host local-sieve comparison

This route is Stage28-specific: compare the first-order local rarity of the two competing conditions on the shared two-face host.

For odd primes define `alpha_p` for the Stage19 space-square local acceptance and `beta_p` for the Stage20 third-face local acceptance.

For `p=1 mod 4`, Stage19 gives

\[
\alpha_p=\rho_p
=1-\frac4p+O(p^{-2}).
\]

For `p=3 mod 4`, Gaussian norm parity makes

\[
\alpha_p=1.
\]

Stage20 gives, for every odd prime,

\[
\beta_p=1-\delta_p,
\qquad
\delta_p=\frac{2(p-\chi_4(p))}{p^2+6p+1}
=\frac2p+O(p^{-2}).
\]

Therefore

\[
\log\frac{\alpha_p}{\beta_p}
=-\frac{2\chi_4(p)}p+O(p^{-2}).
\]

Indeed, on split primes `alpha_p/beta_p=1-2/p+O(p^-2)`, while on inert primes `alpha_p/beta_p=1+2/p+O(p^-2)`.

The prime sum

\[
\sum_p \frac{\chi_4(p)}p
\]

converges, and `sum_p p^-2` converges absolutely. Hence the finite-prime relative products have a positive finite limiting ratio after the finitely many bad primes are absorbed into the constant:

\[
0<C_-\le
\frac{\prod_{p\le z}\alpha_p}{\prod_{p\le z}\beta_p}
\le C_+<\infty
\qquad(z\to\infty),
\]

in the local-product sense.

Equivalently, both mechanisms have the same first-order sieve dimension `2`:

- space-square: coefficient `4/p` on the density-`1/2` split primes;
- third-face: coefficient `2/p` on all odd primes.

This is a genuine comparative result, but its scope is deliberately narrow. Stage19 only has the fixed-finite-prime quantifier order for this local sieve, while Stage20 has a separate growing-prime Selberg theorem. Thus one may **not** promote the bounded local-product ratio to

\[
N_2/M_2 \asymp M_3/M_2
\]

or to `M3/N2=Theta(1)`.

The rigorous consequence is negative/localizing:

```text
SPACE_LOCAL_SIEVE_DIMENSION=2
THIRD_FACE_LOCAL_SIEVE_DIMENSION=2
FIRST_ORDER_LOCAL_SIEVE_DIMENSION_DIFFERENCE=0
LOCAL_PRODUCT_RATIO_POLYNOMIAL_DRIFT=false
LOCAL_PRODUCT_RATIO_EXTRA_LOG_POWER_DRIFT=false_at_first_order
GLOBAL_COUNT_RATIO_CONSTANT_PROVED=false
GROWING_MODULUS_STAGE19_PROVED=false
```

Therefore a polynomial or extra-log asymptotic ordering between `N2` and `M3`, if it exists, cannot be justified merely by comparing the first-order local blocker dimensions already in the repository.

## Route U3 — geometric cover comparison

Both conditions are degree-two style completion restrictions over closely related two-face geometry, but their global counting technology is asymmetric:

- Stage20 third-face completion has the split `4A1` quartic-del-Pezzo / K3 cover plus Huang thin-cover saving and a growing-prime Selberg sieve;
- Stage19 space completion has the squareclass/Kummer/moving-genus-one receiver and the strong inherited half-power whole-family bound, but no theorem converting the fixed-prime parity product into a growing-modulus relative comparison with the third-face cover.

The current del-Pezzo/Kummer literature rematch does not bridge these exact physical heights and moving families. In particular, a generic `B^(1+epsilon)` fixed-del-Pezzo upper is weaker than the current Euler upper and supplies no relative comparison with `N2`.

```text
U3_DIRECT_COVER_DOMINATION_FOUND=false
U3_HEIGHT_MONOTONE_MAP_FOUND=false
U3_UNIFORM_RELATIVE_POINT_COUNT_FOUND=false
```

## Route U4 — direct relative receiver

The unresolved Stage28 upper problem is now sharper than “improve either exponent”. A new theorem can discharge the bridge directly if it supplies, on the exact primitive/canonical common physical host, one of:

```text
RELATIVE_HOST_SHARE_THEOREM:
  Phi20(B) <= G(B) * Sigma19(B)
  with G(B) materially smaller than B^(3/4)(log B)^(5-delta)

JOINT_COMPLETION_CORRELATION_THEOREM:
  quantitative comparison of third-face and space-square completion indicators
  on the same two-face physical measure with effective growing parameters

UNIFORM_TWO_COVER_HEIGHT_THEOREM:
  a common-height rational-point estimate comparing the K3 third-face cover
  against the moving space-square/Kummer cover

STAGE19_GROWING_MODULUS_THEOREM:
  effective uniformity strong enough to compare its local product on the same
  z=z(B) scale as the Stage20 dimension-two sieve
```

Any such theorem must preserve exact cutoff `R<=B`, primitivity, canonicalization, exact face multiplicity and object/incidence adapters.

## Route verdict

```text
MATERIALLY_DISTINCT_ROUTES_TESTED=4
DIRECT_ENDPOINT_ROUTE=NO_IMPROVEMENT
LOCAL_SIEVE_ROUTE=NEW_COMPARATIVE_NEGATIVE_CERTIFICATE
GEOMETRIC_COVER_ROUTE=NO_TRANSFERABLE_DOMINATION_THEOREM
DIRECT_RELATIVE_RECEIVER=PRECISE_OPEN_GATE
BLIND_REOPEN_STAGE27=false
```

Checkpoint40 has therefore performed the roadmap-required bounded deep exploration. It does not manufacture a stronger numeric bridge upper. Its new value is the proof-level localization that the known first-order local sieve dimensions cancel in the relative comparison, pushing any future ordering theorem into genuinely global correlation/height/support information.