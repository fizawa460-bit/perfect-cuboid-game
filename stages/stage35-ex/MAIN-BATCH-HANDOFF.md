# Stage35-EX MAIN batch handoff — Goal4BH reservoir leading-unit orientation torsor

Audited authority remains **V74 / Goal4AK** (hostile review `5142248509`). Goal4AL–Goal4BH are provisional stacked leaves on PR #1723. No E1, Stage35, endpoint, or Perfect Cuboid credit is promoted.

## Exact-green parent

Goal4BG is exact-green:

- exact head: `0ad450e20e4ce74a3b69d1f91720bc50ef955de3`
- aggregate: `34309951404`
- `verify-stage35-ex-current`: `102335489958`
- result: `SUCCESS`

Goal4BG produced six source-oriented Gaussian square roots, identified `h_a=gcd(A,D_BC)` cyclically, and exposed secondary leading-unit signs `sigma_i(ell)` without closing the BF phase gauge.

## Goal4BH provisional exact result

For `ell|s_a`, let

```text
u=x*b,
v=y*c,
r=r_BC,
I_a^2=-1,
I_a == iota_a mod ell,
rho=v_ell(r).
```

The BF-selected Hensel factor has exact valuation

```text
v_ell(u-I_a*v)=2*rho.
```

Hence

```text
q_a=(u-I_a*v)/ell^(2*rho) in Z_ell^*,
(r/ell^rho)^2=q_a*(u+I_a*v).
```

Write

```text
alpha=v_ell(a),
m=min(alpha,rho)=v_ell(h_a).
```

If `alpha!=rho`, the reduced space triple has one unit leg and one `ell`-divisible leg, so

```text
ell does not divide W/h_a.
```

Thus a secondary space orientation requires the exact valuation tie

```text
alpha=rho=m.
```

When additionally `ell|W/h_a`, define

```text
lambda_a=z*(r_BC/ell^m)/(x*y*(a/ell^m)),
lambda_a^2=-1,
sigma_a=lambda_a/iota_a in {+1,-1}.
```

Explicitly

```text
sigma_a
 = z*c*(r_BC/ell^m)/(x^2*b*(a/ell^m)) mod ell.
```

For the reduced space Gaussian factor

```text
Omega_a=z*(r_BC/ell^m)+i*x*y*(a/ell^m),
```

one gets the exact orientation interpretation

```text
sigma_a=-1  <=> BF-selected p_a divides Omega_a,
sigma_a=+1  <=> conjugate p_a divides Omega_a.
```

The selected Gaussian valuation is `2*v_ell(W/h_a)`. Cyclic analogues hold for `b,c`.

Therefore the surviving BF/BG phase problem is reduced exactly to primewise `mu_2` face/space orientation bits. Full leading terms determine their squares and valuations but no source-locked cyclic product relation has yet been obtained.

Exact route status:

```text
Hensel leading unit = exact;
secondary orientation requires valuation tie = exact;
sigma_i explicit = exact;
sigma_i is Gaussian prime matching bit = exact;
universal sigma cycle = not obtained;
branch pruning = no.
```

Artifacts:

- `stages/stage35-ex/35ex-35/goal4bh-reservoir-leading-unit-space-face-sign-cycle-source-lock.md`
- `stages/stage35-ex/35ex-35/goal4bh-reservoir-leading-unit-space-face-sign-cycle.json`
- `stages/stage35-ex/verify_stage35_ex_35_goal4bh_face_space_orientation_torsor.py`

## Next exact leaf

```text
35EX-35_GOAL4BI_SECONDARY_ORIENTATION_HILBERT_PRODUCT_FORMULA_PREFLIGHT
```

Package the `sigma_i(ell)` as local `mu_2` orientation characters and test Hilbert reciprocity/global product formula, including real and 2-adic contributions, for a genuinely new global relation.

No merge. No hostile-audit credit. `MAIN-STATE.json` remains V74 / Goal4AK.
