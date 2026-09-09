# Stage35-EX MAIN batch handoff — Goal4BM complete primary lambda^7 ray dual boundary

Audited authority remains **V74 / Goal4AK** (hostile review `5142248509`). Goal4AL–Goal4BM are provisional stacked leaves on PR #1723. No E1, Stage35, endpoint, or Perfect Cuboid credit is promoted.

## Exact-green parent

Goal4BL is exact-green:

- exact head: `08911659889e93ce242bee3491b6555a5a16b6ab`
- aggregate: `34315466300`
- `verify-stage35-ex-current`: `102351543882`
- result: `SUCCESS`

Goal4BL proved that the canonical fixed-unit character

```text
chi_i(alpha)=(i/alpha)_4
```

descends, on odd primary Gaussian integers, to the rational norm modulo `16`:

```text
chi_i(alpha)=i^((N(alpha)-1)/4).
```

Hence it is orientation-sensitive only at reservoir primes `5,13 mod 16`, and blind at `1,9 mod 16`.

## Goal4BM provisional exact result

For odd primary `alpha=A+B*i`, introduce the ramified supplementary character

```text
chi_lambda(alpha)=((1+i)/alpha)_4
                 =i^((A-B-B^2-1)/4).
```

It is not determined modulo `lambda^6`, but is determined modulo

```text
lambda^7=(1+i)^7=8-8*i.
```

The pair

```text
(chi_i(alpha), chi_lambda(alpha))
```

gives a bijection from the 16 primary ray classes modulo `lambda^7` to `mu_4^2`. Thus the first complete ramified ray dual has been materialized rather than sampled by one character.

This still does not give a universal orientation obstruction. The locally admissible primary class represented by

```text
5+4*i
```

has ray coordinates

```text
(e_i,e_lambda)=(2,0)
```

and order `2`. Therefore every character of conductor dividing `lambda^7` takes the same value on exponent `+1` and exponent `-1` at that class. The direction-a reservoir congruence is locally compatible at `ell=41` with both source roots `±9`.

So:

```text
complete primary lambda^7 ray dual = yes;
ramified character adds non-norm information = yes;
source-fixed ramified value = no;
order-two blind class locally compatible = yes;
all conductor-lambda7 characters detect sigma = no;
global reciprocity contradiction = no;
branch pruning = no.
```

Artifacts:

- `stages/stage35-ex/35ex-35/goal4bm-ramified-one-plus-i-quartic-dual-source-lock.md`
- `stages/stage35-ex/35ex-35/goal4bm-ramified-one-plus-i-quartic-dual.json`
- `stages/stage35-ex/verify_stage35_ex_35_goal4bm_ramified_one_plus_i_quartic_dual.py`

## Next exact leaf

```text
35EX-35_GOAL4BN_COMMON_W_PRIMARY_SPACE_ROOT_RAY_PRODUCT_PREFLIGHT
```

Use the fact that `Psi_a,Psi_b,Psi_c` arise from the same space diagonal `W`. Test whether their source units and common-`W` relations force `Xi` into a proper subset of the 16 primary `lambda^7` ray classes, especially whether they exclude the locally admissible order-two class. Do not open a deeper ray-character tower before testing this cross-direction source constraint.

No merge. No hostile-audit credit. `MAIN-STATE.json` remains V74 / Goal4AK.
