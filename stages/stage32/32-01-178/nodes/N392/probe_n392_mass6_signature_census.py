#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

WIDTH = 113
EXPECTED = {
    "n391_result_blob": "3e72cea011e5a519173a710c20d88bc781c4cee8",
    "n391_result_canonical": "2b30f97aca0873568c324cf9a88ba6dc8ee0e3cceb29e1fc60e9e2c978b02da3",
    "n391_audit_blob": "5c080d67b1f1c90792fa29e5d5ded71fbc4ea45b",
    "n391_audit_canonical": "5ce24718a7cb9c3975eb6d8cc1c84e8b1d51f2a04d8745691bdc2281cdb4b11c",
    "n391_audit_head": "f81d86498324fef2b9601933469a57dd49c72cb8",
    "n391_audit_review": 5193577864,
    "indexer_blob": "4fb0a8dd34909494bd62646373e42877ed7a3c9e",
    "family_blob": "90ff82ed312dcc0cb32cf207935945f550e29170",
    "n357_verifier_blob": "fdca9ad629983d8c31c7e6355540af3545910120",
}
ASSIGNMENT_ORDER = [95,99,103,102,49,97,94,101,93,98,96]
GROUPS = [[101,102,103],[97,98,99],[93,94,95,96]]

def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(msg)

def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",",":"), ensure_ascii=False).encode()).hexdigest()

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

def main() -> None:
    repo = Path(__file__).resolve().parents[5]
    residual = repo / "stages/stage32/residual-32-01-production"
    idx_path = residual / "compressed_terminal_indexer.py"
    fam_path = residual / "compressed_terminal_family.py"
    n357_path = repo / "stages/stage32/verify_n357_v13_current_authority_composition.py"
    req(blob(idx_path) == EXPECTED["indexer_blob"], "indexer blob drift")
    req(blob(fam_path) == EXPECTED["family_blob"], "family blob drift")
    req(blob(n357_path) == EXPECTED["n357_verifier_blob"], "N357 verifier blob drift")

    n391 = checked(repo / "stages/stage32/32-01-178/nodes/N391/RESULT.json", EXPECTED["n391_result_blob"], EXPECTED["n391_result_canonical"])
    audit = checked(repo / "stages/stage32/32-01-178/nodes/N391/AUDIT-PASS.json", EXPECTED["n391_audit_blob"], EXPECTED["n391_audit_canonical"])
    req(audit["status"] == "HOSTILE_AUDIT_PASS" and audit["audited_exact_head"] == EXPECTED["n391_audit_head"] and int(audit["review_id"]) == EXPECTED["n391_audit_review"], "N391 hostile audit receipt drift")

    sys.path.insert(0, str(residual))
    from compressed_terminal_indexer import CompressedTerminalIndexer
    idx = CompressedTerminalIndexer(8,8)
    req(idx.normal_budget + 1 == WIDTH, "width drift")
    n357 = load_module(n357_path, "n392_n357")
    req(n357.ASSIGNMENT_ORDER == ASSIGNMENT_ORDER, "assignment order drift")

    survivors = []
    for block in range(idx.exceptional_count):
        base = tuple(int(v) for v in idx.unrank(block * WIDTH))
        if n357.prefix_survives(base):
            survivors.append(block)

    all_blocks = []
    for wave in ("CUT193","CUT194","CUT195","CUT196","CUT197","CUT198"):
        all_blocks.extend(map(int, n391["waves"][wave]["residual_blocks"]))
    req(len(all_blocks) == 97 and len(set(all_blocks)) == 97, "N391 residual union drift")

    entries = []
    reduced = Counter()
    g3 = Counter()
    for block in all_blocks:
        base = list(map(int, idx.unrank(block * WIDTH)))
        req(base[4] == 0 and idx.rank(tuple(base)) == block * WIDTH, f"base drift: {block}")
        req(n357.prefix_survives(tuple(base)) and n357.n357_accepts(tuple(base)), f"N357 drift: {block}")
        by = dict(zip(ASSIGNMENT_ORDER, base))
        fixed_mass = sum(v for label,v in by.items() if label != 49)
        if fixed_mass != 6:
            continue
        abc = [sum(by[label] for label in group) for group in GROUPS]
        signature10 = [v for i,v in enumerate(base) if i != 4]
        offset = survivors.index(block)
        entry = {
            "abc": abc,
            "b_minus_c": abc[1]-abc[2],
            "base_signature10": signature10,
            "block": block,
            "g3_sum": abc[2],
            "rank_range": [block*WIDTH, block*WIDTH+WIDTH-1],
            "survivor_offset": offset,
        }
        entries.append(entry)
        reduced[tuple(abc)] += 1
        g3[abc[2]] += 1

    req(len(entries) == 13, "mass6 count drift")
    payload = {
        "entry_count": len(entries),
        "exact_base_signature_unique_count": len({tuple(e["base_signature10"]) for e in entries}),
        "g3_distribution": {str(k):v for k,v in sorted(g3.items())},
        "mass6_blocks": [e["block"] for e in entries],
        "mass6_offsets": [e["survivor_offset"] for e in entries],
        "reduced_abc_signature_counts": {"%d,%d,%d" % k:v for k,v in sorted(reduced.items())},
        "entries": entries,
    }
    print("PASS_N392_MASS6_SIGNATURE_PROBE")
    print("N392_PROBE_JSON=" + json.dumps(payload, sort_keys=True, separators=(",",":")))

if __name__ == "__main__":
    main()
