# Stage14-4df

Stage14-4df consumes merged `Stage14-4de` and refines the only possible square-root equality packet.

Stage14-4de writes, after only `B^o(1)` endpoint/unit peels,

```text
H_+=D^2+A^2,
H_-=D^2-A^2,
H_+ = C_* X_* * B^o(1),
H_- = u_* R_* * B^o(1),
Q_mix=C_*u_*=B^(1/4+o(1)),
```

where `X_*` denotes the odd xi-switch product `S*T` and `R_*` the odd xi-agreement product `R*J`.  Merged 4de already proves every plus/minus cross gcd is `B^o(1)`.

The new step is to keep the two same-side overlaps

```text
W_+ = gcd(C_*,X_*),
W_- = gcd(u_*,R_*).
```

They cost no fixed power after `(C_*,u_*)` is fixed because `W_+|C_*` and `W_-|u_*`.  But the exact factorizations imply

```text
C_* W_+ | H_+,
u_* W_- | H_-.
```

Hence the 4de mixed-root congruence automatically lifts from `Q_mix` to

```text
Q_eff := C_*u_*W_+W_-,
t^2=-1 mod C_*W_+,
t^2=+1 mod u_*W_-,
t^4=1 mod Q_eff.
```

If

```text
W_+=B^(w_++o(1)),
W_-=B^(w_-+o(1)),
```

then the primitive `(D,A)` root-line fiber loses exactly `w_++w_-` in exponent while the overlap choices remain divisor-many.  Therefore

```text
E_4df(w_+,w_-) <= 1/2-w_+-w_-.
```

Every fixed-power same-side overlap is strict sub-square-root.  Consequently square-root saturation requires

```text
gcd(C_*,X_*)=B^o(1),
gcd(u_*,R_*)=B^o(1).
```

Together with the cross-coprimality from 4de, the four norm blocks

```text
C_*, X_*=oddpart(S*T), u_*, R_*=oddpart(R*J)
```

are pairwise separated at fixed-power scale.

No strict whole-family improvement is claimed: the zero-overlap stratum still has exponent `1/2`.

The refined mainline receiver is

```text
SquareRootQuarterScalePairwiseSeparatedMixedFourthRootFullResidualPhysicalCompletionDensity.
```

The s-route reactivation test remains **true**.  The new `W_- = gcd(u_*,R_*)` peel is directly in the signed-residual / agreement coordinates owned by the s route, so `Stage14-s7-46` remains the correct restart stage with the refined receiver

```text
SquareRootQuarterScalePairwiseSeparatedMixedFourthRootSignedResidualPhysicalCompletionIncidence.
```

No new mainline H is needed.  Next mainline stage: `Stage14-4dg`.