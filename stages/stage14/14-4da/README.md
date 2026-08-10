# Stage14-4da

Stage14-4da consumes merged `Stage14-X13`, merged `Stage14-4cz`, merged `Stage14-4cx`, and merged `Stage14-s7-41` on latest main.

The entering canonical theorem is already

```text
V(B) << B^(1/2+o(1))
```

from merged X13. Stage14-4da does **not** re-claim the square-root promotion. It refines the possible square-root saturation band.

Merged X13 leaves only

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
H=B^(s+o(1)),
0<=s<=phi-5/24.
```

Let

```text
J=B^(j+o(1)),
D0=(C/J) after the endpoint-small peel,
d=chi-j.
```

Merged 4cx proves

```text
D0 | H^2,
gcd(J,H)=1,
H^2 | h_-h_+,
|h_-h_+|/D0 <= B^(1/4-chi+o(1)).
```

Write the cross-root excess

```text
G := H^2/D0.
```

For fixed `D0`, the relation `D0*G=H^2` forces `G` into one fixed squareclass:

```text
G = sf(D0)*t^2.
```

Hence a dyadic `G=B^(e+o(1))` costs at most `B^(e/2+o(1))` choices, not `B^e`.

Also let

```text
K=oddpart(gcd(x1,x2))*oddpart(gcd(y1,y2))=B^(kappa+o(1)).
```

Merged 4cz gives

```text
gcd(K,C)=1,
K^2 | h_-h_+,
gcd(K,H)=1.
```

Therefore, after removing `D0`, the residual single-column product is divisible by

```text
K^2*G.
```

At `theta=1/4`, its ambient exponent is

```text
a_col=1/4-chi=1/2-2phi.
```

If `2kappa+e>a_col`, the stratum is empty. Otherwise the complete fixed-power count is

```text
E_4da(kappa,e)
 <= 2phi
    + kappa
    + e/2
    + (a_col-2kappa-e)
 = 1/2-kappa-e/2.
```

Consequently every fixed-power same-side root gcd or fixed-power cross-root excess is strictly sub-square-root.

Square-root saturation now requires

```text
K=B^o(1),
H^2/D0=B^o(1),
chi-j=2s,
j=chi-2s.
```

Together with `s<=phi-5/24`,

```text
1/6 <= j <= chi.
```

Thus the surviving square-root receiver is

```text
SquareRootThetaQuarterCrossRootSquareMatchedLostCorePrimitiveSingleColumnIncidence
```

with no fixed-power same-side gcd and no fixed-power cross-root square excess beyond the lost core.

The global exponent remains

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
STRICT_SUB_SQRT_POWER_SAVING_PROVED=false.
```

### H / tH

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
S7_41_MAINLINE_H_GATE_SUPERSEDED=true
GENERIC_GENUS_ONE_H_REOPENED=false
T80_CROSS_PROMOTED_TO_MAINLINE=false
TH22_CROSS_PROMOTED_TO_MAINLINE=false
```

There is still exact prime-power allocation to inspect between the matched cross-root square `H^2`, the lost core `D0`, and the two column signs. No new averaged theorem is requested yet.

Next: `Stage14-4db`.
