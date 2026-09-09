# Stage35-EX Goal4BN source lock — common-W primary space-root ray product and order-two secondary witness

Scope: continue exact-green Goal4BM. Audited authority remains V74 / Goal4AK. Goal4BN asks whether the three primary space square roots
`Psi_a,Psi_b,Psi_c`, which all arise from the same space diagonal `W`, force the BJ orientation carrier `Xi` into a proper subset of the
16 primary ray classes modulo `lambda^7`, especially whether the Goal4BM order-two blind class can be excluded.

The answer is **no with the retained source equations**. The common `W` does give an exact three-way norm relation and three source-canonical
common-norm Gaussian ratios, but these are norm/Hilbert-90 data rather than a new ray obstruction. More decisively, the complete face-plus-space
system has a `41`-adic secondary local model in which the selected primary prime is `5+4*i`, the Goal4BM order-two ray class, and either
`sigma_a=+1` or `sigma_a=-1` can occur while the same common `W` equations remain satisfied.

## 1. Common-W norm factorization

Goal4BG gives pairwise-coprime odd reservoirs

```text
h_a=gcd(a,r_BC),
h_b=gcd(b,r_AC),
h_c=gcd(c,r_AB),
```

and each `h_i` divides `W`. Put

```text
H=h_a*h_b*h_c,
T=W/H.                                                (BN-HT)
```

Because the `h_i` are pairwise coprime, `H|W`. The three primary space roots satisfy

```text
N(Psi_a)=W/h_a=h_b*h_c*T,
N(Psi_b)=W/h_b=h_a*h_c*T,
N(Psi_c)=W/h_c=h_a*h_b*T.                            (BN-Psi-norms)
```

Thus the common diagonal already forces one exact common rational cofactor `T`.

## 2. Three common-norm Gaussian ratios

Define in `Q(i)^*`

```text
R_a=Psi_b*Psi_c/(h_a*Psi_a),
R_b=Psi_a*Psi_c/(h_b*Psi_b),
R_c=Psi_a*Psi_b/(h_c*Psi_c).                         (BN-R)
```

Then directly from `(BN-Psi-norms)`,

```text
N(R_a)=N(R_b)=N(R_c)=T.                              (BN-R-norm)
```

Write the unstripped space factors

```text
Z_a=D_BC+i*A,
Z_b=D_AC+i*B,
Z_c=D_AB+i*C.
```

Since `Omega_i=Z_i/h_i=nu_i*Psi_i^2`, the ratios satisfy exactly

```text
R_a/R_b=(nu_a/nu_b)*(Z_b/Z_a),
R_a/R_c=(nu_a/nu_c)*(Z_c/Z_a).                       (BN-R-ratio)
```

Each right-hand side has rational norm `1`. Hence the common-W coupling produces explicit source norm-one phase ratios, but no new fixed value:
the ratios are already written as quotients of source factors of equal norm `W^2`.

This is a genuine coupling, but it is descriptive rather than obstructive.

## 3. Fixed-i ray coordinate forced only through the common norm

Every `h_i` is a product of primes `1 mod 4`, and each `W/h_i` is an odd primitive Pythagorean hypotenuse, hence `1 mod 4`. Therefore `T=1 mod 4`.

Goal4BL gives, on primary elements,

```text
chi_i(alpha)=i^((N(alpha)-1)/4).
```

Consequently

```text
chi_i(R_a)=chi_i(R_b)=chi_i(R_c)=i^((T-1)/4).        (BN-fixed-i)
```

So common `W` fixes the **norm coordinate** of the three derived ratios. It supplies no formula fixing their independent ramified
`chi_lambda` coordinates. In particular this norm equality alone does not place `Xi` in a proper subset of the Goal4BM 16-class ray group.

## 4. A full 41-adic secondary common-W model

The stronger question is whether the complete common-W source equations could exclude the order-two class represented by

```text
pi=5+4*i,
N(pi)=41,
(e_i(pi),e_lambda(pi))=(2,0).                        (BN-pi41)
```

They do not.

Work over `Z_41`. Fix

```text
ell=41,
t=9,
t^2+1=82=2*41,
u=t^2-1=80,
v_+=2*t=18,
v_-=-2*t=-18,
q=t^2+1=82.                                          (BN-41-data)
```

Then

```text
u^2+v_+^2=q^2=u^2+v_-^2.                             (BN-uvq)
```

Set

```text
x=y=z=c=1,
a=ell*u,
r_BC=ell*v_+    or    ell*v_-,
W=ell*q.                                             (BN-local-base)
```

Hence exactly

```text
a^2+r_BC^2=W^2.
```

Choose the unique `41`-adic Hensel lift `b` with

```text
b == t mod 41,
b^2+1=r_BC^2.                                        (BN-b-lift)
```

It exists because modulo `41` the equation is `b^2+1=0` at `b=t`, and `2t` is a unit.

Then choose Hensel lifts

```text
r_AB^2=a^2+b^2,   r_AB == b mod 41,
r_AC^2=a^2+1,     r_AC == 1 mod 41.                  (BN-face-lifts)
```

Their derivatives are units modulo `41`. Thus the complete reduced face system holds, and automatically

```text
W^2=r_AB^2+1=r_AC^2+b^2=a^2+r_BC^2.                 (BN-common-W)
```

So all three face squares and all three presentations of the same common space diagonal hold in `Z_41`.

For an explicit finite certificate modulo `41^4=2825761`, one may take for the `v_+` branch

```text
a      = 3280,
r_BC   = 738,
W      = 3362,
b      = 363474,
r_AB   = 1573794,
r_AC   = 2553440,                                    (BN-mod41-4)
```

and every equation in `(BN-b-lift)`, `(BN-face-lifts)`, `(BN-common-W)` holds modulo `41^4`.

## 5. The model is secondary and realizes both sigma signs at the same selected prime

In either branch,

```text
v_41(a)=v_41(r_BC)=1,
v_41(W)=2.
```

Therefore

```text
v_41(h_a)=1,
41 | W/h_a,                                          (BN-secondary)
```

while `h_b,h_c` are `41`-adic units. This is exactly Goal4BH's secondary tied-valuation case.

The BF source orientation is

```text
iota_a=b == 9 mod 41.
```

Since `5+4*i=0` implies `i=9 mod 41`, the selected Gaussian prime is exactly the primary prime `pi=5+4*i` from `(BN-pi41)`.

The secondary root is

```text
lambda_a=(r_BC/41)/(a/41)=v_\pm/u mod 41.
```

Because `u=80==-2 mod 41`,

```text
v_+/u = -9 mod 41  -> sigma_a=-1,
v_-/u =  9 mod 41  -> sigma_a=+1.                   (BN-both-sigma)
```

Thus **the same selected order-two primary ray class** is compatible with either BJ orientation sign while the full common-W local system is retained.

The sign of the `41`-adic square root `r_BC` is a finite-place root choice; no global positive endpoint is being asserted.

## 6. Why common W cannot close Goal4BM at this level

The Goal4BM obstruction candidate fails at the order-two class because every conductor-`lambda^7` character has the same value on exponent `+1`
and exponent `-1` there. Goal4BN shows that the extra common-W equations do not locally exclude that class and do not locally fix its `sigma`.

Therefore the retained common-W primary-root relations yield

```text
common rational norm T = yes;
three common-norm Gaussian ratios = yes;
fixed-i coordinate relation = yes;
proper lambda^7 ray subset for Xi = not obtained;
order-two ray class excluded = no;
sigma fixed at order-two class = no;
branch pruning = no.                                 (BN-boundary)
```

This does not prove that no deeper global theorem exists. It proves that the currently retained common-W identities do not supply the missing
lambda^7 ray exclusion.

## 7. Verdict

Certified provisionally:

```text
COMMON_W_COFACTOR_T=true;
THREE_COMMON_NORM_RATIOS_RI=true;
RI_NORM_EQUALS_T=true;
RI_RATIO_SOURCE_NORM_ONE=true;
FIXED_I_COORDINATE_OF_RI_COMMON=true;
FULL_41_ADIC_FACE_PLUS_SPACE_MODEL=true;
ORDER_TWO_PI_5_PLUS_4I_SECONDARY_LOCALLY_COMPATIBLE=true;
BOTH_SIGMA_SIGNS_AT_SAME_SELECTED_PI_LOCALLY_COMPATIBLE=true;
COMMON_W_FORCES_PROPER_LAMBDA7_XI_SUBSET=false;
ORDER_TWO_RAY_CLASS_EXCLUDED=false;
BRANCH_PRUNING=false.
```

Not certified:

```text
global endpoint realizing the 41-adic witness;
universal sigma product;
any h_i=1;
any d_i=1;
E1;
Stage35 closure;
Perfect Cuboid existence/nonexistence.
```

Next exact leaf:

```text
35EX-35_GOAL4BO_DEEPER_LAMBDA8_ORDER_LIFT_PREFLIGHT
```

Question: now that common `W` does not exclude the first blind order-two class, test the next ramified conductor. For `pi=5+4*i`,
`v_lambda(pi^2-1)=7` and `v_lambda(pi^4-1)=9`, so its class has order `4` modulo `lambda^8`; determine whether a conductor-`lambda^8`
character can distinguish the two orientations and, crucially, whether its value is source-controlled or merely starts an unbounded deeper
ray tower.

No merge. No hostile-audit credit. MAIN-STATE remains V74 / Goal4AK.
