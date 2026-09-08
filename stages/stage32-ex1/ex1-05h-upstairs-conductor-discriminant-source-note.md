# Stage32EX1 EX1-05H — upstairs conductor/discriminant coupling

## Scope and notation

This leaf starts from the hostile-audited EX1-00 through EX1-05F checkpoint and the unaudited EX1-05G fixed-correspondence candidate.

Write

- `S0 = (X(8) x X(8))/diag(G0plus)`, the smooth surface carrying the h=4 component;
- `q:S0 -> C2 x C2`, finite etale of degree four;
- `Gamma subset C2 x C2`, the integral correspondence image;
- `D0 subset S0`, one integral component mapping birationally to `Gamma`;
- `nu0:D -> D0`, the normalization, where this `D` is the EX1 smooth curve;
- `f1,f2:D -> C2`, of degrees 105 and 81.

This notation deliberately distinguishes the singular image `D0` from its smooth normalization `D`.

## Retained exact upstairs numerical data

The hostile-audited Stage32 Rosati repair retains, independently of the withdrawn zero-Rosati specialization,

`D0^2 = 3874`

and the three nontrivial V4 translate intersections

`D0.uD0 = 3892`, `D0.vD0 = 4020`, `D0.uvD0 = 4020`.

Hence the cross sum is `11932` and the half-cross sum is `5966`.

Because `q` is etale and `K_{C2 x C2}=p1^*K_C2+p2^*K_C2`, the fixed bidegree `(105,81)` gives

`K_S0.D0 = 2*105 + 2*81 = 372`.

Adjunction on the smooth surface `S0` therefore gives

`p_a(D0) = (D0^2 + K_S0.D0)/2 + 1 = (3874+372)/2+1 = 2124`.

For the EX1 residual state `Q=210+2r`, `0<=r<=28`, EX1-05G gives

`g(D)=106+r`.

Thus the intrinsic normalization defect of the upstairs component is

`delta_D0 = p_a(D0)-g(D) = 2018-r`.

This is not the original V6 normalization defect `472`, and it is not the full downstairs correspondence defect. In fact the retained cross sum gives the exact compatibility check

`delta_Gamma = delta_D0 + (D0.uD0+D0.vD0+D0.uvD0)/2 = (2018-r)+5966 = 7984-r`.

## Conductor/adjunction divisor identity

Since `S0` is smooth, the integral curve `D0` is Cartier and hence Gorenstein. Let `C_nu` be the effective conductor divisor on the normalization `D`. For a Gorenstein integral curve the normalization-duality relation is

`nu0^* omega_D0 ~= omega_D(C_nu)`,

and `deg C_nu = 2*delta_D0`.

Adjunction gives

`omega_D0 ~= (omega_S0 tensor O_S0(D0))|D0`.

Riemann-Hurwitz for the two smooth-curve maps gives

`omega_D ~= f1^*omega_C2 tensor O_D(R105)`
and
`omega_D ~= f2^*omega_C2 tensor O_D(R81)`.

Combining these identities with `omega_S0=q^*omega_{C2 x C2}` yields the divisor-class identities

`C_nu + R105 ~ nu0^*D0 + f2^*K_C2`,
`C_nu + R81  ~ nu0^*D0 + f1^*K_C2`.

Their degrees are

`2*delta_D0 + R105 = 4036`,
`2*delta_D0 + R81  = 4084`.

Substituting `delta_D0=2018-r`, `R105=2r`, `R81=48+2r` verifies both identities for every residual state.

Subtracting the two divisor classes gives

`R81 - R105 ~ f1^*K_C2 - f2^*K_C2`.

Since every genus-two curve is hyperelliptic and its canonical class is twice a Weierstrass point, the line bundle of `R81-R105` is 2-divisible. This is a genuine divisor-class restriction but, without the actual ramification support, it does not remove a residual state.

## Projection discriminant identity

There is also an exact base-divisor form which avoids identifying ramification with singularity defect.

For `i=1,2`, let

`pi_i:D0 -> C2`

be the singular finite projection and let `f_i=pi_i o nu0:D->C2`. At a base point `y`, put `A=O_{C2,y}`. The finite flat `A`-algebras/lattices satisfy

`B=(pi_i*O_D0)_y subset B'=(f_i*O_D)_y`

inside the same finite separable total quotient algebra.

Choose `A`-bases so that the inclusion has matrix `M`. The trace Gram matrices satisfy

`Gram(B)=M Gram(B') M^t`.

Therefore

`v_y(disc B)=v_y(disc B')+2*v_y(det M)`.

For lattices over a DVR,

`v_y(det M)=length_A(B'/B)`.

By normalization, the latter is the sum of the local delta invariants of points of `D0` above `y`. Define the effective index divisor

`A_i = sum_y length_A(B'/B) [y]`.

Then

`deg A_i = delta_D0`.

For the normalized smooth map `f_i`, the discriminant is the norm/pushforward of the different, hence its divisor is the branch divisor `Br_i=f_i*R_i`. Consequently

`Disc(pi_i) = Br_i + 2*A_i`

as effective divisors on `C2`.

Thus

- `deg Disc(pi_105)=R105+2*delta_D0=4036`;
- `deg Disc(pi_81)=R81+2*delta_D0=4084`.

Locally this says

`mult_y Disc(pi_i) = mult_y Br_i + 2*mult_y A_i`.

This is the sought member-level coupling: projection ramification and normalization singularity defect may trade only at the same base point and only through twice the normalization-index multiplicity.

## Why this does not yet prune the 29 states

The retained data determine the total degrees and the divisor-class relations, but not the actual singularity cycle of `D0`, the index divisors `A_i`, the discriminant sections, or the off-cusp branch supports. Over `C`, the existence of effective divisors of these large degrees is not restrictive by itself.

Accordingly this leaf does not identify a numerical compatibility cell with a curve, and it does not exclude any of the 29 `Q` states. It replaces the previous vague blocker by a precise missing datum:

> source-lock the singularity/index cycle of the actual `D0` member or the two projection discriminant sections/ideals strongly enough to compare their support and multiplicity with the six special cusps and the common V4 structure.

## Source references

The algebraic identities used above are standard and are replayed directly in the verifier. Stable reference points:

- Stacks Project, Tag `0C1B`, Riemann-Hurwitz: `https://stacks.math.columbia.edu/tag/0C1B`;
- Stacks Project, Tag `0C17`, quasi-finite Gorenstein different/discriminant and relative dualizing sheaf: `https://stacks.math.columbia.edu/tag/0C17`;
- Stacks Project, Tag `0BWA`, norm of the different equals the discriminant for finite Gorenstein maps: `https://stacks.math.columbia.edu/tag/0BWA`;
- Stacks Project, Tag `0C1R`, normalization quotient length equals the local delta invariant: `https://stacks.math.columbia.edu/tag/0C1R`;
- Stacks Project, Tag `0AA4`, effective-Cartier duality/adjunction input: `https://stacks.math.columbia.edu/tag/0AA4`.

The local formula `disc(B)=det(M)^2 disc(B')` is also proved explicitly above by change of basis and is not delegated to an external computation.

## Firewalls

- `D0` is not the smooth EX1 curve `D`; `D` is its normalization.
- `delta_D0=2018-r` is not the original V6 defect `472`.
- `delta_Gamma=7984-r` is not identified with either `delta_D0` or `472`.
- the fixed deck-cross half-sum `5966` is not localized to singular points without proof.
- discriminant degree is not discriminant support.
- divisor-class 2-divisibility is not promoted to existence or exclusion.
- the superseded zero-Rosati/O210 exclusion is not reused.
- the historical O210-specific `16 -> 3` transvection refinement is not imported.
- no Stage32 MAIN, Q602/O210, theorem, receiver, endpoint, or Perfect Cuboid credit follows.
