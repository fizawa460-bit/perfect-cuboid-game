# Project-wide research arsenal index

```text
REGISTRY=RESEARCH-ARSENAL-R01
STATUS=CURRENT
SCOPE=merged reusable weapons through Stage25 reentry
```

This is the project-wide router. It does not replace canonical proof sources.
`ACTIVE` means preferred for a matching receiver; `PARKED` means valid but
specialized or currently without a receiver; `SUPERSEDED` means retained only
for provenance and must not be selected as the current strongest statement.

## Active weapons

| ID | Type | Reusable output | Canonical package |
|---|---|---|---|
| AR-006 | BOUND | `N_2(B) << B^(1/2+o(1))` | `stage14-arsenal.md` |
| S20-W01 | BOUND | Euler upper `M_3(B) <<_eta B(log B)^(5-eta)` | `stage20-arsenal.md` |
| S20-W02 | CONSTRUCTION | primitive Saunderson `M_3(B) >> B^(1/6)` | `stage20-arsenal.md` |
| S20-W03 | OBSTRUCTION | Euler local blocker law and sieve dimension two | `stage20-arsenal.md` |
| S21-W01 | METHOD | ambient-control interaction classification | `stage21-arsenal.md` |
| S21-W02 | THEOREM | `N_1/M_1 ~ (kappa*pi/18)(log B)^2/B` | `stage21-arsenal.md` |
| S22-W01 | THEOREM | `M_2/M_1 ~ (4*pi^2*C_M2/3)(log B)^4/B` | `stage22-arsenal-promotion.md` |
| S23-W01 | THEOREM | `N_2/N_1 -> 0` on the already-space-integral host | `stage23-arsenal-promotion.md` |
| S23-W02 | FORMULA | `N_2,j=A_pair(j)-A_3`; pair contrasts cancel `A_3` | `stage23-arsenal-promotion.md` |
| S25-W01 | CONSTRUCTION | global and all-direction `N_2,j(B) >>_j B^(1/4)` | `stage25-arsenal-promotion.md` |
| S25-W02 | INVARIANT | exact face/space cross-ratio and positive-divergent sign | `stage25-arsenal-promotion.md` |
| S25-W05 | ADAPTER | exact raw-pair completion proportions and corridor | `stage25-arsenal-promotion.md` |
| S25-W06 | LEDGER | Manin `(a,b)` transitions `(2,2)->(1,4)->(1,6)` | `stage25-arsenal-promotion.md` |

## Parked weapons

| ID | Reason |
|---|---|
| S24-W-C17 | Valid parity-stratum construction, but its `sqrt(log B)` lower is superseded by S25-W01. |
| S24-W-THIN-COVER | Independent qualitative zero-density proof; do not multiply it with AR-006 or the fixed-prime sieve. |
| S25-W04 | Exact only for the audited R504 elliptic base-change/Prym setup; no general current receiver. |

S25-W03 is not a separate selector: it is the primitive-height support
certificate for S25-W01. Stage17 and Stage18 final theorems remain frozen stage
interfaces rather than duplicate weapon cards. Stage19's original half-power
upper and fixed-prime squareclass mechanism are already represented by AR-006
and the Stage14-toolbox Stage15 cards.

## Superseded selectors

| Old selector | Current replacement |
|---|---|
| Stage14 s7-13 whole-family exponent `7/8` | AR-006 half-power upper |
| Stage24 `N_2(B) >> sqrt(log B)` global lower | S25-W01 quarter-power lower |
| Stage24 ratio lower `B^-1(log B)^(-9/2)` | `B^-3/4(log B)^(-5)` from S25-W01 and Stage18 |
| Stage23 `target unboundedness/positive-power lower not proved` firewall | S25-W01 global and directional lower |

## Selection rule

Use the strongest `ACTIVE` item only after population, cutoff, canonicalization,
multiplicity, measure and quantifier matching. Never multiply alternative
zero-density proofs or population interaction ratios as independent
probability factors. Historical cards remain searchable but cannot override
this registry's supersession state.
