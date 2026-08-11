# Stage14-t145 — retain the fixed-U host denominator in endpoint annulus capacity

## Status

`COMPLETE_HOST_NORMALIZED_ENDPOINT_PRINCIPAL_CAPACITY`

Consumes Stage14-t144 on this batch branch together with merged Stage14-t140/t141 and the exact fixed-packet identity `h*k0=eta*epsilon*m`.

Stage14-t140 deliberately used the coarser estimate

```text
M_Y <= B^o(1)*(Y+1)^2
```

for an endpoint width layer `Y<H<=2Y`.  Here the fixed-U host denominator is retained instead of discarded.

## 1. Exact cofactor annulus thickness

Merged t140 gives

```text
N_0=sqrt(B)/(h*k0),
H=2*sqrt(B)*(N_0-N(z))/N(z),
```

and for `H<=sqrt(B)`

```text
H/(3*h*k0)
 <= N_0-N(z)
 <= H/(2*h*k0).
```

Hence for one dyadic width layer

```text
Z(Y)={z:Y<H(z)<=2Y}
```

the scalar cofactor norms lie in an interval of length

```text
O(Y/(h*k0)+1).
```

Each exact norm has only `B^o(1)` primitive Gaussian representations after the frozen local/sector labels. Therefore

```text
#Z(Y)
 <= B^o(1)*(Y/(h*k0)+1).                          (1.1)
```

This factor was already present in t140 and is now kept.

## 2. Refined principal capacity

For each cofactor in `Z(Y)`, the unrestricted canonical split-prime interval has length `O(Y+1)`.  The ordinary-residue principal baseline is

```text
M_Y
 = 1/|R_d| * sum_{z in Z(Y)} |P_z|,
R_d=(Z[i]/dZ[i])^x.
```

Dropping only the denominator `|R_d|>=1` gives

```text
M_Y
 <= B^o(1)*(Y/(h*k0)+1)*(Y+1).                    (2.1)
```

For polynomial endpoint width `Y=B^(lambda+o(1))`, write

```text
h*k0=B^(rho+o(1)),
rho>=0.
```

Then (2.1) yields the exponent bound

```text
M_Y
 <= B^( max(2*lambda-rho, lambda, 0) + o(1)).      (2.2)
```

On the live endpoint range `lambda>=1/4-o(1)`, the zero term is irrelevant.

```text
HOST_NORMALIZED_ENDPOINT_CAPACITY_EXACT=true
ENDPOINT_CAPACITY_WITH_HK0=M_Y_LE_BO1_TIMES_(Y_over_hk0_plus_1)_TIMES_(Y_plus_1)
ENDPOINT_CAPACITY_EXPONENT=max(2lambda-rho,lambda)
```

## 3. Why this is stronger than the quarter-floor estimate

Stage14-t141 used only

```text
M_Y<=B^(2*lambda+o(1))
```

and obtained the universal floor `lambda>=1/4-o(1)` for any layer carrying `B^(1/2-o(1))` principal mass.

With (2.2), a polynomially large fixed-U host scale can no longer be ignored.  If a width layer is to carry principal-scale mass

```text
M_Y >= B^(1/2-o(1)),
```

then necessarily

```text
max(2*lambda-rho,lambda) >= 1/2-o(1).              (3.1)
```

The exact consequence is deferred to t146, where the near-full alternative is separated from the genuinely short endpoint range.

## 4. Beyond-Mitsui host scale gives a subpolynomial gain even at rho=0 exponent

Stage14-t144 proves on a beyond-Mitsui endpoint packet

```text
h*k0 >= C*d
```

for a fixed positive packet constant `C`, while

```text
d>exp(c_safe*sqrt(log B)).
```

Thus (2.1) carries an actual factor at least

```text
1/(h*k0)
 <= exp(-c_safe*sqrt(log B)+O(1))
```

in the `Y^2/(h*k0)` term.

This is a genuine pseudopolynomial capacity improvement but still equals `B^{-o(1)}`, not a fixed `B^-delta` saving.  It must not be promoted to a strict exponent gain by itself.

```text
BEYOND_MITSUI_HOST_CAPACITY_GAIN=PSEUDOPOLYNOMIAL_ONLY
BEYOND_MITSUI_HOST_CAPACITY_FIXED_POWER_SAVING=false
```

## 5. Receiver and H decision

This stage restores a coefficient that t140 intentionally discarded but does not yet choose the surviving exponent alternative.  The minimal receiver is therefore not declared changed until t146 performs that localization.

No new theorem audit is needed: this is exact capacity accounting.

```text
RECEIVER_MATERIALLY_CHANGED=false
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH33_NEEDED=false
NEXT_INTERNAL_TARGET=HostNormalizedEndpointWidthFloorLocalization
NEXT=Stage14-t146
```
