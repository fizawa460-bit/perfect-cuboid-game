#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

WIDTH = 113
ROW = "g1-d008"
ASSIGNMENT_ORDER = [95,99,103,102,49,97,94,101,93,98,96]
GROUPS = [[101,102,103],[97,98,99],[93,94,95,96]]
EXPECTED = {
    "n391_result_blob": "3e72cea011e5a519173a710c20d88bc781c4cee8",
    "n391_result_canonical": "2b30f97aca0873568c324cf9a88ba6dc8ee0e3cceb29e1fc60e9e2c978b02da3",
    "n391_audit_blob": "5c080d67b1f1c90792fa29e5d5ded71fbc4ea45b",
    "n391_audit_canonical": "5ce24718a7cb9c3975eb6d8cc1c84e8b1d51f2a04d8745691bdc2281cdb4b11c",
    "n391_audit_head": "f81d86498324fef2b9601933469a57dd49c72cb8",
    "n391_audit_review": 5193577864,
    "n392_audit_blob": "4b54b08271927065b42839b49c8c3caee45df705",
    "n392_audit_canonical": "ce8295b8c363a2bb27f97d4e83d41c68f70e171f8bc8aa2af0e3b8f394979377",
    "n392_audit_head": "9f9277a2a841a93f978a1549f14049552536424b",
    "n392_audit_review": 5193632260,
    "result_blob": "05e756b060f646708e5e7273840d66e66e232537",
    "result_canonical": "d9f5252b4c6a683ce2ff915b60cfd464f893357d164093692aca3879ca611d6e",
    "state_blob": "c1f5d23bc69c09beb7701efc17ab98d47489c83c",
    "state_canonical": "55edb88c70d4a2a4390edc17e3b8403c34b354bf20589b7ad90cd4d64fbe3b09",
    "probe_blob": "e063e335804252ca24e99a5ea722370f16614722",
    "indexer_blob": "4fb0a8dd34909494bd62646373e42877ed7a3c9e",
    "family_blob": "90ff82ed312dcc0cb32cf207935945f550e29170",
    "n357_verifier_blob": "fdca9ad629983d8c31c7e6355540af3545910120",
    "block_stream": "18e24ba5e4f5e9a874f3734763d224845f3101da72a4498ba47b925d72fbad72",
    "offset_stream": "efc41eb62f665cd1337fad9467dc04e2a85247ba029de5e0228fef2287f8e7eb",
}
EXPECTED_BLOCKS = [35,110,212,221,236,246,271,301,406,492,501,572,617,698,933,942,978,1010,1015,1065,1069,1141,1145,1195,1261,1265,1456,1708,1895,1960]
EXPECTED_OFFSETS = [25,79,157,163,174,183,202,228,301,353,361,406,438,495,645,653,679,700,703,743,745,798,801,840,889,891,1021,1239,1364,1413]
EXPECTED_ABC = {(0,1,4):2,(0,3,2):2,(1,1,3):4,(1,2,2):3,(1,3,1):4,(2,1,2):7,(2,3,0):2,(3,1,1):6}
EXPECTED_G3 = {0:2,1:10,2:12,3:4,4:2}
EXPECTED_BMC = {-3:2,-2:4,-1:7,0:9,1:2,2:4,3:2}


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


def line_stream(values) -> str:
    h = hashlib.sha256()
    for value in values:
        h.update(f"{value}\n".encode())
    return h.hexdigest()


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
    probe_path = repo / "stages/stage32/32-01-178/nodes/N393/probe_n393_mass5_signature_census.py"

    req(blob(idx_path) == EXPECTED["indexer_blob"], "indexer blob drift")
    req(blob(fam_path) == EXPECTED["family_blob"], "family blob drift")
    req(blob(n357_path) == EXPECTED["n357_verifier_blob"], "N357 verifier blob drift")
    req(blob(probe_path) == EXPECTED["probe_blob"], "N393 probe blob drift")

    n391 = checked(repo / "stages/stage32/32-01-178/nodes/N391/RESULT.json", EXPECTED["n391_result_blob"], EXPECTED["n391_result_canonical"])
    audit391 = checked(repo / "stages/stage32/32-01-178/nodes/N391/AUDIT-PASS.json", EXPECTED["n391_audit_blob"], EXPECTED["n391_audit_canonical"])
    audit392 = checked(repo / "stages/stage32/32-01-178/nodes/N392/AUDIT-PASS.json", EXPECTED["n392_audit_blob"], EXPECTED["n392_audit_canonical"])
    result = checked(repo / "stages/stage32/32-01-178/nodes/N393/RESULT.json", EXPECTED["result_blob"], EXPECTED["result_canonical"])
    state = checked(repo / "stages/stage32/32-01-178/nodes/N393/STATE.json", EXPECTED["state_blob"], EXPECTED["state_canonical"])

    req(audit391["status"] == "HOSTILE_AUDIT_PASS", "N391 hostile audit status drift")
    req(audit391["audited_exact_head"] == EXPECTED["n391_audit_head"] and int(audit391["review_id"]) == EXPECTED["n391_audit_review"], "N391 hostile audit receipt drift")
    req(audit392["status"] == "HOSTILE_AUDIT_PASS_RETAINED" and audit392["hostile_audit_verdict"] == "PASS", "N392 hostile audit status drift")
    req(audit392["audited_exact_head"] == EXPECTED["n392_audit_head"] and int(audit392["hostile_audit_review_id"]) == EXPECTED["n392_audit_review"], "N392 hostile audit receipt drift")

    sys.path.insert(0, str(residual))
    from compressed_terminal_indexer import CompressedTerminalIndexer
    idx = CompressedTerminalIndexer(8,8)
    req(idx.normal_budget + 1 == WIDTH, "width drift")
    n357 = load_module(n357_path, "n393_formal_n357")
    req(n357.ASSIGNMENT_ORDER == ASSIGNMENT_ORDER, "assignment order drift")

    survivors: list[int] = []
    for block in range(idx.exceptional_count):
        base = tuple(int(v) for v in idx.unrank(block * WIDTH))
        req(base[4] == 0 and idx.rank(base) == block * WIDTH, f"block-base roundtrip drift: {block}")
        if n357.prefix_survives(base):
            survivors.append(block)
    req(len(survivors) == 7596, "current-prefix survivor block-count drift")

    wave_of: dict[int,str] = {}
    all_n391: list[int] = []
    for wave in ("CUT193","CUT194","CUT195","CUT196","CUT197","CUT198"):
        blocks = list(map(int, n391["waves"][wave]["residual_blocks"]))
        for block in blocks:
            req(block not in wave_of, f"duplicate N391 residual block: {block}")
            wave_of[block] = wave
        all_n391.extend(blocks)
    req(len(all_n391) == 97 and len(set(all_n391)) == 97, "N391 residual-union drift")
    req(n391["transport_checks"]["certlift03"]["residual_fixed_exceptional_mass_distribution"]["5"] == 30, "N391 mass5 ledger drift")

    blocks: list[int] = []
    offsets: list[int] = []
    ranks: list[int] = []
    signatures: list[tuple[int,...]] = []
    abc_counts: Counter[tuple[int,int,int]] = Counter()
    g3_counts: Counter[int] = Counter()
    bmc_counts: Counter[int] = Counter()
    wave_counts: Counter[str] = Counter()

    for block in all_n391:
        base = list(map(int, idx.unrank(block * WIDTH)))
        req(base[4] == 0 and idx.rank(tuple(base)) == block * WIDTH, f"base drift: {block}")
        req(n357.prefix_survives(tuple(base)) and n357.n357_accepts(tuple(base)), f"N357 rejects N391 residual base: {block}")
        by = dict(zip(ASSIGNMENT_ORDER, base))
        fixed_mass = sum(v for label,v in by.items() if label != 49)
        if fixed_mass != 5:
            continue

        abc = tuple(sum(by[label] for label in group) for group in GROUPS)
        bmc = abc[1] - abc[2]
        req(bmc <= 16, f"N356 necessary cut regression: {block}")
        signature10 = tuple(v for i,v in enumerate(base) if i != 4)
        offset = survivors.index(block)
        blocks.append(block)
        offsets.append(offset)
        signatures.append(signature10)
        abc_counts[abc] += 1
        g3_counts[abc[2]] += 1
        bmc_counts[bmc] += 1
        wave_counts[wave_of[block]] += 1

        for x4 in range(WIDTH):
            vals = list(base)
            vals[4] = x4
            rank = block * WIDTH + x4
            req(idx.rank(tuple(vals)) == rank, f"rank roundtrip drift: {rank}")
            req(n357.prefix_survives(tuple(vals)) and n357.n357_accepts(tuple(vals)), f"N357 rejects mass5 rank: {rank}")
            ranks.append(rank)

    req(blocks == EXPECTED_BLOCKS, "mass5 block identities drift")
    req(offsets == EXPECTED_OFFSETS, "mass5 survivor offsets drift")
    req(len(blocks) == 30 and len(ranks) == 3390, "N393 cardinality drift")
    req(len(set(signatures)) == 30, "mass5 exact base-signature uniqueness drift")
    req(dict(sorted(abc_counts.items())) == EXPECTED_ABC, "mass5 descriptive abc census drift")
    req(dict(sorted(g3_counts.items())) == EXPECTED_G3, "mass5 g3 census drift")
    req(dict(sorted(bmc_counts.items())) == EXPECTED_BMC, "mass5 b-c census drift")
    req(line_stream(blocks) == EXPECTED["block_stream"], "mass5 block stream drift")
    req(line_stream(offsets) == EXPECTED["offset_stream"], "mass5 offset stream drift")
    req(result["identity_certificate"]["mass5_block_stream_sha256"] == EXPECTED["block_stream"], "retained mass5 block-stream certificate drift")
    req(result["identity_certificate"]["mass5_survivor_offset_stream_sha256"] == EXPECTED["offset_stream"], "retained mass5 offset-stream certificate drift")
    req(128820 not in ranks, "retained N372 witness unexpectedly enters N393 subset")

    req(result["mass5_blocks"] == blocks, "retained N393 block list drift")
    req(result["mass5_survivor_offsets"] == offsets, "retained N393 offset list drift")
    req(result["scope"]["block_count"] == 30 and result["scope"]["subset_cardinality"] == 3390, "N393 retained scope drift")
    req(result["scope"]["fixed_exceptional_mass"] == 5, "N393 mass selector drift")
    req(result["identity_certificate"]["exact_base_signature_unique_count"] == 30, "N393 retained signature-count drift")
    req(result["descriptive_incidence"]["class_semantics"] == "DESCRIPTIVE_ONLY_NOT_SOLVER_EQUIVALENCE_NOT_COMPRESSION_EQUIVALENCE", "N393 descriptive-class semantic firewall drift")
    req(result["known_picard_status"]["retained_n372_witness_in_subset"] is False, "N393 N372 witness firewall drift")
    req(result["known_picard_status"]["n393_additional_picard64_witness_claims"] == 0, "unexpected N393 Picard64 promotion")

    req(state["status"] == "AUDIT_WAIT", "N393 state must be audit-wait")
    req(state["bounded_leaf"]["block_count"] == 30 and state["bounded_leaf"]["identity_count"] == 3390, "N393 state bounded-leaf drift")
    req(state["bounded_leaf"]["numerical_leaf_compression_credit"] is False, "unexpected N393 compression credit")
    req(state["ownership"]["main_global_residual_feasibility_competition"] is False, "MAIN ownership firewall drift")
    req(state["ownership"]["global_obstruction_rederived"] is False and state["ownership"]["family_level_claim_promoted"] is False, "global/family promotion drift")
    req(state["ownership"]["common_unsat_claim_promoted"] is False and state["ownership"]["symbolic_obstruction_claim_promoted"] is False, "UNSAT/symbolic promotion drift")
    req(state["ownership"]["main_handoff_required"] is False, "unexpected MAIN handoff flag")
    req(state["safety"]["heavy_compute_authorized"] is False and state["safety"]["merge_authorized"] is False, "heavy/merge firewall drift")
    req(state["safety"]["full178_complete"] is False and state["safety"]["stage32_closed"] is False, "closure firewall drift")
    req(state["source_authority"]["v24_remaining_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "V24 semantics drift")

    for key in ("main_pruning_credit","full178_complete","effectivity_final","receiver_credit","theorem_credit","endpoint_credit","stage32_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","heavy_compute_authorized","merge_authorized"):
        req(result["credit"][key] is False, f"N393 result credit firewall drift: {key}")
    req(result["credit"]["additional_pruning_terminals"] == 0 and result["credit"]["numerical_leaf_compression_credit"] is False, "unexpected N393 pruning/compression credit")

    print("PASS_N393_V24_MASS5_30_BLOCK_SIGNATURE_CENSUS")
    print("blocks=30 identities=3390 fixed_mass=5")
    print("abc_classes=8 exact_base_signatures=30")
    print("g3_distribution=0:2,1:10,2:12,3:4,4:2 pruning_credit=0 compression_credit=false")


if __name__ == "__main__":
    main()
