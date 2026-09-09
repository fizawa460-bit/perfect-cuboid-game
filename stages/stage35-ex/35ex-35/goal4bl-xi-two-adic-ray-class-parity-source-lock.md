# Stage35-EX Goal4BL source lock — fixed-i quartic character collapses to rational norm mod 16

Scope: continue exact-green Goal4BK. Audited authority remains V74 / Goal4AK. Goal4BL computes the deeper two-adic/ray-class value of the support-cleaned carrier `Xi` for the canonical fixed-unit quartic character
`chi_i(alpha)=(i/alpha)_4`.

The result sharpens Goal4BK: the apparent two-adic compensator is not an independent hidden Gaussian phase. On odd **primary** Gaussian integers the fixed-i character factors through the rational norm modulo `16`. Consequently its value on `Xi` is computable from the rational norms of the BJ numerator/denominator. This gives an exact formula, but no new obstruction: it is a weighted restatement of the same secondary-orientation partition, and it is blind to the sign at reservoir primes `ell == 1 or 9 mod 16`.

## 1. Primary residue and exact ray depth

Put

```text
lambda = 1+i.
```

For a primary odd Gaussian integer

```text
alpha=A+B*i,
A odd,
B even,
A+B == 1 mod 4,                                      (BL-primary)
```

Goal4BK uses the supplementary law

```text
chi_i(alpha)=(i/alpha)_4=i^((1-A)/2).                 (BL-chi-A)
```

Since

```text
lambda^6=(1+i)^6=-8*i,
```

reduction modulo `lambda^6` is equivalent, up to a unit, to reduction modulo `8` in both integer coordinates. Thus `A mod 8` determines `chi_i(alpha)`.

The primary residue table is

```text
A mod 8   B mod 4   N(alpha) mod 16   chi_i(alpha)
   1         0              1               1
   3         2             13              -i
   5         0              9              -1
   7         2              5               i.        (BL-ray-table)
```

Equivalently, every odd primary `alpha` satisfies

```text
N(alpha) == 3-2*A mod 16,                             (BL-N-A)
```

and therefore

```text
chi_i(alpha)=i^((N(alpha)-1)/4).                      (BL-chi-N)
```

The exponents in `(BL-chi-A)` and `(BL-chi-N)` agree modulo `4`.

So the fixed-i quartic character is a ray character of depth at most `lambda^6`, but on the primary subgroup it actually descends to the rational norm modulo `16`.

## 2. The deeper sign is not already fixed at lambda^5

The stronger congruence `mod lambda^5` is still insufficient, even after the norm modulo `8` is known.

Two exact ambient diagnostics are:

```text
alpha_1=1,
beta_1=-3-4*i,
v_lambda(beta_1-alpha_1)=5,
N(alpha_1)==N(beta_1)==1 mod 8,
chi_i(alpha_1)=1,
chi_i(beta_1)=-1;                                    (BL-witness-real)
```

and

```text
alpha_2=-1-2*i,
beta_2=3+2*i,
v_lambda(beta_2-alpha_2)=5,
N(alpha_2)==N(beta_2)==5 mod 8,
chi_i(alpha_2)=i,
chi_i(beta_2)=-i.                                    (BL-witness-imag)
```

These are ray-class diagnostics only, not endpoint constructions.

## 3. Apply the norm formula to the BJ carrier

Goal4BJ writes

```text
Xi=(M_a^-*M_b^-*M_c^-)/(M_a^+*M_b^+*M_c^+).          (BL-Xi)
```

Define positive rational norms

```text
R_- = N(M_a^-*M_b^-*M_c^-),
R_+ = N(M_a^+*M_b^+*M_c^+).                          (BL-Rpm)
```

Every prime factor of `R_-R_+` is a reservoir prime, hence `1 mod 4`; therefore

```text
R_- == R_+ == 1 mod 4.
```

By `(BL-chi-N)` and multiplicativity,

```text
chi_i(Xi)=i^((R_- - R_+)/4).                          (BL-Xi-character)
```

This is the exact deeper two-adic/ray-class value requested by Goal4BK. No unknown Gaussian leading unit remains for this particular dual character.

The set of secondary reservoir primes has squarefree rational product

```text
S_sec = R_-*R_+
      = product_i gcd(s_i, W/h_i),                    (BL-Ssec)
```

where `i=a,b,c`. Squaring `(BL-Xi-character)` gives

```text
chi_i(Xi)^2=(2/S_sec),                                (BL-Xi-square)
```

with the usual Jacobi symbol. Thus the square of the quartic value depends only on which reservoir primes are secondary, not on their `sigma` orientations.

## 4. Primewise mod-16 sensitivity

For a selected primary prime `pi|ell` with `ell=1 mod 4`,

```text
chi_i(pi)=i^((ell-1)/4).                              (BL-prime-char)
```

Hence

```text
ell mod 16    chi_i(pi)    exponent +1 vs -1
    1             1        same / orientation blind
    5             i        i versus -i
    9            -1        same / orientation blind
   13            -i        -i versus i.               (BL-prime-table)
```

Therefore the canonical fixed-i dual detects the BJ sign only at reservoir primes `5 or 13 mod 16`. It cannot distinguish `sigma=+1` from `sigma=-1` at `1 or 9 mod 16`.

This is stronger than Goal4BK's conditional statement “order-four values can detect orientation”: the exact sensitivity classes are now identified.

## 5. The primitive parity branches do not remove the blind mod-16 classes

Goal4BE proves only

```text
ell|s_a*s_b*s_c => ell=1 mod 4.
```

All four residue classes `1,5,9,13 mod 16` are locally compatible with the reservoir equation. For direction `a`, take modulo `ell`

```text
x=y=c=1,
a=0,
b=iota,
iota^2=-1.                                            (BL-local-model)
```

Then

```text
r_BC^2=(x*b)^2+(y*c)^2 == 0 mod ell,
iota_a=x*b/(y*c)=iota,
(2*x*y*b*c/ell)=1.
```

Exact diagnostics are

```text
ell=5,  iota=2;
ell=13, iota=5;
ell=17, iota=4;
ell=41, iota=9.                                      (BL-four-classes)
```

representing `5,13,1,9 mod 16` respectively.

Because these are odd-prime congruences, the Chinese remainder theorem permits simultaneous imposition of any one of the three retained 2-adic primitive parity branches. This is only a local compatibility statement; no global perfect-cuboid endpoint is asserted.

Thus the Stage35-EX parity dictionary does not upgrade the reservoir restriction from `1 mod 4` to the order-four-sensitive classes `5 or 13 mod 16`.

## 6. What the fixed-i global product actually says

Combining `(BL-prime-char)` with the BJ valuations,

```text
chi_i(Xi)
 = product_{secondary ell} i^(-sigma(ell)*(ell-1)/4). (BL-product)
```

Here `sigma=-1` corresponds to valuation `+1`, and `sigma=+1` to valuation `-1`.

But `(BL-product)` is exactly the evaluation of the source-defined carrier `Xi`; by `(BL-Xi-character)` its value is already the rational norm residue `i^((R_- - R_+)/4)`. Therefore fixed-i quartic reciprocity supplies no second independent equation. It evaluates the existing orientation partition rather than constraining it.

In particular:

```text
the two-adic value for chi_i is computable = yes;
an independent two-adic obstruction = no;
all sigma bits detected by chi_i = no;
universal sigma product = no.                         (BL-boundary)
```

## 7. Verdict

Certified provisionally:

```text
LAMBDA6_RAY_DEPTH_SUFFICIENT=true;
LAMBDA5_PLUS_NORM_MOD8_INSUFFICIENT=true;
FIXED_I_CHARACTER_DESCENDS_TO_NORM_MOD16_ON_PRIMARY=true;
CHI_I_XI_EXACT_NORM_FORMULA=true;
CHI_I_XI_SQUARE_EQUALS_TWO_JACOBI_OF_SECONDARY_SUPPORT=true;
FIXED_I_ORIENTATION_SENSITIVE_CLASSES={5,13} mod 16;
FIXED_I_ORIENTATION_BLIND_CLASSES={1,9} mod 16;
ALL_FOUR_RESERVOIR_MOD16_CLASSES_LOCALLY_COMPATIBLE=true;
FIXED_I_GLOBAL_PRODUCT_INDEPENDENT_RELATION=false;
BRANCH_PRUNING=false.
```

Not certified:

```text
universal sigma product;
quartic reciprocity contradiction;
any h_i=1;
any d_i=1;
E1;
Stage35 closure;
Perfect Cuboid existence/nonexistence.
```

The fixed-i dual route is therefore fail-closed as a universal orientation obstruction. A genuinely new dual must see information not determined by the rational norm. The next exact leaf is

```text
35EX-35_GOAL4BM_RAMIFIED_ONE_PLUS_I_QUARTIC_DUAL_PREFLIGHT
```

Question: test the ramified supplementary quartic character with numerator `1+i` (or its equivalent ray-class functional) against the BJ carrier. Unlike the fixed-i character, it can depend on the imaginary/ray residue of a primary Gaussian prime and may distinguish information lost by the norm-only formula. Determine whether it is source-controlled or merely introduces another free 2-adic phase.

No merge. No hostile-audit credit. MAIN-STATE remains V74 / Goal4AK.
