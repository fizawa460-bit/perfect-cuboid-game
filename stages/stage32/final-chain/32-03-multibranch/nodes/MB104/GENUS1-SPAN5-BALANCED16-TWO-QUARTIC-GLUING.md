# Stage32 MB104 — balanced16 two-zero-quartic gluing

Status: **RETAINED EXACT ALL-l CLOSURE OF ONE 768 SUPPORT ORBIT / SECOND 768 ORBIT SURVIVES / BALANCED16 OPEN / MB104 INCOMPLETE / NO CREDIT**

## Scope

This leaf continues only the displayed uniform genus-one support-span-five ray

```text
D_l = l A,
A = 7H - 4 sum_{i in Sigma} E_i,
|Sigma|=14,
l>=1.
```

The prior finite quotient leaves four balanced support orbits

```text
0000770000ff   size 48
00007b0000ff   size 48
000707000f0f   size 768
00070b000f0f   size 768.
```

The two size-768 orbits arise inside the representative incidence-16 hyperplane

```text
c = a1+a2+i*a3.
```

Its reduced section has two smooth elliptic quartics `Q1,Q2`, each generically doubled in the hyperplane section and each containing eight box nodes.  A balanced support contains seven nodes on each quartic.

## The two quartics and their intersection

Take

```text
Q1:
  a1+i*a3=0,
  b2=0,
  q1=q2=0;

Q2:
  a2+i*a3=0,
  b1=0,
  q1=q3=0.
```

On `Q1` use elliptic-quartic coordinates

```text
[x:y:z:w] = [a2:a3:b1:b3],
```

and on `Q2`

```text
[x:y:z:w] = [a1:a3:b2:b3].
```

In both cases

```text
z^2=x^2+y^2,
w^2=x^2-y^2.
```

The two quartics meet where

```text
a1=a2=-i*a3,
b1=b2=0,
b3^2=-2*a3^2,
c=-i*a3.
```

Thus over `Q(i,sqrt(2))` their intersection consists of the two reduced smooth points

```text
X_+ = [-i,-i,1,0,0,+i*sqrt(2),-i],
X_- = [-i,-i,1,0,0,-i*sqrt(2),-i].
```

In the above coordinates on either quartic,

```text
X_+ = [-i:1:0:+i*sqrt(2)],
X_- = [-i:1:0:-i*sqrt(2)].
```

The intersection is reduced because after imposing `x+i*y=0` and `z=0` the remaining equation is

```text
w^2+2*y^2=0,
```

which has the two distinct roots `w=+-i*sqrt(2)*y`.

Let

```text
Z = Q1 union Q2.
```

## Componentwise triviality

The previous Pic^0 leaf proves for every zero-pairing quartic `Q` that

```text
O_Q(A) ~= O_Q.
```

For one of these quartics, write its eight-node divisor as `B_Q`.  If `P` is the unique omitted box node, then

```text
B_Q ~ 2H_Q,
H_Q ~ 4P,
A|_Q ~ 7H_Q - 4(B_Q-P) ~ 0.
```

A concrete meromorphic trivialization can be chosen as follows.  Let `h` be one ambient hyperplane avoiding `X_+` and `X_-`; let `x,y` be the two coordinate hyperplanes whose zero divisors sum to `B_Q`; and let `ell_P` be the hyperflex plane with

```text
div_Q(ell_P)=4P.
```

Then

```text
g_Q = h^7 * ell_P / (x*y)^4
```

has divisor `A|_Q`.

At `X_+` and `X_-`, the common `h^7` factor cancels between `Q1,Q2`, and on both quartics `x*y=(-i)*1=-i`.  Therefore the line-bundle gluing parameter on `Z` is determined entirely by the hyperflex-plane values.

## Orbit `00070b000f0f`: nontrivial gluing for every l>=1

For the canonical representative support

```text
Sigma = 00070b000f0f,
```

the omitted box nodes are

```text
P1 on Q1: [x:y:z:w]=[0:1:-1:-i],
P2 on Q2: [x:y:z:w]=[0:1:-1:+i].
```

Corresponding hyperflex planes are

```text
ell1 = -2y-z+i*w,
ell2 = -2y-z-i*w.
```

At the two intersection points:

```text
ell1(X_+) = -2-sqrt(2),
ell1(X_-) = -2+sqrt(2),
ell2(X_+) = -2+sqrt(2),
ell2(X_-) = -2-sqrt(2).
```

If `t_+` and `t_-` are the transition constants between the two component trivializations at `X_+` and `X_-`, their invariant ratio is

```text
lambda = t_+/t_-
       = (ell1(X_+)*ell2(X_-))/(ell2(X_+)*ell1(X_-))
       = 17+12*sqrt(2)
       = (1+sqrt(2))^4.
```

This is a positive real number strictly greater than `1`, so

```text
lambda^l != 1
```

for every integer `l>=1`.

A section of `O_Z(D_l)` restricts, in the component trivializations, to constants `(c1,c2)` satisfying the two node-gluing equations

```text
c2 = t_+^l c1,
c2 = t_-^l c1.
```

Because `(t_+/t_-)^l=lambda^l!=1`, the only solution is

```text
c1=c2=0.
```

Hence exactly

```text
H^0(Z,O_Z(D_l)) = 0
```

for every `l>=1`.

Therefore every global section of `O_S(D_l)` vanishes on both `Q1` and `Q2`.  Both quartics are fixed components of every divisor in `|D_l|`.  Since `H.D_l=112l>4`, no divisor in this class can equal one quartic.  Thus the entire support orbit

```text
00070b000f0f   size 768
```

is excluded as an irreducible carrier for **all** `l>=1`.

## Orbit `000707000f0f`: gluing is trivial

For the other canonical representative

```text
Sigma = 000707000f0f,
```

the omitted nodes are

```text
P1 on Q1: [0:1:-1:-i],
P2 on Q2: [0:1:-1:-i].
```

The same hyperflex plane is used on both components, so

```text
lambda = 1.
```

Thus `O_Z(A)` is globally trivial on the two-component union, and so is `O_Z(D_l)` for every `l`.  This gluing argument does **not** force `Q1` or `Q2` into the fixed locus for this orbit.

## Consequence

The displayed uniform P5 ray hard core is reduced from four support orbits to three:

```text
0000770000ff   size 48   OPEN
00007b0000ff   size 48   OPEN
000707000f0f   size 768  OPEN
00070b000f0f   size 768  CLOSED for all l>=1.
```

This closure is specific to the displayed uniform ray.  It does not classify arbitrary unequal exceptional coefficients and does not close whole support-span five or MB104.

The next useful leaf should analyze the surviving `000707...` and the two size-48 orbits by simultaneous zero-quartic restriction/global jet interpolation; the already closed `00070b...` orbit should not be revisited.
