# Stage14 collision/dispersion interface and diagonal-subtraction dictionary

This document is a reusable routing contract. It proves no new global second-moment theorem.

## Common coefficient space

Let \(R\) range over disjoint common-refinement blocks and let
\[
z=(R,\xi,k,U,V,\mathfrak b,\mathfrak i,\mathfrak r)
\]
be the exact physical label, including branch, interval and reconstruction masks. Write its signed coefficient as \(a_z\). All transforms below retain the shared \(U/V\) modulus group, divisor-coupled hyperbola, canonical selector and distinct split auxiliary primes \(p\ne q\). Angular completion is performed before any state-pair collapse.

For a fixed critical \(\xi\)-block let
\[
c_z(p)=1_{\mathrm{good}(z,p)}\chi_p(\widetilde F(z)),\qquad
G_\xi(p,q)=\sum_z a_z c_z(p)c_z(q),
\]
and
\[
D_\xi(p,q)=\sum_z |a_z|^2c_z(p)^2c_z(q)^2.
\]
Then the diagonal-subtracted object is
\[
R_{\mathrm{cent}}(\xi)=\sum_{p,q}\left(|G_\xi(p,q)|^2-D_\xi(p,q)\right)
 =\sum_{z\ne z'}a_z\overline{a_{z'}}
 \left|\sum_p c_z(p)c_{z'}(p)\right|^2.
\]
The last identity is algebraic and remains signed; it is not a positivity claim for each \((p,q)\)-summand.

## Dictionary

| object | diagonal removed | owner / receiver | admissible use |
|---|---|---|---|
| raw fiber energy \(\sum_k|\sum_{z:k(z)=k}a_z|^2\) | none | main/s geometry | localization only |
| collision energy \(C_{\rm off}=\sum_k(r_k^2-r_k)\) for unit weights | exact state diagonal | centered \((\xi,k)\) receiver | lower-bound by amplifier correlation |
| \(R_{\rm cent}(\xi)\) | exact \(z=z'\) contribution \(D_\xi\) | DualSplitKCenteredDispersion | joint \(p,q\) average; never moduluswise absolute completion |
| residue diagonal | equal oriented \((U,V)\bmod pq\) | t51/tH14 | alias-free exact-pair energy; closed at target scale |
| principal squareclass coherence | none after residue cleanup | t/tH principal Kummer incidence | remains open; cannot be called a diagonal |
| nonprincipal selector dispersion | residue and principal pieces separated | t/tH selector receiver | remains open |
| complete angular trace | finite-field complete family | t32 local input | cannot replace the physical sparse selector |

## Adapter contract

**Input from main/s.** A critical packet with \(\xi\asymp B^{3/4}\), \(k\ge B^{3/4-o(1)}\), exact physical labels and the centered identity above. Main/s may use a proved bound for \(R_{\rm cent}\) to control \(C_{\rm off}\), but may not substitute a raw near-linear energy estimate.

**Input from t/tH.** The two-prime second moment is decomposed into: (i) closed residue diagonal, (ii) global principal squareclass component, and (iii) nonprincipal selector dispersion. The latter two are not closed by tH14 R2 or t52/t53.

**Interface output.** A theorem may cross the interface only if it bounds the same signed coefficient space after exact-diagonal subtraction and preserves all physical masks. A theorem that first takes absolute values blockwise, tensorizes \(U\) and \(V\), collapses to a cross-kernel, or replaces the selector by a complete family is rejected.

## Non-circularity gates

1. \`G1\`: exact \(z=z'\) diagonal is subtracted once, and only once.
2. \`G2\`: residue diagonal is not identified with principal squareclass coherence.
3. \`G3\`: \`PhysicalWeightedSquareclassFiberEnergy\` is not imported as an input to prove itself.
4. \`G4\`: \`DualSplitKCenteredDispersion\` is not inferred from per-modulus absolute completion.
5. \`G5\`: complete angular cancellation precedes pair collapse.
6. \`G6\`: signed common-refinement aggregation stays inside the norm.
7. \`G7\`: shared \(U/V\), divisor hyperbola and all physical selectors remain attached.

A failed gate routes back to its owner and does not block toolbox main.

## Current boundary

The adapter aligns the two live descriptions but does not merge them into one proved estimate. In particular, centered \((\xi,k)\) dispersion, global principal Kummer incidence, and nonprincipal selector dispersion remain separate open arithmetic inputs. The unconditional whole-family exponent stays \(7/8\).
