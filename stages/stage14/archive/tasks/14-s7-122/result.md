# Stage14-s7-122 — separate the polynomial outer-pair square-class theorem contract

## Status

`COMPLETE_POLYNOMIAL_OUTER_PAIR_FIBERED_SQUARECLASS_REVERSE_SUPPORT_THEOREM_CONTRACT`

Consumes batch-local `Stage14-s7-120/121`, merged `Stage14-s7-118/119`, and merged `Stage14-Work-cbX40`.

On the remaining active polynomial-pair realization the charged outer variables are

```text
(E,m),
E=B^(epsilon+o(1)),
m=B^(kappa+o(1)),
epsilon>0,
kappa>0,
```

and the square-class host is

```text
z=n=E*m,
M=M_C*n^2.
```

For fixed `n`, the number of factorizations `n=E*m` is at most `tau(n)=B^o(1)`. This preserves fixed-power **multiplicity**, but it does not identify the charged pair measure with a scalar `n` measure because the branch prefilter and residual post-mask may depend on the ordered pair `(E,m)`.

Define

```text
T_pair={
  (E,m) in the charged outer cell :
  C_pre(E,m)=1 and Omega_sq(E,m) != empty
}.
```

Equivalently one may group by the host `n` only as a fibered sum

```text
sum_n sum_{E*m=n} 1_{C_pre(E,m)=1} 1_{Omega_sq(E,m)!=empty},
```

with an inner fiber of size `B^o(1)`. Replacing this by a scalar indicator depending only on `n` would change quantifier location unless pair-independence is separately proved.

Therefore the theorem species required for this branch is

```text
UniformPolynomialOuterPairFiberedFixedSquareClassTwoLevelReverseReciprocalFactorPairSupport.
```

It is distinct from the one-dimensional target of s7-121. A valid theorem may use the `n=Em` host internally, but it must preserve the charged pair baseline, the pair-dependent prefilter, and the existential reverse witness quantifier.

The complete current s receiver is now theorem-contract separated:

```text
1. aligned fixed-E two-sided:
   PARKED UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment;
2. endpoint + fixed-product scalar alternatives:
   UniformOneDimensionalFixedSquareClassTwoLevelReverseReciprocalFactorPairSupport
   then conditional post-mask deficit;
3. polynomial outer-pair alternative:
   UniformPolynomialOuterPairFiberedFixedSquareClassTwoLevelReverseReciprocalFactorPairSupport
   then conditional post-mask deficit.
```

This is a material receiver change. It reaches the s component of Work-cbX40's normal revisit condition (`s7-122 + t158` approximately), but Work should revisit only when the companion t milestone or another earlier trigger is merged.

The theorem targets are now stable enough for the integrated XQ/q route to decide whether q18 is warranted. The s route does not duplicate that literature search as a new sH.

```text
S_POLYNOMIAL_PAIR_FIBERED_THEOREM_TARGET=UniformPolynomialOuterPairFiberedFixedSquareClassTwoLevelReverseReciprocalFactorPairSupport
S_POLYNOMIAL_PAIR_TO_SCALAR_N_SUPPORT_ADAPTER_PROVED=false
S_POLYNOMIAL_PAIR_FIXED_N_FIBER=Bo1
S_POLYNOMIAL_PAIR_FIXED_N_FIBER_RECHARGED=false
S_THEOREM_CONTRACT_SEPARATION_COMPLETE=true
Q18_THEOREM_TARGETS_NOW_STABLE=true
WORK_CBX40_REVISIT_TRIGGER_S7_122_REACHED=true
RECEIVER_MATERIALLY_CHANGED=true
S_ROUTE_H_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT=Stage14-s7-123
```
