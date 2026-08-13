# Stage14-4ew — radial scale as square factor in the second reciprocal difference

## Status

`COMPLETE_RADIAL_SCALE_SQUARE_FACTOR_EXPOSURE`

Consumes Stage14-4ev and merged X13 exact reciprocal identities.

On the fixed primitive ray,

```text
X=h*x,
Y=h*y.
```

Therefore the raw opposite-reciprocal difference of squares is exactly

```text
W2:=X^2-Y^2=h^2*(x^2-y^2).
```

Merged X13 identifies the same integer with

```text
W2=4*Xr*Yr*epsilon_x*U*V,
```

where `(U,V)` is the primitive xi-agreement pair and the remaining root/2-primary labels are charged once. Consequently every accepted radial scale satisfies

```text
h^2*(x^2-y^2)
 = 4*Xr*Yr*epsilon_x*U*V.                 (1)
```

This is not a fresh divisor bound: the right side moves with the canonical background, so one may not fix it while counting diffuse `h`. But (1) proves that radial diffusion is equivalent to polynomial variation of an exact square divisor inside the moving second-reciprocal product. In particular `h` is not a free archimedean dilation independent of the arithmetic packet.

After peeling the fixed primitive-ray factor `x^2-y^2`, define

```text
R_h := 4*Xr*Yr*epsilon_x*U*V/(x^2-y^2)=h^2.
```

Physical radial support is therefore a square-value support of the moving canonical reciprocal product, with `B^o(1)` fiber over each exact square value by merged 4eq.

```text
RADIAL_SCALE_ENTERS_AS_EXACT_SQUARE_FACTOR=true
RADIAL_DIFFUSION_IS_MOVING_SQUARE_VALUE_SUPPORT=true
RIGHT_SIDE_FIXED_FOR_DIFFUSE_COUNT=false
FRESH_DIVISOR_SAVING_CLAIMED=false
RECEIVER_MATERIALLY_CHANGED=false
NEXT_H_NEEDED=false
NEXT=Stage14-4ex
```
