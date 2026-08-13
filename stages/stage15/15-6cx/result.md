# Stage15-6cx — BLIND_REDISCOVERY from the exact cell-normalized forms

Base: Stage15-6cw. This substage deliberately restarts from the explicit formulas only, without using the Arsenal labels to choose a route.

Write
\[
X=abM,\quad Y=cdN,\quad Z=acU,\quad W=bdV.
\]
For every odd switched modulus, `(q,H)=1`, so the cell coefficients are units modulo `q`. The two channel systems are therefore the simultaneous quadratic incidences
\[
X^2+Y^2\equiv0,\qquad Z^2-W^2\equiv0\pmod{d_S},
\]
\[
X^2-Y^2\equiv0,\qquad Z^2+W^2\equiv0\pmod{e_O}.
\]

## Rediscovery 1: root-ratio coordinates

For every odd prime power in the support, primitive states have invertible relevant ratios. Thus the S-channel is locally
\[
X/Y\in\{\rho:\rho^2=-1\},\qquad Z/W\in\{\pm1\},
\]
and the O-channel reverses the two root types. CRT glues these choices into finitely many primitive root-line orientations modulo `q`.

This independently rediscovers the direct root-line model, but now in coefficient-free normalized ratios.

## Rediscovery 2: a discrepancy-first formulation

The desired count is not merely a sum of local densities. For each dyadic physical box and local orientation define
\[
\Delta(q,\rho;\mathcal B)
:=N(q,\rho;\mathcal B)-\frac{\operatorname{Vol}(\mathcal B)}{q^2}.
\]
The small-side obstruction is precisely the sum of these discrepancies over the product-height boxes, not the main density. This suggests averaging `Delta` over `(q,rho)` before taking absolute values. That is a genuine dispersion/large-sieve target and is distinct from bounding every modulus separately.

## Rediscovery 3: mixed norm/split algebra

The same four congruences say that one pair is constrained by a norm-zero condition while the other is constrained by a split difference, with roles reversed between the two channels. Equivalently, primes of the channel modulus select an `i`-orientation on one pair and a sign orientation on the other. This gives a mixed Gaussian/split algebra rather than a pure Gaussian norm problem.

This representation may permit character or Hecke-symbol expansion, but no such average is currently certified. Keep it LIVE.

## Rediscovery 4: factor switching on the split side

Because
\[
X^2-Y^2=(X-Y)(X+Y),\qquad Z^2-W^2=(Z-W)(Z+W),
\]
a large divisor of a split channel can be assigned between two linear factors. The companion plus-form remains a norm condition. This creates a hybrid divisor-switch receiver in which one side is linear after orientation selection. It is not the same bookkeeping as switching the full gcd divisor to a complementary quadratic cofactor.

## Rediscovery 5: local valuation rigidity

At odd `p|q`, the plus-form condition forces `p=1 mod 4`; Hensel lifting then gives boundedly many roots at every prime power away from singular zero ratios. Primitivity excludes simultaneous zero ratios. Therefore the local root multiplicity is divisor-like and the expected density remains `q^-2`; there is no hidden loss from arbitrary many local branches.

This does not supply a power saving, but it removes one possible obstruction and makes a modulus-average discrepancy estimate plausible.

## Rediscovery 6: exact-survivor closure

The ambient four-form congruence family contains many points that need not satisfy the exact space-diagonal-integral/Gaussian-square survivor relation. Therefore a reconstruction attack should ask whether a root-ratio orientation plus three physical residual variables determines the fourth variable up to divisor-many ambiguity. If yes, the fringe can collapse without cancellation. This is logically independent of the discrepancy route and remains UNTESTED/LIVE.

## Blind ranking before consulting prior route labels

1. **Root-ratio discrepancy dispersion**: highest leverage because it attacks the exact small-side fringe rather than the main density, uses `(q,H)=1`, and can also provide large-modulus sparsity.
2. **Exact survivor reconstruction in normalized ratios**: second, because it may remove ambient states deterministically.
3. **Mixed norm/linear-factor switching**: third, because it exposes linear structure on half of each S/O channel.
4. **Pure local-density counting**: supporting layer, not an exponent by itself.
5. **Per-modulus direct lattice count**: necessary local input but known to leave the fringe.

After comparison with 6cw, these are all already represented in the exhaustive ledger; no materially new family was missed.

```text
STAGE15_6_SUBSTAGE=6cx
STAGE15_6CX_BLIND_REDISCOVERY=true
STAGE15_6CX_ROOT_RATIO_NORMALIZATION=true
STAGE15_6CX_DISCREPANCY_FORMULATION=true
STAGE15_6CX_MIXED_NORM_SPLIT_ALGEBRA=true
STAGE15_6CX_LINEAR_FACTOR_SWITCH_REDISCOVERED=true
STAGE15_6CX_LOCAL_ROOT_MULTIPLICITY=DIVISOR_LIKE
STAGE15_6CX_EXACT_SURVIVOR_RECONSTRUCTION=LIVE_UNTESTED
STAGE15_6CX_BLIND_TOP_ROUTE=ROOT_RATIO_DISCREPANCY_DISPERSION
STAGE15_6CX_EXIT=CANDIDATE_CLASSIFICATION_AND_ROUTE_SELECTION_READY
```
