#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PATH = HERE / "bc2-01-support-adapter-preflight.json"


def canonical_sha256_without_this_field(obj):
    payload = dict(obj)
    expected = payload.pop("canonical_sha256_without_this_field")
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return expected, hashlib.sha256(raw).hexdigest()


def require(cond, msg):
    if not cond:
        raise AssertionError(msg)


data = json.loads(PATH.read_text(encoding="utf-8"))
expected, actual = canonical_sha256_without_this_field(data)
require(expected == actual, f"canonical sha mismatch: {expected} != {actual}")
require(data["schema"] == "STAGE32EX5_BC2_01_SUPPORT_ADAPTER_PREFLIGHT_V1", "schema drift")
require(data["leaf"] == "BC2-01_SUPPORT_ADAPTER_PREFLIGHT", "leaf drift")
require(data["status"] == "PREFLIGHT_CONTRACT_PASS_RUNTIME_CALIBRATION_PENDING", "status drift")

auth = data["authority"]
for key in ("hostile_audit_credit", "mathematical_credit", "receiver_credit", "route_qualified", "stage32_main_credit"):
    require(auth[key] is False, f"unauthorized credit: {key}")

adapter = data["adapter_contract"]
require(adapter["node_count"] == 48, "node-count drift")
require("32/32 exact equality" in adapter["calibration_pass_condition"], "calibration condition weakened")
require("never accepted" in adapter["mass_firewall"], "mass firewall weakened")

canon = data["canonical_node_labelling"]
require(canon["requirement"] == "independent of Magma set iteration order", "canonical-label requirement drift")
joined_forbidden = "\n".join(canon["forbidden_shortcuts"])
for token in ("raw iteration index", "floating-point", "Sprint", "exceptional-mass-only"):
    require(token in joined_forbidden, f"missing forbidden shortcut firewall: {token}")

span = data["span_contract"]
require(span["genus0_nonconic_necessary_predicate"] ==
        "support_count >= 7 AND full supported-node coordinate rank == 7",
        "genus-0 predicate drift")
require("six supported nodes" in span["genus1_safe_consequence_predicate"] and
        "rank is 6" in span["genus1_safe_consequence_predicate"],
        "genus-1 witness predicate drift")
require("do not require the full support to have rank exactly 6" in span["genus1_do_not_use"],
        "genus-1 anti-overstrengthening firewall missing")

fw = data["firewalls"]
for key in ("FULL178_closed", "O210_excluded", "Q602_excluded",
            "runtime_calibration_claimed", "effectivity_inferred_from_numerical_survival",
            "perfect_cuboid_nonexistence_claim", "stage32_main_credit"):
    require(fw[key] is False, f"unsafe firewall value: {key}")
for key in ("known_32_conic_exception_preserved", "genus1_hyperplane_component_alternative_preserved"):
    require(fw[key] is True, f"required theorem alternative lost: {key}")
require(fw["mass_treated_as_labelled_support"] is False, "mass mislabeled as support")

require(data["next_if_runtime_calibration_passes"]["leaf"] == "BC2-02_FULL178_SUPPORT_RECONSTRUCTION",
        "next leaf drift")
require(data["next_if_runtime_calibration_passes"]["receiver_exclusion_credit_on_adapter_pass_alone"] is False,
        "adapter pass improperly grants receiver exclusion credit")

print("PASS BC2-01 support-adapter preflight contract")
print(f"canonical_sha256={actual}")
print("runtime_calibration=NOT_CLAIMED")
