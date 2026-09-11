# Stage35-EX MAIN batch handoff — audited Goal4CF current-main integration

Formal authority remains **V74 / Goal4AK** under hostile review `5142248509`. Goal4CF is an independently hostile-audited intermediate quantitative adapter; it does not replace `MAIN-STATE.json` authority and grants no E1, Stage35, endpoint, or Perfect Cuboid credit.

## Goal4CF hostile-audit provenance

PR #1766 contains the long-lived research stack and must not be merged directly.

- mathematical hostile PASS: review `5164213568`, exact head `2ffe07f31d56caf78261d032b7e5a78d500dd146`
- lifecycle-repaired hostile PASS: review `5174608648`, exact head `a059c12ecd298258fa59feac653eb750d7143767`
- no-drift revalidation PASS: review `5174722371`, same exact head `a059c12ecd298258fa59feac653eb750d7143767`
- exact-head aggregate run: `34556563263` SUCCESS
- exact-head dedicated Goal4CF run: `34556563288` SUCCESS

The source mathematical credit ceiling is:

```text
AUDITED_SELECTED_DIRECTION_QUANTITATIVE_DISCRIMINANT_HEIGHT_ADAPTER_NO_E1_CREDIT
```

## Current-main integration strategy

Current-main parent before this integration is:

```text
9ce9abcde2880d6de10dd7f408feb18fb9fab630
```

The three load-bearing Goal4CF artifacts are copied byte-identically from audited head `a059c12ecd298258fa59feac653eb750d7143767`:

- source-lock blob `a94e98e560793cf91548a67bd37989915de00e7a`
- certificate blob `60fae382dd97ab6a905b1678681f829b59595e56`
- historical verifier blob `e0f623087b8814f9d7ab7f8ced6d7d71f5de0033`

The original certificate intentionally retains its historical source-lock environment and pre-audit status text. It is not rewritten to pretend that current root `AGENTS.md` or the cleaned repository lifecycle surface has the same blobs as the old research branch. Instead, `goal4cf-hostile-audit-pass-consumption.json` records the independent audit receipt, and `verify_stage35_ex_35_goal4cf_audited_integration.py` verifies byte identity of the audited artifacts plus the current V74 / Goal4AK authority firewall.

This is the same successor-safe pattern used for the V74 persisted-history replay: preserve the audited historical object, consume it through an explicit current-generation adapter, and do not weaken the old verifier to fit a newer repository state.

No Goal4AL+ provisional research, Goal4BS/BD/AW/AT/AU/AZ/CE historical file forest, or retired/manual Stage35EX workflow fan-out is imported by this integration.

## Audited Goal4CF mathematical result

For each primitive positive endpoint, select the cyclic direction by the maximal reduced pair height, with ties `AB, AC, BC`. For the selected reduced coprime opposite-parity legs `b,c`, set

```text
r=c^2-b^2
s=2bc
t=b^2+c^2.
```

The selected elliptic curve has the global minimal model

```text
v^2+u*v=u^3+((r^2-s^2-1)/4)*u^2-(r^2*s^2/16)*u
```

and exact minimal discriminant

```text
Delta_min=(r*s*t)^4/256.
```

The hostile-audited selected-direction endpoint estimate is

```text
12288*abs(Delta_min(E_*)) >= W^10.
```

Equivalently,

```text
log abs(Delta_min(E_*)) >= 10 log W - log(12288).
```

This is not fixed-direction AW-C2, not an arbitrary-cutoff lower bound, and not a uniform Szpiro or canonical-height coefficient result.

## Credit firewall

Still false / not granted:

```text
FIXED_DIRECTION_AW_C2_DISCHARGED=false
EXPLICIT_MARKED_CANONICAL_HEIGHT_UPPER_CONSTANT=false
UNIFORM_SZPIRO_BOUND=false
STRICT_CANONICAL_HEIGHT_COEFFICIENT_WIN=false
FINITE_HEIGHT_REDUCTION=false
E1_proved=false
R29_PESCH_E1_closed=false
stage35_closed=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
```

The current-main integration itself still requires hostile freshness audit before merge. The source Goal4CF mathematics is already audited; that audit is not being repeated or upgraded here.

## Next bounded obligation after current-main integration PASS

```text
SELECTED_PHYSICAL_MARKED_LOCAL_HEIGHT_COMPARISON_PREFLIGHT
```

Keep the same deterministic selector and actual endpoint `W`. Derive an explicit numerical upper comparison for the selected physical marked point and test whether local contributions can produce a lower comparison without assuming a uniform Szpiro upper bound. A failure to obtain a strict coefficient win must be recorded as a blocker rather than promoted to E1 credit.
