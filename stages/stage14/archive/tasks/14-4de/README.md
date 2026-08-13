# Stage14-4de

Stage14-4de consumes merged `Stage14-4dd`, merged `Stage14-X14`, and the closed-route certificate `Stage14-s7-45`.

The entering whole-family theorem is

```text
V(B) << B^(1/2+o(1)).
```

On every possible square-root-saturating packet,

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
u_res=B^(1/4-chi+o(1)),
P,Q,P+Q,P-Q=B^(1/4+o(1)).
```

Write

```text
D=delta*s,
A=alpha*r,
H_+=D^2+A^2,
H_-=D^2-A^2.
```

Merged X14 / 4cg identify the odd plus factor as `C*S*T` up to the already-frozen `B^o(1)` decorations, while merged s7-27 identifies the odd minus factor as `R*J*u_res`.

Since

```text
gcd(H_+,H_-) | 2*gcd(D,A)^2
```

and `gcd(D,A)=B^o(1)`, the plus and minus factors have only subpolynomial common odd support. In particular

```text
gcd(C,u_res)=B^o(1),
gcd(S*T,u_res)=B^o(1).
```

After the corresponding `B^o(1)` gcd/unit peels, define coprime odd factors

```text
C_* ~ C,
u_* ~ oddpart(u_res),
Q_mix=C_* u_*.
```

Square-root saturation gives

```text
Q_mix=B^(1/4+o(1)).
```

Moreover, for the primitive ratio `t=D/A (mod Q_mix)`, one has

```text
t^2 == -1 mod C_*,
t^2 == +1 mod u_*,
```

hence

```text
t^4 == 1 mod Q_mix.
```

Because the modulus is odd,

```text
C_* = gcd(Q_mix,t^2+1),
u_* = gcd(Q_mix,t^2-1),
```

so the common-core / signed-residual prime-power allocation is recovered from the mixed fourth-root label itself.

This does not yet improve the exponent: `Q_mix` costs `1/4` and a primitive quarter-by-quarter root-line lift costs another `1/4`. The whole-family bound remains `1/2`.

However this is a genuinely new exact bridge back to the s-specific signed-residual coordinates which did not exist when `s7-45` closed the route. Under the merged roadmap reactivation rule:

```text
MATERIAL_RECEIVER_CHANGE_REQUIRES_S_REACTIVATION_CHECK=true
S_ROUTE_REACTIVATION_NEEDED=true
S_ROUTE_REACTIVATION_TRIGGER=FULL_RESIDUAL_CROSS_GCD_AND_MIXED_FOURTH_ROOT_COMPRESSION
S_ROUTE_REACTIVATION_TARGET=Stage14-s7-46
```

The reactivated s target is

```text
SquareRootQuarterScaleMixedFourthRootSignedResidualPhysicalCompletionIncidence.
```

No new mainline H is requested in 4de; the new exact structure must be consumed first. Next mainline stage: `Stage14-4df`.