#!/usr/bin/env python3
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
OLD_WORKER = HERE / "run_hpadj22_zero_center_support_qbc_local_b.py"
NEW_WORKER = HERE / "run_hpadj22_support_qbc_local_row_b.py"
LEGACY_RECEIPT = HERE / "local-support-qbc/row022-b047.json"
RECEIPT_VALIDATOR = HERE / "verify_local_support_qbc_receipt.py"
QBC_PARENT = HERE / "verify_hpadj22_zero_center_qbc_tinterval_g1d192_band4.py"

OLD_WORKER_BLOB = "2c1abfd6d921122d9cf6a67a2f2251b95318e5fd"
NEW_WORKER_BLOB = "37e72735125c232e534d92c6e24c7afc0a0f4f24"
LEGACY_RECEIPT_BLOB = "0f161fa0df18966a8bc38f0160edd76f4f9cc1fe"
LEGACY_RECEIPT_CANON = "2bbc6957864fcb439dc991a26a3ea223d6f3169af7352df8b28966a058a8b47b"
RECEIPT_VALIDATOR_BLOB = "42543e33664848039d086dfd60f041db5d56b299"
QBC_PARENT_BLOB = "3e21729cf39783e96aeff82a8cf734ef53a51f9e"

HELPERS = (
    "req",
    "blob",
    "load",
    "min_square_sum_positive",
    "support_q_lower",
    "pair_square_min",
    "parity_nearest_candidates",
    "bc_t_q_lower",
    "bc_t_q_lower_bruteforce",
    "aggregate_q_lower",
    "support_envelope",
    "support_t_interval",
    "qcut_support",
    "abstract_regression",
)

CORE_START = "    regression_cases = abstract_regression()"
CORE_END = '    req(refined <= parent_refined <= current, "aggregate refinement order drift")'
NEW_DIAGNOSTIC_LINES = {
    '                all_bc_records.append({"b": b, "c": c, "current": "0", "parent_refined": "0", "refined": "0", "zero_reason": "no_active_histogram"})',
    '                all_bc_records.append({"b": b, "c": c, "current": "0", "parent_refined": "0", "refined": "0", "zero_reason": "negative_component3"})',
    '                all_bc_records.append({"b": b, "c": c, "current": "0", "parent_refined": "0", "refined": "0", "zero_reason": "empty_x4_interval"})',
}
OLD_FULL_BAND_ASSERT = [
    "    if full_band:",
    "        req(",
    "            current == fp.EXPECTED_CURRENT,",
    '            f"same-population row-band identity drift {current}!={fp.EXPECTED_CURRENT}",',
    "        )",
]


def req(v: bool, m: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + m)


def blob(p: Path) -> str:
    raw = p.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(o: dict) -> str:
    x = dict(o)
    x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def function_map(text: str):
    tree = ast.parse(text)
    return {
        n.name: n
        for n in tree.body
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def ast_fingerprint(node: ast.AST) -> str:
    return ast.dump(node, annotate_fields=True, include_attributes=False)


def core_lines(text: str) -> list[str]:
    i = text.find(CORE_START)
    req(i >= 0, "missing numerical core start")
    j = text.find(CORE_END, i)
    req(j >= 0, "missing numerical core end")
    return text[i : j + len(CORE_END)].splitlines()


def normalized_core(lines: list[str], *, old: bool) -> list[str]:
    x = list(lines)
    if old:
        hits = []
        for i in range(len(x) - len(OLD_FULL_BAND_ASSERT) + 1):
            if x[i : i + len(OLD_FULL_BAND_ASSERT)] == OLD_FULL_BAND_ASSERT:
                hits.append(i)
        req(hits == [len(x) - len(OLD_FULL_BAND_ASSERT) - 1], "old full-band assertion position drift")
        i = hits[0]
        del x[i : i + len(OLD_FULL_BAND_ASSERT)]
    else:
        got = [line for line in x if line in NEW_DIAGNOSTIC_LINES]
        req(set(got) == NEW_DIAGNOSTIC_LINES and len(got) == 3, "new zero-cell diagnostics drift")
        x = [line for line in x if line not in NEW_DIAGNOSTIC_LINES]
    return x


def main() -> None:
    req(blob(OLD_WORKER) == OLD_WORKER_BLOB, "old worker blob drift")
    req(blob(NEW_WORKER) == NEW_WORKER_BLOB, "new worker blob drift")
    req(blob(LEGACY_RECEIPT) == LEGACY_RECEIPT_BLOB, "legacy receipt blob drift")
    req(blob(RECEIPT_VALIDATOR) == RECEIPT_VALIDATOR_BLOB, "receipt validator blob drift")
    req(blob(QBC_PARENT) == QBC_PARENT_BLOB, "qBC parent blob drift")

    old_text = OLD_WORKER.read_text()
    new_text = NEW_WORKER.read_text()
    old_funcs = function_map(old_text)
    new_funcs = function_map(new_text)

    for name in HELPERS:
        req(name in old_funcs and name in new_funcs, "missing helper " + name)
        req(
            ast_fingerprint(old_funcs[name]) == ast_fingerprint(new_funcs[name]),
            "mathematical helper drift " + name,
        )

    old_core = core_lines(old_text)
    new_core = core_lines(new_text)
    req(len(old_core) == 203, f"old numerical core line count drift {len(old_core)}")
    req(len(new_core) == 201, f"new numerical core line count drift {len(new_core)}")
    req(
        normalized_core(old_core, old=True) == normalized_core(new_core, old=False),
        "row22 numerical accumulation core is not source-identical after allowed nonnumeric edits",
    )

    receipt = json.loads(LEGACY_RECEIPT.read_text())
    req(canon(receipt) == LEGACY_RECEIPT_CANON == receipt["canonical_sha256_without_this_field"], "legacy receipt canonical drift")
    req(receipt["schema"] == "STAGE32_178_LOCAL_SUPPORT_QBC_SINGLE_B_V1", "legacy receipt schema drift")
    t = receipt["target"]
    req(
        (int(t["row_index"]), t["row_id"], int(t["g"]), int(t["d"]), list(t["b_interval"]))
        == (22, "g1-d192", 1, 192, [47, 47]),
        "legacy target drift",
    )
    req(t["full_band_execution"] is False, "legacy b47 unexpectedly full-band")
    req(list(t["containing_band_interval"]) == [36, 47], "legacy containing band drift")

    parent = QBC_PARENT.read_text()
    req("ROW_INDEX = 22" in parent, "qBC parent row index drift")
    req('ROW_ID = "g1-d192"' in parent, "qBC parent row id drift")
    req("row_id, g0, d0 = rows[q.ROW_INDEX]" in old_text, "old fixed-row selector drift")
    req("row_id, g0, d0 = rows[args.row_index]" in new_text, "new generalized-row selector drift")
    req('req((row_id, g, d) == (q.ROW_ID, 1, 192), "target row drift")' in old_text, "old row guard drift")
    req('req(row_id == f"g{g}-d{d:03d}", "row identity drift")' in new_text, "new row guard drift")
    req('req(tq == 4992, "target q threshold drift")' in old_text, "old q-threshold guard drift")
    req((192 * 192 + 16 * 192) // 8 == 4992, "row22 q-threshold arithmetic drift")

    sl = receipt["source_locks"]
    req(sl["local_worker_blob_sha1"] == OLD_WORKER_BLOB, "legacy worker source lock drift")
    req(sl["hpadj22_source_head"] == "4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2", "legacy HPADJ22 source drift")
    req(receipt["semantics"]["same_population_as_current_hpadj22"] is True, "legacy population semantics drift")
    req(receipt["semantics"]["same_current_x4_capacity_rule"] is True, "legacy x4 semantics drift")
    req(receipt["semantics"]["main_consumption_performed"] is False, "legacy receipt already consumed")

    r = receipt["result"]
    req(int(r["support_qbc_refined_survivors"]) == 176436593457463322, "legacy b47 refined count drift")
    req(int(r["current_row_band_survivors"]) == 187902185746998436, "legacy b47 current count drift")
    req(int(r["support_qbc_exact_reduction"]) == 11465592289535114, "legacy b47 reduction drift")

    for k in ("main_credit_changed", "theorem_credit_changed", "endpoint_credit_changed", "merge", "full178_complete"):
        req(receipt["firewalls"][k] is False, "legacy credit firewall drift " + k)

    print("V48_LEGACY_B47_WORKER_EQUIVALENCE=PREFLIGHT_PASS")
    print("TARGET=row022/b47")
    print("NUMERICAL_KERNEL_EQUIVALENT=true")
    print("LEGACY_REFINED=176436593457463322")
    print("MAIN_CREDIT_CHANGED=false")
    print("HOSTILE_AUDIT_REQUIRED=true")


if __name__ == "__main__":
    main()
