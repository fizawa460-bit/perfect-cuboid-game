# Stage14 barrier and obstruction atlas

This is a routing document, not a new theorem. Current bound: \(V(B)\ll B^{7/8+o(1)}\).

## Critical shell

Merged s7-13 gives \(E_{\rm support}=1/2+m\) and \(E_{\rm two-cell}=1-m/3\). Their lower envelope is maximal at \(m=3/8\), giving \(7/8\), with
\[
P,Q\asymp B^{1/2},\quad a,b\asymp B^{3/8},\quad x,y\asymp B^{1/16},\quad \xi=ab\asymp B^{3/4}.
\]

| ID | obstruction | status | next receiver | forbidden shortcut |
|---|---|---|---|---|
| O1 | coordinate/two-cell minimax equality | LIVE | transverse label on the same block | multiply the two bounds |
| O2 | xi-only critical support | CLOSED AS ROUTE | use \(k=\ker(Q^2-P^2)\) | claim xi power sparsity from four cells |
| O3 | \(k\le B^{3/4-\delta}\) | CLOSED | \(B^{(1+\kappa)/2+o(1)}\) shell bound | promote shell bound globally |
| O4 | critical \((\xi,k)\) off-diagonal collisions | LIVE | centered collision second moment | use raw energy without diagonal subtraction |
| O5 | auxiliary bad primes | CLOSED | import t50 | reopen bad-prime bookkeeping |
| O6 | sparse physical two-prime selector | LIVE | selector-sensitive off-diagonal Gaussian dispersion | infer sparse cancellation from complete sums |
| O7 | exact-pair diagonal | CLOSED at alias-free scale | keep diagonal separated | pair-collapse before angular completion |

The unique live intersection is O4 + O6. Main/s owns physical \((\xi,k)\) incidence; t/tH owns the selector-sensitive two-prime second moment; toolbox owns routing only.

Sources: s7-13 PR #434 merge \`079d053d1182e82a1924b37bba9ae33a3907f031\`; t50 PR #439 merge \`72dd462552e64c312c13746f4533c5ef7512d52a\`; 4cc PR #441 merge \`f37b31c9e23462dd184af60c1811175e6759b981\`.
