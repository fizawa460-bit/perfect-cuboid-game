#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
PREFLIGHT = HERE / "BTVA-COMPRESSED-PICARD-LIFT-INTERSECTION-PREFLIGHT.json"

PREFLIGHT_BLOB = "68108dfb110c4ea1d9dc0d74564a431bbbffbbde"
PREFLIGHT_CANON = "19e4149e9171df4d024d49f343882611bf2a54e0e30dfed37d1e0b92f6d796ee"
LANE178_HEAD = "e60f03cf5105bc6e26cb4615acabd6fe0c07625c"

LOCAL_LOCKS = {
    "btva_diagnostic": ("stages/stage32-ex5/breadth-cycle-2/bc2-00-btva-node-support-span-diagnostic.json", "554f8626e0ea225ffb7e6a5b6fe40ee41a7448ee"),
    "runtime_node_bridge": ("stages/stage32-ex5/breadth-cycle-2/bc2-01b-runtime-node-coordinate-bridge.json", "2a14a683e8ec38ec993eb711841c466f2be6eb06"),
    "old_support_blocker": ("stages/stage32-ex5/breadth-cycle-2/bc2-02-full178-support-reconstruction-preflight.json", "68d47f8ad2a3ff8eff13324a700bd96b3c22fbac"),
    "representative_support": ("stages/stage32-ex5/breadth-cycle-2/bc2-02-g1-d186-representative-support-reconstruction.json", "da3b4ed5c57b1797370ff519788d2c69c532985b"),
    "selected64_pairing_solver": ("stages/stage32-ex5/breadth-cycle-2/bc2_02_one_indexed_full178_terminal_pairing_coordinate_completion.py", "a82d56d0e9649b0cdd332b7eacc49bc364e2ffd0"),
    "stage34_arsenal": ("docs/stage34-arsenal-promotion.md", "5703f6fe8e9b2de6a0bd167ffdee33d15cfd3f1a"),
}
LANE178_LOCKS = {
    "aggregate_picard_preflight": ("stages/stage32/32-01-178/fibration-nef/verify_fibration_nef_aggregate_picard_lattice_preflight.py", "5fa9f1d67d6411cb550230b62398aff7bd6488ff"),
    "picard_prefix_preflight": ("stages/stage32/32-01-178/fibration-nef/verify_fibration_nef_picard_prefix_composition_preflight.py", "7f0cfae30b2e081f9579d68bd4e80c1e57f94f6a"),
    "recoverability": ("stages/stage32/32-01-178/fibration-nef/verify_fibration_nef_recoverability.py", "fbd8dad2194378a6bf77d12cc2c65ac03782f112"),
}

OBS = ["a", "b", "c", "t", "x4", "e", "d", "r0", "r1", "r2", "r3", "r4"]


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def lock_json(path: Path, expected_blob: str, expected_canon: str, label: str) -> dict:
    req(path.is_file(), "missing " + label)
    req(blob(path) == expected_blob, label + " blob drift")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == expected_canon,
        label + " stored canonical drift")
    req(canon(obj) == expected_canon, label + " canonical drift")
    return obj


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane178-root", type=Path, required=True)
    args = ap.parse_args()
    lane = args.lane178_root.resolve()

    p = lock_json(PREFLIGHT, PREFLIGHT_BLOB, PREFLIGHT_CANON, "compressed BTVA preflight")
    req(p["status"] == "STRUCTURAL_ADAPTER_PASS__BOUNDED_EXECUTION_NOT_RUN__ZERO_MAIN_CREDIT",
        "preflight status")
    req(p["exact_interface"]["compressed_observable_order"] == OBS, "observable order")
    req(p["exact_interface"]["all140_normal_nonnegativity_required_for_this_preflight"] is False,
        "unsafe all140-normal positivity dependency")
    req(p["btva_genus0_nonconic"]["genus1_claimed"] is False, "genus1 overclaim")
    req(p["btva_genus0_nonconic"]["known_conic_exception_must_be_separate"] is True,
        "known-conic exception lost")
    req(p["lazy_flat_separation"]["per_terminal_59d_witness_required"] is False,
        "59D materialization unexpectedly required")
    req(p["lazy_flat_separation"]["preenumerate_593735_node_hyperplanes_required"] is False,
        "eager hyperplane enumeration unexpectedly required")
    for k, v in p["credit_firewalls"].items():
        req(v is False, "credit firewall " + k)

    # Current state is mutable zero-credit research state: check canonical
    # integrity and authority semantics, not a recursive blob lock.
    state = json.loads((ROOT / "stages/stage32/MAIN-STATE.json").read_text(encoding="utf-8"))
    stored_state_canon = state.get("canonical_sha256_without_this_field")
    req(isinstance(stored_state_canon, str) and canon(state) == stored_state_canon,
        "current MAIN state canonical drift")
    req(state["current_exact_frontier"]["authoritative_remaining_terminals"] ==
        157570677819451133507, "current MAIN authority drift")
    req(state["current_exact_frontier"]["full178_numerical_census_complete"] is False,
        "FULL178 completion overclaim")
    req(state["firewalls"]["merge_authorized"] is False, "merge firewall")

    local = {}
    for label, (rel, expected) in LOCAL_LOCKS.items():
        path = ROOT / rel
        req(path.is_file(), "missing local source " + label)
        req(blob(path) == expected, "local source drift " + label)
        if path.suffix == ".json":
            local[label] = json.loads(path.read_text(encoding="utf-8"))

    # Exact lane head is asserted immediately before this verifier by the
    # startup workflow.  Here we source-lock the load-bearing 178 interface
    # without rerunning its SymPy producer in MAIN startup.
    lane_text = {}
    for label, (rel, expected) in LANE178_LOCKS.items():
        path = lane / rel
        req(path.is_file(), "missing 178 source " + label)
        req(blob(path) == expected, "178 source drift " + label)
        lane_text[label] = path.read_text(encoding="utf-8")

    agg = lane_text["aggregate_picard_preflight"]
    req('OBSERVABLE_ORDER = AGGREGATE_ORDER + ("e", "d", "r0", "r1", "r2", "r3", "r4")' in agg,
        "178 aggregate observable-order source drift")
    req('"rule_is_exact_for_linear_picard_lattice_extendability": True' in agg,
        "178 exact Picard-lattice interface source drift")
    req('"safe_rejection_rule": "a candidate observable vector is impossible if any listed HNF membership congruence is nonzero modulo membership_modulus"' in agg,
        "178 exact rejection-rule source drift")

    pref = lane_text["picard_prefix_preflight"]
    req('OBSERVABLE_ORDER = ("a", "b", "c", "t", "x4", "e", "d", "r0", "r1", "r2", "r3", "r4")' in pref,
        "178 prefix observable-order source drift")
    req("STATIC_WIDTH = 7" in pref and "RESIDUAL_DIM = 5" in pref,
        "178 static/residual split source drift")
    req('"production_domain_bridge_ready": True' in pref,
        "178 production-domain bridge source drift")

    btva = local["btva_diagnostic"]
    nec = btva["theorem_source"]["necessary_conditions"]
    req(nec["genus0_nonconic"] ==
        "other than van Luijk's 32 plane conics, passes through at least seven singularities that span P^6",
        "BTVA genus0 nonconic statement drift")
    req(btva["receiver_scope"]["target"] == "R29-LG2 numerical unibranch FULL178 only",
        "BTVA receiver scope drift")

    blocker = local["old_support_blocker"]
    req(blocker["status"] == "BLOCKED_RETAINED_INTERFACE_MISSING_EXACT_48_SUPPORT_WITNESS",
        "historical blocker status drift")
    req(blocker["minimal_reentry"][2].startswith("Theorem alternative:"),
        "historical support-invariance alternative drift")

    node = local["runtime_node_bridge"]
    rows = node["rows"]
    req(len(rows) == 48, "node bridge row count")
    req([int(r["runtime_index_0based"]) for r in rows] == list(range(48)),
        "node runtime index order")
    req([int(r["retained_exceptional_index_0based"]) for r in rows] == list(range(48)),
        "node exceptional index order")
    req(node["counts"]["unique_canonical_nodes"] == 48 and
        node["counts"]["collisions"] == 0 and node["counts"]["omissions"] == 0,
        "node bridge uniqueness")

    rep = local["representative_support"]
    span = rep["exact_projective_span_checksum"]
    req(span["determinant"] == 16 and span["homogeneous_vector_rank"] == 7 and
        span["support_spans_P6"] is True, "retained exact rank-7 node-span checksum drift")

    arsenal = (ROOT / LOCAL_LOCKS["stage34_arsenal"][0]).read_text(encoding="utf-8")
    req("S34-W03 — receiver-restricted intersection exclusion" in arsenal,
        "S34-W03 router source drift")
    req("B(Q) intersect K(Q) = empty" in arsenal,
        "S34-W03 intersection semantics drift")

    req(p["ownership"]["bridge_issue1817_p0_p1_p2_duplicated"] is False,
        "Bridge ownership overlap")
    req(p["relation_to_old_blocker"]["support_invariance_theorem_required"] is False,
        "old support-invariance blocker reintroduced")

    print("PASS: exact 178 static/residual Picard interface is source-locked at " + LANE178_HEAD)
    print("PASS: historical BC2 binds all 48 exceptional slots to unique canonical nodes")
    print("PASS: retained exact seven-node determinant certifies a P6-spanning node subset exists")
    print("PASS: lazy proper-flat cut construction is structurally admissible; no SymPy producer replay in MAIN startup")
    print("PASS: zero MAIN/receiver/theorem credit; bounded genus-0 real-production execution remains the next gate")


if __name__ == "__main__":
    main()
