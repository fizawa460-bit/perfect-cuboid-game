# Stage27-20-r302d — naive CRT compression is exponent-neutral on the critical wall

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_WALL_FIRST_MOMENT
PARENT_ROUTE=Stage27-20-r302a-c
SOURCE_STAGE=Stage20

The r302a MAIN receiver retains

\[
G_-f^2\equiv-G_+N\pmod{2U},\qquad
G_-f^2\equiv G_+N\pmod{2V},
\]
with the frozen Stage14 primitive rectangle relation
\[
\gcd(U,V)=1.
\]
Hence the odd parts of the two moduli are coprime. Combining the simultaneous congruences by CRT can at most replace the pair by one compatible residue condition modulo their lcm, with only the already-recorded 2-primary compatibility state shared between them.

This does not create a new support saving. Stage14 final already proves, in the reverse reciprocal reconstruction, that the later row CRT conditions are filters on a divisor-many reconstructed set and explicitly states that the row CRT lift is not an independent support variable. Therefore treating the combined modulus as a new density factor would recharge a constraint already internal to the complete host ledger.

So the route

`two root congruences -> one larger CRT modulus -> divide the host by the modulus`

is invalid as a new fixed-power argument unless one first proves a genuinely new occupancy/correlation theorem in the original physical measure. Mere algebraic CRT repackaging has fixed-power exponent zero.

```text
STAGE27_20_R302D_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
PRIMITIVE_RECTANGLE_GCD_U_V_ONE_REUSED=true
NAIVE_TWO_ROOT_CRT_COMPRESSION_DERIVED=true
CRT_COMPRESSION_NEW_INDEPENDENT_SUPPORT=false
ROW_CRT_ALREADY_INTERNAL_TO_STAGE14_RECONSTRUCTION=true
STAGE14_LEDGER_RECHARGED=false
NAIVE_CRT_FIXED_POWER_DEFICIT_PROVED=false
NAIVE_CRT_COMPRESSION_ROUTE_CLOSED=true
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-20-r302e
```
