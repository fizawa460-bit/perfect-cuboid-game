# Stage29-02g — ordinary 8-congruence firewall and the level-4 cover

```text
ROLE=ORDINARY_8_CONGRUENCE_FIREWALL_PLUS_LEVEL4_COVER
STATUS=DERIVED_PENDING_FRESH_AUDIT
```

## 1. Ordinary 8-congruence is abundant

Fisher's `Z(8,1)` parametrizes pairs of symplectically 8-congruent elliptic curves after forgetting the extra endpoint level-4 basis data. The surface is rational over Q, and Fisher's Corollary 1.3 gives infinitely many non-isogenous rational pairs.

Therefore

```text
NAIVE_8_CONGRUENCE_RARITY_OBSTRUCTION=RED
```

No argument may use the bare existence of an 8-torsion isomorphism as evidence that endpoint points should be finite or absent.

## 2. Why the cuboid surface is much harder

Over `K=Q(i)`, Testa--Stoll give

```text
Sbar_K ~= (X(8) x X(8))/Delta G0,
G0=ker(PSL2(Z/8)->PSL2(Z/4)),
|G0|=8.
```

For ordinary symplectic 8-congruence, the simultaneous change of full level-8 basis is by the full diagonal group

```text
Delta PSL2(Z/8),
|PSL2(Z/8)|=192.
```

Thus there is a natural forgetful quotient, generically away from stabilizers/cusps,

```text
Sbar_K  -->  Z(8,1)_K
```

with generic degree

```text
[PSL2(Z/8):G0]=192/8=24.
```

The residual quotient group is

```text
PSL2(Z/4) ~= S4.
```

So the endpoint surface is not the ordinary rational 8-congruence surface. It is the level-4-retaining `S4` cover sitting above it, with ramification/stabilizer data carrying the extra complexity.

This gives the structural receiver

```text
R29-MOD2=EndpointAsLevel4S4CoverOfOrdinarySymplectic8CongruenceSurface
```

## 3. Interpretation

The contrast

```text
ordinary Z(8,1): rational surface / abundant rational pairs
endpoint Sbar: general type / exact level4 + Q-conjugation constraint
```

shows where any useful modular obstruction must live:

```text
NOT in ordinary 8-congruence,
BUT in the 24-sheet level4 lift, its Q(i)/Q descent, branch/stabilizer conditions,
and the physical-open restriction.
```

## Firewalls

- `24` is a generic geometric degree; special stabilizer/cusp fibers require a separate ledger.
- Rationality of the base does not imply rationality or density on the level-4 cover.
- This quotient structure does not decide whether `Sbar(Q)` contains a physical point.

```text
R29_MOD2=PASS_CANDIDATE
GENERIC_DEGREE=24
S4_COVER_BRANCH_LEDGER_COMPLETE=false
ENDPOINT_POINT_SET_COMPUTED=false
```
