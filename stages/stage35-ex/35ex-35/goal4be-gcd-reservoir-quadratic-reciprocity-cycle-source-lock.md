# Stage35-EX Goal4BE source lock — gcd-reservoir quadratic-reciprocity cycle

Scope: continue the Goal4BC fresh-view program after exact-green Goal4BD. Audited authority remains V74 / Goal4AK. Goal4BE asks whether the exact AU reservoirs `h_a,h_b,h_c` carry a quadratic-reciprocity constraint that is genuinely stronger than the already-known Kummer squareclass product `d_A*d_B*d_C=1`. The answer is **yes at the level of one new Jacobi consistency cycle, but no branch pruning yet**: ordinary quadratic reciprocity produces a second rank-two shadow with one unresolved pairwise-symbol bit.

## 1. Exact AU source dictionary

Retain

```text
A=x*y*a,
B=x*z*b,
C=y*z*c,
```

with

```text
gcd(x,y)=gcd(x,z)=gcd(y,z)=1,
gcd(a,b)=gcd(a,c)=gcd(b,c)=1,
gcd(a,z)=gcd(b,y)=gcd(c,x)=1.
```

The reduced primitive Pythagorean faces are

```text
r_AB^2=(y*a)^2+(z*b)^2,
r_AC^2=(x*a)^2+(z*c)^2,
r_BC^2=(x*b)^2+(y*c)^2.                              (BE-FACE)
```

All three reduced hypotenuses are odd. Goal4AU defines

```text
h_a=gcd(a,r_BC),
h_b=gcd(b,r_AC),
h_c=gcd(c,r_AB),                                     (BE-H)
```

and the stripped integers

```text
a0=a/h_a,
b0=b/h_b,
c0=c/h_c.
```

The three marked Kummer classes are

```text
d_A=kappa_A*[b0*c0],
d_B=kappa_B*[a0*c0],
d_C=kappa_C*[a0*b0],
```

with `d_A*d_B*d_C=1` in `Q*/Q*^2`.

## 2. Reservoir primes are 1 modulo 4

Let `ell` be an odd prime dividing `h_a`. Then `ell|a` and `ell|r_BC`.

First `ell` cannot divide `x`: if it did, `(BE-FACE)` modulo `ell` would give `ell|y*c`, contradicting `gcd(x,y)=gcd(c,x)=1`. Likewise `ell` cannot divide `y`, using `gcd(x,y)=gcd(b,y)=1`. Since `ell|a` and `a` is coprime to `b,c,z`, all of

```text
x,y,z,b,c
```

are `ell`-adic units.

Reducing the `BC` face gives

```text
(x*b)^2+(y*c)^2=0 (mod ell),
```

hence

```text
((x*b)/(y*c))^2=-1 (mod ell).                         (BE-Ia)
```

Therefore `-1` is a quadratic residue modulo `ell`, so

```text
ell = 1 (mod 4).                                      (BE-1mod4)
```

The same argument applies cyclically to every odd prime of `h_b` or `h_c`.

The reservoirs are pairwise coprime because they divide the pairwise-coprime integers `a,b,c`. They also divide the space diagonal: for example `h_a|A` and `h_a|D_BC`, hence from

```text
W^2=A^2+D_BC^2
```

one gets `h_a|W`; cyclically the same holds for `h_b,h_c`. Thus

```text
gcd(h_a,h_b)=gcd(h_a,h_c)=gcd(h_b,h_c)=1,
h_a*h_b*h_c | W,                                     (BE-W)
```

and every odd prime in this product is `1 mod 4`.

## 3. Primewise Legendre constraints

For `ell|h_a`, equation `(BE-Ia)` gives a source-selected square root of `-1`:

```text
iota_a(ell) = x*b/(y*c) (mod ell),
iota_a(ell)^2=-1.                                    (BE-iota-a)
```

For a prime `ell=1 mod4`, either root of `-1` has Legendre symbol

```text
(iota_a(ell)/ell)=(-1)^((ell-1)/4)=(2/ell).
```

Taking Legendre symbols in `(BE-iota-a)` therefore yields

```text
(x*y*b*c/ell)=(2/ell),
(2*x*y*b*c/ell)=1.                                   (BE-La-prime)
```

Cyclically,

```text
ell|h_b => (2*x*z*a*c/ell)=1,
ell|h_c => (2*y*z*a*b/ell)=1.                        (BE-Lcyc-prime)
```

These are exact necessary local conditions on every physical endpoint.

## 4. Pass to the squarefree parity kernels

Let

```text
s_a = squarefree positive representative of [h_a],
s_b = squarefree positive representative of [h_b],
s_c = squarefree positive representative of [h_c].  (BE-S)
```

Equivalently, `s_a` is the product of those primes whose valuation in `h_a` is odd, and similarly cyclically. All primes of `s_a,s_b,s_c` are `1 mod4`, and the three integers are pairwise coprime.

Multiplying `(BE-La-prime)` only over primes occurring in `s_a` gives the Jacobi relation

```text
(2*x*y*b*c / s_a)=1.                                 (BE-Ja-raw)
```

Here and below the symbol is `1` by convention when the denominator is `1`. Cyclically,

```text
(2*x*z*a*c / s_b)=1,
(2*y*z*a*b / s_c)=1.                                 (BE-Jraw)
```

Since

```text
h_a=s_a*t_a^2,
h_b=s_b*t_b^2,
h_c=s_c*t_c^2
```

for integers `t_i`, substitute `a=h_a*a0`, `b=h_b*b0`, `c=h_c*c0`. Define

```text
L_a=(2*x*y*b0*c0 / s_a),
L_b=(2*x*z*a0*c0 / s_b),
L_c=(2*y*z*a0*b0 / s_c).                             (BE-L)
```

Then `(BE-Jraw)` is equivalent to

```text
L_a*(s_b/s_a)*(s_c/s_a)=1,
L_b*(s_a/s_b)*(s_c/s_b)=1,
L_c*(s_a/s_c)*(s_b/s_c)=1.                           (BE-SYM)
```

## 5. Quadratic reciprocity produces one new global cycle

Because every prime of every `s_i` is `1 mod4`, quadratic reciprocity has no antisymmetric sign:

```text
(s_a/s_b)=(s_b/s_a),
(s_a/s_c)=(s_c/s_a),
(s_b/s_c)=(s_c/s_b).                                 (BE-QR)
```

Multiplying the three equations `(BE-SYM)` makes every cross-reservoir symbol occur twice and cancel. Therefore

```text
L_a*L_b*L_c=1.                                       (BE-CYCLE)
```

Explicitly,

```text
(2*x*y*b0*c0 / s_a)
*
(2*x*z*a0*c0 / s_b)
*
(2*y*z*a0*b0 / s_c)
=1.                                                   (BE-CYCLE-explicit)
```

This is a genuine new source-derived Jacobi consistency condition. It is not the rational-squareclass identity `d_A*d_B*d_C=1`: it evaluates three stripped Kummer/source expressions at three different reservoir squarefree kernels.

Using the literal AU representatives

```text
D_A=k_A*b0*c0,
D_B=k_B*a0*c0,
D_C=k_C*a0*b0,
```

and `epsilon_i*k_i=2`, the same cycle is

```text
(epsilon_A*x*y*D_A / s_a)
*
(epsilon_B*x*z*D_B / s_b)
*
(epsilon_C*y*z*D_C / s_c)
=1.                                                   (BE-CYCLE-d)
```

Thus Goal4BE couples the marked Kummer layer back to the exact gcd reservoirs through Jacobi evaluation.

## 6. The reciprocity system still has rank two

Set the symmetric pairwise reservoir symbols

```text
u_ab=(s_a/s_b)=(s_b/s_a),
u_ac=(s_a/s_c)=(s_c/s_a),
u_bc=(s_b/s_c)=(s_c/s_b).                                  (BE-U)
```

Then `(BE-SYM)` becomes

```text
u_ab*u_ac=L_a,
u_ab*u_bc=L_b,
u_ac*u_bc=L_c.                                        (BE-R2)
```

Over `F_2` signs, this is the matrix

```text
1 1 0
1 0 1
0 1 1
```

of rank `2`, with kernel generated by `(1,1,1)` in additive sign coordinates. The sole consistency condition is exactly `(BE-CYCLE)`.

Consequently ordinary quadratic reciprocity does **not** determine all three pairwise reservoir symbols. Once `(BE-CYCLE)` holds, one pairwise Jacobi bit remains free.

This is structurally parallel to, but arithmetically distinct from, Goal4AU's rank-two Kummer matrix. No identification of the two free bits is currently source-locked.

## 7. Exact local flexibility witness

The remaining freedom is not an artifact of notation. At an `h_a`-prime, the reduced congruence only constrains the product of four quadratic characters.

For `ell=5`, set `a=0`, `y=c=z=1` modulo `5`. The following two unit assignments both satisfy

```text
(x*b)^2+(y*c)^2=0,
r_AB^2=(z*b)^2,
r_AC^2=(z*c)^2,
W^2=0
```

modulo `5`:

```text
Model I:  x=1, b=2,
Model II: x=2, b=1.                                  (BE-FLEX)
```

In both models

```text
(2*x*y*b*c / 5)=1,
```

but `(b/5)` changes sign, compensated by `(x/5)`. Thus the primewise face/space equations do not pin the individual residue bits that would be needed to close `(BE-R2)`.

This local diagnostic is not a global perfect-cuboid construction. It only verifies the exact source of the unresolved quadratic-character degree of freedom.

## 8. Route verdict and next lift

Certified provisionally:

```text
RESERVOIR_PRIMES_ALL_1_MOD_4=true;
PAIRWISE_RESERVOIRS_COPRIME=true;
RESERVOIR_PRODUCT_DIVIDES_W=true;
PRIMEWISE_LEGENDRE_CONSTRAINTS=true;
NEW_JACOBI_RECIPROCITY_CYCLE=true;
RECIPROCITY_SYMBOL_MATRIX_RANK=2;
ONE_PAIRWISE_JACOBI_BIT_REMAINS_FREE=true.
```

Not certified:

```text
any h_i=1;
any d_i=1;
branch exclusion;
quadratic-reciprocity contradiction;
quartic-reciprocity contradiction;
E1;
Stage35 closure;
Perfect Cuboid existence/nonexistence.
```

Ordinary quadratic reciprocity therefore yields a **new exact gate**, but not a pruning theorem. The reason for the surviving bit is also clear: every reservoir prime is split in `Q(i)`, so ordinary quadratic characters forget which Gaussian prime above `ell` is selected by the source root `iota_i(ell)`.

The next bounded lift is therefore

```text
35EX-35_GOAL4BF_ORIENTED_GAUSSIAN_QUARTIC_RECIPROCITY_RESERVOIR_LIFT_PREFLIGHT
```

with question:

```text
use the source-selected roots iota_a(ell)=x*b/(y*c), and cyclic analogues,
to orient the Gaussian prime above each reservoir prime; test whether quartic
reciprocity removes the remaining rank-two Jacobi bit or only introduces a
new phase gauge.
```

No merge. No hostile-audit credit. MAIN-STATE remains V74 / Goal4AK.
