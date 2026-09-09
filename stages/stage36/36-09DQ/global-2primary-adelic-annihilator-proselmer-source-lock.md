# Stage36 36-09DQ global 2-primary adelic annihilator / pro-Selmer source lock

## Sources

1. Cristian D. Gonzalez-Aviles and Ki-Seng Tan, *A generalization of the Cassels-Tate dual exact sequence*, Math. Res. Lett. 14 (2007), no. 2, 295--302, DOI 10.4310/MRL.2007.v14.n2.a11, arXiv:math/0608587. Main Theorem.
2. Bjorn Poonen and Jose Felipe Voloch, *The Brauer-Manin obstruction for subvarieties of abelian varieties over function fields*, Proposition 4.3, for the equivalent Cassels-dual exact-sequence formulation `0 -> pro-Selmer -> adelic A -> H^1(A^vee)^D` without a finiteness assumption on Sha. This is used only as a conceptual cross-check; the Stage36 number-field 2-primary statement is source-bound to Gonzalez-Aviles--Tan.
3. Stage36 36-09DN source lock `stages/stage36/36-09DN/full-br2-local-common-neighborhood-source-lock.md` for the rational-point Brauer/Weil--Chatelet identification and local evaluation pairing.
4. Stage36 36-09DP source lock `stages/stage36/36-09DP/global-q2-2primary-weil-chatelet-localization-source-lock.md` for the exact global 2-primary localization result already promoted at the parent leaf.

## Unconditional generalized Cassels--Tate interface

Let `A/K` be an abelian variety over a global field and let `m` be a positive integer. Gonzalez-Aviles--Tan define

`T_m Sel(A^t) = inverse_limit_n Sel_{m^n}(A^t)`

and prove the natural exact sequence of compact groups

`0 -> T_m Sel(A^t) -> product_v H^0(K_v,A^t)^hat_m -> H^1(K,A)(m)^D -> Sha(A)(m)^D -> 0`.

Here `(m)` denotes the `m`-primary component, `D` is Pontryagin dual, and `^hat_m` is the `m`-adic completion (with the standard modified `H^0` convention at archimedean places).

The key Stage36 use is exactness at the product of local points. No finiteness of `Sha(A)` is assumed.

## Specialization to the Stage36 Jacobian

Take

`K=Q`, `A=J=Jac(C3_2)`, `m=2`.

A Jacobian is principally polarized, so `J^t ~= J`. The exact sequence gives

`ker( product_v J(Q_v)^hat_2 -> H^1(Q,J)(2)^D ) = image(T_2 Sel(J))`.

The middle map is induced by the sum of the local Tate pairings:

`(x_v)_v |-> [ xi |-> sum_v <x_v, loc_v(xi)>_v ]`.

Thus the exact global 2-primary adelic annihilator is the image of `T_2 Sel(J)`, not automatically the closure of `J(Q)`.

## Brauer-Manin translation for C3_2

Fix the rational boundary point `P0=(0,1)` and the Abel--Jacobi map

`iota(P)=[P-P0] in J`.

For an adelic retained-open point `(P_v)_v`, write

`x_v=iota(P_v) in J(Q_v)`

and let `xhat_v` denote its image in the 2-adic completion `J(Q_v)^hat_2`.

By the DN Brauer/Weil--Chatelet identification, a global nonconstant 2-primary Brauer class corresponds to

`xi in H^1(Q,J)(2)`.

The difference between evaluation at `P_v` and evaluation at `P0` is the local Tate/Lichtenbaum pairing

`inv_v A(P_v) - inv_v A(P0) = <x_v, loc_v(xi)>_v`.

Since `P0` is a global rational point, the sum of `inv_v A(P0)` is zero by global Brauer reciprocity. Therefore

`sum_v inv_v A(P_v) = sum_v <x_v, loc_v(xi)>_v`.

A class of order `2^n` sees only the image of `x_v` modulo `2^n`, so the completed tuple `(xhat_v)_v` is the exact input to the generalized Cassels--Tate map.

Consequently

`(P_v) in U_ret(A_Q)^{Br(C3_2)(2)}`

if and only if

`(xhat_v)_v in image(T_2 Sel(J))`.

Equivalently, the full global 2-primary Brauer-Manin problem currently under study is the intersection problem

`iota_hat_2(U_ret(A_Q)) intersect image(T_2 Sel(J))`.

This is an exact reformulation for the 2-primary subgroup of the Brauer group of the smooth projective curve. It is not a statement about any additional ramified Brauer classes that could exist only on a chosen open model.

## Mordell--Weil closure firewall

For every `n` there is the Kummer/Selmer exact sequence

`0 -> J(Q)/2^n J(Q) -> Sel_{2^n}(J) -> Sha(J)[2^n] -> 0`.

Passing to inverse limits places the 2-adic Mordell--Weil completion inside `T_2 Sel(J)`, with the possible extra part measured by the 2-adic Tate module of `Sha(J)`.

If the relevant infinitely 2-divisible part of `Sha(J)` vanishes (in particular if `Sha(J)[2^infinity]` is finite), then

`T_2 Sel(J) = J(Q)^hat_2`

and its adelic image is the corresponding 2-adic Mordell--Weil closure. Stage36 has not proved such a Sha hypothesis, so DQ must retain `T_2 Sel(J)` as the unconditional annihilator.

## Finite-level route

Membership in `image(T_2 Sel(J))` can be approached through the compatible tower

`Sel_2(J), Sel_4(J), Sel_8(J), ...`.

At each level `2^n`, the adelic Abel--Jacobi image may be reduced modulo `2^n` and tested against the localized `Sel_{2^n}(J)` image. To obtain a genuine pro-Selmer element one must retain compatibility under the transition maps as `n` grows; isolated success at one finite level is not enough.

This selects the next Stage36 leaf as a finite-level/pro-Selmer curve-intersection preflight rather than another single-place Brauer character computation.

## Firewalls

DQ computes the exact annihilator object but does not decide whether the retained-open adelic curve image intersects it. Therefore it proves neither nonemptiness nor emptiness of the global 2-primary Brauer set, no Brauer-Manin obstruction, no fixed `p=2` exclusion, no candidate shrink, no receiver closure, no endpoint closure, and no Perfect Cuboid claim.