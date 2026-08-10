# Stage14-4ce — dual allocation injectivity and double-disagreement switch packet

## Status

`COMPLETE_DUAL_ALLOCATION_INJECTIVITY_AND_DOUBLE_DISAGREEMENT_REDUCTION`

Stage14-4cd localized every block that can still saturate the current whole-family exponent `7/8` to the maximal-difference-kernel endpoint

```text
P,Q,Q-P,Q+P = B^(1/2+o(1)),
xi=ker(PQ)   = B^(3/4+o(1)),
k=ker(Q^2-P^2)=B^(1+o(1)).
```

Merged Stage14-s7-18 then proved the `k=k_-k_+` allocation theorem: same-split critical collisions are impossible and any remaining cross-split collision has a switching product

```text
K_switch >= B^(3/8-o(1))
```

on the 4cd endpoint.

Stage14-4ce proves the exact dual theorem on the `xi=a*b` allocation.  The two reductions combine to show that every remaining endpoint collision must simultaneously move a positive-power part of both squarefree labels, with all odd switching primes split in `Q(i)`.

No auxiliary H line is created and no unproved t/tH selector theorem is imported.

---

## 1. Canonical xi coordinates

For a reduced coordinate

```text
0<P<Q<=X,
gcd(P,Q)=1,
```

write

```text
P=a*x^2,
Q=b*y^2,
```

with `a,b` squarefree.  Reducedness gives

```text
gcd(a,b)=1,
gcd(x,y)=1,
xi=a*b=ker(PQ).
```

Also write

```text
Q^2-P^2=k*h^2
```

with `k` squarefree.  Since a prime dividing `xi` divides exactly one of `P,Q`, it cannot divide `Q^2-P^2`.  Hence

```text
boxed:
gcd(xi,k*h)=1.                                      (1.1)
```

The basic quartic identity is

```text
boxed:
b^2*y^4-a^2*x^4=k*h^2.                            (1.2)
```

The elementary size bounds are

```text
x^2 <= X/a,
y^2 <= X/b,
h^2 <= X^2/k.                                       (1.3)
```

This is the exact xi-side dual of the split-k quartic used in merged s7-18.

---

## 2. Fixed xi split is injective once xi^2 k dominates X^4

Take two reduced states with the same

```text
xi,
k,
a,b
```

and possibly different square roots `(x_i,y_i,h_i)`:

```text
b^2 y_1^4-a^2 x_1^4=k h_1^2,
b^2 y_2^4-a^2 x_2^4=k h_2^2.                       (2.1)
```

Cross multiplication gives

```text
b^2(y_1^4 h_2^2-y_2^4 h_1^2)
 =a^2(x_1^4 h_2^2-x_2^4 h_1^2).                   (2.2)
```

Because `gcd(a,b)=1`,

```text
a^2 | y_1^4 h_2^2-y_2^4 h_1^2,
b^2 | x_1^4 h_2^2-x_2^4 h_1^2.                    (2.3)
```

By (1.3),

```text
|y_1^4 h_2^2-y_2^4 h_1^2| <= 2 X^4/(b^2 k),
|x_1^4 h_2^2-x_2^4 h_1^2| <= 2 X^4/(a^2 k).        (2.4)
```

Therefore if

```text
boxed:
xi^2*k > 2 X^4,                                    (2.5)
```

both brackets vanish.  Positivity gives

```text
y_1^2 h_2=y_2^2 h_1,
x_1^2 h_2=x_2^2 h_1,
```

hence `x_1/y_1=x_2/y_2`.  Both pairs `(x_i,y_i)` are primitive, so they agree, and then `(P,Q)` agree.

Thus

```text
XiFixedSplitInjectivity:
if xi^2*k>2X^4, a fixed coprime squarefree allocation xi=a*b
contains at most one reduced state with a given k.
```

At the old `7/8` shell `xi=B^(3/4+o(1))`, `k>=B^(3/4-o(1))`, `X<=B^(1/2+o(1))`, the left exponent is at least `9/4`, leaving fixed-power room `1/4` over `2`.

---

## 3. Two different xi splits: exact four-cell decomposition

For two states with the same `xi` write

```text
a_1=A*B,   b_1=C*D,
a_2=A*C,   b_2=B*D,
```

where `A,B,C,D` are unique pairwise-coprime squarefree cells and

```text
A*B*C*D=xi.                                         (3.1)
```

Define

```text
Xi_agree=A*D,
Xi_switch=B*C=xi/Xi_agree.                          (3.2)
```

`Xi_switch=1` exactly when the two `a/b` allocations are the same.

The two quartics are

```text
(CD)^2 y_1^4-(AB)^2 x_1^4=k h_1^2,
(BD)^2 y_2^4-(AC)^2 x_2^4=k h_2^2.                 (3.3)
```

Cross multiplication yields

```text
D^2(C^2 y_1^4 h_2^2-B^2 y_2^4 h_1^2)
 =A^2(B^2 x_1^4 h_2^2-C^2 x_2^4 h_1^2).           (3.4)
```

Hence

```text
A^2 | C^2 y_1^4 h_2^2-B^2 y_2^4 h_1^2,
D^2 | B^2 x_1^4 h_2^2-C^2 x_2^4 h_1^2.            (3.5)
```

The same size calculation as before gives

```text
|C^2 y_1^4 h_2^2-B^2 y_2^4 h_1^2|
 <=2X^4/(D^2 k),

|B^2 x_1^4 h_2^2-C^2 x_2^4 h_1^2|
 <=2X^4/(A^2 k).                                    (3.6)
```

If

```text
(Xi_agree)^2*k>2X^4,                               (3.7)
```

both brackets vanish.  If `B>1`, a prime `ell|B` divides the right-hand side of the first vanishing equality but cannot divide the left-hand side, using pairwise cell coprimality and (1.1).  Therefore `B=1`; similarly `C=1`.  The splits coincide, and Section 2 then forces the states to coincide.

Thus every off-diagonal same-`(xi,k)` collision satisfies

```text
boxed:
(Xi_agree)^2*k <= 2X^4.                             (3.8)
```

Equivalently

```text
boxed:
Xi_switch >= xi*sqrt(k)/(sqrt(2)*X^2).              (3.9)
```

At exponent scale, if `xi~B^gamma`, `k~B^kappa`, `X<=B^(1/2+o(1))`,

```text
log_B Xi_switch >= gamma+kappa/2-1-o(1).           (3.10)
```

Consequences:

```text
old 7/8 residual: gamma=3/4, kappa>=3/4
=> Xi_switch >= B^(1/8-o(1));

4cd maximal-k endpoint: gamma=3/4, kappa=1
=> Xi_switch >= B^(1/4-o(1)).                       (3.11)
```

---

## 4. Combine with merged s7-18: double disagreement

Merged s7-18 applies the same integer-divisibility architecture to the `k=k_-k_+` allocation and proves, for every off-diagonal same-`(xi,k)` collision,

```text
K_switch >= k*sqrt(xi)/(sqrt(32)*X^2).              (4.1)
```

Therefore on the 4cd endpoint

```text
boxed:
Xi_switch >= B^(1/4-o(1)),
K_switch  >= B^(3/8-o(1)).                          (4.2)
```

In particular

```text
boxed:
Xi_switch*K_switch >= B^(5/8-o(1)).                 (4.3)
```

This is the new canonical hard packet.  A remaining collision cannot be explained by a small change of one divisor allocation: it must change a positive-power portion of both the product-kernel label and the difference-kernel label.

---

## 5. Every odd switching prime is 1 mod 4

Merged 4cd proved the endpoint residue signature for every odd prime `ell`:

```text
ell|a   => ( k/ell)=+1,
ell|b   => (-k/ell)=+1,
ell|k_- => ( xi/ell)=+1,
ell|k_+ => (-xi/ell)=+1.                           (5.1)
```

Now let `ell` be an odd prime dividing an xi-switch cell, say `B`.  In state 1 it lies in `a_1`, while in state 2 it lies in `b_2`.  Thus both

```text
(k/ell)=+1,
(-k/ell)=+1.
```

Since `ell∤k`, division gives

```text
(-1/ell)=+1,
```

so

```text
boxed:
ell == 1 (mod 4).                                  (5.2)
```

The same holds for primes in `C`.

Likewise, if an odd prime `p` divides a k-switch cell, then it is in `k_-` for one state and `k_+` for the other.  Hence

```text
(xi/p)=+1,
(-xi/p)=+1,
```

and therefore

```text
boxed:
p == 1 (mod 4).                                    (5.3)
```

Consequently all odd primes `3 mod 4` are frozen across a same-`(xi,k)` collision fiber: they cannot switch `a/b` side and cannot switch `k_-/k_+` side.

Equivalently, all nontrivial allocation freedom lives on the Gaussian-split prime support.

This is exact but only a logarithmic-density restriction by itself; it is **not** promoted to a fixed-power saving.

---

## 6. Coupled switch-prime residue graph

The switch support also retains statewise quadratic information.  For every odd prime

```text
ell | Xi_switch
```

we have

```text
(k/ell)=+1,                                         (6.1)
```

and for every odd prime

```text
p | K_switch
```

we have

```text
(xi/p)=+1.                                          (6.2)
```

Together with `(5.2)-(5.3)`, the live endpoint is therefore a genuinely coupled mutual-residue incidence between two large split-prime products, not two independent divisor fans.

We name the next receiver

```text
CoupledDoubleSwitchQuadraticResidueIncidence.
```

It must preserve

```text
Xi_agree, Xi_switch,
K_agree,  K_switch,
xi, k,
physical branch/orientation and reconstruction masks.
```

Forbidden shortcuts:

- multiply local `1/2` residue densities as if independent;
- replace `1 mod 4` support by a fixed-power sparsity claim;
- collapse to raw `(xi,k)` before exploiting both switch products;
- import tH14/t55 squareclass energy as if the physical fiber theorem were proved.

---

## 7. Why the current exponent remains 7/8

For fixed squarefree `xi` or `k`, the number of coprime divisor allocations is `2^omega(.)=B^o(1)`.  Requiring a large switching divisor does not by itself make the allocation count power-small.

Likewise, squarefree integers supported on primes `1 mod 4` have only logarithmic, not fixed-power, sparsity.  Therefore Sections 4-6 do not alone produce a new power of `B`.

The unconditional whole-family bound remains

```text
boxed:
V(B) << B^(7/8+o(1)).
```

The gain of 4ce is structural: the unresolved endpoint is now a double-large-switch, split-prime, mutual-quadratic-residue packet.

---

## 8. H-line decision

The user requested that the 14-4 mainline not create a blocking H line.  Nothing in this stage requires one.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
```

The t-route may independently use tH15 for `SharedUBipartiteSquareclassEnergy`; that is a separate route and is not a prerequisite for 14-4ce or 14-4cf.

---

## 9. Stage boundary

```text
STAGE14_4CE=COMPLETE_DUAL_ALLOCATION_INJECTIVITY_AND_DOUBLE_DISAGREEMENT_REDUCTION
MERGED_4CD_IMPORTED=true
MERGED_S7_18_IMPORTED=true
XI_FIXED_SPLIT_INJECTIVE_IF_xi2_k_GT_2_X4=true
XI_CROSS_SPLIT_AGREEMENT_NECESSARY_BOUND=(Xi_agree)^2*k<=2*X^4
XI_SWITCH_LOWER_BOUND=xi*sqrt(k)/(sqrt(2)*X^2)
OLD_CRITICAL_XI_SWITCH_LOWER_EXPONENT=1/8
FOUR_CD_ENDPOINT_XI_SWITCH_LOWER_EXPONENT=1/4
FOUR_CD_ENDPOINT_K_SWITCH_LOWER_EXPONENT=3/8
FOUR_CD_ENDPOINT_DOUBLE_SWITCH_PRODUCT_LOWER_EXPONENT=5/8
ODD_XI_SWITCH_PRIMES_ARE_1_MOD_4=true
ODD_K_SWITCH_PRIMES_ARE_1_MOD_4=true
INERT_3_MOD_4_ALLOCATION_FROZEN=true
COUPLED_SWITCH_PRIME_RESIDUE_GRAPH_EXACT=true
COUPLED_DOUBLE_SWITCH_QUADRATIC_RESIDUE_INCIDENCE_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4cf
```
