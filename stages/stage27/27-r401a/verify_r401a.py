#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]

def text(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

result = text("stages/stage27/27-r401a/result.md")
registry = json.loads(text("stages/stage27/27-r401a/critical-wall-registry.json"))
controller = json.loads(text("stages/stage27/27-controller.json"))
stage14 = text("stages/stage14/final.md")
audit40 = text("stages/stage27/27-40/audit.md")

assert "AUDIT_VERDICT=PASS" in audit40
assert "CHECKPOINT40_STATUS=UPPER_ATTACK_AUDITED_PASS_AWAITING_MERGE" in audit40
for marker in [
    "E_k\\le3\\theta-\\frac14",
    "E_{\\rm RRF}\\le \\chi+(2\\phi-\\chi)+(1/4-\\chi)=1-2\\theta",
    "proportional branch: `E<=7/16<1/2`",
    "cells with `chi>1/4` are empty",
]:
    assert marker in stage14, marker

# Exact affine optimization on both sides of the critical wall.
for gamma in [Fraction(1, 100), Fraction(1, 32), Fraction(1, 20)]:
    assert 3 * (Fraction(1, 4) - gamma) - Fraction(1, 4) == Fraction(1, 2) - 3 * gamma
    assert 1 - 2 * (Fraction(1, 4) + gamma) == Fraction(1, 2) - 2 * gamma

assert registry["off_wall"]["fixed_power_saving_proved"] is True
assert registry["critical_wall"]["theta"] == "1/4"
assert registry["critical_wall"]["phi_interval"] == "[1/8,1/4]"
assert registry["critical_wall"]["existing_host_minimum_gives_deficit"] is False
assert registry["checkpoint_advanced_to_50"] is False

for marker in [
    "TASK_ID=Stage27-r401a",
    "CHECKPOINT_ADVANCED_TO_50=false",
    "OFF_WALL_FIXED_POWER_SAVING_PROVED=true",
    "ALL_FOUR_COEFFICIENT_FACTORS_BALANCED=true",
    "STRICT_SUB_SQRT_UPPER_PROVED=false",
    "NEXT_EXPECTED_COMMAND=Stage27-audit",
]:
    assert marker in result, marker

assert controller["state"]["CURRENT_CHECKPOINT"] == 40
assert controller["checkpoint_status"]["50"] == "BLOCKED_BY_ACTIVE_CHECKPOINT40_DERIVED_ROUTE"
assert controller["derived_routes"]["Stage27-r401a"]["audit_status"] == "PENDING"
assert controller["next_expected_command"] == "Stage27-audit"

print("STAGE27_R401A_UPSTREAM_AUDIT_MERGE=PASS")
print("STAGE27_R401A_OFF_WALL_FIXED_POWER=PASS")
print("STAGE27_R401A_CRITICAL_WALL_LOCALIZATION=PASS")
print("STAGE27_R401A_NO_THEOREM_INFLATION=PASS")
