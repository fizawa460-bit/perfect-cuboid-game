# Stage36 36-09DS pro-Selmer torsion / injectivity correction source lock

## Purpose

This is a post-audit correction overlay. It does not rewrite the historical 36-09DS exact-head artifact. It revokes only the DS claims that `T_2 Sel(-)` is 2-torsion-free and that the induced maps `Phi_*` and `Psi_*` are injective. The V4 isogeny, degree-8 computation, the two composition identities, and the exponent-2 cokernel conclusion remain valid.

Repository policy `docs/research-os/policies/research-credit-and-promotion-firewalls.md` §10 requires later-discovered invalid credit to be reopened while unaffected historical results are retained explicitly.

## Exact pro-Selmer input from 36-09DQ

36-09DQ source-binds the generalized Cassels--Tate exact sequence and, in particular, the Kummer exact interface

`0 -> B(Q)^hat_2 -> T_2 Sel(B) -> T_2 Sha(B)[2^infinity] -> 0`

for an abelian variety `B/Q`, with `B(Q)^hat_2 = lim_n B(Q)/2^n B(Q)`.

Thus `T_2 Sel(B)` is not automatically 2-torsion-free. The 2-primary torsion of the Mordell--Weil group survives in the 2-adic completion.

For a finitely generated abelian group

`M ~= Z^r direct_sum T_2 direct_sum T_odd`,

one has

`M^hat_2 ~= Z_2^r direct_sum T_2`.

Indeed multiplication by `2^n` is an automorphism on `T_odd`, while for all sufficiently large `n` it is zero on no nonzero element of the finite 2-primary group `T_2`. Hence every nonzero rational 2-primary torsion point maps nontrivially to the 2-adic completion. Mordell--Weil finite generation supplies this decomposition for `B(Q)`.

## Stage36 rational 2-torsion kernels

36-09DT independently computes

- `ker(Phi) = (Z/2Z)^3` as a constant Q-group scheme inside `A[2]`;
- `ker(Psi) = mu_2^3`, which over Q is also a constant `(Z/2Z)^3`, inside `J[2]`.

Therefore

`ker(Phi)(Q) ~= (Z/2Z)^3 subset A(Q)[2]`

and

`ker(Psi)(Q) ~= (Z/2Z)^3 subset J(Q)[2]`.

These nonzero rational 2-torsion subgroups survive in `A(Q)^hat_2` and `J(Q)^hat_2`, hence in `T_2 Sel(A)` and `T_2 Sel(J)` by the DQ Kummer injection. Since `Phi` and `Psi` kill those rational kernel points, the induced pro-Selmer maps satisfy

`ker(Phi_*) != 0`,
`ker(Psi_*) != 0`.

Consequently the historical DS claims

- `T2Sel_2_torsion_free=true`,
- `Phi_injective=true`,
- `Psi_injective=true`,
- `proSelmer_mutual_injections_constructed=true`

are revoked.

This argument gives a definite non-injectivity statement without assuming anything about `Sha`.

## What remains valid from 36-09DS

The exact composition identities remain

`Psi_* Phi_* = [2]` on `T_2 Sel(A)`,
`Phi_* Psi_* = [2]` on `T_2 Sel(J)`.

They imply, without injectivity:

- `ker(Phi_*)` and `ker(Psi_*)` are killed by 2;
- `coker(Phi_*)` and `coker(Psi_*)` are killed by 2.

For example, if `y in T_2 Sel(J)`, then

`2y = Phi_* Psi_*(y)`

lies in `im(Phi_*)`, so `coker(Phi_*)` has exponent dividing 2. If `x in ker(Phi_*)`, then

`2x = Psi_* Phi_*(x) = 0`.

The same argument applies with `Phi` and `Psi` exchanged.

No exact kernel dimension is claimed: besides the visible Mordell--Weil kernel, additional pro-Selmer kernel may come from the Tate-module-of-Sha part. No exact cokernel dimension or cardinality is claimed either.

## Downstream impact

The correction does not invalidate the following independently checked pieces:

- 36-09DR/DS geometric V4 quotient and degree-8 isogeny;
- 36-09DT constant rational kernels;
- 36-09DU descent functions;
- 36-09DV/DW exact local Phi-Kummer images;
- 36-09DX finite global Phi-Selmer computation, including F2 dimension 2 and four classes.

It does invalidate any use of DS as a mutual-injection or product-identification bridge between `T_2 Sel(A)` and `T_2 Sel(J)`. Therefore 36-09DY must be relocked. Its corrected obligation is to determine the actual isogeny pro-Selmer kernel/cokernel defect, with rational 2-torsion included, before any retained-open pro-Selmer intersection or downstream Brauer credit can be released.

## Credit boundary

This correction proves non-injectivity of both induced pro-Selmer maps and preserves only exponent-2 kernel/cokernel control. It does not compute exact kernel/cokernel dimensions, does not identify `T_2 Sel(J)` with a product of elliptic pro-Selmer groups, and grants no 2-primary Brauer-Manin, fixed-p, receiver, endpoint, or Perfect Cuboid credit.
