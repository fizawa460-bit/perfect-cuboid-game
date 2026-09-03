#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EXPECTED_CANONICAL = "919f8bed23fc07a8bd39907c1d348f7e3b7535cee0dd64642aa600ab793f633b"
EXPECTED_V6_CANONICAL = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
EXPECTED_PAIRINGS_SHA = "4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3"
EXPECTED_ODD_BRANCH_BLOB = "cb20a9b287430c2e238f79d3151500c262905468"
EXPECTED_COMMON_COVER = "eb31183bf519fec4ad5bb2d0799b3f0a64b7af893308e09ce0c33119b63440a1"
EXPECTED_NODE_ACTION = "d03cfe8c77614943e8d4ab190c046b801bb90aa18f5bb648973bda0a5300c269"
EXPECTED_BOUNDS = {"u": 1360, "v": 1796, "uv": 1452}
EXPECTED_C_BOUNDS = {"u": 680, "v": 898, "uv": 726}


def csha(x: object) -> str:
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def load_canonical(path: Path) -> tuple[dict, str]:
    raw = json.loads(path.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if csha(raw) != claimed:
        raise SystemExit(f"canonical mismatch: {path}")
    return raw, claimed


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", type=Path, required=True)
    args = ap.parse_args()

    v6, v6canon = load_canonical(ROOT / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json")
    if v6canon != EXPECTED_V6_CANONICAL:
        raise SystemExit("V6 canonical moved")
    pairings = [int(x) for x in v6["witness"]["all140_pairings"]]
    pairings_sha = hashlib.sha256(json.dumps(pairings, separators=(",", ":")).encode()).hexdigest()
    if pairings_sha != EXPECTED_PAIRINGS_SHA or v6["witness"]["all140_pairings_sha256"] != EXPECTED_PAIRINGS_SHA:
        raise SystemExit("V6 all140 pairings moved")
    mult = pairings[-48:]
    if len(mult) != 48 or sum(mult) != 266 or sum(x > 0 for x in mult) != 47 or [93+i for i,x in enumerate(mult) if x == 0] != [98]:
        raise SystemExit("exceptional multiplicity vector regression")

    odd_note = HERE / "post1473-specific-class-multibranch-beauville-odd-branch-wall.md"
    if git_blob_sha1(odd_note) != EXPECTED_ODD_BRANCH_BLOB:
        raise SystemExit("Beauville odd-branch source note moved")
    note = odd_note.read_text()
    required_phrases = [
        "sum_P m_P = C.E = e = 266",
        "sum of the `m_P` over points lying on `E_j` equals the locked exact intersection number `C.E_j`",
        "double cover `Xtilde -> Btilde` is ramified along the exceptional divisor",
        "local equation `y^2=t^m*unit`",
    ]
    if any(s not in note for s in required_phrases):
        raise SystemExit("Beauville local-contact source statement moved")

    _, common = load_canonical(HERE / "post1484-o210-q4-common-double-cover-cartesian-identity.json")
    if common != EXPECTED_COMMON_COVER:
        raise SystemExit("common double-cover canonical moved")
    node, nodecanon = load_canonical(HERE / "post1490-o210-q4-bolza-x-relative-h-marked-node-action.json")
    if nodecanon != EXPECTED_NODE_ACTION:
        raise SystemExit("relative-H node action canonical moved")
    perms = node["marked_node_action"]["nonidentity_permutations_images_of_93_to_140"]

    mm = {93+i: mult[i] for i in range(48)}
    bounds = {}
    for name in ("u", "v", "uv"):
        p = [int(x) for x in perms[name]]
        if len(p) != 48:
            raise SystemExit(f"node action length moved for {name}")
        bounds[name] = sum(mm[j] * mm[p[j-93]] for j in range(93,141))
    if bounds != EXPECTED_BOUNDS:
        raise SystemExit(f"marked local intersection bounds moved: {bounds}")
    cbounds = {k: v // 2 for k,v in bounds.items()}
    if any(v % 2 for v in bounds.values()) or cbounds != EXPECTED_C_BOUNDS:
        raise SystemExit("c_t marked lower bounds moved")
    if sum(cbounds.values()) != 2304 or 8586 - sum(cbounds.values()) != 6282:
        raise SystemExit("defect consequence arithmetic moved")

    cert, claimed = load_canonical(args.check)
    if claimed != EXPECTED_CANONICAL:
        raise SystemExit("local multiplicity adapter canonical moved")
    if cert["exact_multiplicity_vector"]["values"] != mult:
        raise SystemExit("certificate multiplicity vector differs from V6 last48")
    if cert["deck_local_intersection"]["ordered_marked_node_lower_bounds_D_dot_tD"] != bounds:
        raise SystemExit("certificate D.t(D) lower bounds differ from replay")
    if cert["deck_local_intersection"]["c_t_lower_bounds"] != cbounds:
        raise SystemExit("certificate c_t lower bounds differ from replay")
    if cert["decision"]["individual_D_dot_tD_exact"]:
        raise SystemExit("exact D.t(D) claimed from marked lower bounds")
    if cert["defect_consequence"]["O210_excluded"]:
        raise SystemExit("O210 excluded too early")

    print(json.dumps({
        "verdict": "PASS_EXACT_X_LOCAL_MULTIPLICITY_ADAPTER",
        "canonical_sha256": claimed,
        "multiplicity_sum": sum(mult),
        "D_dot_tD_marked_lower_bounds": bounds,
        "c_t_lower_bounds": cbounds,
        "sum_c_t_lower_bound": sum(cbounds.values()),
        "delta_D_upper_bound": 6282,
        "O210_excluded": False,
        "next_exact_leaf": cert["decision"]["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
