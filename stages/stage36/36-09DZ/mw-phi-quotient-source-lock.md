# Stage36 36-09DZ Mordell--Weil / Phi-quotient source lock

## Purpose

36-09DY reduced the remaining fixed-`p=2` isogeny/pro-Selmer ambiguity to the exact rational quotient

`J(Q)/Phi A(Q)`

for

`A=E_tau x E_sigma x E_rho`,
`J=Jac(C3_2)`.

It proved that, writing

`a = dim_F2 J(Q)/Phi A(Q)`,
`a' = dim_F2 A(Q)/Psi J(Q)`,
`r = rank A(Q) = rank J(Q)`,

the only possibilities are

- `(a,a',r)=(1,5,0)`,
- `(a,a',r)=(2,4,0)`,
- `(a,a',r)=(2,5,1)`.

Thus a single explicit non-torsion point on one elliptic quotient forces the third case and closes the remaining one-bit defect.

## Locked Stage36 inputs

1. 36-09DR constructs the Q-defined V4 quotient decomposition and the elliptic quotient

   `E_tau : y^2=(x+4)(x+1/4)(x+9)(x+1/9)`.

2. 36-09DY proves

   `rank A(Q)=rank J(Q) <= 1`,

   `dim Sel^Phi(A/Q)=2`,

   `dim Sel^Psi(J/Q)=5`,

   and the three allowed `(a,a',r)` triples listed above.

3. 36-09DY also proves that the pro-Selmer cokernel dimensions are obtained from the rational Mordell--Weil quotient dimensions plus only the corresponding divisible-Sha isogeny kernel contribution.

## Explicit birational model for E_tau

Let

`C_tau : y^2=(x+4)(x+1/4)(x+9)(x+1/9)`.

Set

`U = -7(x+4)/(4x+1)`,

`V = 126 y/(4x+1)^2`.

A direct rational-function identity gives

`V^2 = U(U+1)(U+49)`.

Thus `C_tau` is birational over Q to the full-rational-2-torsion Weierstrass model

`E_tau^W : V^2 = U(U+1)(U+49)`.

The inverse map on the common affine domain is

`x = -(U+28)/(4U+7)`,

`y = 175 V / (2(4U+7)^2)`.

The verifier checks both substitutions symbolically over Q.  Since both curves are smooth genus-one curves, this birational equivalence identifies their smooth projective models over Q.

## Explicit rational point

The quartic has the exact rational point

`Q_tau = (-29/11, 875/121)`.

The displayed map sends it to

`P = (1,10) in E_tau^W(Q)`.

Indeed

`10^2 = 1*(1+1)*(1+49)=100`.

No bounded search is used as credit here: the listed point is an exact algebraic witness and is replayed directly by the verifier.

## Non-torsion certification

The Weierstrass model has full rational 2-torsion:

`(0,0)`, `(-1,0)`, `(-49,0)`.

Mazur's rational torsion theorem implies that an elliptic curve over Q with full rational 2-torsion has torsion subgroup of the form

`Z/2Z x Z/2nZ`, `1 <= n <= 4`.

Hence every rational torsion point has order dividing 8.

Source: Barry Mazur, *Modular curves and the Eisenstein ideal*, Publications Mathématiques de l'IHÉS 47 (1977), 33--186; equivalently any standard statement of Mazur's classification of rational torsion on elliptic curves over Q.

The verifier performs exact rational group law on

`V^2 = U^3 + 50 U^2 + 49 U`

and checks

`8P != O`.

Therefore `P` is not torsion and

`rank E_tau^W(Q) >= 1`.

Since `E_tau^W` is the elliptic quotient model above,

`rank E_tau(Q) >= 1`.

Hence

`rank A(Q) >= 1`.

Together with the DY upper bound `rank A(Q) <= 1`, this proves

`rank A(Q)=rank J(Q)=1`.

## Exact rational isogeny quotients

The DY triple list now collapses to the unique possibility

`(a,a',r)=(2,5,1)`.

Therefore

`dim_F2 J(Q)/Phi A(Q)=2`,

`dim_F2 A(Q)/Psi J(Q)=5`.

The finite isogeny descent exact sequences are

`0 -> J(Q)/Phi A(Q) -> Sel^Phi(A/Q) -> Sha(A)[Phi] -> 0`,

`0 -> A(Q)/Psi J(Q) -> Sel^Psi(J/Q) -> Sha(J)[Psi] -> 0`.

But DY gives

`dim Sel^Phi=2`,

`dim Sel^Psi=5`.

Consequently

`Sha(A)[Phi]=0`,

`Sha(J)[Psi]=0`.

In particular the divisible 2-primary Sha parts have no residual Phi/Psi kernel contribution.

## Exact pro-Selmer defect

Using the DY Snake-lemma comparison between Mordell--Weil completion, pro-Selmer, and `T_2 Sha`, the vanishing finite Sha kernels above forces

`dim_F2 coker(Phi_* : T_2 Sel(A) -> T_2 Sel(J)) = 2`,

`#coker(Phi_*)=4`,

and

`dim_F2 coker(Psi_* : T_2 Sel(J) -> T_2 Sel(A)) = 5`,

`#coker(Psi_*)=32`.

The exact kernels remain

`ker(Phi_*) ~= (Z/2Z)^3`,

`ker(Psi_*) ~= (Z/2Z)^3`.

Thus the 2-primary isogeny defect is now exact at both kernel and cokernel level.

## What this does not prove

The isogeny maps are still not isomorphisms of pro-Selmer groups.  This leaf does not identify

`T_2 Sel(J)`

with the direct product of the three elliptic quotient pro-Selmer groups.  It does not compute the retained-open Abel--Jacobi/pro-Selmer intersection and grants no global 2-primary Brauer-set, Brauer--Manin, fixed-parameter, receiver, endpoint, or Perfect Cuboid credit.

## Next exact obligation

The finite-to-pro-Selmer defect is no longer the blocker.  The next leaf should use the now-exact defect data to formulate a defect-aware retained-open Abel--Jacobi intersection test, rather than silently replacing `T_2 Sel(J)` by the elliptic product.
