#!/usr/bin/env python3
"""V32: certify the current J2 marked-Pic/2 V4 cocycle exactly.

V31 gives cc=0 and V30 gives the ct class in the semantic Pic(K) basis.  The
six nonzero Pic(K) rows already have exact pullbacks to the locked full Pic(S)
64D basis.  Replaying them through the independently locked full-surface V4
action verifies the involution and commutation cocycle equations and projects
the current class to the retained 75D H1 basis.

The resulting weight-15 coordinate is compared with the older named-J2 H1
artifact only after the current derivation succeeds.  The historical artifact
is comparison-only and is not revived as a derivation authority or promoted to
a standard Kummer column.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from v4_pic2_raw_cocycle_projection import project_raw_cocycle

HERE = Path(__file__).resolve().parent
V30 = HERE / "j2-current-lambda-d-odd-ramified-cech-overlaps-v30.json"
V31 = HERE / "j2-current-cc-global-square-cech-overlap-v31.json"
SIX = HERE / "j2-ct-six-kc-support-fullpic64-pullbacks.json"
SEM = HERE / "j2-semantic-kc-picard-basis.json"
HIST = HERE / "j2-named-v4-h1-target-before-source-orientation.json"
OUT = HERE / "j2-current-v4-pic2-cocycle-v32.json"

LOCKS = {
    V30: "5f911ca53e5e16374250e34e74e557229a9477d4814c910b8db7880dd993d66d",
    V31: "a2e74b2344f380c6e908e282309bb8d31dc4cfcb5a70c05365e1120ced6726fb",
    SIX: "592704594d6d26f9e0b0b2ba529d50c34fd801cede779b4e42b1cf775b63a96d",
    SEM: "c17439c877de3d1cdebd716f4ba2571fb67ec9f07e30d944eafc39ae534380c0",
    HIST: "4625b6d3ea19ec0e4d8a51471c7f60c0c1219de4672d84c64779c4213306f3b3",
    OUT: "e91a7b701690efde3884ca1edc2182b25033a3ff6c7d89bcb8092d02f5a50a7e",
}
UPSTREAM_COMMIT = "51233ed5ef2bf228fac9416c66db9adc0ebcaadd"
UPSTREAM_PATH = "Cuboids/cuboids.magma"


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def locked(path: Path) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    expected = LOCKS[path]
    assert claimed == expected == csha(body), (path.name, claimed, csha(body))
    return obj


def xor_rows(rows: list[list[int]]) -> list[int]:
    out = [0] * 64
    for row in rows:
        assert len(row) == 64
        out = [a ^ (int(b) & 1) for a, b in zip(out, row)]
    return out


def main() -> None:
    v30 = locked(V30)
    v31 = locked(V31)
    six = locked(SIX)
    sem = locked(SEM)
    hist = locked(HIST)
    out = locked(OUT)

    cc20 = v31["actual_cc_defect_marked_pic_mod2"]["coordinates_mod2"]
    ct20 = v30["actual_ct_defect_marked_pic_mod2"]["coordinates"]
    assert cc20 == [0] * 20
    assert len(ct20) == 20 and all(x in (0, 1) for x in ct20)
    assert v31["v4_pic_mod2_frontier"]["ct_coordinates_from_v30"] == ct20

    support0 = [i for i, bit in enumerate(ct20) if bit]
    support1 = [i + 1 for i in support0]
    indlist_k = sem["upstream_source_lock"]["indlistK_1based"]
    assert len(indlist_k) == 20
    support_bigk = [indlist_k[i] for i in support0]

    pullbacks = six["pullbacks"]
    pullback_bigk = [row["BigK_index_1based"] for row in pullbacks]
    assert support_bigk == pullback_bigk == [26, 35, 42, 47, 49, 52]
    assert six["exact_checks"]["only_six_required_support_rows_materialized"] is True
    assert six["exact_checks"]["all_six_rows_reconstructed_from_retained_140_class_marking"] is True
    assert six["exact_checks"]["all_six_rows_transport_through_stage33_09_marked_basis_exactly"] is True

    raw_ct = [int(x) & 1 for x in six["ct_sum_fullPic64_historical_Magma_coordinates_mod2"]]
    assert len(raw_ct) == 64
    rebuilt_ct = xor_rows([row["fullPic64_historical_Magma_coordinates"] for row in pullbacks])
    assert rebuilt_ct == raw_ct
    raw_cc = [0] * 64

    # This call independently checks cc involution, ct involution, and cc/ct
    # commutation against the locked 64D full-surface action matrices.
    projection = project_raw_cocycle(raw_cc, raw_ct)

    # Only now compare with the historical named-J2 H1 record.
    old_h1 = hist["retained_H1_projection"]
    assert projection["coordinates_f2"] == old_h1["coordinates_f2"]
    assert projection["coordinate_weight"] == old_h1["coordinate_weight"] == 15
    assert projection["one_coboundary_coefficient_witness_f2"] == old_h1["one_coboundary_coefficient_witness_f2"]

    assert out["current_marked_pic2"]["cc_semantic_picK20_f2"] == cc20
    assert out["current_marked_pic2"]["ct_semantic_picK20_f2"] == ct20
    assert out["current_marked_pic2"]["ct_support_1based"] == support1
    assert out["current_marked_pic2"]["ct_support_BigK_indices_1based"] == support_bigk
    fs = out["full_surface_pullback"]
    assert fs["cc_fullPic64_f2"] == raw_cc
    assert fs["ct_fullPic64_f2"] == raw_ct
    assert fs["ct_weight"] == sum(raw_ct) == 8
    assert fs["six_row_xor_reconstruction_exact"] is True
    inj = fs["picK_to_picS_mod2_injectivity_source_lock"]
    assert inj == {
        "repo": "MichaelStollBayreuth/Verification",
        "commit": UPSTREAM_COMMIT,
        "path": UPSTREAM_PATH,
        "source_assertion": "assert Rank(ChangeRing(MatKtoS, GF(2))) eq 20;",
    }

    coc = out["v4_1cocycle"]
    assert coc["cc_involution_equation"] is True
    assert coc["ct_involution_equation"] is True
    assert coc["cc_ct_commutation_equation"] is True
    assert coc["tau_component_equals_ct_when_cc_zero"] is True
    saved_h1 = coc["retained_H1_projection"]
    assert saved_h1["coordinates_f2"] == projection["coordinates_f2"]
    assert saved_h1["coordinate_weight"] == projection["coordinate_weight"] == 15
    assert saved_h1["nonzero"] is True
    assert saved_h1["one_coboundary_coefficient_witness_f2"] == projection["one_coboundary_coefficient_witness_f2"]
    assert saved_h1["reconstruction_exact"] is True

    cmp = out["historical_weight15_comparison"]
    assert cmp["coordinates_match_historical_named_j2_reference_exactly"] is True
    assert cmp["historical_reference_used_as_derivation_source"] is False
    boundary = out["exact_information_boundary"]
    assert boundary["current_v4_pic2_1cocycle_materialized"] is True
    assert boundary["current_retained_H1_projection_materialized"] is True
    assert boundary["current_retained_H1_projection_nonzero"] is True
    assert boundary["integral_Pic_lifts_materialized"] is False
    assert boundary["hs_d2_2cocycle_materialized"] is False
    assert boundary["hs_d2_zero_or_nonzero_proved"] is False
    assert boundary["standard_kummer_columns_materialized"] == 0
    assert boundary["stage33_12_closed_exact"] is False

    fw = out["promotion_firewall"]
    assert fw["historical_weight15_artifact_promoted_as_derivation_authority"] is False
    assert fw["standard_kummer_column_promoted"] is False
    assert fw["stage33_13_released"] is False
    assert fw["theorem_credit"] is False and fw["receiver_credit"] is False and fw["endpoint_credit"] is False

    print(json.dumps({
        "success": True,
        "canonical_sha256": LOCKS[OUT],
        "current_h1_weight": projection["coordinate_weight"],
        "historical_weight15_match": True,
        "status": out["status"],
        "next_exact_leaf": out["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
