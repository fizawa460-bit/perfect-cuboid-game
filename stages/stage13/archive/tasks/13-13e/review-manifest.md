# Stage13-13e — R04 review manifest

```text
BUNDLE_ID=STAGE13-FINAL-SELF-CONTAINED-20260809-R04
SOURCE_SNAPSHOT_COMMIT=f652833d194bade57794e4c03c184928a54a31b9
CONTENT_SHA256=789656b5bb2190ae62cf2dcae7a3da06ece4f473780a1229ba7284b10b7f4f1b
BUNDLE_PATH=review/STAGE13-FINAL-SELF-CONTAINED-20260809-R04.html
R04_IMMUTABLE=true
R03_IMMUTABLE=true
THEOREM_CHANGED=false
DETERMINISTIC_AUDIT_STATUS=PASS
NEXT=13-13f
```

## Review target

The byte-for-byte review target is `review/STAGE13-FINAL-SELF-CONTAINED-20260809-R04.html`. Its SHA-256 is
`789656b5bb2190ae62cf2dcae7a3da06ece4f473780a1229ba7284b10b7f4f1b`. Any substantive repair must create a new R05/R06 bundle; R04 is
never edited in place.

## Included source snapshot

All embedded material is read with `git show` from source snapshot
`f652833d194bade57794e4c03c184928a54a31b9`:

- `stages/stage13/13-13c/stage13-final-proof.md` — SHA-256 `2824b435f783bc51543255ba3d378ca4715e6bf69748ce0b24b46bae2b04d383`
- `stages/stage13/13-13b/external-theorem-crosswalk.md` — SHA-256 `3257722939afa137180a76e07b2cddb91409aafe0ff6956c8303a73852e6eaeb`
- `stages/stage13/13-13a/result.md` — SHA-256 `f451207ba7319f1ed7205b747b27b1f1a1b79ab9a9a0514981b9fb0762774cdd`
- `stages/stage13/13-13d/result.md` — SHA-256 `c836127c9e8c595ad8b3a35bd31cde0bd30970ac2d65d6daa6eea26e3366ff2f`
- `stages/stage13/data/13-13d/final_consistency_audit.json` — SHA-256 `dc10c23ed8af7b5fac11b1639d943822d95b0fc26532362ee6b7ae9814123185`

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

R04 is a review snapshot, not the final Stage13 freeze. Stage13-13f targets
independent Grok/Qwen/Claude review when available. Promotion to Stage13-13g
requires at least two independent `CLOSED` verdicts and zero unresolved
received theorem-level objections.

```text
STAGE13_13E=COMPLETE_R04_REVIEW_BUNDLE
R04_IMMUTABLE=true
R03_IMMUTABLE=true
NEXT=13-13f
```
