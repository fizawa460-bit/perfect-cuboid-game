#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages" / "stage32-ex1" / "ex1-00-source-lock-and-target-adapter.json"

def load_json(rel):
    with (ROOT / rel).open("r", encoding="utf-8") as f:
        return json.load(f)

def canonical_sha256(obj):
    payload = dict(obj)
    payload.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()

def git_blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()

def require(cond, msg):
    if not cond:
        raise AssertionError(msg)

def main():
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(canonical_sha256(cert) == cert["canonical_sha256_without_this_field"], "certificate canonical sha256 mismatch")

    locks = cert["source_locks"]
    loaded = {}
    for name, lock in locks.items():
        path = ROOT / lock["path"]
        require(path.is_file(), f"missing source: {name}: {path}")
        require(git_blob_sha1(path) == lock["blob_sha1"], f"blob sha1 mismatch: {name}")
        if path.suffix == ".json":
            obj = json.loads(path.read_text(encoding="utf-8"))
            require(canonical_sha256(obj) == lock["canonical_sha256"], f"canonical sha256 mismatch: {name}")
            loaded[name] = obj

    witness = loaded["v6_witness"]
    require(witness["target"]["row_id"] == "g1-d186", "wrong V6 row")
    require(witness["witness"]["self_intersection"] == 758, "wrong D^2")
    require(witness["target"]["d"] == 186, "wrong d")
    require(witness["target"]["e"] == 266, "wrong e")
    require(witness["witness"]["positive_exceptional_support"] == 47, "wrong V6 positive exceptional support")
    require(witness["witness"]["zero_exceptional_indices"] == [5], "wrong zero exceptional index")

    ae = loaded["v6_member_gap"]
    replay = ae["exact_effective_divisor_replay"]
    require(replay["C_square"] == 758, "AE D^2 mismatch")
    require(replay["K_dot_C"] == 186, "AE K.D mismatch")
    require(replay["arithmetic_genus"] == 473, "AE arithmetic genus mismatch")
    require(replay["required_total_genus_defect_if_integral"] == 472, "AE genus defect mismatch")
    require(replay["target_normalization_genus"] == 1, "AE target genus mismatch")
    require(replay["effective_divisor_exists_in_V6_class"] is True, "AE effectivity missing")
    require(replay["effective_divisor_is_not_integral_irreducible_genus1_carrier"] is True, "AE member firewall missing")
    boundary = ae["retained_member_level_boundary"]
    require(boundary["actual_integral_irreducible_genus1_carrier_materialized"] is False, "AE falsely materializes carrier")
    require(boundary["class_level_data_sufficient_to_choose_member"] is False, "AE falsely chooses member")

    require((758 + 186) // 2 + 1 == 473, "adjunction arithmetic replay failed")
    require(473 - 1 == 472, "normalization defect replay failed")

    ah = loaded["v6_exceptional_and_fsm"]
    exc = ah["v6_exact_data"]["exceptional_pairings"]
    require(len(exc) == 48, "exceptional pairing count mismatch")
    require(sum(exc) == 266, "exceptional mass mismatch")
    require(sum(x > 0 for x in exc) == 47, "positive exceptional support mismatch")
    require(ah["v6_exact_data"]["zero_exceptional_labels_1based"] == [6], "zero exceptional label mismatch")
    require(ah["local_A1_resolution"]["observed_total_exceptional_mass"] == 266, "AH exceptional mass mismatch")
    require(ah["local_A1_resolution"]["node_model"] == "Spec C[x,y,z]/(xz-y^2) = C^2/{+-1}, x=p^2,y=pq,z=q^2", "AH local A1 model mismatch")

    ad = loaded["genus1_node_span"]
    require(ad["exact_replay"]["exceptional_count"] == 48, "AD exceptional count mismatch")
    require(ad["exact_replay"]["positive_exceptional_count"] == 47, "AD positive exceptional count mismatch")
    require(ad["exact_replay"]["zero_exceptional_ids"] == ["EXC_006"], "AD exceptional label mismatch")
    require(ad["conditional_geometric_reading"]["positive_exceptional_pairing_then_meets_corresponding_node"] is True,
            "AD contact semantic adapter missing")
    require(ad["conditional_geometric_reading"]["actual_effective_integral_carrier_proved"] is False,
            "AD falsely proves actual carrier")

    ag = loaded["v6_known140_decomposition"]
    mono = ag["known140_monoid"]
    require(mono["membership"] is True, "known140 monoid membership missing")
    require(mono["nonzero_term_count"] == 61, "known140 term count mismatch")
    require(mono["total_multiplicity"] == 155, "known140 total multiplicity mismatch")
    require(mono["exceptional_curve_multiplicity"] == 82, "known140 exceptional multiplicity mismatch")
    require(mono["normal_curve_multiplicity"] == 73, "known140 normal multiplicity mismatch")
    require(mono["integral_irreducible_genus1_member_constructed"] is False, "AG falsely constructs member")

    c = cert["v6_target"]
    require(c["D_square"] == 758 and c["K_dot_D"] == 186, "certificate V6 invariants mismatch")
    require(c["arithmetic_genus"] == 473 and c["required_total_normalization_genus_defect"] == 472,
            "certificate genus arithmetic mismatch")
    ecc = cert["exceptional_contact_contract"]
    require(ecc["exceptional_pairings"] == exc, "certificate exceptional pairing vector mismatch")
    require(ecc["exceptional_pairing_sum"] == 266, "certificate exceptional mass mismatch")
    require(ecc["exceptional_total_mass_266_is_not_total_delta_472"] is True, "266!=472 firewall missing")

    fire = cert["firewalls"]
    require(fire["266_equals_472"] is False, "forbidden 266=472 identification")
    require(fire["exceptional_pairing_equals_local_delta_without_adapter"] is False, "local delta firewall missing")
    require(fire["effective_divisor_materializes_integral_irreducible_genus1_member"] is False, "member firewall missing")
    require(fire["Q_or_Qi_field_of_definition_asserted"] is False, "unsupported arithmetic field assertion")
    for key in ("stage32_main_credit", "receiver_credit", "theorem_credit", "endpoint_credit",
                "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim"):
        require(fire[key] is False, f"forbidden credit/claim: {key}")

    require(cert["exit"]["source_lock_complete"] is True, "EX1-00 source lock not marked complete")
    require(cert["exit"]["credit_ceiling"] == "SOURCE_LOCK_AND_TARGET_ADAPTER_ONLY", "wrong credit ceiling")
    require(cert["exit"]["next_leaf"] == "EX1-01_GLOBAL_NORMALIZATION_DEFECT_DECOMPOSITION", "wrong next leaf")
    print("PASS_STAGE32EX1_EX1_00_SOURCE_LOCK_AND_TARGET_ADAPTER")

if __name__ == "__main__":
    main()
