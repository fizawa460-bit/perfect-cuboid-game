# EXP16 — Resync audit: lab premises vs current repo state (2026-11-21)

## Trap-B line
Finite claim = "a complete discrepancy list: every factual claim
in the ledger's Ground facts section and Tried list (T1–T7) is
marked CONFIRMED, CORRECTED, or SUPERSEDED against the repo's
current files, with file pointers". Stop condition = every
listed claim checked. This audit moves no goal-connected
number (the ≈3100× ZF yardstick is untouched, as expected);
its value is map accuracy and surprises. One genuine surprise
was found (D1). Method: read the ledger's Ground facts, T1–T7,
and the queue/log claims that rest on repo state; checked each
against the clone at ~/workspace/perfect-cuboid-game,
stage35-ex subtree, 2026-11-21.

## Headline finding (D1) — the repo did not stop at row393
The lab's picture "R3 reached row393 and stopped" is the
AUDITED truth but not the whole recorded truth. MAIN-START-
HERE.md records two owner instructions the lab never cited:
(1) 2026-11-08 — publication work only, research paused after
the row393 snapshot; (2) 2026-11-10 — owner-authorized
resumption of ONLY the same signed −30 / row393 route,
documented in research/r3-row393-resume-20261110/ (PR #1861).
That tree contains SIX relation-harvesting waves (all dated
2026-11-10 JST, author exact replay + same-author second
implementation, NO external independent audit, NO formal row
adoption — the working label "394" is explicitly unadopted,
and MAIN-STATE authority is unchanged). Their cumulative
effect on the finite presentation over the 878-prime base
(norm ≤ 6768):

  wave1 (new394): residual 181 → 181, individually-zero 628
  wave2:          residual 181 → 180, zero 628
  wave3:          residual 180, zero 628 (held candidates done)
  wave4:          residual 180 → 178, zero 628
  wave5:          residual 178 → 177, zero 628 → 630
                  [(3313,2), (4957,0) killed]
  wave6:          residual 177 → 175, zero 630 → 636
                  [(827,0), (1277,3), (2939,2), (2999,0),
                   (6373,1), (6571,0) killed]

Cumulative: 4,632 new algebraic integers, 4,619 independent
new principal relations; unconditional exclusions 0 (stated
in every wave). Next surviving head on the finite
presentation is now P_(953,0), with a recorded dual
certificate (wave6/README.md §"P953の残存と旧双対証書").
Every wave restates: the residual is NOT a class-group
dimension or bound, generation is NOT certified, c_Cl is
undecided. So no lab VERDICT changes; several lab NUMBERS
quoted as current are stale (see D2, D5).

## Discrepancy list

### Ground facts
- G1 Target (c_Cl = 0 or rank J(Q) ≤ 9; dim Sel⁽²⁾ = 9 + c_Cl;
  −30 source forces rank ≥ 10). CONFIRMED.
  classgroup-and-different/proofs/row385.md:38
  (dim 𝒰 = 9, dim 𝒮 = 9 + c_Cl); negative30-mw-selmer/
  row384/PROOF.md:103 (rank ≥ 10 via row382 jet + 8 classes,
  dim Sel⁽²⁾ ≤ 9 + c_Cl from row381); publication/major-
  routes/04-minus30.md states the same reduction.
- G2 row381: c_Cl = 0 under quadratic Hecke GRH (conditional).
  CONFIRMED. negative30-mw-selmer/audits/row381.txt:
  VERDICT=PASS_SCOPED_DEPENDENT_CONDITIONAL_QUADRATIC_HECKE_
  GRH_WITH_RANK31_AUTHOR_CHAIN_LIMIT; CONDITIONAL_NEW_SIGNED_
  SOURCE_EXCLUSION=1 (−30), UNCONDITIONAL=0. negative30-mw-
  selmer/CLAIMS.json: c_Cl_zero_unconditionally_proved=false.
- G3 row383: Gal(L/Q) = S_105; c_Cl ≥ 1 ⇒ zero in 3 bands
  (Re > 0.562/0.572/0.605, |Im| < 2.12); score ≈ +0.009886 vs
  threshold 49/5000, gap 29/1000. CONFIRMED. row383/PROOF.md
  band table (lines 9–11) and ℬ_χ(F) > 49/5000 with lower
  bound 0.00988588984309… (line 83–86); audits/row383.txt:
  PASS_SCOPED_DEPENDENT_..._UNCONDITIONAL_NECESSARY_THREE_
  HECKE_ZERO_BANDS_AND_GALOIS, NEW_UNCONDITIONAL_SIGNED_
  SOURCE_EXCLUSION=0, LOW remainder 9 absolute / 16 signed.
- G4 row384: c_Cl ≥ 2 ⇒ zero in Ω2 (Re > 0.63, |Im| ∈
  (0.26,0.77) ∪ (1.03,1.46)); open obligations ZF2 and δ★
  Sel4 non-lift, with the quoted "次は ZF2 と δ★ の4リフトを
  具体的に検査する". CONFIRMED as a statement of what
  row384/audit say (row384/PROOF.md:7–8; audits/row384.txt:
  "AUDIT DOES NOT PROVE ZF2 OR DELTA_STAR_NONLIFT. THE TWO
  OPEN OBLIGATIONS ARE PRESERVED."). SUPERSEDED IN PART as a
  description of the current open state: the δ★ inspection
  the quote calls for WAS executed (rows 385–387; lab EXP04/
  EXP15) and terminated UNDETERMINED with a named blocker
  (generation certificate); it is not "pending inspection"
  any more. ZF2 remains genuinely untouched. Repo flags
  agree both are unproved: negative30-mw-selmer/CLAIMS.json
  ZF2_proved=false, delta_star_Sel4_nonlift_proved=false;
  classgroup-and-different/CLAIMS.json qstar_computed=false,
  true_Sel4_decided=false. Consequence: the ground-facts
  entry now carries a dated annotation (ledger); no queue
  item changes (E3 covers ZF2, E4/E12 cover δ★).

### Tried list
- T1 (R3 rows 370–393: 878 primes norm ≤ 6768, formal
  residual 181; generation certificate needs all primes
  < 2⁹⁴; DEAD as a finishing method). Numbers CONFIRMED for
  the audited row393 endpoint (04-minus30.md row393 table:
  878 base, individual zero 616 → 628, formal 193 → 181,
  matrix 14,186 × 43,814, rank 13,627, kernel 559;
  audits/row393.txt exists; classgroup CLAIMS.json
  formal181_is_classgroup_rank_or_bound=false). Verdict
  CONFIRMED — every resume wave restates it. But the entry
  is SUPERSEDED as a description of the repo's current
  recorded state: per D1, the unaudited resume waves moved
  the same presentation to residual 175 / zero 636 and
  killed P_(827,0). Any lab text quoting 181 or 628 as
  CURRENT (rather than "audited row393 endpoint") is stale.
  Consequence: T1 annotated in the ledger; no experiment
  depended on 181 as a target, so no queue change.
- T2 (Odlyzko: root disc 44.5 vs unconditional ≈ 23.9).
  CONFIRMED AS LAB-INTERNAL — no repo source exists in the
  −30 materials (the only "Odlyzko" hits in stage35-ex are
  selmer18-parent-chain records for the ±18 degree-36
  field). The figure is the lab's own 2026-11-21 literature
  scout, presented in the ledger without a source pointer.
  Nothing in the repo contradicts it. No change, but the
  ledger entry should not be read as repo-audited.
- T3 (analytic score barrier: score < −0.000142 even with
  800k primes, in that normalization). CONFIRMED verbatim:
  04-minus30.md:57 — "全帯一律非負・現行有限素点資料・未知項
  の追加正下界無しという解析方式では、新2003素点を過大に加え
  てもスコア上側<−0.223342461、さらに80万素点でも
  <−0.000142461。これはその方式の障壁であり、あらゆる解析的
  証明の不可能性ではない。" The ledger's scoping matches.
- T4 (row383 fixture: 20 weights, lengths 229/25 + 397/200×2
  + 56/125×3, support T = 7237/500, Hadamard σ = 7/5,
  ε = 1/100). CONFIRMED: row383/fixture383.json (lengths
  incl. "229/25"); EXP01 replayed all 14 certified values
  exactly against spectral383.json.
- T5 (row384 3-char average, odd-power bound −1/3, Ω2).
  CONFIRMED: row384/PROOF.md:7–8.
- T6 (row383 §5 genus constraint consumed; output the
  W(D_105) restriction). CONFIRMED: row383/PROOF.md:17
  Gal(M/Q) ≃ W(D_105) and the §5 kernel argument
  (PROOF.md:160).
- T7 (Biasse–Fieker etc. scouted dead: GRH/heuristic status,
  |disc| ≈ 10^173 out of range). CONFIRMED AS LAB-INTERNAL
  scout verdict; nothing in the repo contradicts it, and
  EXP15 re-derived the same infeasibility scale from the
  generation side (2⁹⁴ range ≈ 3×10²⁶ prime ideals).

### Queue / log claims resting on repo state
- D2 (from T1): E12 queue entry and EXP15 log quote "181
  formal directions remain (row393)" and EXP15 §0 names
  (827, j=0) as the first remaining direction. CONFIRMED
  for row393 scope; SUPERSEDED as the live head by wave6:
  (827,0) is killed, residual is 175, zero count 636, head
  is P_(953,0) (unaudited record). EXP15's verdict is
  unaffected — the missing input is the generation
  certificate, and the waves explicitly do not supply it.
  E12 entry annotated in the ledger.
- D3: E4 queue entry framing ("the lift is a global
  Cassels–Tate condition, reduced by row385 to one class
  q★"). Already marked SUPERSEDED by EXP04 in the entry
  itself; EXP15 in turn superseded EXP04's step-(i) framing
  (δ★-first provably blocked at 2, row386; η-first route,
  row387). No new discrepancy; annotation pointer added so
  a reader does not stop at the EXP04 layer.
- D4: EXP15 (R3) "the recorded closure provably contains
  no η (Γ̄ ∩ ℋ_nr = {0}, extended through row393)".
  CONFIRMED through row393 (audits/row388.txt VERDICT=
  PASS_SCOPED_DEPENDENT_..._OLD_MULTIPLICATIVE_CLOSURE_
  HNR_ZERO_FORMAL_FB_RESIDUAL332; rows 389–393 audits
  PASS_SCOPED_DEPENDENT). CORRECTED IN SCOPE: EXP15's
  phrasing can be read as covering all recorded relations,
  but the waves added 4,619 independent principal relations
  AFTER row393, and no wave re-examines the ℋ_nr
  intersection for the enlarged closure (the waves work on
  the finite presentation's F₂ row space; they report no η
  and 0 exclusions, but that is not the row388 theorem).
  R3 must not be quoted beyond row393 data. EXP15's
  missing-input verdict does not depend on the enlarged
  closure, so the verdict stands.
- D5: EXP15 "generation proved only for norm < 2⁹⁴ (row393,
  de la Maza)". CONFIRMED and independently gated:
  publication/major-routes/ROW393-PRIMARY-THEOREM-GATE.md
  (2026-11-09) records D-1 PASS on the de la Maza Theorem 1
  application; classgroup-and-different/CLAIMS.json
  class_group_generation_certified=false.
- D6: EXP15 closing "LOW remains 9 absolute / 16 signed".
  CONFIRMED: audits/row383.txt and row384.txt both state
  LOW_UNCONDITIONAL_REMAINDER=9_ABSOLUTE_16_SIGNED;
  classgroup CLAIMS retained_low_absolute_indices=9,
  retained_low_signed_indices=16.

### Authority / governance
- A1 Lab assumption "authority V74 / Goal4AK". CONFIRMED:
  MAIN-STATE.json schema STAGE35_EX_PESCH_E1_STATE_V74_
  GOAL4AK_..., current unit 35EX-35_GOAL4AK..., status
  AUDITED_..._NO_E1_CREDIT; next leaf is GOAL4AL local-
  evaluation preflight (released, not computed) — an E1
  lane item, not a −30 item; nothing there changes any
  lab claim.
- A2 NEW MATERIAL never cited by the lab (beyond D1): the
  2026-11-12 continuation judgement (review-20261112/
  CONTINUATION-JUDGEMENT.md:120) says not to resume LOW
  slot work or −30 relation search without a restart
  condition, and does not cite the waves or PR #1861 —
  i.e. the repo's own later governance does not fold the
  resume delta back in. The waves (11-10) predate the
  judgement (11-12), so there is no contradiction, but
  the lab should treat the wave numbers as an unaudited,
  unadopted side record, exactly as their READMEs demand.
- A3 Minor nuance on the word "audited": row audit files
  exist for every row 370–393 (negative30-mw-selmer/
  audits/, classgroup-and-different/audits/), so the
  ledger's "(from repo, audited)" is accurate at that
  layer; but the publication layer still flags
  classgroup-and-different/CLAIMS.json
  row393_source_theorem_verification = PENDING (source-
  first verification of the row393 theorem in the
  migration corpus). Not a contradiction of any specific
  ledger claim; recorded so "audited" is not over-read.

### Subtrees checked, no bearing / no discrepancy
- materials/original-source-exclusions/ (rows 367–369,
  376): LOW source exclusions (±18; Ward 3/5/7 slots;
  +30 only, PASS_SCOPED_DEPENDENT) — consistent with the
  retained scoped results and with row381's audit note on
  +30. The lab's ground facts do not enumerate LOW slots,
  so nothing to correct.
- materials/selmer18-parent-chain/ (rows 361–364): the
  ±18 degree-36 parent Selmer certificates; its README
  explicitly does NOT transfer class-number-1 to the
  degree-105 −30 field. No bearing.
- materials/hcs-crosslane-c117-119/ (2026-11-09): C117–
  C119 HCS + R1/R4 lane archives, provisional, explicitly
  not adopted; states −30 / LOW / Branch B OPEN. No
  bearing on ledger claims.
- Formal row numbering stops at 393 in BOTH materials
  dirs (proofs row385–393; mw-selmer rows ≤ 384). No
  row394+ exists anywhere; the only post-393 mathematics
  in the repo is the D1 resume tree.
- publication/major-routes/ siblings (01, 02, 03, 05, 06)
  were listed; 04-minus30.md itself presents row393 as
  its endpoint and predates the resume (publication layer,
  2026-11-08) — consistent with A2.

## Tally
Claims checked: Ground facts 4, Tried 7, queue/log
repo-state claims 6 (D2–D6 + E4 framing), authority 1.
- CONFIRMED: G1, G2, G3, T2 (lab-internal), T3, T4, T5,
  T6, T7 (lab-internal), D5, D6, A1, plus the row393-scoped
  halves of T1/D2/D4 and all lab verdicts (T1 dead, EXP15
  missing input, no-credit posture).
- CORRECTED: 1 — D4 (R3 scope: row393 only, not the
  post-wave enlarged closure).
- SUPERSEDED: 3 — T1's numbers as current state (D1/D2:
  residual 181→175, zero 628→636, (827,0) killed, head
  now (953,0), unaudited); G4's obligation pair as
  current-state description (δ★ half executed →
  UNDETERMINED; ZF2 half still open); E12's "(827, j=0)
  first remaining direction" as the live head.
- NEW MATERIAL the lab had never incorporated: the
  2026-11-10 resume tree itself (waves 1–6, PR #1861)
  and the governance sequence around it (A2).

## What changes because of this audit
- No lab verdict changes: T1 stays dead, EXP15's missing
  input stays the blocker, the ≈3100× yardstick and the
  trap-B assessment are untouched, no queue item opens or
  closes.
- Three ledger entries annotated in place with dated
  pointers to this file (T1, Ground-facts row384, E12);
  original text preserved.
- Standing instruction for future lab text: quote 181/628/
  (827, j=0) only as "audited row393 endpoint"; the current
  recorded (unaudited) presentation state is 175/636 with
  head P_(953,0). Quote Γ̄ ∩ ℋ_nr = {0} only through
  row393.
