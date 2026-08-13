# tH22 refinement after Stage14-t78

If Stage14-tH22 has not yet started, retain the t77 requested object

```text
CanonicalGaussianPrimeProjectiveRayCharacterBalancedCoverBilinearLargeSieve
```

but import the following t78 reductions first.

```text
K_ext = K/gcd(K,k),
M = K/gcd(K,g*k) = K_ext/gcd(K_ext,g).
```

Hence the ray modulus is exactly the external squareclass support not absorbed by the fixed radial norm or angular gcd.  The radial-only case satisfies

```text
M=1 <=> K_ext|g.
```

A radial-only block with fixed-power `K_ext` is already contained in the t75 large-`g` branch, so tH22 should audit only `M>1` ray-active packets.

The angular gcd is already tensorized.  With

```text
d_AR=gcd(odd(A),odd(r)),
d_AT=gcd(odd(A),odd(t)),
d_BR=gcd(odd(Bdir),odd(r)),
d_BT=gcd(odd(Bdir),odd(t)),
```

the cells are pairwise coprime, their product is `g`, and exact gcd equality has the Möbius expansion

```text
1_{gcd(x,y)=d}
=1_{d|x}1_{d|y} sum_{e|x/d,e|y/d} mu(e).
```

Therefore the K-coprime cell allocation may be treated as separated direction/cover divisor coefficients.  Only the K-supported cell allocation affects `M`, with `B^o(1)` primewise orientation multiplicity.

Also use the exact cancellation

```text
c/odd(h)=R1*T1,
g*c=odd(h)*odd(r)*odd(t),
ell*g*c=ell*odd(h)*odd(r)*odd(t)<2B.
```

Thus tH22 no longer needs to decide whether angular-gcd allocation can be Möbius/divisor-switched into admissible coefficients; that exact algebraic tensorization is now proved.  The remaining questions are the actual Hecke/projective conductor, the nonprincipal ray-character large sieve, coefficient L2 norms after the divisor decomposition, and preservation of the dyadic/Mellin short-cover hyperbolas.

Do not charge `Q_rad` with artificial projective density, and do not reopen fixed-power radial-only external support.
