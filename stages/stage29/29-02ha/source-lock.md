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

## Abelian-cover framework

The identification below is derived directly from the displayed cuboid equations. For standard terminology/building data for ramified abelian covers use:

- Rita Pardini, *Abelian covers of algebraic varieties*, J. Reine Angew. Math. 417 (1991), 191–213.
- Valery Alexeev and Rita Pardini, *On the existence of ramified abelian covers*, arXiv:1210.6174.

These sources are framework references only; Stage29-02ha does not import a nontrivial rational-point theorem from them.

## Cross-check sources already audited upstream

- Horie–Yamauchi, *The L-function of the surface parametrizing cuboids*, arXiv:2512.22520, already audited in Stage29-02e.
- Stage29-02e global coordinate-K3/newform identification: `K_b -> h16`, `K_c -> h32`, `K_a -> h8`.
- Stage29-02f physical-open boundary and Brauer reduction.
- Stage29-02g exact modular `M(4,8)`/Q-descent compression.

## Novelty boundary

`NEW_IN_REPO=true`: the seven-square-root map to `P^2`, its full `(Z/2)^6` subcover lattice, the six-triple-point explanation of all 48 nodes, and the unification of the seven coordinate K3 quotients are not currently a certified Stage29 foundation.

`LITERATURE_NOVELTY_CLAIM=false`: no claim is made that the observation itself is new to mathematics.
