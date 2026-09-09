# Stage36 36-09DW dual-basis pairing correction source lock

## Status and scope

This is a post-audit correction overlay. It does not rewrite the historical 36-09DW or 36-09DX artifacts. It corrects one load-bearing coordinate assumption in the historical local-duality step and replays the affected finite linear algebra.

The defect is not in Tate local duality itself. The defect is that the historical DW source treated the chosen `ker(Phi)` and `ker(Psi)` bases as mutually Cartier-dual, so it used a coordinatewise Hilbert pairing. The two chosen bases are not mutually dual.

## Retained geometric data

Write

`K=ker(Phi)` and `K^D=ker(Psi)`.

36-09DT fixes the basis of `K`:

- `k1=(alpha_tau,alpha_sigma,0)`,
- `k2=(alpha_tau,0,alpha_rho)`,
- `k3=(beta_tau,beta_sigma,beta_rho)`.

36-09DU fixes the basis of `K^D`:

- `lambda1=[1,2,3,4]`,
- `lambda2=[1,2,5,6]`,
- `lambda3=[1,4,5,8]`.

Using the pullback identifications already fixed by DT,

- `lambda1=Phi(alpha_tau,0,0)`,
- `lambda2=Phi(beta_tau,0,0)`,
- `lambda3=Phi(0,beta_sigma,0)`.

For each elliptic factor, `alpha_h,beta_h` are independent nonzero rational 2-torsion points. Hence their Weil pairing is the unique nontrivial value in `mu_2`, while equal vectors pair trivially.

The Cartier pairing between `K` and `K^D` is therefore represented, in the displayed bases, by the F2 matrix

`C = [[0,1,1],[0,1,0],[1,0,0]]`,

where `C_ij=1` means `<k_i,lambda_j>=-1`.

This matrix is invertible but is not the identity. Its inverse is

`C^{-1}=[[0,0,1],[0,1,0],[1,1,0]]`.

## Coordinate consequence

DU's functions `F1,F2,F3` evaluate the three characters `lambda_j` on a `K`-valued Kummer cocycle. Thus if `u` denotes cocycle coordinates in the `k_i` basis and `x` denotes the DU function-evaluation coordinates, then

`x=C^T u`.

DW's functions `G1,G2,G3` evaluate the three characters `k_i` on a `K^D`-valued Kummer cocycle. Thus if `v` denotes cocycle coordinates in the `lambda_j` basis and `y` denotes the DW `G` coordinates, then

`y=C v`.

The natural local cup/Tate pairing is `u^T C v`, with each scalar product replaced by the local Hilbert pairing. Substituting the evaluation coordinates gives

`x^T C^{-1} y`.

Therefore, in the actual DU/DW squareclass coordinates, the local pairing matrix is not coordinatewise identity. At a place whose squareclass Hilbert matrix is `H_v`, the correct block matrix is

`C^{-1} tensor H_v`.

The historical DW orthogonal-complement step used `I_3 tensor H_v`; that is the defect corrected here.

## Corrected local Phi images

Keep the historical exact `Psi` local images; those were computed directly from the factor `[2]`-Kummer data before the incorrect orthogonal-complement step.

Taking orthogonal complements with `C^{-1} tensor H_v` gives the corrected `Phi` local images in the existing DU coordinate order.

At `infinity`, dimension 1, basis:

`[0,0,1]`.

At `Q_2`, dimension 4, basis:

- `[0,0,0,0,0,1,0,0,0]`,
- `[0,0,0,1,0,0,1,0,0]`,
- `[0,0,0,0,0,0,0,1,0]`,
- `[0,0,0,0,0,0,0,0,1]`.

At `Q_3`, dimension 3, basis:

- `[0,0,0,1,0,0]`,
- `[0,0,0,0,1,0]`,
- `[0,0,0,0,0,1]`.

At `Q_5`, dimension 2, basis:

- `[0,0,0,1,0,0]`,
- `[0,1,0,0,0,1]`.

At `Q_7`, dimension 2, basis:

- `[0,1,0,1,0,0]`,
- `[0,0,0,0,0,1]`.

The local dimensions remain `1,4,3,2,2`, so the global Selmer-ratio exponent remains `-3`.

## Direct rational witness exposing the historical error

Let

`P0=(0,1)` and `P+=(1,25/3)` on `C3_2`.

For the degree-zero divisor `D+=P+-P0`, direct DU function evaluation gives

- `F1(D+)` squareclass `[1]`,
- `F2(D+)` squareclass `[2]`,
- `F3(D+)` squareclass `[6]`.

Hence

`delta_Phi([P+-P0])=([1],[2],[6])`.

This is a global rational Jacobian point, so its localization must lie in every correct local Phi image. It does lie in the corrected images above. It does not lie in the historical DW image at `Q_2`, which forced the historical third coordinate to vanish there. This gives an independent exact witness of the basis-pairing defect.

Similarly, for `P-=(1,-25/3)`,

`delta_Phi([P--P0])=([1],[2],[-6])`.

## Corrected global Phi-Selmer group

Replay the 15-dimensional `Q(S,2)^3` global ambient and the same localization table from DX, but intersect with the corrected local Phi images above.

The combined constraint rank is still 13. Therefore

`dim_F2 Sel^Phi(A/Q)=2`,

`#Sel^Phi(A/Q)=4`.

A convenient basis is

- `([1],[1],[-1])`,
- `([1],[2],[6])`.

The four classes are

- `([1],[1],[1])`,
- `([1],[1],[-1])`,
- `([1],[2],[6])`,
- `([1],[2],[-6])`.

Thus the historical DX numerical dimension/cardinality survive, but the historical basis `([-1],[-1],[1]),([6],[3],[1])` and the claim that the third coordinate is trivial on the whole group are revoked.

## Downstream impact

The following survive because they depend only on dimensions/cardinalities or on independent later witnesses:

- `dim Sel^Phi=2`, `#Sel^Phi=4`;
- direct `Sel^Psi` dimension 5/cardinality 32;
- global Selmer ratio `4/32=1/8`;
- DY exact pro-Selmer kernel dimensions;
- DY rank upper bound `rank<=1`;
- DZ explicit non-torsion witness and hence exact common rank 1;
- DZ quotient dimensions `(a,a')=(2,5)`;
- `Sha(A)[Phi]=0`, `Sha(J)[Psi]=0`;
- exact pro-Selmer kernel/cokernel dimensions Phi `3/2`, Psi `3/5`;
- EA four-coset cardinality/reduction.

The following historical claims are revoked or reopened:

- historical DW explicit Phi local-image bases;
- historical DX squareclass basis and all four listed labels;
- historical DX `third_coordinate_trivial_on_entire_group=true`;
- any downstream statement that used those specific labels or the false coordinatewise dual-basis assumption.

36-09EB is relocked until this correction is externally hostile re-audited and consumed by a separate promotion transition.

## Firewalls

This correction does not itself decide the retained-open intersections, global 2-primary Brauer set, Brauer--Manin obstruction, fixed-p exclusion, receiver closure, endpoint closure, or Perfect Cuboid nonexistence.
