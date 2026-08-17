# Stage27-20-r301e — growing-prime blocker sieve on the space-diagonal target

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301d

## 1. Larger completion population

Let `P_sp(B)` count primitive/canonical shared-edge two-face host objects under the same Euclidean cutoff `R<=B` for which the space diagonal is integral, without requiring the third face to be nonintegral.

Every Stage27 `N_2(B)` object has exactly one shared edge between its two integral faces, hence gives one object counted by `P_sp(B)`.  Therefore

\[
\boxed{N_2(B)\le P_{\rm sp}(B)}.
\]

The larger population may also contain objects with a third integral face; no perfect-cuboid existence statement is used.

## 2. Reuse of the Stage14-e11 sieve

Stage27-20-r301d proves that the Stage14-e10/e11 state-G nonsquare blocker sets are literally blockers for `P_sp` on the same toric host and the same physical height.  Stage14-e11 proves growing-prime uniform Selberg-sieve control for these host residue sets, with

\[
\delta_p=\frac2p+O(p^{-2}),
\]

sieve dimension `2`, and

\[
G(N)=C_G(\log N)^2+O(\log N).
\]

The e11 proof counts host points avoiding the blocker residue sets; it does not depend on the surviving completion target being the third-face square after the blocker set itself has been fixed.  Since every space-diagonal completion avoids the same blocker sets, the same host sieve upper-bounds `P_sp(B)`.

Taking the same admissible growing level `N=(log B)^(1/100)` therefore gives

\[
\boxed{
P_{\rm sp}(B)
\ll
\frac{B(\log B)^5}{(\log\log B)^2}
}
\]

and consequently

\[
\boxed{
N_2(B)
\ll
\frac{B(\log B)^5}{(\log\log B)^2}.
}
\]

The fixed-finite-prime product argument also gives zero density inside the full two-face host.

## 3. This is a valid theorem but not a Stage27 improvement

Stage27 already has

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

For any fixed `epsilon<1/2`, this polynomial half-power theorem is asymptotically stronger than the transferred host-sieve bound above.  Therefore the sieve transfer is mathematically valid but does not lower the current Stage27 upper exponent.

It is also illegal to multiply the host-sieve factor by the existing half-power theorem without a new theorem showing the blocker sieve acts uniformly inside the specific half-power receiver used by Stage14/Stage27.

## 4. Boundary

```text
STAGE27_20_R301E_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
SPACE_DIAGONAL_GROWING_PRIME_SIEVE_TRANSFER_PROVED=true
SPACE_DIAGONAL_HOST_SIEVE_BOUND=B(log B)^5/(log log B)^2
N2_HOST_SIEVE_BOUND_PROVED=true
HOST_SIEVE_BOUND_BEATS_CURRENT_HALF_POWER=false
SIEVE_FACTOR_MULTIPLIED_WITH_HALF_POWER=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEXT_DERIVED_ROUTE=27-20-r301f
```
