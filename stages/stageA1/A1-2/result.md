# StageA1-2 — first published-family anchor cuts

Source seed: Bremner–Elsholtz–Ulas, arXiv:2604.05459 (2026), explicit dimension-3 Hilbert-cube families used in the proofs of Theorems 1.5 and 1.6.

This file records a preliminary algebraic cut at `a0=0`. It is family-specific and requires independent audit before merge.

## Family I — one-parameter family from Theorem 1.5

The published family has

`a0 = 25 P(t)^2`

with

`P(t)=18 t^4 - 319 t^3 - 684 t^2 + 319 t + 18`.

A rational anchored member would require `P(t)=0` for rational `t`.

The cases `t=0` and the point at infinity do not solve the displayed quartic. For `t != 0`, divide by `t^2` and set

`u = t - 1/t`.

Using `t^2+t^-2 = u^2+2`, the quartic equation becomes

`18 u^2 - 319 u - 648 = 0`.

Its discriminant is

`D = 319^2 + 4*18*648 = 148417`.

Since

`385^2 = 148225 < 148417 < 148996 = 386^2`,

`D` is not a rational square. Hence the quadratic has no rational `u`, and therefore the displayed Theorem-1.5 one-parameter family has no rational parameter with `a0=0`.

Verdict:

`THM15_ONE_PARAMETER_ANCHORED_RATIONAL_MEMBER=false`.

This says nothing about Hilbert cubes outside this family.

## Family II — repeated-increment family from Theorem 1.6

The displayed family has an `a0` factorization of the form

`a0=(c-d)^2 Q(c,d)^2`,

where

`Q(c,d)=7c^4+12c^3d-22c^2d^2+12cd^3+7d^4`.

Thus `a0=0` splits into the component `c=d` and the component `Q(c,d)=0`.

### Component `c=d`

This is a degenerate specialization of the parametrized cube and must not be promoted to a nondegenerate anchored solution. The exact degeneracy of the remaining increments is an audit item against the paper's complete formulas.

### Component `Q(c,d)=0`

For `d != 0`, put `x=c/d`. The equation is

`7x^4+12x^3-22x^2+12x+7=0`.

For `x != 0`, divide by `x^2` and set

`y=x+1/x`.

Using `x^2+x^-2=y^2-2`, this becomes

`7y^2+12y-36=0`.

The discriminant is

`12^2+4*7*36 = 1152 = 576*2`,

which is not a rational square. The omitted `x=0` case does not solve the original quartic. Therefore `Q(c,d)=0` has no nonzero rational projective solution.

Conditional on the explicit `a0` factorization and the audit of the `c=d` degeneration, the nondegenerate Theorem-1.6 family has no rational anchored member.

## What was actually learned

Two large explicit infinite Hilbert-cube families can approach many square-cube configurations but miss the exact anchor `a0=0` for elementary algebraic reasons. This is substantive family-exclusion evidence, not a perfect-cuboid obstruction yet.

The next decisive question is whether the more general pre-specialization parametrization has an anchor-boundary component large enough to cover arbitrary anchored cubes, or whether the exclusions above are artifacts of the special one-parameter choices.

A1_2_STATUS=PRELIMINARY_FAMILY_EXCLUSION
GENERAL_PERFECT_CUBOID_CONSTRAINT=false
AUDIT_REQUIRED=true
NEXT=A1-3 general parametric boundary geometry
