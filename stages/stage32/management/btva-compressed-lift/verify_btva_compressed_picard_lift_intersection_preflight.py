#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

import sympy
from sympy import Matrix, I

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
    "selected64_pairing_solver": ("stages/stage32-ex5/breadth-cycle-2/bc2_02_one_indexed_full178_terminal_pairing_coordinate_completion.py", "a82d56d0e9649b0cdd332b7eacc49bc364e2ffd0"),
    "stage34_arsenal": ("docs/stage34-arsenal-promotion.md", "5703f6fe8e9b2de6a0bd167ffdee33d15cfd3f1a"),
}
LANE178_LOCKS = {
    "aggregate_picard_preflight": ("stages/stage32/32-01-178/fibration-nef/verify_fibration_nef_aggregate_picard_lattice_preflight.py", "5fa9f1d67d6411cb550230b62398aff7bd6488ff"),
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


def q(s: str):
    return sympy.sympify(s, locals={"i": I})


def node_matrix(rows: list[dict]) -> Matrix:
    return Matrix([[q(str(v)) for v in row["canonical_stoll_coordinates"]] for row in rows])


def independent_basis_indices(m: Matrix) -> list[int]:
    picked: list[int] = []
    rank = 0
    for i in range(m.rows):
        trial = m[picked + [i], :]
        r = int(trial.rank())
        if r > rank:
            picked.append(i)
            rank = r
            if rank == m.cols:
                break
    return picked


def closure_indices(nodes: Matrix, support: list[int]) -> list[int]:
    if not support:
        return []
    base = nodes[support, :]
    r = int(base.rank())
    out = []
    for i in range(nodes.rows):
        if int(Matrix.vstack(base, nodes[i, :]).rank()) == r:
            out.append(i)
    return out


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

    # Current MAIN state is intentionally NOT blob-locked here.  This verifier
    # is a zero-credit research consumer and must survive later zero-credit
    # MAIN writebacks.  Verify canonical integrity and authority semantics
    # instead; historical V43/V42 boundaries are locked by startup CI.
    state_path = ROOT / "stages/stage32/MAIN-STATE.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))
    stored_state_canon = state.get("canonical_sha256_without_this_field")
    req(isinstance(stored_state_canon, str) and canon(state) == stored_state_canon,
        "current MAIN state canonical drift")
    req(state["current_exact_frontier"]["authoritative_remaining_terminals"] ==
        157570677819451133507, "current MAIN authority drift")
    req(state["current_exact_frontier"]["full178_numerical_census_complete"] is False,
        "FULL178 completion overclaim")
    req(state["firewalls"]["merge_authorized"] is False, "merge firewall")

    for label, (rel, expected) in LOCAL_LOCKS.items():
        path = ROOT / rel
        req(path.is_file(), "missing local source " + label)
        req(blob(path) == expected, "local source drift " + label)

    rev = subprocess.run(
        ["git", "-C", str(lane), "rev-parse", "HEAD"],
        check=True, text=True, capture_output=True,
    ).stdout.strip()
    req(rev == LANE178_HEAD, "live 178 source head drift")
    for label, (rel, expected) in LANE178_LOCKS.items():
        path = lane / rel
        req(path.is_file(), "missing 178 source " + label)
        req(blob(path) == expected, "178 source drift " + label)

    # Re-run the exact 178 Picard image-lattice producer.  It proves that the
    # 12 retained observables are exact integral linear forms on Picard64 and
    # gives exact HNF membership for their image.
    src = lane / LANE178_LOCKS["aggregate_picard_preflight"][0]
    cp = subprocess.run(
        ["python", str(src)],
        cwd=lane, check=True, text=True, capture_output=True,
    )
    cert = json.loads(cp.stdout)
    req(cert["observable_order"] == OBS, "178 replay observable order")
    req(cert["rule_is_exact_for_linear_picard_lattice_extendability"] is True,
        "178 Picard image rule not exact")
    full = cert["full_observable_image_lattice"]
    req(full["rank"] == 12, "178 full observable rank")
    req(full["observable_order"] == OBS, "178 full observable order")
    req(full["image_lattice_index_in_Zm"] >= 1, "invalid image-lattice index")

    btva = json.loads((ROOT / LOCAL_LOCKS["btva_diagnostic"][0]).read_text(encoding="utf-8"))
    nec = btva["theorem_source"]["necessary_conditions"]
    req(nec["genus0_nonconic"] ==
        "other than van Luijk's 32 plane conics, passes through at least seven singularities that span P^6",
        "BTVA genus0 nonconic statement drift")
    req(btva["receiver_scope"]["target"] == "R29-LG2 numerical unibranch FULL178 only",
        "BTVA receiver scope drift")

    blocker = json.loads((ROOT / LOCAL_LOCKS["old_support_blocker"][0]).read_text(encoding="utf-8"))
    req(blocker["status"] == "BLOCKED_RETAINED_INTERFACE_MISSING_EXACT_48_SUPPORT_WITNESS",
        "historical blocker status drift")
    req(blocker["minimal_reentry"][2].startswith("Theorem alternative:"),
        "historical support-invariance alternative drift")

    node = json.loads((ROOT / LOCAL_LOCKS["runtime_node_bridge"][0]).read_text(encoding="utf-8"))
    rows = node["rows"]
    req(len(rows) == 48, "node bridge row count")
    req([int(r["runtime_index_0based"]) for r in rows] == list(range(48)),
        "node runtime index order")
    req([int(r["retained_exceptional_index_0based"]) for r in rows] == list(range(48)),
        "node exceptional index order")
    nodes = node_matrix(rows)
    req(nodes.shape == (48, 7), "node coordinate matrix shape")
    req(int(nodes.rank()) == 7, "48-node configuration does not span P6")

    # Exact linear-algebra regression for the lazy-flat separator.  A proper
    # span closure F has rank < 7.  Any rank-7 support must include a node
    # outside F, hence sum(outside exceptional pairings)>=1 is a necessary cut.
    basis = independent_basis_indices(nodes)
    req(len(basis) == 7 and int(nodes[basis, :].rank()) == 7, "failed to recover node basis")
    checked = 0
    for depth in range(1, 7):
        seed = basis[:depth]
        F = closure_indices(nodes, seed)
        req(int(nodes[F, :].rank()) == depth, f"closure rank drift depth={depth}")
        req(len(F) < 48, f"proper closure became whole configuration depth={depth}")
        req(any(i not in F for i in basis), f"rank-7 basis trapped in proper closure depth={depth}")
        checked += 1

    arsenal = (ROOT / LOCAL_LOCKS["stage34_arsenal"][0]).read_text(encoding="utf-8")
    req("S34-W03 — receiver-restricted intersection exclusion" in arsenal,
        "S34-W03 router source drift")
    req("B(Q) intersect K(Q) = empty" in arsenal,
        "S34-W03 intersection semantics drift")

    req(p["ownership"]["bridge_issue1817_p0_p1_p2_duplicated"] is False,
        "Bridge ownership overlap")
    req(p["relation_to_old_blocker"]["support_invariance_theorem_required"] is False,
        "old support-invariance blocker reintroduced")

    print("PASS: live 178 exposes exact rank-12 compressed Picard observable image")
    print("PASS: historical BC2 node map binds all 48 exceptional slots to exact Q(i) nodes")
    print(f"PASS: lazy proper-flat separation checked on {checked} exact closure ranks; no eager hyperplane table required")
    print("PASS: compressed BTVA lift-intersection route bypasses per-terminal 59D/support materialization structurally")
    print("PASS: zero MAIN/receiver/theorem credit; bounded genus-0 real-production execution remains the next gate")


if __name__ == "__main__":
    main()
