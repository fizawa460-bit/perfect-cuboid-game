# Stage29-02ha source lock — full sign/Kummer cover of the cuboid surface

## Load-bearing endpoint source

The endpoint canonical model is the Testa–Stoll cuboid surface

\[
\bar S\subset \mathbf P^6_{a_1,a_2,a_3,b_1,b_2,b_3,c}
\]

defined by

\[
a_1^2+a_2^2=b_3^2,\quad
 a_2^2+a_3^2=b_1^2,\quad
 a_1^2+a_3^2=b_2^2,\quad
 a_1^2+a_2^2+a_3^2=c^2.
\]

Primary/code lock:

- Michael Stoll / Damiano Testa, *The surface parametrizing cuboids*, arXiv:1009.0388; current author PDF `https://mathe2.uni-bayreuth.de/stoll/papers/Cuboidi.pdf`.
- Verification repository commit `51233ed5ef2bf228fac9416c66db9adc0ebcaadd`, file `Cuboids/cuboids.magma`; the file constructs the above four quadrics and checks the 48 singular points.
- Testa–Stoll, *Curves on the surface of cuboids*, Mathematics of Computation, DOI `10.1090/mcom/4238`, supplies the current endpoint geometry/curve results already locked in Stage29-02a.

Fresh audit rechecked the current Testa–Stoll author PDF. Theorem 1 gives the full geometric automorphism group `G` of order `1536` and the exact sequence

```text
1 -> mu_2^7/mu_2 -> G -> S4 -> 1,
```

where the kernel is the independent coordinate-sign group modulo common projective sign. This independently cross-checks the Stage29-02ha derivation

```text
G_sign ~= (Z/2)^6,
|G_sign|=64,
Aut(base seven-line arrangement) ~= S4,
64*24=1536.
```

The same source explains that the extra automorphism enlarging the rational coordinate-permutation symmetry involves `i`; this is consistent with the exact audit cocycle showing only an `S3` base subgroup lifts over `Q`, while all `S4` lifts over `Q(i)`.

## Abelian-cover framework

The seven-line cover identification itself is derived directly from the displayed cuboid equations. For standard terminology/building data for ramified abelian covers use:

- Rita Pardini, *Abelian covers of algebraic varieties*, J. Reine Angew. Math. 417 (1991), 191–213.
- Valery Alexeev and Rita Pardini, *On the existence of ramified abelian covers*, arXiv:1210.6174.

For the canonical divisor, the audit uses finite-cover Riemann--Hurwitz directly: every branch line has inertia order two, so

```text
K_Sbar = pi^*(K_P2 + (1/2)D)
```

as a `Q`-Cartier identity. This avoids requiring the seven-line branch divisor to be simple normal crossing at the six triple points.

These framework sources do not supply a rational-point theorem for the endpoint.

## Cross-check sources already audited upstream

- Horie–Yamauchi, *The L-function of the surface parametrizing cuboids*, arXiv:2512.22520, already audited in Stage29-02e.
- Stage29-02e global coordinate-K3/newform identification: `K_b -> h16`, `K_c -> h32`, `K_a -> h8`.
- Stage29-02f physical-open boundary and Brauer reduction, including the `24/Q + 24/Q(i)` exceptional-node split now independently recovered by the seven-line cover.
- Stage29-02g exact modular `M(4,8)`/Q-descent compression and residual abstract `S4`.

## Novelty boundary

`NEW_IN_REPO=true`: the seven-square-root map to `P^2`, its full `(Z/2)^6` subcover lattice, its use as one common arithmetic torsor for endpoint lifting, and the resulting subcover adapters were not previously a certified Stage29 foundation.

`LITERATURE_NOVELTY_CLAIM=false`: no claim is made that the sign-cover observation itself is new to mathematics. In particular, the published automorphism exact sequence already contains the same sign kernel and `S4` quotient at the automorphism-group level.

```text
SOURCE_LOCK_AUDIT=PASS
TESTA_STOLL_AUT_EXACT_SEQUENCE=PASS
AUT_ORDER_1536=PASS
LITERATURE_NOVELTY_CLAIM=false
```
