#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

WIDTH = 113
WAVES = ("CUT193", "CUT194", "CUT195", "CUT196", "CUT197", "CUT198")
ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
FIXED_LABELS = [label for label in ASSIGNMENT_ORDER if label != 49]
GROUPS = [[101, 102, 103], [97, 98, 99], [93, 94, 95, 96]]
EXPECTED = {
    "n391_result_blob": "3e72cea011e5a519173a710c20d88bc781c4cee8",
    "n391_result_canonical": "2b30f97aca0873568c324cf9a88ba6dc8ee0e3cceb29e1fc60e9e2c978b02da3",
    "n391_audit_blob": "5c080d67b1f1c90792fa29e5d5ded71fbc4ea45b",
    "n391_audit_canonical": "5ce24718a7cb9c3975eb6d8cc1c84e8b1d51f2a04d8745691bdc2281cdb4b11c",
    "n391_audit_head": "f81d86498324fef2b9601933469a57dd49c72cb8",
    "n391_audit_review": 5193577864,
    "n393_audit_blob": "ae7fab165f5d04730d17cfbc51ae36141acd867e",
    "n393_audit_canonical": "20738e4e83f3fd231bf258eb43677b9cfcd15772beaa449d5044d0a407522cfe",
    "n393_audit_head": "d7f9deb5bfae4e41a4eb8eadb9ce4b715101670d",
    "n393_audit_review": 5193738942,
    "indexer_blob": "4fb0a8dd34909494bd62646373e42877ed7a3c9e",
    "family_blob": "90ff82ed312dcc0cb32cf207935945f550e29170",
    "n357_verifier_blob": "fdca9ad629983d8c31c7e6355540af3545910120",
}


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def checked(path: Path, expected_blob: str, expected_canonical: str) -> dict:
    req(path.is_file(), f"missing source: {path}")
    req(blob(path) == expected_blob, f"blob drift: {path}")
    obj = json.loads(path.read_text())
    body = dict(obj)
    claimed = body.pop("canonical_sha256_without_this_field", None)
    req(claimed == expected_canonical and csha(body) == expected_canonical, f"canonical drift: {path}")
    return obj


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def rank_q(rows: list[list[int]]) -> int:
    if not rows:
        return 0
    a = [[Fraction(v) for v in row] for row in rows]
    r = 0
    cols = len(a[0])
    for c in range(cols):
        pivot = next((i for i in range(r, len(a)) if a[i][c] != 0), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][c]
        a[r] = [v / p for v in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c] != 0:
                f = a[i][c]
                a[i] = [x - f * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def rank_mod(rows: list[list[int]], p: int) -> int:
    if not rows:
        return 0
    a = [[v % p for v in row] for row in rows]
    r = 0
    cols = len(a[0])
    for c in range(cols):
        pivot = next((i for i in range(r, len(a)) if a[i][c] % p), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [(v * inv) % p for v in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c] % p:
                f = a[i][c] % p
                a[i] = [(x - f * y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def affine_ranks(rows: list[list[int]]) -> dict[str, int]:
    augmented = [[1] + row for row in rows]
    return {
        "Q": rank_q(augmented) - 1,
        "GF2": rank_mod(augmented, 2) - 1,
        "GF3": rank_mod(augmented, 3) - 1,
    }


def common_affine_relation_dimensions(rows: list[list[int]]) -> dict[str, int]:
    augmented = [[1] + row for row in rows]
    ncols = len(augmented[0])
    return {
        "Q": ncols - rank_q(augmented),
        "GF2": ncols - rank_mod(augmented, 2),
        "GF3": ncols - rank_mod(augmented, 3),
    }


def integer_stream_sha(values: list[int]) -> str:
    return hashlib.sha256("".join(f"{v}\n" for v in values).encode()).hexdigest()


def signature_stream_sha(rows: list[list[int]]) -> str:
    return hashlib.sha256("".join(",".join(map(str, row)) + "\n" for row in rows).encode()).hexdigest()


def main() -> None:
    repo = Path(__file__).resolve().parents[5]
    residual = repo / "stages/stage32/residual-32-01-production"
    idx_path = residual / "compressed_terminal_indexer.py"
    fam_path = residual / "compressed_terminal_family.py"
    n357_path = repo / "stages/stage32/verify_n357_v13_current_authority_composition.py"
    req(blob(idx_path) == EXPECTED["indexer_blob"], "indexer blob drift")
    req(blob(fam_path) == EXPECTED["family_blob"], "family blob drift")
    req(blob(n357_path) == EXPECTED["n357_verifier_blob"], "N357 verifier blob drift")

    n391 = checked(
        repo / "stages/stage32/32-01-178/nodes/N391/RESULT.json",
        EXPECTED["n391_result_blob"],
        EXPECTED["n391_result_canonical"],
    )
    audit391 = checked(
        repo / "stages/stage32/32-01-178/nodes/N391/AUDIT-PASS.json",
        EXPECTED["n391_audit_blob"],
        EXPECTED["n391_audit_canonical"],
    )
    req(audit391["status"] == "HOSTILE_AUDIT_PASS", "N391 audit status drift")
    req(audit391["audited_exact_head"] == EXPECTED["n391_audit_head"], "N391 audit head drift")
    req(int(audit391["review_id"]) == EXPECTED["n391_audit_review"], "N391 audit review drift")

    audit393 = checked(
        repo / "stages/stage32/32-01-178/nodes/N393/AUDIT-PASS.json",
        EXPECTED["n393_audit_blob"],
        EXPECTED["n393_audit_canonical"],
    )
    req(audit393["status"] == "HOSTILE_AUDIT_PASS_RETAINED", "N393 audit status drift")
    req(audit393["audited_exact_head"] == EXPECTED["n393_audit_head"], "N393 audit head drift")
    req(int(audit393["hostile_audit_review_id"]) == EXPECTED["n393_audit_review"], "N393 audit review drift")

    sys.path.insert(0, str(residual))
    from compressed_terminal_indexer import CompressedTerminalIndexer

    idx = CompressedTerminalIndexer(8, 8)
    req(idx.normal_budget + 1 == WIDTH, "width drift")
    n357 = load_module(n357_path, "n394_n357")
    req(n357.ASSIGNMENT_ORDER == ASSIGNMENT_ORDER, "assignment order drift")

    survivors: list[int] = []
    for block in range(idx.exceptional_count):
        base = tuple(int(v) for v in idx.unrank(block * WIDTH))
        if n357.prefix_survives(base):
            survivors.append(block)

    block_wave: dict[int, str] = {}
    blocks: list[int] = []
    for wave in WAVES:
        for b in map(int, n391["waves"][wave]["residual_blocks"]):
            req(b not in block_wave, f"duplicate N391 block: {b}")
            block_wave[b] = wave
            blocks.append(b)
    req(len(blocks) == 97 and len(set(blocks)) == 97, "N391 residual union drift")

    entries = []
    mass = Counter()
    abc = Counter()
    g3 = Counter()
    bmc = Counter()
    wave_counts = Counter()
    by_mass_rows: dict[int, list[list[int]]] = defaultdict(list)
    signature_rows: list[list[int]] = []
    survivor_offsets: list[int] = []

    for block in blocks:
        base = list(map(int, idx.unrank(block * WIDTH)))
        req(base[4] == 0 and idx.rank(tuple(base)) == block * WIDTH, f"base drift: {block}")
        req(n357.prefix_survives(tuple(base)) and n357.n357_accepts(tuple(base)), f"N357 drift: {block}")
        by = dict(zip(ASSIGNMENT_ORDER, base))
        signature10 = [by[label] for label in FIXED_LABELS]
        fixed_mass = sum(signature10)
        sums = [sum(by[label] for label in group) for group in GROUPS]
        offset = survivors.index(block)
        entries.append({
            "block": block,
            "wave": block_wave[block],
            "survivor_offset": offset,
            "fixed_mass": fixed_mass,
            "abc": sums,
            "g3_sum": sums[2],
            "b_minus_c": sums[1] - sums[2],
            "base_signature10": signature10,
        })
        signature_rows.append(signature10)
        survivor_offsets.append(offset)
        by_mass_rows[fixed_mass].append(signature10)
        mass[fixed_mass] += 1
        abc[tuple(sums)] += 1
        g3[sums[2]] += 1
        bmc[sums[1] - sums[2]] += 1
        wave_counts[block_wave[block]] += 1

    req(len(entries) == 97, "entry count drift")
    req(len({tuple(r) for r in signature_rows}) == 97, "signature uniqueness drift")
    req(dict(sorted(mass.items())) == {2: 2, 3: 15, 4: 37, 5: 30, 6: 13}, "mass distribution drift")
    req(all(0 <= e["survivor_offset"] < len(survivors) for e in entries), "survivor offset drift")

    global_affine = affine_ranks(signature_rows)
    global_relation_dims = common_affine_relation_dimensions(signature_rows)
    per_mass = {}
    for m in sorted(by_mass_rows):
        rows = by_mass_rows[m]
        per_mass[str(m)] = {
            "count": len(rows),
            "affine_rank": affine_ranks(rows),
            "common_affine_relation_dimension": common_affine_relation_dimensions(rows),
        }

    payload = {
        "semantics": "BOUNDED_N391_97_BLOCK_CROSS_MASS_AFFINE_SIGNATURE_PROBE_ONLY_NOT_SOLVER_EQUIVALENCE_NOT_GLOBAL_OBSTRUCTION",
        "entry_count": 97,
        "identity_count": 97 * WIDTH,
        "signature_coordinate_labels": FIXED_LABELS,
        "signature_dimension": 10,
        "exact_base_signature_unique_count": 97,
        "fixed_mass_distribution": {str(k): v for k, v in sorted(mass.items())},
        "wave_distribution": {k: wave_counts[k] for k in WAVES},
        "global_affine_rank": global_affine,
        "global_common_affine_relation_dimension": global_relation_dims,
        "per_mass_structure": per_mass,
        "abc_class_count": len(abc),
        "g3_distribution": {str(k): v for k, v in sorted(g3.items())},
        "b_minus_c_distribution": {str(k): v for k, v in sorted(bmc.items())},
        "block_stream_sha256": integer_stream_sha(blocks),
        "survivor_offset_stream_sha256": integer_stream_sha(survivor_offsets),
        "signature10_stream_sha256": signature_stream_sha(signature_rows),
        "family_level_claim_promoted": False,
        "common_unsat_claim_promoted": False,
        "symbolic_obstruction_claim_promoted": False,
        "main_handoff_required": False,
        "additional_pruning_terminals": 0,
        "numerical_leaf_compression_credit": False,
        "heavy_compute_authorized": False,
        "merge_authorized": False,
    }
    print("PASS_N394_CROSS_MASS_AFFINE_STRUCTURE_PROBE")
    print(
        "global_affine_rank="
        + ",".join(f"{k}:{global_affine[k]}" for k in ("Q", "GF2", "GF3"))
        + " relation_dim="
        + ",".join(f"{k}:{global_relation_dims[k]}" for k in ("Q", "GF2", "GF3"))
    )
    print(
        "mass_distribution="
        + ",".join(f"{k}:{mass[k]}" for k in sorted(mass))
        + f" signatures=97 identities={97 * WIDTH}"
    )
    print("N394_PROBE_JSON=" + json.dumps(payload, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
