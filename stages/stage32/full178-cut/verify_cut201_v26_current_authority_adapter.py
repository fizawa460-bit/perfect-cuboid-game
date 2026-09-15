#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

EXPECTED_HANDOFF_CANON = "1c777be6bcce85c648b5c7a365cf9d4151bc72278438e738a58ef12b019e058a"
CUT201_HEAD = "8eed1449b325c3b990f90b61471bf7ecec0d89bc"
MAIN_V26_HEAD = "409767d0d4e51366afe17fcb600220b1f7627733"
CERTLIFT_AUDIT_RECEIPT_HEAD = "51c56b5c3ee15177c2975b966ab546d0b548c4af"
N400_HEAD = "b1a950cbc6edf3cb85e1ea79473105c6f1f67b03"
WIDTH = 113
PREFIX_COUNT = 7596
PREFIX_STREAM = "529b9c31d36c517484dc176ba1d37674790eec05dc01853f9ce93b36e416c8e3"


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def checked(path: Path, expected_blob: str, expected_canonical: str) -> dict:
    req(path.is_file(), f"missing source {path}")
    req(blob(path) == expected_blob, f"blob drift {path}")
    obj = json.loads(path.read_text())
    body = dict(obj)
    claimed = body.pop("canonical_sha256_without_this_field", None)
    req(claimed == expected_canonical and csha(body) == expected_canonical, f"canonical drift {path}")
    return obj


def head(root: Path) -> str:
    return subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()


def line_stream(values) -> str:
    h = hashlib.sha256()
    for value in values:
        h.update(f"{value}\n".encode())
    return h.hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cut201-root", type=Path, required=True)
    ap.add_argument("--main-v26-root", type=Path, required=True)
    ap.add_argument("--certlift-root", type=Path, required=True)
    ap.add_argument("--n400-root", type=Path, required=True)
    args = ap.parse_args()

    repo = Path(__file__).resolve().parents[3]
    handoff_path = repo / "stages/stage32/full178-cut/CUT201-V26-current-authority-adapter-handoff.json"
    handoff = json.loads(handoff_path.read_text())
    body = dict(handoff)
    claimed = body.pop("canonical_sha256_without_this_field", None)
    req(claimed == EXPECTED_HANDOFF_CANON and csha(body) == EXPECTED_HANDOFF_CANON, "handoff canonical drift")

    cut_root = args.cut201_root.resolve()
    main_root = args.main_v26_root.resolve()
    cert_root = args.certlift_root.resolve()
    n400_root = args.n400_root.resolve()
    req(head(cut_root) == CUT201_HEAD, "CUT201 audited checkout drift")
    req(head(main_root) == MAIN_V26_HEAD, "MAIN V26 request checkout drift")
    req(head(cert_root) == CERTLIFT_AUDIT_RECEIPT_HEAD, "CERTLIFT audit-receipt checkout drift")
    req(head(n400_root) == N400_HEAD, "N400 audited checkout drift")

    cut_dir = cut_root / "stages/stage32/full178-cut"
    cut_result = checked(cut_dir / "CUT201-e8-common-adapter-wave9-result.json", "ebdf1f741365f7403050f22b478eeea5a7a1d653", "8f9ccc51046b9559d15ee5d64ef72be35f798a740a78a85df92d865286dbd467")
    req(blob(cut_dir / "verify_cut201_e8_common_adapter_wave9.py") == "1aad3b1ffb54b1d3be8e4095091904826fbdfa43", "CUT201 verifier drift")
    sys.path.insert(0, str(cut_dir))
    cut = load_module(cut_dir / "cut201_e8_common_adapter_wave9.py", "cut201_v26_source")
    cut.preflight()
    survivors = cut.core.e8.current_main_survivor_block_indices()
    req(len(survivors) == PREFIX_COUNT and line_stream(survivors) == PREFIX_STREAM, "current-prefix stream drift")
    target = survivors[2041:2296]
    req(cut_result["target"]["survivor_offset_range"] == [2041, 2295], "CUT201 offset drift")
    req(cut_result["target"]["block_indices"] == target, "CUT201 target identity drift")
    closed = list(map(int, cut_result["result"]["candidate_closed_block_indices"]))
    req(len(closed) == 226 and len(set(closed)) == 226, "CUT201 closed-set count/uniqueness drift")
    req(line_stream(closed) == "86ef70cd38d91e7ffe49f6069c48440c388142f151abb89d126fcb88182642fb", "CUT201 closed-set stream drift")
    req(set(closed) <= set(target), "CUT201 closed set outside target")
    req(cut_result["result"]["candidate_pruned_terminals"] == 25538, "CUT201 candidate terminal count drift")

    main_state = checked(main_root / "stages/stage32/MAIN-STATE.json", "9242ffc2d44d68b7c6e3a3946fa26f18288fe51b", "39b66cb72dd60900158e60cbca9e0c8dbd15bff3d77f7d9ed2fd096e0f12b9dd")
    disposition = checked(main_root / "stages/stage32/management/cut201-main-disposition/CUT201-G11-V26-MAIN-DISPOSITION.json", "50707eaee4df3a71927967b7ba325939c3030c2f", "946ec777f824eaae75aa14d9c3ab5f348bfea38da020e72ede9750c914f86381")
    req(main_state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V26_N400_AUDIT_SYNCED", "V26 schema drift")
    f = main_state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128 and f["authoritative_remaining_terminals"] == 26876434389242951083886, "V26 authority drift")
    for key in ("cut191_main_pruning_credit","cut193_main_pruning_credit","cut194_main_pruning_credit","cut195_main_pruning_credit","cut196_main_pruning_credit","cut197_main_pruning_credit","cut198_main_pruning_credit","n358_main_pruning_credit","certlift03_main_pruning_credit","hpadj07_main_pruning_credit","n400_main_pruning_credit"):
        req(f.get(key) is True, f"V26 consumed-credit drift {key}")
    req(f.get("cut199_main_pruning_credit") is False, "unexpected CUT199 MAIN credit")
    req("cut200_main_pruning_credit" not in f, "unexpected CUT200 MAIN credit surface")
    req(disposition["main_disposition"]["cross_lane_demand_id"] == "S32.DEMAND.CUT201.CUT.MAIN.V26_CURRENT_AUTHORITY_ADAPTER.V1", "MAIN demand id drift")
    req(disposition["producer"]["audited_exact_head"] == CUT201_HEAD and disposition["producer"]["hostile_audit_review_id"] == 5204865930, "MAIN CUT201 source receipt drift")

    n358 = checked(main_root / "stages/stage32/management/post-n358-current-v18-composition-consumption-20260912.json", "efa87a1b62cc698745f87814cd8f9eb9fe95dbd2", "27c50848e19c242389298b6a23d7c5b6a8ea86afd97c36ced16905adc66a5bdc")
    zero = n358["current_v18_composition_replay"]["zero_overlap_reason"]
    req(zero["equivalently_n358_incremental_domain_empty_on_g1_d008_e8"] is True, "N358 g1-d008/e8 zero-domain drift")

    hpadj = checked(main_root / "stages/stage32/management/hpadj-07/HPADJ07-V23-MAIN-CONSUMPTION.json", "e942711b67ebc43b39a73ab55bc10862654059f8", "6fc1800b84de587e2218c372966e1424186405e57477586e8a284961f575f417")
    req(hpadj["hostile_audit_source"]["hostile_audit_review_id"] == 5191822227, "HPADJ07 audit receipt drift")
    req(hpadj["promotion"]["main_pruning_credit_consumed"] is True, "HPADJ07 consumption drift")
    req("g1-d008/e8 slice" in hpadj["preserved_witnesses"]["reason"], "HPADJ07 g1-d008/e8 charged-slice exclusion drift")
    correction = checked(main_root / "stages/stage32/management/hpadj-07/proof-chain/GENERAL-TYPE-ADJUNCTION-CORRECTION.json", "c90b41dcfbd5bd081629a6fa62d9447d43cb3d5e", "87e9ee4ea791d894f5f1ba093d5ad295ad2ebb3d569f2f50fa9a1b1d4c1858aa")
    req("g1-d008" in correction["corrected_v22_conservative_replay"]["zero_rejection_rows"], "HPADJ07 row-zero replay drift")

    cert_receipt = checked(cert_root / "stages/stage32/cert-lift/CERTLIFT-03-V22-CONSUMPTION-ADAPTER-RECEIPT.json", "291bb8b125566bb72c1caae0537dff2625219ffb", "983042fb058d60b9c2ab39ee24c7192d93fec92ab6c9b81c840c91903133c858")
    cert_audit = checked(cert_root / "stages/stage32/cert-lift/CERTLIFT-03-V22-CONSUMPTION-ADAPTER-HOSTILE-AUDIT-PASS.json", "442f84b392254383736f1b695da7a9b2954c053d", "ceec3c102ad194c05e1429e7af293716a21993fb2dcfd531525c30c371bc2821")
    cert_ledger = checked(cert_root / "stages/stage32/cert-lift/CERTIFICATE-LEDGER.json", "befce1cd6cd3fe9be9d91cb4b4f176283983bac1", "529e30d5793a04e48b5413880758ca15d6c814b9bce656c2378f2361c766b836")
    req(cert_audit["status"] == "HOSTILE_AUDIT_PASS" and cert_audit["review_id"] == 5188860951, "CERTLIFT03 audit drift")
    req(cert_receipt["population"]["current_prefix_blocks"] == PREFIX_COUNT and cert_receipt["population"]["current_prefix_block_stream_sha256"] == PREFIX_STREAM, "CERTLIFT03 prefix identity drift")
    req(cert_receipt["predicate"] == {"d":8,"e":8,"fixed_exceptional_mass_lower_bound":7,"g3_labels":[93,94,95,96],"g3_sum":3}, "CERTLIFT03 predicate drift")
    req(cert_ledger["scope"]["current_main_survivor_offsets"] == [1,1530] and cert_ledger["scope"]["wave_count"] == 6, "CERTLIFT03 six-wave scope drift")
    req(max(hi for lo,hi in (w["offsets"] for w in cert_ledger["waves"])) == 1530, "prior CUT offset ceiling drift")

    cert_target = []
    for b in survivors:
        sig = cut.core.e8.block_signature(b)
        if int(sig["fixed_exceptional_mass"]) >= 7 and int(sig["n355_known_group_sums"][2]) == 3:
            cert_target.append(b)
    req(len(cert_target) == 1677 and line_stream(cert_target) == "c4c15d59240ffbbae50f7ec1184267966d722fb3242a8fb0b1dd632fa1035a43", "CERTLIFT03 exact target replay drift")
    cert_overlap = sorted(set(closed) & set(cert_target))
    incremental = sorted(set(closed) - set(cert_overlap))
    req(len(cert_overlap) == 60 and len(incremental) == 166, "CUT201/CERTLIFT03 partition count drift")
    req(line_stream(cert_overlap) == "df0e221744a44bc156ccc21d0be763e9c3e6572197cc740e152431174fe162ac", "CERTLIFT03 overlap block stream drift")
    req(line_stream(incremental) == "7a67d7f5071853f3376e0a8c39eacefd89eed37855b3f5b59b91d38da0c6a099", "incremental block stream drift")

    n400 = checked(n400_root / "stages/stage32/32-01-178/nodes/N400/RESULT.json", "485c9a0380788bedd25cde5a47204e2c8c62472e", "8459cd213cca964718b36c4bce7006439c85a2527943441ede1f286a7eb56dcb")
    n391 = checked(n400_root / "stages/stage32/32-01-178/nodes/N391/RESULT.json", "3e72cea011e5a519173a710c20d88bc781c4cee8", "2b30f97aca0873568c324cf9a88ba6dc8ee0e3cceb29e1fc60e9e2c978b02da3")
    req(n400["certificate"]["scope"] == "retained N391 97-block population only", "N400 source scope drift")
    req(n400["certificate"]["rejected_terminal_count"] == 5502 and n400["certificate"]["double_charge"] is False, "N400 result drift")
    req(n391["scope"]["terminal_rank_max"] == 234135, "N391 rank ceiling drift")

    candidate_ranks = [b * WIDTH + x4 for b in closed for x4 in range(WIDTH)]
    overlap_ranks = [b * WIDTH + x4 for b in cert_overlap for x4 in range(WIDTH)]
    incremental_ranks = [b * WIDTH + x4 for b in incremental for x4 in range(WIDTH)]
    candidate_ids = [f"g1-d008|e=8|rank={r}" for r in candidate_ranks]
    incremental_ids = [f"g1-d008|e=8|rank={r}" for r in incremental_ranks]
    req(min(candidate_ranks) > n391["scope"]["terminal_rank_max"], "CUT201/N400 rank-domain separation lost")
    req(len(candidate_ranks) == 25538 and len(overlap_ranks) == 6780 and len(incremental_ranks) == 18758, "terminal partition drift")
    req(line_stream(candidate_ranks) == "d38d02ad716d6f4983cff3a1e190091b9509a682734187fb3b0b4dcac8b19856", "candidate rank stream drift")
    req(line_stream(overlap_ranks) == "1965407afe06eab0abc4a7dc9efdade728c81823185cb0fd1745cb4246066aa0", "overlap rank stream drift")
    req(line_stream(incremental_ranks) == "dc61b63b1ff6ade5762e5e5930cdcb1f17f9eaffee90750a143a8d84d5107e83", "incremental rank stream drift")
    req(line_stream(candidate_ids) == "e356ff3832930e203cacf6ad42299c17cec52614d284b8b370b9987764eefeaf", "candidate identity stream drift")
    req(line_stream(incremental_ids) == "0fa6f9ac49363d6506080a96b3ceb3857f4ef21bbbc24222158e2fb57766a097", "incremental identity stream drift")

    pop = handoff["population"]
    ov = handoff["exact_overlap_by_consumed_route"]
    inc = handoff["exact_incremental_set"]
    req(pop["candidate_closed_block_indices"] == closed and pop["candidate_terminal_count"] == 25538, "handoff candidate set drift")
    req(ov["CERTLIFT03"]["overlap_block_indices"] == cert_overlap and ov["CERTLIFT03"]["overlap_terminals"] == 6780, "handoff CERTLIFT03 overlap drift")
    req(inc["incremental_block_indices"] == incremental and inc["incremental_terminal_count"] == 18758, "handoff incremental set drift")
    req(handoff["double_charge_certificate"]["double_charge"] is False and handoff["double_charge_certificate"]["all_overlap_is_certlift03"] is True, "handoff double-charge certificate drift")
    req(handoff["handoff"]["main_authority_subtraction_not_performed_by_producer"] is True, "producer MAIN mutation firewall drift")
    req(handoff["handoff"]["hostile_audit_required_before_demand_satisfaction"] is True, "audit-before-satisfaction firewall drift")
    req(all(v is False for v in handoff["credit_firewall"].values()), "credit firewall drift")

    print(json.dumps({
        "status":"PASS_CUT201_V26_CURRENT_AUTHORITY_ADAPTER_CANDIDATE",
        "candidate_blocks":226,
        "candidate_terminals":25538,
        "certlift03_overlap_blocks":60,
        "certlift03_overlap_terminals":6780,
        "other_consumed_route_overlap_terminals":0,
        "incremental_blocks":166,
        "exact_incremental_rejected_terminals":18758,
        "double_charge":False,
        "main_authority_subtraction_performed_by_producer":False,
        "hostile_audit_required":True
    }, sort_keys=True))


if __name__ == "__main__":
    main()
