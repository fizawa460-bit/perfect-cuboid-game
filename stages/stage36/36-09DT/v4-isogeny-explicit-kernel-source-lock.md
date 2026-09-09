# Stage36 36-09DT explicit V4-isogeny kernel source lock

## Fixed Stage36 objects

36-09DS fixes

- `C3_2: z^2=(t^2+4)(t^2+1/4)(t^2+9)(t^2+1/9)`,
- `J=Jac(C3_2)`,
- `A=E_tau x E_sigma x E_rho`,
- `Phi(a_tau,a_sigma,a_rho)=pi_tau^*(a_tau)+pi_sigma^*(a_sigma)+pi_rho^*(a_rho)`,
- `Psi=Phi^vee`,
- `deg(Phi)=deg(Psi)=8`, with both kernels killed by 2.

The present leaf does not change these maps.

## Hyperelliptic 2-torsion model

For a squarefree even-degree hyperelliptic model `y^2=f(t)` with eight finite ramification points, the geometric Jacobian 2-torsion is represented by even subsets of the eight ramification points, modulo replacing a subset by its complement; addition is symmetric difference. The Galois action is the natural permutation action on ramification points. This is the standard ramification-point description used in explicit 2-descent; see B. Poonen and E. F. Schaefer, *Explicit descent for Jacobians of cyclic covers of the projective line*, J. Reine Angew. Math. 488 (1997), especially the ramification-point description of torsion, and the standard hyperelliptic specialization.

For the fixed curve, label the eight roots

`1=2i, 2=-2i, 3=i/2, 4=-i/2, 5=3i, 6=-3i, 7=i/3, 8=-i/3`.

The three involutions have orbit partitions

- `tau:t->-t`: `{1,2},{3,4},{5,6},{7,8}`,
- `sigma:t->1/t`: `{1,4},{2,3},{5,8},{6,7}`,
- `rho:t->-1/t`: `{1,3},{2,4},{5,7},{6,8}`.

For a quotient `pi_h:C3_2->E_h`, a quotient 2-torsion class represented by a pair of quotient branch points pulls back to the union of the corresponding two `h`-orbits. 36-09DT verifies every subset below directly from these orbit partitions; no classification table is imported.

## Galois action

All eight roots lie in `Q(i)`. Complex conjugation acts by

`c=(1 2)(3 4)(5 6)(7 8)`.

A subset class is Q-rational exactly when its conjugate equals the subset or its complement in the even-subset model. The verifier checks this criterion for each selected generator.

## Dual-isogeny kernel

For an isogeny `f:A->B`, the kernel of the dual isogeny `f^vee:B^vee->A^vee` is the Cartier dual of `ker(f)`; this is the standard Weil-Cartier duality for finite isogeny kernels (classically Mumford, *Abelian Varieties*, III §15, Thm. 1). Therefore the already source-bound identity `Psi=Phi^vee` allows the `ker(Psi)` statement only after `ker(Phi)` has been computed. Over Q, `mu_2` is split, so the Cartier dual of a constant `(Z/2Z)^3` is again a split order-eight group scheme.

## Credit boundary

This source lock supports only the explicit geometric/Galois kernel calculation for the fixed degree-8 isogeny and its dual-kernel consequence. It does not compute the global or local `Phi`-Selmer conditions, the pro-Selmer cokernel cardinality, `T_2 Sel(J)`, the retained-open Abel-Jacobi intersection, a Brauer-Manin obstruction, or any receiver/endpoint claim.
