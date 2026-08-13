# Stage14-s7-121 — normalize the two scalar branches to one theorem species

## Status

`COMPLETE_ONE_DIMENSIONAL_SQUARECLASS_REVERSE_SUPPORT_THEOREM_CONTRACT`

Consumes batch-local `Stage14-s7-120`, merged `Stage14-s7-118/119`, and merged `Stage14-Work-cbX40`.

The two one-dimensional active realizations are:

```text
A. fixed-E endpoint: z=t,
   M=M_A*t^2;
B. polynomial-E fixed primitive product: z=E,
   M=M_B*E^2.
```

After freezing the packet coefficients, each branch has exactly one charged scalar `z` in a dyadic/physical interval `I`, a deterministic prefilter `C_pre(z)`, and the same reverse kernel species

```text
W2(z)=D2*z^2,
F2^-*F2^+=W2(z),
cp=(F2^++F2^-)/2,
dq=(F2^+-F2^-)/2,
cp=c*p,
dq=d*q,
W1=D1*p*q,
F1^-*F1^+=W1,
F1^++F1^- == 0 (mod 2U),
F1^+-F1^- == 0 (mod 2V),
```

with all parity, positivity, gcd, endpoint-small and frozen packet filters retained.

Define the bare scalar support

```text
T_1d={z in I : C_pre(z)=1 and Omega_sq(z) != empty}.
```

The theorem species required to control `delta_sq` on either scalar realization is therefore

```text
UniformOneDimensionalFixedSquareClassTwoLevelReverseReciprocalFactorPairSupport.
```

Uniformity must include all frozen Stage14 coefficient cells and the actual physical interval; a theorem for unrestricted divisors, average coefficients, or a different charged measure is insufficient.

This is one theorem **species**, not an identification of the two branch counts. Their coefficients and residual post-masks remain branch-specific. Any later full physical theorem must separately account for

```text
delta_post
```

on the support `T_1d`.

No claim is made that the bare support has full exponent or a fixed-power deficit. No generic divisor/square-class density is inserted.

```text
S_ONE_DIMENSIONAL_BRANCHES_COMMON_THEOREM_SPECIES=true
S_ONE_DIMENSIONAL_THEOREM_TARGET=UniformOneDimensionalFixedSquareClassTwoLevelReverseReciprocalFactorPairSupport
S_ONE_DIMENSIONAL_BARE_FULL_EXPONENT_PROVED=false
S_ONE_DIMENSIONAL_BARE_FIXED_POWER_DEFICIT_PROVED=false
S_ONE_DIMENSIONAL_POSTMASK_AUTOMATIC=false
S_ONE_DIMENSIONAL_BRANCH_COUNTS_IDENTIFIED=false
S_ROUTE_H_NEEDED=false
RECEIVER_MATERIALLY_CHANGED=false
NEXT=Stage14-s7-122
```
