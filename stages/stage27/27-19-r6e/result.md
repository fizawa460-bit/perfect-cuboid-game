# Stage27-19-r6e — r6 viability verdict and alternate-upper redirect

```text
TASK_ID=Stage27-19-r6e
PARENT_ROUTE=Stage27-19-r6d
ROUTE_KIND=ROUTE_VERDICT
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
CURRENT_MU=1/2
ADVANCE_TO_CHECKPOINT50=false
```

## r6 verdict

The occupied-`R` route has now been pushed through its immediately available algebraic consequences.

1. `r6a` produced the exact occupied-`R` squareclass receiver.
2. `r6b` proved that its squareclass collision is exactly the frozen Stage15 squareclass predicate in different coordinates.  A second squareclass sieve would double-charge the same condition.
3. `r6c` proved the genuinely new primitive support restriction that occupied `R` is odd and has only prime factors `1 mod 4`, but this host is `B^{1-o(1)}` and gives no fixed-power deficit by itself.
4. `r6d` used the new viewpoint to return to an older, genuinely different upper contract and proved a missing representation lemma: fixed `(p,q,g)` multiplicity is `B^{o(1)}`.

Therefore the r6 occupied-`R` lane is **not promising as a standalone fixed-power route** and should be frozen rather than extended by new names.

```text
R6_STANDALONE_FIXED_POWER_VIABILITY=NO_GO
R6_SQUARECLASS_SIEVE_LANE=FROZEN_DUPLICATE_OF_STAGE15
R6_SPLIT_PRIME_SUPPORT_LANE=FROZEN_LOGARITHMIC_ONLY
OCCUPIED_R_SUPPORT_FIXED_POWER_DEFICIT_PROVED=false
```

## Why the batch does not return to the lower lane yet

The audited lower reentry `27-19-r401d` already has a clean reopen contract: a new physical rational curve with effective height `<8`, a stronger polynomial cancellation, or a polynomially thicker family.  Nothing in r6b-r6d supplies such a lower-family construction.

Blindly restarting the nonlinear lower ansatz would therefore violate the anti-loop rule.

```text
LOWER_R401D_REOPEN_INPUT_PRODUCED_BY_R6=false
BLIND_LOWER_RESTART_ALLOWED=false
```

## Alternate upper route now has new input

The old `27-19-r402f` route stopped because it lacked an exact representation theorem for

\[
s^2(m^2+n^2)=pg,\qquad n^2(r^2-s^2)=qg.
\]

Stage27-19-r6d now supplies that theorem at fixed `(p,q,g)`:

\[
\#\text{representations}\le4\tau(pg)^2=B^{o(1)}.
\]

Thus the next upper route is no longer a blind restart.  It can legally reopen the tau/core lane with the representation entropy removed.

For reduced `tau=p/q`, define

\[
G_{p,q}(B)=\#\{g:\text{a physical representation exists at }(p,q,g)\}.
\]

Then

\[
G_{p,q}(B)\le w_B(p/q)\le B^{o(1)}G_{p,q}(B).
\]

On a dyadic tau-height band let

\[
I_T(B)=\sum_{T\le H(p/q)<2T}G_{p,q}(B),
\qquad
E_T(B)=\sum_{T\le H(p/q)<2T}G_{p,q}(B)^2.
\]

The exact next arithmetic target is a fixed-power bound for this **realized-core incidence/energy**, retaining the r402c restriction

\[
g\ll B^2/T.
\]

This is a different counting dimension from r5's fixed-`R` packet and from r6's duplicate squareclass sieve.

## Route selection

```text
UPPER_ALTERNATE_HAS_NEW_INPUT=true
SELECTED_NEXT_ROUTE=27-19-r402g
SELECTED_NEXT_TARGET=TAU_REALIZED_CORE_SUPPORT_ENERGY_WITH_FIXED_CORE_MULTIPLICITY_REMOVED
REUSE_R402C_CORE_BOUND=g<<B^2/T
REUSE_R402F_DYADIC_HYBRID=true
LOWER_ROUTE_SELECTED=false
R6_LANE_FROZEN_AFTER_AUDIT_PASS=true
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
ADVANCE_TO_CHECKPOINT50=false
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage27-19-r6-audit
```
