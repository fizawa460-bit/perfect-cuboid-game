# Stage35-EX Goal4BF source lock — source-oriented Gaussian quartic lift and residual phase gauge

Scope: continue exact-green Goal4BE. Audited authority remains V74 / Goal4AK. Goal4BF lifts the reservoir-prime quadratic data from `Q` to `Z[i]` using the source-selected square root of `-1` at each reservoir prime, and tests whether standard quartic reciprocity removes Goal4BE's one surviving Jacobi bit. It does not: the orientation is canonical, but rational reservoirs factor as an oriented Gaussian divisor times its conjugate, leaving cross-conjugate quartic phases not fixed by the retained source equations.

## 1. Input from Goal4BE

Retain the primitive six-variable dictionary and

```text
h_a=gcd(a,r_BC),
h_b=gcd(b,r_AC),
h_c=gcd(c,r_AB),
```

with pairwise-coprime reservoirs. Every odd reservoir prime is `1 mod 4`.

For `ell|h_a`, Goal4BE gives the source-selected root

```text
iota_a(ell)=x*b/(y*c) mod ell,
iota_a(ell)^2=-1.                                     (BF-iota-a)
```

Cyclically,

```text
iota_b(ell)=x*a/(z*c) mod ell,
iota_c(ell)=y*a/(z*b) mod ell.                         (BF-iota)
```

Let `s_a,s_b,s_c` be the positive squarefree representatives of `[h_a],[h_b],[h_c]` used in Goal4BE.

## 2. The source root selects one Gaussian prime above ell

For `ell|s_a`, define the prime ideal

```text
p_{a,ell}=(ell, i-iota_a(ell)) subset Z[i].            (BF-Pa)
```

The quotient map sends `i` to `iota_a(ell)` in `F_ell`, so `p_{a,ell}` is one of the two conjugate primes above `ell`.

Because

```text
x*b-i*y*c = 0 mod p_{a,ell},
```

this selected prime divides the source Gaussian face factor. Its conjugate does not: modulo the conjugate prime one has `i=-iota_a(ell)`, so

```text
x*b-i*y*c = 2*x*b != 0 mod ell                         (BF-one-side)
```

by the exact source coprimalities and oddness of `ell`.

Since

```text
N(x*b-i*y*c)=r_BC^2,
```

one-sidedness gives the exact valuation

```text
v_{p_{a,ell}}(x*b-i*y*c)=2*v_ell(r_BC),
v_{bar p_{a,ell}}(x*b-i*y*c)=0.                       (BF-val)
```

The same construction holds cyclically.

## 3. Primary normalization and oriented squarefree Gaussian kernels

For each selected odd prime ideal choose its unique primary Gaussian generator

```text
pi_{a,ell} == 1 mod (1+i)^3,                           (BF-primary)
```

and cyclically. This is the standard primary normalization used in quartic reciprocity.

Define the oriented squarefree Gaussian kernels

```text
Sigma_a = product_{ell|s_a} pi_{a,ell},
Sigma_b = product_{ell|s_b} pi_{b,ell},
Sigma_c = product_{ell|s_c} pi_{c,ell}.                (BF-Sigma)
```

Then exactly

```text
N(Sigma_a)=s_a,
N(Sigma_b)=s_b,
N(Sigma_c)=s_c,

s_a=Sigma_a*bar(Sigma_a),
s_b=Sigma_b*bar(Sigma_b),
s_c=Sigma_c*bar(Sigma_c).                              (BF-N)
```

Moreover `Sigma_a` divides `x*b-i*y*c`, and cyclically, because every selected prime occurs there with valuation at least `2*v_ell(h_a)>=1` for `ell|s_a`.

Thus the source data canonically chooses an **oriented Gaussian half** of each rational reservoir squarefree kernel.

## 4. Quartic residue lift

For a selected prime `pi_{a,ell}`, reduction gives

```text
x*b/(y*c) = i mod pi_{a,ell}.                          (BF-red)
```

Hence the quartic residue character satisfies

```text
[x*b/(y*c) / pi_{a,ell}]_4 = [i / pi_{a,ell}]_4.       (BF-Q4a)
```

Cyclic analogues hold. Squaring `(BF-Q4a)` recovers the quadratic/Legendre character used in Goal4BE, because the square of the quartic residue character is the ordinary quadratic character on the residue field.

Therefore Goal4BF is a genuine lift of Goal4BE, not an unrelated Gaussian reparameterization of Goal4AX.

## 5. What quartic reciprocity can exchange

For coprime primary Gaussian integers `alpha,beta`, standard quartic reciprocity gives

```text
[alpha/beta]_4 * [beta/alpha]_4^(-1)
 = (-1)^(((N(alpha)-1)/4)*((N(beta)-1)/4)).            (BF-QR4)
```

The correction factor is explicit from the rational norms and therefore creates no new unknown.

Apply this to the oriented factors `Sigma_a,Sigma_b,Sigma_c`. It exchanges terms such as

```text
[Sigma_a/Sigma_b]_4  <->  [Sigma_b/Sigma_a]_4          (BF-oriented-exchange)
```

up to the explicit norm sign.

However the rational reservoir entering Goal4BE is not `Sigma_b`; it is

```text
s_b=Sigma_b*bar(Sigma_b).                              (BF-conj-factor)
```

Thus a quartic lift of the rational cross-reservoir symbol contains both

```text
[Sigma_b/Sigma_a]_4
and
[bar(Sigma_b)/Sigma_a]_4.                              (BF-two-phases)
```

Quartic reciprocity exchanges the first with the corresponding oriented reverse symbol, but it does not eliminate the second from the retained data. The source root at primes of `s_b` selects `Sigma_b`; it supplies no independent equation identifying the cross-conjugate phase `[bar(Sigma_b)/Sigma_a]_4` with the oriented one.

## 6. Canonical quartic lifts of the BE pairwise symbols

Define

```text
U_ab = [s_b/Sigma_a]_4
     = [Sigma_b/Sigma_a]_4*[bar(Sigma_b)/Sigma_a]_4,
U_ac = [s_c/Sigma_a]_4,
U_bc = [s_c/Sigma_b]_4,                                (BF-U)
```

with the analogous reverse quantities. These are canonically defined by the source-oriented denominators.

Their squares are exactly the BE quadratic pairwise symbols:

```text
U_ab^2=(s_b/s_a),
U_ac^2=(s_c/s_a),
U_bc^2=(s_c/s_b).                                      (BF-square)
```

Thus the surviving BE Jacobi bit lifts to a `mu_4` phase problem. The lift is canonical, but its phase is **not determined** by Goal4BE's quadratic data.

The missing phases may be represented by

```text
G_ab=[bar(Sigma_b)/Sigma_a]_4,
G_ac=[bar(Sigma_c)/Sigma_a]_4,
G_bc=[bar(Sigma_c)/Sigma_b]_4.                         (BF-G)
```

No retained source identity fixes all three `G_ij` or supplies a relation of sufficient rank to eliminate the Goal4BE free bit.

## 7. Exact small-prime phase diagnostic

Goal4BE's `ell=5` local flexibility witness already preserves the same source root `iota=2` in both models:

```text
Model I : x=1, b=2, y=c=1,
Model II: x=2, b=1, y=c=1.                             (BF-5)
```

In both cases `x*b/(y*c)=2=iota mod 5`, so the **same Gaussian prime orientation above 5** is selected. Yet the quartic character contributions of `x` and `b` are interchanged: modulo the selected prime, the order-four character sends `2` to a primitive fourth root while `1` maps to `1`.

Hence source orientation fixes the total ratio phase `(BF-Q4a)` but does not separately fix the factor phases needed to turn the cross-conjugate terms into a contradiction. This is a local diagnostic only, not a global endpoint construction.

## 8. Relation to Goal4AX

Goal4AX already proved that the rational six-norm `Q(i)` Hilbert-90 chart is endpoint-equivalent. Goal4BF is not reopening that route. Its new datum is integral and prime-oriented:

```text
reservoir prime + source root of -1
 -> selected Gaussian prime ideal
 -> primary generator
 -> quartic residue phase.                             (BF-new)
```

The surviving obstruction question therefore lives in Gaussian **square-root/phase compatibility**, not in the rational norm torus itself.

## 9. Verdict

Certified provisionally:

```text
SOURCE_ROOT_SELECTS_GAUSSIAN_PRIME=true;
PRIMARY_ORIENTED_RESERVOIR_KERNELS=true;
ONE_SIDED_GAUSSIAN_VALUATION=true;
QUARTIC_RESIDUE_LIFT_OF_BE=true;
QUARTIC_RECIPROCITY_APPLICABLE_TO_ORIENTED_FACTORS=true;
CROSS_CONJUGATE_PHASES_REMAIN=true;
BE_FREE_BIT_CLOSED_BY_QUARTIC_RECIPROCITY_ALONE=false.
```

Not certified:

```text
quartic-reciprocity contradiction;
any h_i=1;
any d_i=1;
branch exclusion;
E1;
Stage35 closure;
Perfect Cuboid existence/nonexistence.
```

Goal4BF therefore gives an exact oriented Gaussian lift but not pruning. The next missing object is no longer a reciprocity theorem: it is the actual Gaussian square-root factorization of the three primitive Pythagorean faces and whether their source phases are cross-compatible.

Next unit:

```text
35EX-35_GOAL4BG_GAUSSIAN_SQUARE_ROOT_FACE_PHASE_COMPATIBILITY_PREFLIGHT
```

Question: write each primitive face factor as a unit times a Gaussian square, source-lock its unit/conjugation choice, and test whether the three face square roots plus the common space diagonal impose enough cross-phase equations to fix the `G_ij` gauge left by Goal4BF.

No merge. No hostile-audit credit. MAIN-STATE remains V74 / Goal4AK.
