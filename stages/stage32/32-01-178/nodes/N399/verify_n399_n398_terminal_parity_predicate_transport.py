#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

WIDTH = 113
ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
X49_POS = ASSIGNMENT_ORDER.index(49)
X93_POS = ASSIGNMENT_ORDER.index(93)
X98_POS = ASSIGNMENT_ORDER.index(98)
X96_POS = ASSIGNMENT_ORDER.index(96)
WAVES = ["CUT193", "CUT194", "CUT195", "CUT196", "CUT197", "CUT198"]

N398_AUDIT_BLOB = "6146fc8d9bc368594f922defa91b7381c4de6c8e"
N398_AUDIT_CANONICAL = "aa616a76bff47b9352c7eaa5397236e672b8b9d3f6552a85dc6b8c5905365499"
N398_AUDIT_REVIEW = 5198108138
N398_AUDITED_HEAD = "71f078a7521b265e300a450ab129370f077ef6a1"
N398_RESULT_BLOB = "cefe256d00aa6267252f8f1bd3e880c64433344f"
N398_RESULT_CANONICAL = "611632cedd9ff3515bb374a608020dd06079240db5224bb15f90845c7b90cad7"
N396_RESULT_BLOB = "971f1665c8be4c22eef549020046dd0830028dff"
N396_RESULT_CANONICAL = "e34e23e2b17063c2f51d9862af1c2a958002fdb0327e43b5e52d85bcb1a83cd1"
N395_RESULT_BLOB = "02adab67a764a373c59cd42e2e404318f2d7488c"
N395_RESULT_CANONICAL = "0a9ef6ccd8be8e3f270694d155bc7d4ebbd19cc9eab79906c34808440aa7441b"
N391_RESULT_BLOB = "3e72cea011e5a519173a710c20d88bc781c4cee8"
N391_RESULT_CANONICAL = "2b30f97aca0873568c324cf9a88ba6dc8ee0e3cceb29e1fc60e9e2c978b02da3"
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
    req(claimed == expected_canonical, f"claimed canonical drift: {path}")
    req(csha(body) == expected_canonical, f"canonical drift: {path}")
    return obj


def stream_sha(values: list[int]) -> str:
    return hashlib.sha256("".join(f"{v}\n" for v in values).encode()).hexdigest()


def main() -> None:
    repo = Path(__file__).resolve().parents[5]
    lane = repo / "stages/stage32/32-01-178/nodes"
    residual = repo / "stages/stage32/residual-32-01-production"

    audit398 = checked(lane / "N398/AUDIT-PASS.json", N398_AUDIT_BLOB, N398_AUDIT_CANONICAL)
    result398 = checked(lane / "N398/RESULT.json", N398_RESULT_BLOB, N398_RESULT_CANONICAL)
    result396 = checked(lane / "N396/RESULT.json", N396_RESULT_BLOB, N396_RESULT_CANONICAL)
    result395 = checked(lane / "N395/RESULT.json", N395_RESULT_BLOB, N395_RESULT_CANONICAL)
    result391 = checked(lane / "N391/RESULT.json", N391_RESULT_BLOB, N391_RESULT_CANONICAL)

    req(audit398["hostile_audit_verdict"] == "PASS", "N398 audit verdict drift")
    req(audit398["audited_exact_head"] == N398_AUDITED_HEAD, "N398 audited head drift")
    req(int(audit398["hostile_audit_review_id"]) == N398_AUDIT_REVIEW, "N398 review drift")
    req(audit398["continuation"]["allowed"] is True, "N398 continuation closed")
    req(result398["affine_parity_compression"]["derived_equivalent_rule"] == "x49 + x98 = 1 (mod 2)",
        "N398 derived rule drift")
    req(result398["scope"]["block_count"] == 97, "N398 block count drift")
    req(result398["scope"]["source_terminal_count"] == 10961, "N398 terminal count drift")
    req(result395["scope"]["unique_within_block_varying_labels"] == [49], "N395 varying label drift")
    req(result395["transport_result"]["transported_gf2_relation"] == "x93 + x98 + x96 = 1 (mod 2)",
        "N395 relation drift")
    req(result391["identity_certificate"]["rank_formula"] ==
        "for each residual block b and x4 in 0..112: rank=113*b+x4", "N391 rank formula drift")
    req(result391["identity_certificate"]["x4_label"] == 49, "N391 x4 label drift")

    idx_path = residual / "compressed_terminal_indexer.py"
    req(blob(idx_path) == INDEXER_BLOB, "compressed indexer drift")
    sys.path.insert(0, str(residual))
    from compressed_terminal_indexer import CompressedTerminalIndexer

    idx = CompressedTerminalIndexer(8, 8)
    req(idx.normal_budget + 1 == WIDTH, "terminal width drift")

    blocks = [int(b) for wave in WAVES for b in result391["waves"][wave]["residual_blocks"]]
    req(len(blocks) == 97 and len(set(blocks)) == 97, "N391 block union drift")
    req(stream_sha(blocks) == result391["identity_certificate"]["residual_block_stream_sha256"],
        "N391 block stream drift")

    sat_ranks: list[int] = []
    unsat_ranks: list[int] = []
    required_parities: list[int] = []
    parity_distribution = Counter()
    fixed_coordinate_violations = 0
    predicate_mismatches = 0

    for block in blocks:
        base_rank = block * WIDTH
        base = list(map(int, idx.unrank(base_rank)))
        req(idx.rank(tuple(base)) == base_rank, f"base rank roundtrip drift block={block}")
        req(base[X49_POS] == 0, f"base x49 drift block={block}")

        required_from_x98 = 1 ^ (base[X98_POS] & 1)
        required_from_x93_x96 = (base[X93_POS] + base[X96_POS]) & 1
        req(required_from_x98 == required_from_x93_x96,
            f"N398/N395 parity reduction drift block={block}")
        required_parities.append(required_from_x98)
        parity_distribution[required_from_x98] += 1

        block_sat = 0
        for offset in range(WIDTH):
            rank = base_rank + offset
            x = list(map(int, idx.unrank(rank)))
            req(idx.rank(tuple(x)) == rank, f"rank roundtrip drift rank={rank}")
            req(x[X49_POS] == offset, f"x49/rank-offset drift rank={rank}")

            for i in range(len(ASSIGNMENT_ORDER)):
                if i != X49_POS and x[i] != base[i]:
                    fixed_coordinate_violations += 1

            sat_by_rule = ((x[X49_POS] + x[X98_POS]) & 1) == 1
            sat_by_block_parity = (x[X49_POS] & 1) == required_from_x98
            if sat_by_rule != sat_by_block_parity:
                predicate_mismatches += 1

            if sat_by_rule:
                sat_ranks.append(rank)
                block_sat += 1
            else:
                unsat_ranks.append(rank)

        req(block_sat == (57 if required_from_x98 == 0 else 56),
            f"per-block survivor count drift block={block}")

    req(fixed_coordinate_violations == 0, "within-block fixed-coordinate drift")
    req(predicate_mismatches == 0, "terminal predicate mismatch")
    req(parity_distribution == Counter({0: 27, 1: 70}), "required parity distribution drift")
    req(len(sat_ranks) == 5459 and len(unsat_ranks) == 5502, "terminal partition count drift")

    sat_sha = stream_sha(sat_ranks)
    unsat_sha = stream_sha(unsat_ranks)
    req(sat_sha == result396["completion_result"]["sat_terminal_rank_stream_sha256"],
        "N396 SAT rank stream mismatch")
    req(unsat_sha == result396["completion_result"]["unsat_terminal_rank_stream_sha256"],
        "N396 UNSAT rank stream mismatch")

    certificate = {
        "row_id": "g1-d008",
        "g": 1,
        "d": 8,
        "e": 8,
        "block_count": 97,
        "block_width": WIDTH,
        "source_terminal_count": 10961,
        "predicate": "(x49 + x98) mod 2 = 1",
        "block_stream_sha256": stream_sha(blocks),
        "required_parity_stream_sha256": stream_sha(required_parities),
        "sat_terminal_count": len(sat_ranks),
        "unsat_terminal_count": len(unsat_ranks),
        "sat_terminal_rank_stream_sha256": sat_sha,
        "unsat_terminal_rank_stream_sha256": unsat_sha,
    }
    payload = {
        "semantics": "EXACT_TERMINAL_IDENTITY_TRANSPORT_OF_HOSTILE_AUDITED_N398_PARITY_CLASSIFIER_ON_RETAINED_N391_97_BLOCKS; NO_NEW_PRUNING_OR_MAIN_CREDIT",
        "source": {
            "n398_hostile_audit_review_id": N398_AUDIT_REVIEW,
            "n398_audited_exact_head": N398_AUDITED_HEAD,
            "n398_audit_receipt_blob": N398_AUDIT_BLOB,
            "n398_audit_receipt_canonical": N398_AUDIT_CANONICAL,
            "n398_result_blob": N398_RESULT_BLOB,
            "n398_result_canonical": N398_RESULT_CANONICAL,
            "n396_result_blob": N396_RESULT_BLOB,
            "n396_result_canonical": N396_RESULT_CANONICAL,
            "n391_result_blob": N391_RESULT_BLOB,
            "n391_result_canonical": N391_RESULT_CANONICAL,
            "compressed_terminal_indexer_blob": INDEXER_BLOB
        },
        "certificate": certificate,
        "certificate_canonical_sha256": csha(certificate),
        "transport_checks": {
            "all_non_x49_coordinates_fixed_within_each_block": fixed_coordinate_violations == 0,
            "n398_primary_and_n395_reduced_parity_agree_on_all_97_blocks": True,
            "terminal_predicate_matches_block_parity_on_all_10961_terminals": predicate_mismatches == 0,
            "reconstructs_n396_sat_rank_stream_exactly": True,
            "reconstructs_n396_unsat_rank_stream_exactly": True
        },
        "route_control": {
            "outcome": "N398_TERMINAL_PARITY_PREDICATE_TRANSPORT_CANDIDATE",
            "material_result": "EXACT_5459_SURVIVOR_AND_5502_REJECTED_IDENTITY_STREAMS_RECONSTRUCTED_BY_ONE_TWO_COORDINATE_PARITY_PREDICATE_ON_97_RETAINED_BLOCKS",
            "additional_pruning_terminals": 0,
            "same_97x8_parity_census_repeated": False,
            "transport_beyond_retained_97_blocks": False
        },
        "credit_firewall": {
            "bounded_terminal_family_compression_candidate": True,
            "numerical_leaf_compression_credit": False,
            "additional_pruning_credit": False,
            "main_pruning_credit": False,
            "full178_complete": False,
            "integral_carrier_obstruction_promoted": False,
            "effectivity_final": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "stage32_closed": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "heavy_compute_authorized": False,
            "merge_authorized": False
        }
    }

    print("PASS_N399_N398_TERMINAL_PARITY_PREDICATE_TRANSPORT")
    print(json.dumps(payload, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
