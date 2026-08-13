# Stage14-s7-06 — squarefree j=1728 torsion/self-correspondence exclusion

## Purpose

Merged Stage14-s7-05 compresses every physical joint first-point pair to two distinct rational points on one quartic

```text
C_{k,xi}:  k y^2 = 1 - xi^2 z^4,
```

with Jacobian

```text
E_n: Y^2 = X^3 + 4 n^2 X,
n = k*xi,
j(E_n)=1728.
```

The remaining logical gap in s7-05 is that two distinct rational points on a genus-one torsor need not a priori differ by a non-torsion Jacobian point.  Stage14-s7-06 closes exactly that torsion/self-correspondence branch.

The main new conclusion is

```text
physical joint pair
=> n>1 squarefree
=> E_n(Q)_tors = Z/2Z
=> the two canonical positive quartic points are not related by torsion
=> their Jacobian difference has infinite order
=> rank E_n(Q) >= 1.
```

No new whole-family counting exponent is claimed here.  The current merged whole-family upper bound remains `B^(20/21+o(1))`.

---

## 1. Merged inputs

### 1.1 Stage14-s7-05

For a reduced rational coordinate `u=P/Q`, `0<P<Q`, define

```text
xi = ker(PQ),
k  = ker(Q^2-P^2).
```

A physical pair supplies two reduced coordinates

```text
0 < w < u < 1
```

with the same ordered label `(k,xi)`.  Writing

```text
u = xi*z1^2,
w = xi*z2^2,
```

with the canonical positive rational square roots `z1,z2>0`, both points lie on

```text
C_{k,xi}: k*y^2 = 1-xi^2*z^4.
```

The points are distinct because `w<u`.

### 1.2 Merged Stage14-4bt

Merged 4bt independently closes the squarefree-twist torsion gate for the same joint receiver.  We import only its proved theorem boundary:

```text
gcd(k,xi)=1,
n=k*xi is squarefree,
physical n>1,
E_n(Q)_tors = Z/2Z,
physical two-point difference is not torsion.
```

The dedicated 4bt CI is green.  No open PR is used as a theorem input.

---

## 2. Exact coprimality and squarefree twist parameter

For reduced `P/Q`,

```text
gcd(PQ,Q^2-P^2)=1.
```

Therefore their positive squarefree kernels satisfy

```text
boxed:
gcd(xi,k)=1.                                           (2.1)
```

Since both `xi` and `k` are squarefree,

```text
boxed:
n=k*xi is squarefree.                                  (2.2)
```

This is stronger than the s7-05 statement that the Jacobian depends only on the product `k*xi`: the product is already the canonical squarefree twist parameter.

---

## 3. The physical twist cannot be n=1

Suppose `n=1`.  By (2.1), this forces

```text
k=xi=1.
```

Then `PQ` is a square.  Since `gcd(P,Q)=1`, write

```text
P=p^2,
Q=q^2.
```

Also `Q^2-P^2` is a square, so

```text
q^4-p^4=r^2,
0<p<q.
```

The classical Fermat quartic descent already used in merged s7-02 excludes such a nonboundary rational solution.  Hence every physical joint pair satisfies

```text
boxed:
n>1 squarefree.                                        (3.1)
```

---

## 4. Rational torsion on E_n

For squarefree `n>1`, merged 4bt proves

```text
boxed:
E_n(Q)_tors = {O,(0,0)} ~= Z/2Z.                      (4.1)
```

The mechanism is important for the s7 receiver:

1. `E_n: Y^2=X^3+4n^2X` has the unique rational 2-torsion point `(0,0)`.
2. Rational 4-torsion would require a rational half of `(0,0)`.  The duplication equation forces `x=2n` on the positive branch, which gives `y^2=16n^3`; this is rational only when `n` is a square.  Squarefree `n>1` excludes it.
3. Standard rational-torsion reduction, as frozen in merged 4bt, excludes the remaining odd torsion possibilities.

Thus there is only one nontrivial rational torsion translation to classify on the quartic torsor.

---

## 5. The unique torsion self-correspondence on the quartic

On

```text
C_{k,xi}: k*y^2=1-xi^2*z^4
```

consider

```text
tau(z,y)=(-z,-y).                                     (5.1)
```

This is a fixed-point-free involution on the smooth genus-one model.  Once any rational point is chosen as origin, a fixed-point-free involution of order two is translation by a nonzero 2-torsion point.  By (4.1), the only possible rational nonzero torsion point is `(0,0)` on `E_n`.

Therefore `tau` is exactly the unique nontrivial rational torsion self-correspondence relevant to a rational two-point difference.

The physical representatives use the canonical positive lifts

```text
z1>0,
z2>0.
```

Hence

```text
(z2,y2) != tau(z1,y1),                                (5.2)
```

because `tau` changes the sign of the `z` coordinate.

They are also not equal, since `w<u` implies `z2<z1`.

Thus the difference of the two physical points is neither the identity nor the unique nonzero rational torsion point.

Consequently

```text
boxed:
P2-P1 in E_n(Q) has infinite order.                    (5.3)
```

In particular

```text
boxed:
physical joint pair => rank E_n(Q) >= 1.               (5.4)
```

This upgrades the unresolved flag from s7-05.

---

## 6. Collapse from the ordered factorization (k,xi) to n

Because `n` is squarefree and `gcd(k,xi)=1`, the number of ordered factorizations

```text
n=k*xi
```

is exactly bounded by

```text
2^omega(n)=n^o(1).
```

For a reduced coordinate `P/Q`,

```text
n = ker(PQ(Q-P)(Q+P)) < Q^4.
```

Applying this to the two physical coordinates gives

```text
n < Q^4,
n < S^4.
```

Since s7-03/s7-04 give

```text
QS = H_mult << B,
```

we retain the safe physical bound

```text
boxed:
n << B^2.                                             (6.1)
```

Thus `(k,xi)` contributes only a subpolynomial factor over a one-dimensional squarefree twist parameter `n`.

---

## 7. First two-point height receiver

Define `H_2(n)` to be the least product `QS` over all data satisfying:

- `n=k*xi` with `k,xi` coprime positive squarefree;
- two distinct canonical positive rational points on `C_{k,xi}`;
- the physical open inequalities `0<w<u<1`;
- the inverse reconstruction conditions from s7-05.

By Section 5, every such physical pair automatically has infinite-order difference on `E_n`.

Therefore the physical family admits the one-dimensional receiver

```text
V(B)
 << B^o(1)
    # { squarefree n << B^2 : H_2(n) << B }.
```

Equivalently, the positive-rank condition is no longer a separate uncertainty:

```text
H_2(n)<infinity in the physical open
=> rank E_n(Q)>=1.
```

The converse remains false: a positive-rank `E_n` need not supply two admissible small points on the required torsor factorization.

---

## 8. Relation to the current main-line barrier

Merged 4br/4bs prove

```text
V(B) << B^(20/21+o(1))
```

and that the previous size-splitting architecture cannot improve this exponent.

Hence s7 should not replace `H_2(n)` merely by positive rank.  The new counting object must retain the first-two-point height / denominator hyperbola.

To beat the current `20/21` ceiling, a direct twist-family count must save more than `1/21` relative to a `B^(1+o(1))` ambient joint-denominator count.  If one Cauchy square root is used, the squared-energy input must save more than `2/21`.

Open Stage14-4bu is compatible with this receiver and further isolates a balanced denominator strip, but it is not used as a theorem input in this stage.

---

## 9. Boundary

```text
STAGE14_S7_06=COMPLETE_SQUAREFREE_J1728_TORSION_SELF_CORRESPONDENCE_EXCLUSION
MERGED_S7_05_IMPORTED=true
MERGED_4BT_TORSION_GATE_IMPORTED=true
XI_K_COPRIME=true
TWIST_PARAMETER_N=k*xi
TWIST_PARAMETER_N_SQUAREFREE=true
PHYSICAL_TWIST_PARAMETER_N_GT_1=true
TWIST_JACOBIAN=y^2=x^3+4*n^2*x
SQUAREFREE_N_GT_1_RATIONAL_TORSION=Z/2Z
UNIQUE_NONTRIVIAL_TORSION_SELF_CORRESPONDENCE=(z,y)->(-z,-y)
PHYSICAL_POSITIVE_LIFTS_EXCLUDE_TORSION_SELF_CORRESPONDENCE=true
PHYSICAL_TWO_POINT_DIFFERENCE_TORSION=false
PHYSICAL_TWO_POINT_DIFFERENCE_INFINITE_ORDER=true
PHYSICAL_TWIST_PAIR_IMPLIES_POSITIVE_RANK_ON_E_N=true
FIXED_N_FACTORISATION_MULTIPLICITY=B^o(1)
PHYSICAL_TWIST_PARAMETER_BOUND=B^2
ONE_DIMENSIONAL_SQUAREFREE_TWIST_FIRST_TWO_POINT_RECEIVER=true
POSITIVE_RANK_ALONE_IMPLIES_PHYSICAL_FIRST_TWO_POINT=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=20/21
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-s7-07
```

## Next

Stage14-s7-07 should count squarefree `j=1728` twists carrying two admissible positive rational points with `H_2(n)<<B`, retaining the denominator hyperbola.  If merged 4bu is available by then, import its exact fixed-quartic balanced-strip reduction and inert-prime zero trace rather than rederiving them.