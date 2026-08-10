# Stage14-s7-08 — multi-modulus inert second-moment audit and cross-scale recurrence barrier

## Purpose

Merged Stage14-s7-07 reduces the post-local `s7` route to the fixed quartic

```text
F(P,Q)=P*Q*(Q-P)*(Q+P)
```

and the balanced denominator strip

```text
B^(10/21-o(1)) <= Q,S <= B^(11/21+o(1)),
Q*S <= 2B,
```

with the same squarefree twist condition

```text
ker(F(P,Q)) = ker(F(R,S)).
```

It also proves exact complete quadratic-character cancellation for every inert prime `p=3 mod 4` and every all-inert odd squarefree modulus.

The natural next attempt is therefore a multi-modulus second moment / large sieve.  This stage performs that attempt adversarially.

The conclusion is a structural barrier, not a new numerical exponent:

1. the direct quadratic/square-sieve detector built only from the exact `s7-07` incomplete-box estimate is far weaker than the already-merged `20/21` bound;
2. even an *ideal* separate-side squareclass large sieve can only recover the exponent-one Cauchy ceiling `UV*B^o(1)` on a balanced block;
3. more strongly, perfect cancellation of **every nonprincipal marginal character on each scale separately** is compatible with maximal alignment of the two squareclass supports;
4. therefore marginal inert-prime equidistribution is not the missing theorem.  The missing theorem must control the **cross-scale recurrence of the same squarefree twist** directly.

This stage closes the standalone marginal-second-moment route and replaces it by a cross-scale support/transversality receiver.

No open PR is used as a theorem input.

---

## 1. Merged input from s7-07

For a reduced coordinate

```text
x=P/Q,
0<P<Q,
gcd(P,Q)=1,
```

define

```text
F(P,Q)=P*Q*(Q-P)*(Q+P).
```

Merged s7-07 gives

```text
n = ker(F(P,Q)),
```

and for a physical two-point pair

```text
x=P/Q,
y=R/S,
```

we have

```text
ker(F(P,Q)) = ker(F(R,S)) = n,
Q*S <= 2B.
```

Merged s7-06 additionally gives:

- `n>1` and squarefree;
- the two points lie on the same `j=1728` twist;
- their Jacobian difference has infinite order.

The current whole-family theorem remains

```text
V(B) << B^(20/21+o(1)).
```

The critical `s7` block is

```text
Q~U,
S~V,
U*V <= 2B,
B^(10/21-o(1)) <= U,V <= B^(11/21+o(1)).
```

---

## 2. Representation vectors and the actual overlap object

For a dyadic denominator block define

```text
r_U(n)
 = #{primitive reduced coordinates P/Q in the U-block
     with ker(F(P,Q))=n and satisfying the retained s7 admissibility conditions}.
```

Similarly define `r_V(n)`.

The squareclass collision count is

```text
C(U,V)=sum_n r_U(n) r_V(n).
```

Since merged fixed-curve genus-one geometry gives only `B^o(1)` admissible points for a fixed twist/factorization in the polynomial-height range, the power-scale issue is the support overlap

```text
A(U,V)
 = #{n : r_U(n)>0 and r_V(n)>0}.
```

Up to `B^o(1)` factors,

```text
C(U,V) <= A(U,V)*B^o(1),
A(U,V) <= C(U,V).
```

Thus what must ultimately be sparse is not a marginal character sum.  It is the set of squarefree twists which **recur at both denominator scales**.

---

## 3. The direct inert-prime quadratic detector

Let `P_R` be inert primes

```text
p=3 mod 4,
p~R,
```

and write `L=#P_R`.

For a coordinate `x=(P,Q)` define

```text
sigma_p(x)=chi_p(F(P,Q)).
```

If two positive integers have the same squarefree kernel, then for every test prime not dividing either integer their quadratic characters agree.  Hence for a same-kernel pair `(x,y)` all but the primes dividing `F(x)F(y)` contribute

```text
sigma_p(x)*sigma_p(y)=1.
```

Because `F(P,Q)<Q^4`, a polynomial-size prime interval contains only `O(1)` bad prime divisors of any one value on the exponent scale.  Thus the standard quadratic detector is legitimate after the usual bad-prime correction:

```text
1_same-kernel(x,y)
 <= (L-O(1))^(-2)
    * (sum_{p in P_R} sigma_p(x)sigma_p(y))^2.
```

Expanding the square creates:

- diagonal terms `p=q`;
- off-diagonal moduli `pq`.

For `p!=q`, the pair sum factorises:

```text
sum_{x in X_U, y in X_V}
 chi_{pq}(F(x)F(y))
 = S_{pq}(U) S_{pq}(V).
```

Merged s7-07 proves, for all-inert squarefree `m<=U`,

```text
S_m(U) << U*m*log(2U).
```

Therefore if `p,q~R` and

```text
R^2 <= min(U,V),
```

then

```text
|S_{pq}(U)S_{pq}(V)|
 << U*V*R^4*B^o(1).
```

The diagonal contribution is bounded by

```text
U^2*V^2/L.
```

Ignoring logarithms and using `L~R`, the direct square-sieve consequence is therefore

```text
C_raw(U,V)
 << U^2 V^2 / R
    + U V R^4.
```

When `UV~B`, optimisation gives

```text
R = B^(1/5),
C_raw(U,V) << B^(9/5+o(1)).
```

The admissibility condition `R^2<=min(U,V)` is satisfied throughout the critical strip because

```text
2/5 < 10/21.
```

So the failure is not caused by leaving the range of the s7-07 box estimate.  The quadratic detector itself is simply far too coarse: `9/5` is much worse than the already available `20/21` theorem.

This closes the idea that exact inert zero trace plus a routine square-sieve expansion is enough.

---

## 4. Why importing fixed-twist multiplicity still does not rescue a separate-side second moment

The strong merged input is not the raw pair count.  It is fixed-twist multiplicity.

Define the self energies

```text
E_U = sum_n r_U(n)^2,
E_V = sum_n r_V(n)^2.
```

Fixed-twist bounded-height multiplicity gives, on the ambient dyadic block,

```text
E_U << U^2*B^o(1),
E_V << V^2*B^o(1).
```

Then Cauchy gives

```text
C(U,V)
 <= sqrt(E_U E_V)
 << U*V*B^o(1).
```

In the balanced strip this is at best

```text
C(U,V) << B^(1+o(1)).
```

This is the exponent-one ceiling already isolated in s7-05.

A separate-side large sieve can improve nonprincipal Fourier coefficients of `r_U` and `r_V`, but it cannot remove the principal diagonal in the self energies.  Indeed, for nonnegative integer multiplicities,

```text
E_U = sum_n r_U(n)^2 >= sum_n r_U(n),
```

and similarly for `V`.

Any proof that makes the right side power-smaller than the ambient `U^2` count has already proved the desired active-twist sparsity.  It cannot be inserted as a free consequence of marginal character cancellation.

Thus an ideal separate-side `L^2` theorem still stops at

```text
UV*B^o(1),
```

not below `20/21`.

---

## 5. Stronger logical no-go: perfect marginal equidistribution can coexist with maximal support alignment

The previous subsection is quantitative.  There is also a purely structural obstruction.

Let

```text
G=(Z/2Z)^ell
```

be an abstract quadratic-signature group and let both scales have exactly one representation on every signature:

```text
mu_U(g)=1,
mu_V(g)=1
for every g in G.
```

For every nontrivial character `chi` of `G`,

```text
sum_g mu_U(g) chi(g)=0,
sum_g mu_V(g) chi(g)=0.
```

So **all** nonprincipal marginal character sums vanish exactly, not just degree one or degree two.

Nevertheless the support overlap is maximal:

```text
sum_g mu_U(g)mu_V(g)=|G|.
```

Indeed Fourier Parseval gives

```text
sum_g mu_U(g)mu_V(g)
 = |G|^(-1) * sum_chi muhat_U(chi) muhat_V(chi),
```

and only the principal Fourier coefficient survives:

```text
|G|^(-1) * |G|^2 = |G|.
```

Therefore the implication

```text
excellent marginal equidistribution at U
+ excellent marginal equidistribution at V
=> sparse U/V support intersection
```

is false even in an ideal finite model.

This is stronger than the single-CRT capacity warning from s7-07.  Even granting every nonprincipal marginal character for free does not create cross-scale transversality.

What is missing is information that distinguishes the **two scales jointly**.

---

## 6. Interpretation for the inert-prime program

The exact inert-prime trace remains mathematically useful.  What is closed is only the architecture

```text
control U marginal characters
+ control V marginal characters
+ Cauchy / separate-side second moment.
```

That architecture cannot beat the exponent-one ceiling and cannot logically force the overlap set `A(U,V)` to be sparse.

A future inert-prime argument remains viable only if it controls a genuinely cross-scale object, for example a bilinear recurrence operator whose off-diagonal kernel depends simultaneously on `(P,Q)` and `(R,S)` and is not reducible to two marginal norms.

So this stage does **not** say

```text
INERT_PRIME_METHOD_USEFUL=false.
```

It says

```text
MARGINAL_INERT_SECOND_MOMENT_SUFFICIENT=false.
```

---

## 7. The exact next receiver: cross-scale squarefree-twist recurrence

Define

```text
A(U,V)
 = #{squarefree n :
       exists P/Q in the U-block,
       exists R/S in the V-block,
       ker(F(P,Q))=ker(F(R,S))=n,
       physical-open conditions hold,
       Q*S<=2B}.
```

Merged s7-06 further certifies that each such recurrence yields two points on the same squarefree `j=1728` twist

```text
E_n : Y^2=X^3+4n^2X
```

whose difference has infinite order.

Equivalently, write

```text
F(P,Q)=n*a^2,
F(R,S)=n*b^2.
```

Then the recurrence satisfies the joint square-ratio equation

```text
F(P,Q)*b^2 = F(R,S)*a^2,
```

with the denominator-height condition

```text
Q~U,
S~V,
Q*S<=2B,
```

and the non-torsion difference certificate from s7-06.

This is the object that a new theorem must count directly.

A sufficient next theorem would be a uniform bound

```text
A(U,V) << B^(20/21-delta+o(1))
```

for some fixed `delta>0` on every critical balanced block.

At the central scale `U~V~B^(1/2)`, the ambient smaller-side count is `B^(1+o(1))`, so beating the current whole-family theorem requires at least the fixed saving

```text
1 - 20/21 = 1/21.
```

This saving must come from **cross-scale recurrence/height transversality**, not from separate marginal energies.

---

## 8. Candidate geometric/arithmetic handles for s7-09

The next stage should test which exact joint invariant survives after eliminating the common squarefree twist.

Priority handles:

1. **Difference-point height.**  The two quartic points have infinite-order difference on `E_n`.  Compute the difference point explicitly from the two reduced coordinates and compare its naive/canonical height with `Q,S,n`.

2. **Denominator-ratio stratification.**  Separate the genuinely two-scale region `U/V` away from one from the near-diagonal region `U~V`; identify whether the latter has extra self-correspondences.

3. **Cross-scale CM recurrence.**  Treat
   `F(P,Q)b^2=F(R,S)a^2`
   as one joint incidence problem rather than two character marginals.

4. **Prime tests only after coupling.**  Inert characters may still be used after forming a coupled kernel whose nonprincipal sums see both scales simultaneously.  They should not be applied as two independent marginal sieves.

The first of these is the cleanest next audit because s7-06 already guarantees that the difference point is non-torsion.

---

## 9. What is proved and what remains

Proved/closed here:

- the standard quadratic detector using only the merged s7-07 box estimate gives the optimised raw exponent `9/5`, hence is noncompetitive;
- fixed-twist multiplicity plus any separate-side `L^2`/Cauchy transfer stops at `UV*B^o(1)`, exponent one on the central balanced block;
- perfect cancellation of every nonprincipal marginal character is logically compatible with maximal alignment of the two signature supports;
- therefore marginal inert-prime equidistribution alone cannot produce the required fixed `1/21` saving;
- the correct remaining counting object is the cross-scale recurrence support `A(U,V)`.

Not proved here:

- a positive cross-scale recurrence saving;
- a whole-family exponent below `20/21`;
- the square-root bound.

```text
STAGE14_S7_08=COMPLETE_MULTIMODULUS_SECOND_MOMENT_AUDIT_AND_CROSS_SCALE_RECURRENCE_BARRIER
MERGED_S7_07_IMPORTED=true
DIRECT_INERT_SQUARE_SIEVE_OPTIMAL_RAW_EXPONENT=9/5
DIRECT_INERT_SQUARE_SIEVE_BEATS_20_21=false
SEPARATE_SIDE_SELF_ENERGY_BOUND=U^2_AND_V^2_TIMES_B^o(1)
SEPARATE_SIDE_CAUCHY_CEILING=U*V*B^o(1)
CENTRAL_BALANCED_SECOND_MOMENT_EXPONENT=1
MARGINAL_INERT_SECOND_MOMENT_BEATS_20_21=false
PERFECT_NONPRINCIPAL_MARGINAL_CANCELLATION_IMPLIES_SUPPORT_TRANSVERSALITY=false
CROSS_SCALE_SQUAREFREE_TWIST_RECURRENCE_DEFINED=true
PHYSICAL_RECURRENCE_HAS_INFINITE_ORDER_DIFFERENCE=true
CROSS_SCALE_FIXED_SAVING_REQUIRED_AT_CENTER=1/21
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=20/21
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-s7-09
```
