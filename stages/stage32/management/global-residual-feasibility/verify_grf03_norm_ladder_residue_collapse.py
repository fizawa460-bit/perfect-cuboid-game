#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CERT = HERE / "GRF-03-NORM-LADDER-RESIDUE-COLLAPSE.json"
GRF02 = HERE / "GRF-02-PROJECTED-KERNEL.json"
STAGE29 = ROOT / "stages/stage29/29-02c-LG2/finite-search-contract.md"
HPERP = ROOT / "stages/stage32/residual-32-01-production/hperp_integral_adapter.py"
BUNDLE_DIR = ROOT / "stages/stage33/33-07"
BUNDLE_SOURCE = BUNDLE_DIR / "picard_base_rows_retained.py"

sys.path.insert(0, str(BUNDLE_DIR))
import picard_base_rows_retained as retained_bundle

EXPECTED = {
    GRF02: "7c1cda07749fbfb90245995d1def2ae96fb5604b",
    STAGE29: "2c1a4813a77b517482b6fef497f9a517c9d12fe6",
    HPERP: "fb1eb380ca786e42a6b00c5ef454b0e79fdba771",
    BUNDLE_SOURCE: "82e4d450a1d852e34f6615440fb88a029c6e54eb",
}
EXPECTED_CERT_CANONICAL = "b7ff04666b5a29f7cca5da4df0fd9076a6e785702b594bda602cb4085d45c15d"
EXPECTED_GRF02_CANONICAL = "2e08a25e2de891bfabd0bf96ba06d928d733711b2c27449c9818b856665d4d6f"
EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise RuntimeError(msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def main() -> None:
    for path, expected in EXPECTED.items():
        req(path.is_file(), f"missing source lock: {path.relative_to(ROOT)}")
        req(blob(path) == expected, f"source-lock drift: {path.relative_to(ROOT)}")

    cert = json.loads(CERT.read_text())
    stored = cert.pop("canonical_sha256_without_this_field", None)
    req(stored == EXPECTED_CERT_CANONICAL, "GRF-03 stored canonical drift")
    req(csha(cert) == EXPECTED_CERT_CANONICAL, "GRF-03 canonical drift")
    req(
        cert["status"]
        == "EXACT_SYMBOLIC_NO_GO_NORM_LADDER_CONGRUENCE_ADDS_NO_OBSTRUCTION_NO_CREDIT",
        "GRF-03 status drift",
    )

    grf02 = json.loads(GRF02.read_text())
    grf02_stored = grf02.pop("canonical_sha256_without_this_field", None)
    req(grf02_stored == EXPECTED_GRF02_CANONICAL, "GRF-02 stored canonical drift")
    req(csha(grf02) == EXPECTED_GRF02_CANONICAL, "GRF-02 canonical drift")
    rows = grf02["exact_completion_kernel"]["primitive_equation_rows"]
    req(
        rows == [{
            "coefficients": [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            "modulus": 2,
        }],
        "GRF-02 completion parity drift",
    )

    stage29 = STAGE29.read_text()
    req("geometric genus 0, even canonical degree d<=176" in stage29, "Stage29 G0 even-degree contract drift")
    req("geometric genus 1, even canonical degree d<=192" in stage29, "Stage29 G1 even-degree contract drift")
    req("y=m*C-n*H" in stage29, "Stage29 Hperp definition drift")

    bundle = retained_bundle.load()
    req(bundle["canonical_sha256"] == EXPECTED_BUNDLE_CANONICAL, "Picard bundle canonical drift")
    gram = [[int(v) for v in row] for row in bundle["picard_gram_64x64"]]
    req(len(gram) == 64 and all(len(row) == 64 for row in gram), "Picard Gram shape drift")
    req(all(gram[i][j] == gram[j][i] for i in range(64) for j in range(64)), "Picard Gram symmetry drift")
    req(all(gram[i][i] % 2 == 0 for i in range(64)), "retained Picard64 is not even")

    # Exact algebraic collapse:
    # N = 16 n^2 - m^2 C^2 and
    # B_g(d) = 16 n^2 + m^2(d+2-2g).
    # Hence N == B_g(d) mod 2m^2 iff C^2+d+2-2g is even.
    # Every integral Picard64 completion has even C^2 because G has even diagonal.
    for g, cap in ((0, 176), (1, 192)):
        for d in range(2, cap + 1, 2):
            r = math.gcd(d, 16)
            m = 16 // r
            n = d // r
            req((d + 2 - 2 * g) % 2 == 0, f"required parity failed at g={g}, d={d}")
            for c2 in (0, 2, -2, 14, -18):
                N = 16 * n * n - m * m * c2
                B = 16 * n * n + m * m * (d + 2 - 2 * g)
                req((N - B) % (2 * m * m) == 0, f"norm-ladder congruence failed at g={g}, d={d}, C2={c2}")

    req(cert["even_lattice_collapse"]["norm_ladder_congruence_automatic_for_every_integral_completion"], "automatic-congruence flag drift")
    req(not cert["consequence"]["new_quadratic_residue_obstruction_from_norm_ladder_mod_2m2_alone"], "no-go firewall drift")
    req(not cert["ownership"]["concrete_row_or_stratum_selected"], "MAIN selected a concrete 178 target")
    req(not cert["credit_firewall"]["main_pruning_credit"], "unexpected MAIN pruning credit")
    req(not cert["credit_firewall"]["merge_authorized"], "unexpected merge authorization")

    print("GRF-03 PASS: exact norm-ladder congruence is automatic on integral even-Picard completions; no new residue obstruction.")


if __name__ == "__main__":
    main()
