# Stage14-num-α9 — exact B300m extension with B250m checkpoint

> STATUS: `STAGE14_NUM_ALPHA9=COMPLETE_EXACT_B300M_WITH_B250M_CHECKPOINT`
>
> CLASSIFICATION: finite exact census + operational finite stability diagnostics; no asymptotic claim.

Dedicated Actions run `31316301867` completed the four new 25m shards over `200m<d<=300m`. The nested B200m subset reproduced merged α8 in every frozen count, graph field and SHA lock.

## Exact checkpoints

```text
B250m: (Na,Nb,Nc)=(1032,1049,576), N2=2657, T=0
        active faces=3837, max degree=11
B300m: (Na,Nb,Nc)=(1117,1131,618), N2=2866, T=0
        active faces=4146, max degree=11
```

B250m SHA locks: object `864bdd1b33ba6588e3588794e3cc77b75183f228fefca2c1a01f9bc12014e5b6`, object+mask `17a855f4d99b37d4786621387cdfcf11d7b51a6f6e39b0e010eaba30487ebd15`, vertex `4a88038b2c43d1b49c249b37bcdacc2b8f726a6d9847d80be1caada8bb293dff`, edge `b0ec0187089980aed4b6984c5394e8d5263f582b9c176fe4c2861d866abe88cc`.

B300m SHA locks: object `1da0c7454db30a1c216e260cbaca23018fa052d5561b9daefd7e62cba664d3a5`, object+mask `828c226c4e2e665fa78b6e60725eb76ad8f97ecab1c18bfad8ccf2e49573cdae`, vertex `f4ecb8296ba6e9b9ca5a70abf9e5334890ad8adda23bd099a57dab5108990c5b`, edge `a5c4b275dc5d3bb0bae0642e6029156fd3b8e1e85c1eb055a1d184e287c84a85`.

New shell counts are `{'a': 75, 'b': 82, 'c': 43, 'total': 200, 'triple': 0}` for 200m→250m and `{'a': 85, 'b': 82, 'c': 42, 'total': 209, 'triple': 0}` for 250m→300m.

## Stability panel

`N2/sqrt(B)` moves `0.173736136137535 -> 0.168043434861348 -> 0.165468587149747`. The 200m→250m transition fails the 2% operational gate only because `R0` moves by `3.3876%`. The 250m→300m transition is the first post-B200m transition with every primary metric below 2%; its largest primary drift is `1.5561%`.

This is a finite stopping diagnostic only. The terminal gate is not evaluated until α11 has 250→300m, 300→400m and 400→500m. `T=0` through B300m is not a nonexistence proof.

```text
B200M_ALPHA8_FULL_HASH_REGRESSION_MATCH=true
B250M_EXACT_CENSUS_FROZEN=true
B300M_EXACT_CENSUS_FROZEN=true
FIRST_POST_B200M_STABILITY_PANEL_PUBLISHED=true
B250M_TO_B300M_ALL_PRIMARY_DRIFTS_LE_2PCT=true
PERFECT_CUBOID_EMERGENCY=false
FINITE_DIAGNOSTIC_ONLY=true
ASYMPTOTIC_CLAIM=false
NEXT=Stage14-num-alpha10 exact B400m checkpoint
```
