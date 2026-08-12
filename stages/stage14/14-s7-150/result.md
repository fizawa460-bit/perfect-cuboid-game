# Stage14-s7-150 — W1 witness-dependence separability test

## Status

`COMPLETE_W1_WITNESS_DEPENDENCE_SEPARABILITY_TEST`

Consumes merged Stage14-s7-147..149 and merged Work-ckX49/q23.

On every active nonaligned frozen packet the joint incidence first moment is

```text
J1_G = sum_{lambda in Lambda} sum_{f*n=W1(lambda)} R_q17(lambda;f,n),
```

with

```text
W1(lambda)=4*r_ep*s_ep*epsilon_k*p(lambda)*q(lambda),
f*n=W1(lambda),
n+f == 0 (mod 2U),
n-f == 0 (mod 2V).
```

The first-layer witness `lambda` retains the filtered-tau3 factorization data (scalar branch `g*x*y=c_C*z`; pair branch `g*x*y=c_C*E*m`) together with the frozen allocation and first-reverse labels. The quantities `p(lambda),q(lambda)` are reconstructed from the first reverse factor pair and inherited divisibility labels. Therefore `W1` is not a function of the outer scalar `z` alone and, on the polynomial branch, not a function of the host product `E*m` alone.

Freezing the finite packet labels does not freeze `p,q`: they still move with the retained first-layer divisor witness. Thus no exact factorization of the form

```text
W1(lambda)=W_outer(outer)*W_fixed
```

with `W_outer` depending only on the charged outer coordinate is available from the merged algebra.

Likewise, replacing the witness by its outer host would erase the filtered-tau3 conditioning and is forbidden by the charged-measure firewall.

Hence the q23 separability test is negative:

```text
Q23_W1_WITNESS_DEPENDENCE_SEPARABILITY_TEST=FAIL_WITNESS_DEPENDENCE_ESSENTIAL
W1_OUTER_ONLY_SEPARATION_PROVED=false
W1_FIXED_SHIFT_PARAMETER_PROVED=false
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
FILTERED_TAU3_CONDITIONING_PRESERVED=true
```

This is not a sparsity claim. It only says the exact current joint incidence cannot be reduced to an outer-only shift/modulus by the available identities.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-151
```