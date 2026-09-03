#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EXPECTED_CANONICAL = "d03cfe8c77614943e8d4ab190c046b801bb90aa18f5bb648973bda0a5300c269"
EXPECTED_MARKING = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
EXPECTED_INCIDENCE = "efdecb5d5cef219fc39d931521cbc1890a4830b5296e3c6ff7e93ccb6fa6b143"
EXPECTED_DIAGNOSTIC_BLOB = "78b0f55490af271b0124a5e319c60b508408aa37"
EXPECTED_PERMS = {
    "u": [95,96,93,94,99,100,97,98,104,103,102,101,108,107,106,105,110,109,112,111,114,113,116,115,124,123,122,121,120,119,118,117,131,132,129,130,127,128,125,126,134,133,136,135,138,137,140,139],
    "v": [96,95,94,93,100,99,98,97,103,104,101,102,107,108,105,106,111,112,109,110,115,116,113,114,118,117,120,119,122,121,124,123,126,125,128,127,130,129,132,131,139,140,137,138,135,136,133,134],
    "uv": [94,93,96,95,98,97,100,99,102,101,104,103,106,105,108,107,112,111,110,109,116,115,114,113,123,124,121,122,119,120,117,118,132,131,130,129,128,127,126,125,140,139,138,137,136,135,134,133],
}


def csha(x: object) -> str:
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(p[q[i] - 1] for i in range(len(p)))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", type=Path, required=True)
    args = ap.parse_args()

    diagnostic = HERE / "diagnose_stage32_post1490_o210_q4_x_relative_h_node_action.py"
    if git_blob_sha1(diagnostic) != EXPECTED_DIAGNOSTIC_BLOB:
        raise SystemExit("relative-H node diagnostic blob moved")

    marking_path = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"
    marking = load_module(marking_path, "s32_relative_h_cert_marking").load()
    if marking.get("canonical_sha256") != EXPECTED_MARKING:
        raise SystemExit("retained marking canonical moved")
    pp = [tuple(int(x) for x in p) for p in marking["aut_action"]["permutations_1based"]]
    if len(pp) != 9:
        raise SystemExit("retained automorphism generator count moved")
    ident = tuple(range(1, 141))
    if any(len(p) != 140 or tuple(sorted(p)) != ident for p in pp):
        raise SystemExit("retained automorphism permutation shape moved")

    incidence = json.loads((HERE / "post1473-x8-marked-exceptional-incidence.json").read_text())
    claimed_inc = incidence.pop("canonical_sha256_without_this_field")
    if claimed_inc != EXPECTED_INCIDENCE or csha(incidence) != claimed_inc:
        raise SystemExit("marked exceptional incidence moved")
    fibers: dict[str, set[int]] = {}
    for r in incidence["rows"]:
        key = f'{r["first_factor_boundary_label"]}:{r["second_factor_boundary_label"]}'
        fibers.setdefault(key, set()).add(int(r["exceptional_label"]))
    if len(fibers) != 12 or any(len(s) != 4 for s in fibers.values()):
        raise SystemExit("marked 12x4 node partition moved")

    g7, g8, g9 = pp[6], pp[7], pp[8]
    deck = {"u": compose(g7, g9), "v": compose(g7, g8), "uv": compose(g8, g9)}
    if any(compose(p, p) != ident for p in deck.values()):
        raise SystemExit("relative-H generator ceased to be involutive")
    if compose(deck["u"], deck["v"]) != deck["uv"] or compose(deck["v"], deck["u"]) != deck["uv"]:
        raise SystemExit("relative-H actions ceased to form V4")
    exc = list(range(93, 141))
    got = {name: [p[j - 1] for j in exc] for name, p in deck.items()}
    if got != EXPECTED_PERMS:
        raise SystemExit("relative-H marked-node permutation moved")
    for name, p in deck.items():
        if any(p[j - 1] == j for j in exc):
            raise SystemExit(f"relative-H action {name} acquired a fixed marked node")
        for key, nodes in fibers.items():
            if {p[j - 1] for j in nodes} != nodes:
                raise SystemExit(f"relative-H action {name} moved marked fiber {key}")
    for key, nodes in fibers.items():
        j = min(nodes)
        if {j, deck["u"][j - 1], deck["v"][j - 1], deck["uv"][j - 1]} != nodes:
            raise SystemExit(f"marked fiber {key} ceased to be a regular H torsor")

    raw = json.loads(args.check.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if claimed != EXPECTED_CANONICAL or csha(raw) != claimed:
        raise SystemExit("relative-H marked-node certificate canonical mismatch")
    if raw["marked_node_action"]["nonidentity_permutations_images_of_93_to_140"] != EXPECTED_PERMS:
        raise SystemExit("certificate node permutations differ from replay")
    if raw["interpretation"]["picB_to_picX_divisor_action_claimed"]:
        raise SystemExit("forbidden Pic(B)->Pic(X) claim entered certificate")
    if raw["interpretation"]["exceptional_mass_is_local_D_multiplicity_claimed"]:
        raise SystemExit("local multiplicity promoted before adapter")
    if raw["decision"]["O210_excluded"]:
        raise SystemExit("O210 exclusion claimed too early")

    print(json.dumps({
        "verdict": "PASS_EXACT_RELATIVE_H_MARKED_NODE_ACTION",
        "canonical_sha256": claimed,
        "marked_nodes": 48,
        "regular_H_fibers": 12,
        "individual_D_dot_tD_known": False,
        "next_exact_leaf": raw["decision"]["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
