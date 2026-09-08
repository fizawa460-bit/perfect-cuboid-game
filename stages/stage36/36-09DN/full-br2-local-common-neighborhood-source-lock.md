# Stage36 36-09DN full local 2-torsion Brauer common-neighborhood source lock

## Sources

1. Stephen Lichtenbaum, *Duality theorems for curves over p-adic fields*, Inventiones Mathematicae 7 (1969), 120--136, DOI 10.1007/BF01389795.
2. Joost van Hamel, *Lichtenbaum-Tate duality for varieties over p-adic fields*, J. reine angew. Math. 514 (1999), conceptual reconstruction of Lichtenbaum's curve pairing.
3. Tetsuya Uematsu, *Continuity of the local evaluation maps* (2012 note), Theorem 1.1.

The Creutz--Viray background remains source-locked separately in
`stages/stage36/36-09DD/creutz-viray-explicit-image-completeness-source-lock.md`.

## Frozen local-duality interface

Let `K` be a finite extension of `Q_p` and let `C/K` be a smooth projective geometrically integral curve with a `K`-rational point `P0`. Write `J=Jac(C)`.

Lichtenbaum's pairing is the divisor/Brauer evaluation pairing

`Pic(C) x Br(C) -> Br(K) ~= Q/Z`

and is nondegenerate/perfect in the p-adic curve sense. The rational point splits the degree map, so

`Pic(C) ~= Z[P0] + Pic^0(C)`

with `Pic^0(C)=J(K)`. Constant Brauer classes pair only through degree. Consequently the 2-torsion quotient

`(Br(C)/Br(K))[2]`

is dual to a quotient of `J(K)/2J(K)`; in particular it is finite. Equivalently, this finiteness follows from local Tate/Kummer duality: `J(K)/2J(K)` and `H^1(K,J)[2]` are finite, and a rational point identifies the nonconstant Brauer quotient with the corresponding Weil--Chatelet group.

Only **finiteness** of the local nonconstant 2-torsion Brauer quotient is used below. No explicit computation of that group and no Creutz--Viray surjectivity is imported.

## Frozen local-constancy interface

Uematsu Theorem 1.1 states: for a local field `K`, a smooth `K`-scheme `X`, and `A in Br(X)`, the evaluation map

`X(K) -> Br(K) -> Q/Z`

is locally constant in the analytic topology.

Therefore, for the finite group `(Br(C)/Br(K))[2]`, choose finitely many representatives `A_1,...,A_r`. Intersect local neighborhoods of `P0` on which every `A_i` has the same evaluation as at `P0`. The intersection is one common analytic neighborhood `N_K(P0)` such that **every** class in `Br(C)[2]` has the same evaluation at every point of `N_K(P0)` as at `P0`; constant classes require no restriction.

This is a finite-intersection argument. It does not intersect class-dependent neighborhoods over the full infinite Brauer group or over all `2^n`-primary torsion.

## Real place

For `K=R`, each Brauer evaluation map is locally constant. Hence it is constant on the connected component of `P0`. For the Stage36 real curve, the positive-`z` branch through `P0=(0,1)` contains nonboundary points arbitrarily close to `P0`.

## Stage36 retained-open intersection

For

`C3_2: z^2=(t^2+4)(t^2+1/4)(t^2+9)(t^2+1/9)`

we have `P0=(0,1)`. It is a smooth rational point because the right-hand side is `1` at `t=0` and the partial derivative with respect to `z` is `2 != 0` over every characteristic-zero completion.

The retained receiver open removes only a proper finite boundary on this curve (in particular `t=0, +/-1, infinity` in the retained p=2 lane). Thus every sufficiently small local analytic neighborhood of `P0` contains retained-open local points. At finite primes outside the fixed denominator set `{2,3}`, such a point can be chosen integral by taking a sufficiently small nonzero integral `t` and the analytic square root near `z=1`.

Hence, for every place `v` of `Q`, one may choose

`P_v in U_ret(Q_v) intersect N_v(P0)`.

The resulting tuple is adelic: outside `{2,3,infinity}` the chosen points may be integral.

## Global reciprocity consequence for Br[2]

For every global `A in Br(C3_2)[2]` and every place `v`, the construction gives

`inv_v A(P_v) = inv_v A(P0)`.

Because `P0` is a global rational point, `A(P0)` is one class in `Br(Q)`, so global Brauer reciprocity gives

`sum_v inv_v A(P0)=0`.

Therefore

`(P_v) in U_ret(A_Q)^{Br(C3_2)[2]}`.

This proves nonemptiness of the retained-open adelic set orthogonal to the **entire 2-torsion Brauer group** of the smooth projective curve, including classes outside the Creutz--Viray explicit image.

## Firewalls

This source lock does **not** prove:

- orthogonality to all `2^n`-primary Brauer classes simultaneously;
- orthogonality to the full Brauer group;
- that the Creutz--Viray explicit image equals `Br(C3_2)[2]`;
- any Kummer-variety hypothesis required by LIT-PW05;
- fixed `p=2` parameter exclusion;
- receiver emptiness or endpoint closure.

Per-class local constancy alone is not a uniform full-Brauer formal-disk theorem. The upgrade here is valid only for exponent `2`, because the local nonconstant 2-torsion quotient is finite.
