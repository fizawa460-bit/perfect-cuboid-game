# Stage32 MB104 — W20 solo: finite E[2] Abel/conductor bridge — 2026-09-18

Status: **W20 FINITE-E[2] BRIDGE CLOSED NEGATIVELY / BRANCH-SPECIFIC CONDUCTOR ROUTE STILL OPEN / NO CREDIT**

## Scope

This checkpoint advances W20 only. W16 is intentionally untouched.

The retained W20 data are:

- `M_i=psi_i^*O(1)`, `deg M_i=28l`;
- `M_1^2 ~= M_2^2`;
- typewise ramification relations depend only on `M_i^2`;
- `delta_fac=M_1 tensor M_2^(-1) in Pic^0(E)[2]`;
- `delta_fac=O_E(D_z^+-D_w^+)` for the two sheet-selected full fibers;
- `eta in Pic^0(E)[2]` is the residual normalization class with `e=2 iff eta=0`;
- in the `e=2` branch the load-bearing conductor class is `kappa in Ker(Pic(C)[2] -> Pic(E)[2])`.

## Exact E[2] gauge symmetry

Let `tau in Pic^0(E)[2]`. Replace

`M_2` by `M_2 tensor tau`.

Because `tau^2~=O_E`, this operation preserves:

- `deg M_2`;
- `M_2^2`;
- `M_1^2~=M_2^2`;
- both typewise identities `M_1^2 O(-R_1,chi) ~= M_2^2 O(-R_2,chi)`;
- the Riemann-Hurwitz line identity;
- the retained integer branch-count and boundary-saturation equations.

But it changes

`delta_fac = M_1 tensor M_2^(-1)`

to

`delta_fac tensor tau^(-1)`.

Since `Pic^0(E)[2]` has four elements, this gauge action is simply transitive on the four possible values of `delta_fac`.

Therefore the current factor-line/passport interface cannot select one value of `delta_fac` from the four-element set.

Important scope statement: this is an information wall for the retained interface. It does **not** claim that every twist is realized by an actual cuboid factor map with the same full geometric passport.

## Why eta does not remove the gauge freedom

`eta` is a different class. It comes from the residual `G/H` Kummer cover, equivalently the ambient square class `[f_t]` restricted to the normalization.

The retained cuboid identity proves equality of the two factor residual square classes, but it does not identify the factor-pencil difference `delta_fac` with `eta`.

Thus

`delta_fac=eta`

is not a consequence of the current data.

Even imposing the `e=2` condition

`eta=0`

does not choose `delta_fac`, because the factor-line equations remain invariant under the full E[2] twist above.

## Why even delta_fac=eta would not determine the conductor cut

The Hodge obstruction in the e=2 branch depends on the singular-carrier gluing class

`kappa in Ker(Pic(C)[2] -> Pic(E)[2])`.

This is deliberately separated from the normalization class in the retained generalized-Jacobian leaf.

Both `delta_fac` and `eta` live on the smooth normalization `E`. Pullback to `E` forgets `kappa`. Hence even a future identity

`delta_fac=eta`

would only identify normalization-level two-torsion. In the e=2 case both could be zero while `kappa` remains nontrivial and still carries the weighted conductor sign cut.

Therefore a Pic^0(E)[2] bridge alone cannot evaluate or bound

`sum I_ij * alpha_abs(lambda_(p;i,j))`.

## Final W20 disposition

The finite E[2] reduction is mathematically correct and useful as a compression, but it is not a closing mechanism by itself.

The specific W20 route

`delta_fac in E[2] -> identify with eta -> control conductor cut`

is closed negatively at the present interface.

A productive continuation must leave the finite-line-bundle interface and add branch-specific data, for example:

- an explicit conductor-preimage lift to `R=C8/H`;
- actual square-root transport of `sqrt(f_t|_E)` at conductor identifications;
- a singular-carrier descent computation evaluating `kappa` before normalization.

Those are branch-specific conductor routes, not the W20 finite-E[2] bridge retained here.

## W20 solo disposition

`W20 = CLOSED_NEGATIVE_AS_FINITE_E2_BRIDGE`.

No e=2 or e=4 exclusion is proved. No weighted-cut bound, MB104 completion, finite window, receiver/effectivity/theorem/endpoint credit, Perfect-Cuboid claim, or merge authorization is granted.

Remaining user-selected solo route: `W16`.
