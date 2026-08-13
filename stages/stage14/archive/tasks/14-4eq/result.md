# Stage14-4eq — fixed-radial heavy-ray reverse fiber closure

## Status

`COMPLETE_FIXED_RADIAL_HEAVY_RAY_REVERSE_FIBER_CLOSURE`

Consumes merged `Stage14-4el..4ep`, merged `Stage14-s7-78..80`, merged `Stage14-X13`, merged `Stage14-q13`, and latest main `34d855de880c68a6e04ca6db650a14e7fe802e93`. Unmerged descendants are advisory only.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

Merged s7-80 splits the heavy primitive-ray branch into radial concentration and radial diffusion. Fix one exact concentrated reciprocal tuple

```text
C,
(x,y), gcd(x,y)=1,
h,
X=h*x,
Y=h*y,
X=p*c,
Y=q*d.
```

For fixed `h,x,y`, the raw pair `(X,Y)` is fixed. The divisor factorizations `(p,c)` and `(q,d)` are `B^o(1)` by s7-79.

Now use the exact second reciprocal identity from X13:

```text
X^2-Y^2
 = 4*Xr*Yr*epsilon_x*U*V,
```

where `Xr,Yr` are the physical root products and `(U,V)` is the primitive xi-agreement pair. Since `X>Y>0`, the positive integer

```text
W2:=X^2-Y^2
```

is fixed. For fixed finite 2-primary data, the tuples `(Xr,Yr,U,V)` form only a subset of the ordered factorizations of `W2/4`, hence have multiplicity `B^o(1)`.

The endpoint-small factors `(r,s)` and finite sign data then give only `B^o(1)` possible

```text
M=4*r*s*Xr*Yr*epsilon_x*epsilon_k.
```

Thus the previously missing stronger reverse packet is recovered legally:

```text
fixed reciprocal tuple
 => #(U,V,M)=B^o(1).
```

Only now invoke merged X13 in its proved direction:

```text
fixed (U,V,M)
 => full signed-reciprocal / post-column physical reconstruction = B^o(1).
```

Therefore

```text
FIXED_RECIPROCAL_DATA_TO_CANONICAL_BACKGROUND_FIBER_BOUND=Bo1
FIXED_EXACT_H_HEAVY_RAY_REVERSE_FIBER=Bo1
HEAVY_RAY_RADIAL_CONCENTRATION_BRANCH_CLOSED=true
```

This does **not** close the radial-diffusion branch. Polynomially many exact `h` values may still be needed on one fixed primitive ray, and the above argument gives only `B^o(1)` fiber for each individual `h`.

Remaining heavy-ray receiver:

```text
FixedPrimitiveReciprocalRayDiffuseRadialScalePhysicalIncidence.
```

```text
STAGE14_4EQ=COMPLETE_FIXED_RADIAL_HEAVY_RAY_REVERSE_FIBER_CLOSURE
MERGED_S7_78_80_CONSUMED=true
FIXED_RECIPROCAL_DATA_TO_CANONICAL_BACKGROUND_FIBER_BOUND=Bo1
HEAVY_RAY_RADIAL_CONCENTRATION_BRANCH_CLOSED=true
HEAVY_RAY_RADIAL_DIFFUSION_BRANCH_RETAINED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=true
NEXT=Stage14-4er
```
