# Stage14-t132 — localize projective depletion to one fixed cofactor class

## Status

`COMPLETE_FIXED_PROJECTIVE_COFACTOR_CLASS_LOCALIZATION`

Consumes merged `Stage14-t131`, merged `Stage14-t125/t126/t127`, completed merged `Stage14-tH29` as a negative theorem boundary, and merged `Stage14-Work-bsX31` as the latest integration boundary.

Fix the same live fixed-`U` packet, allowed Gaussian factor `a`, endpoint modulus

```text
d=B^o(1),
G=G(d),
g=|G|=B^o(1),
X_U=2B/(h*k0),
L_B=2*sqrt(B).
```

Let `Omega_nb` be the charged-once nonboundary physical primitive cofactor family. For every scalar norm `n` and projective cofactor class `c in G`, define

```text
Omega_{n,c}:={gamma in Omega_nb : N(gamma)=n, [gamma]=c},
W_c(n):=#Omega_{n,c}.
```

Then

```text
W_c(n)>=0,
sum_c W_c(n)=W_phys(n),
W_c(n)<=W_phys(n)<=B^o(1).
```

No multiplicativity of `W_c(n)` is asserted.

## 1. Exact nonnegative class decomposition

The endpoint relation is

```text
[gamma]*[a]*[pi_ell]=1 in G.
```

Hence, once the cofactor class is fixed to `c`, the accepted prime class is the fixed inverse class

```text
q_c:=c^(-1)*[a]^(-1).
```

For a scalar norm `n`, let

```text
P_n:= {canonical split pi_ell : L_B<ell<=X_U/n},
K_n(q):=#{pi in P_n : [pi]=q}.
```

The full physical selected-prime count decomposes exactly as

```text
T=sum_{c in G} T_c,

T_c:=sum_n W_c(n) K_n(q_c).
```

The principal baseline from t112/t126 decomposes with the same nonnegative class weights:

```text
M=sum_{c in G} M_c,

M_c:=1/g * sum_n W_c(n) |P_n|.
```

Every `T_c,M_c` is nonnegative. This is a direct class decomposition before any Fourier expansion.

```text
COFACTOR_PROJECTIVE_CLASS_NONNEGATIVE_DECOMPOSITION_EXACT=true
FIXED_COFACTOR_CLASS_HAS_FIXED_INVERSE_PRIME_CLASS=true
PRINCIPAL_BASELINE_DECOMPOSES_BY_SAME_COFACTOR_CLASSES=true
```

## 2. A bad packet localizes to one principal-scale fixed class

Assume a fixed-power depletion for some fixed `delta>0`:

```text
T<=B^(-delta) M.
```

Call a class `c` high-ratio when

```text
T_c>B^(-delta/2) M_c.
```

Since all terms are nonnegative,

```text
B^(-delta/2) * sum_{c high-ratio} M_c
 < sum_{c high-ratio} T_c
 <= T
 <= B^(-delta) M.
```

Therefore

```text
sum_{c high-ratio} M_c <= B^(-delta/2) M.
```

Thus the complementary low-ratio classes carry

```text
sum_{c low-ratio} M_c
 >= (1-B^(-delta/2)) M.
```

There are only `g=B^o(1)` projective classes. Hence at least one class `c_*` satisfies simultaneously

```text
M_{c_*}
 >= (1-B^(-delta/2)) M/g
 = B^(-o(1)) M,

T_{c_*}
 <= B^(-delta/2) M_{c_*}.
```

So any principal-scale fixed-power obstruction can be frozen to one exact cofactor projective class at only `B^o(1)` charged-once cost, while retaining a fixed positive depletion exponent.

```text
BAD_PACKET_LOCALIZES_TO_ONE_FIXED_PROJECTIVE_CLASS=true
LOCALIZED_CLASS_PRINCIPAL_MASS=BoMinus1_TIMES_TOTAL
LOCALIZED_CLASS_RETAINS_FIXED_POSITIVE_DEPLETION_POWER=true
PROJECTIVE_CLASS_FREEZING_COST=Bo1
```

## 3. Consequence for the t128--t131 real/nonreal split

Merged t128--t131 used Fourier expansion to distinguish

```text
endpoint headroom,
long real/order-two character,
long nonreal character.
```

That distinction remains useful when applying prime-distribution theorems, especially because completed tH29 retains the possible real exceptional-zero boundary. But it is no longer the minimal **cofactor-side** receiver.

After the nonnegative localization above, the exact surviving object is

```text
sum_n W_{c_*}(n)
  K_n(q_*),

q_*:=c_*^(-1)*[a]^(-1),
```

against the principal baseline

```text
1/g * sum_n W_{c_*}(n)|P_n|.
```

The cofactor class and the target prime class are now both fixed. The only polynomial cofactor coordinate is the scalar norm `n`; the only cofactor weight is the nonnegative fixed-class norm weight `W_{c_*}(n)<=B^o(1)`.

The endpoint/long-headroom split remains available as a split of the scalar `n` range. The real/nonreal character split is now a theorem-analysis tool for the **fixed prime progression**, not an independent cofactor receiver.

This materially changes the minimal fixed-`U` receiver to

```text
FixedProjectiveCofactorClassScalarNormWeightAgainstReciprocalFixedProjectivePrimeClassDepletion.
```

Completed tH29 remains the applicable negative theorem boundary: it does not supply a uniform theorem for this weighted reciprocal family, especially with unrestricted endpoint headroom, `d=B^o(1)`, and possible real exceptional-character bias. No new tH is justified before the scalar fixed-class weight `W_{c_*}(n)` is opened internally.

Merged Work-bsX31's common one-dimensional reciprocal-selector language is retained only structurally. No global/s physical-weight adapter or saving is cross-promoted.

```text
MOVING_SELECTED_CLASS_AS_MINIMAL_RECEIVER_SUPERSEDED=true
REAL_NONREAL_COFACTOR_BRANCH_SPLIT_AS_MINIMAL_RECEIVER_SUPERSEDED=true
FIXED_PROJECTIVE_CLASS_RECIPROCAL_PRIME_DEPLETION_RECEIVER_PROVED=true
FIXED_CLASS_SCALAR_NORM_WEIGHT_SUPNORM=Bo1
ENDPOINT_LONG_HEADROOM_SPLIT_RETAINED=true
TH29_NEGATIVE_BOUNDARY_RETAINED=true
RECEIVER_MATERIALLY_CHANGED=true
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH30_NEEDED=false
PREFERRED_RECEIVER=SharedUFixedProjectiveCofactorClassScalarNormWeightAgainstReciprocalFixedProjectivePrimeClassDepletion
NEXT_INTERNAL_TARGET=FixedProjectiveClassScalarNormWeightArithmeticOpening
NEXT=Stage14-t133
