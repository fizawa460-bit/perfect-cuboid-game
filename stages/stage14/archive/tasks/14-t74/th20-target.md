# Stage14-t74 — revised tH20 target

Pre-t74 target:

```text
SmallOddKappaFixedTagMovingCanonicalLargestPrimeSmoothNormValueSieve
```

Post-t74 minimal target:

```text
SmallOddKappaFixedTagCanonicalPrimeShortAngularCofactorHyperbolaSieve
```

Reason: t74 proves

```text
Q=Pminus/ell,
c=odd(Q)=odd(h)*R_V,
h*D_V*Pplus=epsilon*delta*D_pi*Q,
ell*c<2B,
ell*g*c<2B,
q-p,q+p<sqrt(ell),
h*ell*((q-p)^2+(q+p)^2)<=4B,
fixed (U,epsilon,k,h,ell,c) fiber=B^o(1).
```

Thus fixed-norm Pell orbit, class number, regulator, the 2-adic part of `Pminus`, and the positive companion are not independent fixed-power coordinates after `(ell,c)` is fixed.

The tH20 audit should seek a uniform saving for the moving `(ell,c)` / primitive-cover incidence while retaining fixed `(U,kappa,beta)`, the two root hosts, both hyperbolas, short factorization, reconstructed positive-companion predicate, and `ell*delta<=Y_U`.

```text
TH20_NEEDED=true
TH20_PRE_T74_TARGET_MINIMAL=false
TH20_REQUESTED_OBJECT=SmallOddKappaFixedTagCanonicalPrimeShortAngularCofactorHyperbolaSieve
T_ROUTE_BLOCKED_WAITING_FOR_TH20=false
```
