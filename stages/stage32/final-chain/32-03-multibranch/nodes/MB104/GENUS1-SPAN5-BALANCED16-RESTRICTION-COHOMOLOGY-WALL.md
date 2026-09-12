# Stage32 MB104 — balanced16 restriction-map cohomology wall

Status: **RETAINED EXACT COHOMOLOGY REDUCTION / DIRECT KV ROUTE BLOCKED / BALANCED16 OPEN / MB104 INCOMPLETE / NO CREDIT**

## Scope

Work only with the displayed uniform genus-one support-span-five ray

```text
D_l = 7l H - 4l sum_{i in Sigma} E_i,  |Sigma|=14,  l>=1,
```

on one of the four balanced incidence-16 support orbits.  Let `Q` be one of the retained zero-pairing smooth elliptic quartics.  The previous Pic^0 leaf proves

```text
H.Q = K_S.Q = 4,
g(Q)=1,
D_l.Q=0,
O_Q(D_l) ~= O_Q.
```

Every balanced support has at least two zero-pairing elliptic quartics.

## 1. Exact Riemann--Roch reduction

Adjunction on the smooth elliptic quartic gives

```text
0 = 2g(Q)-2 = Q.(Q+K_S) = Q^2+4,
```

hence

```text
Q^2=-4.
```

The retained Picard ray has

```text
D_l^2=336l^2,
K_S.D_l=H.D_l=112l,
K_S^2=16,
chi(O_S)=8.
```

Therefore

```text
chi(O_S(D_l))
 = 8 + (D_l^2-K_S.D_l)/2
 = 168l^2-56l+8.
```

Because `D_l.Q=0`, `Q^2=-4`, and `K_S.Q=4`,

```text
(D_l-Q)^2 = 336l^2-4,
K_S.(D_l-Q)=112l-4,
```

so exactly

```text
chi(O_S(D_l-Q)) = chi(O_S(D_l)).
```

Since `H=K_S` is nef,

```text
H.(K_S-D_l)=16-112l < 0,
H.(K_S-D_l+Q)=20-112l < 0.
```

Thus neither `K_S-D_l` nor `K_S-D_l+Q` can be effective, and Serre duality gives

```text
H^2(S,O(D_l))=0,
H^2(S,O(D_l-Q))=0.
```

## 2. Restriction rank is exactly an H^1 question

Use

```text
0 -> O(D_l-Q) -> O(D_l) -> O_Q -> 0.
```

Let

```text
r = rank( H^0(S,O(D_l)) -> H^0(Q,O_Q) ) in {0,1}.
```

Exactness and the two `H^2=0` statements give

```text
h^0(D_l) = h^0(D_l-Q) + r,
h^1(D_l) = h^1(D_l-Q) + r.
```

Moreover `H^1(D_l) -> H^1(O_Q)` is surjective, because the next group is `H^2(D_l-Q)=0`.  Hence

```text
h^1(D_l) >= 1.
```

So the balanced ray is necessarily special.  In particular,

```text
H^1(D_l-Q)=0  ==>  r=1,
```

which would prove that `Q` is not a fixed component.  Conversely, Riemann--Roch alone cannot decide `r`, because both Euler characteristics are equal.

## 3. The unique omitted exceptional curve is forced in |D_l-Q|

A zero quartic contains eight box nodes and the balanced support contains exactly seven of them.  Let `P` be the unique omitted node and `E_P` its exceptional curve.  Then

```text
D_l.E_P=0,
Q.E_P=1,
E_P^2=-2,
```

hence

```text
(D_l-Q).E_P=-1.
```

Therefore every effective divisor in `|D_l-Q|` contains `E_P`.  Also

```text
O_{E_P}(D_l-Q) ~= O_{P^1}(-1),
```

which is acyclic.  The exact sequence along `E_P` therefore gives canonical cohomology isomorphisms

```text
H^i(D_l-Q-E_P) ~= H^i(D_l-Q),  i=0,1,2.
```

Thus stripping the forced `E_P` does not solve the restriction-map question; it merely removes an acyclic fixed component from the auxiliary linear system.

## 4. Direct Kawamata--Viehweg vanishing is impossible on this leaf

The most direct attempt writes

```text
D_l-Q = K_S + L,
L = D_l-Q-K_S.
```

But

```text
L.E_P=-1,
```

so `L` is not nef.

More importantly, every balanced support has another zero-pairing elliptic quartic `R != Q`.  Since distinct irreducible curves have nonnegative intersection,

```text
D_l.R=0,
K_S.R=4,
Q.R>=0,
```

and therefore

```text
L.R = -4-Q.R < 0.
```

Hence the direct Kawamata--Viehweg route fails on **all four balanced support orbits**, independently of the exceptional-curve issue.

Stripping the forced exceptional curve does not repair this.  For

```text
L_E = D_l-Q-E_P-K_S,
```

one still has, for every other zero quartic `R`,

```text
L_E.R = -4-Q.R-E_P.R < 0.
```

A second exact-sequence attempt uses

```text
0 -> O(D_l-2Q-E_P) -> O(D_l-Q-E_P)
   -> O_Q(D_l-Q-E_P) -> 0,
```

where the restriction on `Q` has degree `3`.  If `H^1(D_l-2Q-E_P)=0`, this would imply `H^1(D_l-Q)=0`.  However the corresponding adjoint residual

```text
N = D_l-2Q-E_P-K_S
```

still satisfies, for another zero quartic `R`,

```text
N.R = -4-2Q.R-E_P.R < 0.
```

So the obvious one-quartic Kawamata--Viehweg ladder is structurally blocked by the **simultaneous zero-quartic configuration**.

## Consequence

The restriction problem has been sharpened to the following exact form:

```text
restriction nonzero
<=> rank r=1
<=> h^1(D_l)=h^1(D_l-Q)+1.
```

A sufficient condition is `H^1(D_l-Q)=0`, but direct nef+big vanishing cannot establish it because another zero quartic always gives a negative intersection.

The next useful input must therefore treat the zero quartics simultaneously, for example:

1. the restriction map to the **union** of all zero quartics and its gluing conditions;
2. explicit global jet interpolation on the canonical model;
3. a semiampleness/effective-cone theorem controlling the whole null locus rather than one quartic at a time.

This leaf does not prove that the restriction map is zero or nonzero.  It does not close balanced16, span5, MB104, or any receiver/theorem/endpoint claim.
