# Stage14-4ev — heavy-ray radial diffusion to exact quotient-line support

## Status

`COMPLETE_HEAVY_RAY_RADIAL_DIFFUSION_TO_EXACT_QUOTIENT_LINE_SUPPORT`

Consumes merged `Stage14-4eq..4eu`, merged `Stage14-s7-80`, merged `Stage14-Work-boX27`, and latest main `58ebe4a8312c74a7d909138c49472e1e4b0825e9`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

The only internal polynomial-common-core branch left by merged 4eu is the heavy primitive ray with polynomially many exact radial scales. Freeze the already charged data

```text
C,
(x,y), gcd(x,y)=1,
N0=x^2+y^2,
m0=N0/C,
```

and one finite sign/parity chart. Merged s7-80 gives exactly

```text
X=h*x,
Y=h*y,
2Q_xi=h(x+y),
2P_xi=h(x-y).
```

Hence the radial-diffusion family has only one polynomial coordinate `h`; `(P_xi,Q_xi)` are not an additional two-dimensional support. Merged 4eq gives a uniform `B^o(1)` full physical reverse fiber for each exact admissible `h`, and Work-boX27 shows that square-root saturation therefore requires polynomially many exact `h` values.

Define the charged physical radial support

```text
H_phys(C,x,y)
 := {h>=1 : the exact quotient-line point
      h/2*(x-y,x+y)
      admits a canonical physical completion}.
```

Then, after all once-charged divisor/sign/root labels,

```text
#heavy-ray physical incidences
 <= B^o(1) * #H_phys(C,x,y).
```

Thus the remaining heavy-ray obstruction is exactly the cardinality/density of `H_phys` inside its physical interval. No inner reconstruction entropy remains.

```text
HEAVY_RAY_ONLY_POLYNOMIAL_COORDINATE_IS_H=true
FIXED_H_FULL_PHYSICAL_FIBER=Bo1
HEAVY_RAY_RADIAL_SUPPORT_SET_DEFINED=true
RECEIVER_MATERIALLY_CHANGED=false
NEXT_H_NEEDED=false
NEXT=Stage14-4ew
```
