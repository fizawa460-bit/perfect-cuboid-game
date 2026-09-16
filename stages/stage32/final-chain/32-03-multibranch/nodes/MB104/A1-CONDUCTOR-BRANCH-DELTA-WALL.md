# Stage32 MB104 — sharp A1 branch-delta / conductor wall

Status: **RETAINED SHARP LOCAL BOUND / MB104 INCOMPLETE / NO CREDIT**

## Purpose

After the order-two BTVA principal-part route saturates at three landing directions per node, the next natural idea is to charge repeated normalization branches through the conductor/delta invariant of the **downstairs** curve germ obtained after contracting the exceptional `(-2)`-curve. This checkpoint records exactly what this gives and why branch count alone cannot give a stronger local coefficient on an `A1` surface singularity.

## Universal reduced-curve inequality

Let `(C,p)` be any reduced complex curve germ and let `r_p` be its number of normalization branches. The normalization delta invariant satisfies

```text
Delta_p(C) >= r_p - 1.
```

Equality is the sharp minimum and characterizes an ordinary `r_p`-tuple in the abstract curve-germ sense.

Reference:

- J. I. Cogolludo-Agustin, T. Laszlo, J. Martin-Morales, A. Nemethi,
  *Delta invariant of curves on rational surfaces I. The analytic approach*,
  Communications in Contemporary Mathematics 24 (2022), 2150052,
  arXiv:1911.07539.
- Example 5.1 gives `delta(C)>=r-1` for every reduced curve germ and equality for the ordinary `r`-tuple.

Therefore, if `C` is the image on the singular cuboid surface of a strict transform with branch counts `r_i` over the 48 box nodes, then

```text
Delta_nodes_down >= sum_i (r_i-1) over r_i>0 = R-N,
```

where

```text
R=sum_i r_i,
N=#{i:r_i>0}.
```

For the FSM-minimal branch population, let `r8_i` count `(A,B)=(1,1)` branches and `N8=#{i:r8_i>0}`. Since `r_i>=r8_i`,

```text
Delta_nodes_down >= R8-N8 >= R8-48.
```

For a projective integral downstairs curve,

```text
p_a(C)-g = sum_p Delta_p(C),
```

so in particular

```text
R8 <= p_a(C)-g+48.
```

This genuinely counts repeated branches and is therefore stronger in type than node-support-only inequalities.

## Sharpness on an A1 surface singularity

The box nodes are `A1` rational double points, equivalently cyclic quotient singularities of type `1/2(1,1)`. Their minimal resolution has one `(-2)` exceptional curve and reduced fundamental cycle.

The same delta-invariant paper, Examples 5.2--5.5, treats rational singularities with reduced fundamental cycle. For a collection of smooth transversal curvettes on the minimal resolution, the contracted reduced curve germ has

```text
Delta_p(C)=r_p-1.
```

In particular, the coefficient one in the universal lower bound is **sharp already on A1**. Thus there is no universal local improvement of the form

```text
Delta_p(C) >= c*r_p - O(1)
```

with `c>1` based only on the number of smooth transverse branches over an A1 exceptional curve.

This is compatible with the earlier MB104 local feasibility packet: distinct FSM-minimal branches have exceptional multiplicity one and can land at distinct points of the exceptional line.

## Global degree comparison is too weak

For the remaining high-span sectors, one can combine the sharp conductor inequality with the classical Castelnuovo arithmetic-genus bound for a nondegenerate integral curve of degree `d` in its linear span. For full span `P^6`, writing

```text
d-1=5m+epsilon, 0<=epsilon<=4,
```

gives

```text
p_a(C) <= pi_6(d) = 5*m*(m-1)/2 + m*epsilon.
```

Hence

```text
R8 <= pi_6(d)-g+48,
```

which is asymptotically quadratic (`~d^2/10`), whereas the FSM inequality

```text
d <= 16g-16+4R8
```

requires an upper bound on `R8` with asymptotic slope strictly below `d/4` to close MB104. Castelnuovo plus the sharp local conductor bound therefore does not provide the needed finite degree window.

For genus-one span `P^5`, the corresponding Castelnuovo bound is also quadratic and has the same structural defect.

## Consequence

The conductor/delta route is retained as follows:

- positive: it gives the exact multiplicity-sensitive lower bound `Delta_nodes_down>=R-N`, hence `R8<=p_a(C)-g+48`;
- negative: `A1` realizes the sharp minimum `delta=r-1`, so no stronger universal local coefficient can be extracted from branch count alone;
- global: standard arithmetic-genus bounds are quadratic in degree and therefore do not meet the `alpha<1/4` target.

Any successful conductor continuation must exploit **additional global structure beyond local branch count**, for example a linear upper bound on downstairs arithmetic genus/conductor for the specific cuboid-surface curve class, or another invariant that charges repeated branches with a stronger degree-normalized coefficient.

## Firewalls

- `MB104_complete=false`.
- no absolute `R8` upper bound is proved.
- no finite degree window is released.
- no finite Picard enumeration is released.
- no receiver/effectivity/theorem/endpoint credit.
- no Perfect Cuboid existence or nonexistence claim.
- no merge authorization.
