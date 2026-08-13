# Stage14-4bl — dual compact half-angle critical-square reduction

## Purpose

Stage14-4bj fixed the missing post-local exponent at

\[
\alpha=\frac{10}{21},
\qquad
\frac{41}{42}-\frac12=\frac{10}{21}.
\]

Merged Stage14-s6-06 gives one exact physical compact selector, obtained by translating the physical elliptic point by `T0=(0,0)`.  Its denominator is supported on the `H2-S2` half-angle column.

Open PR #359 (`14-4bk`) independently found the complementary selector obtained from `T-=(-X^2,0)`, supported on the `H2+S2` column.  This stage does **not** formally import the open PR.  Instead it rederives the complementary selector from the merged s3/s6-05 formulas and combines it with merged s6-06.

The result is an exact dual factorization of the partner leg into

```text
half-angle denominator product × half-angle cancellation product.
```

This allows the size split to be optimized exactly.  The optimum threshold is `X2=B^(20/21)`.  Below it, physical edges already satisfy an absolute `B^(20/21+o(1))` bound, improving the current `B^(41/42+epsilon)` exponent by `1/42` on that sector.  Above it, every remaining edge carries a **critical-scale** dual denominator product or a critical-scale dual square-cancellation product of size at least `B^(10/21)` up to an absolute constant.

No full-family positive `delta_post` is claimed: the missing theorem is now a joint physical root-sign / square-divisor incidence bound for those two critical products.

---

## 1. Primitive partner half-angle roots

For a primitive oriented Pythagorean partner face

\[
S_2^2+X_2^2=H_2^2,
\]

there are unique positive coprime integers `s>t` and

\[
\kappa\in\{1,2\}
\]

such that

\[
\boxed{
H_2+S_2=\kappa s^2,
\qquad
H_2-S_2=\kappa t^2,
\qquad
X_2=\kappa st.
}
\tag{BL.1}
\]

Indeed:

- if `S2=m^2-n^2`, `X2=2mn`, then `kappa=2`, `s=m`, `t=n`;
- if `S2=2mn`, `X2=m^2-n^2`, then `kappa=1`, `s=m+n`, `t=m-n`.

In either case `gcd(s,t)=1`.

---

## 2. Merged minus-column selector from s6-06

Put

\[
G=\gcd(S,S_2)d.
\]

Merged s6-06 proves

\[
G^2=H^2S_2^2+S^2X_2^2
\]

and, for the compact translate by `T0=(0,0)`, the reduced denominator `D_-` satisfies

\[
\boxed{D_-^2\mid H_2-S_2=\kappa t^2.}
\tag{BL.2}
\]

Hence

\[
\boxed{D_-\mid t.}
\tag{BL.3}
\]

Define the exact cancellation cofactor

\[
\boxed{k_-:=t/D_-.}
\tag{BL.4}
\]

If

\[
N_-:=HG-S^2H_2-X^2S_2,
\]

then merged s6-06 gives

\[
\boxed{
\gcd(N_-,H_2-S_2)=\kappa k_-^2.
}
\tag{BL.5}
\]

For a good odd prime `ell^e||t`, `ell∤HSX`, the full prime power survives in `D_-` exactly on the root sign

\[
G\equiv-HS_2\pmod{\ell^{2e}}.
\tag{BL.6}
\]

---

## 3. Independent rederivation of the plus-column selector

Translate the same exact physical point by the other compact rational 2-torsion point

\[
T_-=(-X^2,0).
\]

The s3 physical coordinate gives

\[
Z(P+T_-)=-X^2\frac{Z_P-S^2}{Z_P+X^2}
       =-\frac{(G+HS_2)(HH_2-G)}{X_2^2}.
\tag{BL.7}
\]

Using `G^2=H^2S2^2+S^2X2^2` and `X2^2=H2^2-S2^2`, direct expansion gives

\[
(G+HS_2)(HH_2-G)
=(H_2-S_2)N_+,
\]

where

\[
\boxed{
N_+:=HG+X^2S_2-S^2H_2.
}
\tag{BL.8}
\]

Therefore

\[
\boxed{
Z(P+T_-)=-\frac{N_+}{H_2+S_2}.
}
\tag{BL.9}
\]

The translated point is on the compact real component, is nonzero modulo `2E(Q)`, preserves the canonical-height window, and reconstructs the original physical point by the same torsion translation.

Write its reduced denominator as `D_+^2`.  Since rational x-coordinates on the monic integral Weierstrass model have square denominator,

\[
\boxed{D_+^2\mid H_2+S_2=\kappa s^2.}
\tag{BL.10}
\]

Consequently

\[
\boxed{D_+\mid s.}
\tag{BL.11}
\]

Define

\[
\boxed{k_+:=s/D_+.}
\tag{BL.12}
\]

Then reduction of (BL.9) gives the exact complementary square cancellation

\[
\boxed{
\gcd(N_+,H_2+S_2)=\kappa k_+^2.
}
\tag{BL.13}
\]

For a good odd prime `ell^e||s`, `ell∤HSX`, the full prime power survives in `D_+` exactly on

\[
G\equiv+HS_2\pmod{\ell^{2e}}.
\tag{BL.14}
\]

Thus the two compact torsion translates see the two coprime half-angle columns with opposite root signs.

---

## 4. Exact dual product identity

Put

\[
Q:=D_+D_-,
\qquad
K:=k_+k_-.
\]

Since `D_+ k_+=s`, `D_- k_-=t` and `gcd(s,t)=1`,

\[
\boxed{
QK=st=\frac{X_2}{\kappa}.
}
\tag{BL.15}
\]

This identity is exact, including the 2-adic cases through `kappa`.

Interpretation:

- `Q` is the **dual compact denominator product**;
- `K` is the **dual square-cancellation product**;
- each good odd prime power in the partner leg is assigned by its physical root sign to one of these two products.

The cancellation side also has an exact physical square-divisor receiver:

\[
\boxed{
k_+^2\mid N_+,
\qquad
k_-^2\mid N_-,
\qquad
K^2\mid N_+N_-.
}
\tag{BL.16}
\]

The denominator side has two exact square denominators

\[
D_+^2\mid H_2+S_2,
\qquad
D_-^2\mid H_2-S_2,
\tag{BL.17}
\]

with complementary good-prime root-sign congruences (BL.6), (BL.14).

---

## 5. Optimal partner-leg size split

Merged Stage14-4ag gives maximum physical graph degree `B^o(1)`.  The elementary Euclid-parameter count gives

\[
\#\{(S_2,X_2,H_2):H_2\le B,\ X_2\le Y\}
\ll Y\log(2B).
\]

Therefore physical edges incident to a partner with `X2<=Y` satisfy

\[
\boxed{E_{X_2\le Y}(B)\ll YB^{o(1)}.}
\tag{BL.18}
\]

Let `Y=B^beta`.  Then:

1. the small-partner-leg sector has exponent `beta`;
2. on its complement, (BL.15) implies

\[
\max(Q,K)\ge\sqrt{X_2/\kappa}
\gg B^{\beta/2}.
\tag{BL.19}
\]

To force one of the dual products to reach the full missing post-local scale

\[
\alpha=10/21,
\]

we need

\[
\beta/2\ge10/21,
\]

i.e.

\[
\boxed{\beta\ge20/21.}
\tag{BL.20}
\]

To make the small-leg sector improve the current exponent `41/42`, we need

\[
\beta<41/42.
\]

Thus the exact admissible window is

\[
\boxed{
20/21\le\beta<41/42.
}
\tag{BL.21}
\]

The optimal choice for the strongest unconditional small-leg estimate is the left endpoint

\[
\boxed{\beta_*=20/21.}
\tag{BL.22}
\]

Then

\[
\boxed{
E_{X_2\le B^{20/21}}(B)
\ll B^{20/21+o(1)}.
}
\tag{BL.23}
\]

Relative to the current global physical upper bound `B^(41/42+epsilon)`, this sector gains exactly

\[
\boxed{
\frac{41}{42}-\frac{20}{21}=\frac1{42}.
}
\tag{BL.24}
\]

This is a genuine physical-edge statement, not a fixed-packet coordinate-density estimate.

---

## 6. Critical-square dichotomy on the remaining family

After removing (BL.23), every remaining physical edge has

\[
X_2>B^{20/21}.
\]

By (BL.15),

\[
QK=X_2/\kappa>\frac12 B^{20/21}.
\]

Hence

\[
\boxed{
\max(Q,K)>2^{-1/2}B^{10/21}.
}
\tag{BL.25}
\]

Therefore every square-root-relevant residual physical edge belongs to one of only two critical sectors:

### A. Critical dual-denominator sector

\[
\boxed{Q=D_+D_-\gg B^{10/21}.}
\tag{BL.26}
\]

The edge carries two exact square denominators on coprime half-angle columns and complementary physical root-sign congruences.

### B. Critical dual-cancellation sector

\[
\boxed{K=k_+k_-\gg B^{10/21}.}
\tag{BL.27}
\]

The edge carries the exact large physical square divisor

\[
\boxed{K^2\mid N_+N_-}
\]

with `K^2 >> B^(20/21)`.

This is substantially sharper than the one-selector `B^(1/84)` cofactor remainder: after using both compact torsion translates, the residual square structure is already at the **full critical post-local scale `10/21`**.

---

## 7. Why full `delta_post` is still not declared

The product threshold alone does not justify multiplying two coordinate-density estimates.

- `Q` may split between `D_+` and `D_-`; from `Q>>B^(10/21)` alone, one only knows one individual denominator is at least `B^(5/21)`.
- `K` may similarly split between `k_+` and `k_-`.
- A full saving at product scale therefore requires a **joint dual-selector physical incidence theorem**, not two independent fixed-packet estimates multiplied after conditioning.

The correct next analytic object is now explicit:

1. for the denominator side, a same-edge dispersion count retaining both half-angle root-sign congruences simultaneously;
2. for the cancellation side, a square-divisor/root-sign count for `K^2|N_+N_-` retaining the exact physical gluing.

No arbitrary packet-existence transfer is needed: both selectors are explicit invertible torsion translates of the exact physical point.

Thus

```text
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false.
```

The `B^(20/21+o(1))` estimate is a genuine **sectoral** post-local improvement, not yet a full-family exponent.

---

## Boundary

```text
STAGE14_4BL=DUAL_COMPACT_HALF_ANGLE_CRITICAL_SQUARE_REDUCTION
MERGED_S6_06_MINUS_SELECTOR_IMPORTED=true
OPEN_4BK_FORMALLY_IMPORTED=false
PLUS_SELECTOR_REDERIVED_INDEPENDENTLY=true
PARTNER_HALF_ANGLE_ROOTS_EXACT=true
PARTNER_HALF_ANGLE_FORM=H2+S2=kappa*s^2,H2-S2=kappa*t^2,X2=kappa*s*t
DUAL_PLUS_DENOMINATOR_DIVIDES_S=true
DUAL_MINUS_DENOMINATOR_DIVIDES_T=true
DUAL_PLUS_CANCELLATION_EXACT=true
DUAL_MINUS_CANCELLATION_EXACT=true
DUAL_PRODUCT_IDENTITY=Q*K=X2/kappa
DUAL_CANCELLATION_SQUARE_DIVIDES_NPLUS_NMINUS=true
REQUIRED_POST_LOCAL_SAVING=10/21
OPTIMAL_PARTNER_LEG_SPLIT_EXPONENT=20/21
SMALL_PARTNER_LEG_EDGE_BOUND=B^(20/21+o(1))
SMALL_PARTNER_LEG_SECTOR_SAVING_VS_41_42=1/42
LARGE_PARTNER_LEG_IMPLIES_CRITICAL_DUAL_STRUCTURE=true
CRITICAL_DUAL_DENOMINATOR_OR_CANCELLATION_SCALE=10/21
JOINT_DUAL_SELECTOR_INCIDENCE_THEOREM_PROVED=false
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=41/42
SQRT_B_UPPER_BOUND_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-4bm prove a joint physical dual-selector dispersion theorem: large Q through simultaneous plus/minus root-sign congruences, or large K through the square-divisor condition K^2|N_+N_-, without multiplying conditioned coordinate densities
```
