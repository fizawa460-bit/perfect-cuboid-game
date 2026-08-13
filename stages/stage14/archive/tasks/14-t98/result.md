# Stage14-t98 — decompose one influential generic-bit boundary into sign, divisor, and endpoint-residue events

## Status

`COMPLETE_SINGLE_GENERIC_BIT_BOUNDARY_TYPE_DECOMPOSITION`

Stage14-t98 consumes merged Stage14-t97 and the frozen completed tH26 snapshot. No H target is reopened.

Fix one influential generic split prime `p|delta_G`, write

```text
varpi_p^e=A+iB,
gamma_0=u+iv,
gamma_+=gamma_0(A+iB),
gamma_-=gamma_0(A-iB),
```

and keep the fixed norm-`k0` Gaussian factor `a` from t90. Merged t97 proves that every reconstructed cover coordinate for the two orientations is an integral linear form in

```text
uA, vB, uB, vA.
```

The purpose here is to identify exactly which residual physical predicates can change under the `p`-bit flip.

## 1. Primitive-cover membership is invariant under a generic p-flip

Write

```text
z_+=a gamma_+,
z_-=a gamma_-.
```

The primitive-cover condition is that no rational prime `r` divides the Gaussian integer `z_+` or `z_-` as a rational integer, equivalently no `r` divides both reconstructed cover coordinates.

For `r!=p`, conjugating only the `p`-primary Gaussian factor leaves the pair of Gaussian valuations above `r` unchanged. For `r=p`, genericity gives

```text
p ∤ k0,
p ∤ N(gamma_0),
```

so neither `a` nor `gamma_0` supplies the missing conjugate `p`-factor. Thus neither orientation is divisible by rational `p`.

Hence

```text
P_prim(a,gamma_+)=P_prim(a,gamma_-).
```

Therefore primitive-cover membership cannot be the source of the t96 influence.

```text
GENERIC_BIT_FLIP_PRIMITIVE_SELECTOR_INVARIANT=true
```

## 2. Fixed packet tags remain invariant

By the t91/t97 generic-prime definition, the bit flip does not alter

```text
(kappa,beta),
fixed reciprocal/inversion orientation,
endpoint conductor d,
fixed exceptional-prime support.
```

The t89 strong `Q` gap also keeps the short archimedean magnitude inequalities automatic. These predicates are not reopened.

```text
FIXED_PACKET_TAGS_BIT_FLIP_INVARIANT=true
SHORT_ARCHIMEDEAN_MAGNITUDE_MASKS_REOPENED=false
```

## 3. Remaining boundary type A: linear sign/order changes

After multiplication by fixed `a`, the reconstructed variables

```text
p_cov, q_cov, r=q_cov-p_cov, t=q_cov+p_cov
```

are integral linear forms in `(uA,vB,uB,vA)`. Any residual sign/order convention therefore changes between the two orientations only across an explicit pair of integral linear half-spaces.

Thus every sign contribution to the symmetric difference is of the form

```text
1_{L_+(u,v)>0} xor 1_{L_-(u,v)>0}
```

for explicit fixed-coefficient linear forms `L_+`, `L_-` determined by `(a,A,B)`.

There are only `O(1)` such sign/order predicates per frozen packet.

```text
SIGN_BOUNDARY_REDUCED_TO_O1_LINEAR_HALFSPACE_XOR=true
```

## 4. Remaining boundary type B: four-cell divisor membership

Merged t78/t90 expresses the four-cell data using fixed direction columns

```text
A0=odd(b-a),
B0=odd(b+a)
```

and reconstructed

```text
R=odd(r),
T=odd(t).
```

The four cell divisors are

```text
gcd(A0,R), gcd(A0,T), gcd(B0,R), gcd(B0,T).
```

Hence a four-cell label can change under the `p`-bit flip only if, for some rational prime divisor

```text
q | A0*B0,
```

a divisibility predicate changes between the two explicit reconstructed linear forms:

```text
1_{q|L_+(u,v)} xor 1_{q|L_-(u,v)}.
```

The number of relevant prime/divisor switches is divisor-many, hence `B^o(1)` pointwise. The moduli themselves are fixed packet divisors and are not asserted to be numerically `B^o(1)`.

```text
FOUR_CELL_BOUNDARY_REDUCED_TO_BO1_FIXED_DIVISOR_CONGRUENCE_XORS=true
FIXED_DIVISOR_MODULI_FORCED_SMALL=false
```

## 5. Remaining boundary type C: endpoint projective residue

Merged t87/t90 gives endpoint conductor

```text
d=B^o(1)
```

and an exact projective-character/residue formulation modulo `d`. Therefore the endpoint selector changes only if the two explicit orientations land on opposite sides of one of the `B^o(1)` residue/projective tests modulo `d`.

Equivalently its contribution is a `B^o(1)` union/linear combination of events

```text
1_{L_+(u,v) in C mod d} xor 1_{L_-(u,v) in C mod d}
```

with `C` fixed by the frozen packet.

```text
ENDPOINT_BOUNDARY_REDUCED_TO_BO1_SMALL_MODULUS_RESIDUE_XORS=true
```

## 6. Exact boundary union

Consequently the t97 physical symmetric difference satisfies the exact containment/decomposition

```text
B_p(gamma_0)
 <=
 B_sign(gamma_0)
 + sum_{q|A0B0} B_q(gamma_0)
 + B_proj(gamma_0),
```

where every term is one of the three explicit types above. Using exact Boolean inclusion-exclusion one may replace the majorizing union by an equality with `B^o(1)` terms; no new analytic variable is introduced.

Thus

```text
Inf_p(f)
```

is localized to a `B^o(1)` family of explicit one-boundary averages.

This does **not** yet give fixed-power sparsity. A linear half-space XOR can have positive density, a fixed divisor may be small, and the endpoint modulus is deliberately subpolynomial. Therefore no packet or whole-family saving is claimed.

```text
T97_EXPLICIT_SYMMETRIC_DIFFERENCE_RETAINED=true
GENERIC_BIT_FLIP_PRIMITIVE_SELECTOR_INVARIANT=true
FIXED_PACKET_TAGS_BIT_FLIP_INVARIANT=true
SIGN_BOUNDARY_REDUCED_TO_O1_LINEAR_HALFSPACE_XOR=true
FOUR_CELL_BOUNDARY_REDUCED_TO_BO1_FIXED_DIVISOR_CONGRUENCE_XORS=true
ENDPOINT_BOUNDARY_REDUCED_TO_BO1_SMALL_MODULUS_RESIDUE_XORS=true
SINGLE_BOUNDARY_TYPE_PIGEONHOLE_PROVED=false
FIXED_POWER_BOUNDARY_SPARSITY_PROVED=false
TH26_COMPLETE_CONSUMED=true
TH27_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PREFERRED_RECEIVER=SharedUCanonicalLPFSingleGenericPrimeMixedLinearSignFixedDivisorEndpointResidueBoundary
NEXT=Stage14-t99
```
