#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CERT = Path(__file__).with_name("source-lock-and-model-inventory.json")


def git_blob_sha(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def load_text(rel: str):
    path = ROOT / rel
    data = path.read_bytes()
    return data.decode("utf-8"), git_blob_sha(data)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


cert = json.loads(CERT.read_text(encoding="utf-8"))
require(cert["schema"] == "STAGE35_35_01_SOURCE_LOCK_AND_MODEL_INVENTORY_V1", "schema")
require(cert["status"] == "PASS_SOURCE_LOCK_COMPLETE_MODEL_INVENTORY_BOUNDED", "status")

sources = {entry["path"]: entry for entry in cert["source_locks"]}
expected_paths = {
    "stages/stage29/29-16/active-kernel-ledger.json",
    "stages/stage29/29-08/fibration-crosswalk.md",
    "stages/stage29/29-14/theorem-dependency-ledger.json",
}
require(set(sources) == expected_paths, "source path set")

loaded = {}
for rel, entry in sources.items():
    text, sha = load_text(rel)
    require(sha == entry["blob_sha"], f"blob SHA mismatch: {rel}: {sha}")
    loaded[rel] = text

kernel = json.loads(loaded["stages/stage29/29-16/active-kernel-ledger.json"])
match = [x for x in kernel["class3_kernels"] if x["kernel"] == "K16-C3-MOVING-FIBER-ARITHMETIC"]
require(len(match) == 1, "moving-fiber kernel uniqueness")
entry = match[0]
require(entry["execution_class"] == 3, "execution class")
require(entry["children"] == ["R29-FIB2"], "receiver child")
require(entry["parent_routes"] == ["J12-PARAMETRIC"], "parent route")
require(entry["endpoint_decision_capable"] is True, "decision capability")
require("uniform arithmetic/specialization theorem" in entry["needed"], "uniform theorem wall")
require("globally exhaustive reduction to finitely many fibers" in entry["needed"], "finite reduction alternative")
require("individual-fiber Chabauty or Mordell-Weil computations" in entry["firewall"], "individual-fiber firewall")

cross = loaded["stages/stage29/29-08/fibration-crosswalk.md"]
for token in [
    "[e:x:y:p:q:z:d]",
    "Kbar_c={e^2+x^2=p^2, e^2+y^2=q^2, x^2+y^2=z^2} subset P5",
    "EULER_K3_ELLIPTIC_FIBRATION_COUNT=15_GEOMETRIC",
    "ALL_15_FIBRATIONS_Q_DEFINED_CERTIFIED=false",
    "R29-FIB1=FifteenEulerK3FibrationPhysicalClassAndFieldOfDefinitionLedger",
    "R29-FIB2=ArithmeticRankSpecializationAndEndpointResidualSpaceSquareLiftPerFibration",
    "PESCH_TOTAL_FIBRATION_GLOBAL_MARGINAL_COVERAGE=true",
    "BOUNDED_MW_ENUMERATION_GLOBAL_COVERAGE=false",
    "FULL_ENDPOINT_GENUS5_FIBRATION_COUNT=28_GEOMETRIC",
    "ALL_28_FIBRATIONS_Q_DEFINED_CERTIFIED=false",
    "RATIONAL_SECTION_COVERAGE_PROVED=false",
    "RATIONAL_POINT_EXCLUSION_PROVED=false",
    "SAUNDERSON_GLOBAL_COVERAGE=false",
    "STAGEA2_GLOBAL_COVERAGE=false",
]:
    require(token in cross, f"crosswalk token missing: {token}")

require("first pair is explicitly defined over `Q(i)`" in cross, "Q(i) first rank-4 pair")
require("tau(P) in Q_{>0}^square" in cross, "Peschmann residual square predicate")
require("reduced Euclid positivity/parity/coprimality checks" in cross, "Peschmann lift side conditions")
require("Whether this fibration is one of the 15 Testa--Stoll pencils, a base change, or another elliptic pencil is still open." in cross, "Peschmann/TS relation open")

ledger = json.loads(loaded["stages/stage29/29-14/theorem-dependency-ledger.json"])
open_receivers = ledger["open_coverage_receivers"]
require("R29-FIB1" in open_receivers, "R29-FIB1 open")
require("R29-FIB2" in open_receivers, "R29-FIB2 open")
push = ledger["new_or_newly_formalized_results"]["R29-COV-K3-PUSH"]
require(push["normal_quotient_pushforward"] is True, "normal quotient pushforward")
require(push["smooth_locus_pushforward"] is True, "smooth locus pushforward")
require(push["minimal_k3_resolution_pushforward"] is True, "minimal K3 pushforward")
require(push["converse_lift"] is False, "no converse lift")
require(push["quotient_emptiness"] is False, "no quotient emptiness")

exit_state = cert["exit"]
require(exit_state["source_lock_complete"] is True, "source lock exit")
require(exit_state["model_inventory_complete_for_stage35_entry"] is True, "model inventory exit")
require(exit_state["Q_field_and_physical_fibration_ledger_complete"] is False, "35-02 remains open")
require(exit_state["residual_space_lift_interface_complete"] is False, "35-03 remains open")
require(exit_state["new_theorem_credit"] is False, "no theorem credit")
require(exit_state["receiver_credit"] is False, "no receiver credit")
require(exit_state["next_exact_leaf"] == "35-02_Q_FIELD_PHYSICAL_FIBRATION_LEDGER", "next leaf")

print("PASS STAGE35_35_01_SOURCE_LOCK_AND_MODEL_INVENTORY_V1")
