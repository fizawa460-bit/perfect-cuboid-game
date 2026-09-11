# Stage32 MB104 checkpoint — finite window reduced to a minimal-cusp branch bound

Status: **ACTIVE RETAINED CHECKPOINT / MB104 NOT COMPLETE / NO CREDIT**

## Baseline insufficiency

MB101 plus MB102 alone do not force a finite upper bound on canonical degree `d=H.D`. Their numerical contracts admit formal arbitrary even-degree data such as

```text
g=1: D^2=-d,   Delta_total=0,
g=0: D^2=-d-2, Delta_total=0,
```

which satisfy the retained adjunction/normalization identity and Hodge upper bound. This is an insufficiency witness only; it is not an existence claim for curves.

## Branchwise Freitag--Salvati Manni extension

The proof of Freitag--Salvati Manni Theorem 3.1 was re-opened at the exact point where bijective normalization is used. The published proof has

```text
16(2g-2)k = #zeros - #poles,
#zeros >= 2kd.
```

For one normalization branch over a box node with cusp vector `(a1,a2)`, the differential contributes pole order `16k` and the discriminant factors contribute zero order `(a1+a2)k`. The translation-lattice congruences force

```text
a1,a2>0,
a1 == a2 == 0 mod 4,
a1+a2 == 0 mod 8.
```

Thus a positive pole occurs only when `a1+a2=8`, equivalently in MB101 notation only for `(A,B)=(1,1)`, and then its order is `8k`.

Let

```text
R8 = number of normalization branches over the 48 nodes with (A,B)=(1,1).
```

Summing branchwise yields the retained necessary inequality

```text
d <= 16g - 16 + 4R8.                 (MB104-FSM-MB)
```

For bijective normalization, `R8<=48`, and the published bound is recovered exactly:

```text
d <= 16g-16+4*48 = 176+16g.
```

The detailed proof and certificate are in `FSM-MULTIBRANCH-POLE-*`.

## Exact missing input

A finite degree window follows from either

```text
R8 <= constant,
```

or

```text
R8 <= alpha*d + beta,  alpha < 1/4.
```

Every minimal cusp branch has exceptional multiplicity one, hence

```text
R8 <= R <= M=sum_i D.E_i.
```

## Routes now source-checked and too weak

### Local A1 geometry

Distinct minimal branches can have distinct nonzero landing parameters on the exceptional line and separate after resolution. The local A1/FSM packet therefore gives no bounded number of `(1,1)` branches per node.

### Garcia-Fritz--Urzua symmetric differentials

Their degree computation is `-d+M+4g-4`; in the smooth-at-nodes case it yields `d<=4g+44`, but for the multibranch receiver the uncontrolled term is precisely exceptional mass `M`. Their multiple-differential refinement yields lower exceptional-incidence bounds rather than the required upper `R8` bound.

### Six rank-3 genus-5 fibrations

The six rank-3 quadrics have eight-node base sets that partition the 48 nodes. For the associated nef fiber class,

```text
2F_Q = H - sum_{i in B_Q}E_i,
```

so blockwise nonnegativity gives

```text
sum_{i in B_Q}M_i <= d.
```

Summing all six blocks gives only

```text
R8 <= M <= 6d,
```

far weaker than the required slope `<1/4`. The full family of 28 genus-5 fibrations would need an additional branchwise ramification/tangent charging lemma; simple base-locus/fiber intersection data do not suffice.

### Direct Hodge / Picard projection

Orthogonal projection to `H` and the 48 exceptional classes gives

```text
D^2 <= d^2/16 - (1/2)sum_i M_i^2.
```

Together with MB102,

```text
sum_i M_i^2 <= d^2/8 + 2d - 4g + 4,
R8 <= sqrt(6d^2 + 96d - 192g + 192).
```

Its asymptotic slope is `sqrt(6)`, again far above `1/4`.

The detailed negative-route ledger and certificates are in `R8-BOUND-ROUTE-LEDGER.md`, `R8-ROUTE-WALLS-CERTIFICATE.json`, and `HODGE-EXCEPTIONAL-MASS-*`.

## Current live route classes

The next result must be genuinely branch-sensitive rather than another exceptional-mass or node-support estimate. The surviving route classes are:

1. a global conductor/ramification inequality charging every minimal cusp branch to a bounded divisor;
2. a multi-fibration theorem proving unavoidable criticality for minimal branches strongly enough for a summed Riemann--Hurwitz bound;
3. a modular/symmetric-differential section with additional cusp/tangent vanishing, reducing or cancelling the `8k` minimal-branch pole charge.

Freitag--Salvati Manni explicitly note that a globally holomorphic tensor of their form would improve the degree bound; they report that they did not find such a modular form and suspected none exists, without proving nonexistence. Therefore route 3 is retained as a high-risk research route, not an existing weapon.

## Firewalls

No absolute `R8` bound is claimed. MB104 remains incomplete; finite Picard enumeration is unreleased. There is no receiver, effectivity, final-milestone, theorem, endpoint, Perfect Cuboid, or merge credit.
