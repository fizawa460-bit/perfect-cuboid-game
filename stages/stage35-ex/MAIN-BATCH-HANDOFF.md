# Stage35-EX MAIN batch handoff — Goal4CG current-main integration

Formal authority remains **V74 / Goal4AK** under hostile review `5142248509`. Current `main` already contains the hostile-audited Goal4CF selected-direction discriminant-height adapter through merged PR #1773 at main commit `9a05bdbe2dbb1ba50ef68425c80f5c289260f5da`.

No E1, Stage35, endpoint, or Perfect Cuboid credit is granted by Goal4CG.

## Retained Goal4CF boundary

The audited Goal4CF current-main integration preserves:

```text
Delta_min=(r*s*t)^4/256
12288*abs(Delta_min(E_*)) >= W^10
```

for the deterministic selected cyclic direction and the actual primitive endpoint space diagonal `W`.

Historical Goal4CF hostile-audit provenance remains retained for successor verification:

- mathematical hostile PASS: review `5164213568`, exact head `2ffe07f31d56caf78261d032b7e5a78d500dd146`
- lifecycle-repaired hostile PASS: review `5174608648`, exact head `a059c12ecd298258fa59feac653eb750d7143767`
- no-drift revalidation: review `5174722371`, same exact head `a059c12ecd298258fa59feac653eb750d7143767`
- retained credit ceiling: `AUDITED_SELECTED_DIRECTION_QUANTITATIVE_DISCRIMINANT_HEIGHT_ADAPTER_NO_E1_CREDIT`

The retained research-route provenance is:

```text
stages/stage35-ex/35ex-35/goal4cf-research-route-ledger.md
```

It records the historical AT/AU/BD/AW/AZ/BS/BT-CE route boundaries so they are not silently rediscovered.

## Goal4CG source checkpoint

Historical PR #1771 executed the exact next obligation left by Goal4CF:

```text
SELECTED_PHYSICAL_MARKED_LOCAL_HEIGHT_COMPARISON_PREFLIGHT
```

The historical clean audit checkpoint was:

```text
source exact head = 67fa8115211119cb667caacabde7d52133507f6f
dedicated CI run = 34555204989
dedicated CI job = 103126305682
Goal4BS checkpoint run = 34555205029
```

That old PR was based on `stage35-ex-goal4cf-audit-base` and was not a legal direct merge path to current main. PR #1771 is now being rewritten as a current-main integration PR rather than merged with its old stacked ancestry.

The three Goal4CG checkpoint artifacts are preserved byte-identically:

```text
source-lock blob = c47e5c9a9faac08949f451e306c700102831dcb8
source-lock LF sha256 = 8528b2b818dd505c277372dd44a313e60399e7361503d753376d2899a7010e44
certificate blob = 473fe8a39596cb5741fc8709b22cd22590a0f67c
certificate canonical sha256 = d7eb73b45871c66e2c0ded5c566ae2c6f5e914483419d31823ab2f99e6ad13de
historical verifier blob = 1c753fc01a99efdd88e991fef15347c899d3dc37
```

The historical verifier intentionally retains its old source-lock universe. Current main does not import the full Goal4AL+ file forest merely to satisfy those historical locks. Instead:

```text
stages/stage35-ex/35ex-35/goal4cg-current-main-integration.json
stages/stage35-ex/verify_stage35_ex_35_goal4cg_current_main_integration.py
```

form the successor-safe current-main consumption boundary.

## Goal4CG mathematical checkpoint

For the selected reduced legs `(m,n)`, opposite edge `K`, selected-face diagonals `d_m,d_n`, and

```text
r=n^2-m^2
s=2mn
t=m^2+n^2
```

the physical marked point on the Goal4CF minimal model has exact x-coordinate

```text
u = -(m*n*r/2) * (n*d_m+m*d_n)/(m*d_m-n*d_n).
```

The denominator identity is

```text
(m*d_m-n*d_n)(m*d_m+n*d_n) = -r*W^2.
```

The explicit height bounds are

```text
h_x(P_*) <= 6 log W
hhat(P_*) <= 17/3 log W.
```

The selected curve has the semistable conductor packet

```text
N(E_*) = rad_odd(R)       if v2(s)=2
N(E_*) = 2*rad_odd(R)     if v2(s)>=3
R=abs(r*s*t)
N(E_*) <= R/4
sigma(E_*) >= 4.
```

Using the Goal4CF discriminant coefficient `10`, Petsche's explicit lower bound has best possible coefficient under the retained information

```text
10/(10^15*4^6*log^2(104613*16)) < 1.19e-20,
```

which is far below the explicit upper coefficient `17/3`.

Therefore:

```text
STRICT_PETSCHE_COEFFICIENT_WIN=false
UNIFORM_SZPIRO_UPPER_BOUND=false
FINITE_HEIGHT_REDUCTION=false
```

This is a fail-close of this explicit Petsche/Goal4CF comparison, not a theorem that all future height arguments fail.

## Smaller live blocker exposed by Goal4CG

The remaining local-height obligation is:

```text
UNIFORM_MARKED_BAD_PRIME_COMPONENT_INDEX_CONTROL
```

At bad primes the marked point can reduce to the nodal singular point, while denominator cancellation can change the component analysis. Current retained source identities do not give a uniform favorable component-index theorem.

After a hostile-audit PASS of the current-main #1771 integration, the research order is:

```text
1. test UNIFORM_MARKED_BAD_PRIME_COMPONENT_INDEX_CONTROL;
2. if it does not yield a strict lower comparison, execute the required breadth reopen;
3. do not reopen a route already classified in goal4cf-research-route-ledger.md without a genuinely new adapter.
```

## Credit firewall

Still false / not granted:

```text
UNIFORM_SZPIRO_UPPER_BOUND=false
STRICT_CANONICAL_HEIGHT_COEFFICIENT_WIN=false
UNIFORM_MARKED_BAD_PRIME_COMPONENT_INDEX_CONTROL=false
FINITE_HEIGHT_REDUCTION=false
E1_proved=false
R29_PESCH_E1_closed=false
stage35_closed=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
```

PR #1771 must remain unmerged until its rewritten current-main exact head has green aggregate/lifecycle CI and a hostile freshness PASS anchored to that exact head.
