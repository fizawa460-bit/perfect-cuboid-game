# Stage36 36-09DY finite-isogeny / pro-Selmer defect comparison source lock

## Purpose

This leaf repairs the exact comparison that historical 36-09DS attempted to obtain from a false torsion-freeness claim.  The corrected 36-09DS authority is now externally audited and merged.  The present task is narrower: compare the exact finite `Phi`- and `Psi`-Selmer groups with the maps

`Phi_* : T_2 Sel(A) -> T_2 Sel(J)`,

`Psi_* : T_2 Sel(J) -> T_2 Sel(A)`,

where `A=E_tau x E_sigma x E_rho`, `J=Jac(C3_2)`, `Psi Phi=[2]_A`, and `Phi Psi=[2]_J`.

No product identification of the full pro-Selmer groups is assumed.

## Locked Stage36 inputs

1. 36-09DQ, `global-2primary-adelic-annihilator-proselmer-source-lock.md`, source-locks the Kummer inverse-limit exact interface

   `0 -> B(Q)^hat_2 -> T_2 Sel(B) -> T_2 Sha(B) -> 0`.

2. 36-09DT computes both rational isogeny kernels:

   `ker(Phi)(Q) ~= (Z/2Z)^3`,

   `ker(Psi)(Q) ~= (Z/2Z)^3`.

3. 36-09DW computes the exact local `Phi`- and `Psi`-Kummer image subspaces at

   `S={infinity,2,3,5,7}`.

4. 36-09DX computes

   `dim_F2 Sel^Phi(A/Q)=2`,

   hence `#Sel^Phi(A/Q)=4`, and records the fixed global squareclass localization table used below.

5. The audited 36-09DS correction proves that the visible rational 2-torsion kernels survive in the Mordell--Weil completions, so neither induced pro-Selmer map is injective.  The present leaf strengthens that statement to the exact kernels.

## External source boundary

The load-bearing external facts are standard Selmer/Kummer facts; all Stage36-specific dimensions are replayed from repository-locked finite linear algebra.

- Cristian D. Gonzalez-Aviles and Ki-Seng Tan, *A generalization of the Cassels-Tate dual exact sequence*, Math. Res. Lett. 14 (2007), 295--302, DOI 10.4310/MRL.2007.v14.n2.a11.  This is the existing 36-09DQ source for the compact/pro-Selmer exact interface.
- Nils Bruin, Bjorn Poonen, Michael Stoll, *Generalized explicit descent and its application to curves of genus 3*, Forum Math. Sigma 4 (2016), e6, DOI 10.1017/fms.2016.1.  Section 9 treats the true isogeny Selmer group through the local Kummer images and includes `J(k)/phi A(k)` in that Selmer group.  The usual cohomology sequence gives the standard finite descent exact sequence used here.
- Edward F. Schaefer, *Class Groups and Selmer Groups*, J. Number Theory 56 (1996), 79--114, DOI 10.1006/jnth.1996.0006, especially the local isogeny/Kummer comparison.  Outside the certified required set `S`, good reduction and `2 not equal residue characteristic` give local Selmer ratio 1.
- Greenberg--Wiles global duality formula, e.g. Neukirch--Schmidt--Wingberg, *Cohomology of Number Fields*, 2nd ed., Theorem 8.7.9, is used only as an independent cross-check of the directly replayed dual `Psi`-Selmer dimension.

## Direct replay of the dual Psi-Selmer group

The kernel `ker(Psi)` is also the constant group `(Z/2)^3`, so the same global unramified ambient

`Q(S,2)^3`

with 15 F2 coordinates applies.  Use the exact global localization table from 36-09DX and intersect it, place by place, with the exact `local_Psi_images` subspaces from 36-09DW.

The resulting global intersection has F2 dimension 5 and cardinality 32.  One convenient basis, in squareclass-triple notation, is

- `([1],[1],[3])`,
- `([1],[1],[2])`,
- `([1],[1],[-1])`,
- `([7],[7],[7])`,
- `([-1],[-1],[1])`.

Thus

`dim_F2 Sel^Psi(J/Q)=5`,

`#Sel^Psi(J/Q)=32`.

This is computed directly from the retained local images; it is not inferred from a parity formula.

### Independent global-ratio cross-check

Because both local kernels have eight rational points, the local Selmer-ratio exponent for `Phi` at a place is

`dim_F2 image(delta_Phi,v) - 3`.

The five 36-09DW dimensions are

`1,4,3,2,2`

at `infinity,2,3,5,7`, giving exponents

`-2,+1,0,-1,-1`

and total `-3`.  Outside `S`, 36-09DV certifies good/unramified prime-to-degree conditions, hence local ratio 1.  Therefore

`c(Phi)=2^-3=1/8`.

The Greenberg--Wiles formula for the dual isogenies gives

`c(Phi) = (#Sel^Phi/#Sel^Psi) * (#ker(Psi)(Q)/#ker(Phi)(Q))`.

The rational kernel ratio is `8/8=1`, and the direct finite groups give `4/32=1/8`, exactly matching the local product.

## Tate-Sha torsion lemma

For any abelian group `G`, set

`T_2 G = inverse_limit_n G[2^n]`

with transition multiplication by 2.  This inverse limit is 2-torsion-free.  Indeed, if `x=(x_n)` satisfies `2x=0`, then `2x_{n+1}=0` for every `n`, while compatibility says `x_n=2x_{n+1}`; hence every `x_n=0`.

Apply this to `G=Sha(B)`.  Consequently

`T_2 Sha(A)` and `T_2 Sha(J)` have no nonzero element killed by 2.

Since the maps induced by `Phi,Psi` satisfy the same compositions `[2]`,

`ker(T_2 Sha(A) -> T_2 Sha(J))=0`,

`ker(T_2 Sha(J) -> T_2 Sha(A))=0`.

This is the missing point that rules out any additional Tate-Sha contribution to the pro-Selmer kernels.

## Exact pro-Selmer kernels

Place the DQ exact sequences for `A` and `J` in a commutative diagram with vertical map induced by `Phi`.  The right vertical kernel is zero by the Tate-Sha torsion lemma.  The Snake lemma therefore identifies

`ker(Phi_* on T_2 Sel) = ker(A(Q)^hat_2 -> J(Q)^hat_2)`.

Mordell--Weil groups are finitely generated.  For a map between finitely generated abelian groups whose kernel and cokernel are 2-primary and killed by 2, 2-adic completion preserves the kernel.  Here `Psi Phi=[2]` implies the rational cokernel `J(Q)/Phi A(Q)` is killed by 2, while 36-09DT gives the rational kernel exactly.  Hence

`ker(Phi_*) = ker(Phi)(Q) ~= (Z/2Z)^3`.

The same argument with `Phi` and `Psi` exchanged gives

`ker(Psi_*) = ker(Psi)(Q) ~= (Z/2Z)^3`.

Thus both pro-Selmer kernels have exact F2 dimension 3.  This strictly strengthens the audited correction's earlier statement `kernel nonzero`, without restoring injectivity.

## Rational Mordell--Weil quotient constraints

Write

`a  = dim_F2 J(Q)/Phi A(Q)`,

`a' = dim_F2 A(Q)/Psi J(Q)`,

and let `r` be the common Mordell--Weil rank of the isogenous varieties `A` and `J`.

The standard finite isogeny descent exact sequences are

`0 -> J(Q)/Phi A(Q) -> Sel^Phi(A/Q) -> Sha(A)[Phi] -> 0`,

`0 -> A(Q)/Psi J(Q) -> Sel^Psi(J/Q) -> Sha(J)[Psi] -> 0`.

Therefore

`0 <= a <= 2`,

`0 <= a' <= 5`.

Both rational kernels have dimension 3.  For a homomorphism of finitely generated abelian groups with finite kernel and cokernel, let

`z(f)=#coker(f)/#ker(f)`.

The Snake lemma gives multiplicativity of `z`.  Since `Psi Phi=[2]` on `A(Q)`,

`z(Psi) z(Phi) = z([2] on A(Q)) = 2^r`.

But

`z(Phi)=2^(a-3)`,

`z(Psi)=2^(a'-3)`.

Hence

`r = a+a'-6`.

Because `r>=0`, `a<=2`, and `a'<=5`, the only possibilities are

- `(a,a',r)=(1,5,0)`,
- `(a,a',r)=(2,4,0)`,
- `(a,a',r)=(2,5,1)`.

In particular

`a in {1,2}`,

`a' in {4,5}`,

`r in {0,1}`.

So the Stage36 data already force the common Mordell--Weil rank to be at most one and force both rational isogeny quotients to be nonzero.

## Pro-Selmer cokernel bounds

Let `D_A` and `D_J` denote the 2-primary divisible parts of `Sha(A)` and `Sha(J)`.  The inverse-limit term `T_2 Sha` comes from these divisible parts.  The compositions `[2]` and divisibility imply that

`Phi : D_A -> D_J`,

`Psi : D_J -> D_A`

are surjective.  Their kernels are contained respectively in `Sha(A)[Phi]` and `Sha(J)[Psi]`.

Applying the Snake lemma to the two DQ exact rows shows that `coker(Phi_*)` is an extension of the completed Mordell--Weil quotient by the Tate-Sha cokernel.  Equivalently, if

`d = dim_F2(D_A[Phi])`,

then

`dim_F2 coker(Phi_*) = a+d`,

with

`0 <= d <= dim_F2 Sha(A)[Phi] = 2-a`.

Therefore

`1 <= dim_F2 coker(Phi_*) <= 2`,

so

`#coker(Phi_*) in {2,4}`.

Similarly, writing `d'=dim_F2(D_J[Psi])`,

`dim_F2 coker(Psi_*) = a'+d'`,

`0 <= d' <= 5-a'`,

and hence

`4 <= dim_F2 coker(Psi_*) <= 5`,

so

`#coker(Psi_*) in {16,32}`.

The composition identities independently show that all these cokernels are killed by 2, so the dimension language is legitimate.

This leaf does **not** choose between the remaining alternatives.  In particular it does not assert `#coker(Phi_*)=4` merely because `#Sel^Phi=4`.

## Next exact obligation

The one-bit Phi defect is now isolated.  To decide whether

`dim coker(Phi_*)=1` or `2`,

one must determine the actual rational quotient `J(Q)/Phi A(Q)` and, only if its dimension is 1, determine whether the remaining `Sha(A)[Phi]` class lies in the divisible subgroup.  A direct Mordell--Weil quotient computation is therefore the next efficient leaf; a dual Cassels--Tate/divisible-Sha computation is needed only in the residual `a=1` case.

## Credit boundary

36-09DY proves:

- `Sel^Psi(J/Q)` has F2 dimension 5 and cardinality 32;
- both induced pro-Selmer kernels have exact F2 dimension 3;
- common Mordell--Weil rank is 0 or 1;
- `dim coker(Phi_*)` is 1 or 2;
- `dim coker(Psi_*)` is 4 or 5.

It does not compute either pro-Selmer cokernel exactly, does not identify `T_2 Sel(J)` with the product elliptic pro-Selmer group, does not compute the retained-open curve/pro-Selmer intersection, and grants no global 2-primary Brauer, Brauer--Manin, fixed-p, receiver, endpoint, or Perfect Cuboid credit.
