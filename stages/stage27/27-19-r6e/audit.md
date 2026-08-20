# Stage27-19-r6 — fresh audit

```text
AUDIT_ID=Stage27-19-r6-audit
AUDITED_TASKS=r6b,r6c,r6d,r6e
AUDITED_PR=1251
AUDITED_HEAD=9272a9cd6d5125f745b924446e4e62f5b566e678
AUDIT_VERDICT=PASS
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_TO_CHECKPOINT50=false
CURRENT_MU=1/2
NEXT_ROUTE=Stage27-19-r402g
```

## Audit findings

1. **r6b PASS.** The identities
   `P=(2E/G^2)B0` and `Q=(2E/G^2)A0` imply prime-by-prime
   `v_l(P)-v_l(Q)=v_l(B0)-v_l(A0)`. Hence the occupied-R squareclass collision is exactly the existing Stage15 squareclass predicate in toric coordinates. Charging a second squareclass sieve would double-count the same arithmetic condition.

2. **r6c PASS.** For a primitive occupied space diagonal `R`, `2|R` forces all three physical edges even. Likewise any prime `p=3 mod 4` dividing `R` forces both coordinates in each norm representation divisible by `p`, and hence all three physical edges divisible by `p`. Therefore `R` is odd and every prime divisor is `1 mod 4`. This restriction is genuine but logarithmic-only as a support condition and does not by itself yield a fixed-power deficit.

3. **r6d PASS.** For fixed reduced `(p,q)` and core `g`, `s^2|pg`; there are at most `tau(pg)` choices for `s`, and for each `s` at most `r_2(pg/s^2)<=4 tau(pg)` ordered positive `(m,n)` candidates. The second equation fixes at most one positive `r`. Thus the representation multiplicity is at most `4 tau(pg)^2=B^o(1)` uniformly on the physical range `pg<2B^2`. Consequently the polynomial exponent of a fixed-tau fiber is the exponent of its realized `g` support up to subpower loss.

4. **r6e PASS.** No new lower-lane reopen input was produced, so reopening r401d would violate the anti-loop contract. In contrast r6d supplies genuinely new input to the previously frozen r402f contract by removing fixed-core representation entropy. Redirecting to r402g is therefore a legal non-blind restart.

## CI / integrity

The dedicated workflow `Stage27-19-r6b-r6e route verdict` completed successfully on the audited head (run `32349700130`). The verifier checks the toric identities, known occupied-R split-prime support witnesses, and finite fixed-core multiplicity cases. PR #1251 was mergeable at audit time.

## Final route verdict

```text
R6_STANDALONE_FIXED_POWER_VIABILITY=NO_GO
R6_SQUARECLASS_LANE=FREEZE_DUPLICATE_OF_STAGE15
R6_SPLIT_PRIME_SUPPORT_LANE=FREEZE_LOGARITHMIC_ONLY
R402F_REPRESENTATION_MULTIPLICITY_GATE_DISCHARGED=true
UPPER_ALTERNATE_HAS_NEW_INPUT=true
SELECTED_NEXT_ROUTE=Stage27-19-r402g
SELECTED_NEXT_TARGET=TAU_REALIZED_CORE_SUPPORT_ENERGY_WITH_FIXED_CORE_MULTIPLICITY_REMOVED
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
AUDIT_STATUS=PASS
MERGE_ALLOWED=true
```
