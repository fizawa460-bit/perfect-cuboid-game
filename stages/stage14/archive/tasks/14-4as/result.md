# Stage14-4as — end-to-end weighted retainer synthesis

## Result

Stages 14-4ap, 14-4aq, and 14-4ar have isolated the three arithmetic gates in the collective Stage14 mechanism:

```text
A -> Sigma -> R -> H_C
```

where `A` is the eligible primitive Euclid-base family, `Sigma` is the nontrivial full-2-Selmer gate, `R` is positive Mordell--Weil rank, and `H_C` is the existence of a non-torsion point in the fixed s3 logarithmic canonical-height window. For every admissible s3 comparison constant,

\[
V(B)\le H_C(B).
\]

The purpose of 14-4as is to combine the three already-isolated retainers without any probabilistic independence hypothesis.

## One common weighted family

Fix a dyadic Euclid box and any admissible nonnegative weight `W_Q(F)` used by the centered local-sieve interface. Define

\[
A_Q=\sum_F W_Q(F),
\quad S_Q=\sum_F W_Q(F)s(F),
\quad R_Q=\sum_F W_Q(F)r(F),
\quad H_{Q,C}=\sum_F W_Q(F)h_{B,C}(F).
\]

Pointwise,

\[
h_{B,C}(F)\le r(F)\le s(F)\le1,
\]

so

\[
0\le H_{Q,C}\le R_Q\le S_Q\le A_Q.
\]

Whenever the denominators are nonzero, the exact weighted factorization is

\[
\frac{H_{Q,C}}{A_Q}
=\frac{S_Q}{A_Q}\frac{R_Q}{S_Q}\frac{H_{Q,C}}{R_Q}.
\]

As in 4ap, zero-denominator ratios are interpreted as zero. This identity is purely algebraic and makes no independence assumption.

## Three uniform targets

The local, global/Sha, and height inputs can be stated on this same weighted family as

\[
S_Q\le \rho_{\rm loc}A_Q+E_{\rm loc},
\]

\[
R_Q\le \rho_{\rm glob}S_Q+E_{\rm glob},
\]

\[
H_{Q,C}\le \rho_{\rm ht}R_Q+E_{\rm ht}.
\]

Here every `rho` and `E` may depend on the dyadic box and on the permitted parameters `(B,Q,C)`; no independence or product-density interpretation is imposed.

Substitution gives the exact deterministic transfer

\[
\boxed{
H_{Q,C}\le
\rho_{\rm ht}\rho_{\rm glob}\rho_{\rm loc}A_Q
+\rho_{\rm ht}\rho_{\rm glob}E_{\rm loc}
+\rho_{\rm ht}E_{\rm glob}
+E_{\rm ht}.}
\]

This is the end-to-end theorem target for the three Stage14 retainers.

## Exponent transfer and error budget

Suppose uniformly on the boxes needed for the global decomposition that

\[
A_Q\ll B^{1+o(1)},
\quad
\rho_i\ll B^{-\delta_i+o(1)}
\quad(i={\rm loc,glob,ht}).
\]

Then the main term has exponent

\[
1-\delta_{\rm loc}-\delta_{\rm glob}-\delta_{\rm ht}+o(1).
\]

The three propagated errors must separately satisfy the desired final scale:

\[
\rho_{\rm ht}\rho_{\rm glob}E_{\rm loc},
\quad
\rho_{\rm ht}E_{\rm glob},
\quad
E_{\rm ht}.
\]

Thus a square-root upper-bound program requires not only

\[
\delta_{\rm loc}+\delta_{\rm glob}+\delta_{\rm ht}\ge\tfrac12,
\]

but also each propagated error to be `O(B^{1/2+o(1)})`. This error-budget condition was implicit in 4ap and is now explicit.

If `rho_glob=O(1)` only, then `delta_glob=0`; likewise for either other gate. Constant-density information multiplies constants but supplies no power saving.

## Physical transfer

The weighted statement is an analytic interface. To obtain the physical unweighted bound one must instantiate the allowed family so that the exact/unweighted base count is represented or dominated, and then sum the dyadic boxes. In particular, no cancellation estimate for a signed centered trace alone is automatically an upper bound for `V(B)`.

For the unweighted specialization `W_Q(F)=1`, the same recursion reduces to the 4ap chain

\[
H_C=A\,(\Sigma/A)(R/\Sigma)(H_C/R),
\]

and `V(B)<=H_C(B)` transfers any valid final upper bound to the physical active-vertex count.

## Finite boundary

At `H<=20,000`, the complete audited data still give

```text
A=6372
Sigma=5209
R in [3784,4239]
V=54
```

but 4ar has not measured the complete `H_C` census. Therefore these data do not assign asymptotic values to any `delta_i`, and especially do not identify `V/R` with `H_C/R`.

The current state is consequently a theorem architecture, not a proof of a power saving. The centered local family large sieve remains unproved; 4aq proves no positive global exponent; 4ar proves no uniform height lower-tail exponent.

## Boundary

```text
STAGE14_4AS=END_TO_END_WEIGHTED_RETAINER_THEOREM_TARGET_SYNTHESIZED
COMMON_NONNEGATIVE_WEIGHTED_FAMILY_LOCKED=true
WEIGHTED_THREE_GATE_FACTORIZATION_EXACT=true
INDEPENDENCE_ASSUMPTION_REQUIRED=false
RECURSIVE_THREE_RETAINER_TRANSFER_EXACT=true
PROPAGATED_ERROR_BUDGET_EXPLICIT=true
PHYSICAL_TRANSFER_REQUIRES_UNWEIGHTED_OR_DOMINATING_INSTANTIATION=true
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false
UNIFORM_FIRST_SMALL_POINT_LOWER_TAIL_PROVED=false
POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

No product-density heuristic is promoted to a theorem. No new retainer bound, power saving, square-root law, or leading constant is claimed.

```text
NEXT=Stage14-4at instantiate the end-to-end target on the dyadic Euclid decomposition, choose Q(B), and expose the first quantitatively insufficient retainer or propagated error
```
