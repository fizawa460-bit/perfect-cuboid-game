# Stage27-20-r301b — branch geometry comparison

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
PARENT=Stage27-20-r301a

Stage20 third-face completion uses `t1^2+t2^2=square`. Stage27 space completion uses `1+t1^2+t2^2=square`.

Both branch divisors on `Y=Bl_4(P1xP1)` have class `-2K_Y`. Therefore both degree-two covers have trivial canonical class after normalization and resolution. This is a structural match at the divisor-class and K3 level.

The branch equations are nevertheless different. Stage20 factors over `Q(i)` through `t1+i*t2` and `t1-i*t2`; no analogous factorization is claimed for the space-diagonal branch polynomial.

SAME_BASE_HOST=true
SAME_BRANCH_DIVISOR_CLASS=true
SAME_K3_CANONICAL_TYPE=true
SAME_BRANCH_DIVISOR=false
BIRATIONAL_EQUIVALENCE_PROVED=false
STAGE20_LOCAL_DENSITIES_TRANSFER=false
STAGE20_EXPLICIT_BLOCKER_FACTORS_TRANSFER=false

Only structural cover technology may be reconsidered. Any quantitative theorem must be checked again on the actual space-diagonal cover and the same physical height/measure.

STRICT_SUB_SQRT_UPPER_PROVED=false
NEXT_DERIVED_ROUTE=27-20-r301c
