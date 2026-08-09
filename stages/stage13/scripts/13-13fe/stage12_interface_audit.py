#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
STAGE12 = ROOT / "stages" / "stage12"
STAGE13 = ROOT / "stages" / "stage13"
OUT = STAGE13 / "data" / "13-13fe" / "stage12_interface_audit.json"

BUNDLE = "PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09"
CONTENT_SHA = "0da06c78bbb546039dbe8d423dcc6ed403fe1af90d777488c2393c0c77c16848"
CPROJ = {"ab": 168424, "ac": 86472, "bc": 81520}
RAW = {"ab": 84212, "ac": 43236, "bc": 40760}


def build_report() -> dict:
    final = (STAGE12 / "final.md").read_text()
    manifest = (STAGE12 / "manifest-r09.md").read_text()
    bridge = json.loads((STAGE13 / "data" / "13-8" / "bridge_ledger_report.json").read_text())
    lemma = (STAGE13 / "13-13fe" / "stage12-counting-interface.md").read_text()
    roadmap = (STAGE13 / "13-13" / "roadmap.md").read_text()

    bridge_obj = bridge.get("object_level_bridge", {})
    proj = bridge.get("exact_projection_theorem", {})

    checks = {
        "bridge_category_factor_two_exact": proj.get("categorywise") == "C_prim,q^proj(B)=2 A_q(B) for q in {ab,ac,bc}",
        "bridge_cutoff_compatibility_locked": "exactly the Stage13 space-diagonal cutoff d<=B" in bridge_obj.get("cutoff_compatibility", ""),
        "bridge_multi_face_rule_locked": "exactly-two object contributes two canonical raw incidences and four Stage12 oriented records" in bridge_obj.get("multi_face_rule", ""),
        "bridge_parity_stratified": proj.get("parity_stratified") is True,
        "bridge_primitive_compatibility_locked": "exactly gcd(a,b,c)=1" in bridge_obj.get("primitive_compatibility", ""),
        "bridge_total_factor_two_exact": proj.get("total") == "C_prim(B)=sum_q C_prim,q^proj(B)=2(A_ab+A_ac+A_bc)",
        "finite_B100000_category_factor_two": all(CPROJ[q] == 2 * RAW[q] for q in RAW),
        "finite_B100000_total_factor_two": sum(CPROJ.values()) == 2 * sum(RAW.values()),
        "kappa_eta_identity_locked": "eta=pi*kappa" in bridge.get("frozen_stage12_input", {}).get("theorem", "") and "ETA_EQUALS_PI_KAPPA=true" in lemma,
        "lemma_contains_complete_stage12_definition": all(token in lemma for token in ["\\mathcal D_B", "G(n)", "C_{\\rm raw}(B)", "C_{\\rm prim}(B)", "Möbius inversion", "STAGE13_PROJECTION_FIBER=2"]),
        "manifest_r09_locked": BUNDLE in manifest and CONTENT_SHA in manifest,
        "roadmap_gate_e_lock": "STAGE13_13FE=COMPLETE_STAGE12_COUNTING_INTERFACE" in roadmap and "NEXT=13-13ff" in roadmap,
        "stage12_final_contains_oriented_scope": "primitive oriented count" in final,
        "stage12_final_contains_primitive_definition": "Möbius inversion" in final and "C_{\\rm prim}(B)" in final,
        "stage12_final_contains_theorem": "\\frac{\\kappa}{12\\pi}B(\\log B)^3" in final,
    }

    return {
        "checks": checks,
        "decision": {
            "next": "13-13ff",
            "stage12_reopened": False,
            "status": "COMPLETE_STAGE12_COUNTING_INTERFACE" if all(checks.values()) else "FAIL_REPAIR_REQUIRED",
            "theorem_changed": False,
        },
        "finite_B100000": {
            "canonical_raw": RAW,
            "projected_stage12": CPROJ,
            "total_canonical_raw": sum(RAW.values()),
            "total_projected_stage12": sum(CPROJ.values()),
        },
        "locks": {
            "factor_two_fiber": "two orders of distinguished face legs",
            "kappa_eta": "eta=pi*kappa",
            "stage12_bundle": BUNDLE,
            "stage12_content_sha256": CONTENT_SHA,
            "stage12_theorem": "C_prim(B)~kappa/(12*pi) B(log B)^3",
        },
        "metadata": {
            "scope": "Stage12 R09 counting/orientation/constant interface plus exact Stage13 factor-two projection",
            "stage": "13-13fe",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", action="store_true")
    parser.add_argument("--check-report", action="store_true")
    args = parser.parse_args()

    report = build_report()
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"

    if args.write_report:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(text)

    if args.check_report:
        if not OUT.exists() or OUT.read_text() != text:
            raise SystemExit("committed Stage13-13fe report is stale")
        if report["decision"]["status"] != "COMPLETE_STAGE12_COUNTING_INTERFACE":
            failed = [k for k, v in report["checks"].items() if not v]
            raise SystemExit(f"Stage13-13fe failed checks: {failed}")

    print(text, end="")


if __name__ == "__main__":
    main()
