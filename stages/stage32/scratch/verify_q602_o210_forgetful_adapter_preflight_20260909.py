#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ART = ROOT / "stages/stage32/scratch/q602-o210-forgetful-adapter-preflight-20260909.json"
ACTIVE = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def canonical_sha256(obj: dict) -> str:
    x = dict(obj)
    x.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def assert_lock(lock: dict) -> dict | str:
    path = ROOT / lock["path"]
    data = path.read_bytes()
    assert git_blob_sha1(data) == lock["blob_sha1"], (path, git_blob_sha1(data), lock["blob_sha1"])
    if path.suffix == ".json":
        obj = json.loads(data)
        if "canonical_sha256" in lock:
            assert obj.get("canonical_sha256_without_this_field") == lock["canonical_sha256"]
            assert canonical_sha256(obj) == lock["canonical_sha256"]
        return obj
    return data.decode()


def merged_claims(active: dict) -> dict[str, dict]:
    out = {}
    for c in active.get("supporting_claims", []):
        out[c["claim_id"]] = c
    for c in active.get("claims", []):
        out[c["claim_id"]] = c
    return out


def main() -> None:
    a = load_json(ART)
    assert a["schema"] == "STAGE32_Q602_O210_FORGETFUL_ADAPTER_PREFLIGHT_V1"
    assert a["status"] == "SCRATCH_EXACT_UNAUDITED_TYPED_ADAPTER_PREFLIGHT"
    assert canonical_sha256(a) == a["canonical_sha256_without_this_field"] == "bfd17b6b41e32ab9ce729c2fb735477beb3e70061576433a16d1d0ad30edce69"

    t = a["fixed_target"]
    assert t == {
        "row_id": "g1-d186", "picard_class": "V6", "d": 186, "e": 266,
        "genus": 1, "O": 210, "qprime": 4, "Q": 602,
        "formal_surviving_residue_labels": [73, 97, 235]
    }

    locks = a["source_locks"]
    common = assert_lock(locks["common_double_cover"])
    bolza = assert_lock(locks["bolza_correspondence"])
    f2 = assert_lock(locks["q602_f2_adapter"])
    trans = assert_lock(locks["q602_transvection_refinement"])
    note = assert_lock(locks["q602_transvection_source_note"])

    # Source-typed construction: actual Q602 data are decorations of one O210 carrier.
    assert common["fixed_target"]["row_id"] == "g1-d186"
    assert "hypothetical integral carrier" in common["carrier_consequence"]["hypothesis"]
    assert common["carrier_consequence"]["first_factor"].startswith("Y is the normalization of N")
    assert common["carrier_consequence"]["second_factor"].startswith("Y is the normalization of N")
    assert common["carrier_consequence"]["same_quadratic_extension"] is True

    assert bolza["fixed_target"]["row_id"] == "g1-d186"
    assert bolza["fixed_target"]["O"] == 210 and bolza["fixed_target"]["qprime"] == 4
    assert bolza["fixed_correspondence"]["source_curve"] == {"name": "Y", "genus": 106}
    assert bolza["fixed_correspondence"]["maps"]["f1"]["degree"] == 105
    assert bolza["fixed_correspondence"]["maps"]["f2"]["degree"] == 81
    assert bolza["correspondence_endomorphism"]["definition"] == "T=(f1)_*(f2)^* in End(J(C0))"

    assert f2["fixed_target"]["row_id"] == "g1-d186"
    assert f2["fixed_target"]["O"] == 210 and f2["fixed_target"]["qprime"] == 4
    assert f2["q602_pointwise_exact_W_test"]["surviving_residue_count"] == 16
    assert f2["q602_pointwise_exact_W_test"]["Q602_excluded"] is False

    assert trans["fixed_target"]["row_id"] == "g1-d186"
    assert trans["fixed_target"]["O"] == 210 and trans["fixed_target"]["qprime"] == 4 and trans["fixed_target"]["Q"] == 602
    assert trans["common_involution_parity"]["correspondence_orientation"] == "T=(f1)_*(f2)^*"
    assert trans["retained_residue_filter"]["surviving_residues_decimal"] == [73, 97, 235]
    assert trans["retained_residue_filter"]["Q602_excluded"] is False
    assert "For the fixed O210 correspondence" in note
    assert "actual correspondence" in note

    # Runtime binding to the current effective frontier. This is not an immutable source lock.
    active = load_json(ACTIVE)
    claims = merged_claims(active)
    o210 = claims["S32.O210.EXCLUSION.V3"]
    surv = claims["S32.Q602.SURVIVORS_73_97_235.V1"]
    rb = a["adapter_candidate"]["runtime_bindings"]
    assert o210["claim_core_sha256"] == rb["o210_exclusion_claim_core_sha256"]
    assert o210["authority_status"] == "AUDITED"
    assert o210["scope"] == {"row_id":"g1-d186","picard_class":"V6","O":210,"qprime":4,"target":"population_wide_exclusion"}
    assert surv["claim_core_sha256"] == rb["q602_survivor_claim_core_sha256"]
    assert surv["authority_status"] == "AUDITED"
    assert surv["scope"]["surviving_residues"] == [73, 97, 235]

    ad = a["adapter_candidate"]
    assert ad["claim_id"] == "S32.ADAPTER.Q602_ADMISSIBLE_TO_O210_POPULATION.V1"
    assert ad["kind"] == "adapter_contract"
    assert ad["bridges"]["from_scope_key"] == "S32.Q602.ADMISSIBLE_CONFIGURATION"
    assert ad["bridges"]["to_scope_key"] == "S32.O210.COVER"
    assert "injectivity and surjectivity are neither required nor asserted" in ad["bridges"]["semantics"]
    assert ad["requires"] == ["S32.MAIN.CURRENT_TARGET_CONTEXT.V1", "S32.Q602.SURVIVORS_73_97_235.V1"]

    q2 = a["downstream_q602_claim_candidate"]
    assert q2["claim_id"] == "S32.Q602.EXCLUSION.V2"
    assert q2["new_version_required"] is True
    assert q2["requires"] == [
        "S32.MAIN.CURRENT_TARGET_CONTEXT.V1",
        "S32.Q602.SURVIVORS_73_97_235.V1",
        "S32.O210.EXCLUSION.V3",
        "S32.ADAPTER.Q602_ADMISSIBLE_TO_O210_POPULATION.V1",
    ]

    g = a["authority_gates"]
    assert g["scratch_only"] is True
    assert g["post_sync_o210_reaudit_pass_required_before_downstream_consumption"] is True
    assert g["typed_adapter_hostile_audit_required"] is True
    assert g["q602_v2_hostile_audit_required"] is True
    assert g["claim_sync_required_after_each_pass"] is True
    for k in [
        "q602_excluded_now", "o212_plus_advance_allowed", "full178_complete",
        "stage32_closed", "endpoint_credit", "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim", "merge_authorized"
    ]:
        assert g[k] is False, (k, g[k])

    print("PASS_STAGE32_SCRATCH_Q602_O210_FORGETFUL_ADAPTER_PREFLIGHT")
    print(a["canonical_sha256_without_this_field"])
    print("formal_residues_retained=[73,97,235]")
    print("geometric_q602_realization_population_maps_to_exact_o210_population=true")
    print("authority_change=false")


if __name__ == "__main__":
    main()
