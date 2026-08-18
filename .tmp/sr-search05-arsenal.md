OVERLAPS=AR-002,AR-003,AR-004,AR-006,AR-028,AR-037,AR-038,AR-039
ARSENAL_PATH=docs/stage14-arsenal.md

### AR-002 — Primitive Euclid face decomposition

- **CATEGORY:** exact algebra / parametrization
- **ONE-LINE PURPOSE:** Replace an integral right-triangle face by a unique scale-times-primitive Euclid certificate.
- **INPUT SHAPE:** Positive integers `(e,x,u)` with `e^2+x^2=u^2` and a distinguished leg/orientation.
- **OUTPUT:** Primitive opposite-parity Euclid parameters plus a positive scale, unique after the stated orientation convention.
- **HYPOTHESES:** Exact square identity; parity and leg orientation fixed.
- **PHYSICAL DEPENDENCE:** Independent of integral space diagonal and of the third face.
- **MEASURE:** One-face certificate fiber.
- **QUANTIFIERS:** Pointwise exact.
- **LOSS / COST:** None.
- **REUSE CLASS:** `DIRECT_REUSE`
- **TRIGGER SIGNATURE:** A face-square condition appears and a primitive parameter pair is needed.
- **FAILURE CONDITIONS:** Do not forget the scale, swap the distinguished leg silently, or assume global cuboid primitivity from face primitivity.
- **SOURCE:** `stages/stage14/final.md`, Lemma 3.1 proof; `stages/stage13/final.md`, Sections 3.18–3.20 and 8.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `BACKGROUND`
- **DEPENDENCIES:** AR-001.
- **KNOWN APPLICATION:** Two-face gluing and the Stage12→13 projection bridge.
- **POSSIBLE FUTURE USE:** Stage15 ambient shared-edge normal forms and certificate validation.

### AR-003 — Exact two-face gluing and multiplicity one

- **CATEGORY:** exact algebra / reconstruction
- **ONE-LINE PURPOSE:** Glue two primitive oriented Pythagorean faces along a common leg without hidden scale multiplicity.
- **INPUT SHAPE:** `F_i=(S_i,X_i,H_i)`, a common physical edge, `k_1S_1=k_2S_2`, and global primitive canonical output.
- **OUTPUT:** With `g=gcd(S_1,S_2)`, `k_1=tS_2/g`, `k_2=tS_1/g`; the minimal glued triple is primitive, so global primitivity forces `t=1`.
- **HYPOTHESES:** Primitive face data (`gcd(S_i,X_i)=1`), distinguished shared edge, positivity, canonical ordering, global `gcd=1`.
- **PHYSICAL DEPENDENCE:** Independent of space-diagonal integrality as an algebraic gluing lemma; exact-two gives one shared edge and triple-face gives three.
- **MEASURE:** Raw shared-edge incidence measure.
- **QUANTIFIERS:** Pointwise exact.
- **LOSS / COST:** None.
- **REUSE CLASS:** `DIRECT_REUSE`
- **TRIGGER SIGNATURE:** Two face certificates share a leg and generator multiplicity must be proved.
- **FAILURE CONDITIONS:** Do not fold triple-face objects into exactly-two or omit orientation/swap conventions.
- **SOURCE:** `stages/stage14/final.md`, Lemma 3.1; `stages/stage14/archive/stage14-4ag-kummer-rank-jump.md`; `stages/stage15/README.md`, “Inclusion and multiplicity”.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `ACTIVE`
- **DEPENDENCIES:** AR-001, AR-002.
- **KNOWN APPLICATION:** Stage14 graph simplicity; Stage15 paired enumerator.
- **POSSIBLE FUTURE USE:** Any overlap graph built from two certified faces.

### AR-004 — Raw-pair incidence graph identity

- **CATEGORY:** counting / incidence geometry
- **ONE-LINE PURPOSE:** Convert exactly-two overlap counting into vertices times a uniform fiber degree.
- **INPUT SHAPE:** Physical integral-space-diagonal cuboids and primitive oriented face vertices; edges are raw unordered integral-face pairs.
- **OUTPUT:** `E(B)=N_2(B)+3T(B)=1/2 sum_F deg_B(F)` and `N_2(B)<=E(B)`.
- **HYPOTHESES:** AR-003 multiplicity one; exactly-two/triple separation; Stage14 cutoff `d<=B`.
- **PHYSICAL DEPENDENCE:** Primitive/canonical, integral space diagonal, whole family; triple objects retained.
- **MEASURE:** Whole Stage14 physical raw-incidence graph.
- **QUANTIFIERS:** Exact whole-family identity.
- **LOSS / COST:** None.
- **REUSE CLASS:** `STAGE14_SPACE_DIAGONAL_ONLY`
- **TRIGGER SIGNATURE:** Overlap objects can be represented as pairs of one-face records and vertex degrees may be controlled.
- **FAILURE CONDITIONS:** Not automatically an ambient Stage15 `B_2` theorem; rebuild the graph and degree model there.
- **SOURCE:** `stages/stage14/final.md`, Lemma 3.1; `stages/stage14/archive/stage14-4ag-kummer-rank-jump.md`.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `ACTIVE`
- **DEPENDENCIES:** AR-003.
- **KNOWN APPLICATION:** First step of the Stage14 square-root proof.
- **POSSIBLE FUTURE USE:** `A_2`-side overlap bounds or another family after a fresh graph statement.

### AR-006 — Stage14 physical whole-family square-root theorem

- **CATEGORY:** counting theorem
- **ONE-LINE PURPOSE:** Bound primitive canonical exactly-two cuboids with integral space diagonal.
- **INPUT SHAPE:** `0<a<b<c`, `gcd(a,b,c)=1`, integer `d`, `a^2+b^2+c^2=d^2<=B^2`, exactly two integral face diagonals.
- **OUTPUT:** `N_2(B)<<B^(1/2+o(1))`.
- **HYPOTHESES:** Full R04 proof chain AR-003–AR-016; same cutoff and physical masks.
- **PHYSICAL DEPENDENCE:** Entirely Stage14 with integral space diagonal, whole-family, not fixed direction/cell/U.
- **MEASURE:** Whole physical `A_2` family.
- **QUANTIFIERS:** For every epsilon, all sufficiently large `B`; every physical chamber.
- **LOSS / COST:** `B^o(1)` only above exponent `1/2`.
- **REUSE CLASS:** `STAGE14_SPACE_DIAGONAL_ONLY`
- **TRIGGER SIGNATURE:** A later argument needs a certified upper bound on the `A_2` numerator.
- **FAILURE CONDITIONS:** Says nothing directly about Stage15 ambient `M_2`, a lower bound, a strict sub-square-root saving, or perfect-cuboid existence.
- **SOURCE:** `stages/stage14/final.md`, Theorem 2.1 and Proposition 3.6; `stages/stage14/archive/tasks/14-X13/result.md`.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `ACTIVE`
- **DEPENDENCIES:** AR-003–AR-016.
- **KNOWN APPLICATION:** Final Stage14 theorem; Stage15 numerator context.
- **POSSIBLE FUTURE USE:** Upper-bound numerator in matched A/B comparisons only.

### AR-028 — Consumed/superseded/recharge-forbidden discipline

- **CATEGORY:** proof accounting
- **ONE-LINE PURPOSE:** Charge each support/core/fiber once and retain reusable mechanisms even after their exponent theorem is superseded.
- **INPUT SHAPE:** A multi-stage reduction ledger with exact data dependencies and competing parameterizations.
- **OUTPUT:** Each asset labeled `ACTIVE`, `CONSUMED`, `SUPERSEDED_BUT_REUSABLE`, `PARKED_EXTERNAL_GATE`, `NEGATIVE`, or `BACKGROUND`; recharging consumed support is forbidden.
- **HYPOTHESES:** Quantifier order and source-to-target maps recorded.
- **PHYSICAL DEPENDENCE:** General; Stage14 used it across MAIN/T/S/X/Q.
- **MEASURE:** The original charged outer measure of each item.
- **QUANTIFIERS:** Ledger-level invariant.
- **LOSS / COST:** Prevents duplicated fixed-power costs/savings; `B^o(1)` fibers remain multiplicity.
- **REUSE CLASS:** `DIRECT_REUSE`
- **TRIGGER SIGNATURE:** A later stage renames an old receiver, multiplies two counts of the same core, or deletes a superseded mechanism.
- **FAILURE CONDITIONS:** Superseded theorem exponent does not imply its exact lemma is false; consumed data cannot be charged again.
- **SOURCE:** `stages/stage14/final.md`, Sections 6–7; `stages/stage14/archive/review/manifests/stage14-final-self-contained-provenance-20260812-r01.md`; `stages/stage14/archive/tasks/14-Work-coX53/result.md`.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `ACTIVE`
- **DEPENDENCIES:** None.
- **KNOWN APPLICATION:** Final no-double-charge and route-closure audit.
- **POSSIBLE FUTURE USE:** Default proof-engineering ledger for all later stages.

### AR-037 — Finite-order Selberg--Delange contract

- **CATEGORY:** external theorem interface / analytic verification
- **ONE-LINE PURPOSE:** Lock exactly which finite-order Selberg--Delange theorem is imported and verify every coefficient, analytic-region, and vertical-growth hypothesis separately.
- **INPUT SHAPE:** `F(s)=zeta(s)^z H(s)` with fixed-degree divisor majorant and `H` regular in a standard zero-free-shaped region.
- **OUTPUT:** Any prescribed fixed logarithmic saving by choosing a fixed expansion depth `J`, with constants and uniformity recorded.
- **HYPOTHESES:** Analyticity of `H`; polynomial vertical growth on fixed strips; coefficient majorant; nonzero leading factor; all auxiliary parameters inside the declared uniformity.
- **PHYSICAL DEPENDENCE:** None in the contract; the factorizations `H` and their uniform ranges are application-specific.
- **MEASURE:** One-variable multiplicative coefficient sum, before any two-variable or curved-region transfer.
- **QUANTIFIERS:** Choose the required fixed log-saving and then fix `J`; no parameter-dependent expansion depth.
- **LOSS / COST:** External theorem dependence; later box summation must budget the chosen logarithmic power.
- **REUSE CLASS:** `REUSE_AFTER_EXACT_ADAPTER`
- **TRIGGER SIGNATURE:** An Euler product has a finite-order pole and a proof needs strong fixed log-power remainder rather than a guessed subexponential error.
- **FAILURE CONDITIONS:** Do not cite the theorem without mapping its analytic region and vertical growth, or use one-variable uniformity after introducing an uncontrolled conductor.
- **SOURCE:** `stages/stage12/final.md`, embedded Selberg--Delange reference lock and Stage12-N1-3h/3i/3j; Tenenbaum, Chapter II.5, Theorem II.5.2.
- **SOURCE CONFIDENCE:** `EXTERNAL_THEOREM_DEPENDENT`
- **STATUS:** `ACTIVE_REUSABLE`
- **DEPENDENCIES:** AR-024, AR-033.
- **KNOWN APPLICATION:** Stage12 `beta` and `1*beta` summatory expansions with arbitrary fixed log-power saving.
- **POSSIBLE FUTURE USE:** Any later Euler-product host after its exact factorization and uniformity ledger are supplied.

### AR-038 — Exact shared-hypotenuse convolution

- **CATEGORY:** exact algebra / representation convolution
- **ONE-LINE PURPOSE:** Count oriented two-triangle chains by convolving representations in which the shared integer `p` is first a hypotenuse and then a leg.
- **INPUT SHAPE:** Positive integer chains `x^2+y^2=p^2` and `p^2+c^2=d^2` under a declared height cutoff.
- **OUTPUT:** With `H(p)` the unordered positive hypotenuse representation count and `L_B(p)` the bounded leg representation count,
  `C_raw(B)=2 sum_(p<=B) H(p)L_B(p)`, while canonical primitive objects satisfy
  `C_prim(B)=2N_1(B)+4N_exact2(B)+6N_3(B)`.
- **HYPOTHESES:** Positive distinct sides; the shared `p` and cutoff are identical in both representation functions; primitive/canonical projection is applied only after the raw convolution.
- **PHYSICAL DEPENDENCE:** Stage11 uses integral space diagonal and one or more integral faces; the convolution pattern itself applies to any two compatible representation problems sharing `p`.
- **MEASURE:** Raw oriented chain measure, followed by a separately corrected primitive canonical object measure.
- **QUANTIFIERS:** Exact finite identity for every cutoff.
- **LOSS / COST:** None in the raw convolution; gcd, ordering, repeated-side, and multiple-face corrections remain coupled and cannot be multiplied in independently.
- **REUSE CLASS:** `REUSE_AFTER_EXACT_ADAPTER`
- **TRIGGER SIGNATURE:** One arithmetic value is represented in two roles and a chained population may factor through its representation counts.
- **FAILURE CONDITIONS:** Do not interpret `H(p)L_B(p)` as a primitive unique-object count or treat representation richness as repeated weight on one fixed incidence.
- **SOURCE:** `stages/stage11/scripts/audit_shared_p_convolution.py` and `stages/stage11/data/convolution_report.json`; absorbed analytically but not explicitly indexed in `stages/stage12/final.md`.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `BACKGROUND_REUSABLE`
- **DEPENDENCIES:** AR-002, AR-029, AR-032.
- **KNOWN APPLICATION:** Stage11 raw shared-face-diagonal convolution and the exact face-multiplicity identity.
- **POSSIBLE FUTURE USE:** Representation-function decompositions in Stage15, provided primitive and survivor corrections are kept outside the raw product.

### AR-039 — Mod-7 two-parameter exactly-one family

- **CATEGORY:** explicit construction / lower bound / regression family
- **ONE-LINE PURPOSE:** Produce an unconditional infinite primitive family with integral space diagonal and exactly one integral face.
- **INPUT SHAPE:** Coprime integers `m>n>=1` with `m=2 mod 14` and `n=1 mod 14`.
- **OUTPUT:** For
  `x=m^2-n^2`, `y=2mn`, `p=m^2+n^2`,
  `c=(p^2-1)/2`, and `d=(p^2+1)/2`, the canonical triple
  `(min(x,y),max(x,y),c)` is primitive, has exactly the `xy` face integral,
  and yields `N_1(B)>>B^(1/2)`.
- **HYPOTHESES:** The stated residue classes and coprimality; canonical ordering after construction.
- **PHYSICAL DEPENDENCE:** Integral space diagonal and exactly-one-face `A_1` population.
- **MEASURE:** An injective two-parameter subfamily, not the full `N_1` population.
- **QUANTIFIERS:** Every admissible pair; the lower bound comes from coprime pairs in `T<m<=2T`, `1<=n<=T`.
- **LOSS / COST:** `d<=(25T^4+1)/2` and the coprime rectangle count give
  `N_1(B)>=sqrt(2)/(120pi^2) B^(1/2)-O(B^(1/4)log B)`.
- **REUSE CLASS:** `STAGE14_SPACE_DIAGONAL_ONLY`
- **TRIGGER SIGNATURE:** A proof, enumerator, or regression suite needs certified primitive exactly-one positive examples with a symbolic non-square certificate.
- **FAILURE CONDITIONS:** This is a lower-bound subfamily only; it gives no upper bound for `N_2`, no little-`o` comparison, and no full `N_1` asymptotic.
- **SOURCE:** `stages/stage11/scripts/audit_shared_p_convolution.py` and `stages/stage11/data/convolution_report.json`; Stage10's one-parameter predecessor is `stages/stage10/scripts/audit_one_face_lower_bound.py`.
- **SOURCE CONFIDENCE:** `PROVED_CANONICAL`
- **STATUS:** `BACKGROUND_REUSABLE`
- **DEPENDENCIES:** AR-001, AR-002, AR-030.
- **KNOWN APPLICATION:** Stage11 unconditional `N_1(B)>>B^(1/2)`; modulo 7 forces both remaining face sums to residue `6`, a nonsquare.
- **POSSIBLE FUTURE USE:** Positive regression fixtures, constructive lower bounds, and local-obstruction sanity checks on the A-side.

## Audit summary

- Every `DIRECT_REUSE` entry states exact hypotheses and measure.
- Stage14-space-diagonal theorems are primary-class marked; other Stage14-dependent entries also say so under physical dependence.
- Fixed-U AR-021/022 are local and cannot silently become whole-family results.
- Every `B^o(1)` occurrence is labeled multiplicity/equivalence unless a separate analytic role is stated.
- Same-kernel/different-measure cases are AR-023/024 and indexed explicitly.
- Superseded but reusable mechanisms AR-009/010/014/015/017/018 are retained.
- External/no-go knowledge AR-020/022/025/026/027 and diagnostic AR-031 are retained.
- Upstream reusable mechanisms AR-032–AR-037 are provenance-labeled and require exact population/measure adapters.
- Early-stage survivors AR-038/039 retain one exact convolution and one certified construction; Stage02–10 otherwise add no unsuperseded weapon.
- The registry asserts no new Stage14 theorem and restarts no parked route.

## Frozen registry report

```text
ARSENAL_ENTRY_COUNT=39
DIRECT_REUSE_COUNT=6
ADAPTER_REQUIRED_COUNT=20
NEGATIVE_KNOWLEDGE_COUNT=8
SPACE_DIAGONAL_ONLY_COUNT=6
STAGE15_CURRENTLY_RELEVANT_COUNT=10
UNINDEXED_STAGE14_REGIONS_REMAINING=NONE_IDENTIFIED_AFTER_R04_BURIED_GOLD_AND_TARGETED_SOURCE_AUDIT
ARSENAL_READY_FOR_FUTURE_AGENT_SEARCH=true
```

`ADAPTER_REQUIRED_COUNT` combines eighteen `REUSE_AFTER_EXACT_ADAPTER` entries and two `SAME_KERNEL_DIFFERENT_MEASURE` entries. `NEGATIVE_KNOWLEDGE_COUNT` counts AR-020, AR-022–AR-027, and AR-031. Historical exponent-only stages not cited by R04's source/provenance/buried-gold ledgers remain deliberately outside the Arsenal; their current bounds are superseded and no additional reusable mechanism was identified by the targeted audit.

**High-value reusable weapons:** AR-003 two-face gluing; AR-009 primitive Gaussian root lines; AR-012 reverse reciprocal reconstruction; AR-016 divisor/finite-fiber adapter; AR-023 scalar/pair separation; AR-028 recharge discipline; AR-032 primitive-first Möbius; AR-033 weighted rectangles; AR-035 fixed-prime overlap sieve; AR-036 ordered-chamber transfer; AR-038 shared-hypotenuse convolution; AR-039 certified exactly-one family.

**Five most dangerous traps:** AR-024 same kernel/different conditioned measure; AR-023 scalarizing `(E,m)` through divisor-many fibers; AR-027 average→every-cell promotion; AR-021/022 fixed-U or conductor-range promotion; AR-005/006 Stage14 integral-space-diagonal→Stage15 ambient promotion.

