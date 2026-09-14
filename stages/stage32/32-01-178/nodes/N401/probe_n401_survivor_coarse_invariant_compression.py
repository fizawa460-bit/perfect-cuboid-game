#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

WIDTH = 113
WAVES = ("CUT193", "CUT194", "CUT195", "CUT196", "CUT197", "CUT198")
ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
FIXED_LABELS = [label for label in ASSIGNMENT_ORDER if label != 49]
GROUPS = [[101, 102, 103], [97, 98, 99], [93, 94, 95, 96]]
COARSE_FIELDS = ("mass", "a", "b", "c", "b_minus_c", "wave")
EXPECTED = {
    "n400_audit_blob": "bc9b3548e2af2cc29844f23b3980618cbb446b3e",
    "n400_audit_canonical": "d287af8f43db33d1ae6e0bf469b45a49e24928b9d286fd11a37e72642c6161cf",
    "n400_audited_head": "b1a950cbc6edf3cb85e1ea79473105c6f1f67b03",
    "n400_review": 5203374607,
    "n399_audit_blob": "590ce4b0645455815e1cbb67cbc9a0b35299c0c8",
    "n399_audit_canonical": "a53747a12698afe255e06bee9d243cd5e46747b02a33293c79b4204b8392275c",
    "n391_result_blob": "3e72cea011e5a519173a710c20d88bc781c4cee8",
    "n391_result_canonical": "2b30f97aca0873568c324cf9a88ba6dc8ee0e3cceb29e1fc60e9e2c978b02da3",
    "n391_audit_blob": "5c080d67b1f1c90792fa29e5d5ded71fbc4ea45b",
    "n391_audit_canonical": "5ce24718a7cb9c3975eb6d8cc1c84e8b1d51f2a04d8745691bdc2281cdb4b11c",
    "n394_audit_blob": "0227d9e1da87e6d9ea579d09a35a2db5fa13f568",
    "n394_audit_canonical": "8d2db62de7defea8fc02d6f32cfbab9165f92b08c327f687d430d15ef2729786",
    "indexer_blob": "4fb0a8dd34909494bd62646373e42877ed7a3c9e",
    "family_blob": "90ff82ed312dcc0cb32cf207935945f550e29170",
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
    req(claimed == expected_canonical, f"stored canonical drift: {path}")
    req(csha(body) == expected_canonical, f"canonical drift: {path}")
    return obj


def stream_sha(values: list[object]) -> str:
    return hashlib.sha256("".join(json.dumps(v, sort_keys=True, separators=(",", ":")) + "\n" for v in values).encode()).hexdigest()


def key_for(entry: dict, fields: tuple[str, ...]) -> tuple:
    return tuple(entry[f] for f in fields)


def classify(entries: list[dict], fields: tuple[str, ...]) -> dict:
    groups: dict[tuple, list[dict]] = defaultdict(list)
    for entry in entries:
        groups[key_for(entry, fields)].append(entry)
    conflicts = 0
    max_parities = 0
    for rows in groups.values():
        ps = {int(row["required_x49_parity"]) for row in rows}
        max_parities = max(max_parities, len(ps))
        if len(ps) > 1:
            conflicts += 1
    return {
        "fields": list(fields),
        "class_count": len(groups),
        "conflicting_class_count": conflicts,
        "determines_required_parity": conflicts == 0,
        "nontrivial_block_compression": conflicts == 0 and len(groups) < len(entries),
        "max_parities_per_class": max_parities,
    }


def main() -> None:
    repo = Path(__file__).resolve().parents[5]
    node_root = repo / "stages/stage32/32-01-178/nodes"
    residual = repo / "stages/stage32/residual-32-01-production"

    audit400 = checked(node_root / "N400/AUDIT-PASS.json", EXPECTED["n400_audit_blob"], EXPECTED["n400_audit_canonical"])
    audit399 = checked(node_root / "N399/AUDIT-PASS.json", EXPECTED["n399_audit_blob"], EXPECTED["n399_audit_canonical"])
    n391 = checked(node_root / "N391/RESULT.json", EXPECTED["n391_result_blob"], EXPECTED["n391_result_canonical"])
    audit391 = checked(node_root / "N391/AUDIT-PASS.json", EXPECTED["n391_audit_blob"], EXPECTED["n391_audit_canonical"])
    audit394 = checked(node_root / "N394/AUDIT-PASS.json", EXPECTED["n394_audit_blob"], EXPECTED["n394_audit_canonical"])

    req(audit400["hostile_audit_verdict"] == "PASS", "N400 audit verdict drift")
    req(audit400["audited_exact_head"] == EXPECTED["n400_audited_head"], "N400 audited head drift")
    req(int(audit400["hostile_audit_review_id"]) == EXPECTED["n400_review"], "N400 review drift")
    req(audit400["bounded_result"]["survivor_terminal_count"] == 5459, "N400 survivor count drift")
    req(audit400["bounded_result"]["main_authority_subtraction_performed"] is False, "N400 unexpectedly consumed MAIN")
    req(audit399["hostile_audit_verdict"] == "PASS", "N399 audit verdict drift")
    req(audit399["bounded_result"]["terminal_predicate"] == "(x49 + x98) mod 2 = 1", "N399 predicate drift")
    req(audit391["status"] in ("HOSTILE_AUDIT_PASS", "HOSTILE_AUDIT_PASS_RETAINED"), "N391 audit drift")
    req(audit394["hostile_audit_verdict"] == "PASS", "N394 audit drift")

    idx_path = residual / "compressed_terminal_indexer.py"
    fam_path = residual / "compressed_terminal_family.py"
    req(blob(idx_path) == EXPECTED["indexer_blob"], "indexer blob drift")
    req(blob(fam_path) == EXPECTED["family_blob"], "family blob drift")
    sys.path.insert(0, str(residual))
    from compressed_terminal_indexer import CompressedTerminalIndexer

    idx = CompressedTerminalIndexer(8, 8)
    req(idx.normal_budget + 1 == WIDTH, "terminal width drift")

    blocks: list[int] = []
    block_wave: dict[int, str] = {}
    for wave in WAVES:
        for b in map(int, n391["waves"][wave]["residual_blocks"]):
            req(b not in block_wave, f"duplicate residual block {b}")
            blocks.append(b)
            block_wave[b] = wave
    req(len(blocks) == 97 and len(set(blocks)) == 97, "N391 residual block union drift")

    entries: list[dict] = []
    parity_counts = Counter()
    survivor_total = 0
    survivor_count_stream: list[int] = []
    parity_stream: list[int] = []

    for block in blocks:
        base = list(map(int, idx.unrank(block * WIDTH)))
        req(len(base) == len(ASSIGNMENT_ORDER), f"base width drift at block {block}")
        req(base[4] == 0, f"base x49 drift at block {block}")
        req(idx.rank(tuple(base)) == block * WIDTH, f"rank roundtrip drift at block {block}")
        by = dict(zip(ASSIGNMENT_ORDER, base))
        fixed = [by[label] for label in FIXED_LABELS]
        sums = [sum(by[label] for label in group) for group in GROUPS]
        required = (by[93] + by[96]) & 1
        reduced_required = (1 - by[98]) & 1
        req(required == reduced_required, f"N394/N399 parity relation drift at block {block}")
        survivors = sum(1 for x49 in range(WIDTH) if (x49 & 1) == required)
        req(survivors in (56, 57), f"unexpected survivor count at block {block}")
        parity_counts[required] += 1
        survivor_total += survivors
        survivor_count_stream.append(survivors)
        parity_stream.append(required)
        entries.append({
            "block": block,
            "wave": block_wave[block],
            "mass": sum(fixed),
            "a": sums[0],
            "b": sums[1],
            "c": sums[2],
            "b_minus_c": sums[1] - sums[2],
            "required_x49_parity": required,
            "survivor_terminal_count": survivors,
        })

    req(dict(sorted(parity_counts.items())) == {0: 27, 1: 70}, "required parity distribution drift")
    req(survivor_total == 5459, "N399 survivor total reconstruction drift")
    req(Counter(entry["mass"] for entry in entries) == Counter({2: 2, 3: 15, 4: 37, 5: 30, 6: 13}), "N394 mass distribution drift")

    classifications: list[dict] = []
    for r in range(1, len(COARSE_FIELDS) + 1):
        for fields in itertools.combinations(COARSE_FIELDS, r):
            classifications.append(classify(entries, fields))

    deterministic = [c for c in classifications if c["determines_required_parity"]]
    nontrivial = [c for c in deterministic if c["nontrivial_block_compression"]]
    nontrivial.sort(key=lambda c: (c["class_count"], len(c["fields"]), c["fields"]))
    deterministic.sort(key=lambda c: (len(c["fields"]), c["class_count"], c["fields"]))
    best = nontrivial[0] if nontrivial else None
    minimal_feature_count = len(deterministic[0]["fields"]) if deterministic else None
    minimal_feature_models = [c for c in deterministic if len(c["fields"]) == minimal_feature_count] if deterministic else []

    named_checks = {
        "mass": classify(entries, ("mass",)),
        "wave": classify(entries, ("wave",)),
        "abc": classify(entries, ("a", "b", "c")),
        "g3": classify(entries, ("c",)),
        "b_minus_c": classify(entries, ("b_minus_c",)),
        "mass_wave": classify(entries, ("mass", "wave")),
        "mass_g3": classify(entries, ("mass", "c")),
        "mass_b_minus_c": classify(entries, ("mass", "b_minus_c")),
    }

    by_mass_survivors = Counter()
    by_wave_survivors = Counter()
    by_mass_blocks = Counter()
    by_wave_blocks = Counter()
    for entry in entries:
        by_mass_survivors[entry["mass"]] += entry["survivor_terminal_count"]
        by_wave_survivors[entry["wave"]] += entry["survivor_terminal_count"]
        by_mass_blocks[entry["mass"]] += 1
        by_wave_blocks[entry["wave"]] += 1

    outcome = "COARSE_INVARIANT_PARITY_COMPRESSION_CANDIDATE" if best else "COARSE_INVARIANT_PARITY_COMPRESSION_NO_GO"
    payload = {
        "semantics": "EXACT_BOUNDED_N399_5459_SURVIVOR_COARSE_INVARIANT_COMPRESSION_PROBE_ON_RETAINED_N391_97_BLOCKS_ONLY",
        "source_block_count": 97,
        "source_terminal_count": 10961,
        "survivor_terminal_count": survivor_total,
        "rejected_terminal_count": 5502,
        "required_parity_block_distribution": {"even": parity_counts[0], "odd": parity_counts[1]},
        "survivor_count_by_fixed_mass": {str(k): by_mass_survivors[k] for k in sorted(by_mass_survivors)},
        "block_count_by_fixed_mass": {str(k): by_mass_blocks[k] for k in sorted(by_mass_blocks)},
        "survivor_count_by_wave": {wave: by_wave_survivors[wave] for wave in WAVES},
        "block_count_by_wave": {wave: by_wave_blocks[wave] for wave in WAVES},
        "named_coarse_models": named_checks,
        "deterministic_model_count": len(deterministic),
        "nontrivial_deterministic_model_count": len(nontrivial),
        "minimal_feature_count": minimal_feature_count,
        "minimal_feature_models": minimal_feature_models,
        "best_nontrivial_compression_model": best,
        "outcome": outcome,
        "block_stream_sha256": stream_sha(blocks),
        "required_parity_stream_sha256": stream_sha(parity_stream),
        "survivor_count_stream_sha256": stream_sha(survivor_count_stream),
        "same_97x8_parity_census_repeated": False,
        "terminal_reenumeration_of_n399_rank_stream": False,
        "main_authority_subtraction_performed": False,
        "additional_pruning_terminals": 0,
        "main_pruning_credit": False,
        "full178_complete": False,
        "heavy_compute_authorized": False,
        "merge_authorized": False,
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)

    print("PASS_N401_N399_SURVIVOR_COARSE_INVARIANT_COMPRESSION_PROBE")
    print(f"survivors={survivor_total} even_blocks={parity_counts[0]} odd_blocks={parity_counts[1]}")
    print("outcome=" + outcome)
    print("N401_PROBE_JSON=" + json.dumps(payload, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
