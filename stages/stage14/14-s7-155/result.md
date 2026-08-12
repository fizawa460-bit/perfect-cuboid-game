# Stage14-s7-155 — freeze common-core / coprime-side joint-incidence receiver

## Status

`COMPLETE_COPRIME_SIDE_JOINT_INCIDENCE_RECEIVER_CHANGE`

Stage14-s7-153/154 refine the witness-coupled q23 object without erasing witness dependence.

For every retained first-layer witness `lambda`, the second reciprocal product can now be written exactly as

```text
W1(lambda)=C1*p_H*q_H*p_+*q_-,
C1=4*r_ep*s_ep*epsilon_k,
p_+ | C_+(lambda),
q_- | C_-(lambda),
gcd(C_+,C_-)=1,
gcd(p_+,q_-)=1,
prime_support(p_H*q_H) subset prime_support(H(lambda)).
```

The q17 reciprocal-CRT witness remains

```text
f*n=W1(lambda),
n+f == 0 (mod 2U),
n-f == 0 (mod 2V),
```

with all frozen q17 kernel filters retained. Hence the unresolved first moment is sharpened from a generic witness-coupled `p(lambda)q(lambda)` incidence to a common-core / two-coprime-side incidence.

Scalar theorem species:

```text
UniformScalarFilteredTau3MovingCommonCoreTwoCoprimeSideReciprocalCRTJointIncidenceFirstMomentLowerBound
```

Polynomial outer-pair theorem species:

```text
UniformPolynomialOuterPairFilteredTau3MovingCommonCoreTwoCoprimeSideReciprocalCRTJointIncidenceFirstMomentLowerBound
```

This is a material receiver change. It does not prove positive density: the moving common core `H(lambda)`, side divisor allocations, reciprocal-CRT support, and filtered-tau3 witness remain correlated. The residual root-origin/canonical/allocation/cell/post-column mask remains separately charged after this gate.

The new exact structure is sufficiently specific for the next XQ literature/adapter pass; no new sH is opened here.

```text
RECEIVER_MATERIALLY_CHANGED=true
MOVING_COMMON_CORE_TWO_COPRIME_SIDE_NORMAL_FORM_PROVED=true
JOINT_INCIDENCE_FIRST_MOMENT_LOWER_BOUND_PROVED=false
POST_MASK_REMAINS_SEPARATELY_CHARGED=true
Q24_THEOREM_TARGET_NOW_STABLE=true
Q24_NEEDED=true
S_ROUTE_H_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT=Stage14-s7-156
```