#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "docs/research-arsenal-index.json"


def require(condition, message):
    if not condition:
        raise SystemExit(message)


data = json.loads(REGISTRY.read_text(encoding="utf-8"))
require(data["registry"] == "RESEARCH-ARSENAL-R01", "registry id mismatch")
require(data["status"] == "CURRENT", "registry is not CURRENT")
require("Stage26" in data.get("scope", ""), "registry scope has not advanced through Stage26")

weapons = data["weapons"]
ids = [weapon["id"] for weapon in weapons]
require(len(ids) == len(set(ids)), "duplicate weapon id")
require(set(data["statuses"]) == {"ACTIVE", "PARKED", "SUPERSEDED", "INTEGRATED"}, "status vocabulary drift")

for weapon in weapons:
    require(weapon["status"] in data["statuses"], f"invalid status: {weapon['id']}")
    source = ROOT / weapon["source"]
    require(source.is_file(), f"missing source: {weapon['id']}: {weapon['source']}")
    source_text = source.read_text(encoding="utf-8")
    require(weapon["id"] in source_text or weapon["id"].startswith("S24-W-"), f"source does not identify weapon: {weapon['id']}")

by_id = {weapon["id"]: weapon for weapon in weapons}
required_active = {
    "AR-006", "S20-W03", "S21-W01", "S21-W02",
    "S22-W01", "S23-W01", "S23-W02", "S25-W01", "S25-W02", "S25-W05", "S25-W06",
    "S26-W01", "S26-W02", "S26-W03",
}
require(required_active <= set(by_id), "required active weapon missing")
for weapon_id in required_active:
    require(by_id[weapon_id]["status"] == "ACTIVE", f"required weapon not ACTIVE: {weapon_id}")

require(by_id["S20-W01"]["status"] == "SUPERSEDED", "S20-W01 must be superseded by the Stage26 upper interface")
require(by_id["S20-W02"]["status"] == "SUPERSEDED", "S20-W02 must be superseded by the Stage26 lower")
require(by_id["S25-W03"].get("integrated_into") == "S25-W01", "S25-W03 integration drift")
require(by_id["S25-W04"]["status"] == "PARKED", "S25-W04 must remain route-specific PARKED")
require(by_id["S24-W-C17"]["status"] == "PARKED", "C17 must remain a parked historical lower")
for weapon_id in ("S26-W01", "S26-W02", "S26-W03"):
    require(by_id[weapon_id]["source"] == "docs/stage26-arsenal-promotion.md", f"Stage26 source drift: {weapon_id}")

supersessions = {(item["old"], item["new"]) for item in data["supersessions"]}
require(("TB-LEDGER-current-whole-family-after-s7-13", "AR-006") in supersessions, "7/8 supersession missing")
require(("S24-W-C17 as current global lower", "S25-W01") in supersessions, "C17 supersession missing")
require(("S20-W02 primitive Saunderson lower B^(1/6)", "S26-W01 generalized two-parameter lower B^(1/3-epsilon)") in supersessions, "Stage20 lower supersession missing")
require(("S20-W01 Euler upper package", "S26-W03 same upper with audited K3/local-sieve/thin-cover interface") in supersessions, "Stage20 upper supersession missing")

toolbox = json.loads((ROOT / "docs/stage14-toolbox/index.json").read_text(encoding="utf-8"))
cards = {card["id"]: card for card in toolbox["cards"]}
old = cards["TB-LEDGER-current-whole-family-after-s7-13"]
require(old["status"] == "SUPERSEDED", "historical 7/8 ledger is still CURRENT")
require(old["superseded_by"] == "AR-006", "historical 7/8 replacement drift")

stage23 = (ROOT / "docs/stage23-arsenal-promotion.md").read_text(encoding="utf-8")
require("TARGET_UNBOUNDEDNESS_PROVED=true" in stage23, "Stage23 stale unboundedness firewall")
require("CURRENT_DIRECTIONAL_LOWER=N2,j(B)>>_j B^(1/4) for j=a,b,c" in stage23, "Stage23 directional backflow missing")

stage24 = (ROOT / "docs/stage24-arsenal-promotion.md").read_text(encoding="utf-8")
require("CURRENT_POSITIVE_POWER_LOWER_BOUND=N2(B)>>B^(1/4)" in stage24, "Stage24 current lower missing")
require("C17_STATUS=PARKED_PARITY_EXAMPLE_SUPERSEDED_AS_GLOBAL_LOWER" in stage24, "Stage24 C17 status drift")

stage25 = (ROOT / "docs/stage25-arsenal-promotion.md").read_text(encoding="utf-8")
require("DIRECTIONAL_COROLLARY=N2,j(B)>>_j B^(1/4) for j=a,b,c" in stage25, "S25-W01 directional theorem missing")
require("STATUS=INTEGRATED_INTO_S25-W01_SUPPORT_CERTIFICATE" in stage25, "S25-W03 integration missing")
require("STATUS=PARKED_ROUTE_SPECIFIC" in stage25, "S25-W04 parked status missing")

stage26 = (ROOT / "docs/stage26-arsenal-promotion.md").read_text(encoding="utf-8")
require("S26-W01" in stage26 and "S26-W02" in stage26 and "S26-W03" in stage26, "Stage26 weapon package incomplete")
require("TRUE_M3_EXPONENT_IDENTIFIED=false" in stage26, "Stage26 true-exponent firewall missing")
require("M3_ASYMPTOTIC_PROVED=false" in stage26, "Stage26 asymptotic firewall missing")
require("UPPER_LOWER_MATCH=false" in stage26, "Stage26 upper/lower firewall missing")
require("PERFECT_CUBOID_CONCLUSION=NONE" in stage26, "Stage26 perfect-cuboid firewall missing")

print("RESEARCH_ARSENAL_INDEX=PASS")
print("ACTIVE_WEAPONS=" + str(sum(weapon["status"] == "ACTIVE" for weapon in weapons)))
print("PARKED_WEAPONS=" + str(sum(weapon["status"] == "PARKED" for weapon in weapons)))
print("SUPERSEDED_WEAPONS=" + str(sum(weapon["status"] == "SUPERSEDED" for weapon in weapons)))
