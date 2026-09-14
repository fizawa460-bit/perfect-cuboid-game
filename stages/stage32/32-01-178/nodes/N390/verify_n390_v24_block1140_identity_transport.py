#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

BLOCK = 1140
OFFSET = 797
WIDTH = 113
R0 = BLOCK * WIDTH
R1 = R0 + WIDTH - 1

EXPECTED = {
    "result_canonical": "4b5083e1a8319fc0e001fe4ad5feb72b52a1204ce63ec09cae5f6c2139a0429f",
    "state_canonical": "872ca087bc227016821365ed9af0b588cd320d4040b75f92353a9ea35bf032e5",
    "n389_audit_blob": "dc6a2fd770cebb57f4bd2a931a59e04db0c12776",
    "n389_audit_canonical": "e4f4ccd99ae973abf997cfe8438603ec9c6f427a54a3323a5f557db2cc2651ec",
    "n356_result_blob": "677b1ae2bab910db0805d20ee489d922522919ed",
    "n356_result_canonical": "d1aecec8b78c78f03fa7b82b3dc136668f435d9cfb98636a1a23b704431abe31",
    "n356_audit_blob": "b6dd078c258c51b88c7fccb791893af6dc7a81f1",
    "n356_audit_canonical": "b710cb0fdaf9f5308655e3c5491ec4017e5f19a6a82f3fd5477a8e2396881505",
    "n357_verifier_blob": "fdca9ad629983d8c31c7e6355540af3545910120",
    "indexer_blob": "4fb0a8dd34909494bd62646373e42877ed7a3c9e",
    "family_blob": "90ff82ed312dcc0cb32cf207935945f550e29170",
    "n372_result_blob": "c0267d903fd0b397fcd4766b03964bde788650e7",
    "n372_result_canonical": "b9852fcfa926e77e8c51defe31002e0bf4b281dd1db4b5f320326166932fef48",
    "main_head": "a89580f3fcf42152b47673d2cfec1935c72555c2",
    "main_blob": "b8df16056625db5fbb1947f1e927593de258f1ff",
    "main_canonical": "bdaab3df8871e656652e5c1f78f972405081a45b8d5e421cc4a9bacddef3bf5d",
    "n358_blob": "efa87a1b62cc698745f87814cd8f9eb9fe95dbd2",
    "n358_canonical": "27c50848e19c242389298b6a23d7c5b6a8ea86afd97c36ced16905adc66a5bdc",
    "cut196_head": "85f4e988acf6446fa0d472208e21990621a650b4",
    "cut196_blob": "ae23ce6c44f69f9b2abe15e5aff09c2a10c45fde",
    "cut196_canonical": "194a37f87355f781f9aca341f9935645d818d5daa1c377883606627c80558a92",
    "certlift_head": "289437a4a97a814c2388133cbde0c794d9502e4b",
    "certlift_adapter_blob": "327aa601acad47bc1e486cccbbac3d3dee7c2681",
    "certlift_receipt_blob": "291bb8b125566bb72c1caae0537dff2625219ffb",
    "certlift_receipt_canonical": "983042fb058d60b9c2ab39ee24c7192d93fec92ab6c9b81c840c91903133c858",
    "certlift_symbolic_blob": "56003ce22f8cc84f18311e6f11eecd6e65824d44",
    "hpadj_head": "8d8f1116d82f873d2cddafdd4d3619fb8649891b",
    "hpadj_correction_blob": "c90b41dcfbd5bd081629a6fa62d9447d43cb3d5e",
    "hpadj_correction_canonical": "87e9ee4ea791d894f5f1ba093d5ad295ad2ebb3d569f2f50fa9a1b1d4c1858aa",
    "hpadj_rebase_blob": "8883cfc59a6d48e34d7e256fad15e69714dc02d1",
    "hpadj_rebase_canonical": "9ae15dd70a3ba84fe83d2d11dfa8e1081c44a8b06e68b78dda4f871aa0f00e01",
    "identity_stream": "35a5fe8beb3c7d0875602feb5cdc2fdb8240963533971a568a80fb31357c9f76",
    "rank_stream": "b7b5b94b398322461e9c08a645bbae8bb32ab23afa9c1c75ff7c36c637da924f",
    "pairing_matrix": "bc51d0f83367cd7d1c2f58caf2d8108af7135d8c58d5fc84bdb70d4932ff6b1e",
}

def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(msg)

def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()

def checked(path: Path, expected_blob: str | None, expected_canonical: str | None) -> dict:
    req(path.is_file(), f"missing source: {path}")
    if expected_blob is not None:
        req(blob(path) == expected_blob, f"blob drift: {path}")
    obj = json.loads(path.read_text())
    if expected_canonical is not None:
        body = dict(obj)
        claimed = body.pop("canonical_sha256_without_this_field", None)
        req(claimed == expected_canonical and csha(body) == expected_canonical, f"canonical drift: {path}")
    return obj

def exact_head(root: Path) -> str:
    return subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()

def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod

def line_stream(values) -> str:
    h = hashlib.sha256()
    for value in values:
        h.update(f"{value}\n".encode())
    return h.hexdigest()

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--main-v24-root", type=Path, required=True)
    ap.add_argument("--cut196-root", type=Path, required=True)
    ap.add_argument("--certlift-root", type=Path, required=True)
    ap.add_argument("--hpadj-root", type=Path, required=True)
    args = ap.parse_args()

    repo = Path(__file__).resolve().parents[5]
    residual = repo / "stages/stage32/residual-32-01-production"
    idx_path = residual / "compressed_terminal_indexer.py"
    fam_path = residual / "compressed_terminal_family.py"
    n357_path = repo / "stages/stage32/verify_n357_v13_current_authority_composition.py"
    req(blob(idx_path) == EXPECTED["indexer_blob"], "indexer blob drift")
    req(blob(fam_path) == EXPECTED["family_blob"], "family blob drift")
    req(blob(n357_path) == EXPECTED["n357_verifier_blob"], "N357 verifier blob drift")

    result = checked(repo / "stages/stage32/32-01-178/nodes/N390/RESULT.json", None, EXPECTED["result_canonical"])
    state = checked(repo / "stages/stage32/32-01-178/nodes/N390/STATE.json", None, EXPECTED["state_canonical"])
    n389 = checked(repo / "stages/stage32/32-01-178/nodes/N389/AUDIT-PASS.json", EXPECTED["n389_audit_blob"], EXPECTED["n389_audit_canonical"])
    req(n389["status"] == "HOSTILE_AUDIT_PASS" and n389["review_id"] == 5193336799, "N389 audit receipt drift")
    n372 = checked(repo / "stages/stage32/32-01-178/nodes/N372/RESULT.json", EXPECTED["n372_result_blob"], EXPECTED["n372_result_canonical"])
    req(n372["witness"]["terminal_identity"] == "g1-d008|e=8|rank=128820", "N372 witness moved")

    n356 = checked(repo / "stages/stage32/32-01-178/nodes/N356/RESULT.json", EXPECTED["n356_result_blob"], EXPECTED["n356_result_canonical"])
    n356_audit = checked(repo / "stages/stage32/32-01-178/nodes/N356/HOSTILE-AUDIT-PASS.json", EXPECTED["n356_audit_blob"], EXPECTED["n356_audit_canonical"])
    req(n356_audit["status"] == "PASS" and n356_audit["review_id"] == 5176607630, "N356 audit receipt drift")
    req(n356["transport_contract"]["even_degree_specialization"] == "b-c<=3*d-e", "N356 cut drift")

    sys.path.insert(0, str(residual))
    from compressed_terminal_indexer import CompressedTerminalIndexer
    idx = CompressedTerminalIndexer(8, 8)
    req(idx.normal_budget + 1 == WIDTH, "block width drift")
    n357 = load_module(n357_path, "n390_n357")
    req(n357.ASSIGNMENT_ORDER == [95,99,103,102,49,97,94,101,93,98,96], "assignment order drift")

    identities, ranks, vectors = [], [], []
    expected_base = [0,1,1,0,0,0,1,0,1,0,0]
    for x4, rank in enumerate(range(R0, R1 + 1)):
        vals = list(map(int, idx.unrank(rank)))
        req(vals[4] == x4, f"x4/rank drift at {rank}")
        req(vals[:4] + vals[5:] == expected_base[:4] + expected_base[5:], f"exceptional block drift at {rank}")
        req(idx.rank(tuple(vals)) == rank, f"rank roundtrip drift at {rank}")
        req(n357.prefix_survives(tuple(vals)), f"pre-N357 prefix rejects {rank}")
        req(n357.n357_accepts(tuple(vals)), f"N357 rejects {rank}")
        identities.append(f"g1-d008|e=8|rank={rank}")
        ranks.append(rank)
        vectors.append(vals)
    req(line_stream(identities) == EXPECTED["identity_stream"], "identity stream drift")
    req(line_stream(ranks) == EXPECTED["rank_stream"], "rank stream drift")
    req(csha(vectors) == EXPECTED["pairing_matrix"], "pairing matrix drift")

    by = dict(zip(n357.ASSIGNMENT_ORDER, expected_base))
    groups = [[101,102,103],[97,98,99],[93,94,95,96]]
    sums = [sum(by[x] for x in group) for group in groups]
    req(sums == [1,1,2] and sums[1] - sums[2] <= 16, "N356 block survival drift")

    main_root = args.main_v24_root.resolve()
    req(exact_head(main_root) == EXPECTED["main_head"], "V24 MAIN head drift")
    main_state = checked(main_root / "stages/stage32/MAIN-STATE.json", EXPECTED["main_blob"], EXPECTED["main_canonical"])
    f = main_state["current_exact_frontier"]
    req(f["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "V24 semantics drift")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False, "V24 closure drift")
    for key in ("cut196_main_pruning_credit","cut193_main_pruning_credit","cut197_main_pruning_credit","cut198_main_pruning_credit","n358_main_pruning_credit","certlift03_main_pruning_credit","hpadj07_main_pruning_credit"):
        req(f.get(key) is True, f"V24 consumed-credit drift: {key}")
    ranges = [main_state["source_locks"]["batch_cut_candidates"][k]["offset_range"] for k in ("CUT193","CUT197","CUT198")]
    req(all(not (lo <= OFFSET <= hi) for lo, hi in ranges), "block1140 overlaps later batch CUT")

    n358 = checked(main_root / "stages/stage32/management/post-n358-current-v18-composition-consumption-20260912.json", EXPECTED["n358_blob"], EXPECTED["n358_canonical"])
    zero = n358["current_v18_composition_replay"]["zero_overlap_reason"]
    req(zero["equivalently_n358_incremental_domain_empty_on_g1_d008_e8"] is True, "N358 e8 empty-domain drift")

    cut_root = args.cut196_root.resolve()
    req(exact_head(cut_root) == EXPECTED["cut196_head"], "CUT196 head drift")
    cut = checked(cut_root / "stages/stage32/full178-cut/CUT196-e8-common-adapter-wave4-result.json", EXPECTED["cut196_blob"], EXPECTED["cut196_canonical"])
    req(cut["target"]["survivor_offset_range"] == [766,1020], "CUT196 offset drift")
    req(BLOCK in cut["target"]["block_indices"], "block1140 not targeted by CUT196")
    closed = cut["result"]["candidate_closed_block_indices"]
    req(BLOCK not in closed, "CUT196 closes block1140")
    req(cut["result"]["candidate_pruned_terminals"] == len(closed) * WIDTH, "CUT196 blockwise count drift")
    req(cut["result"]["remaining_nonclosed_block_count"] == 13, "CUT196 residual count drift")

    cert_root = args.certlift_root.resolve()
    req(exact_head(cert_root) == EXPECTED["certlift_head"], "CERTLIFT head drift")
    req(blob(cert_root / "stages/stage32/cert-lift/certlift03_v22_consumption_adapter.py") == EXPECTED["certlift_adapter_blob"], "CERTLIFT adapter blob drift")
    cert_receipt = checked(cert_root / "stages/stage32/cert-lift/CERTLIFT-03-V22-CONSUMPTION-ADAPTER-RECEIPT.json", EXPECTED["certlift_receipt_blob"], EXPECTED["certlift_receipt_canonical"])
    sym = checked(cert_root / "stages/stage32/cert-lift/CERTLIFT-03-G3-MASS7-SYMBOLIC-RECEIPT.json", EXPECTED["certlift_symbolic_blob"], None)
    req(cert_receipt["population"]["target_blocks"] == 1677, "CERTLIFT target count drift")
    pred = sym["predicate"]
    req(pred["fixed_exceptional_mass_lower_bound"] == 7 and pred["g3_labels"] == [93,94,95,96] and pred["g3_sum"] == 3, "CERTLIFT predicate drift")
    fixed_mass = sum(v for label, v in by.items() if label != 49)
    g3 = sum(by[label] for label in [93,94,95,96])
    req((fixed_mass, g3) == (4,2), "block1140 CERTLIFT signature drift")
    req(not (fixed_mass >= 7 and g3 == 3), "block1140 enters CERTLIFT target")

    hp_root = args.hpadj_root.resolve()
    req(exact_head(hp_root) == EXPECTED["hpadj_head"], "HPADJ head drift")
    corr = checked(hp_root / "stages/stage32/management/hpadj-07/proof-chain/GENERAL-TYPE-ADJUNCTION-CORRECTION.json", EXPECTED["hpadj_correction_blob"], EXPECTED["hpadj_correction_canonical"])
    reb = checked(hp_root / "stages/stage32/management/hpadj-07/proof-chain/CURRENT-V23-CONSERVATIVE-REBASE.json", EXPECTED["hpadj_rebase_blob"], EXPECTED["hpadj_rebase_canonical"])
    req("g1-d008" in corr["corrected_v22_conservative_replay"]["zero_rejection_rows"], "HPADJ g1-d008 zero-row drift")
    req(reb["set_theoretic_rebase"]["requires_exact_overlap_for_exact_increment"] is False, "HPADJ rebase semantics drift")

    req(result["scope"]["terminal_rank_range"] == [R0,R1] and result["scope"]["subset_cardinality"] == WIDTH, "N390 result scope drift")
    req(result["known_picard_status"]["other_112_picard64_status"] == "UNCLAIMED", "N390 Picard overclaim")
    req(result["known_picard_status"]["n373_timeout_route_reopened"] is False, "N373 anti-loop drift")
    req(state["ownership_firewall"]["main_global_residual_feasibility_competition"] is False, "MAIN ownership violation")
    req(state["ownership_firewall"]["heavy_compute_authorized"] is False, "heavy compute armed")
    req(result["credit"]["additional_pruning_terminals"] == 0 and state["credit"]["additional_pruning_terminals"] == 0, "unexpected pruning credit")
    for obj in (result["credit"], state["credit"]):
        for key in ("main_pruning_credit","full178_complete","effectivity_final","receiver_credit","theorem_credit","endpoint_credit","stage32_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","merge_authorized"):
            req(obj[key] is False, f"credit firewall moved: {key}")

    print("PASS_N390_V24_BLOCK1140_113_IDENTITY_TRANSPORT")
    print(f"ranks={R0}..{R1} count={WIDTH}")
    print("picard64_status=rank128820_only_audited_other112_unclaimed")

if __name__ == "__main__":
    main()
