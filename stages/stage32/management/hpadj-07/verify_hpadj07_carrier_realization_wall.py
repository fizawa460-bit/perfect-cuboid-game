#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
WALL = HERE / "CARRIER-REALIZATION-WALL.json"
EXPECTED_WALL_CANON = "b51f756e7388321d7a8b834702dd226fca3c99e8412fefd183069e3168ab7619"

LOCKS = {
    "hpadj06": (
        "stages/stage32/management/hpadj-06/CARRIER-ADAPTER.json",
        "2f8d51dd4c52cf9189b829d0cd42679ef110cef9",
        "72144be89761ba82f93fd33ca7647c90a4ba12646d5f63e70537a955d93f106d",
    ),
    "rr": (
        "stages/stage32/final-chain/32-02-effectivity/RR-EFFECTIVITY-SUFFICIENT-CHECKPOINT.json",
        "f6fd9935865542d7d05a9ce83df0263f0f051bc2",
        "ff9ca45aef3f81835609588c2a189ebd26baedd7f4f69b0cba9339a5101f22bc",
    ),
    "hperp": (
        "stages/stage32/final-chain/32-02-effectivity/HPERP-NORM-RR-ADAPTER.json",
        "320eaefb97d5308da8e5f12590d894e55ffc3c63",
        "3dea123243082e06d2d3edaadc1765c6f068f875e0367bc11f0b4138e7500b66",
    ),
    "effectivity_gap": (
        "stages/stage32/32-21/post-21bl-effectivity-gap-separation.json",
        "8b46b85a7fe7d1b366d0ada0a7db852f123e77e1",
        "4afeb8a3add7c203fbbaa9ffdb5b4b4d357df8503979ee80617db654df73d4dc",
    ),
    "genus_defect": (
        "stages/stage32/32-21/post-21bl-genus-defect-preflight.json",
        "ecf4e9d20eddcaef9375f4c6b21ecf9bf6b0cd8c",
        "e59e23b2aefb1a3b622f3f3ed4eb0f83fd7bb335125fa3254c7e4e737caaa96c",
    ),
}
ROUTE_PATH = "stages/stage29/29-02c-LG2/route-contract.json"
ROUTE_BLOB = "99752985fd705ee993d052e5bcc622181c7a4cbc"


def req(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def locked_json(rel: str, blob: str, canon: str | None = None) -> dict:
    path = ROOT / rel
    req(path.is_file(), f"missing source {rel}")
    req(git_blob(path) == blob, f"blob drift {rel}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    if canon is not None:
        req(obj.get("canonical_sha256_without_this_field") == canon, f"stored canonical drift {rel}")
        req(canonical(obj) == canon, f"canonical drift {rel}")
    return obj


def main() -> None:
    wall = json.loads(WALL.read_text(encoding="utf-8"))
    req(wall.get("schema") == "STAGE32_MAIN_HPADJ07_CARRIER_REALIZATION_WALL_V1", "wall schema")
    req(wall.get("canonical_sha256_without_this_field") == EXPECTED_WALL_CANON, "wall stored canonical")
    req(canonical(wall) == EXPECTED_WALL_CANON, "wall canonical")
    pred = wall["predecessor_boundary"]
    req(pred["hostile_audited_exact_head"] == "89e612ed3884ac6f3c10d834fe94c4d73a77c912", "predecessor head")
    req(pred["hostile_audit_status"] == "PASS", "predecessor audit")
    req(pred["merge_authorized"] is False, "predecessor merge firewall")

    src = {name: locked_json(*spec) for name, spec in LOCKS.items()}
    route = locked_json(ROUTE_PATH, ROUTE_BLOB)

    h6 = src["hpadj06"]
    req(h6["reverse_realization_gap"]["status"] == "OPEN_LOAD_BEARING", "HPADJ06 reverse gap")
    req(h6["population_interface"]["terminal_alone_asserts_integral_completion_exists"] is False,
        "terminal completion existence firewall")
    req(h6["population_interface"]["this_adapter_asserts_every_terminal_has_actual_carrier"] is False,
        "actual-carrier existence firewall")
    req(h6["proved_direction"]["contrapositive"] ==
        "HPADJ_REJECTED_TERMINAL -> NO_ACTUAL_MATCHING_INTEGRAL_IRREDUCIBLE_K3_CARRIER",
        "HPADJ06 one-way carrier exclusion")

    rr = src["rr"]
    req("integral irreducible representative" in rr["classifier"]["does_not_conclude"],
        "RR irreducibility firewall")
    req(rr["population_firewall"]["final_survivor_hperp_norm_scalar_available"] is False,
        "RR population scalar gap")
    req(rr["credit_firewall"]["effectivity_final_execution_released"] is False,
        "RR final effectivity firewall")

    hp = src["hperp"]
    req(hp["minimal_survivor_interface"]["current_full178_producer_exports_this_scalar_source_locked_here"] is False,
        "Hperp scalar producer gap")
    req(hp["credit_firewall"]["integral_irreducible_low_genus_carrier_proved"] is False,
        "Hperp carrier firewall")

    eg = src["effectivity_gap"]
    req(eg["exact_gap_result"]["actual_effective_curve_certificate_present"] is False,
        "historical effective-curve gap")
    req(eg["exact_gap_result"]["integral_irreducible_curve_certificate_present"] is False,
        "historical integral-irreducible gap")
    req(eg["strategy_selection"]["new_heavy_compute_authorized"] is False,
        "historical heavy-arm firewall")

    gd = src["genus_defect"]
    req(gd["interpretation"]["actual_effective_integral_curve_certificate_present"] is False,
        "genus-defect curve-existence firewall")
    req(gd["interpretation"]["normalization_genus1_certificate_present"] is False,
        "normalization-genus firewall")
    req(gd["interpretation"]["multibranch_case_resolved"] is False,
        "multibranch firewall")

    verdicts = route["verdicts"]
    req(verdicts["effectivity_certified"] is False, "Stage29 effectivity gap")
    req(verdicts["multibranch_cases_covered"] is False, "Stage29 multibranch gap")
    req(verdicts["isolated_rational_points_excluded"] is False, "Stage29 isolated-point gap")

    req(wall["closed_interfaces"]["terminal_to_picard64_population_identity"] is True,
        "closed terminal/Picard64 interface")
    req(wall["closed_interfaces"]["hpadj_rejected_terminal_excludes_actual_matching_integral_irreducible_k3_carrier"] is True,
        "closed one-way carrier exclusion")

    gates = wall["load_bearing_reverse_chain"]
    req([g["gate"] for g in gates] == [
        "A_INTEGRAL_PICARD_COMPLETION_EXISTENCE",
        "B_EFFECTIVE_DIVISOR_EXISTENCE",
        "C_INTEGRAL_IRREDUCIBLE_CARRIER",
        "D_NORMALIZATION_AND_BRANCH_COMPATIBILITY",
        "E_RECEIVER_ENDPOINT",
    ], "reverse-chain ordering")
    req(all(g["current_status"].startswith("OPEN") for g in gates), "reverse-chain must remain open")

    req(wall["non_routes"]["repeat_terminal_to_picard64_interface"] ==
        "DOMINATED_ALREADY_CLOSED_BY_HPADJ05_HPADJ06", "terminal-interface anti-loop")
    req(wall["non_routes"]["repeat_rr_effectivity_as_irreducibility"] ==
        "INVALID_SEMANTIC_PROMOTION", "RR semantic anti-promotion")
    req(wall["non_routes"]["blind_full178_heavy_arm"] ==
        "NOT_AUTHORIZED_BY_THIS_CHECKPOINT", "heavy anti-loop")

    req(wall["scope"]["main_authority_mutated"] is False, "MAIN authority firewall")
    req(wall["scope"]["main_pruning_credit"] is False, "MAIN pruning firewall")
    req(wall["scope"]["heavy_compute_used"] is False, "heavy-compute use firewall")
    req(wall["scope"]["heavy_compute_authorized"] is False, "heavy-compute authorization firewall")
    req(wall["scope"]["new_cross_lane_demand_opened"] is False, "cross-lane demand firewall")
    for key, value in wall["firewalls"].items():
        req(value is False, f"credit/firewall unexpectedly true: {key}")

    print("PASS hpadj07 precise reverse carrier-realization wall; gates A-E open; no MAIN credit/heavy arm")


if __name__ == "__main__":
    main()
