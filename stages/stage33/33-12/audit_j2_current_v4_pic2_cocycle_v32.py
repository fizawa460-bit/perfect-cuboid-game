#!/usr/bin/env python3
"""V32 diagnostic: replay the current J2 marked-Pic/2 V4 cocycle exactly.

The current compactification data are V31 cc=0 and the V30 ct class in the
20D semantic Pic(K) basis.  Only the six nonzero Pic(K) basis rows are needed:
their exact pullbacks to the locked full Pic(S) 64D basis were already
materialized in j2-ct-six-kc-support-fullpic64-pullbacks.json.  We therefore
transport the current pair to Pic(S)/2, where the locked cc/ct action matrices
and cocycle equations are independently certified by
v4_pic2_raw_cocycle_projection.py.

Equality after pullback reflects equality in Pic(K)/2 because the immutable
upstream source checks Rank(ChangeRing(MatKtoS,GF(2))) eq 20.
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

LOCKS = {
    V30: "5f911ca53e5e16374250e34e74e557229a9477d4814c910b8db7880dd993d66d",
    V31: "a2e74b2344f380c6e908e282309bb8d31dc4cfcb5a70c05365e1120ced6726fb",
    SIX: "592704594d6d26f9e0b0b2ba529d50c34fd801cede779b4e42b1cf775b63a96d",
    SEM: "c17439c877de3d1cdebd716f4ba2571fb67ec9f07e30d944eafc39ae534380c0",
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

    projection = project_raw_cocycle(raw_cc, raw_ct)

    result = {
        "success": True,
        "schema": "STAGE33_12_J2_CURRENT_V4_PIC2_COCYCLE_REPLAY_V32_DIAGNOSTIC",
        "current_marked_pic2": {
            "cc_semantic_picK20_f2": cc20,
            "ct_semantic_picK20_f2": ct20,
            "ct_support_1based": support1,
            "ct_support_BigK_indices_1based": support_bigk,
        },
        "full_surface_pullback": {
            "cc_fullPic64_f2": raw_cc,
            "ct_fullPic64_f2": raw_ct,
            "ct_weight": sum(raw_ct),
            "six_row_xor_reconstruction_exact": True,
            "picK_to_picS_mod2_injectivity_source_lock": {
                "repo": "MichaelStollBayreuth/Verification",
                "commit": UPSTREAM_COMMIT,
                "path": UPSTREAM_PATH,
                "source_assertion": "assert Rank(ChangeRing(MatKtoS, GF(2))) eq 20;",
            },
        },
        "v4_cocycle_replay": {
            "cc_involution_equation": True,
            "ct_involution_equation": True,
            "cc_ct_commutation_equation": True,
            "tau_component_equals_ct_when_cc_zero": True,
            "locked_full_surface_H1_projection": projection,
        },
        "source_locks": {
            "v30_canonical_sha256": LOCKS[V30],
            "v31_canonical_sha256": LOCKS[V31],
            "six_pullbacks_canonical_sha256": LOCKS[SIX],
            "semantic_picK_basis_canonical_sha256": LOCKS[SEM],
        },
        "firewall": {
            "integral_pic_lifts_materialized": False,
            "hs_d2_2cocycle_materialized": False,
            "hs_d2_zero_or_nonzero_proved": False,
            "standard_kummer_columns_materialized": 0,
            "stage33_12_closed_exact": False,
            "stage33_13_released": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
        },
    }
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
