# MB104 Z53 — size48 tangent-cone support reduction and equivariant-smoothing wall — 2026-09-19

Status: **PRE-AUDIT EXACT TANGENT-SUPPORT REDUCTION / EQUIVARIANT-MILNOR SOURCE WALL / NO CREDIT**

## Input

Z51/Z52 give an even Gorenstein type-(ii.a) size48 canonical-cover germ with

```
mult=4,
embdim=4,
codim=2 complete intersection,
initial orders=(2,2),
mu=31.
```

Let

```
Z=E_L+C1+C2+C3+C4+C5+E_R
```

be the fundamental cycle and

```
Gamma=C1+...+C5
```

the fixed A5 chain.

For type (II), m=1, Konno gives the maximal ideal cycle

```
F=Z+Gamma
```

and

```
m O_X = O_X(-F).
```

Thus the exceptional map of the normalized maximal-ideal blow-up is controlled by `O_X(-F)`.

## 1. Exact degree vector of -F

The coefficient vector of F on the seven-chain is

```
(1,2,2,2,2,2,1).
```

Using the all-minus-two chain intersection matrix,

```
F . (E_L,C1,C2,C3,C4,C5,E_R)
  = (0,-1,0,0,0,-1,0).
```

Therefore

```
deg O(-F)|E_L = 0,
deg O(-F)|C1  = 1,
deg O(-F)|C2  = 0,
deg O(-F)|C3  = 0,
deg O(-F)|C4  = 0,
deg O(-F)|C5  = 1,
deg O(-F)|E_R = 0.
```

Only C1 and C5 can map nontrivially to the projectivized tangent cone.

## 2. Reduced exceptional image

Because `m O_X=O_X(-F)` and the linear system is basepoint-free, every connected degree-zero
subcurve is contracted by the maximal-ideal map.

The two degree-one rational components C1 and C5 each map with degree one onto a projective line.

The connected zero-degree subchain between them contracts to a point lying on both images.

Therefore the normalization of the reduced one-dimensional exceptional image consists of at most
two degree-one rational components meeting through the contracted central image.

At this stage it is not proved whether the two image lines are distinct or coincide.

Hence the Z52 projectivized tangent cone

```
Proj gr_m O_(Y#,y#)
```

is a degree-four (2,2) complete-intersection scheme whose reduced one-dimensional support is
carried by at most two lines.

In particular it is **not justified** to treat the tangent-cone quartic as a smooth elliptic
quartic.

Its excess degree is scheme-theoretic/nonreduced data.

## 3. Relation to the first-normal residual

The parallel Z51 first-normal calculation gives

```
H^1(Z,O_Z(-Z)) ~= C
```

and all higher additive Picard layers vanish.

It is therefore natural to test whether this one-dimensional class parametrizes the nonreduced
thickening of the line support in the (2,2) tangent cone.

Z53 does **not** assert that identification.  The exact missing adapter is:

```
first-normal transition coefficient
   ->
quadratic initial forms (q1,q2)
   ->
scheme structure on the two-line tangent support.
```

This is now a single explicit algebraic map to compute, rather than an open-ended analytic
classification problem.

## 4. Equivariant Milnor branch

The total Milnor number is exact:

```
dim H^2(F_Milnor,C)=31.
```

The canonical deck group `mu_3` acts on the central canonical-cover germ.

However, an action on the central germ does not by itself determine an action on an arbitrary
smoothing or on its vanishing cohomology.  To extract the `mu_3` character decomposition of
the 31-dimensional vanishing space, one needs either

- a `mu_3`-equivariant smoothing component, or
- explicit local CI equations with the deck action on the generators and deformation parameters.

Neither is retained yet.

Therefore

```
total_mu=31
!= equivariant_Milnor_character.
```

No downstairs local correction is promoted from the total Milnor number alone.

## 5. Source check

Konno's type-(ii) result supplies exactly the load-bearing facts used here:

- the fixed part Gamma is an A-type rational-double-point chain;
- for type (II), m=1, the maximal ideal cycle is `F=Z+Gamma`;
- `m O_X=O_X(-F)`;
- embedding dimension is four.

The paper does not provide a tangent-cone normal form for this exact marked graph.

## 6. Next leaf

```
MB104-Z54-FIRST-NORMAL-TO-QUADRATIC-INITIAL-FORM-ADAPTER
```

Target one concrete map only.

Construct local generators of `H^0(X,O_X(-F))` near the chain, retain the first-normal transition
parameter `lambda`, and compute the two quadratic initial relations

```
q1(lambda), q2(lambda).
```

Legal success:

1. the two-line scheme is independent of lambda;
2. lambda is forced by the explicit cuboid plumbing coordinates;
3. only finitely many projective quadratic pencils survive.

Do not use `mu=31` for local correction until an equivariant smoothing/action is materialized.

## Firewalls

```
reduced_tangent_support_at_most_two_lines=true
two_lines_distinct_proved=false
tangent_scheme_structure_explicit=false
first_normal_to_tangent_adapter_known=false
equivariant_smoothing_known=false
milnor_character_decomposition_known=false
downstairs_local_correction_computed=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
