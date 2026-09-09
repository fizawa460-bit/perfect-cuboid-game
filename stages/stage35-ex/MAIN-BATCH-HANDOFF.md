# Stage35-EX MAIN batch handoff — Goal4BL fixed-i norm-mod16 ray-class collapse

Audited authority remains **V74 / Goal4AK** (hostile review `5142248509`). Goal4AL–Goal4BL are provisional stacked leaves on PR #1723. No E1, Stage35, endpoint, or Perfect Cuboid credit is promoted.

## Exact-green parent

Goal4BK is exact-green:

- exact head: `9c72ebb551f2d8580a929b07c5dfcf2caa0f236e`
- aggregate: `34313690442`
- `verify-stage35-ex-current`: `102346571027`
- result: `SUCCESS`

Goal4BK produced the canonical fixed-unit quartic dual

```text
chi_i(alpha)=(i/alpha)_4
```

and left its deeper two-adic/ray-class value on the BJ carrier `Xi` unresolved.

## Goal4BL provisional exact result

For odd primary

```text
alpha=A+B*i,
A odd,
B even,
A+B=1 mod 4,
```

one has

```text
chi_i(alpha)=i^((1-A)/2).
```

A complete primary residue computation gives

```text
N(alpha) == 3-2*A mod 16,
```

hence the stronger exact formula

```text
chi_i(alpha)=i^((N(alpha)-1)/4).
```

Thus the apparent two-adic compensator for the **fixed-i** character is not an independent Gaussian phase: on primary elements this character descends to the rational norm modulo `16`.

For

```text
Xi=(M_a^-*M_b^-*M_c^-)/(M_a^+*M_b^+*M_c^+),
R_-=N(M_a^-*M_b^-*M_c^-),
R_+=N(M_a^+*M_b^+*M_c^+),
```

one gets exactly

```text
chi_i(Xi)=i^((R_- - R_+)/4).
```

If

```text
S_sec=R_-*R_+=product_i gcd(s_i,W/h_i),
```

then

```text
chi_i(Xi)^2=(2/S_sec).
```

Primewise sensitivity is now exact:

```text
ell mod16 = 1  -> chi_i(pi)=1   -> sigma blind,
ell mod16 = 5  -> chi_i(pi)=i   -> sigma sensitive,
ell mod16 = 9  -> chi_i(pi)=-1  -> sigma blind,
ell mod16 =13  -> chi_i(pi)=-i  -> sigma sensitive.
```

All four `1 mod4` residue classes are compatible with the retained reservoir congruence; exact local diagnostics use

```text
(ell,iota)=(5,2),(13,5),(17,4),(41,9).
```

These odd-prime models are CRT-compatible with each primitive two-adic parity branch. They are local diagnostics only, not global endpoint constructions.

Therefore fixed `i` does **not** give a universal orientation obstruction. Its global product is exactly the norm-mod16 evaluation of the already-defined BJ orientation partition, not a second independent reciprocity equation.

Exact route status:

```text
lambda^6 ray depth sufficient = yes;
lambda^5 + norm mod8 sufficient = no;
fixed-i character descends to norm mod16 = yes;
chi_i(Xi) exact = yes;
all sigma bits detected = no;
new reciprocity equation = no;
branch pruning = no.
```

Artifacts:

- `stages/stage35-ex/35ex-35/goal4bl-xi-two-adic-ray-class-parity-source-lock.md`
- `stages/stage35-ex/35ex-35/goal4bl-xi-two-adic-ray-class-parity.json`
- `stages/stage35-ex/verify_stage35_ex_35_goal4bl_xi_two_adic_ray_class.py`

## Next exact leaf

```text
35EX-35_GOAL4BM_RAMIFIED_ONE_PLUS_I_QUARTIC_DUAL_PREFLIGHT
```

Test the ramified supplementary quartic character with numerator `1+i` (or the equivalent ray-class functional) against the BJ carrier. Unlike fixed `i`, it can depend on the imaginary/ray residue rather than rational norm alone. Determine whether the source controls that value or whether it introduces another free phase.

No merge. No hostile-audit credit. `MAIN-STATE.json` remains V74 / Goal4AK.
