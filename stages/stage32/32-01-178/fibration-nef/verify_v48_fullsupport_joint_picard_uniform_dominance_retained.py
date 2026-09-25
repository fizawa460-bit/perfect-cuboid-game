#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ART = HERE / "V48-FULLSUPPORT-JOINT-PICARD-UNIFORM-DOMINANCE.json"
ART_BLOB = "50ca55cdb03b68e1eff3399cfdabe2d82f8d7328"
ART_CANON = "15e475bd6dec8a8047f20df0ae2379df1fb2218a1dfd8e3f7db7d0806d343ca3"
THEOREM = HERE / "verify_v48_fullsupport_joint_picard_uniform_dominance.py"
THEOREM_BLOB = "726869efd5d4a574ad536253bc4908802a02ba66"
PROBE = HERE / "run_v48_fullsupport_joint_picard_cell_probe.py"
PROBE_BLOB = "048b61e9cd93d97afa3e22f47eab98904bde85af"
SUPPORT_BLOB = "37e72735125c232e534d92c6e24c7afc0a0f4f24"
JOINT_BLOB = "490db30dc7e4bfc42da0e6dd9947a644dea14275"

def req(v: bool, m: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + m)

def blob(p: Path) -> str:
    raw = p.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canon(o: dict) -> str:
    x = dict(o)
    x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

def main() -> None:
    req(ART.is_file() and blob(ART) == ART_BLOB, "uniform dominance artifact blob drift")
    req(THEOREM.is_file() and blob(THEOREM) == THEOREM_BLOB, "uniform dominance theorem verifier blob drift")
    req(PROBE.is_file() and blob(PROBE) == PROBE_BLOB, "successor probe blob drift")

    art = json.loads(ART.read_text())
    req(canon(art) == ART_CANON == art["canonical_sha256_without_this_field"], "uniform dominance artifact canonical drift")
    req(art["status"] == "UNIFORM_POINTWISE_SUCCESSOR_DOMINANCE_PROVED__ZERO_MAIN_CREDIT__EXECUTION_REQUIRED_FOR_NUMERIC_GAIN", "status drift")

    sl = art["source_locks"]
    req(sl["support_worker_blob_sha1"] == SUPPORT_BLOB, "support source lock drift")
    req(sl["joint_min_verifier_blob_sha1"] == JOINT_BLOB, "joint source lock drift")
    req(sl["successor_probe_blob_sha1"] == PROBE_BLOB, "probe source lock drift")
    req(sl["uniform_dominance_verifier_blob_sha1"] == THEOREM_BLOB, "theorem source lock drift")

    claim = art["claim"]
    req(claim["same_population"] is True, "same-population claim missing")
    req(claim["additive_subtraction"] is False, "additive subtraction forbidden")
    req(claim["statistical_independence"] is False, "independence assumption forbidden")
    req(claim["actual_retained_numeric_gain_claimed"] is False, "numerical gain overclaim")

    reg = art["bounded_regression"]
    req(reg["threshold_states"] == 1120, "threshold regression drift")
    req(reg["strict_tset_states"] == 524, "strict t-set regression drift")
    req(reg["empty_joint_states"] == 238, "empty joint regression drift")
    req(reg["qcut_states_with_nonempty_joint_set"] == 137592, "qcut regression state drift")
    req(reg["qcut_states_with_empty_joint_set"] == 37128, "empty-joint qcut state drift")
    req(reg["strict_qcut_states"] == 17742, "strict qcut state drift")
    req(reg["max_qcut_drop"] == 61, "max qcut drop drift")

    sw = art["strict_witnesses"]["small_exact_qcut"]
    req(sw["separate_tset"] == [1,3] and sw["joint_tset"] == [1], "small t-set witness drift")
    req((sw["current_fullsupport_qcut"], sw["joint_picard_qcut"], sw["strict_qcut_drop"]) == (62,58,4), "small qcut witness drift")

    hw = art["strict_witnesses"]["active_region_structural_threshold"]
    req((hw["b"],hw["c"],hw["support"],hw["t"]) == (36,89,5,103), "active structural target drift")
    req((hw["separate_floor"],hw["joint_floor"],hw["strict_floor_gain"]) == (3137,3377,240), "active structural floor drift")
    req(hw["retained_positive_histogram_mass_at_qbc_test_claimed"] is False, "structural witness overclaimed retained mass")

    scope = art["scope"]
    req(scope["heavy_execution_armed"] is False, "heavy execution unexpectedly armed")
    req(scope["production_scaleout_authorized"] is False, "production unexpectedly authorized")
    req(scope["new_numeric_tightening_claimed"] is False, "numeric tightening overclaim")
    req(scope["main_consumption_performed"] is False, "producer self-consumed")

    for k,v in art["firewalls"].items():
        if k == "hostile_audit_required_before_promotion":
            req(v is True, "hostile audit firewall drift")
        else:
            req(v is False, "credit firewall drift " + k)

    subprocess.run([sys.executable, str(THEOREM)], check=True)

    print("V48_FULLSUPPORT_JOINT_PICARD_UNIFORM_DOMINANCE_RETAINED=PASS")
    print("UNIVERSAL_NONWEAKENING=true")
    print("NUMERIC_GAIN_REQUIRES_AUTHORIZED_EXECUTION=true")
    print("MAIN_CREDIT_CHANGED=false")

if __name__ == "__main__":
    main()
