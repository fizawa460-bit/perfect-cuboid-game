#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ART = HERE / "post1728-v6-empty-o210-q602-typed-adapter-preflight.json"
REG = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
EX3 = ROOT / "stages/stage32-ex3/MAIN-STATE.json"
EXPECTED = "8f236d2f8f55df2f84b252b1e5ad4e656aa3d786c56e0d54642cdb5575e98e1a"


def csha(x: dict) -> str:
    y = dict(x); y.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(y, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def claim(reg: dict, cid: str) -> dict:
    return next(c for c in reg["claims"] if c["claim_id"] == cid)


def main() -> None:
    a = json.loads(ART.read_text())
    r = json.loads(REG.read_text())
    e = json.loads(EX3.read_text())
    assert a["canonical_sha256_without_this_field"] == EXPECTED and csha(a) == EXPECTED
    v6 = claim(r, "S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V2")
    ad = claim(r, "S32.ADAPTER.EX1_V6_CARRIER_TO_MAIN_V6_CARRIER.V1")
    ex1 = claim(r, "S32.EX1.ALL_V6_GENUS1_CARRIERS_EXCLUDED_CANDIDATE.V2")
    assert v6["authority_status"] == ad["authority_status"] == ex1["authority_status"] == "AUDITED"
    assert v6["audit_receipt"]["review_id"] == ad["audit_receipt"]["review_id"] == 5147810198
    assert ex1["audit_receipt"]["review_id"] == 5147627146
    ft = e["fixed_target"]
    assert ft["row_id"] == "g1-d186" and ft["picard_class"] == "V6"
    assert ft["carrier_integral"] and ft["carrier_irreducible"] and ft["target_geometric_genus"] == 1
    assert ft["context_O"] == 210 and ft["context_qprime"] == 4 and ft["context_Q"] == 602
    assert ft["context_surviving_residues"] == [73,97,235]
    cc = e["completion_contract"]
    assert cc["exclusion_requires_population_preserving_cover_exhaustiveness"] is True
    assert cc["positive_terminal_requires_same_actual_V6_carrier_adapter"] is True
    assert a["o210_adapter_preflight"]["requires_hostile_audit"] is True
    assert a["q602_adapter_preflight"]["requires_hostile_audit"] is True
    assert a["decision"]["o210_credit_now"] is False
    assert a["decision"]["q602_credit_now"] is False
    print("PASS_STAGE32_POST1728_V6_EMPTY_O210_Q602_TYPED_ADAPTER_PREFLIGHT")
    print(EXPECTED)


if __name__ == "__main__":
    main()
