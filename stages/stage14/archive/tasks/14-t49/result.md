# Stage14-t49 — external split-prime Frobenius amplifier and non-circular mean-square reduction

## Purpose

Stage14-t48 identified the t47 Gram matrix with the actual canonical-square-normalized four-linear squareclass character, but its sufficient condition was stated as a **uniform worst-row** estimate. Stage14-t49 removes that unnecessary uniformity and replaces it with one global Frobenius mean square over an external family of split auxiliary primes.

At the same time, t49 audits the order of operations in the tH13 product-kernel receiver. If ordered state pairs are collapsed to cross-kernel multiplicities too early, the conductor coefficient energy becomes the unresolved fourth energy `E4`; this is circular. The physical/norm-index cancellation must therefore be applied before that collapse.

## 1. The centered detector may use external split primes

Let the reciprocal-quotient physical states be `s`, with squareclass

\[
\kappa_s=[F_s].
\]

On a visible state remove the exact even canonical square

\[
\widetilde F_s=F_s/\ell_s^2,
\]

and on an invisible state put `Ftilde_s=F_s`. Since `Ftilde_s` and `kappa_s` differ by a rational square, for **every odd auxiliary prime** `p`, not just a state's own canonical prime,

\[
\boxed{
\chi_{\kappa_s}(p)=\left(\frac{\widetilde F_s}{p}\right).
}
\tag{49.1}
\]

We restrict the amplifier to split primes

\[
p\equiv1\pmod4,
\]

because this is exactly the good-prime geometry used by the t32 split-torus completion.

Thus the t47 Gram matrix may be formed from any finite split-prime amplifier `P`:

\[
G_{p,q}
=\sum_s\chi_{\kappa_s}(p)\chi_{\kappa_s}(q)
=\sum_s
\left(\frac{\widetilde F_s}{p}\right)
\left(\frac{\widetilde F_s}{q}\right).
\tag{49.2}
\]

The frozen external audit checks (49.1) `71,680` times using 128 split primes from `2017` through `4073`.

## 2. Frobenius lower bound for the principal collision energy

Let

\[
r_\kappa=\#\{s:\kappa_s=\kappa\},
\qquad
H=\sum_\kappa r_\kappa,
\qquad
A_1=\sum_\kappa r_\kappa^2.
\]

For the amplifier `P`, put

\[
v_\kappa(p)=\chi_\kappa(p).
\]

Then

\[
G_{p,q}=\sum_\kappa r_\kappa v_\kappa(p)v_\kappa(q).
\]

The full Frobenius norm has the exact column expansion

\[
\|G\|_F^2
=\sum_{\kappa,\kappa'}
 r_\kappa r_{\kappa'}
 \langle v_\kappa,v_{\kappa'}\rangle^2.
\tag{49.3}
\]

Every summand on the right is nonnegative. For `kappa=kappa'`,

\[
\langle v_\kappa,v_\kappa\rangle
=P-b_\kappa,
\]

where

\[
b_\kappa=\#\{p\in\mathcal P:p\mid\kappa\}.
\]

Writing `b=max b_kappa`, (49.3) therefore gives the exact lower bound

\[
\boxed{
A_1(P-b)^2\le \|G\|_F^2.
}
\tag{49.4}
\]

This is stronger conceptually than the t47 worst-row route because it uses the positive principal contribution **before** any rowwise maximum.

## 3. Only an averaged two-prime mean square is needed

Split the Frobenius norm into diagonal and offdiagonal prime pairs:

\[
\|G\|_F^2
=\sum_p G_{p,p}^2
+\mathcal R_{\rm off},
\]

with

\[
\boxed{
\mathcal R_{\rm off}
=\sum_{p\ne q\in\mathcal P}
\left|\sum_s
\left(\frac{\widetilde F_s}{p}\right)
\left(\frac{\widetilde F_s}{q}\right)
\right|^2.
}
\tag{49.5}
\]

Since `|G_pp|<=H`,

\[
\sum_pG_{p,p}^2\le PH^2.
\]

Combining this with (49.4) yields

\[
\boxed{
A_1
\le
\frac{PH^2+\mathcal R_{\rm off}}{(P-b)^2}.
}
\tag{49.6}
\]

Therefore a uniform estimate for every row is **not required**.

A sufficient near-linear contract is

\[
b=o(P),
\qquad
P\ge H B^{-o(1)},
\qquad
\mathcal R_{\rm off}\le H P^2 B^{o(1)}.
\tag{49.7}
\]

Under (49.7),

\[
\boxed{A_1\le H B^{o(1)}.}
\tag{49.8}
\]

The advantage is structural: (49.5) is exactly a **global two-split-prime physical mean square**, which is the natural average for t32's two-prime angular completion.

For a dyadic external amplifier `p~L=B^theta`, a polynomial-size squareclass has only `O_theta(1)` prime divisors in that interval. The larger t32 bad set `p|ell Delta mn` is also supported on polynomial-size integers and gives only `B^o(1)` bad-prime incidences per fixed state. Their global aggregate still has to be charged explicitly; t49 does not claim that step is closed.

## 4. Frozen data sit on the natural random-character scale

For the 87 endogenous canonical split primes:

```text
H                                  560
P                                   87
A1                                 592
max bad primes / squareclass         2
full Frobenius              31,336,611
diagonal Frobenius          27,228,401
offdiagonal Frobenius        4,108,210
max row offdiag L2               73,273
Roff / [H P(P-1)]            0.9804984343
```

For 128 external split primes `2017 <= p <= 4073`:

```text
H                                  560
P                                  128
A1                                 592
max bad primes / squareclass         0
full Frobenius              49,148,256
diagonal Frobenius          40,140,800
offdiagonal Frobenius        9,007,456
max row offdiag L2               99,896
Roff / [H P(P-1)]            0.9894649888
```

Thus the frozen offdiagonal mean square is extremely close to the natural random-character scale

\[
\mathcal R_{\rm off}\asymp H P(P-1).
\]

This is only a finite diagnostic, not an asymptotic proof, but importantly the target in (49.7) is not contradicted by the frozen family.

## 5. Exact product-kernel expansion and the order-of-operations barrier

For two squarefree classes `a,b`, let

\[
\tau=\operatorname{sqf}(ab),
\qquad
g=\gcd(a,b).
\]

At a test prime `p`,

\[
\chi_a(p)\chi_b(p)
=
1_{p\nmid g}\,\chi_\tau(p).
\]

Hence if `J` is the set of amplifier primes dividing `g`, the Frobenius norm has the exact refinement

\[
\boxed{
\|G\|_F^2
=
\sum_{\tau,J}
 c(\tau,J)
 \left|\sum_{p\in\mathcal P\setminus J}\chi_\tau(p)\right|^2.
}
\tag{49.9}
\]

Frozen exact reconstruction:

```text
cross-kernel support                    132,961
(tau,J) refinement groups               133,000
total ordered pair mass                 313,600 = H^2
principal tau=1 mass                        592
max nonprincipal tau multiplicity            40
pair mass with nonempty shared J              76
```

However, if one first collapses all ordered state pairs to the coefficients `c(tau)` and then invokes a bilinear tH13 coefficient-energy bound, the coefficient energy is

\[
\sum_\tau c(\tau)^2=E_4.
\]

Frozen:

```text
E4                         1,324,576
nonprincipal E4              974,112
```

This is exactly the quantity still being bounded. Therefore

\[
\boxed{
\text{pair collapse first} \;\Longrightarrow\; E_4\text{ coefficient energy}\;\Longrightarrow\;\text{circular}.
}
\tag{49.10}
\]

The order must instead be:

1. retain the signed physical state sum;
2. apply the t32 split-torus angular completion on good `(p,q)` and norm-index cells;
3. retain the tH12 common refinement and tH13 same-modulus/divisor-coupled aggregation;
4. only after that cancellation, take the global prime-pair mean square / product-kernel bookkeeping.

This is the non-circular route handed to t50.

## tH decision

**No additional tH stage is required. Do not start tH14 yet.**

The external Frobenius amplifier changes the order and averaging of the existing objects, but does not create a new adapter. The live missing theorem is the signed divisor-coupled norm-index mean-square estimate itself, already within the t32 + tH12 + tH13 architecture.

Reopen tH only if t50 exposes a repeated-character or selector obstruction that cannot be represented by the existing common-refinement / same-modulus dispersion receivers.

## Boundary

```text
STAGE14_T49=COMPLETE_EXTERNAL_SPLIT_PRIME_FROBENIUS_AMPLIFIER_AND_NONCIRCULAR_MEAN_SQUARE_REDUCTION
EXTERNAL_SPLIT_PRIME_AMPLIFIER_VALID=true
PRINCIPAL_COLLISION_FROBENIUS_LOWER_BOUND=true
UNIFORM_WORST_ROW_BOUND_REQUIRED=false
AVERAGED_TWO_PRIME_MEAN_SQUARE_SUFFICIENT_FOR_A1_NEAR_LINEAR=true
T32_TWO_PRIME_PHYSICAL_INTERFACE_NATIVE=true
NAIVE_PRODUCT_KERNEL_PAIR_COEFFICIENT_ENERGY_EQUALS_E4=true
PAIR_COLLAPSE_BEFORE_PHYSICAL_CANCELLATION_IS_CIRCULAR=true
SIGNED_NORM_INDEX_AGGREGATION_BEFORE_PAIR_COLLAPSE_REQUIRED=true
GLOBAL_EXTERNAL_TWO_PRIME_MEAN_SQUARE_BOUND_PROVED=false
EXTERNAL_BAD_AUXILIARY_AGGREGATE_BOUND_PROVED=false
GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false
GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
TH14_NEEDED=false
NEXT=Stage14-t50 prove the external split-prime offdiagonal Frobenius mean square R_off<=H*P^2*B^o(1) on the critical family by applying t32 angular completion before Cauchy/pair collapse and retaining the tH12/tH13 signed divisor-coupled norm-index aggregation; separately charge auxiliary bad-prime incidences
```
