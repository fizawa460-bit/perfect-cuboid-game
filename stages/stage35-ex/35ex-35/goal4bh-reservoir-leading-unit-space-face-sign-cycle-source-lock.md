# Stage35-EX Goal4BH source lock — reservoir leading-unit space/face sign torsor

Scope: continue Goal4BG after exact-head verification. Audited authority remains V74 / Goal4AK. Goal4BH resolves the primewise meaning of the new signs `sigma_i(ell)` exposed by Goal4BG. The signs are exactly the orientation-comparison bits between the BF primitive-face Gaussian prime and the reduced space-face Gaussian prime. Full `ell`-adic leading terms determine their squares and the relevant valuations, but do not produce a source-locked cyclic product relation.

## 1. Direction a and the BF Hensel root

Fix an odd prime

```text
ell | s_a,
```

and write

```text
u = x*b,
v = y*c,
r = r_BC.
```

Goal4BE/BF gives

```text
iota_a = u/v mod ell,
iota_a^2=-1 mod ell.
```

Let `I_a in Z_ell` be the unique Hensel lift of this selected root with

```text
I_a^2=-1,
I_a == iota_a mod ell.                               (BH-I)
```

Put

```text
rho=v_ell(r)>0.                                      (BH-rho)
```

Because

```text
r^2=(u-I_a*v)*(u+I_a*v)
```

and `u+I_a*v` is an `ell`-adic unit while the selected BF factor is the other one,

```text
v_ell(u-I_a*v)=2*rho.                                (BH-small)
```

Define the exact leading unit

```text
q_a=(u-I_a*v)/ell^(2*rho) in Z_ell^*.                (BH-q)
```

Then

```text
(r/ell^rho)^2=q_a*(u+I_a*v).                         (BH-rlead)
```

This is the complete first nonzero `ell`-adic coefficient of the primitive-face cancellation producing the reservoir prime.

## 2. When the reduced space triple has a second orientation at ell

Let

```text
alpha=v_ell(a),
m=min(alpha,rho)=v_ell(h_a),
a_m=a/ell^m,
r_m=r/ell^m.                                         (BH-m)
```

The reduced space triple from Goal4BG is

```text
(x*y*a_m)^2+(z*r_m)^2=(W/h_a)^2.                    (BH-space)
```

If `alpha!=rho`, exactly one of `a_m,r_m` is an `ell`-adic unit and the other is divisible by `ell`. Hence

```text
ell does not divide W/h_a.                           (BH-unequal)
```

So a secondary space-side Gaussian orientation above `ell` can occur only in the tied case

```text
alpha=rho=m.                                         (BH-tie)
```

In the tied case both reduced legs are units. Then

```text
ell | W/h_a
```

is equivalent to

```text
lambda_a^2=-1 mod ell,
lambda_a=z*r_m/(x*y*a_m) mod ell.                    (BH-lambda)
```

Thus the secondary orientation condition is exactly the valuation tie plus one leading-unit cancellation.

## 3. Exact formula for sigma_a

Whenever `(BH-lambda)` holds, both `lambda_a` and `iota_a` are roots of `-1`, so

```text
sigma_a=lambda_a/iota_a in {+1,-1}.                  (BH-sigma-def)
```

Using the source formulas,

```text
sigma_a
 = z*c*r_m/(x^2*b*a_m) mod ell.                     (BH-sigma-explicit)
```

The full leading-unit equation `(BH-rlead)` becomes, in the tied case,

```text
r_m^2=q_a*(x*b+I_a*y*c).                             (BH-rlead-tied)
```

Hence the squared value of `(BH-sigma-explicit)` is fixed by the BF Hensel cancellation and the reduced space equation; the remaining sign is precisely the choice of square-root orientation represented by `r_m` relative to `a_m`.

## 4. sigma_a is exactly a Gaussian-prime matching bit

Goal4BF uses

```text
p_a=(ell,i-iota_a).
```

The reduced space Gaussian factor is

```text
Omega_a=z*r_m+i*x*y*a_m.                             (BH-Omega)
```

Modulo `p_a`, substitute `i=iota_a`. Since `lambda_a=sigma_a*iota_a`,

```text
Omega_a
 == x*y*a_m*iota_a*(sigma_a+1) mod p_a.             (BH-match)
```

Therefore

```text
sigma_a=-1  <=>  p_a divides Omega_a,
sigma_a=+1  <=>  bar(p_a) divides Omega_a.           (BH-orient)
```

When the secondary condition holds, write

```text
delta_a=v_ell(W/h_a)>0.
```

Because the reduced space triple is primitive, only one prime above `ell` divides `Omega_a`, and its Gaussian valuation is exactly

```text
2*delta_a.                                            (BH-space-val)
```

Thus `sigma_a` is not an auxiliary notation: it is the exact face-versus-space Gaussian orientation matching bit.

## 5. Cyclic formulas

Cyclically, for a secondary prime in `s_b`,

```text
sigma_b
 = y*c*(r_AC/ell^m)/(x^2*a*(b/ell^m)) mod ell,
```

and for a secondary prime in `s_c`,

```text
sigma_c
 = x*b*(r_AB/ell^m)/(y^2*a*(c/ell^m)) mod ell.       (BH-cyclic)
```

Each equals `-1` when the BF-selected Gaussian prime is also the space-selected prime, and `+1` when the space factor selects the conjugate prime.

## 6. Why full leading terms still do not give a cyclic sign theorem

Equation `(BH-rlead)` determines

```text
(r/ell^rho)^2
```

from the exact Hensel leading unit `q_a`, but it does not canonically replace the source integer square root `r/ell^rho` by a formula in the other retained variables. The sign of that square root relative to `a/ell^rho` is exactly `sigma_a` once the secondary space condition is imposed.

The same issue occurs independently in the `b` and `c` directions. Goal4BE supplies a quadratic Jacobi cycle for the rational reservoir kernels, and Goal4BF supplies oriented quartic prime data, but neither source lock gives an identity multiplying these three secondary square-root orientation choices.

Therefore Goal4BH obtains an exact reduction

```text
remaining BF/BG phase problem
 -> primewise mu_2 face/space orientation bits sigma_i(ell),             (BH-reduction)
```

but no source-locked theorem of the form

```text
product sigma_i(ell)=constant                         (BH-no-cycle)
```

has been derived.

This is a proof boundary, not a claim of mathematical independence of the signs.

## 7. Verdict

Certified provisionally:

```text
BF_HENSEL_LEADING_UNIT_EXACT=true;
SECONDARY_ORIENTATION_REQUIRES_VALUATION_TIE=true;
SIGMA_I_EXPLICIT_LEADING_UNIT_FORMULA=true;
SIGMA_I_EQUALS_GAUSSIAN_PRIME_MATCHING_BIT=true;
SELECTED_SPACE_GAUSSIAN_VALUATION_EVEN_EXACT=true;
PHASE_PROBLEM_REDUCED_TO_MU2_ORIENTATION_TORSOR=true;
SIGMA_CYCLE_RELATION_OBTAINED=false;
BRANCH_PRUNING=false.
```

Not certified:

```text
universal sigma product;
quartic-phase contradiction;
any h_i=1;
any d_i=1;
E1;
Stage35 closure;
Perfect Cuboid existence/nonexistence.
```

Next unit:

```text
35EX-35_GOAL4BI_SECONDARY_ORIENTATION_HILBERT_PRODUCT_FORMULA_PREFLIGHT
```

Question: package the `sigma_i(ell)` as local `mu_2` orientation characters and test whether Hilbert reciprocity/global product formula, including the real and 2-adic places, imposes a global relation not already contained in Goal4BE.

No merge. No hostile-audit credit. MAIN-STATE remains V74 / Goal4AK.
