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
    "result_blob": "fc5f7c91d7cee0cfccd7e73bddfacb5e17528de3",
    "result_canonical": "34e90d53f2c6b9c5b7057e504286f2790fd877f70e1d34ffa15c18d79db2e57a",
    "state_blob": "6111c78223ddc8bf1fb91aeb3045657b0060ff72",
    "state_canonical": "fb6f6e64e9d461a858404b21d83688a8d8327c28b66f59aff0ad3f6787af7ede",
    "indexer_blob": "4fb0a8dd34909494bd62646373e42877ed7a3c9e",
    "family_blob": "90ff82ed312dcc0cb32cf207935945f550e29170",
    "n357_verifier_blob": "fdca9ad629983d8c31c7e6355540af3545910120",
    "block_stream": "ba817154efd106ebf53bd82848a2bab2b60cde21a803b0915f4b4eb906daa8fe",
    "offset_stream": "7d6752811917f74aa66a96e21651526e28d3fa6c23f554d625c0a3b1ff1b81a3",
    "base_matrix": "06af9821f084c058eb06d0e29840280addf24de0ad1aa111a5092e697b1b6a1e",
    "abc_matrix": "b9fd768317d20a140da27ae36b96aff9a6793fe610edc120c637d605fc83023c",
    "projection_matrix": "19b91d95ab3f056caea84887ed8a13d65cc8157af7d3006cfcdf0b5f3e19189b",
    "formal_entry_matrix": "010944362172fd3df235cc637c1a158b6c868ea1e43be37b5dc22bcad996f725",
    "rank_stream": "7584bbe4cca9b9ab8e5d055eb600b5e446560ba4a68d9fd3510de5f1a2cbeea1",
    "identity_stream": "1b1fbcf56f5ed125393b29f703ed98d8a2d091a4931d7e1eb15d73b272794238",
}

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
    req(blob(idx_path) == EXPECTED["indexer_blob"], "indexer blob drift")
    req(blob(fam_path) == EXPECTED["family_blob"], "family blob drift")
    req(blob(n357_path) == EXPECTED["n357_verifier_blob"], "N357 verifier blob drift")

    n391 = checked(repo / "stages/stage32/32-01-178/nodes/N391/RESULT.json", EXPECTED["n391_result_blob"], EXPECTED["n391_result_canonical"])
    audit = checked(repo / "stages/stage32/32-01-178/nodes/N391/AUDIT-PASS.json", EXPECTED["n391_audit_blob"], EXPECTED["n391_audit_canonical"])
    result = checked(repo / "stages/stage32/32-01-178/nodes/N392/RESULT.json", EXPECTED["result_blob"], EXPECTED["result_canonical"])
    state = checked(repo / "stages/stage32/32-01-178/nodes/N392/STATE.json", EXPECTED["state_blob"], EXPECTED["state_canonical"])
    req(audit["status"] == "HOSTILE_AUDIT_PASS" and audit["audited_exact_head"] == EXPECTED["n391_audit_head"] and int(audit["review_id"]) == EXPECTED["n391_audit_review"], "N391 hostile-audit receipt drift")

    sys.path.insert(0, str(residual))
    from compressed_terminal_indexer import CompressedTerminalIndexer
    idx = CompressedTerminalIndexer(8,8)
    req(idx.normal_budget + 1 == WIDTH, "width drift")
    n357 = load_module(n357_path, "n392_n357")
    req(n357.ASSIGNMENT_ORDER == ASSIGNMENT_ORDER, "assignment order drift")

    survivors = []
    for block in range(idx.exceptional_count):
        base = tuple(int(v) for v in idx.unrank(block * WIDTH))
        req(base[4] == 0 and idx.rank(base) == block * WIDTH, f"block base rank drift: {block}")
        if n357.prefix_survives(base):
            survivors.append(block)

    wave_of: dict[int,str] = {}
    all_n391: list[int] = []
    for wave in ("CUT193","CUT194","CUT195","CUT196","CUT197","CUT198"):
        blocks = list(map(int, n391["waves"][wave]["residual_blocks"]))
        for b in blocks:
            req(b not in wave_of, f"duplicate N391 residual block: {b}")
            wave_of[b] = wave
        all_n391.extend(blocks)
    req(len(all_n391) == 97, "N391 residual cardinality drift")

    entries = []
    ranks = []
    identities = []
    abc_counts = Counter()
    g3_counts = Counter()
    bc_counts = Counter()
    wave_counts = Counter()
    for block in all_n391:
        base = list(map(int, idx.unrank(block * WIDTH)))
        by = dict(zip(ASSIGNMENT_ORDER, base))
        fixed_mass = sum(v for label,v in by.items() if label != 49)
        if fixed_mass != 6:
            continue
        req(n357.prefix_survives(tuple(base)) and n357.n357_accepts(tuple(base)), f"N357 rejects mass6 base: {block}")
        abc = [sum(by[label] for label in group) for group in GROUPS]
        bmc = abc[1] - abc[2]
        req(bmc <= 16, f"N356 necessary cut regression: {block}")
        signature10 = [v for i,v in enumerate(base) if i != 4]
        offset = survivors.index(block)
        entry = {"abc":abc,"b_minus_c":bmc,"base_signature10":signature10,"block":block,"g3_sum":abc[2],"rank_range":[block*WIDTH,block*WIDTH+WIDTH-1],"source_wave":wave_of[block],"survivor_offset":offset}
        entries.append(entry)
        abc_counts[tuple(abc)] += 1
        g3_counts[abc[2]] += 1
        bc_counts[bmc] += 1
        wave_counts[wave_of[block]] += 1
        for x4 in range(WIDTH):
            vals = list(base)
            vals[4] = x4
            rank = block * WIDTH + x4
            req(idx.rank(tuple(vals)) == rank, f"rank roundtrip drift: {rank}")
            req(n357.prefix_survives(tuple(vals)) and n357.n357_accepts(tuple(vals)), f"N357 rejects rank: {rank}")
            ranks.append(rank)
            identities.append(f"{ROW}|e=8|rank={rank}")

    blocks = [e["block"] for e in entries]
    offsets = [e["survivor_offset"] for e in entries]
    req(blocks == [36,43,68,111,159,237,355,737,1209,1405,1657,2018,2071], "mass6 block identities drift")
    req(offsets == [26,33,54,80,118,175,264,521,851,980,1203,1465,1508], "mass6 survivor offsets drift")
    req(len(entries) == 13 and len(ranks) == 1469, "N392 cardinality drift")
    req(len({tuple(e["base_signature10"]) for e in entries}) == 13, "exact base-signature uniqueness drift")
    req(dict(sorted(abc_counts.items())) == {(0,2,4):2,(0,4,2):2,(2,2,2):9}, "abc incidence drift")
    req(dict(sorted(g3_counts.items())) == {2:11,4:2}, "g3 incidence drift")
    req(dict(sorted(bc_counts.items())) == {-2:2,0:9,2:2}, "b-c incidence drift")
    req(dict(sorted(wave_counts.items())) == {"CUT193":6,"CUT194":1,"CUT195":1,"CUT196":2,"CUT197":1,"CUT198":2}, "wave incidence drift")

    projection = [{k:v for k,v in e.items() if k != "source_wave"} for e in entries]
    req(line_stream(blocks) == EXPECTED["block_stream"], "block stream drift")
    req(line_stream(offsets) == EXPECTED["offset_stream"], "offset stream drift")
    req(csha([e["base_signature10"] for e in entries]) == EXPECTED["base_matrix"], "base signature matrix drift")
    req(csha([e["abc"] for e in entries]) == EXPECTED["abc_matrix"], "abc matrix drift")
    req(csha(projection) == EXPECTED["projection_matrix"], "entry projection drift")
    req(csha(entries) == EXPECTED["formal_entry_matrix"], "formal entry matrix drift")
    req(line_stream(ranks) == EXPECTED["rank_stream"], "rank stream drift")
    req(line_stream(identities) == EXPECTED["identity_stream"], "identity stream drift")

    req(result["entries"] == entries, "N392 retained entries drift")
    req(result["scope"]["block_count"] == 13 and result["scope"]["subset_cardinality"] == 1469, "N392 scope drift")
    req(result["incidence_census"]["class_semantics"] == "DESCRIPTIVE_GROUP_SUM_INCIDENCE_PARTITION_ONLY_NOT_SOLVER_EQUIVALENCE_NOT_COMPRESSION_PROOF", "incidence semantic firewall drift")
    req(result["known_picard_status"]["retained_n372_witness_rank_128820_in_subset"] is False, "N372 witness subset firewall drift")
    req(result["known_picard_status"]["n392_additional_picard64_witness_claims"] == 0, "unexpected Picard64 promotion")
    req(128820 not in ranks, "N372 witness unexpectedly in N392 subset")
    req(state["family_level_observation"]["new_common_unsat_cause_found"] is False and state["family_level_observation"]["new_symbolic_obstruction_candidate_found"] is False, "family-level promotion drift")
    req(state["ownership_firewall"]["solver_equivalence_promoted"] is False and state["ownership_firewall"]["main_global_residual_feasibility_competition"] is False and state["ownership_firewall"]["heavy_compute_authorized"] is False, "ownership firewall drift")
    req(state["credit"]["additional_pruning_terminals"] == 0 and state["credit"]["numerical_leaf_compression_credit"] is False, "unexpected N392 pruning/compression credit")
    for key in ("main_pruning_credit","full178_complete","effectivity_final","receiver_credit","theorem_credit","endpoint_credit","stage32_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","merge_authorized"):
        req(state["credit"][key] is False, f"N392 credit firewall drift: {key}")

    print("PASS_N392_V24_MASS6_13_BLOCK_SIGNATURE_CENSUS")
    print("blocks=13 identities=1469 fixed_mass=6")
    print("abc_classes=(2,2,2):9,(0,2,4):2,(0,4,2):2")
    print("g3_distribution=2:11,4:2 pruning_credit=0 compression_credit=false")

if __name__ == "__main__":
    main()
