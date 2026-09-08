# EX1-05H upstairs conductor/discriminant off-cusp coupling

Status: **candidate / unaudited**.

## Exact result

Distinguish the singular upstairs image `D0` on the smooth h=4 surface from its smooth normalization `D`.

The retained fixed-V6 data give

- `D0^2=3874`;
- `K.D0=372`;
- `p_a(D0)=2124`;
- nontrivial V4 cross sum `11932`, half-sum `5966`.

For `Q=210+2r`, `0<=r<=28`, the normalization has `g(D)=106+r`, hence

`delta_D0 = 2018-r`.

The downstairs correspondence defect splits exactly as

`delta_Gamma = delta_D0 + 5966 = 7984-r`.

Thus the fixed `5966` is translate-intersection defect, not projection singularity defect.

## Divisor-level coupling

Let `C_nu` be the conductor divisor of `nu0:D->D0`, and let `R105,R81` be the ramification divisors of the two normalized projections. Adjunction plus normalization duality and Riemann-Hurwitz give

`C_nu + R105 ~ nu0^*D0 + f2^*K_C2`,

`C_nu + R81 ~ nu0^*D0 + f1^*K_C2`.

Therefore

`2*delta_D0 + deg(R105)=4036`,

`2*delta_D0 + deg(R81)=4084`.

On the base, if `A_i` is the normalization-index divisor and `Br_i=f_i*R_i`, the trace-lattice determinant identity gives

`Disc(pi_i)=Br_i+2*A_i`, `deg A_i=delta_D0`.

So ramification and singularity index can trade only at the same base point and in even increments.

## Boundary

This is a genuine member-level coupling, but it removes **0/29** Q states. The retained data do not identify the singularity/index cycle of `D0`, the two discriminant sections, or the actual off-cusp branch supports.

Next route:

`EX1-05I_UPSTAIRS_SINGULARITY_CYCLE_OR_PROJECTION_DISCRIMINANT_SUPPORT_EXTRACTION`

Required new datum: actual `D0` singularity/index cycle or projection discriminant ideals/sections, or a theorem fixing their support/multiplicity relative to the six special cusps/common V4 structure.

No full V6 exclusion, Stage32 MAIN/Q602/O210 credit, or Perfect Cuboid conclusion is claimed.
