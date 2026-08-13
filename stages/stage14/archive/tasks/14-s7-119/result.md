# Stage14-s7-119 — open the three active square-class extensions as exact reverse reciprocal factor-pair existence

## Status

`COMPLETE_NONALIGNED_SQUARECLASS_EXTENSION_TO_EXACT_REVERSE_RECIPROCAL_FACTORPAIR_SUPPORT`

Consumes batch-local `Stage14-s7-118`, merged `Stage14-X13`, merged `Stage14-4eq`, and merged `Stage14-s7-112/113`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Freeze one active branch candidate

Let `chi` be one exact precompletion candidate on one of the three nonaligned active realizations. By s7-118 there is a branch scalar `z` such that

```text
M=M0*z^2,
|Xr|*|Yr|=P0*z^2,
```

with `(U,V)`, `r_ep,s_ep`, signs and two-primary decorations fixed on the packet.

Define

```text
W2(z):=4*P0*epsilon_x*U*V*z^2.
```

Merged X13 reverses the second reciprocal equation by positive factor pairs

```text
F2^-*F2^+=W2(z),
cp=(F2^++F2^-)/2,
dq=(F2^+-F2^-)/2,
```

followed by ordered factorizations of `cp` and `dq` into `(c,p)` and `(d,q)`. Parity, positivity, gcd, cell and orientation requirements remain filters.

For each resulting `(p,q)` define

```text
W1:=4*r_ep*s_ep*epsilon_k*p*q.
```

The first reciprocal equation is then equivalent to a positive factor pair

```text
F1^-*F1^+=W1
```

with exact divisibility congruences

```text
F1^+ + F1^- == 0 (mod 2*U),
F1^+ - F1^- == 0 (mod 2*V),
```

which reconstruct `(a,b)` when integral.

## 2. Exact square-class reverse witness set

Define `Omega_sq(chi)` to be the set of tuples

```text
(F2^-,F2^+,c,p,d,q,F1^-,F1^+,a,b)
```

satisfying the two exact reverse reciprocal factorizations above together with all inherited parity, positivity, endpoint-small and already-exposed divisibility filters, but before the remaining labelled root/canonical/post-column acceptance masks are imposed.

Let

```text
R_sq_post(chi;omega) in {0,1}
```

be the conjunction of every retained extension-dependent physical condition not already built into `Omega_sq`.

Then the s7-112 existential extension Boolean is exactly

```text
C_ext(chi)=1
iff
exists omega in Omega_sq(chi) with R_sq_post(chi;omega)=1.
```

No independence or density assertion is used.

## 3. Fixed-candidate witness multiplicity stays subpolynomial

All integers in the reverse equations are polynomially bounded. Divisor bounds in the two factor-pair layers and in the `(cp,dq)` factorizations give uniformly

```text
#Omega_sq(chi) <= B^o(1).
```

This is the same multiplicity fact already available through X13/4eq, now expressed on the exact scalar square-class host. It is not recharged as an outer density saving and it does not imply nonemptiness.

```text
S_SQUARECLASS_REVERSE_WITNESS_SET_DEFINED=true
S_SQUARECLASS_REVERSE_WITNESS_MULTIPLICITY=Bo1
S_SQUARECLASS_REVERSE_EXISTENCE_AUTOMATIC=false
REVERSE_WITNESS_MULTIPLICITY_RECHARGED=false
```

## 4. Branch measures remain distinct

The exact extension equations share a square-class host, but the charged measures do not collapse:

```text
endpoint branch: scalar t with fixed E0,r0;
fixed-product branch: scalar E with fixed m0,u0,v0;
polynomial-pair branch: charged outer pair (E,m), hosted by z=n=Em only inside the reverse extension.
```

In particular, a support theorem in `z` cannot be multiplied or directly substituted for a theorem on the polynomial outer pair without a measure-preserving adapter.

```text
S_SQUARECLASS_EXTENSION_EQUATIONS_COMMON=true
S_SQUARECLASS_OUTER_MEASURE_COMMON=false
S_SQUARECLASS_SUPPORT_CROSS_PROMOTABLE=false
```

## 5. Material receiver change and H decision

The three nonaligned realizations no longer have an opaque generic existential completion receiver. They have an explicit nested structure

```text
branch-specific precompletion support
 -> fixed-square-class reverse reciprocal factor-pair support
 -> residual root/canonical/post-column acceptance.
```

The fixed-E two-sided realization remains separately parked at the merged 4ghH external first-moment gate.

This is a material receiver change. No new sH is opened in this batch: before freezing an external theorem target, the next s stage must separate the bare `Omega_sq` nonemptiness support from `R_sq_post` at exponent level and determine whether the one-dimensional endpoint/fixed-product measures or the polynomial-pair measure produce distinct theorem contracts.

```text
CURRENT_S_RECEIVER=FixedETwoSidedParkedUniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment_OR_FixedEEndpointPreFilterThenSquareClassReverseFactorPairExistenceThenPostMask_OR_PolynomialEFixedProductPreFilterThenSquareClassReverseFactorPairExistenceThenPostMask_OR_PolynomialEFiberedPairPreFilterThenSquareClassHostedReverseFactorPairExistenceThenPostMask
RECEIVER_MATERIALLY_CHANGED=true
S7_119_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-120
```

## Boundary

```text
STAGE14_S7_119=COMPLETE_NONALIGNED_SQUARECLASS_EXTENSION_TO_EXACT_REVERSE_RECIPROCAL_FACTORPAIR_SUPPORT
S_SQUARECLASS_REVERSE_WITNESS_SET_DEFINED=true
S_SQUARECLASS_REVERSE_WITNESS_MULTIPLICITY=Bo1
S_SQUARECLASS_REVERSE_EXISTENCE_AUTOMATIC=false
S_SQUARECLASS_OUTER_MEASURE_COMMON=false
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-120
```
