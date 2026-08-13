# Stage14-4bm — cross-sector power saving and the square-neutral gcd-cell barrier

## Purpose

Merged Stage14-4bl reduces every square-root-relevant physical edge to a partner leg

\[
X_2>B^{20/21}
\]

carrying critical dual denominator/cancellation structure.  Merged Stage14-s6-07 gives an injective transfer to a pair of primitive Pythagorean faces `(F2,F3)` and the exact five-factor decomposition

\[
X_2=X_{2,\mathrm{cross}}q_{--}q_{-+}q_{+-}q_{++}.
\]

Stage14-4bm combines these two merged inputs and asks whether the forced positive-power incidence can already be converted into a full physical-edge saving.

The answer is mixed but quantitatively useful.

1. The **cross-prime sector** can be counted unconditionally and is bounded by
   \[
   O(B^{61/63+o(1)}),
   \]
   a genuine `1/126` exponent improvement over the current `B^(41/42+epsilon)` bound.
2. Outside that sector, one of the four good half-angle gcd cells is forced to satisfy
   \[
   q_{ij}\gg B^{4/21}.
   \]
3. The compatibility square becomes an exact four-linear product in half-angle coordinates.  A shared gcd cell contributes an **automatic square factor `q^2`** to that product.  Therefore a naive `1/q` density or root-sign probability is invalid: the large gcd is square-neutral after physicality is imposed.
4. The remaining theorem is now a single signed/primitive reduced-quartic incidence estimate on the large-good-cell sector.  Merged t35 is structurally compatible but its positive dispersion plus generic Cauchy bound does not prove the required saving.

Thus full `delta_post>0` is still not proved, but the residual family is substantially smaller and the cross branch is closed with a fixed power saving.

---

## 1. Merged inputs

We use only merged results:

- Stage14-s5u / 4bf chain:
  \[
  V(B)\ll B^{41/42+\epsilon}.
  \]
- Stage14-4bl:
  \[
  X_2\le B^{20/21}\quad\Longrightarrow\quad
  E(B)\ll B^{20/21+o(1)},
  \]
  so every unresolved edge has `X2>B^(20/21)`.
- Stage14-s6-07:
  every physical ordered edge injects into primitive faces
  \[
  F_2=(S_2,X_2,H_2),\qquad F_3=(S_3,X_3,H_3),
  \]
  with `H2,H3<=B`, satisfying
  \[
  (S_3X_2)^2-(X_3S_2)^2=\square,
  \]
  and
  \[
  X_2=X_{2,\mathrm{cross}}q_{--}q_{-+}q_{+-}q_{++}.
  \]
- Stage14-t35:
  positive same-modulus dispersion is available in its Gaussian norm setting, but generic absolute-value/Cauchy transfer does not produce a norm-hyperbola power saving.

No open PR is used as a theorem input.

---

## 2. Uniform half-angle coordinates and exact four-linear square

For a primitive oriented Pythagorean face `F=(A,B,C)`, write

\[
C-A=\kappa u^2,\qquad C+A=\kappa v^2,
\qquad \kappa\in\{1,2\},\quad (u,v)=1,
\]

so

\[
A=\frac\kappa2(v^2-u^2),\qquad B=\kappa uv.
\]

For `F2` use `(u,v,kappa2)` and for `F3` use `(r,s,kappa3)`.
Then

\[
S_3X_2=\frac{\kappa_2\kappa_3}{2}\,uv(s^2-r^2),
\]

\[
X_3S_2=\frac{\kappa_2\kappa_3}{2}\,rs(v^2-u^2).
\]

Direct factorization gives

\[
\boxed{
\begin{aligned}
&u^2v^2(s^2-r^2)^2-r^2s^2(v^2-u^2)^2\\
&\qquad=(ru-sv)(ru+sv)(rv-su)(rv+su).
\end{aligned}}
\tag{BM.1}
\]

Hence the physical compatibility condition is equivalent, up to the fixed square factor `(kappa2*kappa3/2)^2`, to

\[
\boxed{
(ru-sv)(ru+sv)(rv-su)(rv+su)=\square.
}
\tag{BM.2}
\]

This is exactly the same four-linear square-cover geometry that appears independently in the Stage14-t route.

---

## 3. The stronger `4/21` forced factor after 4bl

On the unresolved 4bl family,

\[
X_2>B^{20/21}.
\]

From the s6-07 five-factor identity,

\[
X_2=X_{2,\mathrm{cross}}q_{--}q_{-+}q_{+-}q_{++},
\]

so at least one factor satisfies

\[
\boxed{
\max(X_{2,\mathrm{cross}},q_{--},q_{-+},q_{+-},q_{++})
\gg B^{4/21}.
}
\tag{BM.3}
\]

This improves the earlier `41/420` receiver because 4bl has already removed all `X2<=B^(20/21)` edges.

Put

\[
\gamma=\frac4{21}.
\]

We now split according to whether the large receiver is `X2_cross` or a good gcd cell.

---

## 4. Decomposing the cross-prime factor

Let

\[
X_{2,\mathrm{cross}}
=2^{a}\prod_{\substack{p^e\Vert X_2\\p\mid H,\ p\text{ odd}}}p^e.
\]

Put

\[
c=\gcd(H,X_2)_{\rm odd}.
\]

For each odd cross prime, write

\[
e_p=v_p(X_2),\qquad f_p=v_p(H),\qquad
r_p=e_p-\min(e_p,f_p)\ge0.
\]

Define

\[
h=\prod_{p\mid X_{2,\mathrm{cross}},\ p\text{ odd}}
 p^{\lceil r_p/2\rceil}.
\]

Because `f_p>=1` on the cross support,

\[
2\lceil r_p/2\rceil\le e_p,
\]

so

\[
\boxed{h^2\mid X_2.}
\tag{BM.4}
\]

Moreover the excess after removing the true common divisor satisfies

\[
\prod p^{r_p}\mid h^2,
\]

hence

\[
\boxed{
X_{2,\mathrm{cross}}\le 2^a c h^2.
}
\tag{BM.5}
\]

Therefore

\[
X_{2,\mathrm{cross}}\ge B^\gamma
\]

forces at least one of

\[
2^a\ge B^{\gamma/3},\qquad
c\ge B^{\gamma/3},\qquad
h\ge B^{\gamma/6}.
\tag{BM.6}
\]

Constants are harmless in all exponent statements.

---

## 5. Counting the three cross sub-sectors

### 5.1 Large 2-primary partner-leg divisor

Primitive Euclid parameterization gives, uniformly for a power of two `Q`,

\[
\#\{F_2:H_2\le B,\ Q\mid X_2\}
\ll B^{1+o(1)}/Q.
\]

Merged 4ag gives physical graph degree `B^o(1)`, so

\[
2^a\ge B^{\gamma/3}
\quad\Longrightarrow\quad
E(B)\ll B^{1-\gamma/3+o(1)}.
\tag{BM.7}
\]

### 5.2 Large true cross gcd

Merged s6-07 constructs

\[
H_3=\frac d{\gcd(H,X_2)}.
\]

Thus `c>=B^(gamma/3)` implies

\[
H_3\ll B^{1-\gamma/3}.
\]

For fixed `F3`, the compatibility square (BM.2) is a nonsingular quartic genus-one curve in the rational direction `u/v`, with four rational branch points.  The same bounded-height rational-point theorem imported in merged 4ag therefore gives `B^o(1)` compatible primitive `F2` of height at most `B`.

Since the number of primitive oriented `F3` with hypotenuse at most `Y` is `O(Y)`, we obtain

\[
\boxed{
E_{c\ge B^{\gamma/3}}(B)
\ll B^{1-\gamma/3+o(1)}.
}
\tag{BM.8}
\]

This is a direct physical-pair count; no packet-density multiplication is used.

### 5.3 Large squarefull excess in the partner leg

If `h>=H0` and `h^2|X2`, Euclid parameterization and coprimality of its two factors give

\[
\#\{F_2:H_2\le B,\ h^2\mid X_2\}
\ll B^{1+o(1)}/h^2.
\]

Summing over `h>=H0`,

\[
\#\{F_2:\exists h\ge H_0,\ h^2\mid X_2\}
\ll B^{1+o(1)}\sum_{h\ge H_0}\frac1{h^2}
\ll \frac{B^{1+o(1)}}{H_0}.
\]

With `H0=B^(gamma/6)` and again using merged 4ag degree `B^o(1)`, this gives

\[
\boxed{
E_{h\ge B^{\gamma/6}}(B)
\ll B^{1-\gamma/6+o(1)}.
}
\tag{BM.9}
\]

This is the worst of the three cross estimates.

---

## 6. Cross-prime sector closes with a `1/126` gain

Insert

\[
\gamma=\frac4{21}.
\]

Then

\[
1-\frac{\gamma}{6}
=1-\frac2{63}
=\boxed{\frac{61}{63}}.
\]

Therefore

\[
\boxed{
E_{X_{2,\mathrm{cross}}\ge B^{4/21}}(B)
\ll B^{61/63+o(1)}.
}
\tag{BM.10}
\]

Since

\[
\frac{41}{42}-\frac{61}{63}
=\boxed{\frac1{126}},
\]

this is a genuine fixed-power improvement over the current physical upper bound on the entire cross-prime branch.

Together with merged 4bl,

\[
X_2\le B^{20/21}
\]

is already bounded by `B^(20/21+o(1))`, which is even smaller.

Thus every still-unresolved edge must satisfy

\[
\boxed{
X_2>B^{20/21},\qquad
X_{2,\mathrm{cross}}<B^{4/21},
}
\tag{BM.11}
\]

and consequently

\[
\boxed{
\max(q_{--},q_{-+},q_{+-},q_{++})\gg B^{4/21}.
}
\tag{BM.12}
\]

---

## 7. Large good gcd cells are square-neutral

The remaining receiver is one large good cell.

For example, suppose

\[
q=q_{--}\mid u,r.
\]

Write

\[
u=qa,\qquad r=qb.
\]

Then the four-linear product (BM.2) becomes

\[
\begin{aligned}
&(q^2ab-sv)(q^2ab+sv)\\
&\qquad\times q(bv-sa)\,q(bv+sa).
\end{aligned}
\]

Hence

\[
\boxed{
\frac1{q^2}
(ru-sv)(ru+sv)(rv-su)(rv+su)
}
\]

is exactly

\[
\boxed{
(q^2ab-sv)(q^2ab+sv)(bv-sa)(bv+sa).
}
\tag{BM.13}
\]

The extracted factor `q^2` is already a perfect square.

The other three gcd cells have the same property after permuting `u,v,r,s`: each shared half-angle gcd divides two of the four linear factors, so its square is **forced before any square detector is applied**.

Thus

\[
\boxed{
q_{ij}^2\mid
(ru-sv)(ru+sv)(rv-su)(rv+su)
}
\tag{BM.14}
\]

for every good cell, and dividing by that `q_ij^2` preserves the square condition.

This proves a no-go statement:

> the condition `q_ij>=B^(4/21)` does not itself contribute a density factor `1/q_ij`, nor may it be interpreted as independent root-sign cancellation.

It is a structural common divisor already built into the physical four-linear square.

We record

```text
LARGE_GOOD_GCD_CELL_AUTOMATIC_SQUARE_FACTOR=true
NAIVE_GCD_CELL_DENSITY_GAIN_VALID=false.
```

---

## 8. Relation to merged t35

Merged t35 proves a positive same-modulus collision/dispersion estimate in the Gaussian norm skeleton and removes the previous tensor `sqrt(M)` loss.  However its generic Cauchy/duality return gives

\[
(M^2+N)B^{o(1)},
\]

which does not beat the target norm-hyperbola mass by a fixed power.

The main-track obstruction found here is the same phenomenon in physical half-angle coordinates:

- the positive shared modulus is real and large;
- but after the exact square relation is imposed, part of its contribution is an automatic square;
- absolute-value counting of the shared modulus alone cannot supply the missing exponent.

Therefore Stage14-4bm does **not** import t35 as a power-saving theorem for (BM.12).

The useful alignment is methodological: the next theorem must retain a signed square detector / trace **inside the fixed shared-modulus fiber**, rather than first taking absolute values and then applying Cauchy.

---

## 9. Unique residual analytic object

After 4bl + 4bm, the post-local main track has only one unresolved family:

\[
\boxed{
\begin{gathered}
X_2>B^{20/21},\\
X_{2,\mathrm{cross}}<B^{4/21},\\
q=q_{ij}\gg B^{4/21}\quad\text{for one good cell},\\
(ru-sv)(ru+sv)(rv-su)(rv+su)=\square.
\end{gathered}}
\tag{BM.15}
\]

After extracting the automatic `q^2`, one obtains a primitive reduced quartic of the form (BM.13), with the corresponding variable permutation for the other cells.

The correct next target is therefore:

> prove a signed square-sieve / dispersion estimate for the reduced quartic uniformly for dyadic shared modulus `q>=B^(4/21)`, retaining the physical primitive-face boxes and without replacing the square condition by a positive gcd count.

This is narrower than the previous joint `Q/K` formulation and has no remaining abstract packet-existence quantifier.

---

## 10. Quantitative status

Proved in this stage:

\[
E_{X_2\le B^{20/21}}(B)\ll B^{20/21+o(1)}
\]
(imported from merged 4bl), and

\[
\boxed{
E_{X_{2,\mathrm{cross}}\ge B^{4/21}}(B)
\ll B^{61/63+o(1)}.
}
\]

The cross sector therefore gains `1/126` relative to `41/42`.

Not proved:

\[
E_{q_{ij}\ge B^{4/21}}(B)
\ll B^{41/42-\delta}
\]
for any fixed `delta>0`.

Hence the full physical bound remains

\[
\boxed{V(B)\ll B^{41/42+\epsilon}.}
\]

and

```text
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false.
```

---

## Boundary

```text
STAGE14_4BM=CROSS_SECTOR_POWER_SAVING_AND_SQUARE_NEUTRAL_GCD_CELL_BARRIER
MERGED_4BL_IMPORTED=true
MERGED_S6_07_IMPORTED=true
MERGED_T35_COMPATIBILITY_AUDITED=true
HALF_ANGLE_FOUR_LINEAR_SQUARE_FACTORIZATION_EXACT=true
POST_4BL_FORCED_FIVE_FACTOR_EXPONENT=4/21
CROSS_FACTOR_DECOMPOSITION=X2_cross<=2part*c*h^2
CROSS_TRUE_GCD_SMALL_THIRD_FACE_COUNT_PROVED=true
CROSS_SQUAREFULL_EXCESS_COUNT_PROVED=true
CROSS_SECTOR_BOUND=B^(61/63+o(1))
CROSS_SECTOR_SAVING_VS_41_42=1/126
UNRESOLVED_GOOD_GCD_CELL_SCALE=4/21
LARGE_GOOD_GCD_CELL_AUTOMATIC_SQUARE_FACTOR=true
NAIVE_GCD_CELL_DENSITY_GAIN_VALID=false
SIGNED_REDUCED_QUARTIC_DISPERSION_REQUIRED=true
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=41/42
SQRT_B_UPPER_BOUND_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-4bn
```

## Next

`Stage14-4bn`: prove a signed reduced-quartic square-sieve/dispersion estimate on a fixed large good gcd-cell fiber `q>=B^(4/21)`, using the exact four-linear factorization and the same-modulus philosophy of merged t35 without taking absolute values before the physical square detector.
