# Stage13-13fi — R05 review manifest

```text
BUNDLE_ID=STAGE13-FINAL-SELF-CONTAINED-20260809-R05
SOURCE_SNAPSHOT_COMMIT=79f03341b67dd49a8c128cfbeba3f756c91de6f6
CONTENT_SHA256=4214a6e3621b52ce39373799b48fc8325351f650514e732d6e2244d28d475458
BUNDLE_PATH=review/STAGE13-FINAL-SELF-CONTAINED-20260809-R05.html
R05_IMMUTABLE=true
R04_IMMUTABLE=true
R03_IMMUTABLE=true
THEOREM_CHANGED=false
R05_FRESH_EXTERNAL_REVIEW_REQUIRED=true
R04_VERDICTS_CARRY_FORWARD_TO_R05=false
DETERMINISTIC_AUDIT_SCOPE=REPRODUCIBILITY_AND_CONSISTENCY_ONLY
NEXT=13-13fj
```

## Review target

The byte-for-byte review target is `review/STAGE13-FINAL-SELF-CONTAINED-20260809-R05.html`. Its SHA-256 is
`4214a6e3621b52ce39373799b48fc8325351f650514e732d6e2244d28d475458`. The source snapshot is the merged Gate-H commit
`79f03341b67dd49a8c128cfbeba3f756c91de6f6`.

Any substantive repair must create an immutable R06 or later bundle; R05 is
never edited in place.

## Included source snapshot

Every embedded source is read with `git show` from the fixed snapshot:

- `stages/stage13/13-13fh/stage13-r05-canonical-proof.md` — SHA-256 `237fa8fce22bbd54ab320d82714ba9d287f72654cf12789d1c997167408f4952`
- `stages/stage13/13-13ff/external-theorem-contracts.md` — SHA-256 `42413e367c8aeffcbf5ee8a08cfbe87e1682b03b1aefca2dc2d1523725e92422`
- `stages/stage13/13-13fa/result.md` — SHA-256 `89d2bbe57a1fd994b13d84f91720a14dc4823309668bc265594f3385d614f89d`
- `stages/stage13/data/13-13fa/q_independence_finite_audit.json` — SHA-256 `e8f5d33252bc81cf71a2b68344d1ff5cb3095df63d345b00c2ace0ba015aa044`
- `stages/stage13/13-13fh/result.md` — SHA-256 `1b4e7df75fa71c5d8b97e50c3be2f3ca24e789043421666b9f87c377d7a30580`
- `stages/stage13/data/13-13fh/r05_synthesis_readiness_audit.json` — SHA-256 `2729440a04909a7adbd8471310c5d42aa0e29681e6984019af873eb008871df3`

## Frozen theorem contract

```text
N_q(B) ~ kappa I_q/(3 pi^3) B(log B)^3
N1(B)  ~ kappa/(24 pi) B(log B)^3
P_q    = 8 I_q/pi^2
sum I_q = pi^2/8
J_q    = 2 I_q/pi
O_qr(B)=o(B(log B)^3)
T(B)   =o(B(log B)^3)
lambda_p=(p+5)/(2(p+1))
```

## Review policy

R05 begins a fresh external-review ledger. Final Stage13 freeze remains blocked
until this final bundle (or a later repaired immutable bundle) receives at
least two independent `CLOSED` verdicts and has zero unresolved theorem-level
objections.

```text
STAGE13_13FI=COMPLETE_R05_REVIEW_BUNDLE
R05_IMMUTABLE=true
R05_FRESH_EXTERNAL_REVIEW_REQUIRED=true
PROMOTE_TO_13_13G=false
NEXT=13-13fj
```
