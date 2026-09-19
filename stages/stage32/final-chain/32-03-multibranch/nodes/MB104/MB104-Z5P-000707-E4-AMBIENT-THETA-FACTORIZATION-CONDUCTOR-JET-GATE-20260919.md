# MB104 Z5' — 000707 e=4 ambient theta factorization and conductor-jet gate — 2026-09-19

Status: **PARALLEL PRE-AUDIT EXACT AMBIENT FACTORIZATION / FIRST-JET INTERFACE / NO CREDIT**

## Purpose

Continue the original Z5' packet-sensitive arithmetic/product route on the only surviving dangerous
equality-packet support

```text
Sigma=000707000f0f.
```

The preceding exact X(4) grid gives, in the e=4 case,

```text
phi_1^{-1}(i)  = seven-node supported packet,
phi_2^{-1}(1)  = complementary seven-node supported packet,
```

and the two fibers together are the reduced support-hyperplane divisor on the genus-one
normalization.

This note lifts that factorization to the ambient modular product and identifies the remaining
singular-carrier datum exactly.

## 1. Exact support hyperplane equation

In the canonical ordered 48-node model, the fourteen supported nodes of

```text
000707000f0f
```

span the unique hyperplane

```text
h = c-a1-a2-i*a3 = 0.
```

The coefficient vector is, up to scalar,

```text
(-1,-1,-i,0,0,0,1)
```

in coordinates

```text
(a1,a2,a3,b1,b2,b3,c).
```

## 2. Theta-product factorization

Write

```text
d_z=theta00(2z),  e_z=theta10(2z),
d_w=theta00(2w),  e_w=theta10(2w).
```

Freitag--Salvati Manni Theorem 2.4 gives

```text
C  = d_z d_w + e_z e_w,
W1 = e_z d_w + d_z e_w,
W2 = i(e_z d_w-d_z e_w),
W3 = d_z d_w-e_z e_w,
```

with

```text
(a1,a2,a3,c)=(W1,W2,W3,C).
```

Substitution into h gives

```text
h
 = C-W1-W2-iW3
 = (1-i)(d_z-i e_z)(d_w-e_w).                 (THETA-FACT)
```

The bilinear coefficient matrix has rank one; this is an exact identity on the modular product,
not merely an equality after restriction to a hypothetical carrier.

Thus the two factors are exactly the X(4) branch-value sections

```text
d_z-i e_z=0  <=>  t_z=i,
d_w-e_w=0    <=>  t_w=1.
```

This explains the exact seven-node single-fiber saturation found by the factor-cusp adapter.

## 3. Consequence on a hypothetical e=4 normalization

Let

```text
nu:E->C
```

be the genus-one normalization of a dangerous carrier.

The pullback of (THETA-FACT) gives actual section factorization

```text
nu^*h
 = const * s_z * s_w,
```

where

```text
div(s_z)=phi_1^{-1}(i),
div(s_w)=phi_2^{-1}(1).
```

The two divisors are reduced, disjoint, each of degree 56l, and together equal the 112l supported
branch divisor.

This is stronger than line-bundle square-root information: it identifies the two actual factors.

## 4. Why value-level conductor gluing is insufficient

At a supported A1 node exactly one factor vanishes on every dangerous branch:

- on the Q1 seven-node packet, s_z vanishes simply and s_w is nonzero;
- on the Q0 seven-node packet, s_w vanishes simply and s_z is nonzero.

Hence the product section h vanishes simply on every normalization branch.

For a section that is nonzero at the conductor, descent can be tested by comparing its values at
the normalization preimages.  Here the load-bearing factor is zero, so its value is identically
zero and carries no sign information.

The relevant descent datum is the **first nonzero coefficient**.

## 5. Exact local first-jet form

At a typical modular node, Freitag--Salvati Manni give level-eight product parameters

```text
(p,q)
```

with local box quotient

```text
(p,q) ~ (-p,-q).
```

After transport to a supported node and choosing the factor corresponding to the saturated branch
value, the vanishing theta factor is a local uniformizer in one product coordinate.

Thus on a normalization branch one may write

```text
p(s)=a s+O(s^2),
q(s)=b s+O(s^2),
(a,b)!=(0,0).
```

For a node in the s_z-zero packet,

```text
s_z = u_z * a s + O(s^2),
s_w = v_w + O(s),
v_w!=0,
```

and therefore

```text
nu^*h = const * a s + O(s^2).
```

For a node in the s_w-zero packet the analogous leading coefficient is proportional to b.

Hence the singular-carrier descent/sign problem for the half-fiber factors is reduced exactly to
the branchwise first coefficients

```text
a  on the seven s_z-zero nodes,
b  on the seven s_w-zero nodes.
```

Equivalently, after fixing one local normalization orientation, the missing datum is the ratio of
the first theta-coordinate coefficients across each conductor identification.

## 6. Relation to the retained landing parameter

The A1 exceptional landing direction is determined by the projective pair

```text
[a:b]
```

or equivalently by the retained ratio

```text
lambda=b/a
```

when both are nonzero.

However lambda is invariant under simultaneous sign

```text
(a,b)->(-a,-b),
```

while the Beauville/product sheet changes by that simultaneous sign.

Therefore the landing parameter alone does not recover the required conductor sign.

This is exactly why the earlier FSM-minimal / landing-bin data did not evaluate the residual sheet.

## 7. Exact remaining Z5' interface

The new ambient factorization closes all ambiguity above first-jet level:

```text
KNOWN:
  exact support hyperplane;
  exact modular factorization;
  exact two saturated factor fibers;
  exact node-to-factor assignment;
  exact local quotient involution.

MISSING:
  for each actual conductor identification,
  whether the first coefficient pair is glued by
      (a,b) -> (a,b)
  or
      (a,b) -> (-a,-b).
```

That one bit is precisely the singular-carrier conductor/gluing character which normalization-only
Picard and Kummer calculations forget.

Therefore Z5' has reached the same load-bearing datum as the archived conductor route, but now by a
source-complete ambient theta factorization.

A useful next step must compute this first-jet sign from an actual local carrier equation,
normalization/conductor transition, or an independent surface-side jet relation. Repeating
degree/Hurwitz/Picard calculations cannot decide it.

## Source locks

- Freitag--Salvati Manni, *Parametrization of the box variety by theta functions*,
  Theorem 2.4 and Proposition 2.5;
- retained source note
  `FREITAG-SALVATI-MANNI-LOCAL-NODE-THETA-SOURCE-NOTE.md`
  blob `36664f4443e508bb0d9b264f4fe9bb88030bdf38`;
- exact factor-cusp adapter on current compact branch;
- exact 000707 e=4 grid/single-fiber saturation on current compact branch;
- Z33 support-hyperplane contact/equality note blob
  `65656518d30f69ab3a4a892c8d4ae1d5ed72670e`.

## Firewalls

```text
ambient_theta_factorization_exact=true
single_fiber_factorization_exact=true
conductor_first_jet_sign_computed=false
e4_excluded=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
