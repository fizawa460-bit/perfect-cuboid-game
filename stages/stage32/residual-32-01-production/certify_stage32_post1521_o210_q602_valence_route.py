#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CERT_PATH = "stages/stage32/residual-32-01-production/post1521-o210-q602-valence-route.json"
EXPECTED_CANONICAL = "cfd490ca23c6498ae9236228206b69c11290b9a5381e42161e9389e02b71ebcc"
EXPECTED_DIAGONAL = [118,126,134,142,150,158,166,174,182,190,198,206,214,222,230,238,246,254]
EXPECTED_NU = [-17,-15,-13,-11,-9,-7,-5,-3,-1,1,3,5,7,9,11,13,15,17]


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def canonical_sha256(doc: dict) -> str:
    body = dict(doc)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_lock(lock: dict):
    p = ROOT / lock["path"]
    assert p.is_file(), p
    assert blob_sha1(p) == lock["blob_sha1"], p
    if p.suffix == ".json":
        d = json.loads(p.read_text())
        if "canonical_sha256" in lock:
            assert canonical_sha256(d) == lock["canonical_sha256"], p
        return d
    return p.read_text()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", required=True)
    args = ap.parse_args()
    assert Path(args.check).as_posix() == CERT_PATH

    cert = json.loads((ROOT / CERT_PATH).read_text())
    assert cert["schema"] == "STAGE32_POST1521_O210_Q602_VALENCE_ROUTE_V1"
    assert canonical_sha256(cert) == cert["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL

    locks = cert["source_locks"]
    spectrum = load_lock(locks["post1518_trace_spectrum"])
    repair_note = load_lock(locks["post1500_repair_source_note"])
    arsenal_index = load_lock(locks["arsenal_index"])
    s34 = load_lock(locks["arsenal_s34_w03"])
    s32 = load_lock(locks["arsenal_s32_pw03"])
    s28 = load_lock(locks["arsenal_s28_w04"])
    route_note = load_lock(locks["source_note"])

    assert spectrum["exact_spectrum"]["diagonal_intersection_values"] == EXPECTED_DIAGONAL
    assert spectrum["decision"]["Q602_excluded"] is False
    assert "Tr_Q(T^dagger*T)=2*Q(T)" in repair_note.replace(" ", "") or "Tr_Q(T^dagger*T) = 2*Q(T)" in repair_note

    assert arsenal_index["registry_contract"]["authority_order"][0] == "active stage controller and current source locks"
    assert "RECEIVER_RESTRICTED_INTERSECTION_EXCLUSION" in s34
    assert "an exact source/receiver contract" in s34
    assert "LATTICE_IMAGE_HNF_GATE" in s32 and "exact integral observables" in s32
    assert "COMMON_POLARIZATION_FIXED_CURVE_DIFFERENTIAL" in s28

    pre = cert["arsenal_precheck"]
    assert pre["missing_weapon_type"] == "CORRESPONDENCE_GEOMETRY_TO_DIAGONAL_SCALAR"
    assert pre["direct_applicable_card_found"] is False
    assert pre["s34_w03_requires_existing_receiver_condition"] is True
    assert pre["s32_pw03_requires_existing_exact_observable_map"] is True
    assert pre["s28_w04_object_mismatch"] is True
    assert pre["bounded_routing_only"] is True

    fixed = cert["fixed_input"]
    assert fixed["O"] == 210 and fixed["Q"] == 602 and fixed["genus_C0"] == 2
    assert fixed["bidegree"] == [105,81] and fixed["diagonal_values"] == EXPECTED_DIAGONAL

    # Recompute the conditional arithmetic independently.
    nu = [(m - 186) // 4 for m in EXPECTED_DIAGONAL]
    assert all((m - 186) % 4 == 0 for m in EXPECTED_DIAGONAL)
    assert nu == EXPECTED_NU
    assert all(2*n*n != 602 for n in nu)
    assert not any(n*n == 301 for n in range(-100, 101))

    cm = cert["conditional_valence_math"]
    assert cm["induced_endomorphism"] == "T=-nu*id"
    assert cm["cayley_brill_formula"] == "Gamma.Delta=186+4*nu"
    assert cm["trace_formula"] == "Tr_Q(T)=-4*nu=186-Gamma.Delta"
    assert cm["rosati_formula"] == "Q(T)=2*nu^2"
    assert cm["Q602_equation"] == "nu^2=301"
    assert cm["integer_solution_exists"] is False
    assert cm["nu_values_from_audited_diagonal_spectrum"] == EXPECTED_NU
    assert cm["conditional_pruning"] == "18 -> 0"

    d = cert["decision"]
    assert d["valence_proved_for_actual_Gamma"] is False
    assert d["Q602_excluded_unconditionally"] is False
    assert d["O210_excluded_unconditionally"] is False
    assert d["conditional_Q602_exclusion_if_valence"] is True
    assert d["O212_plus_authorized"] is False
    assert "prove or refute valence" in d["next_required_fact"]

    assert "does **not** prove that `Gamma` has valence" in route_note
    ext = locks["external_valence_source"]
    assert ext["author"] == "Igor Dolgachev" and ext["section"] == "5.5.1"
    assert ext["proposition"] == "5.5.1" and "Cayley-Brill" in ext["corollary"]

    ctl = json.loads((ROOT / "stages/stage32/controller.json").read_text())
    assert ctl["schema"] == "STAGE32_LOWGENUS_PICARD_CONTROLLER_V247_POST1520_Q602_RETAINED_GEOMETRY_18_TO_18_AUDITED"
    assert ctl["stage"] == 32 and ctl["stage32_closed"] is False
    assert ctl["advance_allowed"] is True
    assert ctl["current_item"] == "O210_Q602_NEW_SCALAR_COUPLING_ROUTE_SELECTION"
    leaf = ctl["current_leaf"]
    assert leaf["status"] == "AUDITED_BOUNDED_NEGATIVE_18_TO_18"
    assert leaf["O212_and_later_blocked"] is True
    ops = ctl["operations"]
    assert ops["external_source_research_authorized"] is True
    assert ops["new_theorem_work_authorized"] is True
    assert ops["heavy_compute_authorized"] is False and ops["full178_scaleout_authorized"] is False
    pol = ctl["post1520_route_policy"]
    assert pol["arsenal_check_required_before_external_search"] is True
    assert pol["external_literature_allowed_after_no_applicable_card"] is True
    assert pol["new_theorem_work_allowed_after_no_applicable_card"] is True
    assert ctl["math_scope"]["fixed_z_O212_through_O266_qprime4"] == "BLOCKED_BEHIND_O210"
    fw = ctl["firewalls"]
    assert fw["O210_closed"] is False and fw["Q602_excluded"] is False
    assert fw["receiver_credit"] is False and fw["route_credit"] is False
    assert fw["theorem_credit"] is False and fw["endpoint_credit"] is False

    cfw = cert["firewalls"]
    assert all(cfw[k] is False for k in [
        "conditional_implies_unconditional","genus2_implies_valence","bidegree_implies_valence",
        "arsenal_miss_implies_global_absence","geometric_realization_credit","receiver_credit",
        "route_credit","theorem_credit","endpoint_credit","perfect_cuboid_claim"
    ])

    print("PASS: Stage32 new valence route is source-routed and exact conditionally: valence => Q=2 nu^2, so Q602 impossible; actual Gamma valence remains unproved and O210 stays open.")

if __name__ == "__main__":
    main()
