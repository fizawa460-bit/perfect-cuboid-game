# Stage14-s7-20 — dual xi-split injectivity and balanced eight-cell endpoint

## Status

`COMPLETE_DUAL_XI_SPLIT_INJECTIVITY_AND_BALANCED_EIGHT_CELL_LOCALIZATION`

Merged Stage14-s7-19 replaces every surviving same-`(xi,k)` cross-`k`-split collision by a primitive Pythagorean triple.  Stage14-s7-20 now returns to the physical lift and uses the exact canonical factorization of `P,Q` as well as the exact split of `Q-P,Q+P`.

The new point is a duality.

- s7-18 proved that the `k` allocation between `Q-P` and `Q+P` cannot remain fixed on the critical shell.
- s7-20 proves the exact analogue for the `xi=ker(PQ)` allocation between `P` and `Q`.
- at the actual merged 4cd endpoint, positive square-divisibility on the switched `k` cells prevents an arbitrarily large switching product.
- the primitive gcd `d` from s7-19 records, up to the 2-primary convention, exactly the part of `xi` that switches between `P` and `Q`.

Consequently every endpoint collision is forced into a **balanced eight-cell configuration**: all four `k` cells have exponents in `[3/16,5/16]`, and all four `xi` cells have exponents in `[1/8,1/4]`.

This is an unconditional localization theorem.  It still does not by itself give a whole-family exponent below `7/8`.

---

## 1. Imported endpoint data

Take two distinct reduced states with the same squarefree labels

```text
xi=ker(P_1 Q_1)=ker(P_2 Q_2),
k =ker(Q_1^2-P_1^2)=ker(Q_2^2-P_2^2).
```

Merged 4cd/s7-19 localize every block capable of saturating `7/8` to

```text
P_i,Q_i,Q_i-P_i,Q_i+P_i ~ B^(1/2),
xi ~ B^(3/4),
k  = B^(1-o(1)).                                    (1.1)
```

Canonical `P/Q` squarefree coordinates are

```text
P_i=a_i x_i^2,
Q_i=b_i y_i^2,
a_i*b_i=xi,
gcd(a_i,b_i)=1,
```

with

```text
a_i,b_i ~ B^(3/8),
x_i,y_i ~ B^(1/16).                                 (1.2)
```

The difference split is

```text
u_i=(Q_i-P_i)/g_i=k_{-,i} r_i^2,
v_i=(Q_i+P_i)/g_i=k_{+,i} s_i^2,
g_i in {1,2},
k_{-,i}k_{+,i}=k,
```

and 4cd gives

```text
k_{-,i},k_{+,i} ~ B^(1/2),
r_i,s_i=B^o(1).                                      (1.3)
```

Merged s7-19 also gives

```text
v_i^2-u_i^2=xi*z_i^2,
z_i^2 <= 4X^2/xi,
```

so at the endpoint

```text
z_i=B^(1/8+o(1)).                                   (1.4)
```

Finally write

```text
Q_i^2-P_i^2=k*omega_i^2.
```

Since `omega_i=g_i r_i s_i`,

```text
omega_i=B^o(1)                                     (1.5)
```

at the endpoint.

---

## 2. Exact four-cell decomposition of the xi allocation

For the two canonical `P/Q` allocations of the same squarefree `xi`, there are unique pairwise-coprime squarefree cells

```text
R,S,T,J
```

such that

```text
a_1=R*S,
b_1=T*J,
a_2=R*T,
b_2=S*J,
R*S*T*J=xi.                                         (2.1)
```

Interpretation:

- `R`: in `P` for both states;
- `J`: in `Q` for both states;
- `S`: in `P_1` and `Q_2`;
- `T`: in `Q_1` and `P_2`.

Define

```text
Xi_agree = R*J,
Xi_switch= S*T,
xi=Xi_agree*Xi_switch.                              (2.2)
```

The two `xi` allocations coincide exactly when `Xi_switch=1`.

---

## 3. Dual fixed-xi-split injectivity

The two states satisfy

```text
(TJ)^2 y_1^4-(RS)^2 x_1^4 = k*omega_1^2,
(SJ)^2 y_2^4-(RT)^2 x_2^4 = k*omega_2^2.            (3.1)
```

Cross-multiplication gives

```text
J^2(
 T^2 y_1^4 omega_2^2-S^2 y_2^4 omega_1^2
)
=
R^2(
 S^2 x_1^4 omega_2^2-T^2 x_2^4 omega_1^2
).                                                   (3.2)
```

Since `gcd(R,J)=1`,

```text
R^2 | T^2 y_1^4 omega_2^2-S^2 y_2^4 omega_1^2,
J^2 | S^2 x_1^4 omega_2^2-T^2 x_2^4 omega_1^2.      (3.3)
```

For `P_i,Q_i<=X`,

```text
y_1^2<=X/(T*J),
y_2^2<=X/(S*J),
x_1^2<=X/(R*S),
x_2^2<=X/(R*T),
omega_i^2<=X^2/k.
```

Hence

```text
|T^2 y_1^4 omega_2^2-S^2 y_2^4 omega_1^2|
 <= 2X^4/(J^2 k),

|S^2 x_1^4 omega_2^2-T^2 x_2^4 omega_1^2|
 <= 2X^4/(R^2 k).                                    (3.4)
```

Therefore if

```text
(RJ)^2*k > 2X^4,                                    (3.5)
```

both brackets in (3.3) vanish.

If a prime `ell|S`, the first vanishing equality is impossible: `ell` divides the right square-factor term but, by pairwise cell coprimality, reducedness, and

```text
gcd(xi,k*omega_1*omega_2)=1,                       (3.6)
```

the opposite side is an `ell`-adic unit.  Thus `S=1`; similarly `T=1`.

The `xi` splits therefore coincide.  With `S=T=1`, the two vanishing equalities imply

```text
x_1/y_1=x_2/y_2.
```

The canonical root pairs are primitive, so `(x_1,y_1)=(x_2,y_2)` and the two reduced states coincide.

Thus:

```text
FixedXiSplitKInjectivity:
if xi^2*k > 2X^4, a fixed canonical xi split contains
at most one state with a given k.                    (3.7)
```

More generally every off-diagonal same-`(xi,k)` collision satisfies

```text
boxed:
(Xi_agree)^2*k <= 2X^4.                              (3.8)
```

This is the exact `P/Q`-dual of the s7-18 `k`-split theorem.

---

## 4. Every critical collision also has a large xi-switch product

From (3.8),

```text
Xi_agree <= sqrt(2) X^2/sqrt(k),
```

so

```text
boxed:
Xi_switch
 >= xi*sqrt(k)/(sqrt(2) X^2).                       (4.1)
```

At exponent scale, with

```text
xi~B^gamma,
k~B^kappa,
X<=B^(1/2+o(1)),
```

this is

```text
log_B Xi_switch
 >= gamma+kappa/2-1-o(1).                           (4.2)
```

On the old `7/8` critical residual

```text
gamma=3/4,
kappa>=3/4-o(1),
```

we obtain

```text
Xi_switch>=B^(1/8-o(1)).                            (4.3)
```

On the actual 4cd endpoint `kappa=1-o(1)`,

```text
boxed:
Xi_switch>=B^(1/4-o(1)).                            (4.4)
```

Thus every endpoint collision is transverse in **both** squarefree allocations:

```text
k between Q-P and Q+P,
xi between P and Q.                                 (4.5)
```

---

## 5. The primitive gcd d records the switched xi support

Use the s7-19 Pythagorean composition

```text
H=v_1v_2+u_1u_2,
L=v_1u_2+u_1v_2,
W=xi*z_1*z_2,
d=gcd(H,L,W).                                       (5.1)
```

Directly from `u_i=(Q_i-P_i)/g_i`, `v_i=(Q_i+P_i)/g_i`,

```text
H+L = 4Q_1Q_2/(g_1g_2),
H-L = 4P_1P_2/(g_1g_2).                             (5.2)
```

Let `ell` be an odd prime dividing `xi`.  Since `ell|W`,

```text
ell|d
<=> ell|H and ell|L
<=> ell|(H+L) and ell|(H-L)
<=> ell|Q_1Q_2 and ell|P_1P_2.                      (5.3)
```

For an odd `ell|xi`, each state places `ell` in exactly one of `P_i,Q_i`.  Therefore (5.3) holds exactly when the `P/Q` allocation switches between the two states, i.e. when `ell|S*T`.

Hence

```text
boxed:
oddpart(gcd(xi,d)) = oddpart(Xi_switch),             (5.4)

boxed:
oddpart(xi_0) = oddpart(Xi_agree),                   (5.5)
```

where s7-19 defined

```text
xi_0=xi/gcd(xi,d).
```

Only the harmless 2-primary convention can differ.  Thus `xi_0` is not an arbitrary divisor of `xi`: at fixed-power scale it is exactly the **agreement part** of the canonical `P/Q` allocation.

Merged s7-19 proves at the 4cd endpoint

```text
xi_0>=B^(1/4-o(1)).                                 (5.6)
```

Therefore

```text
boxed:
Xi_agree>=B^(1/4-o(1)).                             (5.7)
```

Together with `xi~B^(3/4)` and (4.4),

```text
boxed:
B^(1/4-o(1)) <= Xi_switch,Xi_agree <= B^(1/2+o(1)). (5.8)
```

---

## 6. Positive square-divisibility on switched k cells

Retain the s7-18 `k` cells

```text
k_{-,1}=alpha*beta,
k_{+,1}=gamma*delta,
k_{-,2}=alpha*gamma,
k_{+,2}=beta*delta,
k=alpha*beta*gamma*delta.                           (6.1)
```

The state equations are

```text
(gamma*delta)^2 s_1^4-(alpha*beta)^2 r_1^4=xi*z_1^2,
(beta*delta)^2 s_2^4-(alpha*gamma)^2 r_2^4=xi*z_2^2. (6.2)
```

Reducing the first equation modulo `beta^2`, the second modulo `beta^2`, multiplying by the complementary square units and adding gives

```text
boxed:
beta^2 |
 alpha^2 r_2^4 z_1^2 + delta^2 s_1^4 z_2^2.         (6.3)
```

Similarly modulo `gamma^2`,

```text
boxed:
gamma^2 |
 delta^2 s_2^4 z_1^2 + alpha^2 r_1^4 z_2^2.         (6.4)
```

The right sides are positive; no cancellation estimate is used.

At the 4cd endpoint each of the four split products in (6.1) is `B^(1/2+o(1))`.  Hence there is an exponent `theta` such that

```text
alpha,delta = B^(theta+o(1)),
beta,gamma  = B^(1/2-theta+o(1)).                   (6.5)
```

Using `r_i,s_i=B^o(1)` and `z_i=B^(1/8+o(1))`, the right side of (6.3) has exponent at most

```text
2*theta+1/4+o(1),                                   (6.6)
```

while `beta^2` has exponent

```text
1-2*theta+o(1).                                     (6.7)
```

Since the positive integer in (6.3) is divisible by `beta^2`,

```text
1-2*theta <= 2*theta+1/4,
```

and therefore

```text
boxed:
theta>=3/16-o(1).                                  (6.8)
```

Merged s7-18 already gives

```text
K_switch=beta*gamma>=B^(3/8-o(1)),
```

which via (6.5) gives

```text
theta<=5/16+o(1).                                   (6.9)
```

Consequently

```text
boxed:
B^(3/8-o(1)) <= K_switch,K_agree <= B^(5/8+o(1)),   (6.10)
```

and individually

```text
boxed:
alpha,beta,gamma,delta
 in [B^(3/16-o(1)), B^(5/16+o(1))].                 (6.11)
```

Thus an endpoint collision cannot be produced by moving almost all of `k` from one side to the other; the `k` allocation is quantitatively balanced.

---

## 7. Symmetric switched-xi square divisibility

The `P/Q` equations (3.1) also give positive divisibilities on the switched `xi` cells.  Reducing modulo `S^2` and `T^2` gives

```text
boxed:
S^2 |
 R^2 x_2^4 omega_1^2 + J^2 y_1^4 omega_2^2,         (7.1)

boxed:
T^2 |
 J^2 y_2^4 omega_1^2 + R^2 x_1^4 omega_2^2.         (7.2)
```

Together with the agreement divisibilities (3.3), the `xi` allocation therefore has the same four-square-divisibility pattern as the `k` allocation.

At the endpoint all four canonical coefficients in (2.1) have exponent `3/8+o(1)`.  Hence for some `phi`,

```text
R,J = B^(phi+o(1)),
S,T = B^(3/8-phi+o(1)).                              (7.3)
```

The already-proved product bounds (5.8) are equivalent to

```text
boxed:
1/8 <= phi <= 1/4                                  (7.4)
```

up to `o(1)`.  Equivalently every individual `xi` cell satisfies

```text
boxed:
R,S,T,J
 in [B^(1/8-o(1)), B^(1/4+o(1))].                  (7.5)
```

The positive divisibilities (7.1)-(7.2) independently reproduce the lower endpoint `phi>=1/8`: their right sides have exponent at most `2phi+1/4+o(1)`, while `S^2,T^2` have exponent `3/4-2phi+o(1)`.

---

## 8. Balanced eight-cell endpoint

Every collision still capable of saturating `7/8` is therefore forced into two simultaneous four-cell decompositions:

```text
k cells:
alpha,beta,gamma,delta,
3/16 <= exponent <= 5/16;

xi cells:
R,S,T,J,
1/8 <= exponent <= 1/4.                             (8.1)
```

The exact divisibility system to preserve is

```text
k agreement:
alpha^2 | gamma^2 s_1^4 z_2^2-beta^2 s_2^4 z_1^2,
delta^2 | beta^2 r_1^4 z_2^2-gamma^2 r_2^4 z_1^2;

k switch:
beta^2 | alpha^2 r_2^4 z_1^2+delta^2 s_1^4 z_2^2,
gamma^2 | delta^2 s_2^4 z_1^2+alpha^2 r_1^4 z_2^2;

xi agreement:
R^2 | T^2 y_1^4 omega_2^2-S^2 y_2^4 omega_1^2,
J^2 | S^2 x_1^4 omega_2^2-T^2 x_2^4 omega_1^2;

xi switch:
S^2 | R^2 x_2^4 omega_1^2+J^2 y_1^4 omega_2^2,
T^2 | J^2 y_2^4 omega_1^2+R^2 x_1^4 omega_2^2.       (8.2)
```

All eight moduli are squarefree before squaring, and the cells inside each four-cell family are pairwise coprime.

This is the new live object:

```text
BalancedDoubleAllocationSquareDivisibility.
```

The point of (8.2) is that neither allocation may now be collapsed to a single label before counting.  A future bilinear or determinant argument can use four **difference** square-divisibilities and four **positive** square-divisibilities simultaneously.

---

## 9. Why no new whole-family exponent is promoted yet

The balanced cell windows are genuine fixed-power information, but the number of squarefree allocations of a fixed `xi` or fixed `k` remains `B^o(1)`.  Therefore balance alone does not turn pointwise bounded multiplicity into an average collision saving.

Likewise the eight divisibilities in (8.2) have not yet been converted into a global count over the physical lifts.

Accordingly

```text
V(B) << B^(7/8+o(1))
```

remains the unconditional whole-family theorem.

What has changed is the obstruction: a hypothetical saturating collision must now be simultaneously transverse and quantitatively balanced in **both** squarefree label allocations.

---

## 10. tH / auxiliary-line decision

No new supervisor line is needed.  The s7-20 theorem is elementary integer divisibility on the physical pair and does not use selector-sensitive Gaussian completion.

```text
TH15_NEEDED_BY_S7_20=false
S_AUXILIARY_SUPERVISOR_LINE_CREATED=false
S_ROUTE_BLOCKED_WAITING_FOR_TH14_OR_TH15=false
```

The merged toolbox common-envelope restrictions remain respected: no signed Gaussian theorem is promoted into the positive collision receiver.

---

## 11. Next receiver

Stage14-s7-21 should attack

```text
BalancedDoubleAllocationSquareDivisibility
```

directly on the 4cd endpoint.

The preferred first attempt is a determinant/CRT count that keeps all eight cells and the small roots

```text
r_i,s_i,omega_i=B^o(1),
x_i,y_i~B^(1/16),
z_i~B^(1/8)
```

attached.  In particular, the large positive square divisors in (8.2) should be consumed before any auxiliary-prime average or Cauchy collapse.

The target remains

```text
E_off,critical(B) << B^(7/8-delta+o(1))
```

for some fixed `delta>0`.

---

## 12. Stage boundary

```text
STAGE14_S7_20=COMPLETE_DUAL_XI_SPLIT_INJECTIVITY_AND_BALANCED_EIGHT_CELL_LOCALIZATION
MERGED_S7_19_IMPORTED=true
MERGED_S7_18_IMPORTED=true
MERGED_4CD_ENDPOINT_IMPORTED=true
XI_FOUR_CELL_DECOMPOSITION_EXACT=true
FIXED_XI_SPLIT_K_INJECTIVE_IF_xi2_k_GT_2_X4=true
FIXED_XI_SPLIT_CRITICAL_COLLISIONS_EXIST=false
CROSS_XI_SPLIT_AGREEMENT_NECESSARY_BOUND=(R*J)^2*k<=2*X^4
CRITICAL_XI_SWITCH_PRODUCT_LOWER_EXPONENT=1/8
FOUR_CD_ENDPOINT_XI_SWITCH_PRODUCT_LOWER_EXPONENT=1/4
ODD_GCD_XI_D_EQUALS_ODD_XI_SWITCH=true
ODD_XI0_EQUALS_ODD_XI_AGREE=true
FOUR_CD_ENDPOINT_XI_AGREE_PRODUCT_LOWER_EXPONENT=1/4
FOUR_CD_ENDPOINT_XI_AGREE_PRODUCT_UPPER_EXPONENT=1/2
FOUR_CD_ENDPOINT_XI_SWITCH_PRODUCT_UPPER_EXPONENT=1/2
K_SWITCH_POSITIVE_SQUARE_DIVISIBILITY=true
XI_SWITCH_POSITIVE_SQUARE_DIVISIBILITY=true
FOUR_CD_ENDPOINT_K_SWITCH_PRODUCT_RANGE=[3/8,5/8]
FOUR_CD_ENDPOINT_K_AGREE_PRODUCT_RANGE=[3/8,5/8]
FOUR_CD_ENDPOINT_INDIVIDUAL_K_CELL_RANGE=[3/16,5/16]
FOUR_CD_ENDPOINT_XI_SWITCH_PRODUCT_RANGE=[1/4,1/2]
FOUR_CD_ENDPOINT_XI_AGREE_PRODUCT_RANGE=[1/4,1/2]
FOUR_CD_ENDPOINT_INDIVIDUAL_XI_CELL_RANGE=[1/8,1/4]
BALANCED_DOUBLE_ALLOCATION_SQUARE_DIVISIBILITY_REQUIRED=true
BALANCED_DOUBLE_ALLOCATION_SQUARE_DIVISIBILITY_POWER_SAVING_PROVED=false
LARGE_SWITCH_PRIMITIVE_PYTHAGOREAN_TWO_LEG_INCIDENCE_POWER_SAVING_PROVED=false
LARGE_DISAGREEMENT_CROSS_SPLIT_K_COLLISION_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
TH15_NEEDED_BY_S7_20=false
S_ROUTE_BLOCKED_WAITING_FOR_TH14_OR_TH15=false
NEXT=Stage14-s7-21
```
