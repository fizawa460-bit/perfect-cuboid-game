# Stage14-e supplement roadmap — post-control-track refinements

## Purpose

Stage14-e1 through Stage14-e5 form a completed control experiment.  They are not reopened here.  This supplement track sharpens the solved ambient theory without changing the main Stage14 integer-space-diagonal problem.

The literature-first rule remains mandatory: every supplement must refresh primary literature before promoting a constant, secondary term, effective error, or novelty claim.

## 14-e6 — explicit Peyre/Tamagawa constant

Status: [>] Active.

Goal: replace the e4 placeholder

\[
E_q(B)\sim \Lambda_E M_q B(\log B)^5
\]

by an explicit arithmetic constant for the physical Euclidean projective height.

Required checkpoints:

1. compute Peyre's effective-cone factor `alpha(Y)` for
   \[
   Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1);
   \]
2. lock `beta(Y)=1` and the trivial Brauer correction for the split toric surface;
3. normalize the real Tamagawa density relative to the e4 chamber integrals `M_q`;
4. compute every odd-prime local density in closed form;
5. isolate and compute the bad `p=2` metric factor caused by the coefficients `2,4` in the physical projective map;
6. assemble a convergent Euler product for `Lambda_E`;
7. provide a deterministic numerical interval with a rigorous product-tail bound;
8. verify that removal of the third-face-square thin set leaves the same leading constant.

No secondary term or effective remainder for the counting function is claimed in e6.

## 14-e7 — secondary asymptotics / crossover

Status: [ ] Pending e6.

Target the height-zeta Laurent expansion and lower logarithmic terms explaining why the finite census through `B=10^6` mimics `B(log B)^3` despite the proved `B(log B)^5` main order.

## 14-e8 — quantitative Euler-brick thin-set count

Status: [ ] Pending.

Seek a quantitative saving for the third-face-square subpopulation beyond the e4 qualitative `o(B(log B)^5)` theorem.

## 14-e9 — gcd/lcm and local-statistics decomposition

Status: [ ] Pending.

Resolve the ambient distribution of the common-edge gcd/lcm strata and finite-local statistics as a control object for the main Stage14 arithmetic.

```text
STAGE14_E_CONTROL_TRACK_E1_TO_E5=COMPLETE
STAGE14_E_SUPPLEMENT_TRACK=DEFINED
STAGE14_E6=ACTIVE_EXPLICIT_PEYRE_TAMAGAWA_CONSTANT
NEXT_E_SUPPLEMENT=Stage14-e6 explicit Peyre/Tamagawa constant
```
