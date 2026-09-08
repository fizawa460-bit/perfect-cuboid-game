# Stage36 36-09DW Phi-Selmer five-place local-image source lock

## Exact-green inputs

36-09DT fixes the dual degree-eight isogenies

`Phi:A=E_tau x E_sigma x E_rho -> J=Jac(C3_2)` and `Psi:J->A`,

with `Psi Phi=[2]_A`, `Phi Psi=[2]_J`, constant `ker(Phi)=(Z/2)^3`, split dual `ker(Psi)=mu_2^3`, and explicit kernel bases.

36-09DU fixes the `Phi` connecting coordinates `F1,F2,F3`.
36-09DV fixes the conservative required-place set `S={infinity,2,3,5,7}`.

## Dual-isogeny local orthogonality

For a local field `K` and dual isogenies `Phi` and `Psi`, Tate local duality for the Cartier-dual kernels identifies the two local connecting images as exact orthogonal complements under the local Tate pairing

`H^1(K,ker(Phi)) x H^1(K,ker(Psi)) -> Br(K)[2]`.

This is the finite-kernel form of Tate local duality obtained from the two isogeny exact sequences. We use only the orthogonal-complement statement for the actual local Kummer images. A modern source is J. S. Milne, *Arithmetic Duality*, section on local duality and the commutative diagram attached to an isogeny and its dual.

Under the rational bases fixed by DT/DU, both cohomology groups are represented by triples of local squareclasses and the pairing is coordinatewise Hilbert symbol.

## Factorwise [2]-Kummer completeness

For each elliptic quotient `E_h`, DT supplies two independent rational 2-torsion classes `alpha_h,beta_h`; hence `E_h[2](Q_v)=(Z/2)^2` at every place used here.

For a nonarchimedean local field, `E_h(Q_v)` is a one-dimensional compact p-adic Lie group. The local multiplication-by-two quotient therefore has

- F2-dimension `2` for odd residue characteristic;
- F2-dimension `3` over `Q_2`.

Equivalently the local isogeny Euler characteristic for `[2]` gives `#coker[2]=#ker[2]*|2|_v^{-1}`. At the real place, doubling is surjective on the identity component and `E(R)/2E(R)` has F2-dimension at most one; the explicit nonzero witness used by the verifier makes the dimension exactly one for each factor.

Therefore a bounded list of explicit local points is enough for an exact factorwise Kummer image once its span reaches these theoretical dimensions. The verifier independently reconstructs such spanning witnesses; no sampling/exhaustiveness credit is used beyond saturation of the theorem-supplied upper bound.

## Exact factor Kummer functions

With the quotient equations fixed in 36-09DR, use the following `[2]`-Kummer coordinate functions associated to the DT basis:

`E_tau`:

- `a_tau=(x+4)(x+1/4)`;
- `b_tau=(x+4)(x+9)`.

`E_sigma`:

- `a_sigma=u^2+9/4`;
- `b_sigma=2*(Y+u^2-4)`.

`E_rho`:

- `a_rho=v^2+25/4`;
- `b_rho=2*(Y+v^2-25/3)`.

The last two formulas are the same Hilbert-90 descent identity used already in DU: if `g=(X-ia)(X-ib)=A-iB` and `Y^2=A^2+B^2`, then `(Y+g)^2=2(Y+A)g`.

## Psi connecting coordinates

The DT kernel generators are

`k1=(alpha_tau,alpha_sigma,0)`,
`k2=(alpha_tau,0,alpha_rho)`,
`k3=(beta_tau,beta_sigma,beta_rho)`.

Therefore the dual-isogeny connecting map is obtained from the factor `[2]`-Kummer coordinates by

`G1=a_tau*a_sigma`,
`G2=a_tau*a_rho`,
`G3=b_tau*b_sigma*b_rho`.

This is the character restriction map dual to the inclusion `ker(Phi) subset A[2]`.

## Squareclass bit conventions

- `R*/R*^2`: one sign bit.
- odd `Q_p`: `[v_p mod 2, nonsquare-unit bit]`.
- `Q_2`: `[v_2 mod 2, -1 bit, 5 bit]`.

The coordinatewise Hilbert matrices in these bases are

- `R`: `[[1]]`;
- odd `p`: `[[((p-1)/2 mod 2),1],[1,0]]`;
- `Q_2`: `[[0,0,1],[0,1,0],[1,0,0]]`.

## Credit boundary

36-09DW may certify only the five exact local images `L_v=image(delta_Phi,v)` at `infinity,2,3,5,7` and their explicit F2 bases. It does not yet compute the global Phi-Selmer intersection, pro-Selmer cokernel size, `T_2 Sel(J)`, retained-open intersection, Brauer-Manin obstruction, fixed-p exclusion, receiver closure, or endpoint closure.
