# Stage32 MB104 — `000707000f0f` e=2 ambient Kummer monodromy reduction

Status: **RETAINED AMBIENT-CHARACTER REDUCTION / KAPPA NO LONGER ARBITRARY / NO NUMERICAL UPPER BOUND / e=2,e=4 OPEN / NO CREDIT**

## Scope

Continue the retained `e=2` branch for the dangerous equality packet

```text
Sigma = 000707000f0f,
D_l = 7lH - 4l sum_(p in Sigma) E_p,
l>=1.
```

Let

```text
2 L_abs ~ B_abs
```

be the absent-type half-branch class, with `B_abs` the sixteen absent-type exceptional curves, and put

```text
U := S \ B_abs.
```

The carrier `C` is disjoint from `B_abs`, hence `C subset U`. The double cover defined by `L_abs` restricts to a finite etale degree-two cover

```text
pi_U : Y_U -> U.
```

Source lock: `STACKS-KUMMER-AMBIENT-ETALE-MONODROMY-SOURCE-NOTE.md`.

## 1. A single fixed ambient character controls every conductor sign

The cover `pi_U` determines one ambient `mu_2` / `Z/2` character

```text
alpha_abs : pi_1(U) -> Z/2.
```

Its restriction to the singular carrier is exactly the etale double cover classified by

```text
M = O_C(L_abs|_C),
M^2 ~= O_C.
```

Pulling further to the normalization

```text
nu:E -> C
```

gives the retained normalization character

```text
eta = nu^*M in Pic^0(E)[2].
```

Thus the retained case split becomes

```text
e=2  <=> alpha_abs|_(pi_1(E)) = 0,
e=4  <=> alpha_abs|_(pi_1(E)) != 0.
```

In particular, in the `e=2` case the remaining singular gluing class

```text
kappa in Ker(Pic(C)[2] -> Pic(E)[2])
```

is not a free choice in that kernel. It is the descent shadow of this one fixed ambient character `alpha_abs`.

## 2. Exact branch-pair character

Assume `e=2`. Choose one of the two global sections of the split pullback of `pi_U` to `E`.

Let `p` be a singular point of `C`, with normalization preimages / reduced branches

```text
x_1,...,x_r in E,
beta_1,...,beta_r.
```

All `x_i` map to the same two-point fibre of `pi_U` over `p`. Relative to a labeling of that fibre, the chosen section gives signs

```text
epsilon_i in Z/2.
```

For each pair `(i,j)`, transport from `x_i` to `x_j` along the normalization and close the endpoints at their common image `p`. In the complex realization this is an ordinary loop in `U`; algebraically it is the corresponding finite-etale fibre-transport element. Denote its class by

```text
lambda_(p;i,j).
```

Because `alpha_abs` is trivial on every closed loop coming from `E` in the `e=2` case, the value below is independent of the chosen normalization path:

```text
epsilon_i + epsilon_j
 = alpha_abs(lambda_(p;i,j)) in Z/2.          (MON)
```

Changing the global split section flips every `epsilon_i` simultaneously and leaves `(MON)` unchanged.

Therefore the conductor labels at all singular points are evaluations of the **same ambient character**; they are not independent local binary variables.

## 3. Exact cross-sheet intersection formula with ambient character

The retained local-cut identity is

```text
delta_cross,p
 = sum_(i<j, epsilon_i != epsilon_j) I_p(beta_i,beta_j).
```

Using `(MON)` gives the equivalent exact formula

```text
delta_cross,p
 = sum_(i<j) I_p(beta_i,beta_j)
              * alpha_abs(lambda_(p;i,j)),   (A-CUT)
```

where the character value is read as `0` or `1`.

Hence globally

```text
y/2
 = sum_p delta_cross,p
 = sum_p sum_(i<j) I_p(beta_i,beta_j)
                    * alpha_abs(lambda_(p;i,j)).   (GLOBAL-A-CUT)
```

The retained Hodge requirement is therefore

```text
sum_p sum_(i<j) I_p(beta_i,beta_j)
                    * alpha_abs(lambda_(p;i,j))
 >= 84l^2.                                      (A-HODGE)
```

This is the exact ambient-monodromy form of the `e=2` obstruction.

## 4. Consequence: the missing object is now an inclusion/monodromy map

The previous generalized-Jacobian leaf reduced the problem to `kappa`. This leaf identifies `kappa` with a restriction of a fixed surface-complement torsor.

Thus the next useful computation is one of the following equivalent forms:

```text
conductor branch-pair loops lambda_(p;i,j)
       -> pi_1(U)
       ->[alpha_abs] Z/2,
```

or, after passing to an appropriate mod-two topological/homological realization,

```text
conductor identification cycles
       -> H_1(U,F_2)
       ->[alpha_abs] F_2.
```

A successful upper-bound route must show that high-intersection branch pairs are forced into the kernel of this fixed character often enough to make

```text
y < 168l^2.
```

Equivalently, a direct modular computation of `alpha_abs(lambda_(p;i,j))` would determine the sheet cut exactly.

## 5. What this rules out

The following model is no longer admissible for `e=2`:

```text
choose each singular-point branch labeling independently,
subject only to local delta/conductor data.
```

All labels must arise from the same ambient Kummer torsor. This is a genuine global compatibility constraint, even though no quantitative saving has yet been extracted from it.

The following routes remain insufficient by themselves:

- the rank/dimension of `Ker(Pic(C)[2] -> Pic(E)[2])`;
- purely local delta or pairwise-intersection inequalities;
- smooth `Pic^0(E)[2]` data after `eta=0` is imposed;
- the already-exhausted two-factor square-class comparison.

## Next leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-AMBIENT-CHARACTER-EVALUATION
```

Target: compute `alpha_abs` on the conductor identification cycles using the explicit modular double cover / commensurator model, or compute their image in the mod-two homology of `U=S\B_abs`. Any resulting strict weighted bound below `84l^2` for `(GLOBAL-A-CUT)` excludes `e=2`.

## Firewalls

- No numerical upper bound for `y` is proved here.
- No assertion is made that arbitrary carrier singularities are nodal or multicross.
- The homology formulation is only a realization of the finite-etale monodromy statement; no unstated homology computation is imported.
- `e=2` remains open.
- `e=4` remains open.
- `000707000f0f` remains open.
- Geometric support core remains `864`; dangerous equality-packet core remains `768`.
- MB104/span5/receiver/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No merge authorization.