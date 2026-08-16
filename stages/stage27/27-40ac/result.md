# Stage27-40ac — fully balanced wall intrinsic-structure attack

```text
TASK_ID=Stage27-40ac
OWNER_STAGE=Stage27
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_ONLY
ROUTE_LABEL=WALL_STRUCTURE
STATUS=SUBMITTED_PENDING_CONSOLIDATED_FRESH_AUDIT
ADVANCE_TO_CHECKPOINT50=false
```

## Target

Stage27-r401a localizes possible half-power saturation to the fully balanced wall `theta=1/4`, with all four coefficient factors `B^(1/4+o(1))`. This route tests whether common-core, primitive root-line, or reduced-column structure already frozen in Stage14/15 supplies a previously uncharged fixed-power deficit there.

## 1. Common-core scale split

The repository repeatedly obtains strong root-line spacing only when a charged common/core modulus has polynomial size. In the exact primitive pair setting a root-line modulus `Q=B^(lambda+o(1))` can contribute a `B^{-lambda}`-scale spacing gain. Conversely, when the surviving common/core modulus is only `B^o(1)`, the same root-line condition costs only `B^{o(1)}` and cannot change the polynomial exponent.

This is already visible in the Stage14 conductor/core localization and the Stage15 two-channel/common-support reductions: fixed-power-large core strata are controllable, while saturation is pushed onto low-core/full-conductor/small-common-support strata.

Therefore the critical wall cannot be crossed merely by reusing the existence of a common core. A new theorem must prove one of:

\[
\text{(A) polynomial common-core size on all half-power-saturating mass,}
\]

or

\[
\text{(B) a fixed-power deficit for the low-core population itself.}
\]

Neither is currently frozen as a theorem.

## 2. Root-line recharge firewall

Once a core/orientation is charged, the primitive root-line congruence is a consequence of that same core. Any reduced-column or reconstructed projection carrying the identical residue/root label modulo the same charged modulus cannot be multiplied as an independent density loss.

This is the same no-double-charge phenomenon already exposed in Stage14 same-root synchronization and Stage15 endpoint/core reconstruction: algebraically equivalent projections may improve coordinates but do not create a second independent modulus factor.

Thus an exponent crossing requires a genuinely independent second arithmetic condition, or a joint correlation theorem proving that the physical occupancy of the already-charged line is sparse by a fixed power.

## 3. Reduced-column / reconstruction multiplicity

The relevant reverse maps and divisor/core decorations throughout the terminal MAIN/S reductions have `B^o(1)` fibers once physical outer data and frozen labels are fixed. Such finite/subpolynomial reconstruction multiplicity is exponent-neutral. Re-encoding the wall by reduced columns, reciprocal witnesses, or common-core labels is therefore not itself a fixed-power thinning mechanism.

This matches Stage27-40aa: fixed witness moments/reconstruction multiplicities are exponent-equivalent to support. The only useful new statement would be about support occupancy, not about the number of encodings of an occupied point.

## 4. Exact wall-structure reopen contract

A legal intrinsic wall breakthrough must provide at least one of the following on the same primitive canonical `R<=B` population:

1. **large-core forcing:** every half-power-saturating wall packet has a charged modulus `Q>=B^delta` for fixed `delta>0`;
2. **low-core sparsity:** packets with every available common/core modulus `B^o(1)` have total mass `<<B^(1/2-delta+o(1))`;
3. **independent second modulus:** after the first core/root line is charged, a second non-equivalent modulus/root condition survives and its joint occupancy yields a fixed power;
4. **support correlation:** a direct theorem giving fixed-power sparsity of physical reduced-column/root-line support without claiming independence.

The existing common-core/root-line/reduced-column identities establish none of these four fixed-power statements on the whole critical wall.

## Outcome

The third mandatory r401a continuation has now been executed. It closes algebraic relabeling, same-root recharge, and subpolynomial reconstruction multiplicity as *standalone* sources of a new exponent. It leaves a sharply stated intrinsic wall gate: polynomial core forcing, low-core sparsity, genuinely independent second-modulus structure, or direct support-correlation sparsity.

```text
WALL_STRUCTURE_ATTACK_EXECUTED=true
COMMON_CORE_EXISTENCE_ALONE_FIXED_POWER_SAVING=false
SAME_ROOT_SECOND_CHARGE_ALLOWED=false
REDUCED_COLUMN_RECONSTRUCTION_MULTIPLICITY_FIXED_POWER_SAVING=false
POLYNOMIAL_CORE_FORCING_PROVED=false
LOW_CORE_WALL_SPARSITY_PROVED=false
INDEPENDENT_SECOND_MODULUS_PROVED=false
DIRECT_WALL_SUPPORT_CORRELATION_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
MANDATORY_R401_CONTINUATIONS_EXECUTED_CANDIDATE=true
NEXT_CHECKPOINT=40
AUDIT_STATUS=PENDING_CONSOLIDATED
MERGE_ALLOWED=false
PERFECT_CUBOID_CONCLUSION=NONE
```
