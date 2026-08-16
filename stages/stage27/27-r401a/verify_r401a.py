#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]

def text(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

result = text("stages/stage27/27-r401a/result.md")
terminal = text("stages/stage27/27-r401a/terminal-gate-audit.md")
registry = json.loads(text("stages/stage27/27-r401a/critical-wall-registry.json"))
controller = json.loads(text("stages/stage27/27-controller.json"))
stage14 = text("stages/stage14/final.md")
audit40 = text("stages/stage27/27-40/audit.md")
audit_r401a = text("stages/stage27/27-r401a/audit.md")

assert "AUDIT_VERDICT=PASS" in audit40
assert "CHECKPOINT40_STATUS=UPPER_ATTACK_AUDITED_PASS_AWAITING_MERGE" in audit40
for marker in [
    "E_k\\le3\\theta-\\frac14",
    "E_{\\rm RRF}\\le \\chi+(2\\phi-\\chi)+(1/4-\\chi)=1-2\\theta",
    "proportional branch: `E<=7/16<1/2`",
    "cells with `chi>1/4` are empty",
]:
    assert marker in stage14, marker

for gamma in [Fraction(1, 100), Fraction(1, 32), Fraction(1, 20)]:
    assert 3 * (Fraction(1, 4) - gamma) - Fraction(1, 4) == Fraction(1, 2) - 3 * gamma
    assert 1 - 2 * (Fraction(1, 4) + gamma) == Fraction(1, 2) - 2 * gamma

assert registry["off_wall"]["fixed_power_saving_proved"] is True
assert registry["critical_wall"]["theta"] == "1/4"
assert registry["critical_wall"]["phi_interval"] == "[1/8,1/4]"
assert registry["critical_wall"]["existing_host_minimum_gives_deficit"] is False
assert registry["critical_wall"]["new_discovery"] is False
assert registry["terminal_gates"]["post_stage14_internal_crossing_found"] is False
assert registry["checkpoint_advanced_to_50"] is False

for marker in [
    "TASK_ID=Stage27-r401a",
    "CHECKPOINT_ADVANCED_TO_50=false",
    "OFF_WALL_FIXED_POWER_SAVING_PROVED=true",
    "ALL_FOUR_COEFFICIENT_FACTORS_BALANCED=true",
    "STRICT_SUB_SQRT_UPPER_PROVED=false",
    "CRITICAL_WALL_NEW_DISCOVERY=false",
    "ALL_THREE_STAGE14_TERMINAL_CHAINS_AUDITED=true",
    "NEXT_EXPECTED_COMMAND=Stage27-audit",
]:
    assert marker in result, marker

for marker in [
    "MAIN_INTERNAL_CHAIN_EXHAUSTED=true",
    "T_INTERNAL_CHAIN_EXHAUSTED=true",
    "S_INTERNAL_CHAIN_EXHAUSTED=true",
    "Stage14-X13",
    "14-4ghH",
    "14-tH33",
    "14-s7-164",
    "arXiv:2606.17487",
    "arXiv:2602.01820",
    "NEW_EXACT_TERMINAL_GATE_ADAPTER_FOUND=false",
]:
    assert marker in terminal, marker

# r401a mathematics remains frozen after hostile audit PASS + merge; later
# checkpoint40 child routes may continue without preserving every historical
# controller convenience key from the original r401a submission.
assert "AUDIT_VERDICT=PASS" in audit_r401a
r = controller["derived_routes"]["Stage27-r401a"]
assert r["audit_status"] == "PASS"
assert r["pr"] == 1026
assert r["merge_commit"] == "05f460c6df069f9b6da58409bc19378920a5666f"
assert r["advance_to_checkpoint50"] is False
assert controller["state"]["CURRENT_CHECKPOINT"] == 40
assert controller["checkpoint_status"]["50"] == "BLOCKED_BY_ACTIVE_CHECKPOINT40_DERIVED_ROUTE"
assert controller["next_expected_command"] == "Stage27-audit"

print("STAGE27_R401A_UPSTREAM_AUDIT_MERGE=PASS")
print("STAGE27_R401A_OFF_WALL_FIXED_POWER=PASS")
print("STAGE27_R401A_CRITICAL_WALL_LOCALIZATION=PASS")
print("STAGE27_R401A_NO_THEOREM_INFLATION=PASS")
print("STAGE27_R401A_POSTMERGE_LIFECYCLE=PASS")
