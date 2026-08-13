# Stage14-t107 — expose split-prime orientation witnesses inside Q support

## Status

`COMPLETE_Q_SUPPORT_ORIENTATION_WITNESS_DECOMPOSITION`

Consumes Stage14-t106 on the same batch branch together with merged Stage14-t91.

Write

```text
delta0 = delta_E * delta_G,
delta_E=gcd(delta0,E_U^infinity),
```

where merged t91 proves that `delta_E` has only `B^o(1)` exceptional orientation labels, while every odd split prime power dividing `delta_G` contributes exactly one binary primitive Gaussian orientation bit.

After freezing one fixed norm-`k0` factor, unit convention, reciprocal/inversion orientation, and one exceptional label `e`, every remaining background label over Q is determined by

```text
epsilon in {0,1}^{omega(delta_G)}.
```

Let `A_{Q,e}(epsilon)` be the exact full physical Boolean acceptance predicate inherited from t105. Then

```text
omega_B(Q)>0
<=>
exists e in E(Q), exists epsilon:
A_{Q,e}(epsilon)=1,
```

where

```text
|E(Q)|=B^o(1),
2^{omega(delta_G)}=B^o(1).
```

Hence the scalar support can be written exactly as a finite/subpolynomial union of primitive split-prime orientation witness projections. The fixed denominator tag, endpoint conductor support, and fixed four-cell bad-prime data are already localized in `delta_E`; generic split-prime orientation bits introduce no further fixed-packet local entropy.

```text
Q_SUPPORT_EXPANDED_TO_ORIENTATION_WITNESS_EXISTENCE=true
EXCEPTIONAL_ORIENTATION_LABEL_COUNT=Bo1
GENERIC_ORIENTATION_CUBE_SIZE=Bo1
GENERIC_FIXED_PACKET_LOCAL_ENTROPY_REMOVED=true
Q_DEPENDENT_ARBITRARY_WEIGHT_AS_ANALYTIC_OBJECT_REMOVED=true
GLOBAL_ORIENTATION_ACCEPTANCE_CORRELATION_REMAINS=true
FIXED_U_Q_SUPPORT_SPARSE_POWER_PROVED=false
```

No multiplicativity, Fourier-degree bound, or cancellation is asserted for `A_{Q,e}`. This stage only exposes the exact witness variables hidden by the t105 weight.

## tH decision

The live obstruction is still an exact finite witness predicate rather than a theorem-ready outer arithmetic family.

```text
TH28_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PREFERRED_RECEIVER=SharedUCanonicalLPFBoundaryBearingSplitPrimeOrientationWitnessSupport
NEXT=Stage14-t108
```
