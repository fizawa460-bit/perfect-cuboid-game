# Stage14-4cw

Stage14-4cw consumes merged `s7-36` and attacks its only remaining `9/16` proportional barrier.

The proportional identity

```text
L_-=0,
z_1=a*t,
z_2=b*t,
t=B^(1/8+o(1))
```

is decomposed primewise through

```text
K_x=oddpart(gcd(x_1,x_2)),
K_y=oddpart(gcd(y_1,y_2)),
H_T=oddpart(gcd(x_1,y_2)),
H_S=oddpart(gcd(y_1,x_2)).
```

The full 2-primary part of `t` and the two same-side odd cells have square forced into `u_res`.  Therefore they can carry exponent at most `theta-phi`; the remaining cross-root mass is at least

```text
phi-theta+1/8.
```

Merged `H^4|q_xi` then gives

```text
E_prop<=3theta-1/2<=7/16.
```

The proportional branch is no longer a barrier.  The merged s7-36 nonproportional bound becomes the whole-family theorem:

```text
V(B)<<B^(19/34+o(1)).
```

Current receiver:

```text
NineteenThirtyFourthsSingleCrossRootRowColumnTwinShortLiftIncidence
```

No auxiliary H/tH theorem is requested.  Next: `Stage14-4cx`.