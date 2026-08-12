# Stage14-t156 — actual-scale Kai-inadmissible long modulus window

## Status

`COMPLETE_KAI_INADMISSIBLE_LONG_MODULUS_WINDOW_LOCALIZATION`

Consumes merged Stage14-t155/t154/t144.  No new prime-distribution theorem is used.

For every surviving long cofactor `z`, merged t155 gives

```text
X_z = X_U/N(z) = L_B R(z),
L_B=2*sqrt(B),
R(z)>=B^theta,
theta>0 fixed,
```

and the unresolved branch satisfies

```text
KAI_INADMISSIBLE(z,d):
d^2 > exp(sqrt(log X_z)/C_K).
```

## 1. Invert the Kai condition

Taking logarithms gives

```text
2 log d > sqrt(log X_z)/C_K,
```

hence

```text
log X_z < 4 C_K^2 (log d)^2.                    (1.1)
```

Put `A_K:=4 C_K^2`.  Long headroom gives

```text
log X_z
 >= (1/2+theta) log B + O(1).
```

Therefore every actual-scale Kai-inadmissible long survivor satisfies

```text
log d >= c_{K,theta} sqrt(log B)
```

for a fixed positive constant `c_{K,theta}` depending only on the audited theorem constant and the frozen long-headroom exponent. Equivalently,

```text
d >= exp(c_{K,theta} sqrt(log B)).               (1.2)
```

This is derived from the theorem's actual upper scale, not from the old sufficient `c_safe` label.

```text
KAI_INADMISSIBLE_LONG_FORCES_PSEUDOPOLYNOMIAL_MODULUS_LOWER_BOUND=true
KAI_INADMISSIBLE_LONG_MODULUS_LOWER_BOUND=exp(c_Ktheta_sqrt_logB)
```

## 2. Fixed-U hosting applies on the entire long branch

Merged t144 gives for the fixed packet

```text
d <= m/2,
h*k0 = eta*epsilon*m.
```

Thus with a fixed positive packet constant `c_pkt=2 eta epsilon`,

```text
h*k0 >= c_pkt d.                                  (2.1)
```

This is not endpoint-specific; it follows from selector provenance and the fixed-U packet identity.

```text
LONG_SELECTOR_HOST_LOWER_BOUND=hk0_GE_cpkt_d
```

## 3. Sparse long principal compatibility

Merged t154 proves that a principal sparse long survivor has

```text
R_* >= q_d B^(-o(1)),
q_d=|(Z[i]/dZ[i])^x|=d^2 B^o(1).
```

Since `n_*=N(z_*)>=1`,

```text
R_* = N_0/n_* <= N_0 = sqrt(B)/(h*k0).
```

Using (2.1),

```text
d^2 B^(-o(1))
 <= sqrt(B)/(c_pkt d),
```

so necessarily

```text
d^3 <= B^(1/2+o(1)).                              (3.1)
```

Thus the sparse Kai-inadmissible principal branch lies in the exact window

```text
exp(c_{K,theta} sqrt(log B))
 <= d
 <= B^(1/6+o(1)),
```

in addition to the upstream hard-branch condition `d=B^o(1)`.

```text
KAI_INADMISSIBLE_SPARSE_LONG_PRINCIPAL_MODULUS_CUBE_CAP=true
```

## 4. Area long principal compatibility

Merged t154 gives on a principal area shell

```text
h*k0*q_d*d^2 <= B^(1/2+o(1)).
```

Using `q_d=d^2 B^o(1)` and (2.1),

```text
d^5 <= B^(1/2+o(1)).                              (4.1)
```

Hence the area branch lies in

```text
exp(c_{K,theta} sqrt(log B))
 <= d
 <= B^(1/10+o(1)),
```

again with the stronger upstream asymptotic statement `d=B^o(1)` retained.

```text
KAI_INADMISSIBLE_AREA_LONG_PRINCIPAL_MODULUS_FIFTH_POWER_CAP=true
```

The polynomial upper caps do not themselves create a new fixed-power saving because `d=B^o(1)` was already known.  Their role is to make the surviving theorem family explicit and quantitatively compatible with principal mass.

## 5. Receiver and H decision

The long receiver is unchanged in mechanism but now carries a theorem-ready modulus window.  Stage14-t157 should test whether sparse and area long packets require different external objects or whether both reduce pointwise to the same fixed-residue Gaussian-prime long-interval lower-ratio theorem beyond Kai's pseudopolynomial envelope.

```text
RECEIVER_MATERIALLY_CHANGED=false
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH33_NEEDED=false
NEXT=Stage14-t157
```