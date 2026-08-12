# Stage15-6bs — codimension-two multiplicative-sieve gate

Base: Stage15-6br. Audit verdict: NEW_GATE.

The actual odd core q is squarefree and every p|q forces one of finitely many S/O codimension-two residue conditions on the two torus coordinates. Primewise local density is O(p^-2), orientation multiplicity is 2^{O(omega(q))}=B^o(1), and CRT gives the exact fixed-q index q^2 from 6bl.

Huang effective equidistribution is too weak for polynomially growing q, and the one-large-prime geometric sieve leaves only logarithmic saving. The remaining theorem species must therefore aggregate many small prime conditions before paying the neighbourhood-complexity error: a dimension-two Selberg/large-sieve or universal-torsor congruence estimate uniform in squarefree q.

Target interface:

\[
\sum_{q>Q\atop q\ \mathrm{squarefree}} N_q(B) \ll B^{1+o(1)}/Q,
\]

or any comparable aggregate estimate strong enough to combine with the existing low-q bound.

No such estimate is claimed here.

```text
STAGE15_6_SUBSTAGE=6bs
STAGE15_6BS_AUDIT_VERDICT=NEW_GATE
STAGE15_6BS_FIXED_q_LOCAL_DENSITY=q^-2
STAGE15_6BS_HUANG_ROUTE_EXHAUSTED=true
STAGE15_6BS_LARGE_PRIME_ONLY_ROUTE_EXHAUSTED=true
STAGE15_6BS_REQUIRED_OBJECT=UNIFORM_CODIMENSION_TWO_MULTIPLICATIVE_SIEVE_ON_STAGE15_TORUS
STAGE15_6BS_CAUSAL_THREE_QUARTERS_PROVED=false
STAGE15_6BS_EXIT=DIMENSION_TWO_SIEVE_OR_UNIVERSAL_TORSOR_CONGRUENCE_THEOREM_GATE
```
