#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

AUDITED_EX5_HEAD = "8bea7a6be26e01db0deb138dbd8406f578447921"
AUDITED_EX5_REVIEW = 5187359907
ADAPTER_REL = Path("stages/stage32-ex5/cut-handoff/e8_terminal_population_adapter.py")
ADAPTER_BLOB = "6026d2c8b4a2eb69c453a2bd38c5923f46d6d74f"
EXPECTED_BLOCKS = 7596
EXPECTED_TERMINALS = 858348
EXPECTED_RAW_PARENTS = 12357387


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_adapter(root: Path):
    head = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
    req(head == AUDITED_EX5_HEAD, f"audited EX5 head drift: {head}")
    path = root / ADAPTER_REL
    req(path.is_file(), "audited EX5 adapter missing")
    req(git_blob(path) == ADAPTER_BLOB, "audited EX5 adapter blob drift")
    spec = importlib.util.spec_from_file_location("stage32_main_hnf_probe_ex5_adapter", path)
    req(spec is not None and spec.loader is not None, "cannot load audited EX5 adapter")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def syndrome(rows: list[list[int]], modulus: int, exc_pos: dict[int, int], fixed: dict[int, int]) -> tuple[int, ...]:
    if modulus == 1:
        return ()
    out = []
    for row in rows:
        out.append(sum(int(row[exc_pos[label]]) * int(value) for label, value in fixed.items()) % modulus)
    return tuple(out)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--audited-ex5-root", type=Path, required=True)
    ap.add_argument("--json-output", type=Path)
    args = ap.parse_args()

    a = load_adapter(args.audited_ex5_root.resolve())
    g = a.load_geometry()
    idx = a.indexer()
    survivors = a.current_main_survivor_block_indices()
    req(len(survivors) == EXPECTED_BLOCKS, "current e8 survivor count drift")

    exc_pos = {int(label): i for i, label in enumerate(g.exceptional_labels)}
    fixed_labels_ref: tuple[int, ...] | None = None
    classes: dict[tuple, list[int]] = defaultdict(list)
    class_raw: dict[tuple, int] = {}
    class_mass: dict[tuple, int] = {}
    mass_blocks = Counter()
    mass_classes = Counter()
    total_raw = 0
    stream = hashlib.sha256()

    full_q = int(g.full_check["modulus"])
    x4_q = int(g.x4_check["modulus"])
    req(full_q >= 1 and x4_q >= 1, "invalid HNF quotient modulus")
    full_rows = [[int(v) for v in row] for row in g.full_check["coefficients"]]
    x4_rows = [[int(v) for v in row] for row in g.x4_check["coefficients"]]
    req(all(len(row) == len(g.exceptional_labels) for row in full_rows), "full-check coefficient width drift")
    req(all(len(row) == len(g.exceptional_labels) + 1 for row in x4_rows), "x4-check coefficient width drift")

    for block in survivors:
        sig = a.block_signature(block, idx)
        fixed = {int(k): int(v) for k, v in sig["fixed_exceptional_pairings"].items()}
        fixed_labels = tuple(sorted(fixed))
        if fixed_labels_ref is None:
            fixed_labels_ref = fixed_labels
        req(fixed_labels == fixed_labels_ref, "fixed-label support changed across e8 blocks")
        req(all(label in exc_pos for label in fixed), "fixed label outside selected exceptional coordinates")
        residual = int(sig["residual_exceptional_mass"])
        mass = int(sig["fixed_exceptional_mass"])
        req(residual == 8 - mass, "residual mass drift")
        full_syn = syndrome(full_rows, full_q, exc_pos, fixed)
        x4_syn = syndrome([row[:len(g.exceptional_labels)] for row in x4_rows], x4_q, exc_pos, fixed)
        key = (residual, full_syn, x4_syn)
        raw = int(sig["raw_selected_parent_candidate_count"])
        classes[key].append(int(block))
        class_raw.setdefault(key, raw)
        class_mass.setdefault(key, mass)
        req(class_raw[key] == raw and class_mass[key] == mass, "class-internal residual/raw mismatch")
        total_raw += raw
        mass_blocks[mass] += 1
        stream.update((str(block) + ":" + csha({"r": residual, "f": full_syn, "x": x4_syn}) + "\n").encode())

    req(total_raw == EXPECTED_RAW_PARENTS, "raw parent accounting drift")
    for key in classes:
        mass_classes[class_mass[key]] += 1

    representative_raw = sum(class_raw.values())
    class_count = len(classes)
    max_class_size = max(len(v) for v in classes.values())
    singleton_classes = sum(1 for v in classes.values() if len(v) == 1)
    mass_ge7_blocks = sum(n for m, n in mass_blocks.items() if m >= 7)
    mass_ge7_classes = sum(n for m, n in mass_classes.items() if m >= 7)
    mass_ge7_raw = sum(int(a.block_signature(block, idx)["raw_selected_parent_candidate_count"]) for block in survivors if int(a.block_signature(block, idx)["fixed_exceptional_mass"]) >= 7)
    mass_ge7_rep_raw = sum(class_raw[k] for k in classes if class_mass[k] >= 7)

    # Exact equivalence statement: free exceptional labels and their coefficient
    # matrices are global constants. For equal residual cap and equal fixed
    # syndromes, every free composition has the same full-HNF truth value and
    # the same x4 residue truth values. This is an HNF-layer equivalence only;
    # it does not identify the absolute all140 pairing vector and cannot by
    # itself transfer a downstream QF-LIA UNSAT certificate.
    strict_block_compression = class_count < EXPECTED_BLOCKS
    strict_raw_compression = representative_raw < EXPECTED_RAW_PARENTS
    status = "STRICT_HNF_SYNDROME_COMPRESSION" if strict_block_compression and strict_raw_compression else "NO_STRICT_HNF_SYNDROME_COMPRESSION"

    top_classes = []
    for key, blocks in sorted(classes.items(), key=lambda kv: (-len(kv[1]), kv[1][0]))[:20]:
        top_classes.append({
            "mass": class_mass[key],
            "residual": key[0],
            "block_count": len(blocks),
            "representative_block": blocks[0],
            "raw_parent_candidates_per_block": class_raw[key],
            "signature_sha256": csha({"r": key[0], "f": key[1], "x": key[2]}),
        })

    result = {
        "schema": "STAGE32_MAIN_CROSS_LANE_HNF_SYNDROME_COMPRESSION_PROBE_V1",
        "status": status,
        "scope": {
            "row_id": "g1-d008",
            "d": 8,
            "e": 8,
            "current_main_blocks": EXPECTED_BLOCKS,
            "current_main_terminals": EXPECTED_TERMINALS,
            "raw_selected_parent_candidates": EXPECTED_RAW_PARENTS,
        },
        "source_lock": {
            "ex5_hostile_audited_exact_head": AUDITED_EX5_HEAD,
            "ex5_hostile_audit_review_id": AUDITED_EX5_REVIEW,
            "adapter_path": str(ADAPTER_REL),
            "adapter_blob_sha1": ADAPTER_BLOB,
        },
        "equivalence": {
            "signature": "(residual_exceptional_mass, full_HNF_fixed_syndrome, x4_HNF_fixed_syndrome)",
            "full_modulus": full_q,
            "x4_modulus": x4_q,
            "full_active_rows": len(full_rows),
            "x4_active_rows": len(x4_rows),
            "fixed_labels": list(fixed_labels_ref or ()),
            "free_selected_exceptional_count": len(g.exceptional_labels) - len(fixed_labels_ref or ()),
            "exact_parent_hnf_pattern_equivalence": True,
            "downstream_qf_lia_certificate_transfer_proved": False,
        },
        "compression": {
            "block_count_before": EXPECTED_BLOCKS,
            "syndrome_class_count": class_count,
            "block_class_reduction": EXPECTED_BLOCKS - class_count,
            "max_class_size": max_class_size,
            "singleton_classes": singleton_classes,
            "raw_parent_checks_before": EXPECTED_RAW_PARENTS,
            "representative_raw_parent_checks": representative_raw,
            "raw_parent_check_reduction": EXPECTED_RAW_PARENTS - representative_raw,
            "raw_parent_compression_ratio": EXPECTED_RAW_PARENTS / representative_raw if representative_raw else None,
            "strict_block_compression": strict_block_compression,
            "strict_raw_compression": strict_raw_compression,
        },
        "mass_profile": {
            "blocks": {str(k): mass_blocks[k] for k in sorted(mass_blocks)},
            "classes": {str(k): mass_classes[k] for k in sorted(mass_classes)},
            "mass_ge_7_blocks": mass_ge7_blocks,
            "mass_ge_7_classes": mass_ge7_classes,
            "mass_ge_7_raw_parent_checks_before": mass_ge7_raw,
            "mass_ge_7_representative_raw_parent_checks": mass_ge7_rep_raw,
        },
        "top_classes": top_classes,
        "signature_stream_sha256": stream.hexdigest(),
        "cycle": {
            "route_status": "PASS_NEW_GATE_FROM_STRONGER_VIEW" if strict_block_compression else "BLOCKED_NO_NEW_INFORMATION",
            "active_receiver": "current-MAIN e8 selected64 HNF parent extension",
            "new_view": "fixed-prefix quotient-syndrome equivalence classes",
            "new_view_source": "BLIND",
            "exhaustive_view_audit": True,
            "blind_rediscovery": True,
            "split_triggered": False,
        },
        "firewalls": {
            "main_pruning_credit": False,
            "full178_complete": False,
            "cert_lift_mass7_symbolic_lemma_claimed": False,
            "ex5_parent_unsat_transfer_claimed": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "stage32_closed": False,
            "merge_authorized": False,
        },
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    text = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if args.json_output:
        args.json_output.write_text(text, encoding="utf-8")
    print(json.dumps({
        "status": status,
        "blocks": EXPECTED_BLOCKS,
        "classes": class_count,
        "raw_before": EXPECTED_RAW_PARENTS,
        "raw_representatives": representative_raw,
        "compression_ratio": result["compression"]["raw_parent_compression_ratio"],
        "mass_ge_7_blocks": mass_ge7_blocks,
        "mass_ge_7_classes": mass_ge7_classes,
        "canonical": result["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
