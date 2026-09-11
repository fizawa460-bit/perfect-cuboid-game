# N357 to 32-02 scalar producer gap

N357 RESULT V1 is an aggregate census: it has counts, cut data and stream commitments but no per-survivor integral Picard witness. Therefore N=-y^2 is not derivable from it.

A producer record must source-lock row_id, terminal_identity, d, m=16/gcd(d,16), integral Picard witness identity, exact pairing/Gram provenance sufficient to compute y=mC-nH, and negative_hperp_square_N. The consumer recomputes N from the locked witness; an asserted N alone is rejected.

This is a bridge-only finding: it grants no N357/CUT/MAIN/FULL178/effectivity credit.
