# Stage35 35-01 — source lock and model inventory

```text
UNIT=35-01_SOURCE_LOCK_AND_MODEL_INVENTORY
VERDICT=PASS
NEW_THEOREM_CREDIT=false
R29_FIB2_CLOSED=false
NEXT=35-02_Q_FIELD_PHYSICAL_FIBRATION_LEDGER
```

The three Stage29 entry sources were replayed by exact Git blob SHA through the GitHub connector and matched the Stage35 locks:

```text
stages/stage29/29-16/active-kernel-ledger.json  5d6d4c7709b57064aea5dc0ece672c5170c39550
stages/stage29/29-08/fibration-crosswalk.md       de360854d63cf6a7462ae2a519861f45d058d899
stages/stage29/29-14/theorem-dependency-ledger.json 3978633fca1bd70d89709af49caa37171f649649
```

The compact machine certificate is `source-lock-and-model-inventory.json`; `verify_35_01.py` independently checks the Git blob locks and the load-bearing Stage29 semantics from a repository checkout.

## Frozen entry models

- Full endpoint coordinates are `[e:x:y:p:q:z:d]` with the four cuboid square equations.
- Forgetting only the sign of `d` gives the Euler K3 quotient in `[e:x:y:p:q:z]`; the Stage20/Testa--Stoll normal/minimal-resolution adapter is over `Q`.
- The Euler K3 has 15 geometric elliptic fibrations, but all 15 are not certified individually over `Q`; rank-4 rulings can require splitting fields.
- Peschmann's total `(m,n)` fibration after gcd normalization globally covers the Euler-brick marginal chart. Its source-level lift requires `P` outside the exceptional torsion set, `tau(P)` a positive rational square, and the reduced-Euclid positivity/parity/coprimality checks. Bounded MW enumeration is not exhaustive.
- The full endpoint surface has 28 geometric genus-5 fibrations; all 28 are not certified individually over `Q`, and the first rank-4 pair is over `Q(i)`. Geometric atlas coverage is not rational-point coverage.
- Saunderson and StageA2 remain non-global families.
- Every physical endpoint `Q`-point pushes to each audited `Q`-defined coordinate-sign K3 quotient smooth locus/minimal resolution, but no converse lift or quotient emptiness follows.

## Exit boundary

35-01 closes only source/model inventory. It does not resolve `R29-FIB1`, does not materialize a general per-fibration residual endpoint lift, and grants no receiver/theorem/endpoint credit.

35-02 must now certify the `Q`/splitting-field and physical-class ledger for the fibration classes actually retained for attack, including parameter bases and exceptional/degenerate loci.
