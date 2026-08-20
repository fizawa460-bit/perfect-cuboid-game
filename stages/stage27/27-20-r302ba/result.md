# Stage27-20-r302ba — the collision zero mode is controlled by one explicit gcd-degeneracy ratio

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302az
SOURCE_STAGE=Stage20

Let

```text
g = gcd(C,q).
```

By definition of the singular square-root factor,

```text
s_q(C)^2
 = product_{p^k||q}
     p^{2 min(floor(k/2),floor(v_p(C)/2))}
 <= gcd(C,q)=g.
```

Hence

```text
s_q(C)^3/q
 <= g^{3/2}/q.
```

Therefore the unavoidable zero-frequency baseline from r302az is power-small whenever the packet has a fixed-power gap in the structural ratio

```text
g^{3/2}/q.
```

For example, if `q` itself is polynomially large and `g <= q^{2/3-epsilon}` for fixed `epsilon>0`, then

```text
g^{3/2}/q <= q^{-3epsilon/2},
```

which is a genuine power once the corresponding lower power for `q` is known on the packet range.

No such uniform range is assumed here. Instead define for fixed `kappa>0`

```text
Deg_kappa
 = {packet : g^{3/2}/q > B^{-kappa}}.
```

Outside `Deg_kappa`, the collision zero mode is deterministically at most `B^{-kappa}`. Thus the structural baseline branch can be closed by either:

1. a direct pointwise range theorem forcing `g^{3/2}/q` power-small; or
2. a same-`H_phys^MAIN` exceptional-mass theorem showing `Deg_kappa` carries power-small physical mass.

This separates the zero-mode obstruction from the nonzero residue-energy correlation completely. The former is now a gcd/valuation degeneracy event in the exact merged quadratic congruence, not a spectral theorem problem.

```text
FIRST_MISSING_LEMMA_ZERO_MODE=
MAINWallQuadraticCongruenceGCDDegeneracyExceptionalMass

STAGE27_20_R302BA_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
S_Q_C_SQUARED_LE_GCD_C_Q=true
ZERO_MODE_BY_GCD_THREE_HALVES_OVER_Q_PROVED=true
ZERO_MODE_SPECTRAL_CANCELLATION_RELEVANT=false
GCD_DEGENERACY_BAD_EVENT_DEFINED=true
GCD_DEGENERACY_EXCEPTIONAL_MASS_PROVED=false
NONZERO_ENERGY_FIXED_POWER_DEFICIT_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
CURRENT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302bb
NEXT_BATCH=Stage27-20-r302-main-batch
```