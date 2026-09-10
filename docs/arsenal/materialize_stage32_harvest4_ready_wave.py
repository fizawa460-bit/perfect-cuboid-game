#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROMO = ROOT / "docs" / "stage32-arsenal-promotion.md"
INDEX = ROOT / "docs" / "arsenal" / "index.json"
REVAL = ROOT / "docs" / "arsenal" / "stage32-harvest4-registration-revalidation.json"

EXPECTED_CARDS = [
    "S32-PW01", "S32-PW03", "S32-PW04", "S32-PW05", "S32-PW06",
    "S32-PW07", "S32-PW08", "S32-PW09", "S32-PW10", "S32-PW11", "S32-PW12",
]
EXPECTED_WORKFLOWS = ["S32-WF01", "S32-WF02"]


def main():
    reval = json.loads(REVAL.read_text())
    assert reval["status"] == "READY_WAVE_REVALIDATED_REGISTRY_MATERIALIZATION_PENDING"
    assert reval["registration_shape_after_materialization"]["pw13_active"] is False

    promo = PROMO.read_text()
    extension = "### Harvest 4 extension — authority-preserving filtered random access"
    marker = "# Fourth Stage32 provisional harvest — Harvest 4 ready-wave registration"
    assert promo.count(extension) == 1
    assert promo.count(marker) == 1
    assert "S32_PW13_ACTIVE=false" in promo
    for i in range(7, 13):
        assert f"## S32-PW{i:02d} —" in promo
    assert "## S32-WF01 —" in promo and "## S32-WF02 —" in promo

    idx = json.loads(INDEX.read_text())
    s32 = next(x for x in idx["provisional_harvests"] if x.get("source_stage") == "Stage32")
    assert s32["active_cards"] == EXPECTED_CARDS
    assert s32["active_workflows"] == EXPECTED_WORKFLOWS
    assert s32["retired_merged_ids"]["S32-PW02"] == "S32-PW01"
    assert s32["provisional_active_entry_count"] == 13
    assert "S32-PW13" not in s32["active_cards"]
    assert s32["harvest4_registration"]["arsenal_registration_adds_stage32_mathematical_credit"] is False


if __name__ == "__main__":
    main()
