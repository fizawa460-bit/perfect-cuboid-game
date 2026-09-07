# Stage36 36-09AI source lock: Jacobian of a rank-3 quadric intersection

Accessed: 2026-09-07

## Primary source

Tom Fisher, *Visible 2-torsion in the Tate-Shafarevich group of an elliptic curve*, Section 3, Lemmas 3.1 and 3.2:
https://www.dpmms.cam.ac.uk/~taf1000/papers/visible2torsion.pdf

For quadratic forms `F,G` in four variables over a field of characteristic not 2 or 3:

- smoothness of `X={F=G=0} in P^3` is equivalent to the binary quartic `det(lambda F+mu G)` having no repeated factor;
- when `X` is smooth and `rank(F)=3`, `X` is a 2-covering of its Jacobian elliptic curve
  `y^2 = det(x F + G)`.

Fisher defines the determinant using the symmetric matrices of second partial derivatives.  For the Stage36 diagonal forms this differs from the determinant of the diagonal coefficient matrices by the factor `2^4=16`, which is a rational square.  The models are therefore related by the exact rational scaling of the `y` coordinate by 4.

## Stage36 specialization

Take

```text
F = Qminus = A*u^2-B*v^2-eta*2^e*C*r^2,
G = Qplus  = A*u^2+B*v^2-2^f*D*s^2.
```

The audited/36-09AH hypotheses make `rank(F)=3`, and 36-09AH directly certifies smoothness.  With the coefficient-matrix normalization,

```text
det(xF+G) = delta*x*(1-x^2),
delta = eta*2^(e+f)*A*B*C*D.
```

Thus the Jacobian has the exact rational model

```text
y^2 = delta*x*(1-x^2).
```

The rational change

```text
X = -delta*x,
Y = delta*y
```

gives

```text
Y^2 = X^3-delta^2*X.
```

Writing `N=A*B*C*D`, `g=(e+f) mod 2`, `n=2^g*N`, and `k=2^floor((e+f)/2)`, we have `|delta|=k^2*n`; the further rational scaling `X=k^2*X0`, `Y=k^3*Y0` gives the congruent-number form

```text
Y0^2 = X0^3-n^2*X0.
```

The sign `eta` disappears from the Jacobian coefficient because only `delta^2` occurs.

## Scope firewall

A 2-covering is not a birational equivalence over `Q` unless the torsor is shown soluble.  This source does not supply a rational point on the Stage36 common-`u:v` curve, does not trivialize its 2-covering class, and does not give Mordell-Weil rank or receiver emptiness.  Any later point transport must certify the actual covering map or an explicit rational adapter; model labels and matching `j` are insufficient.
