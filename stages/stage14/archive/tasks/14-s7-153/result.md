# Stage14-s7-153 — exact common-gcd split of the first reverse reconstruction

## Status

`COMPLETE_FIRST_REVERSE_COMMON_GCD_SPLIT`

Consumes merged Stage14-s7-123, s7-150..152, and the exact reverse dictionary from s7-119.

Fix one active nonaligned packet and one frozen squarefree allocation `(A,B)`. Write

```text
R := A*x^2,
S := B*y^2,
gcd(R,S)=1,
F2^- = g*R,
F2^+ = g*S,
```

with the inherited order filter `S>R>0`. The first reverse reconstruction gives

```text
c*p = g*(S+R)/2,
d*q = g*(S-R)/2.
```

Because `gcd(R,S)=1`,

```text
gcd(S+R,S-R) | 2.
```

There are only the parity cases already retained by the frozen two-primary chart.

- If `R,S` are both odd, `(S+R)/2` and `(S-R)/2` are coprime, hence

```text
gcd(c*p,d*q)=g.
```

- If `R,S` have opposite parity, `S+R` and `S-R` are odd and coprime. Integrality of `c*p,d*q` forces `2|g`, and

```text
gcd(c*p,d*q)=g/2.
```

Thus, with

```text
delta_2 = 1  if R,S are both odd,
delta_2 = 2  if R,S have opposite parity,
H := g/delta_2,
```

the reconstruction has the exact form

```text
c*p = H*C_+,
d*q = H*C_-,
gcd(C_+,C_-)=1,
```

where

```text
C_+ = (S+R)/2        and C_- = (S-R)/2       in the both-odd case,
C_+ = S+R            and C_- = S-R           in the opposite-parity case.
```

No density or independence statement is used. This only identifies the complete cross-side common divisor of the two reconstructed products.

```text
FIRST_REVERSE_EXACT_COMMON_GCD_PROVED=true
FIRST_REVERSE_COMMON_GCD=H_equals_g_over_delta2
FIRST_REVERSE_COPRIME_SIDE_FACTORS_PROVED=true
TWO_PRIMARY_CHART_PRESERVED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-154
```