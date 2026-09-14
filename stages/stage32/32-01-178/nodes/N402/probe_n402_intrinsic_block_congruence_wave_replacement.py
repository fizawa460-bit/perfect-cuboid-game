#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

WIDTH = 113
WAVES = ("CUT193", "CUT194", "CUT195", "CUT196", "CUT197", "CUT198")
ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
FIXED_LABELS = [label for label in ASSIGNMENT_ORDER if label != 49]
GROUPS = [[101, 102, 103], [97, 98, 99], [93, 94, 95, 96]]
MAX_MODULUS = 64
BASE_TRIPLES = (
    ("a", "b", "b_minus_c"),
    ("a", "b", "c"),
    ("a", "c", "b_minus_c"),
    ("mass", "a", "b"),
    ("mass", "a", "b_minus_c"),
    ("mass", "a", "c"),
    ("mass", "b", "b_minus_c"),
    ("mass", "b", "c"),
    ("mass", "c", "b_minus_c"),
)
EXPECTED = {
    "n401_audit_blob": "6a9ee07ae6a02c48da6aba7317864681bd9742c7",
    "n401_audit_canonical": "600b381e8dd789330ca591ed5109120a5635d6d438d265b5337c5170d0906a11",
    "n401_audited_head": "b1549688c32c539a63d5d85fec372f6ce0863559",
    "n401_review": 5203957365,
    "n401_result_blob": "d24b2100c90bd6e0f575572765a35fafaaa89196",
    "n401_result_canonical": "2689675c445d241c7874931524884fd45cd9b723a8999890ede9fa8a07870cda",
    "n399_audit_blob": "590ce4b0645455815e1cbb67cbc9a0b35299c0c8",
    "n399_audit_canonical": "a53747a12698afe255e06bee9d243cd5e46747b02a33293c79b4204b8392275c",
    "n391_result_blob": "3e72cea011e5a519173a710c20d88bc781c4cee8",
    "n391_result_canonical": "2b30f97aca0873568c324cf9a88ba6dc8ee0e3cceb29e1fc60e9e2c978b02da3",
    "n391_audit_blob": "5c080d67b1f1c90792fa29e5d5ded71fbc4ea45b",
    "n391_audit_canonical": "5ce24718a7cb9c3975eb6d8cc1c84e8b1d51f2a04d8745691bdc2281cdb4b11c",
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
    return hashlib.sha256(
        "".join(json.dumps(v, sort_keys=True, separators=(",", ":")) + "\n" for v in values).encode()
    ).hexdigest()


def classify(entries: list[dict], fields: tuple[str, ...], modulus: int) -> dict:
    groups: dict[tuple, list[dict]] = defaultdict(list)
    for entry in entries:
        key = tuple(entry[f] for f in fields) + (entry["block"] % modulus,)
        groups[key].append(entry)
    conflicts = 0
    max_parities = 0
    for rows in groups.values():
        ps = {int(row["required_x49_parity"]) for row in rows}
        max_parities = max(max_parities, len(ps))
        if len(ps) > 1:
            conflicts += 1
    return {
        "fields": list(fields),
        "modulus": modulus,
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

    audit401 = checked(
        node_root / "N401/AUDIT-PASS.json",
        EXPECTED["n401_audit_blob"],
        EXPECTED["n401_audit_canonical"],
    )
    result401 = checked(
        node_root / "N401/RESULT.json",
        EXPECTED["n401_result_blob"],
        EXPECTED["n401_result_canonical"],
    )
    audit399 = checked(
        node_root / "N399/AUDIT-PASS.json",
        EXPECTED["n399_audit_blob"],
        EXPECTED["n399_audit_canonical"],
    )
    n391 = checked(
        node_root / "N391/RESULT.json",
        EXPECTED["n391_result_blob"],
        EXPECTED["n391_result_canonical"],
    )
    audit391 = checked(
        node_root / "N391/AUDIT-PASS.json",
        EXPECTED["n391_audit_blob"],
        EXPECTED["n391_audit_canonical"],
    )

    req(audit401["status"] == "HOSTILE_AUDIT_PASS_RETAINED", "N401 audit receipt status drift")
    req(audit401["hostile_audit"]["verdict"] == "PASS", "N401 audit verdict drift")
    req(audit401["hostile_audit"]["audited_exact_head"] == EXPECTED["n401_audited_head"], "N401 audited head drift")
    req(int(audit401["hostile_audit"]["review_id"]) == EXPECTED["n401_review"], "N401 review drift")
    req(result401["bounded_result"]["survivor_terminal_count"] == 5459, "N401 survivor count drift")
    req(result401["bounded_result"]["best_nontrivial_compression_model"]["class_count"] == 66, "N401 class count drift")
    req(result401["bounded_result"]["best_nontrivial_compression_model"]["conflicting_class_count"] == 0, "N401 conflict drift")
    req(audit399["hostile_audit_verdict"] == "PASS", "N399 audit verdict drift")
    req(audit399["bounded_result"]["terminal_predicate"] == "(x49 + x98) mod 2 = 1", "N399 predicate drift")
    req(audit391["status"] in ("HOSTILE_AUDIT_PASS", "HOSTILE_AUDIT_PASS_RETAINED"), "N391 audit drift")

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
        req(required == reduced_required, f"N399 parity relation drift at block {block}")
        survivors = sum(1 for x49 in range(WIDTH) if (x49 & 1) == required)
        req(survivors in (56, 57), f"unexpected survivor count at block {block}")
        parity_counts[required] += 1
        survivor_total += survivors
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
    req(survivor_total == 5459, "N401 survivor reconstruction drift")
    req(stream_sha(blocks) == result401["bounded_result"]["block_stream_sha256"], "N401 block stream drift")
    req(stream_sha(parity_stream) == result401["bounded_result"]["required_parity_stream_sha256"], "N401 parity stream drift")

    searches: list[dict] = []
    for fields in BASE_TRIPLES:
        for modulus in range(2, MAX_MODULUS + 1):
            searches.append(classify(entries, fields, modulus))

    deterministic = [x for x in searches if x["determines_required_parity"]]
    nontrivial = [x for x in deterministic if x["nontrivial_block_compression"]]
    nontrivial.sort(key=lambda x: (x["class_count"], x["modulus"], x["fields"]))
    deterministic.sort(key=lambda x: (x["class_count"], x["modulus"], x["fields"]))
    best = nontrivial[0] if nontrivial else None

    per_triple = []
    for fields in BASE_TRIPLES:
        rows = [x for x in searches if tuple(x["fields"]) == fields]
        det = [x for x in rows if x["determines_required_parity"]]
        det.sort(key=lambda x: (x["modulus"], x["class_count"]))
        best_rows = sorted(rows, key=lambda x: (x["conflicting_class_count"], x["class_count"], x["modulus"]))
        per_triple.append({
            "fields": list(fields),
            "minimal_deterministic_modulus": det[0]["modulus"] if det else None,
            "minimal_deterministic_modulus_class_count": det[0]["class_count"] if det else None,
            "best_near_miss": best_rows[0],
        })

    beats = bool(best and best["class_count"] < 66)
    matches = bool(best and best["class_count"] == 66)
    deterministic_weaker = bool(best and best["class_count"] > 66)
    if beats:
        outcome = "INTRINSIC_BLOCK_CONGRUENCE_REPLACES_WAVE_AND_IMPROVES_N401"
    elif matches:
        outcome = "INTRINSIC_BLOCK_CONGRUENCE_REPLACES_WAVE_AND_MATCHES_N401"
    elif deterministic_weaker:
        outcome = "INTRINSIC_BLOCK_CONGRUENCE_REPLACES_WAVE_BUT_WEAKER_THAN_N401"
    else:
        outcome = "INTRINSIC_BLOCK_CONGRUENCE_NO_GO_MOD_2_TO_64"

    payload = {
        "semantics": "EXACT_BOUNDED_N401_97_BLOCK_INTRINSIC_BLOCK_CONGRUENCE_REPLACEMENT_FOR_OPERATIONAL_WAVE_ONLY",
        "source_block_count": 97,
        "source_terminal_count": 10961,
        "survivor_terminal_count": survivor_total,
        "required_parity_block_distribution": {"even": parity_counts[0], "odd": parity_counts[1]},
        "n401_best_wave_model_class_count": 66,
        "tested_base_triples": [list(x) for x in BASE_TRIPLES],
        "tested_modulus_range": [2, MAX_MODULUS],
        "tested_model_count": len(searches),
        "deterministic_model_count": len(deterministic),
        "nontrivial_deterministic_model_count": len(nontrivial),
        "best_intrinsic_congruence_model": best,
        "per_triple_summary": per_triple,
        "meets_or_beats_n401_class_count": bool(best and best["class_count"] <= 66),
        "strictly_improves_n401_class_count": beats,
        "outcome": outcome,
        "block_stream_sha256": stream_sha(blocks),
        "required_parity_stream_sha256": stream_sha(parity_stream),
        "wave_used_as_classifier_feature": False,
        "wave_used_only_for_source_partition_reconstruction": True,
        "transport_beyond_retained_97_blocks": False,
        "terminal_reenumeration_of_n399_rank_stream": False,
        "same_n401_feature_combination_search_repeated": False,
        "main_authority_subtraction_performed": False,
        "additional_pruning_terminals": 0,
        "main_pruning_credit": False,
        "full178_complete": False,
        "heavy_compute_authorized": False,
        "merge_authorized": False,
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)

    print("PASS_N402_N401_INTRINSIC_BLOCK_CONGRUENCE_WAVE_REPLACEMENT_PROBE")
    print(f"models={len(searches)} deterministic={len(deterministic)} nontrivial={len(nontrivial)}")
    print("outcome=" + outcome)
    if best:
        print("best=" + json.dumps(best, sort_keys=True, separators=(",", ":")))
    print("N402_PROBE_JSON=" + json.dumps(payload, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
