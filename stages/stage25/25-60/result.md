# Stage25 checkpoint60 — causal decomposition, R501/R502 rigidity, and deep-route continuation

CHECKPOINT=60
STATUS=REPAIR_SUBMITTED_FOR_FRESH_AUDIT
DEEP_RESEARCH_MODE=true
PREVIOUS_AUDIT=FAIL_R502_ROUTE_BOUNDARY
REPAIR_SCOPE=R502_PRIMITIVE_HEIGHT_MULTIPLICITY_EXACTLY_TWO_NO_UPGRADE_CERTIFICATE

## 1. Accepted checkpoint60 core retained unchanged

From checkpoint50:

\[
B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

The Stage25 endpoint ratio has the audited envelope

\[
B^{-7/4}(\log B)^{-1}\ll \frac{N_2(B)}{M_1(B)}
\ll_\varepsilon B^{-3/2+\varepsilon}(\log B)^{-1}.
\]

Define

\[
F=\frac{M_2}{M_1},\qquad S=\frac{N_1}{M_1},\qquad
A=\frac{N_2}{M_2},\qquad T=\frac{N_2}{N_1}.
\]

Then

\[
\boxed{I=\frac{A}{S}=\frac{T}{F}=\frac{N_2M_1}{M_2N_1}},
\qquad
\boxed{\frac{N_2}{M_1}=FSI}.
\]

Using the audited checkpoint50 backflow,

\[
\boxed{I(B)\gg B^{1/4}(\log B)^{-7}\to\infty}.
\]

Thus the second-face and space-diagonal requirements have a positive divergent interaction in population-ratio semantics. This is an exact count-ratio correction, not a stochastic-independence claim.

The first hostile checkpoint60 audit explicitly accepted this causal theorem.

## 2. R501 accepted rigidity retained

For R501 reduced parameters in the physical cone,

\[
g_{501}=2^{7[m,n\text{ both odd}]}3^{4[3\mid m]}\le10368,
\]

and the accepted family-specific theorem is

\[
\boxed{N_{R501}(B)=\Theta(B^{1/4}).}
\]

The first hostile checkpoint60 audit accepted this theorem and no part of it is reopened.

## 3. R502 repair — source-level no-upgrade certificate

The previous audit correctly rejected the claim that R502 could be removed from the live set merely because its homogeneous degree is eight. The stronger repair option is now supplied in

`stages/stage25/25-60/r502-primitive-height-no-upgrade.md`.

Using Meskhishvili's third parametrization and `t=m/n`, define

\[
A=(m^4-n^4)(m^4-81n^4),
\]
\[
B=4mn(m^2-3n^2)(m^4+2m^2n^2+9n^4),
\]
\[
C=16m^2n^2(m^4-9n^4),
\]
\[
D=(m^4-2m^2n^2+9n^4)(m^4+10m^2n^2+9n^4).
\]

On the fixed cone

\[
\frac72<\frac mn<4,
\]

we have

\[
\boxed{0<A<B<C}.
\]

The exact primitive gcd is

\[
\boxed{
g_{502}=2^{5[m,n\text{ both odd}]}3^{4[3\mid m]}\le2592.
}
\]

Therefore primitive space height remains genuinely degree eight:

\[
\boxed{D/g_{502}\ge m^8/2592}.
\]

So primitive height `<=B` forces `m,n=O(B^{1/8})`; primitive gcd growth cannot secretly raise the R502 exponent.

The missing-face condition is

\[
w^2=P_{502}(t),
\]

where

\[
P_{502}(t)=t^{16}+16t^{14}-196t^{12}+112t^{10}+5926t^8
+1008t^6-15876t^4+11664t^2+6561.
\]

The checkpoint60 verifier proves `P_502` squarefree modulo `5`; hence the smooth projective curve has genus `7`. By Faltings only finitely many rational parameters acquire the third face. Thus asymptotically all counted R502 parameters give exactly two integral faces.

On the cone the scale-free invariant

\[
\frac{C}{D}
=\frac{16t^2(t^4-9)}{(t^4-2t^2+9)(t^4+10t^2+9)}
\]

has fibers of size at most `8`, because a fixed invariant value gives a nonzero degree-at-most-eight polynomial equation in `t`.

There are `gg T^2` reduced rational parameters in the cone with `m,n<=T`, while raw height is `O(T^8)` and primitive height is bounded below by a constant multiple of `m^8`. Consequently

\[
\boxed{N_{R502}(B)=\Theta(B^{1/4}).}
\]

Thus R502 is independently certified as a genuine same-exponent Stage19 family and **cannot by itself improve the global exponent beyond `1/4`**.

## 4. R504 accepted moving section retained

The generic non-torsion moving section and explicit `3P` section in R504 remain accepted by the previous hostile audit. The presently certified height growth still does not beat exponent `1/4`.

```text
R504_GENERIC_NONTORSION_SECTION_PROVED=true
R504_CURRENT_SECTION_BEATS_QUARTER=false
```

## 5. Persistent route registry and current state

```text
R501=Meskhishvili_first_positive_power_family
R502=Meskhishvili_third_parametrization_fallback
R503=Yoshida_uniform_varying_fiber_height
R504=symmetric_k_aggregation
R505=common_squarefree_core
R506=common_leg_plus_space
R507=R501_primitive_height_rigidity
```

Current route status after the R502 repair submission:

- `R501`: `PROVED_THETA_QUARTER`.
- `R502`: `CLOSED_NO_UPGRADE_WITH_CERTIFICATE_SUBMITTED_FOR_FRESH_AUDIT`; exact family growth `Theta(B^(1/4))`.
- `R503`: `LIVE_HIGH_VALUE_EXTERNAL_THEOREM_GATE`; uniform varying-fiber height/count remains missing.
- `R504`: `LIVE_STRUCTURAL_NO_EXPONENT_UPGRADE_YET`; generic non-torsion section proved.
- `R505`: `LIVE_NO_CLOSED_DIMENSION_HEIGHT_COUNT`.
- `R506`: `LIVE_NO_CLOSED_DIMENSION_HEIGHT_COUNT`.
- `R507`: `PROVED_R501_PRIMITIVE_HEIGHT_RIGIDITY`.

## 6. Current theorem boundary

```text
TWO_PATH_CAUSAL_DECOMPOSITION=PASS
CORRECTED_PRODUCT_IDENTITY_CHECK=PASS
ORDER_OF_CONDITIONS_INTERACTION=POSITIVE_DIVERGENT_SYMMETRIC_CROSS_RATIO
INTERACTION_SIGN=POSITIVE_DIVERGENT
INTERACTION_LOWER=I>>B^(1/4)(log B)^(-7)
DOUBLE_CHARGE_CHECK=PASS
R501_EXACT_FAMILY_GROWTH=Theta(B^(1/4))
R501_GCD_GLOBAL_BOUND=10368
R501_HIDDEN_GCD_EXPONENT_UPGRADE=false
R502_EXACT_FAMILY_GROWTH=Theta(B^(1/4))
R502_GCD_GLOBAL_BOUND=2592
R502_PARAMETER_FIBER_BOUND=8
R502_THIRD_FACE_EXCEPTION_CURVE_GENUS=7
R502_HIDDEN_GCD_EXPONENT_UPGRADE=false
R502_ROUTE_BOUNDARY_CERTIFICATE=SUBMITTED_FOR_FRESH_AUDIT
R504_GENERIC_NONTORSION_SECTION_PROVED=true
GLOBAL_LOWER_EXPONENT_ABOVE_QUARTER_PROVED=false
MATCHING_HALF_POWER_LOWER_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
PERFECT_CUBOID_CONCLUSION=NONE
FINITE_DATA_USED_AS_PROOF=false
EXPLORATION_EVIDENCE_COMPLETE=true
```

## 7. Continuation semantics

A fresh audit is required for the new R502 certificate. A PASS repairs the narrow FAIL finding but still does **not** close checkpoint60 while R503-R506 remain actionable.

```text
ROUTE_ID_IS_PERSISTENT=true
AUDIT_PASS_DOES_NOT_IMPLY_CHECKPOINT60_CLOSE=true
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
NEXT_AFTER_AUDITED_MERGE=CONTINUE_CHECKPOINT60_USING_R503_R506_AND_ANY_GENUINELY_NEW_R508_PLUS_ROUTE
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=60
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage25-audit
```
