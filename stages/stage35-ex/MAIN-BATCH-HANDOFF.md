# Stage35-EX MAIN batch handoff — Goal4BJ support-cleaned global Gaussian quartic orientation carrier

Audited authority remains **V74 / Goal4AK** (hostile review `5142248509`). Goal4AL–Goal4BJ are provisional stacked leaves on PR #1723. No E1, Stage35, endpoint, or Perfect Cuboid credit is promoted.

## Exact-green parent

Goal4BI is exact-green:

- exact head: `933e32403c2f87b65ac3e962647c59e71a35a291`
- aggregate: `34312324963`
- `verify-stage35-ex-current`: `102342539462`
- result: `SUCCESS`

Goal4BI fail-closed ordinary rational Hilbert reciprocity: reservoir primes split in `Q(i)`, so rational squareclasses/norms cannot see the `p_i` versus `bar(p_i)` orientation.

## Goal4BJ provisional exact result

Use the BF squarefree primary reservoir kernels and BG primary space square roots. In direction `a`, define unique primary Gaussian gcds

```text
M_a^- = gcd(Sigma_a,Psi_a),
M_a^+ = gcd(Sigma_a,bar(Psi_a)),
M_a^0 = Sigma_a/(M_a^-*M_a^+).
```

Because the reduced space triple is primitive, `Psi_a` and `bar(Psi_a)` are coprime. Hence

```text
Sigma_a=M_a^-*M_a^+*M_a^0
```

is an exact pairwise-coprime partition. Since every factor is a literal divisor of `Sigma_a`, no non-reservoir Gaussian prime enters the package.

For a BF-selected prime `p_{a,ell}`:

```text
p|M_a^-  <=> secondary and sigma_a=-1,
p|M_a^+  <=> secondary and sigma_a=+1,
p|M_a^0  <=> no secondary orientation.
```

Define cyclically

```text
Xi_a=M_a^-/M_a^+,
Xi_b=M_b^-/M_b^+,
Xi_c=M_c^-/M_c^+,
Xi=Xi_a*Xi_b*Xi_c.
```

The supports are disjoint across `a,b,c`. At each selected reservoir prime,

```text
v_p(Xi)=+1  for sigma=-1,
v_p(Xi)=-1  for sigma=+1,
v_p(Xi)=0   for nonsecondary.
```

Thus all non-reservoir finite support is cleaned exactly, and the single class

```text
[Xi]_4 in Q(i)^*/Q(i)^{*4}
```

recovers the orientation because the local exponents are `1,3,0 mod 4`. The quadratic class cannot: `+1` and `-1` are identical modulo `2`. Hence even Gaussian quadratic `K_2`/Hilbert data is too coarse; the surviving datum is genuinely quartic.

Also

```text
J=Xi/bar(Xi),
N(J)=1,
```

is a global norm-one anti-invariant carrier. This gives no obstruction by itself because `J=Xi/bar(Xi)` is already an explicit Hilbert-90 presentation.

Exact route status:

```text
support-cleaning adapter = obtained;
global Gaussian orientation carrier = obtained;
quartic class recovers sigma = yes;
quadratic K2/Hilbert recovers sigma = no;
norm-one carrier itself obstructive = no;
dual order-four character = not constructed;
global quartic reciprocity contradiction = no;
branch pruning = no.
```

Artifacts:

- `stages/stage35-ex/35ex-35/goal4bj-global-gaussian-k2-quartic-character-adapter-source-lock.md`
- `stages/stage35-ex/35ex-35/goal4bj-global-gaussian-k2-quartic-character-adapter.json`
- `stages/stage35-ex/verify_stage35_ex_35_goal4bj_global_gaussian_orientation_carrier.py`

## Next exact leaf

```text
35EX-35_GOAL4BK_DUAL_QUARTIC_CHARACTER_COFACTOR_UNIT_PREFLIGHT
```

Use complementary Gaussian face/space cofactors and the BH leading units to seek one source-derived order-four dual character of `[Xi]_4`. A viable candidate must have controlled local value at every selected reservoir prime and controlled support elsewhere; otherwise fail-close the Gaussian reciprocity branch.

No merge. No hostile-audit credit. `MAIN-STATE.json` remains V74 / Goal4AK.
