# Stage32 MB104 — U12 dyadic Frattini source wall — 2026-09-18

Status: **W-INFINITY UNKNOWN / CONDITIONAL DIMENSION-FOUR CANDIDATE / PRIOR LEVEL-TWO CLAIM CORRECTED / NO CREDIT**

## Purpose

This leaf performs the hostile/source audit requested by
`MB104-U12-CONGRUENCE-CONTINUITY-GATE-20260917.md`.  It asks whether the
continuous mod-two character image of the dyadic closure is exhausted by the
known two-dimensional level-two quotient.

## Exact source boundary

Katz--Katz--Schein--Vishne, Sections 12--13, source-lock the quotient ring

```text
Q_B/2Q_B,
J=beta' Qbar,
J^2=eps Qbar,
J^3=eps beta' Qbar,
J^4=0,
```

and the exact global quotient

```text
B / P Q_B^1(2) ~= (F2)^2.
```

This proves only the first two-dimensional character image.  The source does
not compute the Frattini quotient of the full dyadic closure, the deeper
principal-level abelianizations, or stabilization of their images in
`H^1(B,F2)`.

The same radical calculation warns against silent stabilization: the deeper
unit filtration has nontrivial graded layers.  Their existence does not prove
that they survive as characters of `B`; conjugation coinvariants, norm one,
the projective center and global density all matter.

## Correct definition and missing locks

Let `G` be the explicitly represented dyadic closure of the Bolza surface
group and let `N_k` be a cofinal principal-level filtration.  The desired
object is

```text
W_infinity = image(Hom_cont(G,F2) -> H^1(Gamma,F2)),
```

equivalently the union of the marked restriction images over the `N_k` only
after cofinality is proved.

A proof-grade computation needs all of:

1. the exact 2-adic representation and equality of the global closure with the
   asserted local principal subgroup;
2. the reduced-norm, square, commutator and central filtrations far enough to
   compute `G/Phi(G)`;
3. cofinality of the chosen `N_k`;
4. the normalizer `S4` action and a marked restriction map into the named
   six-Weierstrass `J[2]` model;
5. a necessity lemma taking common affine spin descent to a character in this
   continuous image.

The repository currently has none of this complete chain.  In particular, the
archived marking work says that abstract group and Weil-form matching recovers
the Richelot plane but not a distinguished absolute line.

## Conditional local dimension candidate

Write `P=(Pi)` in the ramified local quaternion order, with

```text
P^2=(sqrt(2)),
P^4=(2).
```

For `G_n=SL1(O_D) intersect (1+P^n)`, standard valuation estimates give

```text
[G_3,G_3] subset G_6,
G_3^2 subset G_6.
```

Thus the layers at depths `3,4,5` can all contribute to the Frattini quotient.
The natural conditional graded count is

```text
2 + 1 + 2 - 1(center) = 4.
```

If local density and the exact norm/center filtration through `P^6` are
proved, this predicts

```text
dim W_infinity = 4,
W_infinity = H^1(Gamma,F2).
```

That would keep the adjacent theta difference visible at deeper level and
would defeat the hoped-for two-dimensional all-level obstruction.  Neither
the dimension-four conclusion nor the dimension-two alternative is currently
source-locked.  Dimension three is not excluded abstractly either.

## Smallest legal computation

The next exact computation is not an isolated split-prime test.  It is:

```text
1. construct the truncated skew local order O_D/P^6;
2. enumerate norm-one elements in G_3/G_6;
3. compute squares, commutators and the projective central image;
4. obtain the local Frattini quotient;
5. separately prove that the global principal subgroup is dense in the local
   subgroup used above and source-lock the marked restriction to J[2].
```

A finite plateau at one or two levels is not a stabilization theorem.  Without
the density, cofinality and marking adapters, a local enumeration is only a
conditional preflight.

## Consequence

```text
KATZ_LEVEL2_CHARACTER_RANK=2
W_INFINITY_DIMENSION=UNKNOWN
W_INFINITY_DIMENSION_2_PROVED=false
W_INFINITY_DIMENSION_4_PROVED=false
COMMON_LEVEL2_DESCENT_REJECTED=false
CONDITIONAL_MARKED_LEVEL2_LINEAR_ALGEBRA_VALID=true
U12_ALL_LEVEL_FINITE_FACTOR_PROVED=false
U12_REJECTED=false
```

U12 remains `HOLD`.  The earlier level-two note has been corrected in place so
that abstract `3+12` orbit arithmetic is not mistaken for a source-locked
marked descent theorem.

## Firewalls

```text
MB104_complete=false
all_l_exclusion_proved=false
finite_degree_window_proved=false
receiver_credit=false
effectivity_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
