# Stage14-X5 — eliminate quadratic cyclotomic branches and expose the four-sign reciprocal linear cycle

## Status

`COMPLETE_QUADRATIC_CYCLOTOMIC_BRANCH_ELIMINATION_AND_FOUR_SIGN_LINEAR_CYCLE_REDUCTION`

Stage14-X4 leaves the charged-once X-route receiver

```text
OffDiagonalReciprocalCyclotomicQuarticAllocationIncidence
```

with the nine dominant branch labels inherited from merged Stage14-4cl:

```text
(-,-), (-,+), (-,i),
(+,-), (+,+), (+,i),
(i,-), (i,+), (i,i).
```

The `i` label comes from the quadratic cyclotomic factor `b^2+a^2` in a fourth-difference factorization.  Stage14-4cl proves only that an odd prime on such a branch is `1 mod 4`.

Stage14-X5 reconnects that branch decomposition to the older merged Stage14-4cg common-core coprimality locks.  This kills both quadratic branches **exactly**.  Hence the nine branch types collapse to the four linear-linear sign types

```text
(-,-), (-,+), (+,-), (+,+).
```

Moreover the entire odd agreement products are forced into the two linear factors, and the complementary linear quotients multiply exactly to the reduced residuals `u` and `v`.  On the current proved top-theta saturation edge from merged Stage14-s7-25, the dominant linear moduli improve from the 4cl cube-root bounds to square-root bounds:

```text
xi-side dominant modulus >= B^(phi-o(1)),
k-side  dominant modulus >= B^(5/16-o(1)),
```

and the corresponding two dominant linear quotients have total exponent at most `1/8`.

No whole-family power saving is promoted.  The current unconditional bound remains

```text
V(B) << B^(7/8+o(1)).
```

The new minimal X receiver is

```text
FourSignReciprocalLinearFactorCycleIncidence.
```

No canonical index or exponent ledger is modified.

---

## 1. Imported charged-once physical packet

Retain the X1 -> X4 quantifier order.  After the `B^o(1)` endpoint-small and moving-gcd refinements, write

```text
A = alpha*r,
D = delta*s,
U0 = R*X,
V0 = J*Y,

Xi_ag = R*J,
K_ag  = alpha*delta,
```

where

```text
D>A>0,
V0>U0>0,

gcd(alpha,delta)=1,
gcd(R,J)=1,
gcd(Xi_ag,K_ag)=1.
```

The common-core factors of merged 4cg are exactly

```text
H_k^+  = D^2 + A^2,
H_k^-  = D^2 - A^2,
H_xi^+ = V0^2 + U0^2,
H_xi^- = V0^2 - U0^2.                         (1.1)
```

The post-4cg residual norms are

```text
q_k  = C*u,
q_xi = C*v.                                      (1.2)
```

Stage14-X5 does not form a new coefficient space.  It only intersects the merged 4cl cyclotomic allocation with exact 4cg identities already valid on the same physical pair.

---

## 2. The forgotten 4cg coprimality locks

Merged 4cg proves, primewise on the same packet,

```text
gcd(H_k^+,  oddpart(Xi_ag)) = 1,              (2.1)
gcd(H_xi^+, oddpart(K_ag))  = 1.              (2.2)
```

These are stronger than the generic statement that agreement primes are coprime to the opposite bases.  They say that an agreement prime cannot divide the **plus common-core factor itself**.

Merged 4cl also proves

```text
Xi_ag | D^4-A^4 = H_k^+ H_k^-,                (2.3)
K_ag  | V0^4-U0^4 = H_xi^+ H_xi^-.            (2.4)
```

Taking odd parts and using (2.1)-(2.2), Euclid's lemma gives

```text
boxed:
oddpart(Xi_ag) | H_k^- = D^2-A^2,              (2.5)

boxed:
oddpart(K_ag)  | H_xi^- = V0^2-U0^2.           (2.6)
```

Thus the agreement moduli never use the quadratic plus factor.

---

## 3. Both `i` branches are exactly empty

Stage14-4cl defines

```text
M_xi^i = gcd(oddpart(Xi_ag), D^2+A^2),
M_k^i  = gcd(oddpart(K_ag),  V0^2+U0^2).        (3.1)
```

By (1.1) and (2.1)-(2.2), immediately

```text
boxed:
M_xi^i = 1,
M_k^i  = 1.                                     (3.2)
```

Therefore every physical off-diagonal X packet satisfies

```text
XI_QUADRATIC_CYCLOTOMIC_BRANCH_NONTRIVIAL=false,
K_QUADRATIC_CYCLOTOMIC_BRANCH_NONTRIVIAL=false.  (3.3)
```

This is an asymptotic exact theorem, not a finite inference.

The finite 4cl audit had already shown the unexplained diagnostic

```text
nontrivial quadratic branch occurrences = 0
```

on all 37 dual-cross pairs through `Q<=420`.  X5 explains that zero structurally.

Consequently the nine 4cl branch types reduce exactly to

```text
boxed:
(-,-), (-,+), (+,-), (+,+).                    (3.4)
```

---

## 4. Exact two-way linear allocation

Define the remaining branch moduli

```text
M_xi^- = gcd(oddpart(Xi_ag), D-A),
M_xi^+ = gcd(oddpart(Xi_ag), D+A),

M_k^-  = gcd(oddpart(K_ag), V0-U0),
M_k^+  = gcd(oddpart(K_ag), V0+U0).              (4.1)
```

Because every odd agreement prime is coprime to the opposite bases, the two linear factors on each side are coprime on agreement support.  Combining (2.5)-(2.6) with

```text
H_k^-  = (D-A)(D+A),
H_xi^- = (V0-U0)(V0+U0),                         (4.2)
```

gives the exact products

```text
boxed:
M_xi^- * M_xi^+ = oddpart(Xi_ag),                (4.3)

boxed:
M_k^-  * M_k^+  = oddpart(K_ag).                 (4.4)
```

Hence the physical agreement products are **entirely linear-cyclotomic**.

There is no third large branch and no `3^omega` branch allocation any more.  Conditioning on the two signs costs only the constant four branch types.

---

## 5. The linear quotients multiply to the reduced residuals

Merged 4cg / s7-25 gives the exact common-core cancellation

```text
xi*q_k = H_k^+ H_k^-,
q_k=C*u,
oddpart(H_k^+) = C*oddpart(S*T),                  (5.1)
```

and symmetrically

```text
k*q_xi = H_xi^+ H_xi^-,
q_xi=C*v,
oddpart(H_xi^+) = C*oddpart(beta*gamma).           (5.2)
```

Since

```text
xi=(S*T)*Xi_ag,
k=(beta*gamma)*K_ag,
```

taking odd parts in (5.1)-(5.2) and cancelling the common core and switch products yields

```text
boxed:
oddpart(H_k^-) = oddpart(Xi_ag)*oddpart(u),        (5.3)

boxed:
oddpart(H_xi^-) = oddpart(K_ag)*oddpart(v).        (5.4)
```

Now define positive odd linear quotients

```text
Q_xi^- = oddpart(D-A)  / M_xi^-,
Q_xi^+ = oddpart(D+A)  / M_xi^+,

Q_k^-  = oddpart(V0-U0) / M_k^-,
Q_k^+  = oddpart(V0+U0) / M_k^+.                  (5.5)
```

Equations (4.2)-(5.4) give the exact residual-product identities

```text
boxed:
Q_xi^- * Q_xi^+ = oddpart(u),                     (5.6)

boxed:
Q_k^-  * Q_k^+  = oddpart(v).                     (5.7)
```

Thus for fixed charged-once residual triple `(C,u,v)`, the four quotient factors have only

```text
tau(u)*tau(v)=B^o(1)                              (5.8)
```

possible odd allocations, up to the already-fixed finite 2-primary and moving-gcd refinements.

This is the key X5 compression: the fixed-power freedom is now entirely in the four linear agreement moduli, not in an additional cyclotomic or residual branch.

---

## 6. Four-sign reciprocal linear factor cycle

After fixing the harmless quotient allocation and 2-primary data, the four linear equations have the shape

```text
D-A   = 2^a_- M_xi^- Q_xi^-,
D+A   = 2^a_+ M_xi^+ Q_xi^+,

V0-U0 = 2^b_- M_k^- Q_k^-,
V0+U0 = 2^b_+ M_k^+ Q_k^+.                       (6.1)
```

Hence

```text
A = [(D+A)-(D-A)]/2,
D = [(D+A)+(D-A)]/2,

U0 = [(V0+U0)-(V0-U0)]/2,
V0 = [(V0+U0)+(V0-U0)]/2.                         (6.2)
```

The physical cell conditions then require

```text
A/r = alpha,
D/s = delta,
U0/X = R,
V0/Y = J,                                         (6.3)
```

and reciprocally

```text
alpha*delta = M_k^- M_k^+ * (2-primary),
R*J         = M_xi^- M_xi^+ * (2-primary).        (6.4)
```

Equations (6.1)-(6.4), together with the 4x4 good-prime allocation and original reconstruction masks, define the exact remaining object

```text
FourSignReciprocalLinearFactorCycleIncidence.      (6.5)
```

It is strictly narrower than the X4 receiver: quadratic branches and free residual quotients have both been removed.

A generic binary-quartic energy theorem is still an illegal enlargement because it discards (6.4) and the charged-once common-core provenance.

---

## 7. Improved dominant-modulus bounds

Because there are only two branch factors now, (4.3)-(4.4) imply

```text
max(M_xi^-,M_xi^+) >= oddpart(Xi_ag)^(1/2),        (7.1)
max(M_k^-, M_k^+)  >= oddpart(K_ag)^(1/2).         (7.2)
```

In a balanced `(theta,phi)` block,

```text
R,J = B^(phi+o(1)),
alpha,delta = B^(theta+o(1)),                      (7.3)
```

so the dominant linear moduli satisfy

```text
boxed:
M_xi,dom >= B^(phi-o(1)),                          (7.4)

boxed:
M_k,dom >= B^(theta-o(1)).                         (7.5)
```

This strictly improves the 4cl three-way bounds

```text
B^(2phi/3), B^(2theta/3).
```

---

## 8. Current top-theta edge and the `1/8` dominant-quotient budget

Merged Stage14-s7-25 changed the proved saturation locus from the older conditional single corner to the unconditional top-theta edge

```text
theta=5/16,
3/16 <= phi <= 1/4.                                (8.1)
```

X5 uses this only as a scale ledger; it does not multiply independent savings.

On this edge,

```text
D+A <= B^(theta+o(1)) = B^(5/16+o(1)),             (8.2)
V0+U0 <= B^(phi+1/8+o(1)).                         (8.3)
```

Let `sigma_xi,sigma_k in {-,+}` be signs attaining the dominant moduli in (7.4)-(7.5), and define the corresponding full linear quotients (including the fixed 2-primary convention)

```text
T_xi = (D sigma_xi A)/M_xi,dom,
T_k  = (V0 sigma_k U0)/M_k,dom.                    (8.4)
```

Then

```text
T_xi <= B^(theta-phi+o(1)),                        (8.5)
T_k  <= B^(phi+1/8-theta+o(1)).                    (8.6)
```

The common-core strip gives both exponents nonnegative.  Multiplying them cancels `theta,phi`:

```text
boxed:
T_xi*T_k <= B^(1/8+o(1)).                          (8.7)
```

More explicitly on the top edge,

```text
log_B T_xi <= 5/16-phi in [1/16,1/8],
log_B T_k  <= phi-3/16 in [0,1/16].                (8.8)
```

At the lower endpoint `phi=3/16`, the k-side dominant linear factor is saturated up to `B^o(1)` quotient.  At the upper endpoint `phi=1/4`, both dominant quotients are at most `B^(1/16+o(1))`.

The product of the two dominant moduli itself has exponent at least

```text
theta+phi >= 1/2,                                  (8.9)
```

rising to `9/16` at `phi=1/4`.

These are exact scale consequences of the two-way branch elimination; no distributional saving is inserted.

---

## 9. What X5 closes and what remains

X5 closes:

```text
- both nontrivial quadratic cyclotomic `i` branches;
- all five branch types containing `i`;
- the three-way agreement-prime allocation on each reciprocal side;
- the apparent free residual slack inside the linear factors;
- the old cube-root dominant-modulus ledger.
```

The surviving four branches are

```text
(-,-), (-,+), (+,-), (+,+).
```

Finite physical data through `Q<=420` realize all four, so none is removed by a finite-pattern assertion.

X5 does **not** prove a fixed-power bound for

```text
FourSignReciprocalLinearFactorCycleIncidence.
```

In particular, the fact that the quotient allocations are divisor-many for fixed `(C,u,v)` does not by itself count the mutually generated large moduli `M_xi^±,M_k^±`.

Therefore

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false.
```

---

## 10. H / tH decision

No X5-specific H line is needed.

The new gain is exact algebraic structure from merged 4cg + 4cl + s7-25.  Before asking for a large-sieve or external incidence theorem, X6 should exploit the four linear equations (6.1), reciprocal product constraints (6.4), and the `T_xi*T_k<=B^(1/8+o(1))` quotient budget.

A generic quartic-energy or generic cyclotomic-incidence theorem would still enlarge the coefficient space prematurely.

```text
X5_AUXILIARY_H_NEEDED=false
X_ROUTE_BLOCKED_BY_H=false.
```

---

## Boundary

```text
STAGE14_X5=COMPLETE_QUADRATIC_CYCLOTOMIC_BRANCH_ELIMINATION_AND_FOUR_SIGN_LINEAR_CYCLE_REDUCTION
MERGED_X4_IMPORTED=true
MERGED_4CG_COMMON_CORE_IMPORTED=true
MERGED_4CL_CYCLOTOMIC_ALLOCATION_IMPORTED=true
MERGED_S7_25_TOP_EDGE_LEDGER_IMPORTED=true
X1_CHARGED_ONCE_QUANTIFIER_ORDER_PRESERVED=true
XI_PLUS_COMMON_CORE_COPRIME_TO_AGREEMENT=true
K_PLUS_COMMON_CORE_COPRIME_TO_AGREEMENT=true
ODD_XI_AGREEMENT_DIVIDES_HK_MINUS=true
ODD_K_AGREEMENT_DIVIDES_HXI_MINUS=true
XI_QUADRATIC_CYCLOTOMIC_BRANCH_NONTRIVIAL=false
K_QUADRATIC_CYCLOTOMIC_BRANCH_NONTRIVIAL=false
CYCLOTOMIC_BRANCH_TYPES_REDUCED_FROM_9_TO_4=true
SURVIVING_BRANCH_TYPES=(-,-),(-,+),(+,-),(+,+)
XI_LINEAR_BRANCH_PRODUCT=oddpart(R*J)
K_LINEAR_BRANCH_PRODUCT=oddpart(alpha*delta)
XI_LINEAR_QUOTIENT_PRODUCT=oddpart(u)
K_LINEAR_QUOTIENT_PRODUCT=oddpart(v)
XI_DOMINANT_LINEAR_MODULUS_EXPONENT=phi
K_DOMINANT_LINEAR_MODULUS_EXPONENT=theta
TOP_THETA_EDGE=theta=5/16,phi_in_[3/16,1/4]
TOP_EDGE_DOMINANT_QUOTIENT_PRODUCT_EXPONENT_LE=1/8
FOUR_SIGN_RECIPROCAL_LINEAR_FACTOR_CYCLE_INCIDENCE_PROVED=false
REMAINING_RECEIVER=FourSignReciprocalLinearFactorCycleIncidence
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
X5_AUXILIARY_H_NEEDED=false
X_ROUTE_BLOCKED_BY_H=false
NEXT_RECOMMENDED=Stage14-X6 attack the four reciprocal linear sign cycles using the exact quotient-factor identities and the 1/8 dominant-quotient budget
```