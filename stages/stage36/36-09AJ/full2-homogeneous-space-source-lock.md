# Stage36 36-09AJ source lock: full rational 2-descent homogeneous spaces

Accessed: 2026-09-07

## Primary source

David Roberts, *Explicit Descent On Elliptic Curves Over Function Fields*, §3.2.2, equations (3.5)–(3.8), University of Nottingham PhD thesis (2007):
https://johncremona.github.io/theses/roberts.pdf

Roberts writes a full-2 descent homogeneous space for

```text
E : y^2=(x-e1)(x-e2)(x-e3)
```

by choosing squareclasses `d1,d2,d3` with product a square and imposing

```text
x-e1*z0^2=d1*z1^2,
x-e2*z0^2=d2*z2^2,
x-e3*z0^2=d3*z3^2.
```

Taking differences gives the projective intersection of two quadrics

```text
d1*z1^2-d2*z2^2=(e2-e1)*z0^2,
d1*z1^2-d3*z3^2=(e3-e1)*z0^2.
```

Roberts then uses the representative `d3=d1*d2` after squareclass normalization. The construction is algebraic; the thesis notes that the number-field proof is the standard full-2 descent proof (citing Silverman, Chapter X, §1).

## Stage36 exact specialization

Write

```text
c = eta*2^e*C,
d = 2^f*D,
L = A*c*d,
T = A*B*c*d.
```

The audited 36-09AH common-u:v curve is

```text
A*u^2-B*v^2=c*r^2,
A*u^2+B*v^2=d*s^2.
```

Multiplying both equations by the same nonzero rational `L` gives exactly

```text
D1*u^2-D2*r^2=T*v^2,
D1*u^2-D3*s^2=-T*v^2,
```

where

```text
D1=A^2*c*d,
D2=A*c^2*d,
D3=A*c*d^2.
```

Moreover

```text
D1*D2*D3=(A*c*d)^4=L^4
```

is a rational square. Therefore, for the ordered-root model

```text
E_T : y^2=x*(x-T)*(x+T),
(e1,e2,e3)=(0,T,-T),
```

the Stage36 common-u:v curve is exactly the full-2 homogeneous space with squareclass triple

```text
([D1],[D2],[D3])=([c*d],[A*d],[A*c]).
```

Expanded in Stage36 variables:

```text
[d1]=[eta*2^(e+f)*C*D],
[d2]=[2^f*A*D],
[d3]=[eta*2^e*A*C].
```

Their product is trivial in `Q*/Q*^2`.

The audited 36-09AI model `E_n : Y^2=X^3-n^2*X` is obtained from `E_T` by rational square scaling of `x,y`; if `eta=-1` this also swaps the two nonzero ordered 2-torsion roots. Thus the unordered full-2 class is unchanged, while any ordered pair representation must record the possible `d2<->d3` transposition.

## Scope firewall

Identifying the `H^1(Q,E[2])` / full-2 homogeneous-space class does **not** prove that it lies in the 2-Selmer group. Selmer membership additionally requires local solubility of the full genus-one covering at every completion. It also does not prove that the class comes from `E(Q)/2E(Q)`, that the covering has a rational point, or that the receiver is empty/nonempty.
