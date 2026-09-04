# Stage35-EX 35EX-17B — fresh Gaussian coordinate-gcd hook

## Scope

This is the exact new pattern isolated by the post-35EX-17 breadth audit. It does not prove E1. It only source-locks the next receiver for 35EX-18.

Put

```text
zminus = (a*m-b*n) + i*(a*n-b*m),
zplus  = (a*m+b*n) + i*(a*n+b*m),
```

and

```text
gminus = gcd(a*m-b*n, a*n-b*m),
gplus  = gcd(a*m+b*n, a*n+b*m).
```

As usual

```text
c=gcd(U1,U2), p=gcd(W1,V2), d=gcd(V1,W2).
```

All gcds below are positive.

## 1. Exact norms

Direct expansion gives

```text
Norm(zminus)=W1*W2-V1*V2=p*d*Lminus,
Norm(zplus) =W1*W2+V1*V2=p*d*Lplus.            (NORM)
```

Thus the two exact coprime receiver factors already occur as norms of two explicit source Gaussian integers.

## 2. The coordinate gcds split `c` exactly

First `gminus|c`. If a prime power `ell^e` divides both coordinates of `zminus`, then

```text
m*(a*m-b*n)-n*(a*n-b*m)=a*U2,
n*(a*m-b*n)-m*(a*n-b*m)=-b*U2.
```

Since `gcd(a,b)=1`, `ell^e|U2`. Likewise

```text
a*(a*m-b*n)+b*(a*n-b*m)=m*U1,
b*(a*m-b*n)+a*(a*n-b*m)=n*U1,
```

and `gcd(m,n)=1`, so `ell^e|U1`. Hence `gminus|c`. The same calculation with plus signs gives `gplus|c`.

Because `c` is odd, let `ell^e||c`. Primitivity implies `ell` divides none of `a,b,m,n`. From

```text
a^2 == b^2 (mod ell^e),
m^2 == n^2 (mod ell^e)
```

and odd-prime-power uniqueness of the two roots of `X^2=1`, there are signs `epsilon,delta in {+1,-1}` with

```text
a == epsilon*b (mod ell^e),
m == delta*n   (mod ell^e).
```

If `epsilon=delta`, both coordinates of `zminus` vanish modulo `ell^e`; if `epsilon=-delta`, both coordinates of `zplus` vanish modulo `ell^e`. Therefore every prime power of `c` goes wholly into exactly one of `gminus,gplus`.

No odd prime can divide both `gminus` and `gplus`: otherwise sums and differences would force it to divide both members of one primitive parameter pair. Consequently

```text
gcd(gminus,gplus)=1,
gminus*gplus=c.                                (GSPLIT)
```

## 3. Full receiver gives two primitive `p*d`-twisted square norms

Assume the full E1 receiver

```text
Lminus=x^2,
Lplus=y^2.
```

Since `gminus^2|Norm(zminus)=p*d*x^2` and `gminus|c`, while `gcd(c,p*d)=1`, we get `gminus|x`. Similarly `gplus|y`.

Define

```text
X=x/gminus,
Y=y/gplus,
zminus0=zminus/gminus,
zplus0 =zplus/gplus.
```

By definition of the coordinate gcds, `zminus0` and `zplus0` are primitive Gaussian integers: their real and imaginary coordinates are coprime. By `(NORM)` and `(GSPLIT)`,

```text
Norm(zminus0)=p*d*X^2,
Norm(zplus0) =p*d*Y^2.                         (TWIST)
```

Every odd prime dividing `p` divides the primitive hypotenuse `W1`; every odd prime dividing `d` divides the primitive hypotenuse `W2`. Hence every prime in `supp(p*d)` is `1 mod 4`. The residual nonsquare Gaussian squareclass support in `(TWIST)` is therefore split-prime support carried by the moving source quantity `p*d`.

## 4. Relation to earlier Gaussian work

This does not revive the dominated 35EX-13 scalar ratio as a separate receiver. 35EX-13 proved its rational square test is exactly `Lminus=square`; 35EX-14 absorbed that scalar condition.

The new information here is coordinate-level: **both** explicit Gaussian norm forms are made primitive by an exact coprime split of `c`, after which both have the same rational norm twist `p*d` modulo squares.

The next legal question is therefore not whether the scalar 35EX-13 ratio is square again. It is whether the normalized Master Gaussian square constrains the relative split-prime orientation of `zminus0,zplus0` strongly enough to contradict the full receiver, or whether those orientations remain moving/free.

## Exact boundary

```text
GAUSSIAN_COORDINATE_GCD_SPLIT_PROVED=true
GMINUS_GPLUS_EQUALS_C=true
GMINUS_GPLUS_COPRIME=true
FULL_RECEIVER_PRIMITIVE_PD_TWISTED_NORMS_PROVED=true
PD_ODD_PRIME_SUPPORT_SPLIT_ONLY=true
MASTER_GAUSSIAN_FORCES_ORIENTATION_CONTRADICTION=false
E1_PROVED=false
```

No finite squareclass family, fixed support, receiver closure, infinite descent, Stage35 closure, or endpoint claim follows from this hook alone.
