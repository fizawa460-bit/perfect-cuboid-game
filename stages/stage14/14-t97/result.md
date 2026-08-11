# Stage14-t97 — exact arithmetic form of one influential generic orientation bit

## Status

`COMPLETE_SINGLE_GENERIC_ORIENTATION_BIT_ARITHMETIC_BOUNDARY_REDUCTION`

Stage14-t97 consumes merged t96 and does not reopen completed tH26.

Fix one generic split prime `p|delta_G`, write its Gaussian prime power as

```text
varpi^e = A+iB,
```

and factor the remaining cofactor orientation as

```text
gamma_0=u+i v.
```

The two values of the p-orientation bit are exactly

```text
gamma_+ = gamma_0 (A+iB),
gamma_- = gamma_0 (A-iB).
```

Hence

```text
Re(gamma_+) = uA-vB,
Im(gamma_+) = uB+vA,
Re(gamma_-) = uA+vB,
Im(gamma_-) = -uB+vA.
```

In particular

```text
gamma_+ - gamma_- = 2iB gamma_0,
gamma_+ + gamma_- = 2A gamma_0.
```

After multiplication by the fixed Gaussian factor `a` of norm `k0`, every reconstructed cover coordinate, and therefore every remaining physical sign/four-cell test, is an integral linear form in the four bilinear quantities

```text
uA, vB, uB, vA.
```

Because `p` is generic in the t91 sense, flipping this bit does not alter the fixed `(kappa,beta)` tag, endpoint conductor `d`, fixed exceptional support, or the already-frozen reciprocal orientation. Merged t89 also makes the short archimedean cover inequalities automatic from the strong Q gap. Therefore a p-edge on the quotient cube is influential only if one of the residual reconstructed physical predicates changes truth value between the explicit pair `(gamma_+,gamma_-)` above.

Thus the t96 abstract influence event is now an exact arithmetic symmetric-difference event

```text
B_p(gamma_0)
 = 1_{Phys(a gamma_+)} xor 1_{Phys(a gamma_-)}.
```

and

```text
Inf_p(f) = average_{gamma_0 labels} B_p(gamma_0)
```

with the quotient normalization inherited from t96. No extra moving variable is introduced.

This reduction is exact but does not yet prove that `B_p` is one congruence, one interval, or fixed-power sparse. Consequently no packet or whole-family power saving is claimed.

```text
T96_INFLUENTIAL_BIT_RETAINED=true
GENERIC_BIT_FLIP_EXPLICIT_GAUSSIAN_CONJUGATE_PAIR_PROVED=true
BIT_FLIP_COORDINATE_LINEARIZATION_PROVED=true
FIXED_LOCAL_TAGS_UNCHANGED_BY_GENERIC_BIT_FLIP=true
SHORT_ARCHIMEDEAN_MASKS_REOPENED=false
INFLUENCE_EQUALS_EXPLICIT_PHYSICAL_SYMMETRIC_DIFFERENCE=true
SINGLE_CONGRUENCE_BOUNDARY_PROVED=false
FIXED_POWER_BOUNDARY_SPARSITY_PROVED=false
TH26_COMPLETE_CONSUMED=true
TH27_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PREFERRED_RECEIVER=SharedUCanonicalLPFSingleGenericPrimeExplicitPhysicalSymmetricDifferenceBoundary
NEXT=Stage14-t98
```
