Stage35EX C35-09: independent direct O_K/8 square-coset 2-Selmer intersection.
Dependencies: Python 3, SymPy. No Magma/PARI. No GitHub.

Execute: python c35_09_direct_q2_coset_audit.py
Expected:
 EXPLICIT_Q2_QUADRATIC_WITNESS_HENSEL_PASS
 DIRECT_Q2_4_WITNESSES_INDEPENDENT_PASS
 EXACT_RATIONAL_INTERVAL_REAL_SIGNS_PASS
 FULL_DIRECT_Q2_COSET_AND_INDEPENDENT_P3461_SURVIVORS [0, 3, 5, 6]
 PASS_DIRECT_2ADIC_SQUARE_COSET_SEL2_DIM2

Core new direct Q2 test: enumerate 4096 elements in O/4 to get square-unit
subgroup SQ8 subset (O/8)^* of size 1536, then test candidate classes by
membership in SQ8 itself instead of any randomized/greedy squareclass basis.
There are 196608 unit residues and 128 quotient unit classes. Four
explicit local classes give 16 distinct cosets; local Jacobian 2-Kummer
image dimension is theoretically 4, so these span. 2 quadratic divisor
witnesses are proved square using mod16 and local Hensel.
Sign evaluations use exact rational isolating intervals (not floats).
3461 character values use earlier independent mod-3461 residue-field map,
without any lifted factorization. The 7 global S-unit generators were
separately verified from Wolfram fundamental units and Minkowski h_K=1.

Inputs kfield.py,c3_selmer.py,independent_3461.py copied unchanged from
prior Stage35EX C35-03/C35-07 bundle. c3_selmer.py is used ONLY for
exact number-field norm/arithmetic and point_image and the finite-field
independent_3461 module; its vec_2/coords_unit2, sample divisors, and
full Selmer code are NOT invoked by the new verification.

This is a rigorous finite certificate conditional on standard 2-descent
identifications and correctness of exact Jacobian Kummer maps; it does
not certify the upstream perfect-cuboid physical source adapter.
