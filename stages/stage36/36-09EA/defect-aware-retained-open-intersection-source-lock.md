# Stage36 36-09EA defect-aware retained-open intersection source lock

## Purpose

36-09DZ closes the finite-to-pro-Selmer isogeny defect numerically, but it does **not** identify the Jacobian pro-Selmer group with the product of the three elliptic quotient pro-Selmer groups.  The exact `Phi`-cokernel has four elements, so dropping it would repeat the historical 36-09DS error in a different form.

This leaf keeps that defect explicitly and rewrites the full fixed-`p=2` retained-open Brauer condition as a finite union of four translated elliptic-product pro-Selmer images.

No rational coset representatives are guessed here.  Their existence and number are exact; materializing them is the next arithmetic obligation.

## Locked inputs

Let

`J = Jac(C3_2)`,

`A = E_tau x E_sigma x E_rho`.

From the retained V4 geometry,

`Phi : A -> J`,

`Phi(a_tau,a_sigma,a_rho)=pi_tau^* a_tau + pi_sigma^* a_sigma + pi_rho^* a_rho`.

36-09DQ gives the exact fixed-2-primary Brauer--Manin interface

`(P_v) in U_ret(A_Q)^{Br(C3_2)(2)}`

if and only if

`iota_hat_2((P_v)) in loc_J(T_2 Sel(J))`,

where `iota(P)=[P-P0]` and `P0=(0,1)`.

36-09DZ proves

- `rank A(Q)=rank J(Q)=1`;
- `J(Q)/Phi A(Q)` is an F2-vector space of dimension 2 and cardinality 4;
- `Sha(A)[Phi]=0`;
- `Sha(J)[Psi]=0`;
- `ker(Phi_*:T_2 Sel(A)->T_2 Sel(J)) ~= (Z/2)^3`;
- `coker(Phi_*)` has F2 dimension 2 and cardinality 4;
- the finite `Phi`-Selmer group also has dimension 2/cardinality 4.

## The cokernel is represented by rational Mordell--Weil classes

Use the Kummer inverse-limit exact rows

`0 -> A(Q)^hat_2 -> T_2 Sel(A) -> T_2 Sha(A) -> 0`,

`0 -> J(Q)^hat_2 -> T_2 Sel(J) -> T_2 Sha(J) -> 0`.

The DY/DZ defect comparison shows that the `T_2 Sha` contribution to the `Phi` cokernel is zero.  Equivalently, the natural map

`J(Q)^hat_2 / Phi A(Q)^hat_2 -> T_2 Sel(J) / Phi_* T_2 Sel(A)`

is an isomorphism.

Because `J(Q)/Phi A(Q)` is finite 2-primary (indeed F2 dimension 2), completion does not change this quotient.  Hence there is a canonical identification of finite groups

`J(Q)/Phi A(Q) ~= coker(Phi_*) ~= (Z/2)^2`.

Choose any representative set

`R={r_0,r_1,r_2,r_3} subset J(Q)`

for `J(Q)/Phi A(Q)`, with `r_0=0` if desired.  No particular choice is authoritative at this leaf.

Then, as an exact union of cosets inside `T_2 Sel(J)`, 

`T_2 Sel(J) = union_{r in R} ( r + Phi_* T_2 Sel(A) )`.

The union is disjoint modulo `Phi_* T_2 Sel(A)` before localization.  After localization distinct global cosets may have the same adelic image; disjointness is not claimed there.

## Product structure on A is legitimate

This is not an identification of `T_2 Sel(J)` with an elliptic product.  It uses only the literal product variety

`A=E_tau x E_sigma x E_rho`.

At every finite level, Kummer cohomology and local Selmer conditions commute with finite products, so

`Sel_{2^n}(A) = Sel_{2^n}(E_tau) x Sel_{2^n}(E_sigma) x Sel_{2^n}(E_rho)`.

Passing to inverse limits gives the canonical identity

`T_2 Sel(A) = T_2 Sel(E_tau) x T_2 Sel(E_sigma) x T_2 Sel(E_rho)`.

Thus

`Phi_* T_2 Sel(A)`

is exactly the image of the product elliptic pro-Selmer system under the already source-locked pullback-sum map `Phi`.

## Adelic localization

Let `loc_B` denote the natural localization of `T_2 Sel(B)` into the product of local 2-adic Mordell--Weil completions used by 36-09DQ.  Functoriality gives

`loc_J(Phi_* s)=Phi(loc_A(s))`.

Therefore

`loc_J(T_2 Sel(J))`

is exactly

`union_{r in R} ( loc_J(r) + Phi(loc_A(T_2 Sel(A))) )`.

Substituting the product structure of `A`, this becomes

`union_{r in R} [ loc_J(r) + pi_tau^* loc(T_2 Sel(E_tau)) + pi_sigma^* loc(T_2 Sel(E_sigma)) + pi_rho^* loc(T_2 Sel(E_rho)) ]`.

This is a four-coset formula, not a product identification.

## Exact retained-open criterion

Combining the previous identity with the DQ Brauer--Manin interface gives:

`(P_v) in U_ret(A_Q)^{Br(C3_2)(2)}`

if and only if there exist

- `r in R`,
- `s_tau in T_2 Sel(E_tau)`,
- `s_sigma in T_2 Sel(E_sigma)`,
- `s_rho in T_2 Sel(E_rho)`

such that, in the adelic 2-adic completion of `J`,

`iota_hat_2((P_v)) = loc_J(r) + pi_tau^* loc(s_tau) + pi_sigma^* loc(s_sigma) + pi_rho^* loc(s_rho)`.

Equivalently the retained-open/full-2-primary problem is the union of four exact translated intersection problems

`iota_hat_2(U_ret(A_Q)) intersect [loc_J(r)+Phi(loc_A(T_2 Sel(A)))]`,

one for each class in `J(Q)/Phi A(Q)`.

## What is and is not computed

Computed exactly at this leaf:

- the number of defect cosets is 4;
- every defect coset has a rational Mordell--Weil representative;
- the Jacobian pro-Selmer adelic image is the union of those four translated elliptic-product pro-Selmer images;
- the full fixed-2-primary retained-open Brauer condition is equivalent to the resulting four-coset intersection criterion.

Not computed:

- an explicit rational representative for each of the four quotient classes;
- the three elliptic `T_2 Sel(E_h)` groups themselves;
- whether any of the four translated retained-open intersections is empty or nonempty;
- any global 2-primary Brauer-set conclusion;
- any Brauer--Manin obstruction, fixed-parameter exclusion, receiver, endpoint, or Perfect Cuboid credit.

## Next exact obligation

Materialize an exact representative set `R` for `J(Q)/Phi A(Q)` and its local translation data, or produce an equivalent explicit adapter from the four global `Phi`-Selmer squareclass labels to rational Jacobian representatives.  Only then can the four translated retained-open intersections be tested concretely.
