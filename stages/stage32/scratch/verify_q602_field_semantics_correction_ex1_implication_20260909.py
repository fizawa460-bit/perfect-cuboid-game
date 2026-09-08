#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ART = HERE / "q602-field-semantics-correction-ex1-implication-preflight-20260909.json"
COMMON = ROOT / "stages/stage32/residual-32-01-production/post1484-o210-q4-common-double-cover-cartesian-identity.json"
CORR = ROOT / "stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-correspondence-rosati-frontier.json"
TRANS = ROOT / "stages/stage32/residual-32-01-production/post1505-o210-q602-weierstrass-parity-transvection-refinement.json"
HCHAR = ROOT / "stages/stage32/residual-32-01-production/post1623-hperp-v6-hdeck-character-preflight.json"
FRONT = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"


def canonical(x: dict) -> str:
    y = dict(x)
    y.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(y, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def load(p: Path) -> dict:
    return json.loads(p.read_text())


def main() -> None:
    a = load(ART)
    assert canonical(a) == a["canonical_sha256_without_this_field"] == "e141b1987c74a736d9606af4ee689ad2a7fb1ad6c7deb98912d18111493acd8c"

    common = load(COMMON)
    corr = load(CORR)
    trans = load(TRANS)
    hchar = load(HCHAR)
    assert common["canonical_sha256_without_this_field"] == a["source_locks"]["common_double_cover"]["canonical_sha256"]
    assert corr["canonical_sha256_without_this_field"] == a["source_locks"]["bolza_correspondence"]["canonical_sha256"]
    assert trans["canonical_sha256_without_this_field"] == a["source_locks"]["q602_transvection"]["canonical_sha256"]
    assert hchar["canonical_sha256_without_this_field"] == a["source_locks"]["hdeck_character"]["canonical_sha256"]

    assert common["carrier_consequence"]["hypothesis"].startswith("N is the normalization of a hypothetical integral carrier")
    assert corr["correspondence_endomorphism"]["definition"] == "T=(f1)_*(f2)^* in End(J(C0))"
    assert corr["fixed_correspondence"]["target_curve"]["usual_model"] == "s^2=x^5-x"
    assert [corr["fixed_correspondence"]["maps"]["f1"]["degree"], corr["fixed_correspondence"]["maps"]["f2"]["degree"]] == [105,81]
    assert trans["retained_residue_filter"]["surviving_residues_decimal"] == [73,97,235]
    assert hchar["fixed_target"]["surviving_residues_decimal"] == [73,97,235]

    # The retained carrier/correspondence contracts above contain no requirement
    # that the hypothetical V6 member itself be Q-defined.  Therefore BI/BJ's
    # non-Q-definedness fact cannot be promoted into an active Q602 field blocker.
    assert a["retained_q602_semantics"]["q_definedness_of_carrier_required"] is False
    assert a["active_interface_consequence"]["field_descent_blocker_added"] is False
    assert a["correction_of_prior_scratch"]["retracted_active_interface_inference"].startswith("This fact does NOT")

    front = FRONT.read_text()
    for cid in a["source_locks"]["active_frontier"]["claim_ids"]:
        assert cid in front
    assert '"claim_id":"S32.V6.MEMBER_LEVEL_Q602_LOCAL_IDENTITY.V2"' in front
    assert 'without changing population, model, field, or marking semantics' in front
    assert '"authority_status":"DECLARED_GOAL"' in front

    assert a["decision"]["MAIN_credit_changed"] is False
    assert a["decision"]["Q602_excluded"] is False
    assert a["decision"]["O210_excluded"] is False
    assert a["firewalls"]["ex1_terminal_promoted"] is False
    assert a["firewalls"]["o210_vacuous_exclusion_promoted"] is False
    assert a["firewalls"]["q602_vacuous_exclusion_promoted"] is False

    print("PASS_STAGE32_MAIN_Q602_FIELD_SEMANTICS_CORRECTION_EX1_IMPLICATION_PREFLIGHT")
    print(a["canonical_sha256_without_this_field"])


if __name__ == "__main__":
    main()
