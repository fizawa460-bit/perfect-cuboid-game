# Stage14-s7-92 — reciprocal root windows to a short primitive divisor-ratio occupancy receiver

## Status

`COMPLETE_RECIPROCAL_ROOT_WINDOWS_TO_SHORT_PRIMITIVE_DIVISOR_RATIO_OCCUPANCY_RECEIVER`

Consumes batch-local `Stage14-s7-90/91`, merged `Stage14-4fg`, and merged `Stage14-Work-brX30`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Exact ratio-window geometry

Stage14-s7-91 gives, in one frozen physical chart,

```text
R_X(n)=[X_-/(alpha*n), X_+/(alpha*n)],
R_Y(n)=[beta*n/Y_+, beta*n/Y_-],
R_phys(n)=R_X(n) intersect R_Y(n).
```

The root windows are dyadically localized. If necessary, split each polynomial root range into `O(log B)=B^o(1)` dyadic blocks first. Hence on one charged chart

```text
X_+/X_-=B^o(1),
Y_+/Y_-=B^o(1).
```

No fixed-power cost is assigned to this dyadic localization.

## 2. Archimedean nonemptiness only reproduces the radial product window

The interval intersection is nonempty exactly when its lower endpoints do not exceed the opposite upper endpoints:

```text
X_-/(alpha*n) <= beta*n/Y_-,
beta*n/Y_+ <= X_+/(alpha*n).
```

Equivalently,

```text
boxed:
X_-*Y_-/(alpha*beta)
 <= n^2
 <= X_+*Y_+/(alpha*beta).
```

Thus the purely archimedean overlap constrains `n` to the product-scale window

```text
N_arch
 := [sqrt(X_-Y_-/(alpha beta)),
     sqrt(X_+Y_+/(alpha beta))].
```

Its multiplicative width is

```text
sqrt((X_+/X_-)*(Y_+/Y_-))=B^o(1).
```

But a multiplicative dyadic-width interval centered at polynomial height can contain polynomially many integers. Therefore the nonemptiness of the two real root windows alone gives no fixed-power saving on the normalized radial support.

```text
ARCHIMEDEAN_RATIO_WINDOW_NONEMPTY_IFF_N_IN_PRODUCT_WINDOW=true
ARCHIMEDEAN_PRODUCT_WINDOW_MULTIPLICATIVE_WIDTH=Bo1
ARCHIMEDEAN_WINDOW_ALONE_FIXED_POWER_SAVING=false
```

This is a no-go only for charging the real-window overlap itself. It does not discard the arithmetic divisor-ratio selector.

## 3. The ratio interval is multiplicatively short

Whenever `R_phys(n)` is nonempty, its multiplicative width is bounded by each parent interval:

```text
width_mult(R_phys(n))
 <= min(X_+/X_-, Y_+/Y_-)
 = B^o(1).
```

Hence every accepted normalized radial integer `n` must admit a positive coprime divisor pair `(u,v)` satisfying

```text
gcd(u,v)=1,
u*v | n,
u/v in R_phys(n),
```

where `R_phys(n)` is a multiplicatively `B^o(1)`-short interval, together with

```text
E=n/(uv),
sqf(E) and E satisfying the inherited fixed squareclass/gcd masks,
all original orientation/root-origin/allocation/canonical/reverse-completion masks.
```

For fixed `n`, the candidate pair set remains `B^o(1)` because it is a reparametrization of the already charged fixed-`n` `(J1,a1,b1)` / `L` fiber.

The polynomial obstruction is therefore occupancy across many distinct `n`, not multiplicity of ratio candidates at one `n`.

```text
PRIMITIVE_RATIO_WINDOW_MULTIPLICATIVE_WIDTH=Bo1
FIXED_N_PRIMITIVE_RATIO_CANDIDATE_COUNT=Bo1
FIXED_N_RATIO_FIBER_RECHARGED=false
```

## 4. Material receiver change

Merged Work-brX30 leaves the common global/s heavy receiver as normalized radial squareclass divisor-window occupancy. The s-route has now resolved the moving divisor coordinate into its primitive projective content:

```text
L/n=u/v,
gcd(u,v)=1,
uv|n,
E=n/(uv).
```

The minimal s heavy receiver is therefore

```text
FixedPrimitiveRayFixedAgreementPairNormalizedRadialPrimitiveCoprimeDivisorRatioShortWindowPhysicalOccupancyWithMassExponentMuAtMostOneQuarterMinusPhi.
```

This is materially sharper than an unspecified squareclass-divisor window: it separates

```text
archimedean product-window feasibility
```

from

```text
arithmetic occupancy by a primitive coprime divisor ratio in a multiplicatively short window,
with the complementary dilation E carrying the retained squareclass/canonical masks.
```

A surviving heavy ray still requires at least

```text
B^(mu-o(1))
```

distinct accepted normalized `n`, with

```text
0<mu<=1/4-phi<=1/24.
```

No strict sub-square-root saving follows here.

```text
CURRENT_HEAVY_RAY_RECEIVER=FixedPrimitiveRayFixedAgreementPairNormalizedRadialPrimitiveCoprimeDivisorRatioShortWindowPhysicalOccupancyWithMassExponentMuAtMostOneQuarterMinusPhi
RECEIVER_MATERIALLY_CHANGED=true
```

## 5. H decision

No new `sH` is opened at this boundary. The coefficient system is now close to theorem shape, but one internal split remains necessary before an external audit is well posed: distinguish endpoint ratios (`u=1` or `v=1`, or one factor subpolynomial) from genuinely interior balanced primitive ratios, and freeze the exact weight inherited from the complementary dilation `E=n/(uv)` and canonical completion.

That is the natural `Stage14-s7-93` task. Existing non-heavy H gates remain separate and cannot be cross-promoted.

```text
S7_92_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_92=COMPLETE_RECIPROCAL_ROOT_WINDOWS_TO_SHORT_PRIMITIVE_DIVISOR_RATIO_OCCUPANCY_RECEIVER
ARCHIMEDEAN_RATIO_WINDOW_NONEMPTY_IFF_N_IN_PRODUCT_WINDOW=true
ARCHIMEDEAN_WINDOW_ALONE_FIXED_POWER_SAVING=false
PRIMITIVE_RATIO_WINDOW_MULTIPLICATIVE_WIDTH=Bo1
FIXED_N_PRIMITIVE_RATIO_CANDIDATE_COUNT=Bo1
CURRENT_HEAVY_RAY_RECEIVER=FixedPrimitiveRayFixedAgreementPairNormalizedRadialPrimitiveCoprimeDivisorRatioShortWindowPhysicalOccupancyWithMassExponentMuAtMostOneQuarterMinusPhi
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_92_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-93
```
