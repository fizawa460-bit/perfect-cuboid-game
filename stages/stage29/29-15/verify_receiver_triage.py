import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
LEDGER = HERE / "open-receiver-triage.json"
VALID = {"1", "2", "3", "4"}


def main():
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    receivers = data["receivers"]

    ids = [r["id"] for r in receivers]
    assert len(ids) == len(set(ids)), "duplicate receiver/frontier id"
    assert len(receivers) == data["classification_count"], "classification_count mismatch"

    counts = {k: 0 for k in VALID}
    class1_executed = 0

    for r in receivers:
        c = str(r["class"])
        assert c in VALID, f"invalid class for {r['id']}: {c}"
        counts[c] += 1

        status = r.get("final_status", "")
        assert status, f"missing final_status: {r['id']}"

        if c == "1":
            assert status.startswith("DISCHARGED") or status.startswith("EXECUTED_NEGATIVE_LIMIT"), (
                f"class-1 receiver not executed: {r['id']} -> {status}"
            )
            assert r.get("execution_record"), f"class-1 missing execution_record: {r['id']}"
            assert r.get("result"), f"class-1 missing result: {r['id']}"
            class1_executed += 1
        elif c == "2":
            assert status == "CURRENT_TOOL_LIMIT_EXECUTED", f"class-2 status mismatch: {r['id']}"
            assert r.get("exact_limit"), f"class-2 missing exact_limit: {r['id']}"
            assert r.get("reason"), f"class-2 missing reason: {r['id']}"
        elif c == "3":
            assert status == "NEW_THEOREM_REQUIRED", f"class-3 status mismatch: {r['id']}"
            assert r.get("needed"), f"class-3 missing needed theorem: {r['id']}"
            assert r.get("reason"), f"class-3 missing reason: {r['id']}"
        elif c == "4":
            assert status == "DORMANT_NONDECISIVE", f"class-4 status mismatch: {r['id']}"
            assert r.get("reactivate_if"), f"class-4 missing reactivation trigger: {r['id']}"
            assert r.get("reason"), f"class-4 missing nondecisiveness reason: {r['id']}"

    declared = {str(k): v for k, v in data["class_counts"].items()}
    assert counts == declared, f"class_counts mismatch: actual={counts}, declared={declared}"

    summary = data["class1_execution_summary"]
    assert summary["identified"] == counts["1"]
    assert summary["executed"] == class1_executed
    assert summary["pending"] == 0
    assert summary["discharged"] == class1_executed

    post = data["post_triage"]
    assert post["pending_class1_count"] == 0
    assert post["vague_amber_without_execution_class_count"] == 0
    assert post["carry_to_29_16_is_only_classes_2_3_4"] is True
    assert post["perfect_cuboid_existence_claim"] is False
    assert post["perfect_cuboid_nonexistence_claim"] is False

    print(f"receiver/frontier count = {len(receivers)}")
    print(f"class counts = {counts}")
    print(f"class-1 executed = {class1_executed}; pending = 0")
    print("vague AMBER without execution class = 0")
    print("29-16 carry-forward gate = classes 2/3/4 only")


if __name__ == "__main__":
    main()
