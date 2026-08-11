# Stage14-t121 — trace generic physical norm support to the finite sign/canonical selector

## Status

`COMPLETE_GENERIC_NORM_SUPPORT_SELECTOR_TRACE_TO_SIGN_CANONICAL_BOOLEAN`

Consumes merged `Stage14-t120`, merged `Stage14-t90/t91`, and merged `Stage14-t116`.

Fix one t120 exceptional multiplier/local packet

```text
(m,e_loc),
```

and write the scalar cofactor norm as

```text
n=m*g,
gcd(g,E_U)=1,
all odd p|g => p==1 mod 4.
```

For one primitive generic orientation label `epsilon in F_g`, write

```text
gamma = gamma_E * gamma_G(epsilon),
W_sigma = a*gamma = p-i*sigma*q.
```

Merged t90 gives the exact fixed-packet selector list before the endpoint projective condition is separated:

```text
P_prim * P_tag * P_cell * P_proj * P_sign.
```

The descendants consumed by t120 discharge these factors as follows.

- `P_proj` is the moving dominant-prime selector isolated by t109--t114 and is not part of the ell-independent norm-support Boolean.
- `P_prim` is automatic on the primitive orientation cube by merged t91.
- every nontrivial local interaction of `P_tag` and `P_cell` with cofactor primes is supported on `E_U` by merged t91; after `(m,e_loc)` is fixed, those local predicates are fixed constants.
- reciprocal/inversion orientation is already frozen in the packet.

Therefore there is no additional unnamed good-prime local selector left inside the t120 Boolean.  The remaining generic-orientation acceptance is exactly the finite sign/positivity/canonical-normalization predicate inherited from t90:

```text
S_{m,e_loc}(g,epsilon)
 = P_sign(U;a,gamma_E*gamma_G(epsilon)).
```

The finite Gaussian unit, conjugation and two-primary normalization labels used to define the canonical representative were previously absorbed into the exceptional label at `O(1)` cost.  Re-expose that finite symmetry label as

```text
nu in D_U,
|D_U|=O(1),
```

without changing any polynomial exponent.  Then the exact full norm-support condition is

```text
g in G_phys(m,e_loc)
<=>
exists epsilon in F_g,
exists nu in D_U:
P_sign(nu · a*gamma_E*gamma_G(epsilon))=1.
```

This step does not assert that the sign selector is automatic.  It only identifies it as the sole remaining ell-independent generic support Boolean and restores its finite symmetry orbit explicitly.

```text
GENERIC_GOOD_PRIME_UNNAMED_LOCAL_SELECTOR_REMAINS=false
PROJECTIVE_SELECTOR_EXCLUDED_FROM_CORE_SUPPORT=true
PRIMITIVE_SELECTOR_AUTOMATIC_ON_GENERIC_ORIENTATION_CUBE=true
TAG_CELL_GENERIC_LOCAL_INTERACTIONS_ALREADY_FROZEN=true
GENERIC_NORM_SUPPORT_BOOLEAN_EQUALS_SIGN_CANONICAL_EXISTENCE=true
FINITE_GAUSSIAN_SYMMETRY_LABEL_REEXPOSED=true
FINITE_GAUSSIAN_SYMMETRY_LABEL_COUNT=O1
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
PREFERRED_RECEIVER=SharedUGenericSplitPrimeNormFiniteGaussianSignCanonicalSupportOrSelectedProjectiveClassNearTotalDepletion
NEXT_INTERNAL_TARGET=FiniteGaussianSymmetryCanonicalChamberCoverage
NEXT=Stage14-t122
```
