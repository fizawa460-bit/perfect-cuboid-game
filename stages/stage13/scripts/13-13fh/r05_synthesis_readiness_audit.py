#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
STAGE13 = ROOT / "stages" / "stage13"
OUT = STAGE13 / "data" / "13-13fh" / "r05_synthesis_readiness_audit.json"


def read(path: str) -> str:
    return (STAGE13 / path).read_text()


def has_all(text: str, tokens: list[str]) -> bool:
    return all(token in text for token in tokens)


def build_report() -> dict:
    proof = read("13-13fh/stage13-r05-canonical-proof.md")
    result = read("13-13fh/result.md")
    roadmap = read("13-13/roadmap.md")
    plan = read("13-13f/r05-repair-plan.md")

    gate_files = {
        "A": read("13-13fa/result.md"),
        "B": read("13-13fb/result.md"),
        "C": read("13-13fc/result.md"),
        "D": read("13-13fd/result.md"),
        "E": read("13-13fe/result.md"),
        "F": read("13-13ff/result.md"),
        "G": read("13-13fg/result.md"),
    }

    required_gate_locks = {
        "A": "STAGE13_13FA=COMPLETE_Q_INDEPENDENCE_AND_FINITE_DISCREPANCY_AUDIT",
        "B": "STAGE13_13FB=COMPLETE_EXPLICIT_WIENER_BOUND",
        "C": "STAGE13_13FC=COMPLETE_CURVED_REGION_ERROR_ACCUMULATION",
        "D": "STAGE13_13FD=COMPLETE_RETAINED_HARMONIC_CONDUCTOR_BOOKKEEPING",
        "E": "STAGE13_13FE=COMPLETE_STAGE12_COUNTING_INTERFACE",
        "F": "STAGE13_13FF=COMPLETE_EXACT_EXTERNAL_THEOREM_CONTRACTS",
        "G": "STAGE13_13FG=COMPLETE_FIXED_INERT_PRIME_TRANSFER",
    }

    forbidden_legacy_phrases = [
        "For angular phase `theta`",
        "number of boxes is `O((log B)^C)`",
        r"1\le\ell\le(\log X)^4",
        "finite harmonic cancellation order A = 48",
        "For the principal character tuple",
        "future R04 review bundle",
    ]

    checks = {
        "gates_a_through_g_complete": all(
            required_gate_locks[k] in gate_files[k] for k in required_gate_locks
        ),
        "r05_entrypoint_visible": has_all(proof, [
            "# Stage13 — R05 canonical proof candidate",
            "R05 canonical theorem lock",
        ]),
        "notation_separated": has_all(proof, [
            "Gaussian local angular phase",
            "denoted `vartheta`",
            "geometric polar angle",
        ]),
        "cellp_defined_at_first_use": has_all(proof, [
            r"C_{\ell,p}(s_h,s_r,s_s)",
            r"C_\vartheta(p^{-s_h},p^{-s_r},p^{-s_s})",
        ]),
        "stage12_interface_inlined": has_all(proof, [
            r"\mathcal D_B",
            "C_{\\rm raw}(B)",
            "Möbius inversion",
            "PRIMITIVE_ORIENTED_DISTINGUISHED_FACE_RECORDS",
            "STAGE13_PROJECTION_FIBER=2",
        ]),
        "wiener_constant_derived": has_all(proof, [
            "17744}{243",
            "3465625}{6561",
            "529p^{-5/4}",
            "P5_EXPLICIT_FINITE_BOUND_LT=432",
        ]),
        "curved_box_ledger_explicit": has_all(proof, [
            r"N_{\rm box}=O(\Lambda^{27})",
            "N=64",
            r"\mathcal E_{\rm finite}\ll B\Lambda^{-35}",
            r"\frac3{16}",
        ]),
        "harmonic_conductor_visible": has_all(proof, [
            r"X^{1-\delta_H}(1+\ell)^{C_H}(\log2X)^{D_H}",
            "4C_H+D_H+6",
            "FIXED_A48_REQUIRED=false",
        ]),
        "external_contracts_visible": has_all(proof, [
            "H1: nonzero Gaussian angular Hecke functions",
            "H2: fixed finite residue twists",
            "D1: `L(s,chi_4)`",
            "V1: Vaaler sawtooth approximation",
            "Riesz/Perron",
        ]),
        "finite_discrepancy_scope_visible": has_all(proof, [
            "B=100000",
            "B=5000000",
            "FINITE_DATA_CONTRADICTS_THEOREM=false",
            "PROVED_EFFECTIVE_CONVERGENCE_RATE=false",
        ]),
        "principal_pole_sector_visible": has_all(proof, [
            "principal pole sector",
            "AUXILIARY_CHARACTER_ALIASING_INCLUDED=true",
            "NONPRINCIPAL_POLE_SECTOR_LOSS_AT_LEAST_ONE=true",
        ]),
        "limit_order_visible": has_all(proof, [
            "fix S_k",
            "k -> infinity",
            "GROWING_MODULUS_THEOREM_USED=false",
        ]),
        "audit_scope_limited": has_all(proof, [
            "DETERMINISTIC_AUDIT_SCOPE=REPRODUCIBILITY_AND_CONSISTENCY_ONLY",
            "not substitutes for the mathematical arguments",
        ]),
        "theorem_lock_unchanged": has_all(proof, [
            "THEOREM_CHANGED=false",
            "THEOREM_CONTRACT_REOPEN_REQUIRED=false",
            "EXACT_ONE_TOTAL=N1(B)~kappa/(24*pi)B(log B)^3",
        ]),
        "legacy_r04_shortcuts_absent": not any(
            phrase in proof for phrase in forbidden_legacy_phrases
        ),
        "gate_h_result_ready": has_all(result, [
            "STAGE13_13FH=COMPLETE_R05_SYNTHESIS_READINESS",
            "R05_SYNTHESIS_READY=true",
            "R05_BUNDLE_CREATED=false",
            "R05_FRESH_EXTERNAL_REVIEW_REQUIRED=true",
            "NEXT=13-13fi",
        ]),
        "roadmap_advanced": has_all(roadmap, [
            "STAGE13_13FH=COMPLETE_R05_SYNTHESIS_READINESS",
            "13-13fi",
            "NEXT=13-13fi",
            "PROMOTE_TO_13_13G=false",
        ]),
        "repair_plan_closed": has_all(plan, [
            "Gate H — notation / audit scope / canonical synthesis / R05 readiness",
            "Status: `[x] COMPLETE — 13-13fh`",
            "R05_SYNTHESIS_READY=true",
            "NEXT=13-13fi",
        ]),
    }

    failed = [name for name, ok in checks.items() if not ok]
    return {
        "metadata": {
            "stage": "13-13fh",
            "scope": "R05 repaired canonical proof synthesis and bundle-build readiness",
        },
        "checks": checks,
        "decision": {
            "status": "COMPLETE_R05_SYNTHESIS_READINESS" if not failed else "FAIL_REPAIR_REQUIRED",
            "failed_checks": failed,
            "theorem_changed": False,
            "theorem_contract_reopen_required": False,
            "r05_synthesis_ready": not failed,
            "r05_bundle_created": False,
            "fresh_external_review_required": True,
            "next": "13-13fi",
        },
        "locks": {
            "r03_immutable": True,
            "r04_immutable": True,
            "r04_verdicts_carry_forward_to_r05": False,
            "deterministic_audit_scope": "REPRODUCIBILITY_AND_CONSISTENCY_ONLY",
            "promote_to_13_13g": False,
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
            raise SystemExit("committed Stage13-13fh report is stale")
        if report["decision"]["status"] != "COMPLETE_R05_SYNTHESIS_READINESS":
            raise SystemExit(f"Stage13-13fh failed checks: {report['decision']['failed_checks']}")

    print(text, end="")


if __name__ == "__main__":
    main()
