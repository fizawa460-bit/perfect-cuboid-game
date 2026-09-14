#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

WIDTH = 113
N394_AUDITED_HEAD = "5cd1b2eadb7fd2921686bc3a2554fdd1b427f431"
N394_AUDIT_REVIEW = 5194812379
N394_AUDIT_BLOB = "0227d9e1da87e6d9ea579d09a35a2db5fa13f568"
N394_AUDIT_CANONICAL = "8d2db62de7defea8fc02d6f32cfbab9165f92b08c327f687d430d15ef2729786"
N394_RESULT_BLOB = "cc8298c0a4d5d003be2eb00d828df42ceb6a1af0"
N394_RESULT_CANONICAL = "2bb9ca471ec6ce50e77921de17113bb5dda711e48d1026240f683660a2ea4fbc"
N394_PROBE_BLOB = "042bb940a6c586092f6b31312d3b16551e566a58"
INDEXER_BLOB = "4fb0a8dd34909494bd62646373e42877ed7a3c9e"


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
    req(
        claimed == expected_canonical and csha(body) == expected_canonical,
        f"canonical drift: {path}",
    )
    return obj


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def integer_stream_sha(values: list[int]) -> str:
    return hashlib.sha256("".join(f"{v}\n" for v in values).encode()).hexdigest()


def signature_stream_sha(rows: list[list[int]]) -> str:
    return hashlib.sha256(
        "".join(",".join(map(str, row)) + "\n" for row in rows).encode()
    ).hexdigest()


def main() -> None:
    repo = Path(__file__).resolve().parents[5]
    node394 = repo / "stages/stage32/32-01-178/nodes/N394"
    residual = repo / "stages/stage32/residual-32-01-production"

    audit394 = checked(
        node394 / "AUDIT-PASS.json", N394_AUDIT_BLOB, N394_AUDIT_CANONICAL
    )
    req(audit394["status"] == "HOSTILE_AUDIT_PASS_RETAINED", "N394 audit status drift")
    req(audit394["audited_exact_head"] == N394_AUDITED_HEAD, "N394 audit head drift")
    req(
        int(audit394["hostile_audit_review_id"]) == N394_AUDIT_REVIEW,
        "N394 audit review drift",
    )
    req(audit394["hostile_audit_verdict"] == "PASS", "N394 audit verdict drift")

    result394 = checked(
        node394 / "RESULT.json", N394_RESULT_BLOB, N394_RESULT_CANONICAL
    )
    req(
        result394["route_control"]["outcome"] == "BOUNDED_RELATION_CLASSIFIED_NO_PRUNING",
        "N394 route outcome drift",
    )
    req(
        result394["classification"]["q_exact_relations"] == ["x95 = 0", "x99 = 1"],
        "N394 exact relation classification drift",
    )
    req(
        result394["classification"]["gf2_extra_relation"]
        == "x93 + x98 + x96 = 1 (mod 2)",
        "N394 GF2 relation classification drift",
    )

    probe394_path = node394 / "probe_n394_cross_mass_affine_structure.py"
    req(blob(probe394_path) == N394_PROBE_BLOB, "N394 probe blob drift")
    probe394 = load_module(probe394_path, "n395_n394_probe")
    req(probe394.WIDTH == WIDTH, "N394 width drift")

    idx_path = residual / "compressed_terminal_indexer.py"
    req(blob(idx_path) == INDEXER_BLOB, "compressed indexer blob drift")
    req(
        audit394["source_locks"]["indexer_blob"] == INDEXER_BLOB,
        "N394 audit indexer lock drift",
    )

    n391 = probe394.checked(
        repo / "stages/stage32/32-01-178/nodes/N391/RESULT.json",
        probe394.EXPECTED["n391_result_blob"],
        probe394.EXPECTED["n391_result_canonical"],
    )

    sys.path.insert(0, str(residual))
    from compressed_terminal_indexer import CompressedTerminalIndexer

    idx = CompressedTerminalIndexer(8, 8)
    req(idx.normal_budget + 1 == WIDTH, "terminal block width drift")

    blocks: list[int] = []
    for wave in probe394.WAVES:
        blocks.extend(map(int, n391["waves"][wave]["residual_blocks"]))
    req(len(blocks) == 97 and len(set(blocks)) == 97, "N391 residual union drift")

    order = list(probe394.ASSIGNMENT_ORDER)
    req(order == [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96], "assignment order drift")
    label_to_index = {label: i for i, label in enumerate(order)}
    relation_labels = [95, 99, 93, 98, 96]
    varying_labels: set[int] = set()
    terminal_signatures: list[list[int]] = []
    ranks: list[int] = []

    for block in blocks:
        start = block * WIDTH
        base = tuple(int(v) for v in idx.unrank(start))
        req(base[4] == 0, f"base x4 drift: block {block}")
        req(idx.rank(base) == start, f"base rank drift: block {block}")

        for offset in range(WIDTH):
            rank = start + offset
            terminal = tuple(int(v) for v in idx.unrank(rank))
            req(idx.rank(terminal) == rank, f"rank/unrank drift: block {block} offset {offset}")

            changed = {
                order[i]
                for i, (a, b) in enumerate(zip(base, terminal))
                if a != b
            }
            varying_labels.update(changed)
            req(changed <= {49}, f"non-x49 within-block drift: block {block} offset {offset}")

            by = dict(zip(order, terminal))
            req(by[95] == 0, f"x95 relation violation: block {block} offset {offset}")
            req(by[99] == 1, f"x99 relation violation: block {block} offset {offset}")
            req(
                (by[93] + by[98] + by[96]) % 2 == 1,
                f"GF2 relation violation: block {block} offset {offset}",
            )
            req(
                all(terminal[label_to_index[label]] == base[label_to_index[label]] for label in relation_labels),
                f"relation-coordinate transport drift: block {block} offset {offset}",
            )

            terminal_signatures.append([by[label] for label in probe394.FIXED_LABELS])
            ranks.append(rank)

    req(len(ranks) == 10961, "terminal identity count drift")
    req(varying_labels == {49}, "expected x49 to be the unique within-block varying label")
    req(
        len({tuple(row) for row in terminal_signatures}) == 97,
        "transported fixed-signature count drift",
    )

    payload = {
        "semantics": "EXACT_N394_RELATION_TRANSPORT_TO_ALL_N391_WITHIN_BLOCK_TERMINALS_ONLY_NOT_PICARD64_UNSAT_NOT_EFFECTIVITY",
        "source_n394_audited_head": N394_AUDITED_HEAD,
        "source_n394_hostile_audit_review": N394_AUDIT_REVIEW,
        "block_count": 97,
        "block_width": WIDTH,
        "terminal_identity_count": len(ranks),
        "assignment_order": order,
        "unique_within_block_varying_labels": sorted(varying_labels),
        "transported_relation_labels": relation_labels,
        "transported_exact_relations": ["x95 = 0", "x99 = 1"],
        "transported_gf2_relation": "x93 + x98 + x96 = 1 (mod 2)",
        "relation_violation_count": 0,
        "transported_fixed_signature_unique_count": 97,
        "terminal_rank_stream_sha256": integer_stream_sha(ranks),
        "transported_signature10_stream_sha256": signature_stream_sha(terminal_signatures),
        "additional_pruning_terminals": 0,
        "numerical_leaf_compression_credit": False,
        "picard64_unsat_promoted": False,
        "integral_carrier_obstruction_promoted": False,
        "family_level_claim_promoted": False,
        "common_unsat_claim_promoted": False,
        "symbolic_obstruction_claim_promoted": False,
        "main_handoff_status": "TERMINAL_RELATION_TRANSPORT_VERIFIED_NO_EFFECTIVITY",
        "heavy_compute_authorized": False,
        "merge_authorized": False,
    }
    print("PASS_N395_N394_RELATION_TERMINAL_TRANSPORT")
    print(
        f"blocks={payload['block_count']} width={WIDTH} terminals={len(ranks)} "
        f"varying_labels={payload['unique_within_block_varying_labels']} violations=0"
    )
    print("N395_PROBE_JSON=" + json.dumps(payload, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
