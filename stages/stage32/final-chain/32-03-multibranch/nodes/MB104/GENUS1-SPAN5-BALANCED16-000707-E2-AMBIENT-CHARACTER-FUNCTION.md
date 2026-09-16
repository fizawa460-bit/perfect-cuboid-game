# Stage32 MB104 — `000707000f0f` e=2 ambient character as an explicit factor square-class

Status: **RETAINED EXPLICIT KUMMER REPRESENTATIVE / ABSTRACT AMBIENT CHARACTER REDUCED TO ONE RATIONAL FUNCTION / NO NUMERICAL CUT BOUND / e=2,e=4 OPEN / NO CREDIT**

## Scope

Continue the retained ambient-Kummer leaf. Fix one product-induced genus-five fibration with factor coordinate

```text
t=(c+a1)/(a2+i*a3).
```

For the absent singular type `b3=0`, the two bad values are `+i,-i`. Let their reduced `G2` components on the resolution be `Q_a,Q_b`, with exceptional eight-node sums

```text
E_a=sum_(p in T_a) E_p,
E_b=sum_(p in T_b) E_p.
```

The full resolved bad fibers are

```text
F_a=2Q_a+E_a,
F_b=2Q_b+E_b.
```

Define

```text
Delta=Q_a-Q_b,
L_abs=Delta+E_a,
B_abs=E_a+E_b.
```

Then `2L_abs~B_abs`.

## 1. Exact divisor of the factor character

Set

```text
f_t=(t-i)/(t+i).
```

Because `t-i` and `t+i` cut out the two complete fibers,

```text
div(f_t)=F_a-F_b.
```

Substituting the resolved fiber divisors gives

```text
div(f_t)
 =2(Q_a-Q_b)+E_a-E_b
 =2Delta+E_a-E_b.
```

On the other hand

```text
2L_abs-B_abs
 =2(Delta+E_a)-(E_a+E_b)
 =2Delta+E_a-E_b.
```

Hence exactly

```text
div(f_t)=2L_abs-B_abs.                         (DIV)
```

This is stronger than the previous statement that `f_t|_E` represents the residual normalization class: it identifies the **ambient** half-branch Kummer datum.

## 2. The ambient torsor is the square-class of `f_t`

Put

```text
U=S\\B_abs.
```

The double cover defined by the half-branch relation `2L_abs~B_abs` is etale over `U`. By `(DIV)`, after rationally trivializing `O(L_abs)`, its Kummer equation differs only by inversion and a nonzero square scalar from

```text
z^2=f_t.
```

In a 2-torsion square-class group inversion does not change the class. Therefore the retained ambient character

```text
alpha_abs: pi_1(U)->Z/2
```

is precisely the monodromy character of the explicit Kummer class

```text
[f_t] in k(S)^*/k(S)^{*2},
f_t=(t-i)/(t+i).                              (KUM)
```

The complementary factor gives the same ambient class because the retained cuboid identity proves

```text
f_t/f_u=((c+a3)/b3)^2.
```

Thus there is one canonical square-class for the current purpose, not two competing factor classes.

## 3. Even valuations on the complement

On `U`, the absent exceptional components have been removed. The remaining zero/pole divisors of `f_t` are

```text
2Q_a and 2Q_b.
```

Hence every codimension-one valuation of `f_t` on `U` is even. This is exactly compatible with the fact that `z^2=f_t` extends as an etale double cover over `U`: small meridians around `Q_a` or `Q_b` have trivial mod-two local branching contribution.

Therefore any nontrivial value of `alpha_abs` on a conductor identification loop is **global square-root monodromy**, not a local odd-valuation effect around the two absent `G2` divisors.

## 4. Conductor-pair evaluation becomes square-root transport of one function

Assume `e=2`. Then `f_t|_E` is a square in `k(E)^*`. Choose

```text
g in k(E)^*,
g^2=f_t|_E.
```

For two normalization branches `x_i,x_j` over the same singular point `p`, the conductor sign difference is exactly the failure of the chosen square root `g` to descend with the same fibre value across the identification:

```text
epsilon_i+epsilon_j
 = alpha_abs(lambda_(p;i,j)).
```

Equivalently, after choosing compatible local trivializations, it is detected by whether the two limiting square-root values satisfy

```text
g(x_i)= g(x_j)
```

or

```text
g(x_i)=-g(x_j).
```

Thus the weighted cut is no longer an abstract fundamental-group problem:

```text
y/2
 = sum_p sum_(i<j) I_p(beta_i,beta_j)
   * [square-root transport of f_t changes sign between x_i,x_j].
```

The remaining task is to compute this sign transport from the explicit factor map / modular lift at conductor-identification pairs.

## 5. Route consequence

The active e=2 problem has now been reduced through the chain

```text
singular Picard kappa
 -> ambient character alpha_abs
 -> explicit Kummer square-class [f_t]
 -> sign comparison of one square root g on normalization preimages.
```

This eliminates the need to compute the full group `pi_1(U)` or `H_1(U,F_2)` if the modular/factor coordinates can directly determine the limiting signs of `g`.

A useful next input is therefore an exact branch-pair formula for the lift of

```text
sqrt((t-i)/(t+i))
```

through the `C8/H` product-cover coordinate, or an equivalent algebraic expression whose values at the two normalization preimages of each conductor identification can be compared.

## Firewalls

- No claim is made that even codimension-one valuations make the etale cover globally trivial.
- No sign comparison at a Stage32 conductor pair is computed here.
- No upper bound for `y` is proved.
- `e=2` and `e=4` remain open.
- `000707000f0f` remains open.
- Geometric support core remains `864`; dangerous equality-packet core remains `768`.
- MB104/span5/receiver/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No merge authorization.
