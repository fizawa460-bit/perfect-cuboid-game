# Stage25-60 R504 exceptional base-change search

STATUS=ACTIVE_RESEARCH_SUBMITTED_FOR_FRESH_AUDIT
ROUTE=R504
CHECKPOINT=60

## Purpose

The hostile repair-2 audit left exactly one repo-native lane live:

```text
R504_EXCEPTIONAL_BASE_CHANGE_RESIDUAL=LIVE_EXPLICIT_CURVE_SEARCH
```

This artifact executes that search rather than relabeling it as an external gate.

## Exact rank-jump receiver

For
\[
E_F:\ Y^2=X^3-4(k^4+1)^2X
\]
and a rational base change `k=phi(u)`, put
\[
C_\phi:\ y^2=\operatorname{num}(\phi(u)^4+1)\operatorname{den}(\phi(u))^4.
\]
The twist-descent already audited for R504 shows that a new independent pullback section can occur only when the anti-invariant part of `J(C_phi)` contains an additional elliptic factor Q-isogenous to
\[
E_0:v^2=u^3-4u.
\]
Thus the residual search is an explicit curve/Jacobian search, not an unspecified rank computation.

## Degree-two normal form

Up to source and target PGL2 changes, a degree-two rational map has one-dimensional branch data. The useful search invariant is therefore the branch divisor of the pullback of the four roots of `k^4+1`; after removing inherited factors, an exceptional candidate must force an extra genus-one quotient whose Jacobian has `j=1728` and the correct Q-isogeny/twist class.

The previously audited representatives

```text
BC1: phi(u)=u^2
BC2: phi(u)=(u^2-1)/(2u)
```

are the two maximally symmetric branch configurations already materialized in the repository. Their genus-three pullback Jacobians have no additional `E0` factor and hence no rank jump.

## Fresh exceptional mutations

The following mutations are the next symmetry-forcing degree-two ansatz classes, obtained by moving the two branch values through the dihedral orbit preserving the quartic root set. They are not counted as new route IDs; they remain R504 refinements.

```text
BC3: phi_a(u)=(u^2-a)/(2u), a in Q* modulo square/PGL2 normalization
BC4: phi_a(u)=(u^2+a)/(2u), a in Q* modulo square/PGL2 normalization
BC5: phi_a(u)=a*u^2, a in Q* modulo fourth-power/twist normalization
```

For BC3/BC4, a genuinely exceptional member must make one of the residual genus-one quotients acquire `j=1728`; equivalently its binary-quartic invariants must satisfy the vanishing condition `J=0`. For BC5, scaling only changes the quartic twist class and cannot create a second independent anti-invariant `E0` copy without the same `J=0` exceptional condition.

This reduces the live search to solving the explicit coefficient condition `J(a)=0` in each one-parameter ansatz, followed by a Q-isogeny/twist check and then the Stage19 physical-height adapter. A finite scan in `a` is not accepted as proof.

## What is and is not closed

The search has therefore advanced from an unstructured `some exceptional phi` gate to three explicit one-parameter mutation classes and an exact algebraic exceptional condition. It has **not** proved that `J(a)=0` has no rational solution in all classes, and it has not classified arbitrary degree-two `phi`.

```text
R504_BC3_STATUS=LIVE_EXPLICIT_INVARIANT_EQUATION
R504_BC4_STATUS=LIVE_EXPLICIT_INVARIANT_EQUATION
R504_BC5_STATUS=LIVE_EXPLICIT_INVARIANT_EQUATION
R504_EXCEPTIONAL_CONDITION=RESIDUAL_GENUS1_BINARY_QUARTIC_J_INVARIANT_ZERO
R504_EXCEPTIONAL_BASE_CHANGE_RESIDUAL=LIVE_EXPLICIT_CURVE_SEARCH
R504_ARBITRARY_DEGREE2_CLASSIFICATION_PROVED=false
R504_NEW_RANK_JUMP_PROVED=false
R504_NEW_STAGE19_FAMILY_PROVED=false
GLOBAL_STAGE25_LOWER_CHANGED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
```

## Next attack

Compute the residual binary-quartic invariant polynomial `J(a)` for BC3, BC4 and BC5 symbolically; factor it over Q; for every rational component satisfying `J(a)=0`, test the resulting genus-one quotient for Q-isogeny to `E0`, then materialize the cuboid height/multiplicity adapter. If all three ansatz classes close, broaden to the general degree-two branch parameter rather than declaring an external gate.
