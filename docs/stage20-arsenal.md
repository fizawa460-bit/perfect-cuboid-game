# Stage20 reusable arsenal

STATUS=AUDITED_PASS
REGISTRY=STAGE20-ARSENAL-R01

These entries are portable interfaces for later Stage16-28 work. They do not replace their canonical proof sources.

## S20-W01 — Explicit Euler thin-cover upper interface

```text
NAME=S20-W01_EXPLICIT_EULER_THIN_COVER_UPPER
TYPE=theorem
SOURCE_STAGE=Stage14-e11 reused and frozen by Stage20-70
ASSUMPTIONS=primitive canonical Euler cuboids; 0<a<b<c; gcd=1; Euclidean R<=B; all three face diagonals integral; no space-diagonal integrality condition
VALID_RANGE=as B->infinity; every fixed eta<1/46
WHAT_IT_DOES=M3(B)<<_eta B(log B)^(5-eta); concrete safe form M3(B)<<B(log B)^(5-1/50)
WHAT_IT_DOES_NOT_DO=does not prove endpoint eta=1/46; does not prove a power saving B^(1-delta); does not identify the true exponent or asymptotic constant; does not impose an integral space diagonal
POTENTIAL_RECEIVERS=Stage26,Stage27,Stage28
AUDIT_STATUS=SOURCE_AUDITED_STAGE14_E11;STAGE20_PROMOTION_AUDITED_PASS
```

Canonical provenance: Stage14-e11 / PR #188. Stage14-e10 and e8 remain weaker valid provenance layers.

## S20-W02 — Primitive Saunderson quantitative lower family

```text
NAME=S20-W02_PRIMITIVE_SAUNDERSON_LOWER
TYPE=theorem|method
SOURCE_STAGE=Stage20-50a
ASSUMPTIONS=even integer m>=10; u=m^2-1,v=2m,w=m^2+1; A=u|4v^2-w^2|,B1=v|4u^2-w^2|,C=4uvw
VALID_RANGE=all sufficiently large Euclidean cutoff B after canonical sorting
WHAT_IT_DOES=produces distinct primitive canonical Euler cuboids with R<31m^6 and proves M3(B)>=floor((B/31)^(1/6)/2)-4, hence M3(B)>>B^(1/6)
WHAT_IT_DOES_NOT_DO=does not match the upper bound; does not prove exponent 1/6 is intrinsic or sharp; does not prove a square-root law; does not impose an integral space diagonal
POTENTIAL_RECEIVERS=Stage26,Stage27,Stage28,any future Euler-population lower-bound comparison
AUDIT_STATUS=Stage20-50_PROVED_AUDITED_PASS;STAGE20_PROMOTION_AUDITED_PASS
```

Canonical proof: `stages/stage20/20-50/construction-proof.md`; proof-complete transcription also appears in `stages/stage20/final.md`.

## S20-W03 — Euler local blocker law

```text
NAME=S20-W03_EULER_LOCAL_BLOCKER_LAW
TYPE=obstruction|theorem
SOURCE_STAGE=Stage14-e10/e11 reused and frozen by Stage20-60/70
ASSUMPTIONS=Stage14-e/Stage20 two-face toric host under the same primitive/canonical Euclidean-height population; third-face completion x^2+y^2=square
VALID_RANGE=p=2 exact physical law; every odd prime p; fixed-prime products; growing-prime sieve only under the e11 theorem contract
WHAT_IT_DOES=provides delta_2=2/9 and delta_p=2(p-chi_4(p))/(p^2+6p+1)=2/p+O(p^-2); gives a concrete arithmetic obstruction and sieve dimension two; e11 supplies growing-prime uniformity
WHAT_IT_DOES_NOT_DO=does not prove independence of primes beyond the certified adelic/sieve statement; does not determine the global Euler exponent; must not be multiplied with K3/divisor losses as independent costs
POTENTIAL_RECEIVERS=Stage26,Stage27,Stage28
AUDIT_STATUS=SOURCE_AUDITED_STAGE14_E10_E11;STAGE20_PROMOTION_AUDITED_PASS
```

## Routing summary

| Weapon | Primary receiver | Main use |
|---|---|---|
| S20-W01 | Stage26/27 | certified target upper bound and zero-density input |
| S20-W02 | Stage26/27 | target survival floor and infinitude |
| S20-W03 | Stage26/28 | causal obstruction and anti-independence bookkeeping |

```text
ARSENAL_ENTRY_COUNT=3
ARSENAL_PROMOTION_REQUIRED=YES
ARSENAL_PROMOTION_STATUS=AUDITED_PASS
STAGE20_CLOSEOUT_AUDIT=PASS
```
