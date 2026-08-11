# Stage14-t128 — consume tH29 and split depletion by prime headroom and projective-character type

## Status

`COMPLETE_PROJECTIVE_DEPLETION_HEADROOM_REAL_NONREAL_TRISPLIT`

Consumes the completed independent `Stage14-tH29` audit and Stage14-t127.  No positive theorem is imported from tH29.

The t127/tH29 target is

```text
T=M+D,
D=1/g * sum_{chi!=1} D_chi,
g=|G(d)|=B^o(1),
```

on the exact hyperbola

```text
N(gamma)*ell<=X_U,
ell>2*sqrt(B).
```

For one cofactor norm `n=N(gamma)`, define the exact multiplicative prime headroom

```text
R(n)
 := (X_U/n)/(2*sqrt(B))
 = sqrt(B)/(h*k0*n)
 >1.
```

Fix any small constant `theta>0` and split the charged cofactor family into

```text
Omega_edge(theta)={gamma: 1<R(N(gamma))<B^theta},
Omega_long(theta)={gamma: R(N(gamma))>=B^theta}.
```

Let

```text
T=T_edge+T_long,
M=M_edge+M_long
```

be the corresponding exact nonnegative physical/principal masses.

If

```text
T <= B^(-delta) M
```

for some fixed `delta>0`, then the weighted average of the nonnegative ratios `T_edge/M_edge` and `T_long/M_long` is at most `B^-delta` (ignoring zero-baseline pieces).  Hence at least one nonzero branch itself satisfies

```text
T_branch <= B^(-delta) M_branch.
```

Thus a bad packet localizes to an endpoint-headroom depletion branch or a long-headroom depletion branch without loss of fixed exponent.

## 1. Endpoint-headroom branch

On `Omega_edge(theta)`,

```text
B^(1/2-theta)/(h*k0)
 < N(gamma)
 < B^(1/2)/(h*k0),
```

and the prime interval is

```text
(2*sqrt(B), 2*sqrt(B)*R(N(gamma))]
subset
(2*sqrt(B), 2*B^(1/2+theta)].
```

No lower bound away from headroom `1` is available inside this branch.  This is exactly the endpoint-short regime isolated by tH29.

Define the first live mechanism

```text
EndpointHeadroomProjectivePrimeDepletion.
```

No prime-distribution theorem is charged here.

## 2. Long-headroom branch and character pigeonhole

On `Omega_long(theta)` every prime interval has fixed-power multiplicative headroom at least `B^theta`.  Write the nonprincipal Fourier contribution as

```text
D_long
 = 1/g * sum_{chi!=1} D_chi,long.
```

If the long branch has fixed-power depletion, then

```text
D_long <= -(1-B^(-delta)) M_long.
```

Since the number of nonprincipal characters is only

```text
g-1=B^o(1),
```

there exists at least one nonprincipal `chi` with

```text
|D_chi,long|
 >= B^(-o(1)) M_long.
```

Thus principal-scale depletion on the long branch forces a principal-scale individual projective-character correlation at exponent level.

Split those characters exactly into

```text
chi^2=1   (real/order-two),
chi^2!=1  (nonreal, paired with conjugate chi-bar).
```

This gives two distinct live mechanisms.

### Real-character branch

```text
LongHeadroomRealProjectiveHeckeCharacterPrincipalScaleBias.
```

The frozen hypotheses do not exclude real projective characters or an exceptional real Hecke zero.  tH29 therefore certifies no uniform cancellation/lower-distribution theorem for this branch.

### Nonreal-character branch

```text
LongHeadroomNonrealProjectiveCharacterPhysicalCofactorBilinearCorrelation.
```

Here there is no real exceptional-zero mechanism, but tH29 found no theorem-ready Type-I/Type-II, spin, or multiplicative decomposition for the retained physical cofactor character sum.  The branch remains an internal coefficient-structure problem before any further H audit.

## 3. New minimal receiver

The old single receiver

```text
NonboundaryPhysicalCofactorSelectedProjectiveClassNearTotalPrimeDepletion
```

has therefore split into three mathematically distinct mechanisms:

```text
(A) EndpointHeadroomProjectivePrimeDepletion,
(B) LongHeadroomRealProjectiveHeckeCharacterPrincipalScaleBias,
(C) LongHeadroomNonrealProjectiveCharacterPhysicalCofactorBilinearCorrelation.
```

This is a material receiver change.  No one branch is proved power-saving here.

The next internal priority is (A): quantify how much charged principal/cofactor mass can lie in the endpoint headroom layer as `theta` varies.  In parallel, branch (B) should inspect the actual order-two quotient characters of `G(d)` before any new literature search, and branch (C) should open the cofactor character coefficient into norm/orientation factors.

```text
PROJECTIVE_DEPLETION_HEADROOM_SPLIT_EXACT=true
FIXED_POWER_BAD_PACKET_LOCALIZES_TO_EDGE_OR_LONG_BRANCH=true
LONG_BRANCH_PRINCIPAL_SCALE_CHARACTER_PIGEONHOLE=true
PROJECTIVE_CHARACTERS_REAL_NONREAL_SPLIT_EXACT=true
TH29_CONSUMED=true
TH29_DIRECT_THEOREM_APPLICABLE=false
RECEIVER_MATERIALLY_CHANGED=true
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH30_NEEDED=false
PREFERRED_RECEIVER=SharedUEndpointHeadroomProjectivePrimeDepletionOrLongHeadroomRealProjectiveHeckeBiasOrLongHeadroomNonrealProjectiveCofactorBilinearCorrelation
NEXT_INTERNAL_TARGET=EndpointHeadroomChargedPrincipalMassLayerAudit
NEXT=Stage14-t129
```
