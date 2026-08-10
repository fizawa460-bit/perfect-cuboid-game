# Stage14-4cz

Stage14-4cz consumes merged `Stage14-4cy`, merged `Stage14-s7-40`, and the exact same-side root-gcd placement from merged `Stage14-s7-37` on latest main.

The entering canonical theorem is

```text
V(B) << B^(23/44+o(1)).
```

and every possible saturation packet is already confined to

```text
theta=23/88,
phi=19/88,
chi=j=9/44,
H=B^o(1),
C=J=C_Cayley*B^o(1),
```

with two remaining short supports of exponent `1/22`.

The new point is that the **same-side** odd root gcd

```text
K_x=oddpart(gcd(x1,x2)),
K_y=oddpart(gcd(y1,y2)),
K=K_x*K_y
```

is not merely a divisor of the first residual `u_res`. On the unique 23/44 endpoint it enters both remaining short coordinates simultaneously:

```text
K^2 | u_res,
K^2 | M,
K^2 | N,
K | L_-,
K | L_+,
gcd(K,C)=1.
```

Hence, after the column split

```text
L_-=J_L-*h_-,
L_+=J_L+*h_+,
```

we have

```text
K|h_-,
K|h_+,
K^2|h_-h_+.
```

The Cayley row can likewise be divided by `K^2` without changing its modulus because `K` is a unit modulo `C`.

If

```text
K=B^(kappa+o(1)),
0<=kappa<=1/22,
```

the charged-once endpoint count becomes

```text
E_4cz(kappa)
 <= 2phi
    + kappa
    + 2*max(0,1/22-2kappa).
```

At `phi=19/88`, this is

```text
19/44 + kappa + 2*max(0,1/22-2kappa).
```

Its maximum is still `23/44`, but equality is possible only at

```text
kappa=0.
```

In particular every fixed-power same-side root gcd is strictly subcritical, and

```text
kappa>=1/132
```

already gives a square-root-scale bound `<=1/2` on that stratum.

Therefore any surviving 23/44 saturation sequence must satisfy

```text
K_x=K_y=B^o(1).
```

Together with merged 4cy/s7-40

```text
H_S=H_T=B^o(1),
```

all four cross-state odd root-gcd cells are subpolynomial. The four physical roots are therefore globally odd-primitive up to `B^o(1)` pairwise gcds.

The whole-family exponent itself remains

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44.
```

New receiver:

```text
TwentyThreeFortyFourthsGloballyOddPrimitiveFourRootFullCayleyTwinShortFirstResidualIncidence
```

No mainline H/tH theorem is needed. The next exact step is to use global odd primitivity inside the remaining twin `1/22` signed-reciprocal reconstruction before requesting any averaged theorem.

Next: `Stage14-4da`.
