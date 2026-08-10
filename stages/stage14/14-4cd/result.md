# Stage14-4cd — four-root lattice congruence and maximal-k endpoint localization

## Purpose

Merged Stage14-4cc leaves the current unconditional whole-family bound

```text
V(B) << B^(7/8+o(1))
```

and localizes any block capable of approaching that ceiling to the shorter reduced coordinate

```text
u=P/Q,
0<P<Q,
gcd(P,Q)=1,
P,Q~B^(1/2),
xi=ker(PQ)~B^(3/4),
k=ker(Q^2-P^2)>=B^(3/4-o(1)).
```

Stage14-4cd combines the canonical square-part roots of all four linear factors

```text
P,
Q,
Q-P,
Q+P
```

before any square sieve.  The four roots force an exact rank-one congruence lattice on the two squarefree factors of `k`.  This yields the new support law

```text
N_critical(d,kappa)
 << B^(1/8+(d+kappa)/2+o(1)),
```

where

```text
Q-P~B^d,
k~B^kappa.
```

Hence every fixed-power departure from either `d=1/2` or `kappa=1` is already strictly below `7/8`.  The only residual capable of saturating the current exponent lies at

```text
Q-P~B^(1/2),
k=B^(1-o(1)),
```

with both normalized difference factors essentially squarefree.

No unproved selector-sensitive Gaussian completion, principal squareclass estimate, or centered collision theorem is used.

---

## 1. Merged inputs and transfer level

### 1.1 Current critical coordinate shell

Merged s7-13 / 4cb / 4cc give, on any block approaching `7/8`,

```text
P=a*x^2,
Q=b*y^2,
a,b squarefree,
a,b~B^(3/8),
x,y~B^(1/16),
xi=a*b=ker(PQ)~B^(3/4).
```

Because

```text
P*Q = xi*(x*y)^2 ~ B,
```

we have

```text
x*y = B^(1/8+o(1)).                                (1.1)
```

The merged fixed-coordinate genus-one receiver used by s7-13 gives only `B^o(1)` physical partner multiplicity once the shorter reduced coordinate is fixed.  Therefore a support bound for `(P,Q)` transfers to the physical whole-family count with the same fixed-power exponent.

### 1.2 Difference-kernel split

Merged s7-15 gives

```text
g = gcd(Q-P,Q+P) in {1,2},
A = (Q-P)/g,
C = (Q+P)/g,
gcd(A,C)=1,
A = k_-*r^2,
C = k_+*s^2,
```

where

```text
k_-,k_+ squarefree,
gcd(k_-,k_+)=1,
k=k_-*k_+=ker(Q^2-P^2).                            (1.2)
```

### 1.3 tH14 R2 / t52 boundary

The canonical merged tH14 import is R2.  It proves the product-row quadratic-large-sieve adapter after the t32 physical completion, but explicitly leaves

```text
PhysicalWeightedSquareclassFiberEnergy
```

unproved.  Merged t52 further shows that treating selector-sensitive Gaussian completion as an independent black box would hide the global principal squareclass problem.

Stage14-4cd imports only those proved boundaries.  It does not use

```text
PhysicalWeightedSquareclassFiberEnergy,
SelectorSensitiveGaussianCompletion,
CenteredXiKCollisionSecondMoment,
GenericCrossGoodLD2KummerPrincipalIncidence.
```

No additional 14-4 supervisor/H branch is required for this stage.

---

## 2. Coprimality of the four canonical roots

Write

```text
P = a*x^2,
Q = b*y^2,
A = k_-*r^2,
C = k_+*s^2.
```

Primitive reducedness gives

```text
gcd(x,y)=1,
gcd(r,s)=1.                                        (2.1)
```

More strongly,

```text
gcd(x*y,r*s)=1.                                    (2.2)
```

For an odd prime `ell`, if `ell|x` and `ell|r`, then `ell|P` and `ell|(Q-P)`, hence `ell|Q`, contradicting `gcd(P,Q)=1`.  The other three cross-pairs are identical.

At `ell=2`, if `g=1`, then `P,Q` have opposite parity and `Q-P,Q+P` are odd, so `r,s` are odd.  If `g=2`, then `P,Q` are both odd, so `x,y` are odd.  Thus no factor 2 is shared either.

Consequently `r*s` is a unit modulo `x^2*y^2`.

---

## 3. Exact rank-one congruence lattice

From

```text
Q-P = g*k_-*r^2,
Q+P = g*k_+*s^2
```

we get

```text
2P = g*(k_+*s^2-k_-*r^2),
2Q = g*(k_+*s^2+k_-*r^2).
```

Put

```text
c_g=2/g in {1,2}.
```

Using `P=a*x^2`, `Q=b*y^2`,

```text
k_+*s^2-k_-*r^2 = c_g*a*x^2,                     (3.1)
k_+*s^2+k_-*r^2 = c_g*b*y^2.                     (3.2)
```

Hence

```text
k_+*s^2 ==  k_-*r^2 (mod x^2),                   (3.3)
k_+*s^2 == -k_-*r^2 (mod y^2).                   (3.4)
```

By (2.2), `r*s` is invertible modulo `x^2*y^2`, while `gcd(x,y)=1`.  CRT therefore produces a unique unit

```text
lambda=lambda(x,y,r,s) mod M,
M=x^2*y^2,
```

such that

```text
k_+ == lambda*k_- (mod M).                         (3.5)
```

Thus the two moving squarefree difference kernels lie in one determinant-`M` rank-one congruence lattice.  This is an exact pre-sieve dimension reduction and uses no character cancellation.

---

## 4. Lattice-box count

Dyadically fix

```text
x~X,
y~Y,
r~R,
s~S,
k_-~K_-,
k_+~K_+.
```

For fixed roots, dropping squarefreeness and coprimality only enlarges the set.  The number of kernel pairs satisfying (3.5) obeys

```text
N_lattice
 << K_-*K_+/M + K_- + K_+ + 1,
M=X^2*Y^2.                                         (4.1)
```

Indeed, for each `k_-`, one residue class modulo `M` is allowed for `k_+`; the displayed symmetric form safely absorbs the rectangle boundary.

There are `O(XYRS)` root quadruples, so

```text
N_block
 << XYRS * (
      K_-*K_+/(X^2Y^2)
      + K_-
      + K_+
      + 1
    ) * B^o(1).                                    (4.2)
```

Once `(x,y,r,s,k_-,k_+,g)` is fixed, equations (3.1)-(3.2) determine `a,b`, hence `P,Q`; dropping positivity, integrality and squarefreeness can only enlarge the count.

By the fixed-coordinate transfer in §1.1, (4.2) bounds the corresponding physical block up to `B^o(1)`.

---

## 5. Critical-shell exponent

Remain on

```text
P,Q~B^(1/2),
xi~B^(3/4).
```

Write

```text
Q-P~B^d,             0<=d<=1/2,
k~B^kappa,           3/4-o(1)<=kappa<=d+1/2.      (5.1)
```

Since `Q+P~B^(1/2)`,

```text
Q^2-P^2=(Q-P)(Q+P)~B^(d+1/2).                    (5.2)
```

But

```text
Q^2-P^2=g^2*k*(r*s)^2,
```

so

```text
R*S = B^((d+1/2-kappa)/2+o(1)).                  (5.3)
```

From (1.1),

```text
X*Y = B^(1/8+o(1)).                               (5.4)
```

Also

```text
K_-*K_+ = B^(kappa+o(1)).                         (5.5)
```

The volume term of (4.2) is therefore

```text
XYRS * K_-K_+/(X^2Y^2)
 = B^(1/8+(d+kappa)/2+o(1)).                      (5.6)
```

Thus

```text
E_main(d,kappa)=1/8+(d+kappa)/2.                  (5.7)
```

### Boundary terms

Let

```text
alpha_-=log_B K_-,
alpha_+=log_B K_+.
```

Because

```text
K_-*R^2~B^d,
K_+*S^2~B^(1/2),
```

we have

```text
alpha_-<=d,
alpha_+<=1/2,
alpha_-+alpha_+=kappa.                            (5.8)
```

The `K_-` boundary contribution in (4.2) has exponent at most

```text
E_- <= 3/8+3d/2-kappa/2,
```

and

```text
E_- - E_main <= 1/4+d-kappa <= 3/4-kappa <=0.    (5.9)
```

The `K_+` boundary contribution has exponent at most

```text
E_+ <= 7/8+d/2-kappa/2,
```

and

```text
E_+ - E_main <= 3/4-kappa <=0.                   (5.10)
```

The root-only term is smaller.  Hence throughout the live 4cc critical range,

```text
N_critical(d,kappa)
 << B^(1/8+(d+kappa)/2+o(1)).                     (5.11)
```

This bound is unconditional.

---

## 6. Exact endpoint localization

Since

```text
d<=1/2,
kappa<=1,
```

(5.11) never exceeds `7/8`.

For every fixed `delta>0`, either

```text
d<=1/2-delta
```

or

```text
kappa<=1-delta
```

implies

```text
N_critical
 << B^(7/8-delta/2+o(1)).                         (6.1)
```

Therefore any sequence of blocks that can still saturate `7/8` must satisfy

```text
d=1/2-o(1),
kappa=1-o(1).                                    (6.2)
```

Equivalently,

```text
Q-P = B^(1/2+o(1)),
k    = B^(1+o(1)).                                (6.3)
```

This strictly sharpens 4cc, which only forced `k>=B^(3/4-o(1))`.

---

## 7. The difference factors are essentially squarefree

From (5.3) and (6.2),

```text
R*S=B^o(1).
```

Hence individually

```text
r,s=B^o(1).                                        (7.1)
```

Since

```text
(Q-P)/g=k_-r^2~B^(1/2),
(Q+P)/g=k_+s^2~B^(1/2),
```

we obtain

```text
k_-=B^(1/2+o(1)),
k_+=B^(1/2+o(1)).                                  (7.2)
```

The full hard core is therefore

```text
P,Q,Q-P,Q+P       ~ B^(1/2),
a,b               ~ B^(3/8),
x,y               ~ B^(1/16),
xi=a*b            ~ B^(3/4),
k_-,k_+           ~ B^(1/2),
r,s                = B^o(1),
k=k_-k_+           ~ B.                           (7.3)
```

The former 4cc twist band

```text
B^(3/2-o(1)) <= n=xi*k <= B^(7/4+o(1))
```

collapses at the `7/8` endpoint to

```text
n=xi*k=B^(7/4+o(1)).                               (7.4)
```

---

## 8. Exact quadratic-residue signature

The endpoint packet has four pairwise-coprime squarefree coefficient blocks `(a,b,k_-,k_+)` up to the harmless 2-primary convention.  Equations (3.1)-(3.2) imply the following exact odd-prime conditions.

For every odd `ell|a`,

```text
(k/ell)=+1.                                        (8.1)
```

For every odd `ell|b`,

```text
(-k/ell)=+1.                                       (8.2)
```

For every odd `ell|k_-`,

```text
(xi/ell)=+1.                                       (8.3)
```

For every odd `ell|k_+`,

```text
(-xi/ell)=+1.                                      (8.4)
```

For example, if `ell|a`, (3.1) gives

```text
k_+s^2 == k_-r^2 (mod ell),
```

and all factors being divided are units, so `(k/ell)=1`.  The other three statements follow identically, with the sign supplied by (3.1) or (3.2).

These conditions are not multiplied as independent local half-densities.  They define the next genuine transverse receiver: a bilinear signed quadratic-residue incidence graph between

```text
(a,b)      at scale B^(3/8)
```

and

```text
(k_-,k_+)  at scale B^(1/2).
```

---

## 9. Relation to tH14 R2 and t52

The endpoint theorem above is independent of the t-track completion problem.

Merged tH14 R2 proves

```text
DUAL_QUADRATIC_LARGE_SIEVE_PRODUCT_ROW_ADAPTER_PROVED=true
```

but leaves

```text
PHYSICAL_WEIGHTED_SQUARECLASS_FIBER_ENERGY_PROVED=false.
```

Merged t52 confirms that the unresolved selector-sensitive completion contains the global principal squareclass collision problem; after residue cleanup the generic cross-good LD2 Kummer principal incidence remains open.

Accordingly:

```text
TH14_R2_CONSUMED=true,
TH15_NEEDED=false,
MAINLINE_H_NEEDED=false.
```

No new mainline-H task is needed.  14-4 can continue directly on the arithmetic endpoint residue graph while the t-track attacks its own Kummer/principal receiver.

---

## 10. Current exponent and next task

The exact endpoint `d=1/2`, `kappa=1` still permits the support exponent `7/8`, so no new whole-family fixed-power saving is claimed:

```text
V(B) << B^(7/8+o(1)).
```

What 4cd proves is that the obstruction is now confined to the maximal-`k`, four-linear-factor endpoint (7.3), with the exact residue signature (8.1)-(8.4).

The next 14-4 stage should attack this endpoint directly by bilinear quadratic-residue dispersion between `(a,b)` and `(k_-,k_+)`, while preserving the four-root congruence lattice rather than discarding it before Cauchy.

```text
NEXT=Stage14-4ce.
```

---

## Stage boundary

```text
STAGE14_4CD=FOUR_ROOT_LATTICE_CONGRUENCE_AND_MAXIMAL_K_ENDPOINT_LOCALIZATION
MERGED_4CC_IMPORTED=true
MERGED_S7_15_IMPORTED=true
MERGED_TH14_R2_IMPORTED=true
MERGED_T52_IMPORTED=true
FIXED_COORDINATE_PARTNER_MULTIPLICITY=B^o(1)
FOUR_CANONICAL_SQUAREPART_ROOTS_USED_SIMULTANEOUSLY=true
CROSS_ROOT_COPRIMALITY_GCD_XY_RS_EQ_1=true
DIFFERENCE_KERNEL_CONGRUENCE_LATTICE_EXACT=true
DIFFERENCE_KERNEL_LATTICE_MODULUS=x^2*y^2
CRITICAL_LATTICE_SUPPORT_EXPONENT=1/8+(d+kappa)/2
KAPPA_BELOW_ONE_BY_DELTA_SAVING=delta/2
Q_MINUS_P_BELOW_HALF_BY_DELTA_SAVING=delta/2
SEVEN_EIGHT_RESIDUAL_REQUIRES_Q_MINUS_P_EXPONENT=1/2-o(1)
SEVEN_EIGHT_RESIDUAL_REQUIRES_K_EXPONENT=1-o(1)
DIFFERENCE_SQUAREPART_PRODUCT=B^o(1)
K_MINUS_EXPONENT=1/2+o(1)
K_PLUS_EXPONENT=1/2+o(1)
CRITICAL_TWIST_PARAMETER_EXPONENT=7/4+o(1)
ENDPOINT_QUADRATIC_RESIDUE_SIGNATURE_EXACT=true
PHYSICAL_WEIGHTED_SQUARECLASS_FIBER_ENERGY_PROVED=false
GENERIC_CROSS_GOOD_LD2_KUMMER_PRINCIPAL_INCIDENCE_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
TH14_R2_CONSUMED=true
TH15_NEEDED=false
MAINLINE_H_NEEDED=false
NEXT=Stage14-4ce
```
