# Stage14-toolbox-ab — cross-route variable and normalization dictionary

## Purpose

Stage14-toolbox-aa created the permanent reusable research-toolbox contract. The first extraction stage now resolves the highest-risk maintenance problem shared by Stage14 `14-4` and `s`: the same historical letters are reused for different mathematical objects, while the two routes now share a long normalized witness chain.

Stage14-toolbox-ab packages only merged results. It does not prove a new Stage14 theorem.

## Canonical translation chain

The merged main/s interface can now be read as

```text
first physical Pythagorean face
(S,X,H)
  -> Euclid chart (m,n)
  -> five odd support columns
  -> rational witness Z=A/D^2, W=Y/D^3
  -> factors G0,G1,G2
  -> signed kernels di and square variables ui
  -> odd edge packet (a,b,c) with finite tau packet
  -> shared fixed-packet two-quadrics
  -> physical compact torsion selector D_T
  -> actual two-face variables (S2,X2,H2,d)
  -> physical gluing G=gcd(S,S2)*d
  -> gaps U,V and conjugate numerators
  -> partner half-angle t and cancellation cofactor k.
```

The human-readable master dictionary is

```text
docs/stage14-toolbox/variable-dictionary.md
```

and five canonical cards are registered in `docs/stage14-toolbox/index.json`.

## Canonical cards

### 1. Euclid five-column normalization

```text
TB-DICTIONARY-euclid-five-columns
```

Locks

```text
S=2mn
X=(m-n)(m+n)
H=m^2+n^2
```

and the five odd moving columns

```text
m, n, m-n, m+n, m^2+n^2.
```

It explicitly warns that the historical s5 `A`/`D` column labels are not the rational witness numerator/denominator variables.

### 2. Rational witness -> kernel packet -> two quadrics

```text
TB-DICTIONARY-witness-kernel-two-quadrics
```

Locks

```text
Z=A/D^2
W=Y/D^3
G0=A
G1=A-S^2D^2
G2=A+X^2D^2
Gi=di ui^2

d0=tau0*a*b
d1=tau1*a*c
d2=tau2*b*c
```

and the shared normalized main/s two-quadrics

```text
d0u0^2-d1u1^2=S^2D^2
d2u2^2-d0u0^2=X^2D^2.
```

This is the exact bridge between merged Stage14-4bg and Stage14-s6-01.

### 3. Denominator selectors

```text
TB-DICTIONARY-denominator-selectors
```

Separates three objects that must never be silently identified:

```text
D      = denominator of one chosen rational witness
D_min  = least bounded-height denominator for an abstract packet
D_T    = denominator of the canonical compact physical torsion translate.
```

For the physical packet containing the canonical translate only,

```text
D_min <= D_T.
```

### 4. Physical pair / compact half-angle variables

```text
TB-DICTIONARY-physical-pair-compact-half-angle
```

Locks

```text
g=gcd(S,S2)
G=g*d
R=H2-S2
Nplus =HG+S^2H2+X^2S2
Nminus=HG-S^2H2-X^2S2
U=G-HS2
V=HH2-G
```

with

```text
Z_P=Nplus/R
Z_T=-Nminus/R=-UV/X2^2
D_T^2=R/gcd(Nminus,R)=X2^2/gcd(X2^2,UV).
```

For partner Euclid parameters:

```text
R=kappa*t^2
D_T|t
k=t/D_T
gcd(Nminus,R)=kappa*k^2.
```

### 5. Symbol-collision warning

```text
TB-WARNING-cross-route-symbol-collisions
```

The main collisions frozen are

```text
A        rational numerator vs s5 A-column
D        witness denominator vs s5 D-column vs D_min vs D_T
G_i      witness factors vs physical G=g*d
U,V      physical gaps vs generic dyadic box variables
d        physical space diagonal vs d_i signed kernels
a,b,c    witness edge-kernel divisors vs generic cuboid edge names.
```

## Source provenance

Canonical cards use only merged sources:

```text
Stage14-4bg   PR #344  merge 80e59daf772f39ec6d48435717440e1c120c4e47
Stage14-s6-01 PR #345  merge 86b91ffcd8bae79452ef75f187c8570a3819d386
Stage14-4bj   PR #355  merge 7ab3c21cc07714b24edfa1a36425b4beaeb2a6e7
Stage14-s6-05 PR #356  merge c2273d0388b48f8fb51d9dc69d8977efbc83db37
Stage14-s6-06 PR #360  merge 42f4315b0659bd402a94adeb8822588ea153305a
```

Open Stage14-4bk PR #359 was inspected only as current context and is deliberately excluded from canonical provenance.

## What this stage changes operationally

A later main/s worker should no longer need to reread the full historical chain merely to determine which `D`, `G`, `U`, `a`, or `A` a formula means. The canonical dictionary makes the normalization boundary explicit before theorem reuse.

This does **not** authorize automatic transfer of estimates merely because the variables have been identified. Quantifier/scale boundaries remain intact:

```text
fixed packet != moving family
coordinate density != packet existence
unweighted != arbitrary weight
M-scale != physical B-scale
abstract packet != physical reconstructed pair.
```

## Validation

The dedicated deterministic audit checks:

- all five canonical IDs are in the registry;
- type/status/source PR/source merge SHA match their card headers;
- source merge SHAs are 40-hex values;
- every card contains all required schema sections;
- the master dictionary contains the locked normalization identities;
- `D`, `D_min`, and `D_T` are explicitly separated;
- open PR #359 is not a canonical source;
- the registry advances to `Stage14-toolbox-ac`.

## Boundary

```text
STAGE14_TOOLBOX_AB=COMPLETE_CROSS_ROUTE_VARIABLE_AND_NORMALIZATION_DICTIONARY
CANONICAL_DICTIONARY_CARD_COUNT=4
CANONICAL_WARNING_CARD_COUNT=1
MAIN_S_SHARED_WITNESS_CHAIN_NORMALIZED=true
EUCLID_FIVE_COLUMN_DICTIONARY_FROZEN=true
WITNESS_KERNEL_TWO_QUADRICS_DICTIONARY_FROZEN=true
D_DMIN_DT_SEPARATED=true
PHYSICAL_PAIR_COMPACT_HALF_ANGLE_DICTIONARY_FROZEN=true
CROSS_ROUTE_SYMBOL_COLLISION_WARNING_FROZEN=true
OPEN_PR_USED_AS_CANONICAL_SOURCE=false
TOOLBOX_OWNS_NEW_STAGE14_THEOREM=false
NEXT=Stage14-toolbox-ac current exponent and saving ledger
```
