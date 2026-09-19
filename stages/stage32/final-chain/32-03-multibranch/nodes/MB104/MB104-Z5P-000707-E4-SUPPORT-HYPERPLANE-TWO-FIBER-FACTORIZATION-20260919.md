# MB104 Z5' — 000707 e=4 support-hyperplane two-fiber factorization — 2026-09-19

Status: **PARALLEL PRE-AUDIT EXACT NORMALIZATION FACTORIZATION / NO CREDIT**

## Input

Assume the dangerous equality packet on

```text
Sigma=000707000f0f
```

in the `e=4` case.

Let

```text
phi_1,phi_2:E->X(4)~=P1
```

be the two degree-56l factor maps on the genus-one normalization.

The exact factor-cusp adapter gives four occupied branch-value cells:

```text
(1,1)    : 4 nodes,
(i,-i)   : 4 nodes,
(-1,1)   : 3 nodes,
(i,i)    : 3 nodes.
```

Thus every supported normalization point lies on the reducible target divisor

```text
D_grid = {x=i} union {y=1}
```

of bidegree (1,1).

## 1. Pullback degree is exactly exhausted

Each factor map has degree 56l, hence

```text
deg (phi_1,phi_2)^* O(1,1)=112l.
```

The two exact single-fiber saturations are disjoint:

```text
phi_1^{-1}(i):
  seven nodes, 56l distinct unramified points;

phi_2^{-1}(1):
  the complementary seven nodes, 56l distinct unramified points.
```

Therefore

```text
(phi_1,phi_2)^* D_grid
 = B_node,
```

where `B_node` is the reduced divisor of all 112l supported normalization branches.

There is no residual point in the pullback of D_grid.

## 2. Compare with the support hyperplane

Z33 proves for the unique support hyperplane section h that

```text
div_E(nu^* h)=B_node
```

reduced.

Hence the two sections have exactly the same divisor on the smooth elliptic normalization:

```text
div_E(nu^*h)
 =
div_E(s_(1,i) s_(2,1)),
```

where `s_(1,i)` is the pullback of a target linear form cutting the fiber `x=i`, and
`s_(2,1)` similarly cuts `y=1`.

Consequently there is an exact line-bundle isomorphism

```text
nu^* O_S(H)
 ~= M_1 tensor M_2,
```

with

```text
M_j=phi_j^*O_P1(1),
```

and under this isomorphism

```text
nu^*h = c * s_(1,i) s_(2,1)
```

for one nonzero scalar c.

This is an **actual section factorization**, not only an equality of divisor classes.

## 3. Full-G common-cover consequence

The retained full-G character-line argument applies to the e=4 common labelled G-cover and gives

```text
M_1 ~= M_2 =: M.
```

Therefore

```text
nu^*O_S(H) ~= M^2.
```

If

```text
B_1=phi_1^{-1}(i),
B_2=phi_2^{-1}(1),
```

then

```text
B_1 ~ B_2,
B_1+B_2 = B_node = div_E(nu^*h),
2[B_1]=[B_node]=2[B_2]
```

in Pic(E).

Thus the two seven-node packets are not merely equal in degree: they are the two effective
half-hyperplane divisors supplied by the two factor pencils.

## 4. Scope and next use

On a complex elliptic curve an even-degree line bundle always admits square roots, so

```text
nu^*O_S(H) ~= M^2
```

is not by itself contradictory.

The new information is the **distinguished effective factorization**

```text
support-hyperplane section
 = factor-1 saturated fiber
 + factor-2 saturated fiber.
```

A further Z5' obstruction must show that this specific half-hyperplane factorization is
incompatible with the common G-cover / conductor gluing, rather than using degree or Picard
divisibility alone.

## Source locks

- exact X(4) factor-cusp adapter and 000707 e=4 grid verifier on the current compact branch;
- Z33 support-hyperplane equality note blob
  `65656518d30f69ab3a4a892c8d4ae1d5ed72670e`;
- P6H full-G common character-line note blob
  `cbc8307689ae91b08f547fe1c69606086d06dec1`.

## Firewalls

```text
support_hyperplane_two_fiber_factorization_exact=true
normalization_half_hyperplane_square_exact=true
e4_excluded=false
surface_level_square_root_not_claimed=true
conductor_gluing_compatibility_not_resolved=true
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
