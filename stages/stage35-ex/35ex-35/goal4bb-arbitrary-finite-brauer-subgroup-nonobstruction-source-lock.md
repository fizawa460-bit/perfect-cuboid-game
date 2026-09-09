# Stage35-EX Goal4BB source lock — arbitrary finite Brauer subgroups are non-obstructing on the source-local relaxation

Scope: strengthen Goal4BA from the explicit visible algebraic/unit-character subgroup to an **arbitrary fixed finite set of classes in `Br(U)`**. Audited authority remains V74 / Goal4AK. The result is a finite-subgroup nonobstruction theorem on the source-admissible adelic relaxation `A_src^loc`; it is not a statement about the full infinite Brauer intersection, E1, or Perfect Cuboid existence/nonexistence.

## 1. Geometry and local population

Let `U={h!=0}` be the smooth open of the minimal resolution used throughout Goal4Y--Goal4AR. The exact affine receiver chart contains

```text
U_PC:
p^2=1+x^2,
q^2=1+y^2,
z^2=x^2+y^2,
w^2=1+x^2+y^2,
x*y*p*q*z*w != 0.
```

Goal4AO fixes

```text
A_src^loc
 = U_PC(R)^+
   x U_PC(Q_2)^src
   x product'_{ell odd} U_PC(Q_ell),

U_PC(Q_2)^src
 = {P:v2(x)>0,v2(y)>0,v2(x)!=v2(y)}.               (BB-LOC)
```

Retain the 35EX-22 rational smooth affine anchor

```text
P*=(272/225,0,353/225,1,272/225,353/225).            (BB-P*)
```

It has `h=1` and is a smooth point of the affine receiver, hence defines a rational point of `U`. It is outside the selected `U_PC` only because `y=0`.

35EX-22 proves two exact facts used below:

1. at every fixed local place, nonzero-`y` points of `U_PC` exist in every sufficiently small neighborhood of `P*`;
2. for every prime `ell>=173`, there is an integral smooth point `Q_ell in U_PC(Z_ell)`; the construction is a smooth Hensel lift and all six open coordinates are units.

At `Q_2`, the local deformation can be chosen with

```text
v2(y)>4=v2(272/225),                                  (BB-2)
```

so it lies in the source-marked subset. At infinity it can be chosen with `y>0`.

## 2. Fix an arbitrary finite Brauer set

Let

```text
F={alpha_1,...,alpha_r} subset Br(U)                  (BB-F)
```

be any finite set. No algebraicity, explicit symbol presentation, unit-character description, or membership in the known `A,B` span is assumed.

For each fixed `alpha_j`, Goal4AN's general spread-out argument applies: a Brauer class on the finite-type Q-variety `U` is represented by finite algebraic/etale data and therefore extends, after inverting finitely many rational primes, to a Brauer class on a smooth integral model of the relevant open. Because `F` is finite, one common finite set of excluded primes works for all `alpha_j` simultaneously.

Likewise, local evaluation of a Brauer class on a smooth variety over a local field is locally constant. Since `F` is finite, at each fixed local place the finitely many local-constancy neighborhoods of `P*` have a common intersection.

## 3. Choose one finite bad set S

Choose a finite set of places `S` containing:

- infinity and `2`;
- all primes `<173`;
- all denominator primes of `P*`;
- every bad-reduction/model prime needed to spread out `U`, the smooth affine locus used by 35EX-22, and every `alpha_j`;
- any additional primes required so that the integral 35EX-22 smooth points lie on the chosen common smooth integral model.

Outside `S`, each `alpha_j` extends to the common smooth model and `P*` gives an integral section.

## 4. Bad places: simultaneous deformation preserves all finite evaluations

For each `v in S`, take a nonzero-`y` deformation

```text
Q_v in U_PC(Q_v)
```

inside a common local-constancy neighborhood of `P*` for **all** `alpha_j`. At `v=2` impose `(BB-2)`; at infinity impose `y>0`.

Then

```text
inv_v alpha_j(Q_v)=inv_v alpha_j(P*)
for every alpha_j in F and every v in S.             (BB-BAD)
```

This uses only finiteness of `F` and local constancy; no explicit formula for any `alpha_j` is required.

## 5. Good primes: integral evaluation is zero for every class in F

For `ell notin S`, choose the integral smooth open point

```text
Q_ell in U_PC(Z_ell)
```

from 35EX-22. Both `Q_ell` and the integral specialization of `P*` define `Z_ell`-points of the common smooth model.

Each extended `alpha_j` therefore pulls back to `Br(Z_ell)`. The Henselian local-ring Brauer identification used already in Goal4AN gives

```text
Br(Z_ell) ~= Br(F_ell)=0.
```

Consequently

```text
alpha_j(Q_ell)=0=alpha_j(P*) in Br(Q_ell),
```

and hence

```text
inv_ell alpha_j(Q_ell)=inv_ell alpha_j(P*)=0          (BB-GOOD)
```

for every `alpha_j in F` and every `ell notin S`.

## 6. Global reciprocity

The choices `(BB-BAD)` and `(BB-GOOD)` give, for every place `v` and every `alpha_j in F`,

```text
inv_v alpha_j(Q_v)=inv_v alpha_j(P*).                 (BB-MATCH)
```

Because `P* in U(Q)`, its evaluation `alpha_j(P*)` is a class in `Br(Q)`. Global Brauer reciprocity gives

```text
sum_v inv_v alpha_j(P*)=0.
```

Using `(BB-MATCH)`,

```text
sum_v inv_v alpha_j(Q_v)=0
```

for every `alpha_j in F`.

All but finitely many `Q_ell` are integral, `Q_infinity` is positive, and `Q_2` satisfies the exact source marking. Thus

```text
Q=(Q_v) in (A_src^loc)^F,
```

and therefore

```text
(A_src^loc)^F != empty                                (BB-THEOREM)
```

for **every finite set `F subset Br(U)`**.

Equivalently, every finite subgroup `B0 subset Br(U)` has

```text
(A_src^loc)^B0 != empty.                              (BB-FINITE)
```

## 7. Relation to Goal4AQ / Goal4AR

Goal4AQ proves that the full infinite visible unit-character layer is endpoint-equivalent. Goal4AR proves the full Brauer route is endpoint-equivalent:

```text
(A_src^loc)^Br(U) nonempty
iff positive source-marked U(Q) point exists
iff Stage35 E1-counterexample population nonempty.
```

Goal4BB is fully compatible with this. It says only that **every finite intersection** of Brauer orthogonality conditions is nonempty. It does not assert that the infinite intersection over all of `Br(U)` is nonempty.

Thus any Brauer obstruction capable of closing E1 on this local population would necessarily be genuinely infinite in the sense that no finite subgroup already gives emptiness.

This strictly strengthens Goal4AR's previous boundary

```text
finite_additional_Brauer_shortcut_ruled_out=false
```

to the provisional exact statement

```text
finite_additional_Brauer_shortcut_ruled_out=true
```

for the source-local population `A_src^loc`.

No computation of the transcendental Brauer group is needed for this finite-subgroup theorem: arbitrary fixed transcendental classes are included in `F` and handled by the same local-constancy/spread-out argument.

## 8. Credit boundary and next route

Certified provisionally:

```text
EVERY_FINITE_BRAUER_SUBGROUP_BM_NONEMPTY=true;
FINITE_BRAUER_SHORTCUT_RULED_OUT=true;
FULL_INFINITE_BRAUER_ROUTE_ENDPOINT_EQUIVALENT=true.
```

Not certified:

```text
(A_src^loc)^Br(U) nonempty;
Br(U) explicitly computed;
transcendental Brauer group computed;
E1;
Stage35 closure;
Perfect Cuboid existence/nonexistence.
```

Goal4BB also supersedes the need to compute the visible-unit lattice index merely for the purpose of excluding a finite Brauer shortcut. That index remains structurally interesting but is no longer load-bearing for this route.

After Goal4BB, every lens in the Goal4AS fresh candidate ledger has received an exact test or blocker: marked Kummer/common-cover, canonical height, nonlinear descent, finite Brauer shortcut, amplification/counting, and cross-face norm/torsor. The next required action is therefore a fresh post-ledger breadth audit rather than silently recycling one of these exhausted views.

Next unit:

```text
35EX-35_GOAL4BC_POST_GOAL4AS_LEDGER_EXHAUSTION_FRESH_VIEW_AUDIT
```

No merge. No hostile-audit credit. MAIN-STATE remains V74 / Goal4AK.
