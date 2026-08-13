# Stage14-4bq — diagonal-pair genus-one closure

## Result

Merged 4bo leaves the normalized good-cell residual

```text
C=(a0,b0,c0,d0),   #C << B^(3/7+o(1)),
q11,q12,q21,q22 pairwise coprime,
Q=q11*q12*q21*q22>B^(16/21),
```

with merged s6-08 detector

```text
F=(q12^2*a0*d0)^2-(q21^2*b0*c0)^2,
G=(q22^2*b0*d0)^2-(q11^2*a0*c0)^2,
F*G=square>0.
```

Define the two diagonal products

```text
U=q11*q22,
V=q12*q21,
UV=Q.
```

The key point is that `F` depends only on `(q12,q21)` and `G` only on `(q11,q22)`.

### Main diagonal moves on genus one

Fix `(q12,q21)` and the normalized core. Put `x=q11`, `y=q22`. Then `F=F0!=0` is fixed and

```text
Y^2=F0*(y^4*(b0*d0)^2-x^4*(a0*c0)^2).
```

With `t=x/y`, `W=Y/y^2`,

```text
W^2=F0*((b0*d0)^2-(a0*c0)^2*t^4).
```

This is a smooth genus-one quartic with rational 2-torsion. The merged t22 bounded-height mechanism gives `B^o(1)` admissible reduced rational slopes. Since `gcd(q11,q22)=1`, the reduced slope uniquely determines `(q11,q22)`. Hence

```text
# {(q11,q22) | fixed core,q12,q21} <= B^o(1).
```

### Off diagonal moves on genus one

Fix `(q11,q22)` and the core. Put `x=q12`, `y=q21`. Then `G=G0!=0` is fixed and

```text
W^2=G0*((a0*d0)^2*t^4-(b0*c0)^2),
t=x/y.
```

The same argument and `gcd(q12,q21)=1` give

```text
# {(q12,q21) | fixed core,q11,q22} <= B^o(1).
```

## Count only the smaller diagonal

Because

```text
UV=Q<=X2<=B,
```

we have

```text
min(U,V)<=B^(1/2).
```

Split into `U<=V` and `V<U`. Enumerating the smaller diagonal pair costs at most

```text
sum_{n<=B^(1/2)} tau(n)=B^(1/2+o(1)).
```

The opposite diagonal then has only `B^o(1)` possibilities by the genus-one argument above. Therefore, per normalized core,

```text
# good-cell residual states <= B^(1/2+o(1)).
```

Using the merged 4bo core count,

```text
boxed:
E_good-res(B) << B^(3/7+1/2+o(1))
              = B^(13/14+o(1)).
```

This closes the entire 4bo good-cell residual, including the 4bp hard complement; no further largest-prime decomposition is needed for the current exponent ledger.

## Full-family recombination

Use the exhaustive merged sector split:

```text
4bl small partner leg:  B^(20/21+o(1)),
4bm cross branch:       B^(61/63+o(1)),
4bq good-cell residual: B^(13/14+o(1)).
```

In denominator 126 these are

```text
120/126, 122/126, 117/126.
```

Hence

```text
boxed:
V(B) << B^(61/63+o(1)).
```

The previous whole-family exponent was `41/42=123/126`, so

```text
boxed:
delta_post = 41/42-61/63 = 1/126.
```

This is the first proved positive whole-family post-local saving on the direct 14-4 main track.

The square-root target is not proved. The remaining gap is

```text
61/63-1/2=59/126.
```

The active bottleneck is now the merged 4bm cross branch at exponent `61/63`; the good-cell residual is strictly smaller.

## Boundary

```text
STAGE14_4BQ=DIAGONAL_PAIR_GENUS_ONE_CLOSURE_AND_FIRST_FULL_POST_LOCAL_SAVING
DIAGONAL_PRODUCTS_UV_EQUAL_Q=true
MAIN_DIAGONAL_MOVING_SLOPE_GENUS_ONE=true
OFF_DIAGONAL_MOVING_SLOPE_GENUS_ONE=true
DIAGONAL_PAIR_SLOPE_TO_INTEGER_PAIR_INJECTIVE=true
FIXED_CORE_FIXED_ONE_DIAGONAL_OTHER_DIAGONAL_MULTIPLICITY=B^o(1)
SMALLER_DIAGONAL_PRODUCT_LE_B_HALF=true
GOOD_CELL_RESIDUAL_BOUND=B^(13/14+o(1))
WHOLE_FAMILY_SECTOR_MAX_EXPONENT=61/63
WHOLE_FAMILY_POST_LOCAL_SAVING=1/126
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=true
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=61/63
REMAINING_GAP_TO_SQRT=59/126
SQRT_B_UPPER_BOUND_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-4br
```
