#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage32-ex2/EX2-03/known140-zero-curve-omission-witnesses.json"
HERE = ROOT / "stages/stage32/residual-32-01-production"
STAGE33_07 = ROOT / "stages/stage33/33-07"
V6 = ROOT / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
AG = HERE / "post1648ag-v6-known140-basis-elimination.json"
EX2_02 = ROOT / "stages/stage32-ex2/EX2-02/exact-fixed-component-extraction.json"
DIAG = ROOT / "stages/stage32-ex2/diagnose_ex2_03c_known140_omission.py"
WORKFLOW = ROOT / ".github/workflows/stage32ex2-ex2-03c-known140-omission.yml"
RUNKEY = ROOT / "stages/stage32-ex2/runkeys/ex2-03c-known140-omission.json"

EXPECTED_CERT_BLOB = "a4b9396790b6c3b026a4a624247a48b1148a6d36"
EXPECTED_CANONICAL = "60f6b4010549485282fab8d78da0e863e4746b07a83a9a0e33ddb2e175330330"
LOCKS = {
    DIAG: "b972cb8ccc5e827b2375428d13e6770538af37f6",
    WORKFLOW: "3ceee84e523bdbedf6d5638a5adcd7566389de51",
    RUNKEY: "f2425c03f0c8b81d658bd930cd843a0c3523fca7",
    V6: "dae90ed19395355bebeebe2a6aa6bb1c6e53c244",
    AG: "e0bbe443919d1ec5424bffa84c1c5a79befbdf1e",
    EX2_02: "b07fd12a40acbfc478cdab472157cb4a34efe39c",
}

sys.path.insert(0, str(HERE))
from hperp_integral_adapter import HperpIntegralPairingAdapter  # noqa: E402


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def main() -> None:
    assert blob(CERT) == EXPECTED_CERT_BLOB
    for path, expected in LOCKS.items():
        assert blob(path) == expected, (path, blob(path), expected)

    cert = json.loads(CERT.read_text())
    assert cert["schema"] == "STAGE32EX2_EX2_03C_RETAINED_ZERO_CURVE_OMISSION_WITNESSES_V1"
    assert cert["status"] == "PASS_RETAINED_EXACT_OMISSION_WITNESSES_FOR_TWO_ZERO_CURVES"
    payload = dict(cert)
    stored = payload.pop("canonical_sha256_without_this_field")
    assert stored == EXPECTED_CANONICAL == csha(payload)

    runkey = json.loads(RUNKEY.read_text())
    assert runkey["generation"] == 1 and runkey["armed"] is True
    assert runkey["target_zero_labels_1based"] == [17, 21, 24, 25, 30, 31, 98]

    v6 = json.loads(V6.read_text())
    ag = json.loads(AG.read_text())
    ex2_02 = json.loads(EX2_02.read_text())
    assert v6["canonical_sha256_without_this_field"] == "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
    assert ag["canonical_sha256_without_this_field"] == "03adb4f7522470dd15fa0a74e1c142da823824a6e9d853348615f670c159d25d"
    assert ex2_02["exact_scan"]["zero_pairing_labels_1based"] == [17, 21, 24, 25, 30, 31, 98]

    # Giant retained payloads stay runner-side and are imported only through the
    # existing exact adapter. Nothing is whole-fetched into chat context.
    bundle = load_retained(STAGE33_07 / "picard_base_rows_retained.py", "ex2_03c_picard")
    marking = load_retained(STAGE33_07 / "stage32_picard_marking_retained.py", "ex2_03c_marking")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    coords = adapter.class_coordinates_in_retained_basis
    gram = Matrix(bundle["picard_gram_64x64"])
    vcoords = Matrix([int(x) for x in v6["witness"]["picard_coordinates"]])
    stored_pairings = [int(x) for x in v6["witness"]["all140_pairings"]]

    assert cert["certified_nonfixed_zero_labels_1based"] == [17, 98]
    assert cert["unresolved_zero_labels_1based"] == [21, 24, 25, 30, 31]
    assert len(cert["positive_witnesses"]) == 2

    for witness in cert["positive_witnesses"]:
        z = int(witness["zero_label_1based"])
        coeffs = [0] * 140
        for term in witness["decomposition"]:
            label = int(term["known140_label_1based"])
            mult = int(term["multiplicity"])
            assert 1 <= label <= 140 and mult > 0
            assert coeffs[label - 1] == 0
            coeffs[label - 1] = mult
        assert coeffs[z - 1] == 0
        assert len(witness["decomposition"]) == witness["nonzero_term_count"]
        assert sum(coeffs) == witness["total_multiplicity"]
        # The diagnostic commits to the complete 140-coefficient vector, not
        # merely its sparse serialization.
        assert csha(coeffs) == witness["decomposition_sha256"]

        reconstructed = coords.T * Matrix(coeffs)
        assert reconstructed == vcoords
        replay_pairings = [int(x) for x in (coords * gram * reconstructed)]
        assert replay_pairings == stored_pairings
        assert witness["picard64_reconstruction_exact"] is True
        assert witness["all140_pairing_reconstruction_exact"] is True

    assert cert["inference"]["curve_17_nonfixed_divisorial_component"] is True
    assert cert["inference"]["curve_98_nonfixed_divisorial_component"] is True
    assert cert["inference"]["remaining_five_fixedness_unresolved"] is True
    assert cert["inference"]["fixed_part_fully_classified"] is False
    assert cert["claim_sync"]["triggered"] is True

    for row in cert["bounded_negative_results"]:
        assert row["zero_label_1based"] in [21, 24, 25, 30, 31]
        assert row["credit"] == "NO_EXACT_WITNESS_MATERIALIZED_NO_UNSAT_CREDIT"

    for key, value in cert["credit_firewall"].items():
        assert value is False, (key, value)

    print(json.dumps({
        "verdict": "PASS_STAGE32EX2_EX2_03C_RETAINED_OMISSION_WITNESSES",
        "certified_nonfixed_zero_labels_1based": [17, 98],
        "unresolved_zero_labels_1based": [21, 24, 25, 30, 31],
        "fixed_part_fully_classified": False,
        "stage32_main_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
