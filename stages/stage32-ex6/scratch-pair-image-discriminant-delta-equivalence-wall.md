# Stage32EX6 — pair-image discriminant versus normalization-defect wall

Status: `SCRATCH_EXACT_BOUNDED_DISCRIMINANT_DELTA_EQUIVALENCE_NO_ENDPOINT_CREDIT`.

This is the third isolated micro-diagnostic on branch `scratch/stage32-ex6-simultaneous-critical-support`, continuing PR #1715 exact retained head `e722b1774134486e2d1eb34ca5f2284d9f5d27d8`. It is not MAIN authority, not a retained consolidation, and does not update `MAIN-STATE.json`.

## Scope

Assume the same hypothetical integral irreducible geometric-genus-one V6 carrier at `O=266` used throughout EX6.

The retained factor-pair geometry gives a birational pair-image

`B subset P1_x x P1_y`

of bidegree

`(a,b)=(81,105)`

with normalization `N` of genus one. The retained intermediate-quotient source note gives

`p_a(B)=(81-1)(105-1)=8320`,

hence

`delta(B)=p_a(B)-g(N)=8319`.

The two normalization projections have degrees `105` and `81`.

The bounded question is whether the two scalar critical-value discriminants of the pair-image supply a genuinely new coupling beyond the retained Riemann--Hurwitz and delta/conductor data.

## Global discriminant degrees

Write a bihomogeneous defining equation for `B` as `F(x,y)=0`, of degree `a=81` in the first factor and degree `b=105` in the second factor.

For the degree-`b` projection to the first `P1`, the discriminant of `F` in the second variable is a section of degree

`deg Disc_y(F) = 2*a*(b-1)`.

Numerically,

`deg Disc_y(F) = 2*81*104 = 16848`.

The normalization map `N -> P1_x` has degree `b=105` and `g(N)=1`, so Riemann--Hurwitz gives the actual normalization ramification divisor degree

`deg R_x = 2*g(N)-2 + 2*b = 210`.

Therefore

`deg Disc_y(F) - deg R_x`
`= 16848-210`
`= 16638`
`= 2*8319`
`= 2*delta(B)`.

For the opposite projection, the discriminant in the first variable has degree

`deg Disc_x(F) = 2*b*(a-1)`
`              = 2*105*80`
`              = 16800`.

The normalization projection has degree `a=81`, hence

`deg R_y = 2*g(N)-2 + 2*a = 162`.

Again,

`deg Disc_x(F) - deg R_y`
`= 16800-162`
`= 16638`
`= 2*delta(B)`.

Thus both directions satisfy the exact identity

`PAIR_IMAGE_DISCRIMINANT_EXCESS = 2*delta(B) = 16638`.

More generally for an integral bidegree `(a,b)` pair-image with normalization genus `g`,

`deg Disc_y - deg R_x`
`= 2*a*(b-1) - (2*g-2+2*b)`
`= 2*((a-1)*(b-1)-g)`
`= 2*delta(B)`,

and symmetrically for the other projection.

This is the global normalization/conductor correction. Stacks Project Section 33.41 (Tag `0C44`) records that the local normalization quotient has length equal to the delta invariant; the retained Stage32 source note already fixes the global `delta(B)=8319` value for this exact V6 pair-image.

## Why scalar discriminants do not measure common criticality

A discriminant of the singular pair-image contains singularity factors that need not be normalization ramification.

Two local models make the firewall explicit.

### Immersed node

Take

`F=y^2-x^2=(y-x)(y+x)`.

The two normalization branches are

`(x,y)=(t,t)` and `(t,-t)`.

Projection to `x` is unramified on both branches. Nevertheless

`Disc_y(F)=4*x^2`.

So a discriminant factor can be entirely singular-image/conductor contribution even when the normalization has zero projection ramification and zero simultaneous criticality on both branches.

### Non-immersive cusp

Take

`F=y^2-x^3` with normalization `(x,y)=(t^2,t^3)`.

Here `delta=1`, the `x`-projection has ramification order `1`, the `y`-projection has ramification order `2`, and the branch is simultaneously critical. Yet the scalar discriminants also contain the same unavoidable `2*delta` normalization-defect correction on top of normalization ramification.

Thus curves with the same local delta contribution can have different simultaneous-critical behavior. Scalar discriminant degree does not determine the coefficientwise overlap `gcd(R105,R81)`.

## Consequence for the EX6 critical-value candidate

The obvious downstairs critical-value route based only on the two discriminant totals is therefore exact but non-independent:

- the degree-105 discriminant total is `16848 = 210 + 16638`;
- the degree-81 discriminant total is `16800 = 162 + 16638`;
- the common excess `16638` is exactly `2*delta(B)`;
- no positive lower bound on simultaneous normalization ramification follows;
- no member-level upper bound on `eta` or `rho` follows.

This does **not** prove that every possible critical-value/Jacobian route is exhausted. A finer relation could still exist at the actual `X(8) x X(8)` lift or in an explicit fixed-V6 pair-image equation, local Jacobian ideal, conductor factorization, subresultant, or higher-jet landing theorem. The bounded repository searches performed for `discriminant`, `resultant`, and pair-map terms did not surface such a retained explicit member-level asset; that search miss is not a repository-wide nonexistence claim.

The existing simultaneous-support scratch results therefore remain the relevant ceiling:

- O266 node common critical support is empty;
- opposite smooth-boundary excess supports `eta105` and `eta81` are disjoint;
- `c_common <= 28` remains the best current common-overlap cap;
- intrinsic delta gives only the dominated `c_common <= 472` bound;
- scalar pair-image discriminant totals add no independent inequality.

## Decision

Canonical scratch decisions:

- `PAIR_IMAGE_DISC_DEG_105_DIRECTION = 16848`;
- `PAIR_IMAGE_DISC_DEG_81_DIRECTION = 16800`;
- `PAIR_IMAGE_NORMALIZATION_RAMIFICATION_105 = 210`;
- `PAIR_IMAGE_NORMALIZATION_RAMIFICATION_81 = 162`;
- `PAIR_IMAGE_DISCRIMINANT_EXCESS_EACH_DIRECTION = 16638`;
- `PAIR_IMAGE_DISCRIMINANT_EXCESS_EQUALS_2DELTA = true`;
- `SCALAR_DISCRIMINANT_TOTALS_INDEPENDENT_OF_DELTA = false`;
- `SCALAR_DISCRIMINANTS_FORCE_POSITIVE_COMMON_OVERLAP = false`;
- `X8_MEMBER_LEVEL_JACOBIAN_OR_SUBRESULTANT_COUPLING = UNTESTED`;
- `INDEPENDENT_ETA_RHO_CAP_OBTAINED = false`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Firewalls

- No explicit fixed-V6 pair-image equation is claimed to have been constructed.
- The discriminant calculation is for the retained downstairs bidegree `(81,105)` pair-image and is not silently promoted to a stronger `X(8) x X(8)` member-level theorem.
- A bounded search miss is not repository-wide absence.
- Discriminant multiplicity is not identified with normalization ramification at singular image points.
- No conductor or delta total is recharged as an `eta/rho` cap.
- No Stage32 MAIN, O266 endpoint, lower-O, or Perfect Cuboid credit follows.
- This scratch leaf remains non-authoritative until a later retained consolidation and hostile-audit workflow.
