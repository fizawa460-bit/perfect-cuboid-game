# Stage15-6bj — equal-hypotenuse / square-sieve independence audit

Base: Stage15-6bi. Audit verdict: `BLOCK`.

Put

\[
E_1=xp-yq,\quad E_2=xq+yp,\quad E_3=xp+yq,\quad E_4=yp-xq.
\]

The two Gaussian products satisfy

\[
E_1^2+E_2^2=E_3^2+E_4^2=S^2.
\]

However this equal-hypotenuse condition is not a new independent arithmetic constraint. Indeed

\[
E_3^2-E_1^2=E_2^2-E_4^2
\]

is exactly

\[
(2xp)(2yq)=(2xq)(2yp),
\]

i.e. the rank-one product identity already forced by the endpoint definitions. Conversely endpoint inversion plus equal norms recovers that identity.

Thus replacing the Stage15 receiver by “two Pythagorean triples with equal hypotenuse” discards the primitive Gaussian/core provenance without adding a new saving condition.

A direct Heath-Brown square-sieve invocation is also not certified here. The square sieve controls square-valued tuple counts after character-sum input; Stage15 now needs a support statement in `S`, and 6be already showed that support and physical point count are equivalent up to `B^o(1)`. A generic tuple bound cannot silently be promoted to the desired support half-power.

Primary reference audited: D. R. Heath-Brown, *The Square Sieve and Consecutive Square-Free Numbers*, Math. Ann. 266 (1984), 251–260.

```text
STAGE15_6_SUBSTAGE=6bj
STAGE15_6BJ_AUDIT_VERDICT=BLOCK
STAGE15_6BJ_EQUAL_HYPOTENUSE_INDEPENDENT_CONSTRAINT=false
STAGE15_6BJ_ENDPOINT_RANK_ONE_IDENTITY_REPACKAGED=true
STAGE15_6BJ_GENERIC_SQUARE_SIEVE_DIRECT_SUPPORT_ADAPTER=false
STAGE15_6BJ_EXIT=JOINT_CORE_ENDPOINT_CONGRUENCE_AUDIT_READY
```
