# Stage14-4eb — canonical first-reciprocal substitution

## Status

`COMPLETE_CANONICAL_FIRST_RECIPROCAL_TAUTOLOGY_AND_SECOND_LAYER_LOCALIZATION`

Consumes merged `Stage14-4ea`, merged `Stage14-s7-46`, merged s-batch `Stage14-s7-66..68`, merged `Stage14-X13`, and latest main at batch start `e601b1e4224e718eafa67018f964ca40ee607377`. Unmerged descendants are advisory only.

The canonical theorem remains

```text
V(B) << B^(1/2+o(1)),
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Canonical primitive coordinates

Use the merged primitive slope coordinates

```text
gcd(a,b)=1,
0<a<b,
r=g a,
s=g b,
g=B^o(1),
D=(r+s)/2,
A=(s-r)/2.
```

Hence exactly

```text
D-A=g a,
D+A=g b.
```

Merged s7-66 localizes the minus agreement allocation to coprime divisors

```text
U | b,
V | a,
gcd(U,V)=1,
```

up to the already-frozen `B^o(1)` endpoint / 2-primary decoration.

Define the first signed quotients

```text
c_+ := (D+A)/U = g b/U,
c_- := (D-A)/V = g a/V.
```

These are determined once the primitive slope, allowed common-scale decoration, and canonical minus allocation witness are fixed.

## 2. First reciprocal equation becomes the complementary-square identity

Merged s7-27/s7-46 gives the exact first reciprocal equation

```text
(c_+ U)^2-(c_- V)^2
 = 4 r_e s_e epsilon_k p q,
```

where `r_e,s_e` denote the endpoint-small factors used in the reciprocal packet and `(p,q)` is the k-agreement pair.

After the canonical substitution,

```text
c_+ U=D+A=g b,
c_- V=D-A=g a,
```

so the left side is

```text
(D+A)^2-(D-A)^2
 =4DA
 =g^2(b^2-a^2).
```

Merged s7-46 already identifies the same physical packet by

```text
4 r_e s_e epsilon_k p q = 4DA.
```

Therefore the first reciprocal equation adds no new polynomial-density condition after the canonical allocation data are fixed. It reconstructs / filters the divisor-many k-agreement product and its ordered split; it does not supply an independent saving.

```text
CANONICAL_FIRST_RECIPROCAL_SUBSTITUTION_EXACT=true
FIRST_RECIPROCAL_EQUATION_IS_RECONSTRUCTION_AFTER_CANONICAL_ALLOCATION=true
FIRST_RECIPROCAL_NEW_FIXED_POWER_SELECTOR=false
FIRST_RECIPROCAL_RECHARGE_ALLOWED=false
```

## 3. Consequence for the two-factor density receiver

Merged 4ea gives

```text
mu_G = mu_can * mu_recip.
```

The calculation above shows that the `mu_recip` factor cannot obtain a fixed-power loss from the first reciprocal equation itself. After one canonical allocation witness is fixed, the only genuinely unresolved reciprocal acceptance is the opposite/second reciprocal difference-of-squares system together with its row/post-column physical filters.

Thus

```text
RECIPROCAL_CONDITIONAL_FIRST_LAYER_DISCHARGED=true
RECIPROCAL_CONDITIONAL_REDUCED_TO_SECOND_RECIPROCAL_AND_POST_COLUMN_FILTER=true
```

This is a receiver contraction, not a strict saving.

## 4. Next

Stage14-4ec should read the second reciprocal equation in the X13 reverse quantifier order and turn the remaining acceptance into an explicit divisor-pair predicate for one fixed difference-of-squares integer.

## Boundary

```text
STAGE14_4EB=COMPLETE_CANONICAL_FIRST_RECIPROCAL_TAUTOLOGY_AND_SECOND_LAYER_LOCALIZATION
CANONICAL_FIRST_RECIPROCAL_SUBSTITUTION_EXACT=true
FIRST_RECIPROCAL_EQUATION_IS_RECONSTRUCTION_AFTER_CANONICAL_ALLOCATION=true
FIRST_RECIPROCAL_NEW_FIXED_POWER_SELECTOR=false
RECIPROCAL_CONDITIONAL_FIRST_LAYER_DISCHARGED=true
RECIPROCAL_CONDITIONAL_REDUCED_TO_SECOND_RECIPROCAL_AND_POST_COLUMN_FILTER=true
CANONICAL_ALLOCATION_FIXED_POWER_DEFICIT_PROVED=false
RECIPROCAL_CONDITIONAL_FIXED_POWER_DEFICIT_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=false
NEXT=Stage14-4ec
```
