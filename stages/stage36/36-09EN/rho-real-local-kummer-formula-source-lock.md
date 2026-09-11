# Stage36 36-09EN — uniform real local Kummer formula

For every allowed primitive positive parameter, the translated rho model is

```text
y^2=X(X-P^2)(X-Q^2)
```

with three distinct real roots `0,P^2,Q^2`, all nonnegative and with `P,Q !=0`, `P^2!=Q^2`.

Use the EL Kummer pair

```text
delta_infinity(X,y)=([X],[X-P^2])
```

in `R^*/R^{*2}` sign bits.

For `X>max(P^2,Q^2)`, both coordinates are positive, giving the trivial class. For any

```text
0<X<min(P^2,Q^2),
```

the cubic has sign `(+)(-)(-)=+`, hence real points exist and the Kummer sign pair is exactly

```text
(0,1).
```

The real multiplication-by-two quotient has F2-dimension one for this three-real-root curve, so

```text
W_infinity=span{(0,1)}.
```

This formula is independent of the ordering of `P^2,Q^2` and of the parameter. Together with 36-09EM and the dyadic 36-09EN source, every local Kummer block required by the symbolic Sel2 matrix is explicitly fixed.
