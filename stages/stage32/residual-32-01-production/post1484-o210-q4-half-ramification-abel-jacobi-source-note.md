# Stage32 post-1484 O210 q'=4 half-ramification Abel--Jacobi source note

Scope: fixed recovered V6 class only, target `g1-d186`, `d=186`, `e=266`, `z=(-15,62,-44,26,32)`, at `O=210`, `q'=4`. This note refines the degree-24 half-ramification Picard identity on the genus-one normalization `N`. It does not construct or exclude a carrier.

## Locked prior result

The preceding exact reduction gives an effective degree-24 divisor

`E = sum k_P P + sum(r_Q-1)Q + sum(e_S-1)S`

on `N`, with

`O_N(E) ~= z^*O_P1(1) tensor w^*O_P1(-1)`.

Here `z,w:N->P1=X(4)` have degrees `105,81`. The support coefficients are not arbitrary: they are exactly the exceptional-endpoint excess, second strict-boundary tangency, and off-cusp ramification units from the 24-unit local decomposition.

## Ramification divisors of z and w

Let `R_z` and `R_w` be the ramification divisors of `z` and `w` on the genus-one curve `N`.

Riemann--Hurwitz gives

`K_N ~= z^*K_P1 tensor O_N(R_z)`

and

`K_N ~= w^*K_P1 tensor O_N(R_w)`.

Since `K_N` is trivial and `K_P1=O_P1(-2)`, this is

`O_N(R_z) ~= z^*O_P1(2)`,

`O_N(R_w) ~= w^*O_P1(2)`.

The degree checks are

`deg(R_z)=2*105=210`,

`deg(R_w)=2*81=162`.

For the first factor, the retained six-cusp certificate gives more: `R_z` is supported only over the six modular cusp values, all ramification is simple, and its 210 points consist of 182 first-factor strict-boundary ramification points plus 28 exceptional `m=2` contacts. This must not be confused with the 210 odd `m=1` contacts that branch the separate quadratic cover `pi:Y->N`.

## Exact divisor-class identity

Square the preceding half-ramification Picard identity:

`O_N(2E) ~= z^*O_P1(2) tensor w^*O_P1(-2)`.

Using the two Riemann--Hurwitz identities,

`O_N(2E) ~= O_N(R_z-R_w)`.

Therefore

`2E ~ R_z-R_w`,

or equivalently the origin-free Picard condition

`[2E-R_z+R_w]=0 in Pic^0(N)`.

The degree check is

`2*24-210+162=0`.

If an origin on the genus-one curve is chosen, the same statement is the Abel--Jacobi/group-law condition that the weighted point sum of the degree-zero divisor `2E-R_z+R_w` is zero.

Equivalently, for fiber divisors `Z_inf=z^*(inf)` and `W_inf=w^*(inf)`, the differential identities

`div(dz)=R_z-2Z_inf`,

`div(dw)=R_w-2W_inf`

show that `R_z-R_w-2E` is principal, consistently with `E~Z_inf-W_inf`.

## What this does and does not solve

This identifies the correct remaining object: a support-constrained Abel--Jacobi realization problem on `N`, not a surface Picard support-count problem.

The older Stage32 integral Picard support preflights solve a different problem. They work in the 64-dimensional resolved-surface Picard lattice and ask which exceptional curves have positive surface intersection with a candidate surface class `C`. Those pairings do not provide the divisor classes or Abel--Jacobi coordinates of normalization points appearing in `E`, `R_z`, or `R_w`. Reusing that preflight as a certificate for this leaf would therefore be invalid.

Likewise, the old degree-93/93 commensurator obstruction required both descended projections to be etale; it is not applicable when the second degree-81 map has ramification 48.

The identity `[2E-R_z+R_w]=0` itself is a consequence of the already fixed line-bundle class and therefore is not a new standalone exclusion. To advance, one needs either:

1. source-locked Picard/Abel--Jacobi data for the allowed normalization support points, sufficient to test the weighted support condition; or
2. a valid simultaneous `105/81` correspondence theorem that imposes an equivalent stronger restriction without requiring those point coordinates.

No such one-sided-ramified correspondence theorem is presently retained in the Stage32 assets checked for this leaf.

## Firewalls

- `O=210` is not excluded here.
- The 210 branch points of `pi:Y->N` are not identified with `R_z`.
- Surface Picard pairings are not normalization-point Abel--Jacobi coordinates.
- O186/O188, old 93/93, first-Hurwitz-only, scalar-T-only, and abstract degree-24 effectivity routes remain closed.
- No FULL178, receiver, route, theorem, endpoint, or perfect-cuboid credit follows.
- Promotion requires bounded hostile audit.

The next exact leaf is

`O210_Q4_SUPPORT_CONSTRAINED_ABEL_JACOBI_REALIZATION_OF_HALF_RAMIFICATION_DIVISOR`.
