# Stage14-s7-133 — exact quadratic divisor-root normal form for the second reverse layer

## Status

`COMPLETE_SECOND_REVERSE_QUADRATIC_DIVISOR_ROOT_NORMAL_FORM`

Consumes batch-local `Stage14-s7-132`, merged `Stage14-s7-129..131`, merged q20, and the merged reverse dictionary.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. One divisor variable

For one retained first-layer witness `lambda`, write

```text
W1=W1(lambda)>0,
f=F1^-,
F1^+=W1/f,
f|W1.
```

The exact reciprocal integrality conditions inherited from s7-119 are

```text
F1^+ + F1^- == 0 (mod 2*U),
F1^+ - F1^- == 0 (mod 2*V).
```

Substituting `F1^+=W1/f` and multiplying by the positive divisor `f` gives the equivalent simultaneous conditions

```text
W1 + f^2 == 0 (mod 2*U*f),
W1 - f^2 == 0 (mod 2*V*f).
```

Together with `f|W1` and the inherited positivity/parity/order filters, this is an exact one-divisor-variable description of the second reverse layer.

## 2. Exact conditioned weight

Define

```text
R_qdr(lambda;f)=1
```

iff

```text
f|W1(lambda),
W1(lambda)+f^2 == 0 (mod 2*U*f),
W1(lambda)-f^2 == 0 (mod 2*V*f),
```

and all already-exposed second-layer positivity/parity/order conditions hold.  The residual root/canonical/post-column post-mask is excluded.

Then

```text
N_rev2(lambda)=sum_{f|W1(lambda)} R_qdr(lambda;f)
```

exactly.

Hence

```text
S_SECOND_REVERSE_QUADRATIC_DIVISOR_ROOT_ENCODING_EXACT=true
SECOND_REVERSE_POSTMASK_INSERTED=false
```

## 3. q20 normal-form test

The normal form is now explicit, but it is not a fixed shift or a fixed binary form in the charged outer variable: `W1(lambda)` moves with the retained first-layer witness, and the modulus itself contains the divisor variable `f`.

Therefore the presently proved object is not directly a classical fixed-shift `d_3*d` correlation, a single fixed binary-form divisor sum, a generalized-divisor AP sum with outer-only modulus, or a finite-complexity linear-divisor system.

```text
Q20_FIXED_SHIFT_OR_BINARY_FORM_NORMAL_FORM_TEST=FAIL_MOVING_W1_AND_DIVISOR_HOSTED_MODULUS
FIXED_SHIFT_D3_D_ENCODING_PROVED=false
FIXED_BINARY_FORM_ENCODING_PROVED=false
OUTER_ONLY_AP_ENCODING_PROVED=false
LINEAR_DIVISOR_SYSTEM_ENCODING_PROVED=false
```

The failure is at the exact encoding level; no literature theorem is rejected beyond its stated interface.

## 4. Multiplicity boundary

Since `f|W1(lambda)` and all quantities have polynomial height,

```text
N_rev2(lambda)<=tau(W1(lambda))=B^o(1),
```

which is the already charged multiplicity envelope and is not a density saving.

## 5. Boundary

```text
STAGE14_S7_133=COMPLETE_SECOND_REVERSE_QUADRATIC_DIVISOR_ROOT_NORMAL_FORM
S_SECOND_REVERSE_QUADRATIC_DIVISOR_ROOT_ENCODING_EXACT=true
Q20_FIXED_SHIFT_OR_BINARY_FORM_NORMAL_FORM_TEST=FAIL_MOVING_W1_AND_DIVISOR_HOSTED_MODULUS
RECEIVER_MATERIALLY_CHANGED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-134
```
