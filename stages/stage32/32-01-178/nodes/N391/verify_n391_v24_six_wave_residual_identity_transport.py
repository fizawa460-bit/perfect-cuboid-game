#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

WIDTH = 113
ROW = "g1-d008"
CURRENT_PREFIX_BLOCKS = 7596
CURRENT_PREFIX_STREAM = "529b9c31d36c517484dc176ba1d37674790eec05dc01853f9ce93b36e416c8e3"

EXPECTED = {
    "result_canonical": "2b30f97aca0873568c324cf9a88ba6dc8ee0e3cceb29e1fc60e9e2c978b02da3",
    "state_canonical": "9857cfc21ef4efe4539c36d2893981432a16fc49fe80bbd8e537f9042099c3d8",
    "n390_audit_blob": "cce347854e35c7611adb42d381fa8e87e03dae01",
    "n390_audit_canonical": "ab3bd3ec7a57d31e0e1be8a2ed33afb6b3d7069b3826dcf3d353635a847301d9",
    "n390_audit_head": "eee37af18eb4304bc816f37a6dbc79e76fe23c94",
    "n390_audit_review": 5193499219,
    "n356_result_blob": "677b1ae2bab910db0805d20ee489d922522919ed",
    "n356_result_canonical": "d1aecec8b78c78f03fa7b82b3dc136668f435d9cfb98636a1a23b704431abe31",
    "n356_audit_blob": "b6dd078c258c51b88c7fccb791893af6dc7a81f1",
    "n356_audit_canonical": "b710cb0fdaf9f5308655e3c5491ec4017e5f19a6a82f3fd5477a8e2396881505",
    "n357_verifier_blob": "fdca9ad629983d8c31c7e6355540af3545910120",
    "indexer_blob": "4fb0a8dd34909494bd62646373e42877ed7a3c9e",
    "family_blob": "90ff82ed312dcc0cb32cf207935945f550e29170",
    "main_head": "a89580f3fcf42152b47673d2cfec1935c72555c2",
    "main_blob": "b8df16056625db5fbb1947f1e927593de258f1ff",
    "main_canonical": "bdaab3df8871e656652e5c1f78f972405081a45b8d5e421cc4a9bacddef3bf5d",
    "n358_blob": "efa87a1b62cc698745f87814cd8f9eb9fe95dbd2",
    "n358_canonical": "27c50848e19c242389298b6a23d7c5b6a8ea86afd97c36ced16905adc66a5bdc",
    "certlift_head": "289437a4a97a814c2388133cbde0c794d9502e4b",
    "certlift_ledger_blob": "befce1cd6cd3fe9be9d91cb4b4f176283983bac1",
    "certlift_ledger_canonical": "529e30d5793a04e48b5413880758ca15d6c814b9bce656c2378f2361c766b836",
    "certlift_symbolic_blob": "56003ce22f8cc84f18311e6f11eecd6e65824d44",
    "hpadj_head": "8d8f1116d82f873d2cddafdd4d3619fb8649891b",
    "hpadj_correction_blob": "c90b41dcfbd5bd081629a6fa62d9447d43cb3d5e",
    "hpadj_correction_canonical": "87e9ee4ea791d894f5f1ba093d5ad295ad2ebb3d569f2f50fa9a1b1d4c1858aa",
    "block_stream": "b28506a8c959f521f4299338cc49899078e28ab5faa73b0736d9e1c877d12f56",
    "offset_stream": "a07d22bd500a7e9a45dd22285fc1b0c6767c6a81a6f9cefe4c2283c2df722e0f",
    "base_matrix": "4eddd29031a72faeff00a1fdbcd12ad086b2cd371a92408e0440efaed346a50d",
    "rank_stream": "6b699fdf0e8735a489b2d6086b18a074817af211583b8be266ddcd804f5a8cce",
    "identity_stream": "80028b025feacf650a778d9f314c23b8eb2c00a19ab59ad4dd134c76116de6f0",
}

CUTS = {
    "CUT193": {
        "head": "5b2ebb3f67805eddefef835878ba4b9744bfdbd9",
        "path": "stages/stage32/full178-cut/CUT193-e8-common-adapter-wave1-result.json",
        "blob": "ef72967a97e41287671f25647ad6fc24aef31ccb",
        "canonical": "161abe2cf9a00b95ce2b1acd422008bbb5c72929ea7a72e9892b94546abae2c1",
        "offsets": [1, 255],
        "residual": 28,
    },
    "CUT194": {
        "head": "847f3bff0c5e0d0530bfb8db406e955b2d231d9a",
        "path": "stages/stage32/full178-cut/CUT194-e8-common-adapter-wave2-result.json",
        "blob": "dab1a28f55918b617112799f11ac9614eb8a481c",
        "canonical": "c63f6da3dd0ec443572f8561bb7774491ce7d7c09ce319a322fb52e5b1e08cd4",
        "offsets": [256, 510],
        "residual": 21,
    },
    "CUT195": {
        "head": "2618f4dcd546d569b212753ac7abc10e07ee5828",
        "path": "stages/stage32/full178-cut/CUT195-e8-common-adapter-wave3-result.json",
        "blob": "d9fe913dccd41446780dbdde9f0200970ee9129e",
        "canonical": "1a7d802f427761d304ee06451d00ea67a1365d7d2629cdbf2ac88b6b4ff08aed",
        "offsets": [511, 765],
        "residual": 23,
    },
    "CUT196": {
        "head": "85f4e988acf6446fa0d472208e21990621a650b4",
        "path": "stages/stage32/full178-cut/CUT196-e8-common-adapter-wave4-result.json",
        "blob": "ae23ce6c44f69f9b2abe15e5aff09c2a10c45fde",
        "canonical": "194a37f87355f781f9aca341f9935645d818d5daa1c377883606627c80558a92",
        "offsets": [766, 1020],
        "residual": 13,
    },
    "CUT197": {
        "head": "adce53dc9004c24bffb3ba9f88e9d5d6e51cf6a5",
        "path": "stages/stage32/full178-cut/CUT197-e8-common-adapter-wave5-result.json",
        "blob": "e98f33ef093003e724ff6574bfec546ab1221955",
        "canonical": "f99d0f051ce95e269658e0ec945d727db32a94687bfd8acde5ee354e00776fa0",
        "offsets": [1021, 1275],
        "residual": 5,
    },
    "CUT198": {
        "head": "16e439bc65e723c9f2658c274d53fb839738dcd2",
        "path": "stages/stage32/full178-cut/CUT198-e8-common-adapter-wave6-result.json",
        "blob": "29a392b20d3f88519f5e8a6f3d2225ec5955bcb2",
        "canonical": "60f2d1d4d926d3f0c527a15fb2978d11dea7ca5dc9d02825c2671fc793618607",
        "offsets": [1276, 1530],
        "residual": 7,
    },
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
    for cut in CUTS:
        ap.add_argument(f"--{cut.lower()}-root", type=Path, required=True)
    ap.add_argument("--certlift-root", type=Path, required=True)
    ap.add_argument("--hpadj-root", type=Path, required=True)
    args = ap.parse_args()

    repo = Path(__file__).resolve().parents[5]
    residual_dir = repo / "stages/stage32/residual-32-01-production"
    idx_path = residual_dir / "compressed_terminal_indexer.py"
    fam_path = residual_dir / "compressed_terminal_family.py"
    n357_path = repo / "stages/stage32/verify_n357_v13_current_authority_composition.py"

    req(blob(idx_path) == EXPECTED["indexer_blob"], "indexer blob drift")
    req(blob(fam_path) == EXPECTED["family_blob"], "family blob drift")
    req(blob(n357_path) == EXPECTED["n357_verifier_blob"], "N357 verifier blob drift")

    result = checked(
        repo / "stages/stage32/32-01-178/nodes/N391/RESULT.json",
        None,
        EXPECTED["result_canonical"],
    )
    state = checked(
        repo / "stages/stage32/32-01-178/nodes/N391/STATE.json",
        None,
        EXPECTED["state_canonical"],
    )
    n390 = checked(
        repo / "stages/stage32/32-01-178/nodes/N390/AUDIT-PASS.json",
        EXPECTED["n390_audit_blob"],
        EXPECTED["n390_audit_canonical"],
    )
    req(
        n390["status"] == "HOSTILE_AUDIT_PASS"
        and n390["audited_exact_head"] == EXPECTED["n390_audit_head"]
        and int(n390["review_id"]) == EXPECTED["n390_audit_review"],
        "N390 audit receipt drift",
    )

    n356 = checked(
        repo / "stages/stage32/32-01-178/nodes/N356/RESULT.json",
        EXPECTED["n356_result_blob"],
        EXPECTED["n356_result_canonical"],
    )
    n356_audit = checked(
        repo / "stages/stage32/32-01-178/nodes/N356/HOSTILE-AUDIT-PASS.json",
        EXPECTED["n356_audit_blob"],
        EXPECTED["n356_audit_canonical"],
    )
    req(n356_audit["status"] == "PASS", "N356 audit status drift")
    req(
        n356["transport_contract"]["even_degree_specialization"] == "b-c<=3*d-e",
        "N356 cut drift",
    )

    sys.path.insert(0, str(residual_dir))
    from compressed_terminal_indexer import CompressedTerminalIndexer

    idx = CompressedTerminalIndexer(8, 8)
    req(idx.normal_budget + 1 == WIDTH, "block width drift")
    n357 = load_module(n357_path, "n391_n357")
    assignment_order = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
    req(n357.ASSIGNMENT_ORDER == assignment_order, "assignment order drift")

    survivors: list[int] = []
    for block_index in range(idx.exceptional_count):
        base = tuple(int(v) for v in idx.unrank(block_index * WIDTH))
        req(base[4] == 0, "block-base x4 drift")
        if n357.prefix_survives(base):
            survivors.append(block_index)
    req(len(survivors) == CURRENT_PREFIX_BLOCKS, "current-prefix block count drift")
    req(line_stream(survivors) == CURRENT_PREFIX_STREAM, "current-prefix stream drift")

    cert_root = args.certlift_root.resolve()
    req(exact_head(cert_root) == EXPECTED["certlift_head"], "CERTLIFT head drift")
    ledger = checked(
        cert_root / "stages/stage32/cert-lift/CERTIFICATE-LEDGER.json",
        EXPECTED["certlift_ledger_blob"],
        EXPECTED["certlift_ledger_canonical"],
    )
    sym = checked(
        cert_root / "stages/stage32/cert-lift/CERTLIFT-03-G3-MASS7-SYMBOLIC-RECEIPT.json",
        EXPECTED["certlift_symbolic_blob"],
        None,
    )
    req(ledger["profile"]["residual_total"] == 97, "CERTLIFT residual total drift")
    req(ledger["candidate_rule"]["selected_residual_blocks"] == 0, "CERTLIFT MASS7 residual selection drift")
    req(
        sym["predicate"]["fixed_exceptional_mass_lower_bound"] == 7
        and sym["predicate"]["g3_sum"] == 3,
        "CERTLIFT symbolic predicate drift",
    )

    all_blocks: list[int] = []
    all_offsets: list[int] = []
    seen: set[int] = set()

    ledger_waves = {w["id"]: w for w in ledger["waves"]}
    for cut_id, spec in CUTS.items():
        root = getattr(args, f"{cut_id.lower()}_root").resolve()
        req(exact_head(root) == spec["head"], f"{cut_id} exact head drift")
        cut = checked(root / spec["path"], spec["blob"], spec["canonical"])

        lo, hi = spec["offsets"]
        req(cut["target"]["survivor_offset_range"] == [lo, hi], f"{cut_id} offset range drift")
        expected_target = survivors[lo : hi + 1]
        req(cut["target"]["block_indices"] == expected_target, f"{cut_id} target block identity drift")

        closed = list(map(int, cut["result"]["candidate_closed_block_indices"]))
        closed_set = set(closed)
        residual_blocks = [b for b in expected_target if b not in closed_set]
        req(len(residual_blocks) == spec["residual"], f"{cut_id} residual count drift")
        req(
            cut["result"]["candidate_pruned_terminals"] == len(closed) * WIDTH,
            f"{cut_id} blockwise pruning count drift",
        )

        lw = ledger_waves[cut_id]
        req(lw["exact_head"] == spec["head"], f"{cut_id} ledger head drift")
        req(lw["result_canonical"] == spec["canonical"], f"{cut_id} ledger canonical drift")
        req(lw["offsets"] == [lo, hi], f"{cut_id} ledger offsets drift")
        req(lw["residual_blocks"] == residual_blocks, f"{cut_id} ledger residual identities drift")
        req(lw["residual"] == len(residual_blocks), f"{cut_id} ledger residual count drift")

        rr = result["waves"][cut_id]
        req(rr["residual_blocks"] == residual_blocks, f"{cut_id} N391 residual identities drift")
        req(line_stream(residual_blocks) == rr["residual_block_stream_sha256"], f"{cut_id} residual stream drift")

        offsets = [survivors.index(b) for b in residual_blocks]
        req(all(lo <= o <= hi for o in offsets), f"{cut_id} residual offset outside wave")
        req(line_stream(offsets) == rr["residual_offset_stream_sha256"], f"{cut_id} offset stream drift")

        for b in residual_blocks:
            req(b not in seen, f"duplicate residual block across waves: {b}")
            seen.add(b)
        all_blocks.extend(residual_blocks)
        all_offsets.extend(offsets)

    req(len(all_blocks) == 97 and len(seen) == 97, "six-wave residual union drift")
    req(line_stream(all_blocks) == EXPECTED["block_stream"], "six-wave residual block stream drift")
    req(line_stream(all_offsets) == EXPECTED["offset_stream"], "six-wave residual offset stream drift")

    group_labels = [[101, 102, 103], [97, 98, 99], [93, 94, 95, 96]]
    base_vectors: list[list[int]] = []
    ranks: list[int] = []
    identities: list[str] = []
    masses: list[int] = []
    b_minus_c: list[int] = []

    for block_index in all_blocks:
        base = list(map(int, idx.unrank(block_index * WIDTH)))
        req(base[4] == 0, f"block {block_index} x4 base drift")
        req(idx.rank(tuple(base)) == block_index * WIDTH, f"block {block_index} base rank drift")
        req(n357.prefix_survives(tuple(base)), f"block {block_index} prefix rejected")
        req(n357.n357_accepts(tuple(base)), f"block {block_index} N357 rejected")
        base_vectors.append(base)

        by = dict(zip(assignment_order, base))
        fixed_mass = sum(v for label, v in by.items() if label != 49)
        groups = [sum(by[label] for label in labels) for labels in group_labels]
        masses.append(fixed_mass)
        b_minus_c.append(groups[1] - groups[2])
        req(groups[1] - groups[2] <= 16, f"block {block_index} N356 rejected")
        req(fixed_mass <= 6, f"block {block_index} unexpectedly enters MASS7 predicate")

        for x4 in range(WIDTH):
            vals = list(base)
            vals[4] = x4
            rank = block_index * WIDTH + x4
            req(idx.rank(tuple(vals)) == rank, f"rank roundtrip drift at {rank}")
            req(n357.prefix_survives(tuple(vals)), f"prefix rejects rank {rank}")
            req(n357.n357_accepts(tuple(vals)), f"N357 rejects rank {rank}")
            ranks.append(rank)
            identities.append(f"g1-d008|e=8|rank={rank}")

    req(csha(base_vectors) == EXPECTED["base_matrix"], "base pairing matrix drift")
    req(line_stream(ranks) == EXPECTED["rank_stream"], "rank stream drift")
    req(line_stream(identities) == EXPECTED["identity_stream"], "identity stream drift")
    req(len(ranks) == 10961, "identity cardinality drift")
    req(min(b_minus_c) == -3 and max(b_minus_c) == 4, "N356 observed range drift")

    mass_dist = Counter(masses)
    expected_mass = {2: 2, 3: 15, 4: 37, 5: 30, 6: 13}
    req(dict(sorted(mass_dist.items())) == expected_mass, "residual mass distribution drift")
    for mass, counts in ledger["profile"]["mass_bins"].items():
        m = int(mass)
        expected_res = expected_mass.get(m, 0)
        req(int(counts["residual"]) == expected_res, f"CERTLIFT residual mass-bin drift at {m}")

    main_root = args.main_v24_root.resolve()
    req(exact_head(main_root) == EXPECTED["main_head"], "V24 MAIN head drift")
    main_state = checked(
        main_root / "stages/stage32/MAIN-STATE.json",
        EXPECTED["main_blob"],
        EXPECTED["main_canonical"],
    )
    f = main_state["current_exact_frontier"]
    req(
        f["authoritative_remaining_terminals_semantics"]
        == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET",
        "V24 residual semantics drift",
    )
    for key in (
        "cut193_main_pruning_credit",
        "cut194_main_pruning_credit",
        "cut195_main_pruning_credit",
        "cut196_main_pruning_credit",
        "cut197_main_pruning_credit",
        "cut198_main_pruning_credit",
        "n358_main_pruning_credit",
        "certlift03_main_pruning_credit",
        "hpadj07_main_pruning_credit",
    ):
        req(f.get(key) is True, f"V24 consumed-credit drift: {key}")
    req(
        f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False,
        "V24 closure firewall drift",
    )

    n358 = checked(
        main_root / "stages/stage32/management/post-n358-current-v18-composition-consumption-20260912.json",
        EXPECTED["n358_blob"],
        EXPECTED["n358_canonical"],
    )
    zero = n358["current_v18_composition_replay"]["zero_overlap_reason"]
    req(
        zero["equivalently_n358_incremental_domain_empty_on_g1_d008_e8"] is True,
        "N358 e8 empty-domain drift",
    )

    hpadj_root = args.hpadj_root.resolve()
    req(exact_head(hpadj_root) == EXPECTED["hpadj_head"], "HPADJ head drift")
    hpadj = checked(
        hpadj_root / "stages/stage32/management/hpadj-07/proof-chain/GENERAL-TYPE-ADJUNCTION-CORRECTION.json",
        EXPECTED["hpadj_correction_blob"],
        EXPECTED["hpadj_correction_canonical"],
    )
    req(
        ROW in hpadj["corrected_v22_conservative_replay"]["zero_rejection_rows"],
        "HPADJ no longer has g1-d008 as zero-rejection row",
    )

    req(result["scope"]["residual_block_count"] == 97, "N391 result block count drift")
    req(result["scope"]["subset_cardinality"] == 10961, "N391 result identity count drift")
    req(result["transport_checks"]["certlift03"]["max_fixed_exceptional_mass"] == 6, "N391 MASS7 firewall drift")
    req(result["known_picard_status"]["n391_additional_picard64_witness_claims"] == 0, "N391 Picard promotion drift")
    req(state["ownership_firewall"]["main_global_residual_feasibility_competition"] is False, "N391 MAIN competition firewall drift")
    req(state["ownership_firewall"]["heavy_compute_authorized"] is False, "N391 heavy firewall drift")
    req(state["credit"]["additional_pruning_terminals"] == 0, "N391 unexpected pruning credit")
    for k in (
        "main_pruning_credit",
        "full178_complete",
        "effectivity_final",
        "receiver_credit",
        "theorem_credit",
        "endpoint_credit",
        "stage32_closed",
        "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim",
        "merge_authorized",
    ):
        req(state["credit"][k] is False, f"N391 credit firewall drift: {k}")

    print("PASS_N391_V24_CUT193_198_RESIDUAL_97_BLOCK_IDENTITY_TRANSPORT")
    print("blocks=97 identities=10961 width=113")
    print("mass_distribution=2:2,3:15,4:37,5:30,6:13")
    print("picard64_additional_claims=0 pruning_credit=0")


if __name__ == "__main__":
    main()
