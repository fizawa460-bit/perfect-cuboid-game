# Stage14-s7-49 — exact centering, zero-mode isolation, and inverse-fraction adapter

## Status

`COMPLETE_CENTERED_NORM_ROOTLINE_TO_KLOOSTERMAN_INVERSE_FRACTION_ADAPTER`

Stage14-s7-49 consumes merged `Stage14-s7-48`, merged immutable `Stage14-sH48`, and the compatible merged `Stage14-4df` six-atomic-block separation.

The entering whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

The purpose of this stage is to construct the centering/completion adapter which sH48 identified as missing.  No off-the-shelf theorem is invoked here and no new whole-family exponent is claimed.

---

## 1. Imported primitive rotated-pair packet

After the frozen endpoint, 2-primary, and `B^o(1)` gcd peels, write

```text
m=D+A,
n=D-A,
P_-=m*n=epsilon_-*u_*R*J,
N_+=m^2+n^2=2*epsilon_+*C_*S*T.
```

On the square-root saturation band,

```text
m,n=B^(1/4+o(1)),
C_*=B^(chi+o(1)),
1/6<=chi<=1/4,
u_*=B^(1/4-chi+o(1)),
R,J=B^(1/8+chi/2+o(1)),
S,T=B^(1/4-chi/2+o(1)).
```

Merged 4df upgrades the earlier four-block separation to the atomic statement that

```text
C_*, S, T, u_*, R, J
```

are pairwise separated at fixed-power scale.  Therefore, after the already-permitted subpolynomial peel,

```text
gcd(C_*,P_-)=1,
gcd(C_*,m*n)=1.
```

In particular both `m` and `n` are units modulo `C_*`.

```text
MERGED_SH48_CONSUMED=true
MERGED_4DF_SIX_BLOCK_SEPARATION_IMPORTED=true
C_STAR_COPRIME_TO_ROTATED_PRODUCT=true
```

---

## 2. Exact norm root-line decomposition

Let

```text
R_-(C_*):={rho mod C_* : rho^2 == -1 (mod C_*)}.
```

The physical packet already forces every odd fixed-power prime of `C_*` to be a split Gaussian prime.  Hence, after the frozen endpoint convention,

```text
#R_-(C_*)=2^omega(C_*)=B^o(1).
```

Because `n` is a unit modulo `C_*`,

```text
C_* | m^2+n^2
```

is equivalent to

```text
m*n^(-1) in R_-(C_*).
```

Therefore exactly

```text
boxed:
1_{C_* | m^2+n^2}
 = sum_{rho in R_-(C_*)} 1_{m == rho*n (mod C_*)}.       (2.1)
```

No physical packet is relaxed in (2.1).

```text
NORM_DIVISIBILITY_EXACT_ROOTLINE_UNION=true
ROOTLINE_MULTIPLICITY=Bo1
```

---

## 3. Exact Fourier centering of every Gaussian root line

Write

```text
e_C(x):=exp(2*pi*i*x/C).
```

Orthogonality gives, for every root `rho`,

```text
1_{m == rho*n (mod C_*)}
 = (1/C_*) * sum_{h mod C_*} e_{C_*}(h*(m-rho*n)).
```

Separating `h=0` and summing over the root set gives the exact identity

```text
boxed:
1_{C_* | m^2+n^2}
 = r_-(C_*)/C_*
   + K_{C_*}(m,n),                                  (3.1)
```

where

```text
r_-(C_*):=#R_-(C_*),

K_{C_*}(m,n)
 := (1/C_*)
    * sum_{rho in R_-(C_*)}
      sum_{0!=h mod C_*}
        e_{C_*}(h*(m-rho*n)).                       (3.2)
```

For every fixed unit `n`, the centered kernel has exact zero mean over `m mod C_*`:

```text
boxed:
sum_{m mod C_*} K_{C_*}(m,n)=0.                    (3.3)
```

This is the canonical local centering that was missing at the sH48 snapshot.

```text
EXACT_LOCAL_CENTERING_PROVED=true
CENTERED_KERNEL_MEAN_ZERO=true
ZERO_FREQUENCY_SEPARATED_EXACTLY=true
```

---

## 4. The zero mode reproduces exactly the square-root barrier

Use the minus-side coordinates `(u_*,R,J)` as the charged-once ambient packet.  Their total exponent is

```text
(1/4-chi) + (1/8+chi/2) + (1/8+chi/2) = 1/2.
```

Now temporarily expose the extra norm divisor `C_*`.  A dyadic `C_*~B^chi` family has `B^(chi+o(1))` possible values, while the zero-frequency density in (3.1) is

```text
r_-(C_*)/C_* = B^(-chi+o(1)).
```

Thus the `C_*` support and its local zero-frequency density cancel exactly at fixed-power scale:

```text
boxed:
E_zero
 = 1/2 + chi - chi
 = 1/2.                                             (4.1)
```

The balanced `(S,T)` quotient split and all reciprocal/orientation/completion masks may be retained as bounded selectors; they do not create a new polynomial coordinate after `(m,n,C_*)` is fixed.

Therefore the principal local density is precisely capable of carrying the existing square-root barrier.

```text
ZERO_MODE_EXPONENT=1/2
ZERO_MODE_ALONE_STRICT_SUBSQRT=false
SQRT_BARRIER_IDENTIFIED_WITH_LOCAL_ZERO_MODE=true
```

This is not a lower bound for physical packets.  It is the exact exponent ledger of the principal term in the centered expansion.

---

## 5. Product identity converts every nonzero frequency to an inverse-fraction phase

On the same physical packet,

```text
P_-=m*n=epsilon_-*u_*R*J
```

and `gcd(P_-,C_*)=1`.  Since `m` is a unit modulo `C_*`,

```text
n == P_- * inverse(m) (mod C_*).
```

Substitute this into each nonzero term in (3.2).  The phase becomes

```text
boxed:
e_{C_*}(h*m - h*rho*P_*inverse(m)),                (5.1)
```

with `P_*=P_-` modulo `C_*`.

Equivalently, for coefficients

```text
a=h,
b=-h*rho*P_-,
```

it is the classical inverse-fraction / incomplete Kloosterman shape

```text
boxed:
e_{C_*}(a*m+b*inverse(m)).                         (5.2)
```

All coefficients are physical: `rho` is the Gaussian `sqrt(-1)` root label and `P_-` is the rotated-coordinate product.  No artificial averaging variable has been introduced.

```text
NONZERO_FREQUENCY_INVERSE_FRACTION_ADAPTER_PROVED=true
KLOOSTERMAN_TYPE_PHASE_EXACT=true
PRODUCT_SIDE_PHYSICAL_MASK_RETAINED=true
```

This is the precise adapter whose absence prevented direct use of the Kloosterman-fraction literature in sH48.

---

## 6. Frequency gcd produces an exact conductor stratification

The modulus in (5.2) is not automatically primitive because `h` may share factors with `C_*`.

For every nonzero frequency define

```text
g:=gcd(h,C_*),
q:=C_*/g,
h=g*h0,
gcd(h0,q)=1.
```

Then the phase reduces exactly to modulus `q`:

```text
boxed:
e_{C_*}(h*m-h*rho*P_-*inverse(m))
 = e_q(h0*m-h0*rho_q*P_-*inverse(m)),              (6.1)
```

where `rho_q` is the reduction of `rho mod q` and still satisfies

```text
rho_q^2 == -1 (mod q).
```

For fixed `q|C_*`, the frequencies of exact conductor `q` are parametrized by

```text
h=(C_*/q)*h0,
0<h0<q,
gcd(h0,q)=1,
```

so there are exactly `phi(q)` such frequencies per root line.

Thus the centered nonzero contribution is not one uniform modulus family: it is a divisor stratification over effective conductors

```text
q|C_*,
q>1.
```

```text
FREQUENCY_CONDUCTOR_STRATIFICATION_PROVED=true
EFFECTIVE_KLOOSTERMAN_MODULUS=q
EXACT_CONDUCTOR_FREQUENCY_COUNT=phi(q)
```

This conductor loss must be handled before importing a theorem whose saving depends on the modulus size.

---

## 7. Why sH48 is not reopened and why a new H is premature

The completed `sH48` theorem audit is a frozen certificate for the pre-centering positive correlation receiver.  Stage14-s7-49 has now supplied a materially new exact adapter, but the resulting oscillatory family still has an internal arithmetic issue:

```text
q=C_*/gcd(h,C_*)
```

may range from endpoint-small to full size.

A theorem request that ignores this conductor stratification would be underspecified and could silently assume a large primitive modulus which is not yet proved.

Therefore

```text
SH48_REOPENED=false
S7_49_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

The s route should first split the nonzero frequencies by effective conductor and prove either:

1. low-conductor blocks are harmless by an internal divisor/frequency argument; or
2. square-root saturation forces `q` into a fixed-power-large range; or
3. the low-conductor mass itself has a smaller exact receiver.

Only after this peel should a possible `sH50` theorem target be frozen.

---

## 8. New receiver

The sH48 preferred receiver

```text
CenteredPrimitiveQuarterPairProductNormDualBalancedCellFactorizationDispersion
```

is now sharpened to

```text
boxed:
CenteredPrimitiveQuarterPairPhysicalInverseFractionConductorStratifiedDispersion.
```

Mandatory structure:

```text
m,n=B^(1/4+o(1)),
gcd(m,n)=B^o(1),
P_-=m*n=epsilon_-u_*RJ,
C_*=B^(chi+o(1)),
1/6<=chi<=1/4,
gcd(C_*,P_-)=1,
R_-(C_*)={rho:rho^2=-1 mod C_*},

1_{C_*|m^2+n^2}
 = r_-(C_*)/C_*
 + (1/C_*) sum_rho sum_{h!=0} e_{C_*}(h(m-rho*n)),

n=P_*inverse(m) mod C_*,
nonzero phase=e_{C_*}(h*m-h*rho*P_*inverse(m)),
q=C_*/gcd(h,C_*),
all balanced-cell / squarefree / separation / reciprocal masks retained.
```

The next deterministic task is the conductor peel, not another generic literature search.

---

## 9. Whole-family theorem and boundary

No new global exponent is claimed:

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
```

Boundary:

```text
STAGE14_S7_49=COMPLETE_CENTERED_NORM_ROOTLINE_TO_KLOOSTERMAN_INVERSE_FRACTION_ADAPTER
MERGED_S7_48_IMPORTED=true
MERGED_SH48_CONSUMED=true
MERGED_4DF_SIX_BLOCK_SEPARATION_IMPORTED=true
C_STAR_COPRIME_TO_ROTATED_PRODUCT=true
NORM_DIVISIBILITY_EXACT_ROOTLINE_UNION=true
EXACT_LOCAL_CENTERING_PROVED=true
CENTERED_KERNEL_MEAN_ZERO=true
ZERO_FREQUENCY_SEPARATED_EXACTLY=true
ZERO_MODE_EXPONENT=1/2
SQRT_BARRIER_IDENTIFIED_WITH_LOCAL_ZERO_MODE=true
NONZERO_FREQUENCY_INVERSE_FRACTION_ADAPTER_PROVED=true
KLOOSTERMAN_TYPE_PHASE_EXACT=true
FREQUENCY_CONDUCTOR_STRATIFICATION_PROVED=true
EFFECTIVE_KLOOSTERMAN_MODULUS=q
SH48_REOPENED=false
S7_49_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_CURRENT_STATE=ACTIVE_REACTIVATED
S_ROUTE_NEXT=Stage14-s7-50
NEXT=Stage14-s7-50
```
