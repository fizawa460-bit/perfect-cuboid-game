# Stage32 post1648T scratch source note — KRR official ancillary does not materialize the marked conjugating g

This leaf is scratch-only and grants no MAIN or arithmetic credit. Its negative conclusion is deliberately bounded to the official arXiv v4 ancillary inventory for Koziarz–Rito–Roulleau, *The Bolza curve and some orbifold ball quotient surfaces* (arXiv:1904.00793v4).

The arXiv record lists exactly one ancillary file, `Magma_KRR.pdf`. The paper itself says the auxiliary file contains only the Magma code used in Sections 5 and 6. Inspection of the complete two-page ancillary confirms that it contains a `// Section 5.3:` block followed by a `// Section 6.1:` block. The first block performs elimination and incidence/tangency calculations for the plane quartic model; the second constructs the Section 6.1 projective maps and curve computations.

The Section 4 conjugacy used by Stage32 is not computed in this ancillary. In particular, this official ancillary does not materialize an explicit automorphism `g` with `H48=g G48 g^-1`, a matrix for `g` on homology or `A[2]`, a KKK-canonical-basis change, a branch-point-to-half-characteristic table, or a marked theta-divisor normalization.

This is consistent with the main paper: Corollary 6 states existence of an automorphism `g` inducing the conjugacy, and the paragraph after Proposition 7 says one may change the embedding by composing with `g` and then identify `H48` with `G48`; it does not supply the marked matrix needed by Stage32 at that locator.

Therefore the specific proposed route “recover the actual KRR conjugating g from `Magma_KRR.pdf` / the official v4 ancillary” is closed as a bounded source-negative leaf. This does **not** prove that no explicit marked conjugacy exists elsewhere. The remaining load-bearing datum is still non-inner-conjugacy-invariant marked ppav information: an actual source-bound conjugating element, explicit branch-point → half-characteristic marking in the chosen canonical cycle basis, marked theta divisor, or equivalent absolute ppav normalization.

External locators checked:
- arXiv:1904.00793v4 record, ancillary-file inventory (`Magma_KRR.pdf`);
- `https://arxiv.org/src/1904.00793v4/anc/Magma_KRR.pdf`, complete 2-page ancillary;
- KRR Section 4, Corollary 6 and the paragraph following Proposition 7.
