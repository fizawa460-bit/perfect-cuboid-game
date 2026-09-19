# MB104 Z49B — unique holomorphic lift of the size48 index-three plumbing cover — 2026-09-19

Status: **PRE-AUDIT EXACT HOLOMORPHIC-LIFT UNIQUENESS / LOCAL COVER MODEL / NO CREDIT**

## Input

Use one actual size-48 contraction germ

```text
phi:N(D) -> (Y,y)
```

with

```text
D=Q_1 union B union Q_2,
Q_i^2=-4, g(Q_i)=1, j(Q_i)=1728,
B^2=-2, B~=P^1.
```

Z48 fixes the marked negative component neighborhoods.
Z49 fixes the canonical topological degree-three cover direction and, up to simultaneous deck
inversion, the meridian character

```text
chi(mu_Q1)=chi(mu_B)=chi(mu_Q2)=1 in Z/3.
```

The question is whether this topological cover admits multiple holomorphic lifts.

## 1. The punctured-germ holomorphic cover is unique

Put

```text
U = Y \ {y}.
```

The contraction is an isomorphism

```text
N(D) \ D ~= U.
```

The retained Z49 character determines a connected finite topological covering

```text
pi_U: U^# -> U
```

of degree three, unique up to deck-generator inversion.

A finite covering of a complex manifold has a unique complex-analytic structure on the covering
space for which the covering map is a local biholomorphism: use the complex charts of U and lift
them through each evenly covered neighborhood.

Therefore the retained topological cover has exactly one holomorphic etale lift over U:

```text
topological cover direction
=> unique holomorphic degree-three etale cover of U.     (HOL-LIFT)
```

There is no independent C^*, Pic^0, or higher-jet holomorphic-lift modulus once the topological
cover is fixed.

## 2. Extension across the contraction point is unique

Let `K(U^#)` denote the finite extension of the meromorphic function field of U induced by the
cover.

Normalize the normal analytic germ `(Y,y)` in this finite field extension.  Analytic
normalization is unique and finite.  Hence there is a unique normal finite germ

```text
pi:(Y^#,y^#) -> (Y,y)
```

extending `pi_U`.

Since the topological character is the exact order-three canonical character retained in Z49,
this extension is the canonical index-one cover.

Consequently

```text
analytic_holomorphic_lift_unique = true.
```

The remaining problem is not a moduli problem for the cover; it is to write an explicit analytic
presentation of the already unique cover.

## 3. Explicit local model over a smooth point of D

Near a smooth point of one exceptional component choose a coordinate `x` normal to D.

The meridian character is nonzero.  Up to deck inversion it is 1, so the unique extension of the
cover across that smooth branch is

```text
x = t^3.
```

Thus the cover of the resolution plumbing is totally ramified of index three along every
irreducible component of D.

## 4. Explicit local model at each plumbing node

At either transverse attachment choose smooth coordinates `(x,y)` on S with

```text
D=(xy=0),
Q_i=(x=0),
B=(y=0)
```

(or the reversed labels).

On the complement `xy != 0`, Z49 gives equal nonzero characters on the two meridians.
Choosing the common value 1, the cyclic cover is

```text
t^3 = x y.                                      (NODE-COVER)
```

Indeed a loop around either x=0 or y=0 multiplies t by the same primitive cube root.

The normal extension across the crossing is therefore the hypersurface

```text
xy-t^3=0,
```

which is the A_2 rational double point.

Simultaneous deck inversion replaces the common character 1 by 2 and gives an isomorphic cover
after normalization.  Hence each of the two Q--B plumbing nodes lifts to the same exact A_2 local
model.

## 5. What is now explicit

For the cover of the size48 plumbing resolution:

```text
generic exceptional point:   x=t^3,
each Q--B node:               xy=t^3 (A_2),
cover over the complement:   unique etale Z/3 cover.
```

Thus no residual holomorphic plumbing parameter survives.

The global connected cover `Y^#` is uniquely determined as the normalization of Y in that
punctured cover.

## 6. Remaining interface

This does **not** yet give a single affine hypersurface/complete-intersection equation for
`(Y^#,y^#)`.

The next exact task is now algebraic rather than classificatory:

1. resolve the two A_2 points of the branched plumbing cover;
2. compute the resulting exceptional intersection configuration;
3. contract the preimage exceptional locus;
4. determine whether the resulting Gorenstein germ has a recognized explicit canonical,
   hypersurface, complete-intersection, or splice-type presentation;
5. only then evaluate local symmetric-Euler/Chern corrections.

There is no longer a named holomorphic-lift modulus to search for.

## External theorem anchors

- Classical covering-space/Riemann-existence principle for complex manifolds: a finite
  topological covering carries a unique complex structure making the covering holomorphic etale.
- Uniqueness and finiteness of normalization of a reduced complex analytic space in a finite
  extension of its meromorphic function field.

These are used after the exact topological canonical character has already been fixed by Z49;
they do not infer the cover from the resolution graph alone.

## Firewalls

```text
topological_degree3_cover_direction_unique=true
holomorphic_etale_lift_on_punctured_germ_unique=true
normal_extension_across_point_unique=true
holomorphic_lift_modulus_remaining=false
generic_branch_model_x_eq_t3=true
plumbing_node_cover_A2=true
global_canonical_cover_equation_known=false
local_symmetric_euler_computed=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
