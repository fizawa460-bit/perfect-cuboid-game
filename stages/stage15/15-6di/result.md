# Stage15-6di — exact reconstructed-graph packet and discrepancy

Base: merged Stage15-6dh after fresh audit PASS. Execute `ROOT_RATIO_DISCREPANCY_DISPERSION_ON_THE_RECONSTRUCTED_GRAPH` without importing any Stage14 fixed-packet exponent.

Keep the exact cross-gcd-cell normal form
\[
m=abM,\quad n=cdN,\quad r=acU,\quad s=bdV,
\qquad H=abcd,
\]
with pairwise-coprime cells, physical cutoff `R<=B`, exact product-height consequence
\[
HMNUV\le B,
\]
and exact survivor equations
\[
a^4M^2U^2+d^4N^2V^2=kP^2,
\qquad
b^4M^2V^2+c^4N^2U^2=kQ^2.
\]
Put `g=gcd(P,Q)`. Stage15-6df gives
\[
kg^2\mid \Delta,\qquad \Delta=(abM)^4-(cdN)^4,
\]
and `gcd(kg,HMNUV)=1`.

## 1. Exact graph nodes after 6da

A reconstructed graph node is the data

```text
x=(a,b,c,d; M,N,U; completion label nu; V,k,P,Q,g; physical masks)
```

such that:

- `(a,b,c,d)` is a legal cross-gcd cell package;
- `(M,N,U)` is a residual base triple;
- `nu` chooses one of the `B^o(1)` exact fourth-variable completions supplied by Stage15-6da;
- the resulting `(V,k,P,Q,g)` satisfies both exact survivor norm equations and `kg^2|Delta`;
- `R<=B`, `HMNUV<=B`, primitivity, positivity, exactly-two, canonical-order and direction masks all hold.

Thus the completion label is a subpolynomial decoration, not an independent fourth polynomial support.

Let `G(P)` denote one legal dyadic/physical graph packet, obtained by fixing the cell package and dyadic ranges for the residual base variables while retaining the exact masks. No replacement of `R<=B` by an unrestricted box is made.

## 2. Switched modulus and legal orientations

For each graph node define
\[
G_S=\gcd(m^2+n^2,r^2-s^2),
\qquad
G_O=\gcd(m^2-n^2,r^2+s^2).
\]
Fix switched divisors
\[
d_S\mid G_S,\qquad e_O\mid G_O,
\qquad q=d_Se_O.
\]
Stage15-6ct gives
\[
(q,H)=1.
\]
For every odd prime power in `d_S`, choose a legal root/sign orientation
\[
m/n\equiv \rho_S,\quad \rho_S^2\equiv-1,
\qquad r/s\equiv \epsilon_S,\quad \epsilon_S\in\{\pm1\};
\]
for every odd prime power in `e_O`, choose
\[
m/n\equiv \epsilon_O,\quad \epsilon_O\in\{\pm1\},
\qquad r/s\equiv \rho_O,\quad \rho_O^2\equiv-1.
\]
CRT gives one primitive residue line for `(m,n)` and one for `(r,s)` modulo `q`. Let `omega` denote the resulting legal composite orientation. The number of legal orientations is `q^{o(1)}` and every node satisfying `d_S|G_S,e_O|G_O` belongs to exactly one such orientation, up to the already-isolated bounded 2-adic convention.

## 3. Local count, main density and discrepancy

Define
\[
N_{d_S,e_O,\omega}(P)
:=\#\{x\in G(P):x\text{ lies in orientation }\omega\bmod q\}.
\]
For one fixed primitive orientation, the ambient two-pair root-line density is exactly `q^{-2}`. We therefore **define**, without assuming equidistribution of the reconstructed graph,
\[
M_{d_S,e_O,\omega}(P):=\frac{|G(P)|}{q^2},
\]
\[
\boxed{D_{d_S,e_O,\omega}(P)
:=N_{d_S,e_O,\omega}(P)-\frac{|G(P)|}{q^2}.}
\]
The equality is a definition of the discrepancy, not a claim that the graph already has density `q^{-2}`.

Summing over legal orientations recovers the exact switched count:
\[
N_{d_S,e_O}(P)=\sum_{\omega}N_{d_S,e_O,\omega}(P).
\]
Hence
\[
N_{d_S,e_O}(P)
=\frac{\Omega(d_S,e_O)}{q^2}|G(P)|
+\sum_{\omega}D_{d_S,e_O,\omega}(P),
\]
where `Omega(d_S,e_O)=q^{o(1)}` is the exact legal orientation count. No orientation is charged twice.

## 4. Exact weighted small-range error

For a modulus ceiling `Q0`, retain the exact repaired divisor weights
\[
\lambda(d_S,e_O)=\varphi(d_S)\varphi(e_O).
\]
The graph-packet discrepancy contribution is
\[
\boxed{
E_P(Q_0)
:=\sum_{d_Se_O\le Q_0}
\lambda(d_S,e_O)
\sum_{\omega}D_{d_S,e_O,\omega}(P).
}
\]
This is the quantity on which cancellation must be taken **before absolute values**. The exact `phi(d_S)phi(e_O)` weights are preserved.

The previous conditional local profile `beta=-1` is compatible with this normalization: the main density has two root-line factors `q^{-2}`, while the divisor weight has size at most `q`, leaving the same weighted `q^{-1+o(1)}` scale after orientation summation.

## 5. Measure and charging audit

- `R<=B` remains the physical population definition.
- `HMNUV<=B` is used only as an exact consequence/majorant, never as a replacement population.
- `(q,H)=1` is retained before local root-line counting.
- `kg^2|Delta` remains attached to every graph node.
- the Stage15-6da completion multiplicity is used once as a graph decoration and not charged as a power saving;
- `phi(d_S)phi(e_O)` weights remain exact;
- no Stage14 Type-II, large-sieve, spacing or spectral exponent is imported.

```text
STAGE15_6_SUBSTAGE=6di
STAGE15_6DI_RECONSTRUCTED_GRAPH_PACKET_EXACT=true
STAGE15_6DI_COMPLETION_LABEL_MULTIPLICITY=B^o(1)
STAGE15_6DI_PHYSICAL_R_LE_B_PRESERVED=true
STAGE15_6DI_HMNUV_LE_B_PRESERVED=true
STAGE15_6DI_Q_COPRIME_H=true
STAGE15_6DI_KG2_DIVIDES_DELTA=true
STAGE15_6DI_LOCAL_MAIN_DENSITY_PER_ORIENTATION=q^-2
STAGE15_6DI_DISCREPANCY_DEFINED=true
STAGE15_6DI_EXACT_PHI_WEIGHTS_PRESERVED=true
STAGE15_6DI_AVERAGE_BEFORE_ABSOLUTE_VALUES=true
STAGE15_6DI_EXIT=WHOLE_FAMILY_SECOND_MOMENT_READY
```