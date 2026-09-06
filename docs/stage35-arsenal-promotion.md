# Stage35 / Stage35-EX Arsenal initial provisional harvest promotion

Status: `PROVISIONAL_INITIAL_HARVEST_IMPLEMENTATION`

```text
SOURCE_STAGE=Stage35 / Stage35-EX
INITIAL_HARVEST=true
DISCOVERY_PR=1669
DISCOVERY_EXACT_HEAD=28282d3f01a47bfedb4290c6219b36dbde89c784
IMPLEMENTATION_PR=1672
IMPLEMENTATION_BRANCH=stage35-arsenal-initial-provisional-harvest-promotion
STAGE35_CANONICAL_INCEPTION=43b5cc4a655cf68e9bdefad22800071d6f8d9fa0
STAGE35_EX_CANONICAL_INCEPTION=7423eab4f153df7e58c3c9aa7ef3ecdf3f53c4f8
HARVEST_LOWER_BOUND=43b5cc4a655cf68e9bdefad22800071d6f8d9fa0
HARVEST_UPPER_BOUND=9184c7ab694415592cc428a675c0ebed27cac510
INSPECTED_SCOPE=Stage35 from canonical inception plus Stage35-EX from canonical inception through frozen harvest upper bound
ARSENAL_REGISTRATION_DOES_NOT_CHANGE_STAGE35_MATHEMATICAL_AUTHORITY=true
```

Active Stage35 / Stage35-EX controller and source locks remain above every provisional card below. This registration creates no Stage35 progress, Stage35-EX progress, E1/Peschmann credit, uniform theorem credit, receiver closure, Brauer obstruction credit, endpoint credit, or perfect-cuboid existence/nonexistence conclusion.

Accepted Harvest-3 classifications only:

- new provisional weapons: `DISC-S35-A03,A05,A06,A08,A10`
- extensions without new IDs: `DISC-S35-A02,A09 -> S34-W01`; `DISC-S35-A04 -> Stage14 AR-017/AR-018 Gaussian orientation lineage`
- new provisional workflow: `DISC-S35-C05`
- historical/negative exclusions: `DISC-S35-E01-E06,F01-F03`
- Stage35-specific exclusions: `DISC-S35-A07,A11,B02,B07,D01-D03`
- rejected duplicates: `DISC-S35-A01,B01,B03,B04,B05,B06,C01,C02,C03,C04,C06`

## S35-PW01 PARAMETRIC_SQUARECLASS_COMPATIBILITY_GRAPH

**Maturity:** PROVISIONAL

Reusable contract:

```text
finite nonzero factor set
+ complete pair-product squareclass relations
+ exact identification of all squareclass-relevant shared-prime channels
+ fixed sign / 2-adic conventions
-> construct an edge-labelled graph in K*/K*^2
-> solve vertex squareclasses in terms of independent live reservoirs
-> permit the reservoirs to remain parameter-dependent and of non-fixed prime support
```

```text
HYPOTHESES=exact factor set; complete pair-product squareclass relations; all squareclass-relevant shared-prime channels identified; sign and 2-adic conventions fixed
APPLICABILITY=multi-factor square receivers where prime sharing is controlled but remains parameter-dependent
DO_NOT_USE_FOR=fixed finite squareclass enumeration; rational-point classification; receiver closure; S34-W01 exhaustiveness without a separate finite-support theorem
```

Source lock:

```text
source_pr=1511
source_exact_head=3642810596eb1aa6e58a59fd6805e872b2ac8bc1
authoritative_source=stages/stage35-ex/35ex-09/bridge-squareclass-graph.md
authoritative_source_blob_sha=1cbd3fdf4891ffabc1911ae19632f593a87b5d14
certificate=stages/stage35-ex/35ex-09/bridge-squareclass-certificate.json
certificate_blob_sha=000f32599d404e5b5ea0a3a3b8495d14405a8e5e
certificate_canonical_sha256=null
verifier=stages/stage35-ex/verify_stage35_ex.py
verifier_blob_sha=31c045b3414800eae272ed6fbacd6e224d851ca6
nearest_existing_card=S34-W01
```

Distinction: `S34-W01` requires a finite exhaustive squareclass branch family before downstream closure. `S35-PW01` stops earlier and outputs a complete parametric compatibility graph whose reservoirs may remain live and unbounded.

## S35-PW02 EXACT_RECEIVER_INVOLUTION_QUOTIENT_ADAPTER

**Maturity:** PROVISIONAL

Reusable contract:

```text
source receiver + exact order-two involution
-> transport the involution on the full receiver data, including auxiliary square roots
-> pass to invariant coordinates / fixed field
-> classify fixed and boundary loci
-> prove an exact converse reconstruction
-> obtain an iff quotient receiver rather than only model/j-invariant similarity
```

```text
HYPOTHESES=exact order-two involution; receiver equations and auxiliary square roots equivariant; fixed/boundary loci classified; all inverse denominators controlled
APPLICABILITY=Diophantine receivers with a genuine algebraic involution preserving the full source condition
DO_NOT_USE_FOR=quotient point implies rational source point without lift proof; arithmetic dimension drop; receiver emptiness; semilinear Galois descent by analogy
```

Source lock:

```text
source_pr=1567
source_exact_head=d836c743628b47d62e4db18c344981be8fe839f4
authoritative_source=stages/stage35-ex/35ex-26/base-involution-receiver-descent.md
authoritative_source_blob_sha=09be1e8edf30052750e68d04ea21821b8ffdb794
certificate=stages/stage35-ex/35ex-26/base-involution-receiver-certificate.json
certificate_blob_sha=ec3df8ed179295097878b1d8817edbf446418f2a
certificate_canonical_sha256=null
verifier=stages/stage35-ex/verify_stage35_ex_26.py
nearest_existing_card=S30-W02 (adjacent pattern only); S34-W03 downstream
```

Distinction: `S30-W02` is semilinear finite-action Galois descent. This is a rational algebraic involution on the complete receiver with exact quotient and converse; `S34-W03` is only downstream after such a dictionary exists.

## S35-PW03 RATIONAL_SOURCE_LIFT_PRESERVING_KUMMER_NORMAL_FORM

**Maturity:** PROVISIONAL

Reusable contract:

```text
exact quotient receiver
+ explicit rational-source lift discriminant
-> identify the missing rational-source lift as an iff square condition
-> change coordinates to an explicit Kummer-style simultaneous square system
-> prove forward and converse rational reconstruction
```

```text
HYPOTHESES=exact quotient receiver; explicit rational-source lift discriminant; nonzero denominators on the retained open; forward and converse source maps
APPLICABILITY=quotient receivers whose rational points over-cover the rational source and whose missing lift is exact square data
DO_NOT_USE_FOR=cohomological H2(mu2) lift binding; marked Brauer equality; Mordell-Weil closure; rational-point classification; quotient points without lift condition
```

Source lock:

```text
source_pr=1571
source_exact_head=dc1930632304d2c47e5583e4d8cb324cbbd73e15
authoritative_source=stages/stage35-ex/35ex-27/rational-source-lift-kummer-normal-form.md
authoritative_source_blob_sha=0c2e2ae3aa9624e6022ef02d5ede2f4ede303b1f
certificate=stages/stage35-ex/35ex-27/rational-source-lift-kummer-certificate.json
certificate_blob_sha=df6637ce8b5a4127edb70d5d1f1d973ee300a9ca
certificate_canonical_sha256=null
verifier=stages/stage35-ex/verify_stage35_ex_27.py
nearest_existing_card=S33-PW09; S31-W01
```

Distinction: `S33-PW09` is a marked cohomological Kummer-lift binding adapter and `S31-W01` is a quartic/elliptic birational adapter; neither supplies an algebraic rational-source lift condition for an over-covering quotient receiver.

## S35-PW04 RECIPROCAL_SHARED_FACTOR_RECEIVER_COMPRESSION

**Maturity:** PROVISIONAL

Reusable contract:

```text
completed simultaneous square receiver
+ exact elimination exposing a common reciprocal factor
-> factor out the shared term
-> give explicit forward/inverse square-root scalings
-> replace the source by a strictly smaller iff receiver
-> separately record whether reciprocal symmetry preserves the physical chamber
```

```text
HYPOTHESES=completed source receiver; exact elimination identity; shared factor exact; forward/inverse square-root scales rational and nonzero; boundary denominators classified
APPLICABILITY=coupled Kummer/norm/square systems with reciprocal paired factors
DO_NOT_USE_FOR=receiver closure; physical descent when chamber is not preserved; new character/isogeny credit already present upstream; point classification
```

Source lock:

```text
source_pr=1579
source_exact_head=21ce592d3f30fd10b421ed0d3be68a702c26c65a
authoritative_source=stages/stage35-ex/35ex-29/reciprocal-common-factor-kummer-compression.md
authoritative_source_blob_sha=b663ef8b27503b10263d882c7e831b9dba3c05a2
certificate=stages/stage35-ex/35ex-29/reciprocal-common-factor-kummer-certificate.json
certificate_blob_sha=2f9f89d0571753e5885cf37b64de5f9367146d4d
certificate_canonical_sha256=null
verifier=stages/stage35-ex/verify_stage35_ex_29.py
verifier_blob_sha=39a9d709d75788f7e9176dffceb37efcc6f23d5f
nearest_existing_card=S34-W03; S31-W01
```

Distinction: neither `S34-W03` nor `S31-W01` performs exact common-factor compression of a completed simultaneous square receiver.

## S35-PW05 FINITE_EXCEPTIONAL_PRIME_CLASSIFICATION_BY_CENSUS_WEIL_COMPLETION

**Maturity:** PROVISIONAL

Reusable contract:

```text
exact finite-field degeneration predicate
-> exhaustively classify all primes below an explicit threshold
+ construct an explicit smooth bounded-genus auxiliary curve/family for the complement
+ prove a bad-point bound
+ prove the Weil lower bound beats that bad-point count above the threshold
-> obtain the complete exceptional-prime set and a nondegenerate witness for every remaining prime
```

```text
HYPOTHESES=exact finite-field predicate; projective/canonical normalization for exhaustive small-prime census; explicit auxiliary curve/family; smoothness outside named bad primes; explicit bad-point bound; Weil lower bound stronger than bad-point count beyond a proved threshold
APPLICABILITY=all-prime local-support or degeneration classifications with finitely many small exceptional primes and a bounded-genus large-prime witness family
DO_NOT_USE_FOR=Q_p classification; global rational points; global squareclass exhaustiveness; large-prime witness without smoothness/bad-point proof
```

Source lock:

```text
source_pr=1633
source_exact_head=fcedffa7f2d768ee8b1bc78b04611e1f0a401e77
authoritative_source=stages/stage35-ex/35ex-35/goal4e-all-odd-prime-zero-support-classification.json
authoritative_source_blob_sha=58ffdb975e95ba1d636ab8ff3b364d5042fe94a7
certificate=stages/stage35-ex/35ex-35/goal4e-all-odd-prime-zero-support-classification.json
certificate_blob_sha=58ffdb975e95ba1d636ab8ff3b364d5042fe94a7
certificate_canonical_sha256=null
verifier=stages/stage35-ex/verify_stage35_ex_35_goal4e.py
verifier_blob_sha=37723cd995ad207e1a7899796a2b2f193f735729
nearest_existing_card=S34-W03
```

Distinction: `S34-W03` excludes one specified receiver intersection; this contract classifies the entire exceptional-prime set for a local property by finite census plus a uniform large-prime Weil completion.

## S35-WF01 ENDPOINT_RETURN_CIRCULARITY_FIREWALL

**Maturity:** PROVISIONAL WORKFLOW

Reusable workflow:

```text
original endpoint/source contract frozen
+ exact transform chain
+ explicit returned endpoint-like coordinate map
-> classify each returned predicate as inherited / newly derived / forbidden-to-reuse
-> require an explicit reverse/source adapter before re-importing primitive, orientation, or source-only hypotheses
-> prevent algebraic return to a familiar endpoint model from creating circular proof credit
```

```text
HYPOTHESES=original endpoint/source contract frozen; transform-chain provenance exact; returned endpoint-like coordinate map explicit
APPLICABILITY=long algebraic proof chains that return to an earlier geometric/endpoint model and risk circular reuse of assumptions
DO_NOT_USE_FOR=endpoint closure; theorem credit; reverse population equivalence without an adapter; reusing source-specific hypotheses because equations look identical
```

Source lock:

```text
source_pr=1581
source_exact_head=00d6199c0df611b0606b15b8a46897629363cb10
authoritative_source=stages/stage35-ex/35ex-30/endpoint-gauge-return-firewall.md
authoritative_source_blob_sha=e6db9d64941faafa8c906389f99ec3089e425576
certificate=stages/stage35-ex/35ex-30/endpoint-gauge-return-certificate.json
certificate_blob_sha=3057e494c8dbea2bfce8d636ead0fbcb962efff4
certificate_canonical_sha256=null
verifier=stages/stage35-ex/verify_stage35_ex_30.py
nearest_existing_card=S30-WF03
```

Distinction: `S30-WF03` controls upward semantic credit across typed layers; `S35-WF01` adds a distinct circularity check when a transformed route returns algebraically to an earlier endpoint model.

## S34-W01 Stage35 initial-harvest provisional extension

No new ID is created. Formal `S34-W01` remains the controlling card. Stage35 adds two provisional pre-enumeration adapters only:

1. **Dynamic reservoir preflight** (`DISC-S35-A02`): record the complete pairwise-gcd reservoir incidence table and separate odd-prime from sign/2-adic support; fail closed before finite squareclass enumeration if support remains parameter-dependent. Source PR/head `1511 / 3642810596eb1aa6e58a59fd6805e872b2ac8bc1`; source `stages/stage35-ex/35ex-06/four-factor-gcd-support.md` blob `9f3a3215536f7b9c52ddfd629b9af856fd7bb86c`; certificate blob `380d2ab51c4b1a646b4b5c3ba6aae5914ba02252`; verifier blob `31c045b3414800eae272ed6fbacd6e224d851ca6`.
2. **Primitive pair-gcd skeleton preprocessor** (`DISC-S35-A09`): from `gcd(A,B,C)=1`, extract pairwise-coprime shared gcds and private cofactors, and derive only source-justified coprimality/parity relations before factor/squareclass descent. Source PR/head `1603 / 51ae29a044d0e2524285e56237cf0e32269a54cf`; source/certificate blob `d0cd03a5ff744d5f6536b6d2784c0e0d543fea48`; verifier blob `d228ecc608ba7c4c26a7e7ba5b70d29186367b6e`.

These extensions do not change `S34-W01`'s formal conclusion and do not authorize finite exhaustive squareclass enumeration without its original hypotheses.

## Stage14 AR-017 / AR-018 Gaussian orientation lineage — Stage35 provisional extension

No new ID is created. `DISC-S35-A04` adds a source-locked **multi-orientation independence test**: quotient exact relabelings/mirrors, fix unit/conjugation ambiguity, and only then extract a joint quadratic-field squareclass or equivalent rational-coordinate square condition from two genuinely distinct oriented Gaussian square factorizations.

Source PR/head `1515 / 6a2193c19cce6d9022764c2daf6a2431e2348c1f`; source `stages/stage35-ex/35ex-13/alternate-norm-gaussian-coupling.md` blob `196d2be1bbfbcb2b416535d7bb051a9b2ec93104`; verifier `stages/stage35-ex/verify_stage35_ex_13.py` blob `7a5122ad30921548a18d8b7fba3af7af2cbd5214`. The standalone mirrored orientation remains duplicate; a necessary Gaussian square condition remains non-global.

## Negative / historical exclusions

`DISC-S35-E01-E06,F01-F03` are retained only in discovery PR #1669 for anti-loop/history. They are not active Arsenal weapons and receive no stable Stage35 ID.

## Stage35-specific exclusions

`DISC-S35-A07,A11,B02,B07,D01-D03` remain Stage35-specific payloads. They are not registered as reusable active weapons.

## Rejected duplicates

No new IDs for `DISC-S35-A01,B01,B03,B04,B05,B06,C01,C02,C03,C04,C06`. Their controlling interfaces remain the existing Stage34/Stage33/Stage30/Research-OS contracts identified by Harvest 3.

## Credit firewall

```text
ARSENAL_REGISTRATION_DOES_NOT_CHANGE_STAGE35_MATHEMATICAL_AUTHORITY=true
STAGE35_PROGRESS_INCREMENT=0
STAGE35_EX_PROGRESS_INCREMENT=0
E1_CLOSED=false
PESCHMANN_CONJECTURE_CREDIT_ADDED=false
UNIFORM_THEOREM_CREDIT_ADDED=false
RECEIVER_CLOSURE_ADDED=false
BRAUER_OBSTRUCTION_CREDIT_ADDED=false
ENDPOINT_CREDIT_ADDED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
