# Stage35-EX Goal4BX source lock — bridge quartic global-product congruence boundary

Scope: consume exact-green Goal4BW and test whether multiplying the source-fixed bridge quartic phases over all odd primes of `e` creates a global product obstruction. At the retained bridge-congruence layer it does not: the residual phases are reductions of one global rational square-root coordinate, but simultaneous CRT models realize every two-prime phase pattern and both product signs. This does not rule out an additional integral/global E1 identity. Mathematical authority remains V74 / Goal4AK.

## 1. Exact parent

```text
parent head = 34adeb61fcb4ec07f674be9e6a00639866969683
Goal4BW dedicated run = 34420170653 SUCCESS
```

Let

```text
E = rad_odd(e).
```

For every `ell|E`, Goal4BV fixes `iota_e(ell)` and Goal4BW fixes

```text
omega_ell = W1/V1 mod ell in {+1,-1},
r/s = omega_ell*iota_e(ell).                         (BX-root)
```

Write `Q_e(ell)` for the real Goal4BV quartic phase under the necessary quadratic bridge condition.

## 2. The residual local bit comes from one global rational coordinate

Goal4BW gives in Branch L

```text
N_L=p*q=omega_ell*z_L(ell)^2,
z_L(ell)=q*v/s mod ell.
```

Because every `ell|e` divides the primitive E1 hypotenuse `w=r^2+s^2`, `ell` does not divide `s`; hence the same global rational number

```text
Z_L = q*v/s                                             (BX-ZL)
```

reduces to `z_L(ell)` at every bridge prime.

In Branch R,

```text
z_R(ell)=(1+iota_e(ell))*q*v/s.
```

With the ordered reduced Master legs

```text
A=(V1/q)*T,
B=D*(V2/q),
iota_e(ell)=A/B mod ell,
```

and `gcd(B,e)=1`, this is the reduction of the single global rational

```text
Z_R = q*v*(A+B)/(s*B).                                 (BX-ZR)
```

Thus the residual Legendre bits are not unrelated anonymous local variables.

## 3. Oriented global bridge product

Let `pi_{e,ell}` be the Goal4BV primary Gaussian generator selected by the source root, and define

```text
Sigma_e = product_{ell|E} pi_{e,ell}.                  (BX-Sigma)
```

For Branch `*=L,R`, multiplicativity gives

```text
P_e := product_{ell|E} Q_e(ell)
     = [N_*/Sigma_e]_4
     = Omega_e * Jacobi(Z_*, E),                       (BX-product)
```

where

```text
Omega_e = product_{ell|E} [omega_ell/pi_{e,ell}]_4
```

is source-fixed and the rational Jacobi symbol is interpreted after clearing denominators, which are units modulo `E`.

So Goal4BX does obtain a genuine global compression: all residual bridge phases collapse to one Jacobi bit. The question is whether the retained bridge equations force that bit.

## 4. Simultaneous two-prime CRT diagnostic

The answer is no at the congruence layer. Work modulo

```text
E=65=5*13.
```

Choose the source root

```text
iota = 57 mod65,
iota=2 mod5,
iota=5 mod13,
iota^2=-1 mod65,
omega=1,
q=1.
```

For Branch L set

```text
s=1,
r=iota,
v=x,
u=iota*x,
p=x^2 mod65.                                           (BX-CRT-L)
```

Then simultaneously modulo both bridge primes

```text
r^2+s^2=0,
u^2+v^2=0,
p*r*s=q*u*v,
p/q=omega*(v/s)^2.
```

Choose `x` by CRT:

```text
x mod5  x mod13   x mod65   p=x^2 mod65   phases at (5,13)
1        1         1          1             (+,+)
1        2         41         56            (+,-)
2        1         27         14            (-,+)
2        2         2          4             (-,-)
```

Since `Q_e(ell)=Legendre(x,ell)` here, every phase pair occurs. In particular the product `P_e` takes both signs.

For Branch R use

```text
s=1,
r=iota,
v=x,
u=-iota*x,
p=iota*x^2 mod65.                                      (BX-CRT-R)
```

Then

```text
2*p*r*s=q*(u^2-v^2),
p/q=iota*(v/s)^2,
N_R=2*p.
```

The same four CRT values of `x` give

```text
x mod65   p mod65   phases at (5,13)
1          57        (-,-)
41         7         (-,+)
27         18        (+,-)
2          33        (+,+)
```

Again every phase pair and both product signs occur.

These are simultaneous bridge-local congruence models only. They are not global Master-Hits and not E1 counterexamples.

## 5. Goal4BX verdict

Certified provisionally:

```text
BRIDGE_RESIDUAL_PHASES_HAVE_ONE_GLOBAL_RATIONAL_CARRIER=true
ORIENTED_BRIDGE_KERNEL_SIGMA_E_DEFINED=true
BRIDGE_PHASE_PRODUCT_COMPRESSES_TO_ONE_JACOBI_BIT=true
TWO_PRIME_CRT_MODELS_REALIZE_ALL_PHASE_PATTERNS=true
BRIDGE_CONGRUENCE_LAYER_FORCES_GLOBAL_PRODUCT=false       (BX-VERDICT)
```

Not certified:

```text
full integral E1 system leaves the global Jacobi bit free;
bridge double-square integer identities cannot force the bit;
universal bad bridge quartic product;
branch exclusion;
E1;
Stage35 closure;
Perfect Cuboid existence/nonexistence.
```

## 6. Next leaf

A further bridge-quartic advance now requires a genuinely integral adapter, not another local reciprocity rewrite:

```text
35EX-35_GOAL4BY_BRIDGE_QUARTIC_INTEGER_GLOBAL_ADAPTER_PREFLIGHT
```

Goal4BY should use the exact integer bridge double-square identities

```text
p*w-q*H=e*A0^2,
p*w+q*H=e*B0^2
```

and the factor-allocation data to test whether `Jacobi(Z_L,E)` or `Jacobi(Z_R,E)` is forced globally. If no such integer relation is obtained, no bridge-quartic pruning credit is available from the current route.

No merge. No hostile-audit credit. MAIN-STATE remains V74 / Goal4AK.
