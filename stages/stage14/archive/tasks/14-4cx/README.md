# Stage14-4cx

This stage consumes merged `4cw`, merged `s7-38`, merged `X12`, and the Cayley-good-core arithmetic of `4cq/4cs`.

Entering theorem:

```text
V(B) << B^(61/112+o(1)).
```

The new exact observation is that the apparent Cayley-only annulus

```text
A_C := C_Cayley/J
```

is endpoint-small.  Indeed

```text
A_C | C/C_res | g_star^2,
g_star/H_star^2 | Omega,
Omega=B^o(1),
```

while the full Cayley-good core is coprime to the Cayley numerator `M`; since `H_star|M`,

```text
gcd(C_Cayley,H_star)=1.
```

Therefore

```text
A_C | Omega^2 = B^o(1).
```

Consequently the lost core

```text
D=C/J=(C/C_Cayley)A_C
```

satisfies, after endpoint-small peel,

```text
D_0 | H^2.
```

Moreover `J|C_Cayley` is coprime to `H`, while merged X12 gives

```text
H | gcd(L_-,L_+).
```

Hence `H` survives into both column cofactors and

```text
D_0 | h_-h_+.
```

This has two consequences:

1. every fixed-power nonproportional block with `chi>1/4` is empty;
2. on `chi<=1/4`, the entire lost-core factor is removed from the column cofactor support before the full Cayley-row lift is counted.

The resulting complete counts are

```text
E_DRC <= 2phi + 1/2 - 2chi + 2s,
E_H   <= 3phi - 1/8 - 3s,
s=log_B H.
```

Their `2:3` weighted minimum gives

```text
E <= 23/20 - (12/5)theta.
```

Combining with the merged `s`/`k` counts yields

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44.
```

The equality segment is

```text
theta=23/88,
19/88 <= phi <= 21/88,
s=phi-19/88,
J=C_Cayley=B^(9/44+o(1)).
```

The remaining row lift has exponent `1/22`; the residual column support decreases from `1/22` to `0` across the segment as the forced lost-core divisor grows from `B^o(1)` to `B^(1/22+o(1))`.

Receiver:

```text
TwentyThreeFortyFourthsCayleyAnnulusCollapseLostCoreColumnRowLiftTradeoff
```

No mainline H/tH theorem is needed.  Next: `Stage14-4cy`.
