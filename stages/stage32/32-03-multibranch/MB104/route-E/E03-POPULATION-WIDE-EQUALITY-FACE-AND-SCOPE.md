# E03 — Population-wide form of E02, and the scope of E01/E02 over the GitHub frontier (2026-11-02)

Status: research note, **unaudited, zero credit**. It uses only E02 §1–§2, i.e. FSM facts (F1)–(F3) and the derived
Beauville chain, together with Lemma E01′.

## 1. Population-wide statement (no assumption on the class)

Notation, for an integral curve C̄ ⊂ B (any class):

- Ē is the normalization of C̄, of genus g;
- C̃ ⊂ S is the strict transform;
- d := K_B·C̄ = H·C̃;
- μ(C) := Σ_{p∈nodes} C̃·E_p is the total exceptional contact mass;
- M ≤ μ is the number of normalization points of Ē over ∪E_p;
- r ≤ M is the number of branch points of Y → Ē.

**Lemma E03.** If g ≤ 1, then:

1. r > 0, and r ≥ d − 4g + 4. This is (B4), with the case r = 0 excluded exactly as in E02 §3, an argument that does not depend on the class.
2. If r = d − 4g + 4, then d ≤ 85.
3. Hence, if d ≥ 86: **μ ≥ M ≥ r ≥ d − 4g + 5**.

*Proof.*

- (1) is E02 §2–§3. Those steps use only (F1)–(F3), never the class of C.
- For (2), on the equality face E02 §2(E),(S) gives a minimal étale correspondence Z ⊂ C8×C8 with legs of degree n = ed/8 and Z/Stab_G(Z) = Ē, where |Stab| = 2e.
  - Lemma E01′ needs n < 16·2e/3, i.e. ed/8 < 32e/3, i.e. d < 256/3, i.e. d ≤ 85.
  - Equivalently, Area(Ē) = πd < 256π/3.
- (3) follows from (1) and (2). □

**Corollary E03.1 (counting exclusion).** No curve of geometric genus ≤ 1 lies in a class with

μ ≤ d − 4g + 4 and d ≥ 86,

or with μ < d − 4g + 4 (any d). For genus 1 this reads: μ ≤ d and d ≥ 86, or μ < d. For genus 0: μ ≤ d + 4 and d ≥ 86, or μ < d + 4.

**Corollary E03.2 (E02 recovered).** For the uniform class 7lH − 4lΣ_{14}E_p we have μ = 14·8l = 112l = d ≥ 112. So the class is excluded for every l ≥ 1.

**What E03 does not do.** Classes with μ > d − 4g + 4 remain open: there the legs may ramify, and E01′ does not apply. Small degrees d ≤ 85 on the exact equality face also remain open.

## 2. Scope over the GitHub frontier (STATE `retained_frontier`)

Which retained records concern carriers in |lP| = |7lH − 4lΣ_{000707}E_p|, the class that E02 covers?

| Record (`retained_frontier`) | Carrier | Covered by E02? |
|---|---|---|
| `pair_map` (route A, r = 1..4, "864") | "integral MB carrier in \|lP\| with elliptic normalization" (restriction note, blob `18617398`) | yes |
| `r4`, `genus7_fibration`, `isotropic_shell_preflight` | auxiliary to the \|lP\| pair map | yes (as far as they serve that carrier) |
| `rank3_fourmap_b3_quotient`, `support_hyperplane_subcanonical_bridge` | C = lP, support 000707 | yes |
| `b3_*`, `absent_eta_character_line`, `anti_invariant_conductor_source_wall` (route B) | the same carrier (b3 quotient of lP) | yes |
| `e2_*` (6 records), `parking_reopen_contract`, `compact_C8_etale_correspondence_preflight`, `conductor_pair_low_degree_pushforward_preflight` | support 000707, e = 2 | yes |
| `cycle_breadth_audit_20260920` | lP | yes |
| `z12_*`, `projective_ci_*`, `normalization_module_*`, `elliptic_linear_series_*`, `null_union_*`, `equigeneric_*` | method walls for the same carrier | yes, as far as they concern it |

The column "Covered by E02?" means: if E01/E02 survive audit, the hypothetical carrier these records study does not
exist. The records then become moot; they are not individually refuted.

The "864" in `pair_map` is a count of balanced supports. E02 holds for every 14-node support with uniform coefficients
(7l, 4l), so any such support is covered. Whether all 864 have exactly that uniform shape must be checked against
the pair-map source before it is stated as fact.

The frozen Drive routes C and D (F35–F82) were written for the same 000707 carrier. Their status follows the same rule, but
is recorded here only as an expectation, not as a check.

## 3. What remains of MB104 after E01–E03 (if audited)

MB104's mission is a "population-wide finite degree/intersection restriction" (MISSION.json). After E01–E03:

- **Excluded:**
  - the uniform 14-node class |lP| (support 000707 and any other 14-node support), for all l;
  - every class with μ < d − 4g + 4;
  - every class with μ ≤ d − 4g + 4 and d ≥ 86.
- **Remaining:**
  - genus-≤1 curves with μ ≥ d − 4g + 5 (strictly off the equality face);
  - the equality face for d ≤ 85.

  E03 gives the population-wide restriction r ≥ d − 4g + 5 for d ≥ 86. This is a necessary condition, not a finite window.
- To obtain a finite window, the off-face case needs a new idea. For example, a ramified version of E01′ (an orbifold or Belyi-type uniformization of Z → C8 with controlled ramification R = 2e(r − d + 4g − 4)) or a bound on μ − d.

## 4. Audit points

1. Lemma E03 (1)–(3): check that E02 §2–§3 uses no class-specific input. The only class-specific step in E02 is the count μ = d.
2. Corollaries E03.1 and E03.2: arithmetic.
3. The scope table: check each record's carrier against its source blob.
4. No credit, frontier change or MB104 closure is claimed.
