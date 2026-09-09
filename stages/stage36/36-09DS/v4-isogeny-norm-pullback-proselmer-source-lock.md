# Stage36 36-09DS V4 isogeny norm/pullback and pro-Selmer transport source lock

## Scope

This leaf starts from the exact-green 36-09DR decomposition of

`J = Jac(C3_2)`

through the three degree-two quotient maps

`pi_tau : C3_2 -> C3_2/<tau>`,
`pi_sigma : C3_2 -> C3_2/<sigma>`,
`pi_rho : C3_2 -> C3_2/<rho>`,

whose quotient Jacobians are denoted `E_tau`, `E_sigma`, and `E_rho`.
Set

`A = E_tau x E_sigma x E_rho`.

No identification of `T_2 Sel(J)` with `T_2 Sel(A)` is assumed.

## Structural sources

1. E. Kani and M. Rosen, *Idempotent relations and factors of Jacobians*,
   Mathematische Annalen 284 (1989), 307--328.

   For the Klein four action, the idempotent relation gives the 36-09DR
   isogeny decomposition. Because the total quotient `C3_2/V4` has genus
   zero, its Jacobian is zero.

2. J. S. Milne, *Jacobian Varieties*, in *Arithmetic Geometry* (1986),
   especially the Albanese/autoduality discussion.

   We use the canonical principal polarizations to identify the dual of
   pullback on Jacobians with norm/pushforward.

3. Stacks Project, Section 31.18 (Norms), in particular the degree property
   of the norm for finite morphisms.

The identities below are also replayed from the explicit V4 group algebra
and therefore do not depend on a black-box numerical Jacobian computation.

## Norm/pullback identities

For each involution `h in {tau,sigma,rho}`, write `pi_h^*` for pullback and
`pi_{h,*}` for norm/pushforward on Jacobians. Since `deg(pi_h)=2`,

`pi_{h,*} pi_h^* = [2]`

on `E_h`, and

`pi_h^* pi_{h,*} = 1+h`

on `J`.

For distinct `h,k`, the correspondence `pi_{h,*} pi_k^*` factors through
the common quotient by `<h,k>=V4`. Since `Jac(C3_2/V4)=0` by 36-09DR,

`pi_{h,*} pi_k^* = 0`.

Define

`Phi : A -> J`,
`Phi(a_tau,a_sigma,a_rho) = pi_tau^* a_tau + pi_sigma^* a_sigma + pi_rho^* a_rho`,

and

`Psi : J -> A`,
`Psi(x) = (pi_{tau,*}x, pi_{sigma,*}x, pi_{rho,*}x)`.

The diagonal/off-diagonal identities give

`Psi Phi = [2]_A`.

On `J`,

`Phi Psi = (1+tau)+(1+sigma)+(1+rho)`.

The V4 norm `1+tau+sigma+rho` factors through the genus-zero total quotient,
so it acts as zero on `J`; hence

`Phi Psi = [2]_J`.

Under the canonical principal polarizations, `Psi = Phi^vee`. Therefore

`deg(Phi)=deg(Psi)`,

while

`deg(Psi Phi)=deg([2]_A)=2^(2 dim A)=2^6=64`.

Consequently

`deg(Phi)=deg(Psi)=8`.

Moreover `ker(Phi) subset A[2]` and `ker(Psi) subset J[2]`; each geometric
kernel has order 8. This leaf does not identify the rational Galois-module
structure of either kernel.

## Pro-Selmer transport

Let `T_2 Sel(-)` mean the inverse limit of the `2^n`-Selmer groups under
multiplication by 2, as already used by 36-09DQ. Functoriality of Kummer
maps and Selmer local conditions gives induced homomorphisms

`Phi_* : T_2 Sel(A) -> T_2 Sel(J)`,
`Psi_* : T_2 Sel(J) -> T_2 Sel(A)`

with the same compositions `[2]`.

The inverse-limit module `T_2 Sel(B)` is 2-torsion-free for any abelian
variety `B`: if `2x=0`, then compatibility `x_n=2x_{n+1}` forces every
coordinate `x_n` to vanish. Therefore both `Phi_*` and `Psi_*` are
injective.

The composition identities also show that both cokernels are killed by 2:
for example `2y=Phi_*Psi_*(y)` for every `y in T_2 Sel(J)`.

This is the exact DS credit ceiling. It does **not** compute the cokernel
dimension or cardinality, does not identify either geometric kernel as a
constant `(Z/2)^3`, and does not prove

`T_2 Sel(J) = T_2 Sel(E_tau) x T_2 Sel(E_sigma) x T_2 Sel(E_rho)`.

The next obligation is the explicit 2-isogeny/pro-Selmer defect needed to
turn elliptic quotient descent data into an exact retained-open intersection
test.
