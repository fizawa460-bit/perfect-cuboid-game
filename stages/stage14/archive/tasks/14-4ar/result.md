# Stage14-4ar — positive-rank to first-small-point retainer

## Result

Stage14-s3 gives the necessary physical implication

\[
d\le B\quad\Longrightarrow\quad
\widehat h(P)\le C(\log B+\log H(F))
\]

for some fixed comparison constant `C`, with `P` non-torsion on

\[
E_F: Y^2=Z(Z-S^2)(Z+X^2).
\]

To isolate this final arithmetic retainer, define

\[
\lambda(F)=\min\{\widehat h(P):P\in E_F(\mathbf Q)\text{ non-torsion}\},
\]

with `lambda(F)=+infinity` when `rank E_F(Q)=0`. Let

\[
r(F)=1_{\operatorname{rank}E_F(\mathbf Q)>0},
\qquad
h_{B,C}(F)=1_{\lambda(F)\le C(\log B+\log H(F))}.
\]

Then `h_{B,C}(F)<=r(F)`. Put

\[
u_{B,C}(F)=r(F)-h_{B,C}(F).
\]

Thus, exactly,

\[
\mathcal H_C(B)=R(B)-U_C(B),
\qquad
U_C(B)=\sum_F u_{B,C}(F).
\]

For every admissible fixed s3 comparison constant,

\[
V(B)\le \mathcal H_C(B).
\]

The converse is not claimed: a sufficiently small rational elliptic point need not satisfy the frozen physical-coordinate conditions.

## Weighted lower-tail target

Let `W_Q(F)>=0` be any weight compatible with the centered full-local sieve used in 4aq. Define

\[
R_Q=\sum_F W_Q(F)r(F),\quad
H_{Q,C}=\sum_F W_Q(F)h_{B,C}(F),\quad
U_{Q,C}=\sum_F W_Q(F)u_{B,C}(F).
\]

Pointwise `h=r-u`, hence without any independence assumption,

\[
H_{Q,C}=R_Q-U_{Q,C}.
\]

The uniform first-small-point lower-tail theorem needed by the main track can therefore be targeted as

\[
H_{Q,C}\le \rho_{\rm ht}(B,Q,C)R_Q+E_{\rm ht}(B,Q,C),
\]

uniformly over the dyadic Euclid boxes and allowed centered-local weights. Equivalently,

\[
U_{Q,C}\ge (1-\rho_{\rm ht}(B,Q,C))R_Q-E_{\rm ht}(B,Q,C).
\]

If eventually

\[
\rho_{\rm ht}(B,Q,C)\ll B^{-\delta_{\rm ht}}
\]

with negligible error, then `delta_ht` contributes directly to the 4ap exponent budget. A mere constant-density bound contributes no power saving.

## Finite-data boundary

The complete 4am census gives only the physical subcount `V`, not the complete canonical-height-window count `H_C`. At `H<=20,000`,

```text
R in [3784,4239]
V=54
V/R in [0.0127388535,0.0142706131]
```

Since

\[
V\le H_C\le R,
\]

these data **do not** show that `H_C/R` is itself about `1.3%`. They only give a physical lower bound on the height-window retainer.

The s3 diagnostic remains informative but non-asymptotic: among 96 sampled actual first hits, canonical height has median `3.6080` and maximum `6.5243`; 29 inactive controls already certified to have positive rank have found witness heights with median `10.2839` and maximum `35.9080`. Those inactive witnesses are not certified Mordell--Weil minima, so they cannot be used as a numerical census of `lambda(F)`.

This distinction is essential: 14-4ar formulates the correct lower-tail object but does not pretend the existing finite audit has measured it completely.

## Boundary

```text
STAGE14_4AR=FIRST_SMALL_POINT_RETAINER_ISOLATED_AND_WEIGHTED_LOWER_TAIL_TARGET_FORMULATED
MINIMUM_NON_TORSION_CANONICAL_HEIGHT_INTERFACE_LOCKED=true
PHYSICAL_HIT_IMPLIES_HEIGHT_RETAINER=true
HEIGHT_RETAINER_EXACT_COMPLEMENT_IDENTITY=true
CENTERED_LOCAL_WEIGHTED_HEIGHT_IDENTITY=true
UNIFORM_WEIGHTED_SMALL_POINT_LOWER_TAIL_TARGET_FORMULATED=true
HEIGHT_RETAINER_FINITE_COMPLETE_CENSUS_MEASURED=false
UNIFORM_FIRST_SMALL_POINT_LOWER_TAIL_PROVED=false
POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

No regulator distribution theorem, least-generator theorem, uniform small-point density, power saving, or `sqrt(B)` asymptotic is claimed.

```text
NEXT=Stage14-4as synthesize the local, global/Sha, and first-small-point weighted retainers into one end-to-end theorem target without assuming independence
```
