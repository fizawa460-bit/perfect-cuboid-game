#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT = HERE / "post1526-diagonal-theta-h-orbit-symmetry-negative.json"
CONTROLLER = ROOT / "stages/stage32/controller.json"
FSM_ADAPTER = HERE / "post1529-fsm-stoll-diagonal-action-source-lock.json"
H_DECK = HERE / "post1490-o210-q4-equivariant-beauville-deck-cross-exclusion.json"

EXPECTED_CANONICAL = "d34c3cb285cbef1732af6b9a837dbc2b2d9dd3eee19564eec2b78d15c399dc7b"
EXPECTED_FSM_ADAPTER_CANONICAL = "5726289d8948beaaf3ed4e2dc260f49d1b3b3054642f3460b6b1e53c77ea23bc"
EXPECTED_H_DECK_CANONICAL = "8c32735092671d725034de8d14d09c09ac275517fa5f0e225791d2fc53eb5bf3"
EXPECTED_BLOBS = {
    "stages/stage32/32-21/post1473-v6-witness-body-recovered.json": "dae90ed19395355bebeebe2a6aa6bb1c6e53c244",
    "stages/stage33/33-07/stage32_picard_marking_retained.py": "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7",
    "stages/stage32/residual-32-01-production/post1522-o210-q602-two-generator-centralizer-cm-norm-source-note.md": "10156b4f27e3598684980790bb034cf80afc969e",
    "stages/stage32/residual-32-01-production/post1529-fsm-stoll-diagonal-action-source-lock.json": "809d7096cf98cf94b37455b6281cb23cbdcc6b41",
    "stages/stage32/residual-32-01-production/post1490-o210-q4-equivariant-beauville-deck-cross-exclusion.json": "9cd6d7122b8a3149b8ab79396946d72b986649df",
    "stages/stage32/residual-32-01-production/post1526-diagonal-theta-h-orbit-symmetry-negative-source-note.md": "8d33f335e088a0b92ac10f6bf1af47ae1237991f",
    "stages/stage32/residual-32-01-production/diagnose_stage32_post1526_diagonal_theta_picard_equivariance.py": "4e42cbd226f7c2697d711679ffbd3c532801adba",
}


def canonical_sha(obj: dict) -> str:
    core = dict(obj)
    got = core.pop("canonical_sha256_without_this_field")
    calc = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    if got != calc:
        raise SystemExit(f"canonical mismatch: field={got} calc={calc}")
    return calc


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def compose_symbolic(action: list[str], generator: list[str], coords: list[str]) -> list[str]:
    gmap = dict(zip(coords, generator))
    out = []
    for expr in action:
        sign = -1 if expr.startswith("-") else 1
        var = expr[1:] if sign == -1 else expr
        repl = gmap[var]
        sign2 = -1 if repl.startswith("-") else 1
        var2 = repl[1:] if sign2 == -1 else repl
        out.append(("-" if sign * sign2 == -1 else "") + var2)
    return out


def symbolic_word_action(word: str, adapter: dict) -> list[str]:
    coords = adapter["coordinate_order"]
    gens = adapter["stoll_generators_used"]
    out = list(coords)
    for token in word.split("*"):
        if token not in gens:
            raise SystemExit(f"adapter word uses unpinned Stoll generator: {token}")
        out = compose_symbolic(out, gens[token], coords)
    return out


def main() -> None:
    cert = json.loads(CERT.read_text())
    if cert["schema"] != "STAGE32_POST1526_DIAGONAL_THETA_H_ORBIT_SYMMETRY_NEGATIVE_V1":
        raise SystemExit("certificate schema moved")
    if cert["status"] != "EXACT_BOUNDED_NEGATIVE_PENDING_HOSTILE_AUDIT":
        raise SystemExit("certificate lifecycle moved")
    if canonical_sha(cert) != EXPECTED_CANONICAL:
        raise SystemExit("certificate canonical moved")

    for rel, expected in EXPECTED_BLOBS.items():
        got = git_blob_sha(ROOT / rel)
        if got != expected:
            raise SystemExit(f"source-lock blob moved: {rel}: {got} != {expected}")

    adapter = json.loads(FSM_ADAPTER.read_text())
    if adapter["schema"] != "STAGE32_POST1529_FSM_STOLL_DIAGONAL_ACTION_SOURCE_LOCK_V1":
        raise SystemExit("FSM/Stoll adapter schema moved")
    if canonical_sha(adapter) != EXPECTED_FSM_ADAPTER_CANONICAL:
        raise SystemExit("FSM/Stoll adapter canonical moved")
    fsm_lock = adapter["source_locks"]["freitag_salvati_manni"]
    stoll_lock = adapter["source_locks"]["stoll_cuboids_magma"]
    if (
        fsm_lock["arxiv_version"],
        fsm_lock["locator"],
        stoll_lock["repository"],
        stoll_lock["commit"],
        stoll_lock["path"],
        stoll_lock["blob_sha1"],
    ) != (
        "1303.6495v1",
        "Section 2; theta-coordinate transformation formulas, restricted here to U=[[1,2],[0,1]] and S=[[0,-1],[1,0]]",
        "MichaelStollBayreuth/Verification",
        "51233ed5ef2bf228fac9416c66db9adc0ebcaadd",
        "Cuboids/cuboids.magma",
        "0422b69847f2afb97cb7b3ed02ebef91279f61b1",
    ):
        raise SystemExit("FSM/Stoll external source locator moved")

    expected_adapter_actions = {
        "U": {
            "matrix": [[1, 2], [0, 1]],
            "normalized_box_action": ["-a1", "-a2", "a3", "b1", "b2", "-b3", "c"],
            "stoll_word": "g4*g5*g9",
        },
        "S": {
            "matrix": [[0, -1], [1, 0]],
            "normalized_box_action": ["a3", "-a2", "a1", "b3", "b2", "b1", "c"],
            "stoll_word": "g2*g5",
        },
    }
    if adapter["fsm_section2_actions"] != expected_adapter_actions:
        raise SystemExit("two-action FSM adapter moved")
    for name, row in adapter["fsm_section2_actions"].items():
        got = symbolic_word_action(row["stoll_word"], adapter)
        if got != row["normalized_box_action"]:
            raise SystemExit(f"{name} adapter no longer reconstructs from pinned Stoll substitutions")

    hdeck = json.loads(H_DECK.read_text())
    if hdeck["schema"] != "STAGE32_POST1490_O210_Q4_EQUIVARIANT_BEAUVILLE_DECK_CROSS_EXCLUSION_V1":
        raise SystemExit("post1490 H-deck asset schema moved")
    if canonical_sha(hdeck) != EXPECTED_H_DECK_CANONICAL:
        raise SystemExit("post1490 H-deck asset canonical moved")
    hwords = hdeck["equivariant_adapter"]["modular_to_stoll"]
    if hwords != {"u": "g7*g9", "uv": "g8*g9", "v": "g7*g8"}:
        raise SystemExit("post1490 H-deck source map moved")

    source_locks = cert["source_locks"]
    if source_locks["fsm_stoll_action_adapter"] != {
        "path": "stages/stage32/residual-32-01-production/post1529-fsm-stoll-diagonal-action-source-lock.json",
        "blob_sha1": "809d7096cf98cf94b37455b6281cb23cbdcc6b41",
        "canonical_sha256": EXPECTED_FSM_ADAPTER_CANONICAL,
        "fsm_locator": "arXiv:1303.6495v1 Section 2",
        "stoll_locator": "MichaelStollBayreuth/Verification@51233ed5ef2bf228fac9416c66db9adc0ebcaadd: Cuboids/cuboids.magma blob 0422b69847f2afb97cb7b3ed02ebef91279f61b1",
    }:
        raise SystemExit("certificate FSM/Stoll source lock moved")
    if source_locks["post1490_h_deck_asset"] != {
        "path": "stages/stage32/residual-32-01-production/post1490-o210-q4-equivariant-beauville-deck-cross-exclusion.json",
        "blob_sha1": "9cd6d7122b8a3149b8ab79396946d72b986649df",
        "canonical_sha256": EXPECTED_H_DECK_CANONICAL,
    }:
        raise SystemExit("certificate H-deck source lock moved")

    finite = cert["finite_actions"]
    if finite["diagonal_generators"]["U"]["stoll_word"] != adapter["fsm_section2_actions"]["U"]["stoll_word"]:
        raise SystemExit("certificate U word disagrees with source adapter")
    if finite["diagonal_generators"]["S"]["stoll_word"] != adapter["fsm_section2_actions"]["S"]["stoll_word"]:
        raise SystemExit("certificate S word disagrees with source adapter")
    expected_h_cert = {"id": "1", "u": hwords["u"], "v": hwords["v"], "uv": hwords["uv"]}
    if finite["H_deck_translations"] != expected_h_cert:
        raise SystemExit("certificate H-deck words disagree with post1490 asset")

    target = cert["fixed_target"]
    if (target["row_id"], target["O"], target["qprime"], target["required_Q"]) != (
        "g1-d186", 210, 4, 602
    ):
        raise SystemExit("fixed O210/Q602 target moved")

    if finite["generated_group_order_on_all140"] != 8:
        raise SystemExit("diagonal theta group order moved")
    if finite["H_orbit_preserving_count"] != 1:
        raise SystemExit("H-orbit stabilizer count moved")
    if finite["H_orbit_preserving_words"] != ["1"]:
        raise SystemExit("nonidentity H-orbit stabilizer unexpectedly appeared")
    if finite["scalar_joint_centralizer_pair_exists"] is not False:
        raise SystemExit("scalar centralizer pair flag moved")

    expected_rows = [
        ("1", ["id"], [1, 0, 0, 1]),
        ("1S", [], [1, 1, 1, -1]),
        ("1U", [], [1, 0, 0, -1]),
        ("1SU", [], [1, -1, 1, 1]),
        ("1US", [], [1, 1, -1, 1]),
        ("1SUS", [], [0, 2, 2, 0]),
        ("1USU", [], [1, -1, -1, -1]),
        ("1USUS", [], [0, 2, -2, 0]),
    ]
    got_rows = [
        (row["word"], row["H_orbit_matches"], row["projective_differential_matrix"])
        for row in finite["enumeration"]
    ]
    if got_rows != expected_rows:
        raise SystemExit("finite enumeration certificate moved")

    decision = cert["decision"]
    if decision["result"] != "EXACT_BOUNDED_NEGATIVE" or not decision["route_closed"]:
        raise SystemExit("negative route decision moved")
    if any(
        decision[k]
        for k in ["O210_excluded", "Q602_excluded", "O212_plus_advance_allowed", "controller_change_authorized"]
    ):
        raise SystemExit("negative leaf illegally promotes Stage32 authority")

    fw = cert["firewalls"]
    if any(fw.values()):
        raise SystemExit("negative leaf firewall regression")

    controller = json.loads(CONTROLLER.read_text())
    ct = controller["fixed_target"]
    if controller.get("stage32_closed") is not False:
        raise SystemExit("controller unexpectedly closes Stage32")
    if (ct["row_id"], ct["O"], ct["qprime"], ct["Q"]) != ("g1-d186", 210, 4, 602):
        raise SystemExit("live controller O210/Q602 target moved")

    diag = HERE / "diagnose_stage32_post1526_diagonal_theta_picard_equivariance.py"
    proc = subprocess.run(["python3", str(diag)], cwd=ROOT, text=True, capture_output=True, check=True)
    out = proc.stdout
    required_lines = [
        "STAGE32_POST1529_DIAGONAL_THETA_PICARD_DIAGNOSTIC_V4",
        "source_locked_U_word=g4*g5*g9",
        "source_locked_S_word=g2*g5",
        "source_locked_H_words={'u': 'g7*g9', 'v': 'g7*g8', 'uv': 'g8*g9'}",
        "diag_theta_group_order_on_140=8",
        "word=1 H_orbit_matches=['id'] diff_matrix=(1, 0, 0, 1)",
        "word=1S H_orbit_matches=[] diff_matrix=(1, 1, 1, -1)",
        "word=1U H_orbit_matches=[] diff_matrix=(1, 0, 0, -1)",
        "word=1SU H_orbit_matches=[] diff_matrix=(1, -1, 1, 1)",
        "word=1US H_orbit_matches=[] diff_matrix=(1, 1, -1, 1)",
        "word=1SUS H_orbit_matches=[] diff_matrix=(0, 2, 2, 0)",
        "word=1USU H_orbit_matches=[] diff_matrix=(1, -1, -1, -1)",
        "word=1USUS H_orbit_matches=[] diff_matrix=(0, 2, -2, 0)",
        "H_orbit_preserving_count=1",
        "H_orbit_preserving_words=['1']",
        "scalar_joint_centralizer_pair_exists=False",
        "scalar_pair=None",
    ]
    missing = [line for line in required_lines if line not in out]
    if missing:
        raise SystemExit("diagnostic replay mismatch: " + repr(missing))

    print("PASS STAGE32_POST1529_DIAGONAL_THETA_H_ORBIT_SOURCELOCK_REPAIR_V1")
    print("canonical_sha256=" + EXPECTED_CANONICAL)
    print("source_locked_words=U:g4*g5*g9 S:g2*g5 u:g7*g9 v:g7*g8 uv:g8*g9")
    print("group_order=8 H_orbit_preserving_count=1 words=['1']")
    print("O210/Q602 remain OPEN; O212+ remains blocked; controller unchanged")


if __name__ == "__main__":
    main()
