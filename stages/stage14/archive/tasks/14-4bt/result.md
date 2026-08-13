# Stage14-4bt — squarefree j=1728 twist compression and torsion-pair exclusion

## Purpose

Merged Stage14-4bs replaces the exhausted `20/21` size-splitting architecture by the exact joint reduced-coordinate receiver from merged Stage14-s7-04.  A physical ordered edge supplies two reduced rationals

\[
u=P/Q,\qquad w=R/S,\qquad 0<w<u<1,
\]

with

\[
QS\ll B,\qquad \frac{PR}{QS}\in \mathbf Q^{\times 2},
\]

and

\[
\ker(Q^2-P^2)=\ker(S^2-R^2).
\]

Stage14-4bt compresses these two simultaneous squareclass conditions to a single squarefree `j=1728` twist parameter and proves that the two physical points always differ by a non-torsion Jacobian point.  This is a receiver change; it does not yet improve the merged whole-family exponent `20/21`.

No open PR is used as a theorem input.  The same-twist formulas are derived here directly from merged s7-04.

---

## 1. Canonical squareclass labels

For a reduced rational `0<P<Q`, define

\[
\xi(P,Q)=\ker(PQ),\qquad k(P,Q)=\ker(Q^2-P^2),
\]

where `ker` is the positive squarefree kernel.

Because `(P,Q)=1`,

\[
\gcd(PQ,Q^2-P^2)=1.
\]

Hence

\[
\boxed{\gcd(\xi,k)=1.}
\tag{BT.1}
\]

The rational squareclass of `P/Q` equals the squareclass of `PQ`, so

\[
\frac{PR}{QS}\in\mathbf Q^{\times2}
\iff
\xi(P,Q)=\xi(R,S).
\tag{BT.2}
\]

The merged s7-04 difference condition is exactly

\[
k(P,Q)=k(R,S).
\tag{BT.3}
\]

Thus every physical joint pair has a common ordered label `(k,xi)` with `(k,xi)=1`.

---

## 2. One quartic twist

Write

\[
PQ=\xi a^2,\qquad Q^2-P^2=k b^2.
\]

Put

\[
z=a/Q,\qquad y=b/Q.
\]

Then

\[
P/Q=\xi z^2,
\]

and

\[
\boxed{k y^2=1-\xi^2z^4.}
\tag{BT.4}
\]

The second reduced coordinate gives another rational point on the same curve

\[
C_{k,\xi}:\quad k y^2=1-\xi^2z^4.
\]

Since `0<w<u<1`, choose the canonical positive square roots `z_1,z_2>0`; then `z_1\ne z_2`.

The binary quartic Jacobian is the `j=1728` curve

\[
\boxed{E_n:\ Y^2=X^3+4n^2X,\qquad n=k\xi.}
\tag{BT.5}
\]

By (BT.1), `n` is squarefree.

---

## 3. The twist parameter is nontrivial

If `n=1`, then `k=xi=1`.  Since `PQ` is a square and `(P,Q)=1`, both `P` and `Q` are squares:

\[
P=p^2,\qquad Q=q^2.
\]

Also `Q^2-P^2` is a square, giving

\[
q^4-p^4=r^2
\]

with `0<p<q`.  This is excluded by the classical Fermat quartic descent already used in merged Stage14-s7-02.

Therefore every physical joint pair has

\[
\boxed{n>1\text{ squarefree}.}
\tag{BT.6}
\]

---

## 4. Rational torsion on `E_n`

For squarefree `n>1`,

\[
E_n(\mathbf Q)_{\rm tors}=\{O,(0,0)\}\cong\mathbf Z/2\mathbf Z.
\tag{BT.7}
\]

A compact proof uses standard inputs already acceptable in Stage14:

1. `E_n` has the unique rational 2-torsion point `(0,0)`.
2. For every good prime `p=3 mod 4`, the `j=1728` CM trace is zero, hence `#E_n(F_p)=p+1`.  Together with reduction of rational torsion and Dirichlet primes in suitable progressions, this excludes odd torsion (the only odd primes needed after Mazur are 3 and 5).
3. A rational point `T` with `2T=(0,0)` must satisfy the duplication numerator `x(T)^2-4n^2=0`.  The positive possibility `x(T)=2n` gives `y(T)^2=16n^3`, rational only when `n` is a square.  Since `n>1` is squarefree, no rational 4-torsion exists; therefore no 8- or 12-torsion exists either.

Thus (BT.7) follows.

---

## 5. The physical pair cannot differ by the 2-torsion point

On the quartic `C_{k,xi}`, consider

\[
\tau(z,y)=(-z,-y).
\]

It is an involution with no geometric fixed point: at finite `z`, a fixed point would require `z=y=0`, impossible on (BT.4); at infinity the two points are exchanged.  Hence on this genus-one torsor `tau` is translation by the unique nonzero rational 2-torsion point of the Jacobian, namely `(0,0)`.

The physical representatives use canonical positive lifts `z_1,z_2>0`.  Therefore

\[
(z_2,y_2)\ne\tau(z_1,y_1),
\]

because `tau` changes the sign of `z`.

The points are also distinct because `0<w<u<1`.  Combining with (BT.7), their Jacobian difference is neither `O` nor `(0,0)`.  Hence

\[
\boxed{P_2-P_1\in E_n(\mathbf Q)\text{ has infinite order}.}
\tag{BT.8}
\]

This removes the torsion/self-correspondence branch from the joint receiver.

---

## 6. Power-scale collapse from `(k,xi)` to one squarefree `n`

Because `n` is squarefree and `(k,xi)=1`, the number of ordered factorizations

\[
n=k\xi
\]

is at most

\[
2^{\omega(n)}=n^{o(1)}.
\]

Moreover each point satisfies `n<=Q^4` and `n<=S^4`.  Since `QS\ll B`,

\[
\boxed{n\ll B^2.}
\tag{BT.9}
\]

Thus the two squareclass labels carry only `B^o(1)` multiplicity over one squarefree twist parameter `n`.

Define `H_2(n)` to be the least product `QS` among all coprime squarefree factorizations `n=kxi` and two distinct canonical positive rational points on `C_{k,xi}` that satisfy the physical open inequalities.  Then a physical hit below `B` implies

\[
H_2(n)\ll B
\]

for some squarefree `1<n\ll B^2`, and the associated Jacobian has a non-torsion difference point.

Using the same fixed-curve bounded-height multiplicity mechanism already used in merged 4bq, fixed `n` and fixed factorization contribute only `B^o(1)` admissible bounded-height point pairs.  Therefore the next one-dimensional receiver is

\[
\boxed{
V(B)\ll B^{o(1)}\#\{\,n\ll B^2:\ n\text{ squarefree},\ H_2(n)\ll B\,\}.
}
\tag{BT.10}
\]

This receiver is not yet a new numerical upper bound; the merged `B^(20/21+o(1))` bound remains stronger until the squarefree-twist family is shown sparse.

---

## 7. What is closed and what remains

Closed here:

- the joint product-square and same-difference-kernel conditions are one common `(k,xi)` twist;
- `gcd(k,xi)=1` exactly;
- `n=kxi` is squarefree and `n>1`;
- the two physical points have an infinite-order Jacobian difference;
- factorization multiplicity over fixed `n` is only `B^o(1)`;
- the main receiver is reduced to a one-dimensional squarefree `j=1728` twist family with a first two-point multiplicative-height condition.

Not proved here:

- a power-saving bound for the number of squarefree `n` with `H_2(n)<=B`;
- a new whole-family exponent below `20/21`;
- the square-root bound.

The next stage should count squarefree twists with a non-torsion difference point of two-point height `H_2(n)<=B`, retaining the `QS` hyperbola instead of replacing it by a generic positive-rank condition.

```text
STAGE14_4BT=SQUAREFREE_J1728_TWIST_COMPRESSION_AND_TORSION_PAIR_EXCLUSION
JOINT_XI_LABEL_EQUALITY_EXACT=true
JOINT_K_LABEL_EQUALITY_EXACT=true
XI_K_COPRIME=true
TWIST_PARAMETER_N=k*xi
TWIST_PARAMETER_N_SQUAREFREE=true
PHYSICAL_TWIST_PARAMETER_N_GT_1=true
TWIST_JACOBIAN=y^2=x^3+4*n^2*x
SQUAREFREE_N_GT_1_RATIONAL_TORSION=Z/2Z
PHYSICAL_TWO_POINT_DIFFERENCE_TORSION=false
PHYSICAL_TWO_POINT_DIFFERENCE_INFINITE_ORDER=true
FIXED_N_FACTORISATION_MULTIPLICITY=B^o(1)
PHYSICAL_TWIST_PARAMETER_BOUND=B^2
ONE_DIMENSIONAL_SQUAREFREE_TWIST_RECEIVER_DEFINED=true
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=20/21
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4bu
```
