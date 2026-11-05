# E03 — Population-wide form of E02, and the scope of E01/E02 over the GitHub frontier (2026-11-02)

Status: research note, **zero credit**. Audits:

- round 1, DeepSeek (reading): PASS;
- round 2, Claude (executing): FAIL, for one must-fix. The must-fix was the missing hypothesis "C̄ ⊂ B, d ≥ 1" (the exceptional curves E_p are counterexamples to the old wording). Revision 2 fixes it.
- round 3, independent hostile reading audit (2026-11-06): PASS for E03 (1) with the standing hypothesis (re-audit of the round-2 fix). Scope: E03 (1) only, see §5.

E03 uses only:

- E02 §1–§2, i.e. the FSM facts (F1)–(F3) and the derived Beauville chain;
- Lemma E01′.

## 1. Population-wide statement

"Population-wide" here means independent of the class of the curve. It does **not** mean independent of E01′, i.e. of the compact X(8) uniformization and the congruence propagation in E01 §2a, or of the FSM facts (F1)–(F3).

**Standing hypothesis.** C̄ ⊂ B is an integral curve on the box variety. Equivalently, C̃ ⊂ S is an integral curve that is **not** one of the 48 exceptional curves E_p. Then d := K_B·C̄ = H·C̃ ≥ 1. (Each E_p has H·E_p = 0 and is a rational curve; it is not covered, and the old wording without this hypothesis was false for E_p.)

Notation:

- Ē is the normalization, of genus g;
- μ(C) := Σ_p C̃·E_p is the total exceptional contact mass;
- M ≤ μ is the number of normalization points of Ē over ∪E_p;
- r ≤ M is the number of branch points of Y → Ē. By (B1), r is even.

**Lemma E03.** Under the standing hypothesis, if g ≤ 1, then:

1. r > 0 and r ≥ d − 4g + 4 (this is (B4); r = 0 is excluded as in E02 §3);
2. if r = d − 4g + 4, then d ≤ 85, and for g = 0 even d ≤ 42;
3. hence, if d ≥ 86: **μ ≥ M ≥ r ≥ d − 4g + 5**, and in fact r ≥ d − 4g + 6 when d is even, because r is even.

*Proof.*

- (1) is E02 §2–§3. Those steps use only (F1)–(F3) and g ≤ 1, never the class.
- (2) On the equality face, E02 §2(E),(S) gives a minimal étale correspondence Z with legs of degree n = ed/8 and Z/Stab_G(Z) = Ē, where |Stab| = 2e. Stab acts faithfully on Z: a nontrivial diagonal element of G has only finitely many fixed points on C8×C8, so it cannot fix the curve Z pointwise.
  - Then Area(Ē) = πd. Lemma E01′ (g ≤ 1, Zograf with g + 1 ≤ 2) gives πd < 256π/3, so d ≤ 85.
  - For g = 0, the same Zograf bound with g + 1 = 1 gives πd < 128π/3, so d ≤ 42.
- (3) follows from (1) and (2), using the parity of r. □

Also: if d is odd, r = d − 4g + 4 is odd, so the equality face is empty for odd d.

**Corollary E03.1.** Let C̄ ⊂ B satisfy the standing hypothesis, and let g ≤ 1. Then C̄ cannot satisfy

μ < d − 4g + 4, or μ = d − 4g + 4 with d ≥ 86 (d ≥ 43 if g = 0).

In words: a class (in Pic S, not an exceptional class) contains no integral curve of geometric genus g ≤ 1 with these values of μ and d.

**Corollary E03.2.** For the uniform class 7lH − 4lΣ_{14}E_p we have μ = 112l = d ≥ 112. So no integral curve of geometric genus ≤ 1 lies in it, for every l ≥ 1. This recovers E02.

## 2. Scope over the GitHub frontier (STATE `retained_frontier`)

Round 2 (Claude, executing) read the carrier of **all 27 retained records**. Each record either concerns the |lP| carrier (H·P = 112, P² = 336, δ = 168l² + 56l) or is auxiliary to it through P. Examples of the auxiliary kind are `genus7_fibration` and `isotropic_shell_preflight`, which are about P·F for a fibre class F. No record treats a different carrier.

| Record (`retained_frontier`) | Carrier | Covered by E01/E02 |
|---|---|---|
| `pair_map` (route A, r = 1..4, "864") | \|lP\|, elliptic normalization (restriction note, blob `18617398`) | yes |
| `r4`, `genus7_fibration`, `isotropic_shell_preflight` | auxiliary to \|lP\| through P | yes |
| `rank3_fourmap_b3_quotient`, `support_hyperplane_subcanonical_bridge`, `cycle_breadth_audit_20260920` | C = lP, support 000707 | yes |
| `b3_*`, `absent_eta_character_line`, `anti_invariant_conductor_source_wall` (route B) | b3 quotient of the lP carrier | yes |
| `e2_*` (6 records), `parking_reopen_contract`, `conductor_pair_low_degree_pushforward_preflight` | support 000707, e = 2 | yes |
| `compact_C8_etale_correspondence_preflight` | G-stable Z, legs 56l, Z/G = E, i.e. **e = 4** | yes (E01′ with \|A\| = 8: 56l < 128/3 fails) |
| `z12_*`, `projective_ci_*`, `normalization_module_*`, `elliptic_linear_series_*`, `null_union_*`, `equigeneric_*` | method walls for the same carrier | yes |

"Covered" means: if the hypothetical carrier these records study does not exist (E02), the records become moot. They are not individually refuted.

**The 864 supports**

- They decompose into three orbits, all of the uniform 14-node shape P = 7H − 4ΣE_i, |Σ| = 14:

  | Orbit | Count |
  |---|---|
  | `0000770000ff` | 48 |
  | `00007b0000ff` | 48 |
  | `000707000f0f` | 768 |
  | **Total** | **864** |

- Sources: Z3 notes on commit `d13afbb1` (blobs `dca4eeca`, `30885461`) and the pair-map discriminant note (blob `0e1f7d60`).
- The fourth orbit `00070b000f0f`, already excluded by Z33G, has the same shape.
- E02 holds for every 14-node support, so it covers all 864 class by class.

The frozen Drive routes C and D (F35–F82) were written for the same 000707 carrier. This is recorded as an expectation only.

## 3. What remains of MB104 after E01–E03

MB104's mission is a "population-wide finite degree/intersection restriction" (MISSION.json). All statements below concern integral curves on B (non-exceptional on S) of geometric genus g ≤ 1.

- **Excluded:**
  - every curve in a uniform 14-node class 7lH − 4lΣE_p, for all l. This includes all 864 supports.
  - every curve with μ < d − 4g + 4;
  - every curve with μ = d − 4g + 4 and d ≥ 86 (d ≥ 43 if g = 0);
  - every curve on the equality face with d odd.
- **Remaining (the off-face condition is a condition on r, not on μ):**
  - curves with μ ≥ d − 4g + 5. Among these, r ≥ d − 4g + 5 is forced when d ≥ 86. For d ≤ 85, the equality face r = d − 4g + 4 is still possible.
  - curves with μ = d − 4g + 4 and d ≤ 85 (d ≤ 42 if g = 0), with d even.
- This is a necessary condition, not a finite window. A finite window needs a new idea for the off-face case. For example, a ramified version of E01′ with controlled leg ramification R = 2e(r − d + 4g − 4), or a bound on μ − d.

## 4. Audit points

1. Lemma E03 (1)–(3): E02 §2–§3 uses no class-specific input. The standing hypothesis is now explicit.
2. Corollaries E03.1 and E03.2, and the g = 0 and parity refinements.
3. Scope table and the 864 breakdown, against the cited blobs.
4. No credit, frontier change or MB104 closure is claimed.

## 5. Audit history

- **Round 1: DeepSeek (reading), PASS at `51b57aac`. No must-fix.** Should-fix items:
  1. The scope column was an expectation. Now superseded: round 2 read all 27 records.
  2. "Population-wide" is relative to E01′ → §1.
  3. Scripts were not re-executed at this head → noted.
- **Round 2: Claude (executing), FAIL at `51b57aac`. One must-fix.**
  - Ran e02_counts.py, bolza_mod2.py and c8_net.py with and without `-O`: exit 0, with hashes matching STATE.
  - Independently re-derived:
    - E01′;
    - E02 §2 (a), (b), (B1), (B2), (B4), (E) and (S);
    - the r = 0 argument;
    - E03 (1)–(3);
    - known FSM curves: boundary elliptic curves (d = 4, r = 8), Prop 2.9 (d = 4, r = 4, on the face), Prop 2.6 rational curves (d = 2, e = 4, r = 6 = d + 4, on the face).
  - Must-fix: the E_p (d = 0, μ = −2, genus 0) contradicted the old Corollary E03.1. → Fixed by the standing hypothesis in §1.
  - Should-fix items:
    1. STATE audit statuses vs content → STATE updated: E01 §2a and E02 revision 3 are now covered by rounds after their PASS, and are recorded as such.
    2. The "remaining" set confused μ and r → §3 rewritten.
    3. "class with μ < …" phrasing → Corollary E03.1 reworded.
    4. `compact_C8_*` is e = 4 → moved in the table.
    5. The 864 breakdown → added as fact, with sources.
    6. Faithfulness of Stab on Z → stated in Lemma E03 (2), and in E02 (S).
    7. Optional refinements (parity of r; d ≤ 42 for g = 0) → added.
- **Round 3: independent hostile reading audit, PASS (2026-11-06), on revision 2 (sha256 `ad217d3e…`, unchanged).**
  - Read through the Stage 32-02 audit package R2, Appendix K. That appendix reproduces E03 (1) with its full
    proof and the standing hypothesis "C̃ integral, not an E_p (C̄ ⊂ B, d ≥ 1)". The package is kept locally, outside this repository.
  - Verdict: the round-2 must-fix is fixed. r > 0, r even and r ≥ d − 4g + 4 are correct. This is the E02 §2–§3
    argument plus the standing hypothesis.
  - Also accepted: the d = 16 corollary built on it (with E02 (B1) and E04): μ < 18 excludes every integral curve with g ≤ 1. This is the d = 16 case of the E05 μ filter.
  - Scope: reading only, no scripts executed in this round. E03 (2), (3), the corollaries and the scope table were not re-read in this round.
    They keep their round-1 PASS (DeepSeek) and the round-2 re-derivation (Claude, executing).
  - No must-fix. No credit change.
