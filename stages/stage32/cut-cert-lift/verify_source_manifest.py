#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "SOURCE-LOCKS.json"
EXPECTED_IDS = ["CUT193", "CUT194", "CUT195", "CUT196", "CUT197", "CUT198"]
EXPECTED_BLOCKS_PER_WAVE = 255
EXPECTED_TERMINALS_PER_BLOCK = 113
EXPECTED_TERMINALS_PER_WAVE = EXPECTED_BLOCKS_PER_WAVE * EXPECTED_TERMINALS_PER_BLOCK
EXPECTED_EX5_PRODUCER_HEAD = "fd00531181228c9f367a49eb61ddc3af6ab84ab3"
EXPECTED_EX5_ADAPTER = "stages/stage32-ex5/cut-handoff/e8_terminal_population_adapter.py"


def req(cond, msg):
    if not cond:
        raise RuntimeError(msg)


def main():
    obj = json.loads(MANIFEST.read_text())
    req(obj.get("schema") == "STAGE32_CUT_CERT_LIFT_SOURCE_LOCKS_V1", "schema drift")
    shared = obj.get("shared_inputs", {})
    req(shared.get("ex5_e8_terminal_producer_exact_head") == EXPECTED_EX5_PRODUCER_HEAD,
        "EX5 producer exact-head lock drift")
    req(shared.get("adapter_path") == EXPECTED_EX5_ADAPTER, "EX5 adapter path drift")
    req(shared.get("source_mode") == "separate_exact_head_checkout_read_only",
        "EX5 source mode drift")

    waves = obj.get("waves")
    req(isinstance(waves, list) and len(waves) == 6, "wave count drift")
    req([w.get("id") for w in waves] == EXPECTED_IDS, "wave order drift")

    next_offset = 1
    total_blocks = 0
    total_terminals = 0
    total_pruned = 0
    rates = {}
    for w in waves:
        wid = w["id"]
        req(w.get("offset_start") == next_offset, f"offset gap/overlap at {wid}")
        req(w.get("offset_end") - w.get("offset_start") + 1 == EXPECTED_BLOCKS_PER_WAVE,
            f"offset width drift at {wid}")
        req(w.get("blocks") == EXPECTED_BLOCKS_PER_WAVE, f"block count drift at {wid}")
        req(w.get("terminals") == EXPECTED_TERMINALS_PER_WAVE, f"terminal count drift at {wid}")
        req(isinstance(w.get("exact_head"), str) and len(w["exact_head"]) == 40,
            f"exact head malformed at {wid}")
        req(str(w.get("audit_status", "")).startswith("PASS_"), f"audit status not pass-locked at {wid}")
        pruned = w.get("candidate_pruned_terminals")
        req(isinstance(pruned, int) and 0 <= pruned <= EXPECTED_TERMINALS_PER_WAVE,
            f"pruned count invalid at {wid}")
        total_blocks += w["blocks"]
        total_terminals += w["terminals"]
        total_pruned += pruned
        rates[wid] = pruned / EXPECTED_TERMINALS_PER_WAVE
        next_offset = w["offset_end"] + 1

    agg = obj.get("aggregate", {})
    req(agg.get("blocks") == total_blocks, "aggregate block drift")
    req(agg.get("terminals") == total_terminals, "aggregate terminal drift")
    req(agg.get("candidate_pruned_terminals") == total_pruned, "aggregate pruned drift")
    req(agg.get("candidate_pruning_fraction") == f"{total_pruned}/{total_terminals}",
        "aggregate fraction drift")

    fw = obj.get("firewalls", {})
    for key in [
        "read_only_source_evidence",
        "no_main_credit",
        "no_relabel_unknown_as_unsat",
        "no_cross_e_extrapolation_without_exact_adapter",
        "no_merge_authorization",
    ]:
        req(fw.get(key) is True, f"firewall disabled: {key}")

    print(json.dumps({
        "verdict": "PASS_CERT_LIFT_SOURCE_MANIFEST_CONSISTENCY",
        "waves": EXPECTED_IDS,
        "blocks": total_blocks,
        "terminals": total_terminals,
        "candidate_pruned_terminals": total_pruned,
        "candidate_pruning_fraction": total_pruned / total_terminals,
        "per_wave_pruning_fraction": rates,
        "next_offset_after_locked_waves": next_offset,
        "ex5_producer_exact_head": EXPECTED_EX5_PRODUCER_HEAD,
        "heavy_compute": False,
        "main_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
