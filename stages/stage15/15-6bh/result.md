# Stage15-6bh — diagonal-support restatement firewall

Base: merged PR #851. This is an audit stage.

## Verdict

`AUDIT_VERDICT=BLOCK` for treating the admissible diagonal support bound as an independent causal theorem.

Stage15-6be proved that for every fixed physical diagonal variable

\[
S=kZW=(\gamma/2)R,\qquad \gamma\in\{2,4\},
\]

the complete physical survivor fiber has cardinality `B^o(1)`. Let

\[
\mathcal S(B)=\{S\le 2B:\text{a physical Stage15 survivor lies over }S\}.
\]

Then trivially every support value contributes at least one survivor, while 6be gives a subpolynomial upper multiplicity. Hence

\[
\boxed{|\mathcal S(B)|\le N_2(B)\le |\mathcal S(B)|B^{o(1)}.}
\]

Moreover `S=(gamma/2)R` with only two values of `gamma`, so the `S`-support is only a finite relabeling of the integral-space-diagonal support.

Therefore asking for

\[
|\mathcal S(B)|\ll B^{1/2+o(1)}
\]

as a new black-box theorem is equivalent up to `B^o(1)` to the numerator theorem we are trying to rederive causally. It is not a simpler external gate.

The correct next move is to reopen the algebra *inside one support value* only to identify a lower-dimensional structural receiver, not to assume a support theorem.

```text
STAGE15_6_SUBSTAGE=6bh
STAGE15_6BH_AUDIT_VERDICT=BLOCK
STAGE15_6BH_FIXED_S_FIBER_SUBPOLYNOMIAL=true
STAGE15_6BH_SUPPORT_COUNT_EQUIVALENT_TO_N2_UP_TO_Bo1=true
STAGE15_6BH_S_IS_FINITE_RELABEL_OF_R=true
STAGE15_6BH_SUPPORT_THEOREM_AS_BLACKBOX_CIRCULAR=true
STAGE15_6BH_EXIT=COMPLEMENTARY_GAUSSIAN_PRODUCT_RECEIVER_AUDIT_READY
```
