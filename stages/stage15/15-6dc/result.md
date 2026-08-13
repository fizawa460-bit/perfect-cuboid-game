# Stage15-6dc — EXHAUSTIVE_VIEW_AUDIT of the reconstructed three-variable/Pell graph

Base: Stage15-6da is accepted as an exact reconstruction theorem: for fixed legal cross-gcd cells and any three residual variables, the fourth residual variable has only `B^o(1)` exact-survivor completions. The fresh audit correctly treats this as a **material receiver change**. We therefore do not promote the previously parked dispersion route yet.

Keep
\[
m=abM,\quad n=cdN,\quad r=acU,\quad s=bdV,
\qquad H=abcd,
\qquad HMNUV\le B,
\]
with pairwise-coprime cells, `(q,H)=1`, and the exact survivor equations
\[
a^4M^2U^2+d^4N^2V^2=kP^2,
\]
\[
b^4M^2V^2+c^4N^2U^2=kQ^2.
\]
Write
\[
X=abM,\qquad Y=cdN,\qquad \Delta=X^4-Y^4\ne0.
\]
Stage15-6da turns the exact survivor set into a divisor-many graph over any chosen three residual coordinates. The question is now how to count or thin **that graph**, not the ambient four-variable congruence family.

## A. Root-ratio discrepancy dispersion — LIVE / UNTESTED ON RECONSTRUCTED GRAPH

For fixed cells/core/local orientations, one may subtract the `q^-2` local main density and average the remaining root-line discrepancy over `(q,rho)` **after** restricting to the reconstructed graph. This is materially different from 6cx because one ambient support variable has been eliminated before dispersion.

No Stage14 fixed-packet Type-II, spacing, or spectral exponent is promoted. A whole-family physical graph adapter is still required.

## B. Pell/unit-orbit counting — LIVE / SUPPORTING / SECOND-CONDITION REFINEMENT UNTESTED

For fixed `(M,N,U,k)`, the first norm equation is
\[
(d^2NV)^2-kP^2=-(a^2MU)^2.
\]
Stage15-6da counts its bounded-height solutions by ideal divisors times `O(log B)` unit powers. Used alone this is exponent-neutral after summing the base triples. However the **second** norm equation cuts this Pell orbit and has not been exploited quantitatively. Counting the intersection of the Pell unit orbit with the second norm-square condition is a distinct LIVE refinement.

## C. Norm-equation / ideal-factor averaging — LIVE / UNTESTED

Instead of applying the divisor bound pointwise to each norm target, average the ideal-divisor multiplicity over the reconstructed base triples and common cores. Average divisor complexity can improve logarithms, but a fixed power saving is not automatic. The possibility that the second norm equation forces atypical ideal-factor alignments remains UNTESTED.

## D. Reconstructed divisor switching — LIVE / UNTESTED

The exact `phi(d_S)phi(e_O)` divisor expansion and complementary cofactors remain legal. After reconstruction, however, switching can be performed on graph nodes rather than ambient four-variable states. This may expose inverse-threshold decay without paying an independent fourth support. It is not identical to the old ambient complementary receiver and remains LIVE.

## E. Mixed norm / linear-factor incidence — LIVE / STRENGTHENED BY AN EXACT ELIMINANT

Eliminating `V^2` and `U^2` from the two survivor equations gives the exact identities
\[
\boxed{
\Delta U^2
=k\bigl((b^2MP)^2-(d^2NQ)^2\bigr),
}
\]
\[
\boxed{
\Delta V^2
=k\bigl((a^2MQ)^2-(c^2NP)^2\bigr).
}
\]
Indeed the first identity is `b^4M^2*(first norm) - d^4N^2*(second norm)`, and the second is `a^4M^2*(second norm) - c^4N^2*(first norm)`.

Thus every reconstructed survivor lies simultaneously on two factored incidences:
\[
\Delta U^2
=k(b^2MP-d^2NQ)(b^2MP+d^2NQ),
\]
\[
\Delta V^2
=k(a^2MQ-c^2NP)(a^2MQ+c^2NP).
\]
The odd core already satisfies `k^circ|Delta`. After the bounded 2-adic convention is isolated, the quotient of `Delta` by the charged core is an exact fixed-side coefficient. This **double eliminant** is a deterministic graph-sparsity mechanism not present in the ambient root-line receiver.

No extra saving is claimed yet: the square factors `U^2,V^2` move, so an AR-012-style fixed-target conclusion cannot be imported automatically. But the route is materially distinct and LIVE.

## F. Local valuation structure — LIVE / SUPPORTING

For every odd `p|q`, `(p,H)=1` and the relevant cell coefficients are units. Channel primes are in `p=1 mod 4`, local root multiplicity is bounded divisor-like, and the exact eliminants now additionally couple `v_p(Delta/k^circ)` to the two linear-factor valuations. A valuation split between the `+` and `-` factors may restrict legal graph branches. No fixed exponent is yet certified.

## G. Deterministic graph sparsity by second-equation intersection — LIVE / UNTESTED

Stage15-6da used one Pell norm equation to enumerate a divisor-many completion list and treated the second equation as a postfilter. On the reconstructed graph the natural deterministic refinement is to ask whether that second equation removes all but `B^o(1)` **unit-orbit positions after fewer than three base variables are fixed**, or whether the two exact eliminants force an additional divisor relation. This could reduce the graph dimension without cancellation and is therefore LIVE.

## H. Pure per-modulus lattice counting — DOMINATED AS GLOBAL ROUTE / RETAINED LOCAL ENGINE

The primitive root-line lattice estimate remains correct locally. As a global strategy it is dominated by reconstructed-graph methods because using it before reconstruction recreates the one-sided fringe that 6da has already compressed.

## I. Pair-energy / old cross-resultant route — DOMINATED FOR CURRENT GRAPH GATE

The earlier pair-energy machinery controls large shared prime support and degeneracies. It does not automatically exploit the new divisor-many graph completion and therefore remains a fallback, not the selected reconstructed-graph route.

## Exhaustive-view conclusion

Material LIVE/UNTESTED reconstructed-graph routes are:
- root-ratio discrepancy dispersion;
- Pell/unit-orbit intersection with the second norm equation;
- norm/ideal-factor averaging;
- reconstructed divisor switching;
- mixed norm/linear-factor incidence through the double eliminant;
- local-valuation refinement;
- deterministic second-equation graph sparsity.

No LIVE or UNTESTED route is deleted.

```text
STAGE15_6_SUBSTAGE=6dc
STAGE15_6DC_MATERIAL_RECEIVER_CHANGE_ACKNOWLEDGED=true
STAGE15_6DC_EXHAUSTIVE_VIEW_AUDIT=true
STAGE15_6DC_6DA_RECONSTRUCTION_ACCEPTED=true
STAGE15_6DC_DISPERSION=LIVE_UNTESTED
STAGE15_6DC_PELL_UNIT_ORBIT=LIVE
STAGE15_6DC_IDEAL_FACTOR_AVERAGING=LIVE_UNTESTED
STAGE15_6DC_RECONSTRUCTED_DIVISOR_SWITCH=LIVE_UNTESTED
STAGE15_6DC_DOUBLE_ELIMINANT=true
STAGE15_6DC_MIXED_FACTOR_INCIDENCE=LIVE
STAGE15_6DC_LOCAL_VALUATION=LIVE_SUPPORTING
STAGE15_6DC_DETERMINISTIC_GRAPH_SPARSITY=LIVE_UNTESTED
STAGE15_6DC_EXIT=RECONSTRUCTED_GRAPH_BLIND_REDISCOVERY_READY
```