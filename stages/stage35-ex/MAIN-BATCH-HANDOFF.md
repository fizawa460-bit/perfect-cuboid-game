# Stage35-EX MAIN batch handoff — Goal4BG Gaussian face/space phase compatibility

Audited authority remains **V74 / Goal4AK** (hostile review `5142248509`). Goal4AL–Goal4BG are provisional stacked leaves on PR #1723. No E1, Stage35, endpoint, or Perfect Cuboid credit is promoted.

## Exact-green parent

Goal4BF is exact-green:

- exact head: `ab134d4cd9d21efb9f90f89e3215e81caa3561e2`
- aggregate: `34306382710`
- `verify-stage35-ex-current`: `102324844711`
- result: `SUCCESS`

Goal4BF source-locks an oriented Gaussian prime above every reservoir prime and lifts Goal4BE to quartic residue phases, but leaves the cross-conjugate gauge `G_ab,G_ac,G_bc` unresolved.

## Goal4BG provisional exact result

The three primitive reduced face factors

```text
Phi_AB=y*a+i*z*b,
Phi_AC=x*a+i*z*c,
Phi_BC=x*b+i*y*c
```

have coprime conjugate factors and square norms. Hence, with unique primary square roots,

```text
Phi_AB=eps_AB*Theta_AB^2,
Phi_AC=eps_AC*Theta_AC^2,
Phi_BC=eps_BC*Theta_BC^2.
```

The Goal4BF oriented reservoir kernels are literal divisors of these source roots:

```text
Sigma_a | bar(Theta_BC),
Sigma_b | bar(Theta_AC),
Sigma_c | bar(Theta_AB).
```

The reservoirs also have a second exact meaning:

```text
gcd(A,D_BC)=h_a,
gcd(B,D_AC)=h_b,
gcd(C,D_AB)=h_c.
```

Thus each `h_i|W` and division produces three primitive space Pythagorean triples and therefore three more canonical Gaussian square roots

```text
D_BC/h_a+i*A/h_a = nu_a*Psi_a^2,
D_AC/h_b+i*B/h_b = nu_b*Psi_b^2,
D_AB/h_c+i*C/h_c = nu_c*Psi_c^2.
```

At a reservoir prime `ell|s_a`, BF sees

```text
iota_a=x*b/(y*c) mod ell,
iota_a^2=-1.
```

After stripping the common gcd `h_a`, the space factor instead sees the leading quotients

```text
a'=a/ell^m,
r'=r_BC/ell^m,
m=v_ell(h_a).
```

If their valuations are unequal, there is no secondary space-side root of `-1` at `ell`. If both are units and `ell|W/h_a`, then

```text
lambda_a=z*r'/(x*y*a'),
lambda_a^2=-1,
lambda_a=sigma_a*iota_a,
sigma_a in {+1,-1}.
```

Cyclic analogues hold. Therefore common `W` does not yet fix the BF cross-conjugate gauge; it exposes new valuation-stripped signs `sigma_i(ell)` that are not determined by the retained AU/BE/BF source identities.

Exact route status:

```text
six source-oriented Gaussian square roots = yes;
reservoir/space-gcd coupling = yes;
secondary leading-unit phase bits = yes;
BF gauge closed = no;
branch pruning = no.
```

Artifacts:

- `stages/stage35-ex/35ex-35/goal4bg-gaussian-square-root-face-phase-compatibility-source-lock.md`
- `stages/stage35-ex/35ex-35/goal4bg-gaussian-square-root-face-phase-compatibility.json`
- `stages/stage35-ex/verify_stage35_ex_35_goal4bg_gaussian_face_space_phase.py`

## Next exact leaf

```text
35EX-35_GOAL4BH_RESERVOIR_LEADING_UNIT_SPACE_FACE_SIGN_CYCLE_PREFLIGHT
```

Use full `ell`-adic leading terms to classify the `sigma_i(ell)` and test whether they satisfy a cyclic product relation strong enough to close the BE/BF phase freedom.

No merge. No hostile-audit credit. `MAIN-STATE.json` remains V74 / Goal4AK.
