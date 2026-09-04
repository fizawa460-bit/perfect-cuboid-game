# Stage35-EX 35EX-08 — simultaneous-square compatibility gives a third primitive Pythagorean triple

## Scope

Assume a Master-Hit is also an E1 counterexample. Keep the 35EX-02 notation

```text
c = gcd(U1,U2),
p = gcd(W1,V2),
q = gcd(V1,V2),
D = U1/c,
T = U2/c.
```

Let

```text
w = r^2+s^2,
H = u^2+v^2
```

be the primitive hypotenuses supplied by 35EX-03 for the E1 square and the Master square. This leaf uses both square norms simultaneously.

No theorem or receiver credit is claimed.

## 1. Raw square roots

The hypothetical E1 square has raw legs

```text
W1*U2,
U1*V2,
```

and canonical gcd `g0=c*p`. Hence its positive raw hypotenuse is

```text
c*p*w.
```

The Master square has raw legs

```text
V1*U2,
U1*V2,
```

and canonical gcd `h=c*q`. Its positive raw hypotenuse is

```text
c*q*H.
```

Therefore

```text
(W1*U2)^2 + (U1*V2)^2 = (c*p*w)^2,
(V1*U2)^2 + (U1*V2)^2 = (c*q*H)^2.
```

Subtract the second identity from the first. Since

```text
W1^2 - V1^2
 = (W1-V1)*(W1+V1)
 = (a-b)^2*(a+b)^2
 = U1^2,
```

we obtain

```text
(c*p*w)^2 - (c*q*H)^2 = U1^2*U2^2.
```

After division by `c^2`,

```text
(p*w)^2 = (q*H)^2 + (U1*U2/c)^2.
```

Using `U1=c*D`, `U2=c*T`, the odd leg is

```text
U1*U2/c = c*D*T.
```

Thus every E1 counterexample forces the branch-independent Pythagorean identity

```text
(q*H)^2 + (c*D*T)^2 = (p*w)^2.        (HB)
```

## 2. Exact gcd of the bridge legs

Set

```text
e = gcd(c,H).
```

We claim

```text
gcd(q*H, c*D*T) = e.
```

First, `q` is coprime to `c,D,T`:

- `gcd(q,c)=1` from 35EX-02;
- `q|V1` and `gcd(U1,V1)=1`, so `gcd(q,D)=1`;
- `q|V2` and `gcd(U2,V2)=1`, so `gcd(q,T)=1`.

Second, `H=u^2+v^2` is coprime to `D*T` in both 2-adic branches.

Branch L has

```text
u^2-v^2 = (V1/q)*T,
2*u*v   = D*(V2/q).
```

The primitive hypotenuse `H` is coprime to both `u^2-v^2` and `2uv`, hence to `T` and `D`.

Branch R has

```text
u^2-v^2 = D*(V2/q),
2*u*v   = (V1/q)*T,
```

so the same conclusion holds.

Therefore only the common factor of `H` and `c` remains, proving the claim.

Identity (HB) then implies `e | p*w`. Since `gcd(e,p)=1`, in fact

```text
e | w.
```

Thus `e` is a common divisor of `c,w,H`. Every odd prime dividing `e` divides a primitive Pythagorean hypotenuse and hence is `1 mod 4`.

## 3. Primitive bridge triple

Divide (HB) by `e^2` and put

```text
X = q*H/e,
Y = c*D*T/e = U1*U2/(c*e),
Z = p*w/e.
```

Then

```text
X^2 + Y^2 = Z^2,
gcd(X,Y)=1.
```

Moreover `X` is even while `Y,Z` are odd. Hence this is a primitive Pythagorean triple. There exist coprime integers

```text
alpha > beta > 0,
gcd(alpha,beta)=1,
alpha-beta odd,
```

such that

```text
q*H/e          = 2*alpha*beta,
U1*U2/(c*e)    = alpha^2-beta^2,
p*w/e          = alpha^2+beta^2.       (HB-param)
```

This is a third primitive parameter pair, forced by simultaneous E1 and Master squareness.

The even parameter among `(alpha,beta)` has exact 2-adic valuation

```text
v2(q)-1 = min(v2(V1),v2(V2))-1.
```

## 4. Equivalent double-square form

Because the primitive bridge triple has odd hypotenuse `Z` and even leg `X`, the two coprime odd integers `Z-X` and `Z+X` multiply to the square `Y^2`. Therefore each is itself a square.

Define

```text
A = alpha-beta,
B = alpha+beta.
```

Then `A,B` are positive odd and coprime, and

```text
p*w - q*H = e*A^2,
p*w + q*H = e*B^2,                     (HB-double-square)
A*B = U1*U2/(c*e).
```

Equivalently,

```text
p*(r^2+s^2) - q*(u^2+v^2) = e*A^2,
p*(r^2+s^2) + q*(u^2+v^2) = e*B^2.
```

This is the exact new compatibility supplied by the simultaneous-square/Gaussian lens: the two previous primitive hypotenuses are not independent; their `p,q`-weighted sum and difference are the same common factor `e` times two coprime odd squares.

## 5. Why this is new relative to 35EX-03..07

35EX-03 parameterized the E1 and Master squares separately and coupled their legs. 35EX-05..07 used the additive leg equations and exposed/froze the moving four-factor squareclass.

The bridge identity instead subtracts the two **full square norms** before reducing to factor-square data. Its output is a third primitive Pythagorean triple and the new coprime factorization

```text
A*B = U1*U2/(c*e).
```

No finite squareclass theorem follows yet, and no descent map has yet been proved. But this is a genuinely new exact constraint on every hypothetical E1 counterexample.

## Next exact leaf

```text
35EX-09_HYPOTENUSE_BRIDGE_FACTOR_ALLOCATION_AND_DESCENT_TEST
```

Required questions:

1. split the coprime product `A*B=U1*U2/(c*e)` against the primitive factorizations `(a-b)(a+b)` and `(m-n)(m+n)`;
2. determine exact prime-power allocation and 2-adic/sign constraints;
3. test whether `(alpha,beta)` yields a size-decreasing admissible counterexample or only another product rectangle;
4. if no descent follows, freeze the exact obstruction rather than claiming progress from a third parametrization alone.

## Credit boundary

```text
THIRD_PRIMITIVE_BRIDGE_TRIPLE_PROVED_CONDITIONALLY=true
HYPOTENUSE_DOUBLE_SQUARE_COMPATIBILITY_PROVED_CONDITIONALLY=true
INFINITE_DESCENT_PROVED=false
E1_PROVED=false
R29_PESCH_E1_CLOSED=false
R29_FIB2_CLOSED=false
J12_PARAMETRIC_CLOSED=false
STAGE35_CLOSED=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
