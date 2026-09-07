#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INDEX = ROOT / "docs/arsenal/index.json"
SOURCE = "../stage36-literature-strengthening-promotion.md"
DISCOVERY_PR = 1690
DISCOVERY_HEAD = "f1a2d3074e802b0fd4555cb827e165c3de2bdfc9"
ARSENAL_BASE_MAIN = "386b6a52d7bfec2e8903412c7ca56976b46c288b"
IMPLEMENTATION_PR = 1692
IMPLEMENTATION_BASE_MAIN = "e758e05953df2cf8cd4ab26ac1e9d72374e99760"
STAGE36_SOURCE_HEAD = "2fc3f4b8afb28bb23765bd861cbd7c52aafd6563"
HARVEST_HEAD = "07a465cb5025e7c0188fb63610bb40e4b54e7a84"


def lit(authors, title, venue, year, doi, url, theorem, source_type, conditional="none beyond stated theorem hypotheses"):
    return {
        "authors": authors,
        "title": title,
        "journal_or_publisher": venue,
        "year": year,
        "doi": doi,
        "canonical_url": url,
        "theorem_identifier": theorem,
        "source_type": source_type,
        "conditional_assumptions": conditional,
    }


def repo(pr, head, path, blob, verifier, verifier_blob, adapter):
    return {
        "stage36_source_pr": pr,
        "stage36_source_exact_head": head,
        "source_or_certificate_path": path,
        "source_or_certificate_blob_sha": blob,
        "verifier_path": verifier,
        "verifier_blob_sha": verifier_blob,
        "repo_adapter_contract": adapter,
    }


def main():
    data = json.loads(INDEX.read_text())
    assert data["schema"] == "RESEARCH_ARSENAL_V12_LITERATURE_PROVISIONAL"
    assert not any(r.get("path") == SOURCE for r in data.get("support_records", []))
    assert "stage36_literature_strengthening" not in data
    assert not any(h.get("source_stage") == "Stage36 Literature Strengthening" for h in data.get("provisional_harvests", []))

    data["support_records"].append({
        "path": SOURCE,
        "class": "PROVISIONAL",
        "role": "Stage36 Phase4 literature-backed strengthening provenance; discovery freeze #1690 remains the implementation boundary and Stage36 mathematical authority is unchanged",
    })

    extension_rows = [
        ("S36-PW02", "S36-PW02", "S36_PW02_KANI_ROSEN_THEOREM_LOCK"),
        ("S36-PW03", "S36-PW03", "S36_PW03_TWIST_EIGENSPACE_RANK_JUMP_APPLICABILITY_EXTENSION"),
        ("S36-PW04", "S36-PW04", "S36_PW04_GLOBAL_TORSOR_CLASS_HANDOFF"),
        ("S36-PW06", "S36-PW06", "S36_PW06_GUSIC_TADIC_SPECIALIZATION_THEOREM_LOCK"),
        ("S36-PW07", "S36-PW07", "S36_PW07_GLOBAL_RECIPROCITY_HANDOFF"),
        ("S30-W01", "DISC-S36-B01", "STAGE36_LITERATURE_QUADRATIC_MODULE_COMPRESSION_EXTENSION"),
        ("S31-W01", "DISC-S36-B08", "STAGE36_LITERATURE_SUCCESSIVE_COVER_GENUS_PREFLIGHT_EXTENSION"),
        ("S34-W02", "DISC-S36-B12", "STAGE36_LITERATURE_SPECIALIZATION_GROWTH_APPLICABILITY_EXTENSION"),
    ]
    existing_ext_keys = {(e.get("target_id"), e.get("source_stage"), e.get("role")) for e in data.get("provisional_extensions", [])}
    for target, candidate, role in extension_rows:
        key = (target, "Stage36 Literature Strengthening", role)
        assert key not in existing_ext_keys
        data["provisional_extensions"].append({
            "target_id": target,
            "source_stage": "Stage36 Literature Strengthening",
            "source_candidate": candidate,
            "path": SOURCE,
            "maturity": "PROVISIONAL",
            "role": role,
        })

    data["provisional_harvests"].append({
        "source_stage": "Stage36 Literature Strengthening",
        "path": SOURCE,
        "source_pr": IMPLEMENTATION_PR,
        "source_branch": "arsenal-stage36-literature-strengthening-implementation",
        "discovery_pr": DISCOVERY_PR,
        "discovery_exact_head": DISCOVERY_HEAD,
        "arsenal_base_main": ARSENAL_BASE_MAIN,
        "implementation_base_main": IMPLEMENTATION_BASE_MAIN,
        "stage36_arsenal_source_head": STAGE36_SOURCE_HEAD,
        "harvest_snapshot_head": HARVEST_HEAD,
        "promotion_status": "PROVISIONAL_STAGE36_LITERATURE_IMPLEMENTATION_PENDING_HOSTILE_AUDIT",
        "active_cards": [],
        "retired_merged_ids": {},
        "card_roles": {},
        "card_summaries": {},
        "active_workflows": ["LIT-WF02"],
        "workflow_roles": {"LIT-WF02": "GLOBAL_H1_LOCALIZATION_RECIPROCITY_APPLICABILITY_WORKFLOW"},
        "workflow_summaries": {
            "LIT-WF02": "Fail-closed applicability audit from repo local rows/charts to one fixed global H1/Kummer system with exact localization, place normalization and theorem-input binding; constructs no missing global class and grants no mathematical credit."
        },
        "provisional_card_count": 0,
        "provisional_workflow_count": 1,
        "provisional_active_entry_count": 1,
        "routeable_for_candidate_discovery": True,
        "formal_selector": False,
        "repo_theorem_credit": False,
        "external_literature_theorem_provenance": True,
        "hostile_audit_required_before_formal_treatment": True,
        "stage36_mathematical_credit_added": False,
    })

    kani = lit("Ernst Kani; Michael Rosen", "Idempotent relations and factors of Jacobians", "Mathematische Annalen 284, 307-328", 1989, "10.1007/BF01442878", "https://doi.org/10.1007/BF01442878", "Theorem B", "original peer-reviewed paper")
    gusic = lit("Ivica Gusic; Petra Tadic", "A remark on the injectivity of the specialization homomorphism", "Glasnik Matematicki 47, 265-275", 2012, "10.3336/gm.47.2.03", "https://doi.org/10.3336/gm.47.2.03", "Theorem 1.1", "original peer-reviewed paper")
    kellock = lit("Lilybelle Cowland Kellock; Vladimir Dokchitser", "Root numbers and parity phenomena", "Bulletin of the London Mathematical Society 55, 2557-2597", 2023, "10.1112/blms.12931", "https://doi.org/10.1112/blms.12931", "Lemma 2.9", "original peer-reviewed paper")
    silverman = lit("Joseph H. Silverman", "Heights and the specialization map for families of abelian varieties", "Journal fur die reine und angewandte Mathematik 342, 197-211", 1983, "10.1515/crll.1983.342.197", "https://doi.org/10.1515/crll.1983.342.197", "Theorem C", "original peer-reviewed paper")
    loughran = lit("Daniel Loughran; Cecilia Salgado", "Rank jumps on elliptic surfaces and the Hilbert property", "Annales de l'Institut Fourier 72, 617-638", 2022, "10.5802/aif.3457", "https://doi.org/10.5802/aif.3457", "Theorems 1.1 and 1.2", "original peer-reviewed paper", "inactive until the exact Stage36 family satisfies the selected theorem hypotheses")
    sch95 = lit("Edward F. Schaefer", "2-Descent on the Jacobians of Hyperelliptic Curves", "Journal of Number Theory 51, 219-232", 1995, "10.1006/jnth.1995.1044", "https://doi.org/10.1006/jnth.1995.1044", "paper-level explicit 2-descent framework; exact selected internal locator not frozen by Phase3", "original peer-reviewed paper", "no theorem-output credit until an exact global class and selected locator are bound")
    sch98 = lit("Edward F. Schaefer", "Computing a Selmer group of a Jacobian using functions on the curve", "Mathematische Annalen 310, 447-471", 1998, "10.1007/s002080050156", "https://doi.org/10.1007/s002080050156", "paper-level function-to-Selmer framework; exact selected internal locator not frozen by Phase3", "original peer-reviewed paper", "no theorem-output credit until an exact global class and selected locator are bound")
    cfoss = lit("J. E. Cremona; T. A. Fisher; C. O'Neil; D. Simon; M. Stoll", "Explicit n-descent on elliptic curves, II. Geometry", "Journal fur die reine und angewandte Mathematik 632, 63-84", 2009, "10.1515/CRELLE.2009.050", "https://doi.org/10.1515/CRELLE.2009.050", "explicit n-covering geometry; exact selected theorem/algorithm not frozen in LIT-PW03", "original peer-reviewed paper", "routes only after the repo branch is proved to represent the named global covering class")
    serre = lit("Jean-Pierre Serre", "A Course in Arithmetic", "Springer, Graduate Texts in Mathematics 7", 1973, "10.1007/978-1-4684-9884-4", "https://doi.org/10.1007/978-1-4684-9884-4", "Chapter III Theorems 2-4", "authoritative monograph")
    milne = lit("J. S. Milne", "Arithmetic Duality Theorems", "2nd edition, author edition/BookSurge", 2006, None, "https://www.jmilne.org/math/Books/ADTnot.pdf", "Theorem I.4.10", "authoritative monograph", "Poitou-Tate use requires a genuine fixed global finite module and exact local conditions")
    pardini = lit("Rita Pardini", "Abelian covers of algebraic varieties", "Journal fur die reine und angewandte Mathematik 417, 191-214", 1991, "10.1515/crll.1991.417.191", "https://doi.org/10.1515/crll.1991.417.191", "Theorem 2.1", "original peer-reviewed paper")
    arf = lit("Cahit Arf", "Untersuchungen uber quadratische Formen in Korpern der Charakteristik 2. I", "Journal fur die reine und angewandte Mathematik 183, 148-167", 1941, "10.1515/crll.1941.183.148", "https://doi.org/10.1515/crll.1941.183.148", "structural Arf-invariant classification source; exact internal locator not promoted beyond Phase3", "original peer-reviewed paper")
    taylor = lit("Donald E. Taylor", "The Geometry of the Classical Groups", "Heldermann Verlag, Sigma Series in Pure Mathematics 9", 1992, None, None, "Theorem 8.5", "authoritative monograph", "transvection result is duplicate-routed to S32-PW06; it does not identify Stage36 source-labelled orbits")
    stoll = lit("Michael Stoll", "Descent on elliptic curves", "Panoramas et Syntheses 36, 151-179", 2012, None, "https://arxiv.org/abs/math/0611694", "standard Kummer/Selmer descent framework; no new theorem locator promoted for S36-PW05", "authoritative survey / published chapter")

    accepted = {
        "S36-PW02": {
            "classification": "LITERATURE_DIRECT",
            "proposed_role": "V4_CURVE_JACOBIAN_QUOTIENT_DECOMPOSITION_LITERATURE_LOCK",
            "literature": [kani],
            "theorem_hypotheses_summary": "smooth curve; exact V4 action/maps over stated field; quotient/full-group genera and Kani-Rosen relation exact",
            "conclusion_summary": "theorem-locked Jacobian isogeny decomposition only; no rational-point converse",
            "repo": repo(1642, "be979251c6e3d7a2431fb56537520afd2596c7d9", "stages/stage36/36-09O/physical-square-lift-v4-quotient-preflight.json", "6a2678ebedba40e13277100441361039ee47ca28", "stages/stage36/verify_stage36_36_09O.py", "ed0ae786505e3443226eaed6e61b7c78ee389191", "exact maps/genus/full-quotient/differential checks -> Kani-Rosen Theorem B"),
            "strength_delta": "exact theorem lock; mathematical output unchanged",
            "maturity_recommendation": "PROVISIONAL_LITERATURE_DIRECT",
        },
        "S36-PW03": {
            "classification": "EXTEND_STAGE36_EXISTING",
            "proposed_role": "TWIST_EIGENSPACE_AND_RANK_JUMP_APPLICABILITY_EXTENSION",
            "literature": [kellock, silverman, loughran],
            "theorem_hypotheses_summary": "explicit quadratic twist/eigenspaces; rank-jump theorem only after exact elliptic-surface family hypotheses pass",
            "conclusion_summary": "standard twist rank decomposition plus fail-closed optional rank-jump context; no receiver implication",
            "repo": repo(1664, "25229e7b0dfbbc5524266ce49e8edaf217841701", "stages/stage36/36-09U/qi-antiinvariant-rankjump-descent-preflight.json", "a1f0c924d267ab4f45aaada6c9bcb3a5f544f284", "stages/stage36/verify_stage36_36_09U.py", "21b3b1461195cfae1a1294832f8e77f09a09983b", "STAGE36_FAMILY_TO_RANK_JUMP_THEOREM_HYPOTHESES (missing for Loughran-Salgado use)"),
            "strength_delta": "theorem provenance and applicability/failure contract only",
            "maturity_recommendation": "PROVISIONAL_EXTENSION_BLOCKED_FOR_RANK_JUMP_THEOREM_UNTIL_HYPOTHESES_MATCH",
        },
        "S36-PW04": {
            "classification": "LITERATURE_ADAPTED",
            "proposed_role": "POINTWISE_CHART_TO_GLOBAL_TORSOR_CLASS_HANDOFF",
            "literature": [sch95, sch98, cfoss],
            "theorem_hypotheses_summary": "actual named global H1/Kummer covering class and exact localization maps required; pointwise chart tuples alone are insufficient",
            "conclusion_summary": "typed handoff to existing LIT-PW03 only after global-class adapter; no Selmer/rational-point credit now",
            "repo": repo(1560, "dcdae282120f29a42679b654e21bd35f843e4cbf", "stages/stage36/36-04/h-torsor-lift-class.json", "a06e201a9b554da71c5e75d8f8541e7284f8d020", "stages/stage36/verify_stage36_36_04.py", "35d288d8a18adee95830caa6ee9d6b0d8ebe9e53", "POINTWISE_CHART_TUPLE_TO_GLOBAL_KUMMER_OR_TORSOR_CLASS (missing; fail closed)"),
            "strength_delta": "cohomological handoff semantics only after missing adapter",
            "maturity_recommendation": "PROVISIONAL_ADAPTED_BLOCKED_BY_GLOBAL_CLASS_ADAPTER",
        },
        "S36-PW06": {
            "classification": "LITERATURE_DIRECT",
            "proposed_role": "RELATIVE_2ISOGENY_KUMMER_SPECIALIZATION_BASELINE_EXACT_THEOREM_LOCK",
            "literature": [gusic],
            "theorem_hypotheses_summary": "nonconstant split-full-2 E/Q(t), good t0, every required nonconstant square-free divisor evaluates nonsquare",
            "conclusion_summary": "injective specialization; repo q0=6 replay plus fixed-fiber descent and visible sections yields the existing generic rank/Kummer baseline",
            "repo": repo(1640, "8ca23e42a057af260c7051c20dd8f608067efefd", "stages/stage36/36-09N/relative-2isogeny-kummer-image-rank1-preflight.json", "02a14439d94d7f6e5ac2f65e995e8acfb6845788", "stages/stage36/verify_stage36_36_09N.py", "e7effbe9ee6106505db013f326ec653627885054", "q0=6 divisor criterion replay + fixed-fiber 2-isogeny descent + visible section/torsion/Kummer synthesis"),
            "strength_delta": "exact theorem lock; no full-MW upgrade",
            "maturity_recommendation": "PROVISIONAL_LITERATURE_DIRECT",
        },
        "S36-PW07": {
            "classification": "LITERATURE_ADAPTED",
            "proposed_role": "LOCAL_CHARACTER_MATRIX_TO_GLOBAL_RECIPROCITY_HANDOFF",
            "literature": [serre, milne],
            "theorem_hypotheses_summary": "one fixed global squareclass/finite module, exact localizations, complete relevant-place panel including 2 and infinity",
            "conclusion_summary": "global compatibility/orthogonality only after global-localization adapter; reciprocity is not automatically a contradiction",
            "repo": repo(1664, "25229e7b0dfbbc5524266ce49e8edaf217841701", "stages/stage36/36-09Y/kummer-complement-prime-2adic-hilbert-preflight.json", "20c6d782e59bff820392731ec81653d15b2d1921", "stages/stage36/verify_stage36_36_09Y.py", "63b4cc43e91c18a8ff295b288995e23395de8539", "DYNAMIC_RESERVOIR_ROWS_TO_GLOBAL_KUMMER_LOCALIZATION_SYSTEM (missing; fail closed)"),
            "strength_delta": "potential local-to-global handoff; LOCAL_GLOBAL_OBSTRUCTION_INCREMENT remains zero",
            "maturity_recommendation": "PROVISIONAL_ADAPTED_BLOCKED_BY_GLOBAL_LOCALIZATION_ADAPTER",
        },
        "DISC-S36-B01->S30-W01": {
            "classification": "EXTEND_OLDER_EXISTING",
            "proposed_role": "FIELD_SEPARATED_QUADRATIC_MODULE_INVARIANT_COMPRESSION_EXTENSION",
            "literature": [arf, taylor],
            "theorem_hypotheses_summary": "exact F2 quadratic/bilinear module and radical; actual source acting subgroup must be identified before structural orbit compression",
            "conclusion_summary": "structural invariant compression only where source subgroup realizes theorem equivalence; no transvection duplication",
            "repo": repo(1541, "3a78f9ff156b53f509625d353df48d1b3e02b836", "stages/stage36/36-02/representative-inventory.json", "88130b9380a677a191f91c24df87618e65be0a2f", "stages/stage36/verify_stage36_36_02_audited.py", "97dd2e3834365e8b013f9ff076b1b05595362aee", "source-labelled kernel/action -> radical/nondegenerate quotient/Arf-Witt invariants with base/extension orbit separation"),
            "strength_delta": "older-card structural compression vocabulary; no new ID",
            "maturity_recommendation": "PROVISIONAL_DELTA",
        },
        "DISC-S36-B08->S31-W01": {
            "classification": "EXTEND_OLDER_EXISTING",
            "proposed_role": "SUCCESSIVE_COVER_GENUS_PREFLIGHT_LITERATURE_EXTENSION",
            "literature": [pardini],
            "theorem_hypotheses_summary": "exact successive double-cover branch divisors, smooth generic layers, branch-collision/degenerate strata separated",
            "conclusion_summary": "generic genus/degeneration preflight then route genus-one layer to existing S31-W01; no point classification",
            "repo": repo(1624, "6ede28751914a881a5ddaca7691538a8a3e4780c", "stages/stage36/36-09J/reciprocal-involution-two-linear-cover-preflight.json", "72e9ca86f726f2ff286c983138d9381acdd97e62", "stages/stage36/verify_stage36_36_09J.py", "b5357a344ffab51118f4f1ec92904367c79c6541", "successive cover branch/discriminant data -> genus/degeneration preflight -> S31-W01 routing"),
            "strength_delta": "older-card applicability preflight; no new ID",
            "maturity_recommendation": "PROVISIONAL_DELTA",
        },
        "DISC-S36-B12->S34-W02": {
            "classification": "EXTEND_OLDER_EXISTING",
            "proposed_role": "GENERIC_SUBGROUP_SPECIALIZATION_GROWTH_APPLICABILITY_EXTENSION",
            "literature": [silverman, loughran],
            "theorem_hypotheses_summary": "generic subgroup/torsion certified; receiver adapter exact; growth species separated; Loughran-Salgado only after exact family hypotheses pass",
            "conclusion_summary": "receiver-compatible specialization must lie outside tested generic subgroup via rank/index/torsion enlargement; no empty growth-locus claim",
            "repo": repo(1655, "f48184e2ab7fabe6fd07b553aa1cda507874569d", "stages/stage36/36-09R/etau-rankjump-receiver-esigmatau-growth-preflight.json", "b55d042ede01032ff8c8b0d872510a53cb857969", "stages/stage36/verify_stage36_36_09R.py", "62707dc5126e9ea6caad5fd41834cab488b29945", "generic subgroup receiver test -> typed rank/saturation/torsion growth obligation; theorem context only after hypothesis adapter"),
            "strength_delta": "older-card family-specialization preflight; no closure",
            "maturity_recommendation": "PROVISIONAL_DELTA",
        },
    }

    data["stage36_literature_strengthening"] = {
        "status": "PROVISIONAL_IMPLEMENTATION_PENDING_HOSTILE_AUDIT",
        "literature_delta_stage": "Stage36",
        "literature_audit_pr": DISCOVERY_PR,
        "literature_audit_exact_head": DISCOVERY_HEAD,
        "arsenal_base_main": ARSENAL_BASE_MAIN,
        "implementation_pr": IMPLEMENTATION_PR,
        "implementation_branch": "arsenal-stage36-literature-strengthening-implementation",
        "implementation_base_main": IMPLEMENTATION_BASE_MAIN,
        "stage36_arsenal_source_head": STAGE36_SOURCE_HEAD,
        "stage36_harvest_snapshot_head": HARVEST_HEAD,
        "stage36_delta_only": True,
        "phase3_manifest_frozen": True,
        "literature_population_expanded": False,
        "hostile_audit_required_before_formal_treatment": True,
        "authority_order": ["active Stage36 authority", "existing formal Arsenal", "Stage36 provisional Arsenal", "Stage36 literature-backed provisional extension"],
        "credit_firewall": {
            "LITERATURE_ARSENAL_REGISTRATION_DOES_NOT_CHANGE_STAGE36_MATHEMATICAL_AUTHORITY": True,
            "STAGE36_PROGRESS_INCREMENT": 0,
            "STAGE36_THEOREM_CREDIT_INCREMENT": 0,
            "RECEIVER_CLOSURE_INCREMENT": 0,
            "MW_CLOSURE_INCREMENT": 0,
            "LOCAL_GLOBAL_OBSTRUCTION_INCREMENT": 0,
            "ENDPOINT_CREDIT_INCREMENT": 0,
            "PERFECT_CUBOID_EXISTENCE_CLAIM": False,
            "PERFECT_CUBOID_NONEXISTENCE_CLAIM": False,
            "NOVEL": False,
            "FIRST_PROOF": False,
            "NEW_THEOREM": False,
        },
        "implementation_manifest": {
            "stage36_card_extensions": [
                {"candidate_id": "S36-PW02", "target_card": "S36-PW02", "class": "LITERATURE_DIRECT"},
                {"candidate_id": "S36-PW03", "target_card": "S36-PW03", "class": "EXTEND_STAGE36_EXISTING"},
                {"candidate_id": "S36-PW04", "target_card": "S36-PW04", "class": "LITERATURE_ADAPTED"},
                {"candidate_id": "S36-PW06", "target_card": "S36-PW06", "class": "LITERATURE_DIRECT"},
                {"candidate_id": "S36-PW07", "target_card": "S36-PW07", "class": "LITERATURE_ADAPTED"},
            ],
            "older_card_extensions": [
                {"candidate_id": "DISC-S36-B01", "target_card": "S30-W01", "class": "EXTEND_OLDER_EXISTING"},
                {"candidate_id": "DISC-S36-B08", "target_card": "S31-W01", "class": "EXTEND_OLDER_EXISTING"},
                {"candidate_id": "DISC-S36-B12", "target_card": "S34-W02", "class": "EXTEND_OLDER_EXISTING"},
            ],
            "new_literature_weapons": [],
            "new_literature_workflows": [
                {"candidate_id": "GLOBAL-H1-LOCALIZATION-RECIPROCITY-AUDIT", "stable_id": "LIT-WF02", "role": "GLOBAL_H1_LOCALIZATION_RECIPROCITY_APPLICABILITY_WORKFLOW", "class": "NEW_LITERATURE_WORKFLOW"}
            ],
            "source_anchor_only": ["S36-PW01", "S36-PW05"],
            "duplicates": [
                "HOSTILE-RECIPROCAL-METHODS",
                "HOSTILE-FINITE-PRIME-WEIL-COMPLETION",
                "HOSTILE-TRANSVECTION-SYMPLECTIC-STRUCTURE",
                "HOSTILE-FINITE-GROUP-RECONSTRUCTION",
                "HOSTILE-MW-LOCAL-SIEVE",
                "HOSTILE-FACTOR-SQUARECLASS-LINEARIZATION",
                "HOSTILE-GAUSSIAN-ORIENTATION-NORM",
            ],
            "not_applicable": ["MILLER-STOLL2013-TO-S36-PW05-2ISOGENY"],
            "research_gaps": ["GLOBAL-HILBERT-SELMER-COMPATIBILITY-TERMINAL"],
            "possible_novelty_flags": [],
            "repo_specific_no_new_literature_delta": ["DISC-S36-B02->S35-PW02", "DISC-S36-B04->S34-W03"],
        },
        "accepted_item_metadata": accepted,
        "source_anchor_only": {
            "S36-PW01": {"literature": [pardini], "strength_delta": "source anchor only; mathematical output unchanged", "source_pr": 1590, "source_exact_head": "f22d67dda4183c3bfd39710ebb4083f5185f3f49"},
            "S36-PW05": {"literature": [stoll], "strength_delta": "source anchor only; mathematical output unchanged", "source_pr": 1632, "source_exact_head": "98d057a47fc37a897fb14e904cdf9d52913f082b"},
        },
        "workflow_metadata": {
            "LIT-WF02": {
                "classification": "NEW_LITERATURE_WORKFLOW",
                "literature": [serre, milne],
                "exact_reusable_contract": "repo local rows/charts -> identify one fixed global H1/Kummer system -> prove exact localizations and all-place normalization -> bind literature theorem inputs -> PASS typed package or FAIL_CLOSED",
                "HYPOTHESES": ["named global finite module/class", "exact localization maps", "complete relevant-place panel", "field-change semantics explicit"],
                "APPLICABILITY": "repo branches attempting to upgrade local character/Kummer data to reciprocity, Selmer or global-duality inputs",
                "DO_NOT_USE_FOR": ["constructing a missing global class", "Hilbert reciprocity as a contradiction", "local admissibility as rational point", "theorem/receiver/endpoint credit"],
                "stage36_source_input": ["S36-PW04", "S36-PW07"],
                "repo_adapter": "workflow audits the existence and exactness of the global-localization adapter; it does not create the adapter",
                "adapter_source_verifier": "none at registration; workflow is fail-closed and carries zero mathematical credit",
                "output": "typed theorem-input package or first missing obligation",
                "maturity_recommendation": "PROVISIONAL",
            }
        },
    }

    INDEX.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print("PASS: Stage36 literature Phase4 registry mutation materialized")


if __name__ == "__main__":
    main()
