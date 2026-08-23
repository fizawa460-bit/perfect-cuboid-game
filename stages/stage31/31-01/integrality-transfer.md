# Stage31-01 — integrality transfer

## Verdict

```text
C_TO_E_INTEGRALITY_ASSUMPTION_USED=false
DIRECT_QUARTIC_INTEGRALITY_TRANSFER=VERIFIED
INTEGRALITY_TRANSFER_GAP_COUNT=0
```

Stage29 correctly rejected the implication

```text
C_anom(Z) -> E_anom(Z)
```

as unproved. The explicit Stage31 birational map has denominators, so Stage31 does **not** repair the proof by asserting that implication.

Instead it uses the direct integral model

```text
C_anom: 20 Z^2 = f(Y)
U = 10 Z
Q: U^2 = 5 f(Y)
   = 5Y^4+40Y^3+90Y^2-40Y+5.
```

For every `(Y,Z) in Z^2` on `C_anom`, `(Y,U=10Z)` is an integral point on `Q`. This map is injective. Conversely an integral point `(Y,U)` on `Q` comes from an integral point on `C_anom` exactly when `10 | U`, in which case `Z=U/10`.

Thus a complete enumeration of `Q(Z)` followed by the exact divisibility test `10|U` is a complete enumeration of `C_anom(Z)`. No elliptic integrality preservation is required.

## Complete execution

Magma V2.29-9 `IntegralQuarticPoints(Q,[1,10])` returned the three hyperelliptic-sign representatives

```text
(-1,10), (1,-10), (11,370).
```

Restoring `U -> -U` gives six signed integral points. Every returned `U` is divisible by 10, hence

```text
C_anom(Z) = {
  (-1,-1), (-1,1),
  ( 1,-1), ( 1,1),
  (11,-37), (11,37)
}.
```

The Magma handbook entry for `IntegralQuarticPoints(Q,P)` states that the routine returns all integral points on the quartic. The exact execution is pinned by workflow run `32607148918`, artifact `9484415535`, and artifact digest `sha256:32c6f9ab32b60faa29b7a8cf7cfc3133115ea19ece422facf51ff255089f8a17`.

## Why the elliptic model is still retained

Stage31 also supplies an explicit birational map to

```text
E_anom: y^2=x^3-275x+1750
```

and Magma independently proves its full Mordell--Weil group is `Z/2 + Z`. These facts repair the missing geometric adapter and cross-check Paper E, but they are no longer the logical bridge used for integral-point completeness. This avoids the exact Stage29 firewall that an elliptic integral-point list does not automatically close the quartic.
