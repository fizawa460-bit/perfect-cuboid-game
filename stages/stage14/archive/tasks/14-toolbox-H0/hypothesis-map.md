# Stage14-toolbox-H0 — connection hypothesis map

Scope: independent adversarial audit of the connection between the merged centered `(xi,k)` collision receiver and the merged selector-sensitive two-auxiliary Gaussian dispersion receiver. This H-line consumes merged sources only and claims no new Stage14 theorem.

## Objects being connected

For fixed critical `xi`, the s-side unit-weight collision target is

\[
C_{\rm off}(\xi)=\sum_k r_\xi(k)(r_\xi(k)-1).
\]

Merged s7-15 obtains it from a character amplifier by

\[
C_{\rm off}(\xi)(P-2b)^2\le R_k(\xi),
\qquad
R_k(\xi)=\sum_{s\ne t}\left|\sum_{p\in\mathcal P}c_s^{(k)}(p)c_t^{(k)}(p)\right|^2,
\]

with `c_s^(k)(p)=(k_s/p)` on good primes.

The t/tH Gaussian receiver instead uses

\[
c_z^{(G)}(p)=1_{\rm good(z,p)}\chi_p(\widetilde F(z))
\]

and a signed physical coefficient family `a_z`. Merged toolbox-ao correctly aligns the bookkeeping space and diagonal vocabulary, but that alignment by itself is not an implication from a Gaussian estimate to `C_off`.

## Minimal connection hypotheses

### H0-C1 — physical-state lift is exact
There must be an injective or multiplicity-controlled map from each s-side physical state to one retained Gaussian label `z`, preserving `xi`, `k`, branch/orientation, interval/reconstruction masks, and the exact state diagonal. A representational lift may not create or delete same-`(xi,k)` pairs by a fixed power of `B`.

### H0-C2 — collision specialization is positive
To recover the unit-weight combinatorial collision count, the Gaussian quadratic form must be evaluated on the unit/nonnegative physical specialization, or one must prove an explicit positive-semidefinite domination. Arbitrary signed `a_z` are insufficient: signed cross-terms can cancel the same-`k` contribution.

A sufficient specialization is `a_z=1` for the physical states in one fixed `xi` collision packet. More generally, all same-`k` coefficients must have a common phase and cross-`k` terms must not destroy the lower bound.

### H0-C3 — same-k Gaussian row coherence
For every off-diagonal pair with the same `(xi,k)`, the actual Gaussian rows must satisfy

\[
\left|\sum_{p\in\mathcal P}c_z^{(G)}(p)c_{z'}^{(G)}(p)\right|\ge (1-o(1))P.
\]

A clean sufficient condition is an exact squareclass bridge

\[
\chi_p(\widetilde F(z))=\eta_{\xi}(p)\,(k(z)/p)
\]

for all good active primes, where `eta_xi(p)` is independent of the state inside the fixed `xi` packet. Then same `k` implies identical Gaussian rows after the common twist. No such identity is supplied merely by putting the two objects in the same coefficient space.

### H0-C4 — bad-prime budget remains sublinear
The union of selector/denominator/ramification exclusions for a same-`k` pair must satisfy `b=o(P)`, so the amplifier lower bound remains `(P-2b)^2=P^2(1-o(1))`.

### H0-C5 — exact diagonal alignment, once only
The `D_xi(p,q)` subtraction used by the centered collision receiver must be the exact physical state diagonal after the H0-C1 lift. It is subtracted exactly once. The oriented residue diagonal closed by t51/tH14 is a separate relation and must not be subtracted again as though it were the state diagonal. Principal squareclass coherence is not a diagonal.

### H0-C6 — the theorem must be centered at the s-scale
The raw Gaussian target

\[
\mathcal M\ll P^2E_A B^{o(1)}
\]

has natural size `H_xi P^2` for unit weights. The s receiver needs instead a diagonal-subtracted estimate of size

\[
R_G(\xi)\ll H_\xi^2 P B^{o(1)}
\]

(or any quantitatively equivalent estimate yielding a fixed power saving after division by `P^2`). When `P>H_xi`, the raw natural-scale theorem is strictly weaker by the factor `P/H_xi` and does not imply the centered theorem.

At the s7-15 critical exponents `H_xi<=B^(1/8+o(1))` and `P=B^(1/7+o(1))`, this missing factor is exactly

\[
B^{1/7-1/8}=B^{1/56}.
\]

### H0-C7 — auxiliary-prime family compatibility
The estimate used for the implication must apply to the same active prime family. The merged t/tH Gaussian receiver is formulated for split primes, while s7-16's exact local Fourier self-duality is on inert primes. The inert local theorem cannot be inserted into the split Gaussian mean square without a proved prime-family transfer or a reformulation on a common family. The earlier s7-15 abstract amplifier can use split primes, so this is a restriction on importing s7-16 local cancellation, not on the existence of the collision amplifier itself.

### H0-C8 — conductor/scale compatibility for the tH14 R2 QLS adapter
Merged tH14 R2 proves

\[
\mathcal M\ll (K+L^2)E_{\rm sq}B^{o(1)}
\]

and requires `2rho>=d` when `K<=B^(d+o(1))`, `L=B^rho`. With the current safe `d=4`, the adapter requires `rho>=2`; it therefore does not directly supply a theorem at the s7-15 conditional scale `rho=1/7`. To use the QLS adapter exactly at `rho=1/7` would require a block conductor `d<=2/7`, or a different mean-square theorem.

### H0-C9 — noncircular squareclass control
The R2 input

\[
E_{\rm sq}\ll E_A B^{o(1)}
\]

cannot be assumed when it specializes to the principal squareclass collision energy `A1` that the Stage14 Frobenius route is trying to control. A Gaussian theorem used to close the centered `(xi,k)` receiver must obtain its selector/squareclass anti-coherence from independent physical geometry, not from the target collision energy under another name.

### H0-C10 — order and masks are preserved
The merged ao gates remain mandatory: signed common-refinement aggregation, shared `U/V` modulus group, divisor-coupled hyperbola, canonical/physical selector, branch/interval/reconstruction masks, distinct auxiliary primes, and angular completion before any ordered-pair cross-kernel collapse.

## Implication certificate

A safe implication has the following form.

1. Specialize the Gaussian theorem to the exact unit-weight physical states of one fixed critical `xi` packet (`C1`,`C2`).
2. Use a proved statewise character bridge to get same-`k` Gaussian row coherence (`C3`,`C4`).
3. Subtract only the exact state diagonal (`C5`).
4. Apply a genuinely centered Gaussian dispersion bound at `H_xi^2 P` scale (`C6`) on the same prime family and admissible scale (`C7`,`C8`).
5. Ensure the proof of that bound does not import principal/squareclass energy circularly (`C9`) and preserves the physical masks/order (`C10`).

Then

\[
C_{\rm off}(\xi)P^2(1-o(1))\le R_G(\xi)\ll H_\xi^2P B^{o(1)},
\]

so

\[
C_{\rm off}(\xi)\ll H_\xi^2P^{-1}B^{o(1)}.
\]

Without all of `C1`-`C10`, the merged sources establish compatibility of bookkeeping, not a proved collision-to-Gaussian implication.
