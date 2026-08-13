# Stage14-s7-159 — unit-character principal-domination normal form

## Status

`COMPLETE_UNIT_CHARACTER_PRINCIPAL_DOMINATION_NORMAL_FORM`

Consumes merged Stage14-s7-156..158 and merged Work-cmX51/q25.

On the exact unit stratum

```text
Q=2UV,
gcd(W1(lambda),Q)=1,
f*n=W1(lambda),
r=n*f^{-1} (mod Q).
```

The q17 CRT conditions give one fixed unit residue `rho0 (mod Q)` determined by

```text
rho0 == -1 (mod 2U),
rho0 == +1 (mod 2V).
```

For the retained nonnegative allocation weight `w(lambda;f,n)`, define

```text
A_0 := sum_{lambda,f,n} w(lambda;f,n)
```

over the unit stratum before imposing `r=rho0`, and for every Dirichlet character `chi (mod Q)`

```text
A_chi := sum_{lambda,f,n} w(lambda;f,n) chi(n*f^{-1}).
```

Exact character orthogonality gives

```text
J_unit
 = (1/phi(Q)) * sum_chi conjugate(chi(rho0)) A_chi
 = P_unit + E_unit,
P_unit := A_0/phi(Q),
E_unit := (1/phi(Q))*sum_{chi != 1} conjugate(chi(rho0)) A_chi.
```

This is an exact signed decomposition. The common-core average and the scalar versus `(E,m)` charged measures remain inside every `A_chi`.

Therefore the q25 unit test does not require a new support multiplicity estimate. Its precise sufficient input is

```text
|E_unit| <= (1-epsilon_B) P_unit
```

with `epsilon_B` large enough for the required fixed-power survival on the principal cell. Equivalently, one may prove an aggregate nonprincipal bound directly; bounding each character separately and summing is only sufficient and is not assumed lossless.

No cancellation estimate is proved here.

```text
Q25_UNIT_CHARACTER_PRINCIPAL_DOMINATION_NORMAL_FORM_TEST=PASS_EXACT_PRINCIPAL_PLUS_NONPRINCIPAL_DISCREPANCY
UNIT_CHARACTER_PRINCIPAL_NONPRINCIPAL_EXACT_DECOMPOSITION_PROVED=true
UNIT_CHARACTER_AGGREGATE_DISCREPANCY_BOUND_PROVED=false
COMMON_CORE_AVERAGE_MUST_BE_RETAINED=true
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
S_ROUTE_H_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT=Stage14-s7-160
```