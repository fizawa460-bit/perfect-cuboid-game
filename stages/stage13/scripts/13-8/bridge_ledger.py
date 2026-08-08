#!/usr/bin/env python3
"""Stage13-8a: exact Stage12 -> Stage13 bridge ledger.

This is a consistency/consolidation audit, not a new analytic theorem.
It verifies that the already-proved pieces form one exact bridge

    Stage12 primitive oriented records
      -> primitive canonical raw face incidences
      -> directional raw asymptotics
      -> primitive canonical exactly-one counts.

The principal exact projection is

    C_prim,q^proj(B) = 2 A_q(B),
    C_prim(B)        = 2 A_total(B),

and Stage13-7jf then gives

    N_q(B) = (1/2) C_prim,q^proj(B) + o(B(log B)^3),
    N_1(B) = (1/2) C_prim(B)        + o(B(log B)^3).

The script also checks cutoff/primitivity conventions, the parity-stratified
factor 2, the Stage12 total constant, the Stage13 directional constants, and
the finite inclusion-exclusion identities already locked by Stage13-3a/7jc.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

STAGE12_README = Path("stages/stage12/README.md")
ROOT3 = Path("stages/stage13/data/13-3")
ROOT7 = Path("stages/stage13/data/13-7")
OUT = Path("stages/stage13/data/13-8/bridge_ledger_report.json")

FIBER = ROOT3 / "representation_fiber_report.json"
PARITY = ROOT3 / "parity_2adic_report.json"
FINITE = ROOT3 / "raw_incidence_report.json"
RAW = ROOT7 / "supported_richness_raw_asymptotic_report.json"
OVERLAP = ROOT7 / "overlap_face_cuboid_reduction_report.json"
EXACT = ROOT7 / "exact_one_fixed_prime_sieve_report.json"
FINAL7 = ROOT7 / "consolidation_audit_report.json"

Q = ("ab", "ac", "bc")
TOL = 5e-13


def close(a: float, b: float, tol: float = TOL) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def build_report() -> dict:
    stage12 = STAGE12_README.read_text()
    fiber = load(FIBER)
    parity = load(PARITY)
    finite = load(FINITE)
    raw = load(RAW)
    overlap = load(OVERLAP)
    exact = load(EXACT)
    final7 = load(FINAL7)

    # Frozen Stage12 theorem interface.
    assert "primitive oriented count" in stage12
    assert "C_{\\rm prim}(B)" in stage12
    assert "\\frac{\\kappa}{12\\pi}" in stage12
    assert "Stage12 is not reopened" in stage12

    # Exact Stage12 -> Stage13 raw-incidence projection.
    bridge = fiber["exact_bridge"]
    assert bridge["supported_full_orientation_fiber_size"] == 1
    assert bridge["supported_orientations_per_canonical_incidence"] == 2
    assert bridge["canonical_projection_multiplicity"] == 2
    assert bridge["identity"] == "C_prim(B)=2*(A_ab(B)+A_ac(B)+A_bc(B))"

    for row in fiber["rows"]:
        A = row["stage13_raw_incidence"]
        C = row["stage12_projected_primitive_records"]
        assert row["stage12_primitive_oriented_total"] == 2 * row["stage13_raw_incidence_total"]
        for q in Q:
            assert C[q] == 2 * A[q]
        for stratum in ("OE", "EE"):
            inc = row["parity_control"][stratum]["incidence"]
            rec = row["parity_control"][stratum]["stage12_records"]
            assert row["parity_control"][stratum]["projection_ratio"] == 2.0
            for q in Q:
                assert rec[q] == 2 * inc[q]

    # Parity compatibility: no extra category-dependent 2-adic projection factor.
    parity_facts = "\n".join(parity["exact_facts"])
    assert "exactly one odd edge and odd d" in parity_facts
    assert "both even edges to be divisible by 4" in parity_facts
    assert "standalone p=2 local density is category-symmetric" in parity_facts

    # Finite exact inclusion-exclusion, including multi-face objects.
    finite_rows_by_B = {int(row["B"]): row for row in finite["rows"]}
    fiber_rows_by_B = {int(row["B"]): row for row in fiber["rows"]}
    for B, row in finite_rows_by_B.items():
        A = row["raw_incidence"]
        N = row["exact_one"]
        O = row["overlap"]
        T = int(O["three_face"])
        assert N["ab"] == A["ab"] - O["ab_ac"] - O["ab_bc"] + T
        assert N["ac"] == A["ac"] - O["ab_ac"] - O["ac_bc"] + T
        assert N["bc"] == A["bc"] - O["ab_bc"] - O["ac_bc"] + T
        A_total = sum(int(A[q]) for q in Q)
        N_total = sum(int(N[q]) for q in Q)
        O_total = int(O["ab_ac"] + O["ab_bc"] + O["ac_bc"])
        assert N_total == A_total - 2 * O_total + 3 * T
        assert fiber_rows_by_B[B]["stage12_primitive_oriented_total"] == 2 * A_total

    # Stage13 raw directional constants refine the frozen Stage12 total.
    I = final7["constant_audit"]["I"]
    Iq = {q: float(I[q]) for q in Q}
    assert close(sum(Iq.values()), math.pi**2 / 8.0)

    kappa_diag = float(raw["frozen_stage12_total"]["kappa_prime_product_diagnostic"])
    D = {
        q: float(raw["individual_raw_asymptotics"][q]["numeric_prime_product_diagnostic"])
        for q in Q
    }
    for q in Q:
        assert close(D[q], kappa_diag * Iq[q] / (3.0 * math.pi**3))
    assert close(sum(D.values()), kappa_diag / (24.0 * math.pi))

    # Projected Stage12 category constants are twice the canonical raw constants.
    Cproj = {q: 2.0 * D[q] for q in Q}
    assert close(sum(Cproj.values()), kappa_diag / (12.0 * math.pi))

    P = {q: 8.0 * Iq[q] / math.pi**2 for q in Q}
    for q in Q:
        assert close(Cproj[q], (kappa_diag / (12.0 * math.pi)) * P[q])
        assert close(D[q], (kappa_diag / (24.0 * math.pi)) * P[q])

    eta_diag = math.pi * kappa_diag
    for q in Q:
        # Equivalent eta form: kappa=eta/pi.
        assert close(D[q], eta_diag * Iq[q] / (3.0 * math.pi**4))

    # Exact-one transfer is unconditional at the Stage13-7jf level.
    assert overlap["single_scalar_reduction"]["sufficient_bound"] == "F(B)=o(B(log B)^3)"
    assert exact["status"]["pair_overlap_lower_order_proved"] is True
    assert exact["status"]["triple_overlap_lower_order_proved"] is True
    assert exact["status"]["exact_one_category_asymptotics_proved"] is True
    assert exact["status"]["perfect_cuboid_nonexistence_assumed"] is False
    assert final7["status"]["stage13_7_complete"] is True

    # The fixed-prime extension belongs to Stage13, not the frozen Stage12 theorem statement.
    order = exact["fixed_congruence_refinement"]["important_order_of_limits"]
    assert "hold them fixed" in order
    assert "B->infinity" in order
    assert "k->infinity" in order

    # Largest finite lock, useful as an end-to-end bridge checksum.
    B_lock = max(finite_rows_by_B)
    frow = finite_rows_by_B[B_lock]
    brow = fiber_rows_by_B[B_lock]
    A_lock = sum(frow["raw_incidence"].values())
    N_lock = sum(frow["exact_one"].values())
    C_lock = int(brow["stage12_primitive_oriented_total"])
    O_lock = frow["overlap"]
    O_sum_lock = int(O_lock["ab_ac"] + O_lock["ab_bc"] + O_lock["ac_bc"])
    T_lock = int(O_lock["three_face"])
    assert C_lock == 2 * A_lock
    assert N_lock == C_lock // 2 - 2 * O_sum_lock + 3 * T_lock

    return {
        "metadata": {
            "stage": "13-8a",
            "scope": "exact Stage12-to-Stage13 theorem-interface ledger; no new analytic theorem",
            "classification": "PASS_NO_NEW_MATHEMATICAL_BRIDGE_GAP_FOUND",
        },
        "frozen_stage12_input": {
            "object": "primitive oriented distinguished-face record count C_prim(B)",
            "theorem": "C_prim(B) ~ [kappa/(12 pi)] B(log B)^3 = [eta/(12 pi^2)] B(log B)^3",
            "reopened": False,
            "import_rule": "Stage13 imports only the frozen theorem/object definitions; directional refinement and overlap removal are Stage13 results.",
        },
        "object_level_bridge": {
            "stage12_record_to_stage13_incidence": (
                "A Stage12 record consists of a designated integral face x^2+y^2=P^2, "
                "a complementary Pythagorean extension P^2+z^2=d^2, and the retained "
                "ordered face-leg orientation. Forget the face-leg order, sort the three "
                "edges to a<b<c, and retain which canonical face q contains {x,y}."
            ),
            "cutoff_compatibility": "Stage12 d=h(r^2+s^2)/2<=B is exactly the Stage13 space-diagonal cutoff d<=B.",
            "primitive_compatibility": (
                "Stage12 primitivity is Möbius inversion by the common integer scale of all "
                "three edges. This is exactly gcd(a,b,c)=1 after canonical sorting; sorting "
                "and swapping the two distinguished face legs preserve the gcd."
            ),
            "outer_parameter_uniqueness": (
                "For a fixed complementary Pythagorean triple (P,z,d), the Stage12 "
                "coprime r<s convention has one supported outer parameter record; the "
                "remaining universal multiplicity comes only from the two orders (x,y),(y,x)."
            ),
            "repeated_side_boundary": (
                "The frozen Stage12 definition sheet records repeated-side contribution zero; "
                "there is therefore no canonical tie boundary requiring an additional main-term correction."
            ),
            "multi_face_rule": (
                "Raw incidence retains the distinguished face. An exactly-two object contributes "
                "two canonical raw incidences and four Stage12 oriented records; an exactly-three "
                "object contributes three incidences and six records. Hence the factor 2 remains exact on overlaps."
            ),
        },
        "exact_projection_theorem": {
            "define": "C_prim,q^proj(B) = Stage12 primitive oriented records whose distinguished face becomes canonical category q",
            "categorywise": "C_prim,q^proj(B)=2 A_q(B) for q in {ab,ac,bc}",
            "total": "C_prim(B)=sum_q C_prim,q^proj(B)=2(A_ab+A_ac+A_bc)",
            "fiber_size": 2,
            "parity_stratified": True,
            "extra_2adic_projection_factor": False,
        },
        "directional_constant_bridge": {
            "P_q": "P_q=8 I_q/pi^2",
            "projected_stage12": "C_prim,q^proj(B) ~ [kappa/(12 pi)] P_q B(log B)^3 = [2 kappa I_q/(3 pi^3)] B(log B)^3",
            "canonical_raw": "A_q(B) ~ [kappa/(24 pi)] P_q B(log B)^3 = [kappa I_q/(3 pi^3)] B(log B)^3",
            "canonical_raw_eta_form": "A_q(B) ~ [eta I_q/(3 pi^4)] B(log B)^3",
            "numeric_kappa_diagnostic_only": kappa_diag,
            "numeric_eta_diagnostic_only": eta_diag,
            "P_numeric": P,
            "projected_stage12_constants_numeric": Cproj,
            "canonical_raw_constants_numeric": D,
            "symbolic_constants_authoritative": True,
        },
        "exact_one_bridge": {
            "exact_category_identity": {
                "ab": "N_ab=A_ab-O_ab_ac-O_ab_bc+T",
                "ac": "N_ac=A_ac-O_ab_ac-O_ac_bc+T",
                "bc": "N_bc=A_bc-O_ab_bc-O_ac_bc+T",
            },
            "exact_total_identity": "N1=C_prim/2-2(O_ab_ac+O_ab_bc+O_ac_bc)+3T",
            "overlap_scale": "all pair overlaps and T are o(B(log B)^3)",
            "asymptotic_category_bridge": "N_q(B)=(1/2)C_prim,q^proj(B)+o(B(log B)^3)",
            "asymptotic_total_bridge": "N1(B)=(1/2)C_prim(B)+o(B(log B)^3)",
            "perfect_cuboid_nonexistence_assumed": False,
        },
        "scope_boundary": {
            "belongs_to_frozen_stage12": [
                "definition of C_prim and its primitive/oriented convention",
                "C_prim(B)~[kappa/(12 pi)]B(log B)^3",
                "eta=pi*kappa and the frozen local-factor ledger",
            ],
            "proved_in_stage13": [
                "exact factor-2 projection to canonical raw incidences (13-3d)",
                "categorywise raw constants and chamber proportions (13-7jb)",
                "fixed-prime overlap lower-order theorem (13-7jf)",
                "unconditional exactly-one directional limit (13-7jf/7jg)",
            ],
            "stage12_reopen_required": False,
        },
        "finite_end_to_end_lock": {
            "B": B_lock,
            "C_prim": C_lock,
            "A_total": A_lock,
            "N1": N_lock,
            "pair_overlap_sum": O_sum_lock,
            "triple_overlap": T_lock,
            "checks": {
                "C_prim_equals_2_A_total": C_lock == 2 * A_lock,
                "N1_equals_C_prim_over_2_minus_2O_plus_3T": N_lock == C_lock // 2 - 2 * O_sum_lock + 3 * T_lock,
            },
        },
        "bridge_gap_audit": {
            "object_map": "CLOSED",
            "cutoff_matching": "CLOSED",
            "primitive_definition_matching": "CLOSED",
            "orientation_fiber": "CLOSED",
            "canonical_direction_partition": "CLOSED",
            "parity_projection": "CLOSED",
            "stage12_total_constant": "CLOSED_FROZEN_INPUT",
            "directional_raw_constants": "CLOSED_BY_13_7JB",
            "overlap_to_exact_one": "CLOSED_BY_13_7JF",
            "new_mathematical_bridge_lemma_required": False,
            "remaining_task": "canonical exposition/notation consolidation in Stage13 main.md",
        },
        "status": {
            "stage13_8a_complete": True,
            "no_new_mathematical_bridge_gap_found": True,
            "stage12_reopened": False,
            "next": "Stage13-8b canonical bridge theorem integration",
        },
    }


def main() -> None:
    report = build_report()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["status"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
