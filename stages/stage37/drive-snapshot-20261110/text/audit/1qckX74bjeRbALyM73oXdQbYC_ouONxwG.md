# Stage37 audit — M3-PESCH-TI-002

VERDICT=PASS_WITHIN_SESSION_ADVERSARIAL_REVIEW_OF_EXACT_STRUCTURE
This is an in-session check, not an independently staffed external audit.
RANK_ZERO_FAMILY=NOT_PROVED
WEIGHTED_SAVING=NOT_PROVED
1072_AGGREGATE=HOLD

1. Model identity: the quotient quartic maps birationally, with rational inverse, to Y^2=X(X-alpha)(X-beta); not merely an isogenous curve. Wolfram reduced the residual to zero. Exceptional h=0/infinity points are precisely four two-torsion points. Finite physical h!=0 cannot map to X=0 or Y=0. PASS.
2. Integral minimal model: a1=1, A2=(2beta-alpha-1)/4 and A4=beta(beta-alpha)/16 are integral. Symbolic c4 and discriminant agree with U^4+16V^2W^2 and U^8V^2W^2/16. Odd bad primes and the prime 2 all have unit c4, proving minimal multiplicative reduction; other primes have good reduction. The at-2 proof does not invoke a char!=2 short-Weierstrass lemma. PASS.
3. Torsion exclusion: two lower two-torsion roots have negative differences; halving the upper root requires VW square. Pairwise coprimality and Fermat's area-one descent exclude this. Mazur leaves only groups of size 4 or 12. PASS.
4. Finite-field proof: all good projective source classes over each of 7,11,13,17 are enumerated, including infinity by proving it is bad. Exact point counts contain no factor 3. Only prime-to-q injection is needed, so no false claim that p-primary torsion always injects at every prime. G_tor torsion is exactly size 4. PASS.
5. Mathematical-versus-computational hard locus: initial possible formulation H_TI subset A was narrowed. It is valid for the mathematical complement of the full sufficient TI condition, NOT for an incomplete finite certificate registry. The saved receiver instead derives directly from endpoint => (exceptional or positive rank). UNKNOWN stays UNKNOWN. PASS after this scope correction.
6. Weighted receiver: uses the same symmetric physical mu_B, not unweighted pairs; exceptional positions are bounded by 2 times the exact marginal. Coincident sources have unit total mass. No independence, finite-modulus density, or double credit. PASS.
7. Unproved assertions: no rank values computed; no positive-rank weighted mass bound; fixed 17017 does not make exceptions negligible; no EuV semistability statement; no actual worker validation; 1072 remains HOLD; all closure/saving/nonexistence flags remain false. PASS.

Verification: verify_ti002.py printed the exact projective tables {7:{8:4},11:{8:4,16:4},13:{16:8},17:{16:12}} and 2040 integer/rational diagnostics. Wolfram's exact four polynomial residuals were all zero. The universal proofs are in the card, the bounded integer checks are diagnostics only.

Approved continuation: TI-003, unconditional rank-zero family by exact 2-descent and its physical source weights; torsion exceptional receiver may be refined separately. No need to reread the entire T11 history.
