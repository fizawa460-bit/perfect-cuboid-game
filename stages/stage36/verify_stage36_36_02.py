#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = ROOT / "stages/stage36/MAIN-STATE.json"
INV_PATH = ROOT / "stages/stage36/36-02/representative-inventory.json"
BASE = "8c59c81bcf0bcd442705cfb7a3db297253b34679"

SOURCE_LOCKS = {
    "stage29_kernel_checker": ("stages/stage29/29-02hb/campedelli_kernel_check.py", "0e44eea33eb696f32e556a893310a563ed31cb12"),
    "stage29_q_qi_symmetry_result": ("stages/stage29/29-02ha/result.md", "b1ca15c16df1467c7cece4b78db4b2a41e147f90"),
    "stage29_exact_sign_cover_model": ("stages/stage29/29-02ha/exact-sign-cover-model.md", "fc2d5284a259750f45d2d756a952002671e3bccc"),
    "stage29_campedelli_quotient_adapter": ("stages/stage29/29-02hb/campedelli-quotient-adapter.md", "5f959d60106243bb31df06a3961ab04182d78fc7"),
    "stage29_campedelli_route_contract": ("stages/stage29/29-02hb/route-contract.json", "75045d8f15786836e8a7383fc07ef95161fa86e7"),
}
ARSENAL_LOCKS = {
    "router": ("docs/arsenal/index.json", "aa45d19c2f1d8970c7f142bf744c5c17e75abe5a"),
    "S30-W01": ("docs/arsenal/cards/formal/S30-W01.md", "0b0d8871ce873896e62e841deb698f3c505abda5"),
    "S30-WF02": ("docs/arsenal/cards/workflows/S30-WF02.md", "38e4625155eb079bbe3d50d663c6256559319886"),
    "S30-WF03": ("docs/arsenal/cards/workflows/S30-WF03.md", "12740198aba19ade18302819f8e890dbda4eb701"),
}
LINE_FORMS = {
    "A1": "x",
    "A2": "y",
    "A3": "z",
    "B3": "(x+y)",
    "B2": "(x+z)",
    "B1": "(y+z)",
    "C": "(x+y+z)",
}


def require(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(msg)


def blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load_checker():
    path = ROOT / SOURCE_LOCKS["stage29_kernel_checker"][0]
    spec = importlib.util.spec_from_file_location("stage29_campedelli_kernel_check", path)
    require(spec is not None and spec.loader is not None, "cannot load Stage29 kernel checker")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def gamma_c0_basis(mod, kernel):
    rows = []
    for row in kernel:
        row = tuple(row)
        if row[6]:
            row = tuple(x ^ 1 for x in row)
        require(row[6] == 0, "C=0 gauge failed")
        rows.append(row[:6])
    rr, _ = mod.rref(rows, 6)
    return tuple(r for r in rr if any(r))


def signature(mod, kernel) -> str:
    return "/".join("".join(map(str, r)) for r in gamma_c0_basis(mod, kernel))


def label_map(mod, lab):
    return {n: "".join(map(str, lab[n])) for n in mod.NAMES}


def supports_and_radicals(mod, lab):
    supports = []
    radicals = []
    for r in range(3):
        support = [n for n in mod.NAMES if lab[n][r]]
        supports.append(support)
        radicals.append("*".join(LINE_FORMS[n] for n in support))
    return supports, radicals


def index_permutation(p):
    return [p[0] + 1, p[1] + 1, p[2] + 1]


def main() -> None:
    state = json.loads(STATE_PATH.read_text())
    inv = json.loads(INV_PATH.read_text())

    require(inv.get("schema") == "STAGE36_36_02_THREE_Q_REPRESENTATIVE_INVENTORY_V1", "inventory schema moved")
    require(inv.get("base_main_sha") == BASE, "inventory base moved")
    require(inv.get("status") == "EXACT_THREE_Q_REPRESENTATIVES_PENDING_HOSTILE_AUDIT", "inventory status moved")

    declared_sources = inv.get("source_locks", {})
    for key, (rel, sha) in SOURCE_LOCKS.items():
        require(declared_sources.get(key) == {"path": rel, "blob_sha": sha}, f"source declaration moved: {key}")
        require(blob_sha(ROOT / rel) == sha, f"source blob drift: {key}")

    declared_arsenal = inv.get("arsenal_locks", {})
    for key, (rel, sha) in ARSENAL_LOCKS.items():
        row = declared_arsenal.get(key, {})
        require(row.get("path") == rel and row.get("blob_sha") == sha, f"Arsenal declaration moved: {key}")
        require(blob_sha(ROOT / rel) == sha, f"Arsenal blob drift: {key}")
    require("FINITE_EQUIVARIANT_ACTION_IDENTIFICATION" in (ROOT / ARSENAL_LOCKS["S30-W01"][0]).read_text(), "S30-W01 role moved")
    require("IMMUTABLE_LAYERED_CERTIFICATE_REPLAY" in (ROOT / ARSENAL_LOCKS["S30-WF02"][0]).read_text(), "S30-WF02 role moved")
    require("ADAPTER_CREDIT_LAYER_FIREWALL" in (ROOT / ARSENAL_LOCKS["S30-WF03"][0]).read_text(), "S30-WF03 role moved")
    require(declared_arsenal.get("S30-W02") == "NOT_TRIGGERED_Q_FORM_ALREADY_EXACT_FROM_CONSTANT_SIGN_GROUP_AND_Q_LIFTABLE_S3", "S30-W02 routing moved")

    q_qi = (ROOT / SOURCE_LOCKS["stage29_q_qi_symmetry_result"][0]).read_text()
    for needle in [
        "Q-liftable base subgroup:      S3, order 6",
        "Q(i)-liftable base group:      S4, order 24",
        "All 24 incidence automorphisms are actual `PGL_3(Q)` automorphisms",
    ]:
        require(needle in q_qi, f"Q/Q(i) symmetry anchor missing: {needle}")

    sign_model = (ROOT / SOURCE_LOCKS["stage29_exact_sign_cover_model"][0]).read_text()
    for needle in [
        "L_{a1}=x",
        "L_{a2}=y",
        "L_{a3}=z",
        "L_{b3}=x+y",
        "L_{b2}=x+z",
        "L_{b1}=y+z",
        "L_c=x+y+z",
    ]:
        require(needle in sign_model, f"sign-cover line form missing: {needle}")

    adapter = (ROOT / SOURCE_LOCKS["stage29_campedelli_quotient_adapter"][0]).read_text()
    for needle in [
        "Cbar_H := Sbar/H",
        "deg(beta_H)=8",
        "Every coordinate-sign automorphism and every enumerated subgroup `H` is defined over `Q`",
        "S  --etale degree 8-->  C_H",
    ]:
        require(needle in adapter, f"Campedelli quotient anchor missing: {needle}")

    route = json.loads((ROOT / SOURCE_LOCKS["stage29_campedelli_route_contract"][0]).read_text())
    enum = route["exact_kernel_enumeration"]
    require(enum["distinct_rank3_kernels"] == 10, "Stage29 ten-kernel count moved")
    require(enum["certified_Q_kernel_orbit_sizes"] == [6, 2, 2], "Stage29 Q split moved")
    require(enum["geometric_Qi_kernel_orbit_sizes"] == [8, 2], "Stage29 Q(i) split moved")
    require(enum["exact_Q_isomorphism_class_count_proved"] is False, "Q-isomorphism firewall moved")

    mod = load_checker()
    labs = mod.admissible_labelings()
    require(len(labs) == 1680, "admissible labeling count moved")
    kernels = {}
    for lab in labs:
        kernels.setdefault(mod.kernel_of_labeling(lab), lab)
    require(len(kernels) == 10, "kernel count moved")
    keys = list(kernels)

    q_group = mod.q_liftable_coordinate_permutations()
    geom_group = mod.arrangement_automorphisms()
    require(len(set(q_group)) == 6, "Q-liftable group order moved")
    require(len(geom_group) == 24, "geometric group order moved")
    q_orbits = mod.kernel_orbits(keys, q_group)
    geom_orbits = mod.kernel_orbits(keys, geom_group)
    require(sorted(map(len, q_orbits)) == [2, 2, 6], "Q orbit partition moved")
    require(sorted(map(len, geom_orbits)) == [2, 8], "Q(i) orbit partition moved")
    require(sorted(i for o in q_orbits for i in o) == list(range(10)), "Q orbit coverage incomplete")

    computed = {}
    for qo in q_orbits:
        containing = [go for go in geom_orbits if set(qo) <= set(go)]
        require(len(containing) == 1, "Q orbit does not refine a unique geometric orbit")
        go = containing[0]
        type_id = f"Q{len(qo)}_GEOM{len(go)}"
        require(type_id not in computed, f"duplicate orbit type: {type_id}")

        _, rep_index = min((signature(mod, keys[i]), i) for i in qo)
        rep_kernel = keys[rep_index]
        rep_lab = kernels[rep_kernel]
        supports, radicals = supports_and_radicals(mod, rep_lab)

        support_rows = [tuple(rep_lab[n][r] for n in mod.NAMES) for r in range(3)]
        require(mod.rank_vectors(support_rows) == 3, f"generic squareclass rank not 3: {type_id}")

        stabilizer = sorted(index_permutation(p) for p in q_group if mod.permute_kernel(rep_kernel, p) == rep_kernel)
        computed[type_id] = {
            "q_orbit_size": len(qo),
            "geometric_qi_orbit_size": len(go),
            "label_map": label_map(mod, rep_lab),
            "kernel_upstairs_basis": ["".join(map(str, r)) for r in rep_kernel],
            "gamma_C0_basis": ["".join(map(str, r)) for r in gamma_c0_basis(mod, rep_kernel)],
            "orbit_member_gamma_signatures": sorted(signature(mod, keys[i]) for i in qo),
            "stabilizer_index_permutations": stabilizer,
            "character_supports": supports,
            "function_field_radicals": radicals,
            "canonical_model": "normalization of P2_Q in Q(P2)(sqrt(F1),sqrt(F2),sqrt(F3)) with the listed radicals",
            "resolved_model": "minimal resolution of Cbar_H",
            "q_defined": True,
        }

    require(set(computed) == {"Q6_GEOM8", "Q2_GEOM8", "Q2_GEOM2"}, "three Q representative types moved")
    require(inv.get("representatives") == computed, "representative inventory does not match exact replay")

    finite = inv.get("finite_reconstruction", {})
    require(finite.get("raw_admissible_labelings") == 1680, "inventory labeling count moved")
    require(finite.get("distinct_rank3_kernels") == 10, "inventory kernel count moved")
    require(finite.get("q_orbit_sizes") == [6, 2, 2], "inventory Q split moved")
    require(finite.get("geometric_qi_orbit_sizes") == [8, 2], "inventory Q(i) split moved")
    require(finite.get("exact_Q_isomorphism_class_count_proved") is False, "inventory Q-isomorphism firewall moved")

    degree = inv.get("degree_check", {})
    require(degree.get("three_character_support_vectors_independent_for_each_representative") is True, "degree independence flag moved")
    require(degree.get("generic_squareclass_rank") == 3, "generic squareclass rank moved")
    require(degree.get("canonical_quotient_degree") == 8, "canonical quotient degree moved")
    require(degree.get("resolved_etale_quotient_degree") == 8, "resolved quotient degree moved")

    require(inv.get("pass_condition") == {"THREE_CERTIFIED_Q_REPRESENTATIVES_EXACT": True, "EXACT_Q_ISOMORPHISM_CLASS_COUNT_CLAIM": False}, "36-02 pass condition moved")
    require(inv.get("promotion", {}).get("hostile_audit_required") is True, "36-02 hostile audit gate missing")
    require(inv.get("promotion", {}).get("promoted_to_audited_authority") is False, "36-02 prematurely promoted")
    require(inv.get("promotion", {}).get("next_leaf_before_audit_allowed") is False, "36-03 prematurely allowed")
    require(all(v is False for v in inv.get("claims", {}).values()), "36-02 inventory leaked higher credit")

    require(state.get("schema") == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V4_36_02_PENDING_AUDIT", "Stage36 state schema moved")
    require(state.get("status") == "ACTIVE_PENDING_HOSTILE_AUDIT", "Stage36 state status moved")
    require(state.get("base_main_sha") == BASE, "Stage36 state base moved")
    require(state.get("promotion_gates", {}).get("source_authority_lock_complete") is True, "36-01 audited promotion lost")
    require(state.get("promotion_gates", {}).get("three_Q_representatives_exact") is False, "36-02 gate prematurely promoted")
    unit = state.get("completed_units", {}).get("36-02", {})
    require(unit.get("status") == "EXACT_THREE_Q_REPRESENTATIVES_PENDING_HOSTILE_AUDIT", "36-02 state result moved")
    require(unit.get("THREE_CERTIFIED_Q_REPRESENTATIVES_EXACT") is True, "36-02 exact result missing")
    require(unit.get("EXACT_Q_ISOMORPHISM_CLASS_COUNT_CLAIM") is False, "36-02 Q-isomorphism overclaim")
    require(unit.get("promotion_status") == "PROVISIONAL_NOT_AUDITED", "36-02 promotion status moved")
    current = state.get("current", {})
    require(current.get("unit") == "36-02", "current unit advanced")
    require(current.get("next_exact_leaf") == "36-02_THREE_Q_REPRESENTATIVE_INVENTORY", "36-03 started before audit")
    require(current.get("provisional_successor_after_hostile_audit") == "36-03_PHYSICAL_OPEN_PUSH_AND_BOUNDARY", "36-03 successor moved")
    require(all(v is False for k, v in state.get("claims", {}).items()), "Stage36 claims leaked higher credit")

    print("PASS STAGE36_36_02_THREE_Q_REPRESENTATIVE_INVENTORY_V1")
    print("Q_orbits=6+2+2; geometric_Qi_orbits=8+2; representatives=Q6_GEOM8,Q2_GEOM8,Q2_GEOM2")
    print("each representative: exact H kernel + seven-line label map + Q-defined degree-8 function-field model")
    print("arsenal=S30-W01,S30-WF02,S30-WF03; S30-W02 not triggered")
    print("36-02 provisional exact result; hostile audit required; 36-03 not started")


if __name__ == "__main__":
    main()
