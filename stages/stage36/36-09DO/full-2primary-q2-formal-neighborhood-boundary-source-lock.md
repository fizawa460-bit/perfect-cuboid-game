# Stage36 36-09DO local full-2-primary formal-neighborhood boundary source lock

## Sources

1. Stephen Lichtenbaum, *Duality theorems for curves over p-adic fields*, Invent. Math. 7 (1969), 120--136, DOI 10.1007/BF01389795.
2. Arthur Mattuck, *Abelian varieties over p-adic ground fields*, Ann. of Math. (2) 62 (1955), 92--119, DOI 10.2307/2007101, especially Theorem 7.
3. J. S. Milne, *Arithmetic Duality Theorems*, 2nd ed., local duality for abelian varieties (Theorem I.3.2 in the online notes / Theorem III.7.8 in standard citations).
4. Stage36 36-09DN source lock `stages/stage36/36-09DN/full-br2-local-common-neighborhood-source-lock.md`.

## Frozen local-duality interface

Let `K=Q_2`, let `C=C3_2 x_Q K`, and let `J=Jac(C)`. The global rational point `P0=(0,1)` identifies `Pic^0(C)` with `J(K)` and splits the degree contribution. Lichtenbaum local duality identifies the nonconstant Brauer evaluation pairing with the Pontryagin dual pairing against `J(K)`.

For each `n>=1`, the local nonconstant `2^n`-torsion Brauer characters are represented inside the continuous `2^n`-torsion character group of `J(K)`. Equivalently, local Tate duality identifies `H^1(K,J)[2^n]` with the dual of the finite quotient `J(K)/2^n J(K)` (up to the standard self-dual Jacobian identification).

Thus an element `x in J(K)` is annihilated by **all** local 2-primary Brauer characters only if its image vanishes in every finite quotient `J(K)/2^n J(K)`, i.e.

`x in intersection_{n>=1} 2^n J(K)`.

## Mattuck structure at Q2

Mattuck Theorem 7 gives an open finite-index subgroup of `J(Q_2)` analytically/topologically isomorphic to `Z_2^g`, where `g=dim J=3` for `C3_2`.

After shrinking, choose a torsion-free open subgroup

`M ~= Z_2^3`.

The compact abelian group `J(Q_2)` is therefore a finite extension of `Z_2^3`. Its infinitely 2-divisible subgroup `intersection_n 2^n J(Q_2)` is finite of odd order; in particular its intersection with `M` is `{0}`.

Hence every nonzero `x in M` survives in `J(Q_2)/2^n J(Q_2)` for some `n`. Since that quotient is finite abelian, there is a finite-order character of 2-power order nonzero on the image of `x`; local Tate/Lichtenbaum duality realizes it as a local 2-primary Brauer evaluation character.

## Abel-Jacobi consequence near P0

Because `C3_2` has genus 3, the Abel-Jacobi map based at `P0`,

`iota: C(Q_2) -> J(Q_2),   P |-> [P-P0]`,

is locally injective at `P0` (indeed the usual Abel-Jacobi map is an embedding for a positive-genus smooth projective curve). Shrink an analytic neighborhood `N` of `P0` until `iota(N)-iota(P0)` lies in the torsion-free Mattuck subgroup `M`.

Then for every `P in N` with `P != P0`, the displacement `[P-P0]` is nonzero in `M`, so some local 2-primary Brauer class has evaluation at `P` different from its evaluation at `P0`.

Therefore there is **no punctured analytic neighborhood of P0** on which all local `2^infinity`-primary Brauer evaluations are simultaneously equal to their value at `P0`.

This is an exact obstruction to extending the finite-intersection argument of 36-09DN from exponent 2 to the full local 2-primary Brauer group at the dyadic place.

## Odd finite places

For `K=Q_p` with odd `p`, Mattuck gives an open pro-`p` subgroup of `J(K)`. Continuous 2-primary characters kill that pro-`p` subgroup, so only the finite quotient contributes to the local 2-primary character group. Thus the structural infinite 2-primary common-neighborhood failure is specifically dyadic; odd finite places do not create the same unbounded-exponent problem.

## Global-local firewall

The preceding argument concerns the **entire local** 2-primary Brauer/Weil--Chatelet character group at `Q_2`.

It does **not** show that every separating local class is the localization of a global class in `Br(C3_2)[2^infinity]`. Therefore it does not prove that

`U_ret(A_Q)^{Br(C3_2)[2^infinity]}`

is empty, and it does not prove fixed `p=2` exclusion.

The next missing object is the localization image

`loc_2(Br(C3_2)[2^infinity]/Br(Q)[2^infinity])`

inside the local nonconstant `2`-primary Brauer group. Two opposite outcomes remain possible:

- the global localization image has bounded exponent / finite image, in which case a DN-style finite common-neighborhood argument may revive for the **global** 2-primary subgroup;
- the global localization image contains sufficiently deep dyadic characters, in which case it may separate all retained-open formal points near `P0` and produce a genuine global Brauer-Manin restriction.

No conclusion between those alternatives is imported here.

## Firewalls

This source lock proves only the local dyadic formal-neighborhood no-go for simultaneous full-2-primary constancy. It does not prove full 2-primary Brauer-set nonemptiness or emptiness, full Brauer-set nonemptiness or emptiness, a Brauer-Manin obstruction, fixed-p exclusion, candidate shrink, receiver emptiness, endpoint closure, or Perfect Cuboid nonexistence.
