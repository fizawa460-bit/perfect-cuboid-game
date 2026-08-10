# Stage14-4bu — fixed universal quartic critical strip and inert-prime zero trace

## Purpose

Merged Stage14-4bt compresses the joint physical two-point receiver to squarefree `j=1728` twists

\[
E_n:Y^2=X^3+4n^2X,
\qquad n=k\xi,
\]

with `n>1` squarefree and with an infinite-order difference between the two physical points.  The current whole-family bound remains

\[
V(B)\ll B^{20/21+o(1)}.
\]

Stage14-4bu asks whether the twist parameter can be reorganized into a family on which the remaining `20/21` barrier can actually be attacked.

The main outcome is structural rather than a new exponent:

1. `n` is the squarefree kernel of one **fixed universal binary quartic**;
2. all unbalanced denominator sectors are reduced to the current `20/21` ceiling by the already merged fixed-coordinate genus-one fibers;
3. the only new family-level target is a balanced off-diagonal squareclass collision for that fixed quartic;
4. for every odd prime `p=3 mod 4`, the complete quadratic-character trace of this quartic vanishes **exactly**, and the same is true for every squarefree modulus supported on such primes;
5. primitive incomplete square boxes satisfy an elementary `O(U m log(2U))` bound for those inert moduli.

No new whole-family exponent is claimed here.

---

## 1. Merged inputs only

We use only merged results:

- Stage14-4br / 4bs:
  \[
  V(B)\ll B^{20/21+o(1)},
  \qquad 20/21-1/2=19/42.
  \]
- Stage14-s7-04: for reduced physical coordinates
  \[
  u=P/Q,\qquad w=R/S,
  \]
  one has
  \[
  QS\ll B,
  \]
  together with the product-square and same-difference-kernel conditions.  A fixed reduced coordinate has `B^o(1)` compatible physical partners.
- Stage14-4bt: put
  \[
  \xi=\ker(PQ),\qquad k=\ker(Q^2-P^2).
  \]
  Then `(xi,k)=1`, `n=k xi` is squarefree, `n>1`, and a physical pair gives a non-torsion difference on `E_n`.
- Stage14-t42 is compatible as an energy/dispersion interface, but no t42 power-saving statement is imported here.

No open PR is a theorem input.

---

## 2. The twist parameter is one fixed quartic squareclass

Since

\[
\gcd(PQ,Q^2-P^2)=1,
\]

the two squarefree kernels multiply without cancellation.  Hence

\[
\boxed{
 n
 =\ker(PQ)\ker(Q^2-P^2)
 =\ker\!\left(PQ(Q^2-P^2)\right).
}
\tag{BU.1}
\]

Define the universal homogeneous binary quartic

\[
\boxed{
F(P,Q):=PQ(Q-P)(Q+P).
}
\tag{BU.2}
\]

Then every physical joint pair satisfies

\[
\boxed{
\ker F(P,Q)=\ker F(R,S)=n.
}
\tag{BU.3}
\]

Thus the one-dimensional `j=1728` twist parameter of 4bt is exactly the squareclass label of one fixed four-linear form.

Important quantifier boundary:

> equality of the total labels `ker F(P,Q)=ker F(R,S)` is a necessary majorant condition, not a converse physical criterion.

Physicality still retains the separate `xi` and `k` equalities, ordering, primitivity, and the denominator-product cutoff.

We record

```text
TWIST_PARAMETER_IS_FIXED_BINARY_QUARTIC_KERNEL=true
FIXED_QUARTIC_SQUARECLASS_COLLISION_CONVERSE_PHYSICAL=false
```

---

## 3. Elementary height consequence

For `0<P<Q`,

\[
\xi=\ker(PQ)<Q^2,
\qquad
k=\ker(Q^2-P^2)<Q^2.
\]

Therefore

\[
\boxed{n<Q^4.}
\tag{BU.4}
\]

The same argument for `(R,S)` gives `n<S^4`.  Consequently every physical two-point witness obeys

\[
\boxed{Q>n^{1/4},\qquad S>n^{1/4}.}
\tag{BU.5}
\]

Hence its two-point denominator product satisfies

\[
\boxed{QS>n^{1/2}.}
\tag{BU.6}
\]

This recovers the safe physical range `n<<B^2` from the exact multiplicative cutoff `QS<<B`; it does not by itself improve the `20/21` exponent.

---

## 4. General denominator split

Let `L=B^lambda`.  Every physical pair lies in either

\[
\min(Q,S)\le L
\]

or the complementary sector `Q,S>L`.

The number of reduced fractions in `(0,1)` with denominator at most `L` is `O(L^2)`.  By the merged s7-04 fixed-coordinate `B^o(1)` partner multiplicity,

\[
\boxed{
E_{\min(Q,S)\le L}(B)
\ll L^2B^{o(1)}
=B^{2\lambda+o(1)}.
}
\tag{BU.7}
\]

Therefore the current `20/21` ceiling is matched at the exact denominator exponent

\[
\boxed{\lambda_0=10/21.}
\tag{BU.8}
\]

More generally, to seek a new whole-family saving `delta>0`, choose

\[
\lambda=10/21-\delta/2.
\]

Then the small-denominator sector is already

\[
O(B^{20/21-\delta+o(1)}).
\]

The unresolved complement has

\[
Q,S>B^{10/21-\delta/2}.
\]

Since `QS<<B`, each denominator is also at most

\[
B^{11/21+\delta/2+o(1)}.
\]

At the zero-saving boundary the unique critical strip is therefore

\[
\boxed{
B^{10/21-o(1)}\lesssim Q,S\lesssim B^{11/21+o(1)},
\qquad QS\ll B.
}
\tag{BU.9}
\]

This is the first exact balanced-denominator receiver on the 14-4 main track.

---

## 5. Exact inert-prime complete trace

Let `p` be an odd prime with

\[
p\equiv3\pmod4,
\]

and let `chi_p` be the quadratic character modulo `p`, extended by `chi_p(0)=0`.

For `Q` nonzero modulo `p`, put `t=P/Q`.  Since `Q^4` is a square,

\[
\chi_p(F(P,Q))
=\chi_p\!\left(t(1-t^2)\right).
\tag{BU.10}
\]

Set

\[
f(t)=t(1-t^2).
\]

For `t` not equal to `0,+1,-1`,

\[
\frac{f(t^{-1})}{f(t)}=-\frac1{t^4}.
\]

Because `p=3 mod 4`,

\[
\chi_p(-1)=-1,
\]

so inversion pairs cancel exactly:

\[
\chi_p(f(t^{-1}))=-\chi_p(f(t)).
\]

The exceptional values `t=0,+1,-1` contribute zero.  Hence

\[
\boxed{
\sum_{t\bmod p}\chi_p(t(1-t^2))=0.
}
\tag{BU.11}
\]

The `Q=0` row also contributes zero because `F(P,0)=0`.  Therefore

\[
\boxed{
\sum_{P,Q\bmod p}\chi_p(F(P,Q))=0
\qquad(p\equiv3\bmod4).
}
\tag{BU.12}
\]

This is exact zero, stronger than a generic square-root complete-sum estimate.

---

## 6. Squarefree inert moduli

Let `m` be odd, squarefree, and suppose every prime divisor of `m` is `3 mod 4`.  Use the Jacobi character

\[
\chi_m=\prod_{p\mid m}\chi_p.
\]

CRT factorization together with (BU.12) gives

\[
\boxed{
\sum_{P,Q\bmod m}\chi_m(F(P,Q))=0.
}
\tag{BU.13}
\]

Thus every squarefree inert modulus has an exact zero complete two-variable trace.

---

## 7. Primitive incomplete square boxes

Define

\[
S_m(U)
:=\sum_{\substack{1\le P,Q\le U\\(P,Q)=1}}
\chi_m(F(P,Q)).
\]

Möbius inversion gives

\[
S_m(U)
=\sum_{\substack{d\le U\\(d,m)=1}}
\mu(d)\,T_m(U/d),
\]

where

\[
T_m(V)=\sum_{1\le P,Q\le V}\chi_m(F(P,Q)).
\]

For `V>=m`, tile the square into complete `m x m` blocks.  Every complete block vanishes by (BU.13), leaving only two boundary strips and a corner, so

\[
T_m(V)\ll Vm.
\]

For `V<m`, use the trivial bound `T_m(V)<<V^2`.  Splitting the Möbius sum at `d=U/m` yields

\[
\boxed{
S_m(U)\ll U m\log(2U).
}
\tag{BU.14}
\]

uniformly for `m<=U`; for `m>U` the trivial `O(U^2)` bound is retained.

This gives a deterministic signed dispersion adapter on the exact fixed quartic in the balanced denominator strip.

It is not yet a whole-family theorem: the principal same-squareclass collision remains an energy/existence problem, and taking absolute values before using (BU.14) would discard the cancellation.

---

## 8. Why generic twist-height alone is not the next proof step

The receiver from 4bt has only the safe ranges

\[
n\ll B^2,\qquad H_2(n)\ll B.
\]

A lower bound on the first non-torsion height for each individual twist, without correlation between the two physical points and the fixed quartic squareclass, does not by itself convert these ranges into an exponent below `20/21`.

Accordingly Stage14-4bu imports **no new external generic twist-height theorem as a saving theorem**.  The exact arithmetic receiver (BU.9)--(BU.14) is stronger for the next Stage14 step because it retains both the denominator hyperbola and a signed character on the universal quartic.

---

## 9. Current quantitative boundary

No new whole-family exponent is claimed:

\[
\boxed{V(B)\ll B^{20/21+o(1)}.}
\]

The remaining gap to square-root scale is still

\[
\boxed{20/21-1/2=19/42.}
\]

What has changed is the unique unresolved object.  Any improvement beyond `20/21` can now be sought entirely inside the balanced family

\[
B^{10/21-o(1)}\lesssim Q,S\lesssim B^{11/21+o(1)},
\]

with

\[
\ker F(P,Q)=\ker F(R,S),
\qquad
F(X,Y)=XY(Y-X)(Y+X),
\]

while retaining the stronger separate physical labels and the exact denominator hyperbola.

The natural next stage is one-Cauchy / inert-prime dispersion on this balanced fixed-quartic collision, with the principal squareclass energy kept explicit.

---

## Locked boundary

```text
STAGE14_4BU=FIXED_QUARTIC_CRITICAL_STRIP_AND_INERT_PRIME_ZERO_TRACE
TWIST_PARAMETER_IS_FIXED_BINARY_QUARTIC_KERNEL=true
FIXED_BINARY_QUARTIC=PQ(Q-P)(Q+P)
PHYSICAL_PAIR_IMPLIES_FIXED_QUARTIC_SQUARECLASS_COLLISION=true
FIXED_QUARTIC_SQUARECLASS_COLLISION_CONVERSE_PHYSICAL=false
POINT_DENOMINATOR_LOWER_BOUND_FROM_N=Q>n^(1/4)
TWO_POINT_HEIGHT_LOWER_BOUND=H_2(n)>n^(1/2)
SMALL_DENOMINATOR_SECTOR_BOUND=L^2*B^o(1)
CRITICAL_DENOMINATOR_EXPONENT=10/21
BALANCED_DENOMINATOR_STRIP_LOWER=10/21
BALANCED_DENOMINATOR_STRIP_UPPER=11/21
INERT_PRIME_COMPLETE_CHARACTER_SUM_ZERO=true
INERT_SQUAREFREE_MODULUS_COMPLETE_CHARACTER_SUM_ZERO=true
INERT_MODULUS_PRIMITIVE_BOX_BOUND=U*m*log(2U)
GENERIC_TWIST_HEIGHT_THEOREM_IMPORTED_AS_MAIN_SAVING=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=20/21
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
REMAINING_GAP_TO_SQRT=19/42
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4bv
```
