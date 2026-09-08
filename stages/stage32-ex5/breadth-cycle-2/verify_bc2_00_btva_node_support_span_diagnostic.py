#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ARTIFACT = ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2-00-btva-node-support-span-diagnostic.json"
MAIN_STATE = ROOT / "stages/stage32-ex5/MAIN-STATE.json"
AGG = ROOT / "stages/stage32/residual-32-01-production/aggregate_stage32_post21bl_full178_node_mass_shards.py"
CONTRACT = ROOT / "stages/stage29/29-02c-LG2/finite-search-contract.md"
RESULT = ROOT / "stages/stage29/29-02c-LG2/result.md"

EXPECTED_CANONICAL = "fd4a566243959a3bbabccfe68ffd1aa52de10ad591f0916819591e35b4d7563d"
EXPECTED_BLOBS = {
    MAIN_STATE: "6721539364b40622572d6cf9fe2898a1f6b8d0f2",
    AGG: "92561bbc1cac6f2d5c47bf37bfbc9c6bfaba3cdd",
    CONTRACT: "2c1a4813a77b517482b6fef497f9a517c9d12fe6",
    RESULT: "820ed4e1b1a53db14085678de6f186b59ae0ea48",
}


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    hdr = f"blob {len(data)}\0".encode()
    return hashlib.sha1(hdr + data).hexdigest()


def main() -> None:
    p = json.loads(ARTIFACT.read_text())
    got = p.pop("canonical_sha256_without_this_field")
    assert got == EXPECTED_CANONICAL
    assert csha(p) == EXPECTED_CANONICAL

    assert p["schema"] == "STAGE32EX5_BC2_00_BTVA_NODE_SUPPORT_SPAN_DIAGNOSTIC_V1"
    assert p["status"] == "FIRST_PASS_COHERENT_REENTRY_DIAGNOSTIC_UNAUDITED"
    assert p["route_family"] == "SYMMETRIC_DIFFERENTIAL_NODE_SUPPORT_SPAN_LANE"
    assert p["reentry"]["criterion"] == "MATERIALLY_NEW_ROUTE_FAMILY_WITH_NEW_BREADTH_CYCLE"
    assert p["reentry"]["final_material_novelty_requires_second_pass_dedup"] is True
    assert p["theorem_source"]["locator"] == "Theorem 1.2"
    assert p["theorem_source"]["doi"] == "10.2140/ant.2022.16.1377"
    assert p["theorem_source"]["arxiv"] == "1912.08908"
    assert "seven singularities that span P^6" in p["theorem_source"]["necessary_conditions"]["genus0_nonconic"]
    assert "six singularities spanning a hyperplane" in p["theorem_source"]["necessary_conditions"]["genus1_consequence"]

    for path, expected in EXPECTED_BLOBS.items():
        assert git_blob_sha(path) == expected, (path, git_blob_sha(path), expected)

    state = json.loads(MAIN_STATE.read_text())
    assert state["current"]["status"] == "EX5_ROUTE_DECISION_CLOSURE_BOUNDED_EXHAUSTION_AUDITED"
    assert "MATERIALLY_NEW_ROUTE_FAMILY_WITH_NEW_BREADTH_CYCLE" in state["route_anti_loop"]["reentry_requires_one_of"]
    assert state["credit"]["stage32_main_credit"] is False

    agg_text = AGG.read_text()
    assert '"formula": "e >= ceil((d-16g+16)/4)"' in agg_text
    assert 'node_support_hashes.add(p["node_support_certificate_canonical_sha256"])' in agg_text
    assert '"strong_48bit_node_support_not_inferred_from_exceptional_mass": True' in agg_text
    assert '"theorem_credit": False' in agg_text
    assert '"receiver_credit": False' in agg_text

    contract_text = CONTRACT.read_text()
    assert "exceptional-divisor incidence lower bounds from Testa--Stoll Lemma 21" in contract_text
    assert "These filters do not by themselves certify effectivity." in contract_text

    result_text = RESULT.read_text()
    for token in [
        "repo=https://github.com/MichaelStollBayreuth/Verification",
        "commit=51233ed5ef2bf228fac9416c66db9adc0ebcaadd",
        "file=Cuboids/cuboids.magma",
        "blob=0422b69847f2afb97cb7b3ed02ebef91279f61b1",
        "the 48 singular points and known low-degree curves",
    ]:
        assert token in result_text

    assert p["authority"]["arsenal_read_in_first_pass"] is False
    assert p["authority"]["repository_wide_dedup_complete"] is False
    assert p["authority"]["route_credit"] is False
    assert p["authority"]["mathematical_credit"] is False
    assert p["firewalls"]["mass_not_labelled_support"] is True
    assert p["firewalls"]["node_count_not_projective_span"] is True
    assert p["firewalls"]["known_32_conics_exception_preserved"] is True
    assert p["firewalls"]["genus1_alternative_preserved"] is True
    assert p["firewalls"]["stage32_main_credit"] is False

    print(json.dumps({
        "verdict": "PASS_BC2_00_BTVA_NODE_SUPPORT_SPAN_FIRST_PASS_DIAGNOSTIC",
        "canonical_sha256": EXPECTED_CANONICAL,
        "route_credit": False,
        "mathematical_credit": False,
        "second_pass_dedup_required": True,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
