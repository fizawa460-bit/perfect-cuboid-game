# MB104 — branchwise Freitag--Salvati Manni pole lemma

Status: **RETAINED NECESSARY INEQUALITY / MB104 STILL INCOMPLETE / NO RECEIVER CREDIT**

## Source

Freitag--Salvati Manni, *Parametrization of the box variety by theta functions* (2013), Section 3, Theorem 3.1 proof:

- source URL: `https://www.mathi.uni-heidelberg.de/~freitag/preprints/box.pdf`
- relevant printed pages: 10--11 (PDF pages containing Section 3 proof)
- theorem statement: for bijective normalization, `d <= 176 + 16g`;
- proof identity: `16(2g-2)k = #zeros - #poles`;
- zero lower bound: `#zeros >= 2kd`;
- local cusp vector satisfies `a1,a2>0`, `a1 == a2 == 0 mod 4`, `a1+a2 == 0 mod 8`, hence `a1+a2>=8`;
- local tensor contribution has differential pole order `16k` and `Delta(z)^k Delta(w)^k` zero order `(a1+a2)k`;
- the published proof then uses bijectivity only to replace the number of normalization branches over the 48 nodes by at most `48`, giving total pole order at most `384k`.

This node does not alter the published theorem. It extracts the branchwise inequality before that final bijectivity bound.

## Lift to the resolution without bijectivity

Let `nu:Cbar->C` be the normalization of an irreducible curve `C` on the box surface, and let `pi:S->B` be the blow-up/minimal resolution of the 48 ordinary double points. The composite `Cbar->B` lifts to `S`: on the smooth curve `Cbar`, the pullback of the ideal of a node is locally principal on every nonconstant branch, so the universal property of the blow-up applies branchwise.

Thus every normalization preimage over a box node gives a punctured disk to which the local cusp calculation in the published proof applies independently.

## Exact branchwise pole calculation

For a normalization branch `b` over a node, write its cusp vector as in the published proof

```text
(a1_b,a2_b),
a1_b,a2_b > 0,
a1_b == a2_b == 0 (mod 4),
a1_b+a2_b == 0 (mod 8).
```

In MB101 notation

```text
A_b=a1_b/4,
B_b=a2_b/4,
A_b,B_b positive integers,
A_b+B_b even.
```

Before cancellation, `(dzdw)^(8k)` contributes pole order `16k`; the two discriminant factors contribute zero order `(a1_b+a2_b)k`. Since the auxiliary modular form is chosen nonzero at every node, the net pole order at this branch is at most

```text
p_b(k)=k*max(0,16-a1_b-a2_b).
```

Because `a1_b+a2_b` is a positive multiple of `8`, there are only two cases relevant to poles:

```text
a1_b+a2_b=8   -> p_b(k)=8k,
a1_b+a2_b>=16 -> p_b(k)=0.
```

Equivalently in MB101 notation, a pole occurs only for

```text
(A_b,B_b)=(1,1).
```

Define

```text
R8 = number of normalization branches over all 48 nodes with (A,B)=(1,1).
```

Then

```text
#poles <= 8k R8.
```

The published zero-divisor argument is unchanged and gives

```text
#zeros >= 2kd.
```

Therefore

```text
16(2g-2)k = #zeros-#poles
             >= 2kd-8kR8,
```

so, after division by `2k`,

```text
d <= 16g - 16 + 4R8.                 (MB104-FSM-MB)
```

This is the exact multibranch correction to the point where the original proof inserts bijectivity.

## Recovery of the published theorem

If normalization is bijective, each box node has at most one normalization preimage, hence

```text
R8 <= 48.
```

The branchwise inequality becomes

```text
d <= 16g-16+4*48 = 176+16g,
```

exactly recovering Freitag--Salvati Manni Theorem 3.1.

## Interface with MB101

Every `(A,B)=(1,1)` branch has exceptional multiplicity

```text
m=min(A,B)=1.
```

Hence, with MB101 notation,

```text
R8 <= R <= M=sum_i D.E_i.
```

A weaker Picard-linear consequence is therefore

```text
d <= 16g-16+4M.
```

This weaker inequality is not a finite degree bound because MB101/MB102 currently provide no population-wide absolute bound on `M`.

## New exact bottleneck

The MB104 finite-window problem is now sharper. It is enough to control the **minimal-cusp branch count** `R8`; arbitrary high-contact branches `(A+B>=4)` create no pole in this argument and should not be charged.

A finite degree window would follow from either of the following genuinely new inputs:

```text
R8 <= constant,
```

or more generally

```text
R8 <= alpha*d + beta  with alpha < 1/4.
```

Indeed then

```text
(1-4alpha)d <= 16g-16+4beta.
```

No such bound is claimed in this checkpoint.

## Relation to later symmetric-differential literature

Bruin--Thomas--Varilly-Alvarado, arXiv:1912.08908, Theorem 1.2, constrains the number and span of **distinct nodes** met by genus `0` or `1` curves; the same paper also proves abstract finiteness for genus `0/1` curves through at most 13 singularities. Those results constrain node support `N`, not the normalization multiplicity `R8` at a node, so they do not by themselves close `(MB104-FSM-MB)`.

## Firewalls

- This is a necessary inequality, not an existence theorem.
- It does not assert that every formal MB101 profile is realized by a curve.
- It does not import the bijective `176/192` windows into the multibranch population.
- It does not bound `R8`, `R`, or `M` absolutely.
- MB104 remains incomplete and finite Picard enumeration remains unreleased.
- No receiver/effectivity/final-milestone/theorem/endpoint or Perfect Cuboid credit is granted.
