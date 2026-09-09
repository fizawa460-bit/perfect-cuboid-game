# Stage36 36-09ED dyadic rank-one Mordell--Weil saturation source lock

## Purpose

36-09EC proves for the fixed curve that

`T_2 Sel(J)=J(Q)^hat_2`

and that the literal elliptic product has rank vector

`(rank E_tau, rank E_sigma, rank E_rho)=(1,0,0)`.

Thus the only infinite 2-adic Mordell--Weil direction is the `E_tau` direction. 36-09ED certifies an explicit 2-adically saturated generator for that direction, while keeping the finite torsion directions and the four 36-09EB Jacobian translations explicit. It does **not** yet decide any retained-open intersection.

## Locked inputs

1. 36-09DZ fixes the birational Weierstrass model

   `E_tau^W : V^2=U(U+1)(U+49)=U^3+50U^2+49U`

   and the rational non-torsion point

   `P=(1,10)`.

2. 36-09EC proves

   `rank E_tau(Q)=1`,

   `dim_F2 Sel_2(E_tau/Q)=3`,

   `Sha(E_tau)(2)=0`,

   and gives the exact global `[2]`-Kummer basis

   `([-1],[3]), ([7],[7]), ([1],[2])`.

3. 36-09DW fixes the `E_tau` factor Kummer functions on the quartic model

   `a_tau=(x+4)(x+1/4)`,

   `b_tau=(x+4)(x+9)`,

   relative to the rational base point `(0,1)`.

4. Arsenal workflow `S31-WF01` is consulted only as a credit firewall: a rank witness is not automatically a full saturated Mordell--Weil basis. ED therefore proves exactly the weaker statement needed here, namely saturation after 2-adic completion. It does not claim that `P` is a generator of `E_tau(Q)/tors` over `Z`.

## Exact rational 2-primary torsion on E_tau

The Weierstrass model has rational 2-torsion

`(0,0), (-1,0), (-49,0)`.

Set

`Q4=(7,56)`, `T=(-1,0)`.

Exact group-law replay gives

`2 Q4=(0,0)`

and hence `Q4` has order `4`; `T` is an independent order-2 point. Therefore

`<Q4,T> ~= Z/4Z x Z/2Z`

is a rational torsion subgroup of order `8`.

To prove it is the whole rational torsion group, use good reduction at `5` and `11`. The cubic discriminant has prime support contained in `{2,3,7}`, so both primes are good. Direct point counts give

`#E_tau(F_5)=8`,

`#E_tau(F_11)=16`.

For good reduction, prime-to-residue-characteristic rational torsion injects into the reduced group. The count at `5` excludes every prime-primary torsion component except possibly 2-primary and 5-primary, and bounds the 2-primary order by `8`; the count at `11` excludes 5-primary torsion. Thus

`E_tau(Q)_tors ~= Z/4Z x Z/2Z`

exactly, and it is entirely 2-primary.

The standard input here is the good-reduction injectivity of prime-to-residue-characteristic torsion (for example Silverman, *The Arithmetic of Elliptic Curves*, Chapter VII, §3).

## Torsion Kummer subspace in the retained DW coordinates

The DZ inverse birational map is

`x=-(U+28)/(4U+7)`,

`y=175V/(2(4U+7)^2)`.

It sends

`Q4=(7,56)` to `(-1,4)` on the quartic,

and

`Q4+T=(-7,42)` to `(1,25/3)` on the quartic.

Evaluating the retained DW Kummer functions relative to `(0,1)` gives

`delta_2(Q4)=([-1],[6])`,

`delta_2(Q4+T)=([1],[2])`.

Because the Kummer map is a homomorphism on `E_tau(Q)/2E_tau(Q)`, this also gives

`delta_2(T)=([-1],[3])`.

Hence the exact image of rational torsion modulo doubling is the two-dimensional subspace

`span{([-1],[3]),([1],[2])}`.

## P has odd free coefficient

36-09EC computes

`delta_2(P)=([-7],[42])`.

In the exact EC Selmer basis,

`([-7],[42]) = ([-1],[3]) + ([7],[7]) + ([1],[2])`

in squareclass-vector notation. Therefore `delta_2(P)` does not lie in the torsion Kummer subspace above; adjoining it raises the F2-rank from `2` to `3`, exactly the full dimension of `E_tau(Q)/2E_tau(Q)`.

Write the finitely generated Mordell--Weil group as

`E_tau(Q) ~= Z G + E_tau(Q)_tors`

and write

`P=mG+t`.

The image of `P` in the free quotient modulo `2` is nonzero, so `m` is odd. Thus `m` is a unit in `Z_2`, and `P` spans the free direction after 2-adic completion:

`E_tau(Q)^hat_2 = Z_2 P + E_tau(Q)_tors`.

Equivalently, `P` is a **2-adically saturated free generator**. This is intentionally weaker than claiming `m=+/-1` over `Z`.

## Exact ED reduction

Combining EC with the rank-zero factors gives

`A(Q)^hat_2 = (Z_2 P + E_tau(Q)_tors) x E_sigma(Q)(2) x E_rho(Q)(2)`.

The last two factors are finite because their Mordell--Weil ranks are zero. ED does not yet claim their complete torsion point lists; those finite lists may be materialized only if the translated intersection test needs them.

Therefore every one of the four EB translated adelic images is controlled by

- one coefficient `n in Z_2` multiplying the explicit point `P` in the `E_tau` direction;
- finitely many 2-primary torsion choices on the three elliptic factors;
- one of the four rational Jacobian translations `0,D_plus,D_minus,D_sum`.

The next exact leaf can work residue-disk by residue-disk at `Q_2`, using the rank-zero factors as finite constraints and the single `Z_2` parameter as the only infinite variable.

## Credit boundary

36-09ED does **not** decide any of the four translated retained-open intersections. It does not prove a global 2-primary Brauer set empty or nonempty, no Brauer--Manin obstruction, no fixed-`p=2` exclusion, no candidate shrink, no receiver closure, no endpoint closure, and no Perfect Cuboid result.

The exact gain is only the 2-adic saturation statement and the resulting one-variable-plus-finite reduction.
