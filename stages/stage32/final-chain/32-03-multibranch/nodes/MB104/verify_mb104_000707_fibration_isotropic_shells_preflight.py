#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
CERT = HERE / "MB104-000707-FIBRATION-ISOTROPIC-SHELLS-PREFLIGHT-CERTIFICATE.json"
RUNKEY = HERE / "runkeys" / "000707-FIBRATION-ISOTROPIC-SHELLS-V1.json"
STATE = ROOT / "stages/stage32/final-chain/32-03-multibranch/fib/STATE.json"
RETAINED_RUNNER = HERE / "run_mb104_000707_fibration_isotropic_shells.py"
LOCAL_ENGINE = HERE / "run_mb104_000707_fibration_shell_local_exact.py"
LOCAL_SHARD_VERIFIER = HERE / "verify_mb104_000707_fibration_shell_local_exact_shard.py"
LOCAL_AGGREGATE = HERE / "aggregate_mb104_000707_fibration_shell0_local_exact.py"
PICARD_BASE = ROOT / "stages/stage33/33-07/picard_base_rows_retained.py"
PICARD_MARKING = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"
STOLL_HELPER = ROOT / "stages/stage33/33-07/stoll_cuboid_source.py"
HPERP_ADAPTER = ROOT / "stages/stage32/residual-32-01-production/hperp_integral_adapter.py"
PAIRING_PREFIX = ROOT / "stages/stage32/residual-32-01-production/pairing_prefix_engine.py"
RESIDUAL = HPERP_ADAPTER.parent


def blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


d = json.loads(CERT.read_text(encoding="utf-8"))
k = json.loads(RUNKEY.read_text(encoding="utf-8"))
s = json.loads(STATE.read_text(encoding="utf-8"))

assert d["schema"] == "STAGE32_MB104_000707_FIBRATION_ISOTROPIC_SHELLS_PREFLIGHT_V5"
assert d["status"] == "PRE_AUDIT_EXECUTION_PREFLIGHT_COLD_GEN12_LOCAL_EXACT_DISJOINT_SHARDS_NO_NUMERICAL_RESULT_NO_CREDIT"
assert d["support"]["mask"] == "000707000f0f"
assert d["support"]["P2"] == 336
assert d["support"]["H_dot_P"] == 112
expected = [
    (0,10,30,10,400,-320),
    (1,10,34,9,400,-288),
    (2,10,38,8,400,-256),
    (3,12,36,12,144,-192),
]
got = [
    (x["shell_index"],x["H_dot_F"],x["P_dot_F"],x["support_mass"],x["minus_transform_square"],x["transform_dot_P"])
    for x in d["shells"]
]
assert got == expected

assert k["schema"] == "STAGE32_MB104_000707_FIBRATION_ISOTROPIC_SHELLS_RUNKEY_V1"
assert k["generation"] == 12
assert k["mode"] == "COLD"
assert k["armed"] is False
assert k["support_mask"] == "000707000f0f"
assert k["pilot"]["shell_index"] == 0
assert k["pilot"]["measured"] is False
assert k["resume"]["partition_key"] == "shell0_split_coordinate_interval_shard"
assert k["resume"]["expected_workunit_count"] == 8
assert k["resume"]["aggregate_requires_exact_union_0_7"] is True
assert k["concurrency"]["planned_effective_heavy_concurrency"] == 1
assert k["concurrency"]["stage_heavy_cap"] == 18
assert k["execution_gate"]["automatic_execution_authorized"] is False
assert k["execution_gate"]["state_transition_recorded"] is False
assert k["execution_gate"]["current_head_execution_blocked"] is True

assert s["schema"] == "STAGE32_MB_FIB_STATE_V1"
assert s["execution"]["runkey_generation"] == 12
assert s["execution"]["heavy_armed"] is False
assert s["execution"]["execution_authorized"] is False

# Fail closed before executing any retained or replacement engine source.
LOCK_BEFORE_EXEC = {
    "runner_git_blob": RETAINED_RUNNER,
    "local_exact_engine_git_blob": LOCAL_ENGINE,
    "local_exact_shard_verifier_git_blob": LOCAL_SHARD_VERIFIER,
    "local_exact_aggregate_git_blob": LOCAL_AGGREGATE,
    "stage33_stoll_helper_blob": STOLL_HELPER,
    "stage33_picard_marking_blob": PICARD_MARKING,
    "stage33_picard_base_rows_blob": PICARD_BASE,
    "hperp_integral_adapter_blob": HPERP_ADAPTER,
    "pairing_prefix_engine_blob": PAIRING_PREFIX,
}
for key, path in LOCK_BEFORE_EXEC.items():
    got_blob = blob(path)
    assert d["source_locks"][key] == got_blob, ("certificate", key, d["source_locks"][key], got_blob)
    assert k["source_locks"][key] == got_blob, ("runkey", key, k["source_locks"][key], got_blob)
    assert s["imported_source"][key] == got_blob, ("STATE", key, s["imported_source"][key], got_blob)

g11 = d["execution_repair"]["generation11_failure"]
assert g11["run_id"] == 35510077408
assert g11["execution_head"] == "4e6d3ddea9d0369d001539a2794b7577c389195e"
assert g11["artifact_id"] == 10604769896
assert g11["status"] == "EXECUTION_FAILED_NO_NUMERICAL_RESULT"
assert g11["failure_stage"] == "PUBLIC_MAGMA_CVP_WALL_BEFORE_FIRST_SHELL_ROW"
assert g11["mathematical_credit"] is False

spec = importlib.util.spec_from_file_location("mbfib_local_exact", LOCAL_ENGINE)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)

contract = mod.split_contract(0, 8)
assert contract["shell_index"] == 0
assert contract["shard_count"] == 8
assert contract["coverage_is_exact_disjoint"] is True
assert len(contract["coordinate_bounds"]) == 63
assert len(contract["intervals"]) == 8
assert contract["bound_method"] == "EXACT_DUAL_NORM_DIAGONAL_FROM_POSITIVE_DEFINITE_HPERP_GRAM"
nonempty = [tuple(x) for x in contract["intervals"] if x[0] <= x[1]]
assert nonempty
assert nonempty[0][0] == contract["split_coordinate_bound"][0]
assert nonempty[-1][1] == contract["split_coordinate_bound"][1]
for a,b in zip(nonempty,nonempty[1:]):
    assert a[1] + 1 == b[0]

solver, x, y, f, problem = mod.build_solver(0, 0, shard_count=8, timeout_ms=1)
assert len(x) == 63 and len(y) == 140 and len(f) == 64
assert len(solver.assertions()) > 250
assert problem["pc"] == -320
assert problem["shell"]["hperp_norm"] == 400
assert problem["shell"]["support_mass"] == 10

source = LOCAL_ENGINE.read_text(encoding="utf-8")
assert 'SolverFor("QF_NIA")' in source
assert "run_magma(" not in source
assert "CloseVectors(" not in source
assert "exact_coordinate_bounds" in source
assert "split_contract" in source
assert "PARTIAL_UNKNOWN_NO_CREDIT" in source
assert "COMPLETE_EXACT_SHARD_ZERO_CREDIT" in source
assert "certificate_source_locks" in source
assert "execution_surface_generation" in source
assert "local_exact_engine_git_blob" in source
assert "local_exact_shard_verifier_git_blob" in source

shard_verify_source = LOCAL_SHARD_VERIFIER.read_text(encoding="utf-8")
assert 'd["source_locks"] == engine.certificate_source_locks()' in shard_verify_source

aggregate_source = LOCAL_AGGREGATE.read_text(encoding="utf-8")
assert "SHARD_VERIFIER" in aggregate_source
assert "subprocess.run([" in aggregate_source
assert 'd.get("status") != "COMPLETE_EXACT_SHARD_ZERO_CREDIT"' in aggregate_source
assert 'd.get("solver", {}).get("final_solver_result") != "unsat"' in aggregate_source
assert "expected_source_locks = engine.certificate_source_locks()" in aggregate_source
assert "input_shard_canonical_sha256" in aggregate_source

# Retain the hostile-audited exact H-perp -> Picard64 bridge check.
sys.path.insert(0, str(RESIDUAL))
adapter_spec = importlib.util.spec_from_file_location("mbfib_hperp_integral_adapter_gen12", HPERP_ADAPTER)
adapter_mod = importlib.util.module_from_spec(adapter_spec)
assert adapter_spec.loader is not None
sys.modules[adapter_spec.name] = adapter_mod
adapter_spec.loader.exec_module(adapter_mod)
marking = mod.retained.load_marking()
bundle = mod.retained.load_picard_base()
adapter = adapter_mod.HperpIntegralPairingAdapter.from_retained(marking, bundle)
ac = adapter.certificate
assert ac["saturated_picard64_integral_adapter_validated"] is True
assert ac["retained_basis_known_labels_1based"] == mod.retained.RETAINED_BASIS_KNOWN_LABELS_1BASED
assert ac["selected64_change_of_basis_unimodular"] is True
assert ac["selected64_gram_change_of_basis_exact"] is True

assert d["enumeration"]["shell0_shard_count"] == 8
assert d["enumeration"]["resume_first"] is True
assert d["enumeration"]["unknown_or_resource_wall_is_no_credit"] is True
assert all(v is False for v in d["firewalls"].values())
assert all(v is False for v in k["credit"].values())
print(json.dumps({
    "success": True,
    "generation": 12,
    "split_coordinate_0based": contract["split_coordinate_0based"],
    "split_coordinate_bound": contract["split_coordinate_bound"],
    "intervals": contract["intervals"],
}, sort_keys=True))
print("PASS: 000707 generation12 local exact shell0 engine is cold, source-locked, disjoint-partitioned, resumable, and zero-credit")
