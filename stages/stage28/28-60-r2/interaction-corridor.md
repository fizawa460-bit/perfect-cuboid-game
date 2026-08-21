# Stage28-60-r2 — current corridor relative to the interaction threshold

```text
ROUTE=R18_INTERACTION_THRESHOLD_CORRIDOR
STATUS=NEGATIVE_CERTIFICATE_WITH_EXACT_TRANSLATION
```

The normalized interaction curvature

\[
\mathcal K_{28}=(\log B)^2\mathcal I_{face}/\mathcal I_{sp}
\]

is asymptotically a positive constant multiple of the direct bridge `M3/N2`.  Therefore the existing Stage28 checkpoint30 corridor translates without loss of polynomial information.

For every fixed `epsilon>0`,

\[
\frac{M_3}{N_2}\gg_\varepsilon B^{-1/6-\varepsilon},
\]

and for every fixed `0<delta<1/46`,

\[
\frac{M_3}{N_2}
=o\!\left(B^{3/4}(\log B)^{5-\delta}\right).
\]

Hence

\[
\boxed{
\mathcal K_{28}(B)\gg_\varepsilon B^{-1/6-\varepsilon}
}
\]

and

\[
\boxed{
\mathcal K_{28}(B)
=o\!\left(B^{3/4}(\log B)^{5-\delta}\right).
}
\]

Equivalently, for the unnormalized quotient

\[
\mathcal J_{28}=\mathcal I_{face}/\mathcal I_{sp},
\]

\[
\boxed{
\mathcal J_{28}(B)
\gg_\varepsilon
B^{-1/6-\varepsilon}(\log B)^{-2}
}
\]

and

\[
\boxed{
\mathcal J_{28}(B)
=o\!\left(B^{3/4}(\log B)^{3-\delta}\right).
}
\]

The critical ordering scale is `J_28 ~ (log B)^(-2)`.  The present corridor crosses that threshold by a huge margin, so no asymptotic ordering follows.

The same failure can be seen by comparing the two interaction corridors separately.  `S25-W02` and the current `N2` upper give, schematically,

\[
B^{1/4}(\log B)^{-7}
\ll \mathcal I_{sp}
\ll_\varepsilon B^{1/2+\varepsilon}(\log B)^{-7},
\]

while checkpoint60 and the current `M3` upper give

\[
B^{1/3}(\log B)^{-9}
\ll \mathcal I_{face}
=o\!\left(B(\log B)^{-4-\delta}\right)
\]

for each fixed `delta<1/46` after choosing the corresponding audited endpoint-free upper.  These two corridors overlap too broadly to order the interactions.

Thus “both interactions diverge” is genuinely weaker than the comparison needed by Stage28.

```text
CURRENT_BOUNDS_LOCATE_J_RELATIVE_TO_LOG_MINUS_2=false
BOTH_INTERACTIONS_DIVERGE_BUT_RELATIVE_ORDER_UNKNOWN=true
DIRECT_BRIDGE_CORRIDOR_IMPROVED=false
NEW_EXPONENT_CLAIM=false
AUDIT_REQUIRED=true
```