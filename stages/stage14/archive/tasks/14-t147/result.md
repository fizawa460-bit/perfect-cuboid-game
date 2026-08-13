# Stage14-t147 — restore the ordinary Gaussian residue denominator in endpoint capacity

## Status

`COMPLETE_ORDINARY_RESIDUE_DENOMINATOR_RESTORATION_AND_D_SQUARED_CAPACITY_GAIN`

Consumes merged `Stage14-t146`, merged `Stage14-t135`, and merged `Stage14-Work-byX37` from latest main.

The entering endpoint branches already have one fixed cofactor residue and one fixed prime residue modulo the odd squarefree selector modulus `d=B^o(1)`.  Stage14-t145 intentionally dropped the ordinary-residue denominator in order to expose only the host factor.  This stage restores that denominator exactly.

## 1. Exact size of the ordinary Gaussian residue group

Write

```text
R_d=(Z[i]/d Z[i])^x.
```

For every odd prime `p|d`, CRT and the split/inert alternatives give

```text
p == 1 (mod 4): |(Z[i]/pZ[i])^x|=(p-1)^2,
p == 3 (mod 4): |(Z[i]/pZ[i])^x|=p^2-1.
```

Equivalently, with `chi4` the nontrivial character modulo four,

```text
|(Z[i]/pZ[i])^x|=(p-1)*(p-chi4(p)).
```

Hence, because `d` is odd and squarefree,

```text
boxed:
|R_d|
 = product_{p|d} (p-1)(p-chi4(p))
 = phi(d) * |G(d)|.                               (1.1)
```

Merged t87 gives `|G(d)|=d*B^o(1)`.  Standard elementary Euler-product bounds give `phi(d)=d*B^o(1)` on the present `d=B^o(1)` range.  Therefore

```text
boxed:
|R_d|=d^2*B^o(1),                                 (1.2)
1/|R_d| <= B^o(1)/d^2.                            (1.3)
```

No equidistribution theorem is used.

```text
ORDINARY_GAUSSIAN_RESIDUE_GROUP_ORDER_EXACT=true
ORDINARY_GAUSSIAN_RESIDUE_GROUP_ORDER=phi(d)*|G(d)|
ORDINARY_GAUSSIAN_RESIDUE_GROUP_ORDER_SCALE=d^2*Bo1
```

## 2. Restore the denominator in the endpoint principal baseline

Merged t135 defines the fixed-residue principal baseline exactly as

```text
M_Y
 = 1/|R_d| * sum_{z in Z(Y)} |P_z|.
```

Merged t145 gives

```text
#Z(Y) <= B^o(1)*(Y/(h*k0)+1),
|P_z| <= O(Y+1).
```

Combining these with (1.3),

```text
boxed:
M_Y
 <= B^o(1)/d^2
    * (Y/(h*k0)+1)
    * (Y+1).                                      (2.1)
```

Thus t145's host-normalized capacity is sharpened by a further `d^-2` factor.  Since `d=B^o(1)`, this does not alter the fixed B-power exponent by itself, but it is a genuine quantitative pseudopolynomial gain and must be retained in subsequent endpoint localization.

```text
RESIDUE_NORMALIZED_ENDPOINT_CAPACITY_PROVED=true
RESIDUE_NORMALIZED_ENDPOINT_CAPACITY=M_Y_LE_BO1_OVER_d2_TIMES_(Y_over_hk0_plus_1)_TIMES_(Y_plus_1)
D_SQUARED_PRINCIPAL_CAPACITY_GAIN_PROVED=true
D_SQUARED_GAIN_FIXED_POWER=false
```

## 3. Beyond-Mitsui consequence

On the beyond-Mitsui endpoint branches,

```text
d > exp(c_safe*sqrt(log B)).
```

Therefore (2.1) contains the explicit additional suppression

```text
1/d^2
 < exp(-2*c_safe*sqrt(log B)).                    (3.1)
```

This is stronger than the host-only pseudopolynomial factor recorded in t145, but remains `B^{-o(1)}` and cannot alone be promoted to a strict power saving.

```text
BEYOND_MITSUI_RESIDUE_CAPACITY_GAIN=PSEUDOPOLYNOMIAL_D_SQUARED
BEYOND_MITSUI_RESIDUE_CAPACITY_FIXED_POWER_SAVING=false
```

## 4. Receiver and H decision

This stage restores an exact coefficient already present in the t135 baseline.  It does not yet separate sparse-cofactor from many-cofactor realizations, so the mechanism labels from t146 are retained until t148/t149.

No new theorem audit is justified: the prime-distribution hypotheses are unchanged from tH30/tH32.

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
NEXT_INTERNAL_TARGET=SparseVersusManyCofactorDisjointLocalizationWithResidueNormalizedBaseline
NEXT=Stage14-t148
```
