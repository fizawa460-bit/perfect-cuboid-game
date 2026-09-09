# Stage36 36-09EC factor pro-Selmer / Mordell--Weil closure source lock

## Purpose

36-09EA and 36-09EB reduce the fixed `p=2` retained-open Brauer problem to four concrete translations

`r + Phi(loc_A(T_2 Sel(A)))`,

with

`R={0,D_plus,D_minus,D_sum}`

and corrected hostile-audited Phi labels. The remaining literal-product input is

`T_2 Sel(A)=T_2 Sel(E_tau) x T_2 Sel(E_sigma) x T_2 Sel(E_rho)`.

This leaf computes the factor `[2]`-Selmer dimensions exactly from the already retained DW local `[2]`-Kummer images and shows that the factor pro-Selmer systems are exactly the 2-adic Mordell--Weil completions. It therefore replaces the abstract elliptic pro-Selmer factors by a rank-one Mordell--Weil closure problem before any translated retained-open intersection is claimed decided.

## Source-bound inputs

1. 36-09DR fixes `A=E_tau x E_sigma x E_rho` and the three quotient quartics.
2. 36-09DV fixes the conservative bad/required set `S={infinity,2,3,5,7}` and records that the displayed quotient models have good reduction outside the finite part of `S`. For the factor multiplication-by-two descents, `deg([2])=4` is also a unit outside `S`; hence the factor local Kummer conditions are unramified there and the same `Q(S,2)` ambient is sufficient.
3. 36-09DW directly computes the exact factorwise local `[2]`-Kummer images at all places in `S`. These factor images were computed before the historical incorrect Phi-orthogonal-complement step and are retained by the hostile-audited DW correction.
4. 36-09DZ proves `rank A(Q)=1` using the explicit non-torsion point on `E_tau`. Since `A` is the literal direct product and `rank(E_tau)>=1`, this forces `rank E_tau(Q)=1`, `rank E_sigma(Q)=0`, `rank E_rho(Q)=0`.
5. Every factor has full rational 2-torsion, so `dim_F2 E_h(Q)[2]=2`.

## Exact global factor `[2]`-Selmer replay

For each factor use the 10-dimensional ambient `Q(S,2)^2` with ordered squareclass generators `[-1],[2],[3],[5],[7]` in each of the two factor Kummer coordinates. Localize those ten basis classes at `infinity,2,3,5,7` using the same squareclass bit conventions as DW, and intersect with the exact DW factor local Kummer subspaces.

The resulting constraint ranks and global Selmer dimensions are

- `E_tau`: constraint rank `7`, so `dim Sel_2(E_tau/Q)=3`;
- `E_sigma`: constraint rank `8`, so `dim Sel_2(E_sigma/Q)=2`;
- `E_rho`: constraint rank `8`, so `dim Sel_2(E_rho/Q)=2`.

One deterministic RREF basis in squareclass-pair notation is

`Sel_2(E_tau)`:
- `([-1],[3])`,
- `([7],[7])`,
- `([1],[2])`;

`Sel_2(E_sigma)`:
- `([-1],[1])`,
- `([1],[6])`;

`Sel_2(E_rho)`:
- `([-1],[1])`,
- `([1],[3])`.

Only the subspaces/dimensions are authoritative; another row basis for the same subspace is equivalent.

## Sha consequence

For every elliptic curve over Q the Kummer exact sequence gives

`0 -> E(Q)/2E(Q) -> Sel_2(E/Q) -> Sha(E/Q)[2] -> 0`.

Because each factor has rational 2-torsion dimension 2,

`dim E(Q)/2E(Q) = rank E(Q) + 2`.

The rank vector `(1,0,0)` therefore gives lower dimensions `(3,2,2)`, exactly equal to the computed Selmer dimensions. Hence

`Sha(E_tau)[2]=Sha(E_sigma)[2]=Sha(E_rho)[2]=0`.

A nonzero 2-primary torsion group always contains an element of order 2. Consequently `Sha(E_h)(2)=0` for all three factors, and in particular `T_2 Sha(E_h)=0`.

Thus `T_2 Sel(E_h)=E_h(Q)^hat_2` for each factor and `T_2 Sel(A)=A(Q)^hat_2`.

## Jacobian consequence

36-09DZ already proves `Sha(A)[Phi]=0` and the exact Snake-lemma comparison for the degree-eight isogeny `Phi:A->J`.

Since `Sha(A)(2)=0`, its divisible 2-primary part is zero. The DY/DZ comparison therefore gives zero cokernel on the `T_2 Sha` row. Hence `T_2 Sha(J)=0` and the DQ exact sequence reduces to

`T_2 Sel(J)=J(Q)^hat_2`.

This is an exact equality of the global pro-Selmer object with the 2-adic Mordell--Weil completion for the fixed curve; no finiteness hypothesis on an otherwise unknown Sha is being assumed.

## Exact EC reformulation

The four EA/EB translated intersections are now the single exact question

`iota_hat_2(U_ret(A_Q)) intersect loc_J(J(Q)^hat_2)`.

Equivalently, using EB's four representatives,

`iota_hat_2(P_v)=loc_J(r)+Phi(loc_A(a))`

for some `r in {0,D_plus,D_minus,D_sum}` and `a in A(Q)^hat_2`.

Thus the remaining obstruction is no longer an unknown pro-Selmer or Sha contribution. It is a concrete 2-adic Mordell--Weil closure / retained-open curve intersection.

The literal rank is one: the free 2-adic direction comes from `E_tau`, while `E_sigma` and `E_rho` have rank zero. The next exact step is therefore a dyadic rank-one intersection computation, with finite 2-primary torsion translates and the four EB defect representatives retained explicitly.

## Useful exact generator witness

36-09DZ gives the quartic point `Q_tau=(-29/11,875/121)` mapping to `P=(1,10)` on `V^2=U(U+1)(U+49)`. Direct evaluation of the DW `E_tau` factor Kummer functions relative to `(0,1)` gives squareclass pair `([-7],[42])`.

In the global `Sel_2(E_tau)` basis above this equals the sum of all three basis rows. The next leaf may use this together with explicit torsion Kummer classes to certify that the free coefficient of `P` is odd and hence that `P` spans the free Mordell--Weil direction after 2-adic completion. EC itself does not need that saturation statement to obtain `T_2 Sel(E_tau)=E_tau(Q)^hat_2`.

## Credit boundary

EC does **not** yet claim that any of the four translated retained-open intersections is empty or nonempty. It does not claim the global 2-primary Brauer set empty or nonempty, no Brauer--Manin obstruction, no fixed-`p=2` exclusion, no candidate shrink, no receiver closure, no endpoint closure, and no Perfect Cuboid result.

The exact gain is that every pro-Selmer/Sha ambiguity has been removed: the remaining problem is a rank-one dyadic Mordell--Weil closure intersection with four explicit rational translations.
