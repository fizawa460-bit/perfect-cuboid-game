# Next-receiver selector at the 7/8 checkpoint

```yaml
ID: TB-RECIPE-next-receiver-selector-7-8
TYPE: RECIPE
STATUS: CURRENT
TITLE: Select a legal next receiver from the current 7/8 critical shell without reopening closed routes
SCOPE: BOTH
SOURCE_STAGE: Stage14-s7-14
SOURCE_PR: 437
SOURCE_MERGE_SHA: 31c3636016f5f0ff80133f0c1b6a9cbbd91a3697
SOURCE_FILES:
  - stages/stage14/14-s7-14/result.md
  - stages/stage14/14-4cb/result.md
  - stages/stage14/14-t50/result.md
```

## INPUT

A proposed new Stage14 main/s theorem or support receiver at the current `7/8` checkpoint.

## OUTPUT

Classify it as

```text
DIRECT_GO
BRIDGE_GO
SUPPORT_GO
PARK
REJECT
```

with current priority

```text
1. off-diagonal (xi,k) collision power saving
2. realized xi sparsity with fixed delta>0
3. genuinely transverse coefficient gain eta>0
4. selector-sensitive two-modulus second moment as support/bridge
```

The full gates are frozen in `docs/stage14-toolbox/next-receiver-selector.md`.

## VARIABLE DICTIONARY

- `DIRECT_GO`: merged sufficient contract would directly improve main/s whole-family exponent.
- `BRIDGE_GO`: useful theorem but exact operator/quantifier bridge still required.
- `SUPPORT_GO`: merged source explicitly requests support work.
- `PARK`: valid but exponent-inactive information.
- `REJECT`: repeats a closed-negative route or violates a safety lock.

## USED BY

- Choosing Stage14-4cc / s7-15 style work.
- Deciding whether t/tH results may enter the main/s receiver.
- Avoiding repeated work on already-closed barriers.

## DO NOT USE FOR

- Do not treat the priority order as a proof of which route is easiest.
- Do not promote a `BRIDGE_GO` theorem to a main/s exponent before the bridge is merged.

## PROVENANCE NOTES

The selector reorganizes only merged 4cb, s7-14, and t50 theorem contracts.