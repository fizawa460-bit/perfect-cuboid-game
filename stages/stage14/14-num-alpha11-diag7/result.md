# Stage14-numα11-diag7 — conditional second-face survival

## Result

Stage14-numα11-diag7 decomposes the Stage13 -> Stage14 transition by conditioning on the **source integral face**.

For exactly-two pair counts

```text
a = ab & ac
b = ab & bc
c = ac & bc
```

define the exactly-two endpoint loads

```text
E_ab = a+b
E_ac = a+c
E_bc = b+c.
```

On every matched Stage13 cutoff through `B=100000`, the triple count is zero and the exact identity

```text
A_q - N1_q = E_q
```

holds categorywise. Thus

```text
S_q = E_q/A_q
```

is exactly the finite conditional rate that a raw face incidence of type `q` acquires a second integral face.

## B=100000

Raw face incidences:

```text
A = (84212, 43236, 40760)
```

Exactly-two pair counts:

```text
(a,b,c) = (33,33,23)
```

Endpoint loads:

```text
(E_ab,E_ac,E_bc) = (66,56,56)
```

Second-face survival rates:

```text
S_ab = 0.000783736285
S_ac = 0.001295216949
S_bc = 0.001373895976
```

Relative to `bc=1`:

```text
ab : ac : bc = 0.570448 : 0.942733 : 1
```

So the large `ab` source population has a substantially **lower** second-face survival rate than `ac` and `bc`. This is the direct finite mechanism that flattens the Stage13 one-face/raw-face imbalance before the Stage14 exactly-two pair law is formed.

The destination split conditional on survival is

```text
from ab: ac 50.0%, bc 50.0%
from ac: ab 58.93%, bc 41.07%
from bc: ab 58.93%, ac 41.07%
```

## Exact algebraic bridge to 2:2:1

If the pair vector were exactly

```text
a:b:c = 2:2:1,
```

then the endpoint loads would be

```text
E_ab:E_ac:E_bc
 = (a+b):(a+c):(b+c)
 = 4:3:3.
```

Therefore a hypothetical Stage14 `2:2:1` limiting law is equivalent to a `4:3:3` limiting law for exactly-two face endpoints.

Combining this hypothetical endpoint target with the **proved Stage13 directional limit**

```text
P_inf = (0.5347369332, 0.2453591778, 0.2199038889)
```

would require the relative total second-face survival profile

```text
S_ab:S_ac:S_bc = 0.548317 : 0.896253 : 1
```

up to a common scale.

The empirical B=100k profile is

```text
0.570448 : 0.942733 : 1,
```

and its normalized-shape L1 distance to that hypothetical bridge target is

```text
0.022335699.
```

This numerical closeness is diagnostic only. At B=100k there are only `89` exactly-two objects.

## B=500,000,000 numerator-only structure

The frozen Stage14 population gives

```text
(a,b,c) = (1374,1371,750)
```

with pair proportions

```text
(0.393133, 0.392275, 0.214592)
```

and L1 distance `0.029184549` to `2:2:1`.

The corresponding endpoint loads are

```text
(E_ab,E_ac,E_bc) = (2745,2124,2121)
```

or

```text
1.294201 : 1.001414 : 1,
```

close to the `4:3:3` endpoint benchmark (`1.3333:1:1`). The normalized endpoint L1 distance to `4:3:3` is `0.014592275`.

The B500m destination mixes are already close to the exact `2:2:1` signatures:

```text
from ab: ac 50.0546%, bc 49.9454%
from ac: ab 64.6893%, bc 35.3107%
from bc: ab 64.6393%, ac 35.3607%
```

For exact `2:2:1`, these would be respectively `1/2:1/2`, `2/3:1/3`, `2/3:1/3`.

## Boundary

B500m contains only the exactly-two numerator population. The raw Stage13-style face denominators are not available at that cutoff, so **no B500m survival rates are invented or extrapolated**.

```text
STAGE14_NUM_ALPHA11_DIAG7=CONDITIONAL_SECOND_FACE_SURVIVAL_DIAGNOSTIC_COMPLETE
MATCHED_MAX_B=100000
RAW_MINUS_EXACT_ONE_EQUALS_EXACT_TWO_ENDPOINT_LOAD=true
PAIR_2_2_1_EQUIVALENT_TO_ENDPOINT_4_3_3=true
B100K_SURVIVAL_REL_BC=0.5704480528733604,0.9427329077620501,1
B100K_AB_SURVIVAL_LOWER_THAN_AC_BC=true
B500M_ENDPOINT_LOAD=2745,2124,2121
B500M_ENDPOINT_L1_TO_4_3_3=0.014592274678111639
B500M_RAW_FACE_DENOMINATORS_AVAILABLE=false
ASYMPTOTIC_SECOND_FACE_SURVIVAL_PROFILE_CLAIM=false
ASYMPTOTIC_TWO_FACE_DIRECTION_LAW_CLAIM=false
NEXT=Stage14-num-alpha11-diag8 extend matched raw-face denominators beyond B=100k
```
