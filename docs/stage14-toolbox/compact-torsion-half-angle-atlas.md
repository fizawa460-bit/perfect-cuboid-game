# Stage14 toolbox — compact torsion denominators and half-angle identities

This atlas is the reusable physical-side interface connecting the Stage14 elliptic witness to primitive Pythagorean half-angle arithmetic.

The guiding distinction is:

```text
generic rational witness denominator D
!= packet least denominator D_min
!= physical compact torsion denominators D_-, D_+.
```

The compact selectors are attached to the exact physical point and are invertible by rational 2-torsion translation. They therefore preserve physical reconstruction and avoid the existence-vs-coordinate quantifier gap that affected earlier relaxed witness counts.

## 1. Physical elliptic point and the first compact torsion translate

For a primitive oriented first face

```text
S^2+X^2=H^2
```

use

```text
E_{S,X}: W^2=Z(Z-S^2)(Z+X^2).
```

The physical point `P` lies on the unbounded real component `Z>S^2`. Translation by

```text
T0=(0,0)
```

is exactly

```text
Z(P+T0)=-S^2*X^2/Z(P),
W(P+T0)= S^2*X^2*W(P)/Z(P)^2.
```

It is an involution. Since `Z(P)>S^2`, the translated point lies on

```text
-X^2 < Z(P+T0) < 0,
```

the compact/nonidentity real component. Hence it is automatically nonzero in `E(Q)/2E(Q)`. Torsion translation preserves non-torsion and canonical height, and applying the same translation again recovers the physical point.

The compact sign chamber is `(--+)`. Only four sign/2-adic packets are needed:

```text
(-1,-1, 1),
(-2,-2, 1),
(-2,-1, 2),
(-1,-2, 2).
```

With `d0=-e0`, `d1=-e1`, `d2=e2`, the compact cover contains the positive-definite identities

```text
e2*u2^2+e0*u0^2=X^2*D^2,
e2*u2^2+e1*u1^2=H^2*D^2,
```

so `|u_i|<=B D` on the physical cutoff.

## 2. Physical two-face gluing and conjugate coordinates

Let the partner primitive oriented face be

```text
S2^2+X2^2=H2^2,
```

and put

```text
g=gcd(S,S2),
G=g*d.
```

For a physical edge,

```text
G^2=S^2*H2^2+X^2*S2^2
   =H^2*S2^2+S^2*X2^2.
```

Define

```text
R-=H2-S2,
N-=H*G-S^2*H2-X^2*S2,
Nphys=H*G+S^2*H2+X^2*S2.
```

Then

```text
Z_P=Nphys/R-,
Nphys*N-=S^2*X^2*(R-)^2,
Z_-=Z(P+T0)=-N-/R-.
```

The physical gap variables

```text
U=G-H*S2,
V=H*H2-G
```

satisfy

```text
U>0,
V>0,
U*(G+H*S2)=S^2*X2^2,
V*(H*H2+G)=X^2*X2^2,
U*V=(H2+S2)*N-,
Z_-=-U*V/X2^2.
```

Thus the compact denominator is controlled by the actual partner leg, not merely by a polynomial height box.

## 3. Exact minus-column denominator

Write the reduced denominator of `Z_-` as `D_-^2`. Then

```text
D_-^2=(H2-S2)/gcd(N-,H2-S2)
     =X2^2/gcd(X2^2,U*V).
```

In particular

```text
D_-^2 | H2-S2,
D_- | X2.
```

For the uniform half-angle coordinates

```text
H2+S2=kappa*s^2,
H2-S2=kappa*t^2,
X2=kappa*s*t,
kappa in {1,2},
gcd(s,t)=1,
```

we have

```text
D_- | t,
k_-:=t/D_-,
gcd(N-,H2-S2)=kappa*k_-^2.
```

So the compact denominator problem is exactly a denominator-versus-square-cancellation allocation on the minus half-angle column.

## 4. Complementary plus-column selector

Translate the same physical point by the other compact rational 2-torsion point

```text
T-=(-X^2,0).
```

Define

```text
R+=H2+S2,
N+=H*G+X^2*S2-S^2*H2.
```

Then the exact translated coordinate is

```text
Z_+=Z(P+T-)=-N+/R+
            =-(G+H*S2)*(H*H2-G)/X2^2.
```

If its reduced denominator is `D_+^2`, then

```text
D_+^2 | H2+S2=kappa*s^2,
D_+ | s,
k_+:=s/D_+,
gcd(N+,H2+S2)=kappa*k_+^2.
```

Thus the two invertible compact torsion translates see the two coprime half-angle columns symmetrically.

## 5. Dual product identity

Put

```text
Q=D_+*D_-,
K=k_+*k_-.
```

Since `D_+k_+=s` and `D_-k_-=t`,

```text
Q*K=s*t=X2/kappa.
```

Also

```text
k_+^2 | N+,
k_-^2 | N-,
K^2 | N+*N-.
```

Interpretation:

```text
Q = dual compact denominator product,
K = dual square-cancellation product.
```

This is an exact factorization identity, not a probabilistic split and not by itself a counting saving.

## 6. Good odd root-sign routing

Let `ell^e || X2` be odd and `ell ∤ H*S*X`. The gluing identity gives

```text
G == +H*S2 or -H*S2 (mod ell^(2e)).
```

The selector laws are complementary:

```text
ell^e | D_-  iff ell^(2e)|H2-S2 and G==-H*S2 mod ell^(2e),
ell^e | D_+  iff ell^(2e)|H2+S2 and G==+H*S2 mod ell^(2e).
```

The opposite sign is absorbed by the corresponding cancellation cofactor.

## 7. Third-face half-angle gcd matrix

The exact physical transfer produces a third primitive face `F3`. Write

```text
t2-=t_-(F2), t2+=t_+(F2),
t3-=t_-(F3), t3+=t_+(F3).
```

On odd prime powers of `X2` coprime to `2H`, define

```text
q--=gcd(t2-,t3-),
q-+=gcd(t2-,t3+),
q+-=gcd(t2+,t3-),
q++=gcd(t2+,t3+).
```

The four cells are pairwise coprime and

```text
q--*q-+*q+-*q++=X2_good.
```

The compact selectors occupy exactly two cells:

```text
(D_-)_good       = q-+,
(k_-)_good       = q--,
(D_+)_good       = q+-,
(k_+)_good       = q++.
```

Thus root signs are deterministic divisor allocation in a 2x2 gcd matrix. There is no free `2^{-omega}` density factor.

## 8. Fast dispatch

When a proof receives a physical pair `(F1,F2,d)`:

```text
1. compute g=gcd(S,S2), G=gd;
2. normalize F2 by kappa,s,t;
3. form N-,N+;
4. extract D_-,D_+ from reduced square denominators;
5. set k_-=t/D_-, k_+=s/D_+;
6. use QK=X2/kappa;
7. if prime-by-prime information is needed, transfer to F3 and use q--,q-+,q+-,q++.
```

Use `D_min` only for the historical abstract packet statistic. Use `D_-/D_+` for exact physical compact selectors.

## 9. Forbidden shortcuts

Do not use any of the following without an additional merged transfer theorem:

```text
large D_+ or D_- -> whole-family saving,
large Q -> two independent denominator savings,
large K -> automatic square-divisor density saving,
root sign -> independent Bernoulli probability,
D_min = D_- = D_+,
generic witness D = compact physical D_-/D_+,
compact torsion translation on E_{S,X} = s7 j=1728 twist torsion correspondence.
```

The exact formulas are reusable arithmetic structure. Their counting consequences depend on the quantifier scope of the receiving theorem.
