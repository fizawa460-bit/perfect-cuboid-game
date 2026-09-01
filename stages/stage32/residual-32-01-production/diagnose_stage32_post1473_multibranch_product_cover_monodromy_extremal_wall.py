#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

D = 186
E = 266
UPSTREAM_CANONICAL = "250f987a4aa298362ce0c8b4a0993d762434e0cece3236a85f08280d5587b078"
TANGENT_CANONICAL = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"
NOTE_BLOB_SHA1 = "667672b0980a00ef55bbdbb4e6e0e7e0e9cf20cf"
CERT_CANONICAL = "1184aec81858aafe84183297644722bc2bffbe0013c79de5a2fec92c031d218b"


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def canonical_without(path: Path, field: str) -> tuple[dict, str]:
    obj = json.loads(path.read_text())
    body = dict(obj)
    body.pop(field, None)
    return obj, csha(body)


def main() -> None:
    repo = Path(__file__).resolve().parents[3]
    here = Path(__file__).resolve().parent

    upstream_path = here / "post1473-specific-class-multibranch-beauville-odd-branch-wall.json"
    note_path = here / "post1473-specific-class-multibranch-product-cover-monodromy-extremal-wall.md"
    cert_path = here / "post1473-specific-class-multibranch-product-cover-monodromy-extremal-wall.json"
    tangent_path = repo / "stages/stage33/33-07/exceptional-p1-tangent-coordinates.json"

    upstream, upstream_actual = canonical_without(upstream_path, "canonical_sha256_without_this_field")
    if upstream_actual != UPSTREAM_CANONICAL or upstream.get("canonical_sha256_without_this_field") != UPSTREAM_CANONICAL:
        raise ValueError(f"audited upstream canonical moved: {upstream_actual}")

    if git_blob_sha1(note_path) != NOTE_BLOB_SHA1:
        raise ValueError("source note blob moved")

    tangent, tangent_actual = canonical_without(tangent_path, "canonical_sha256")
    if tangent_actual != TANGENT_CANONICAL or tangent.get("canonical_sha256") != TANGENT_CANONICAL:
        raise ValueError(f"retained tangent canonical moved: {tangent_actual}")
    progress = tangent.get("constructive_progress", {})
    required_false = (
        "order2_source_first_residue_functions_materialized",
        "project_14x26_L_squareclass_tensor_materialized",
        "absolute_delta_loc_computed",
        "chosen_global_geometric_lifts_materialized",
    )
    if any(progress.get(k) is not False for k in required_false):
        raise ValueError("retained tangent evidence boundary changed")

    # Audited q'=2 case: n1+n2=q'd/4=93 and n_i<=floor(q'O/8)=floor(O/4).
    q2_sum = 2 * D // 4
    if q2_sum != 93:
        raise ValueError("q'=2 projection-degree sum regression")
    allowed_q2 = [O for O in range(0, E + 1, 2) if q2_sum <= 2 * (O // 4)]
    if not allowed_q2 or min(allowed_q2) != 188 or 186 in allowed_q2:
        raise ValueError(f"q'=2 integer sharpening failed: {allowed_q2[:3]}")
    s1_q2_min = math.ceil((3 * min(allowed_q2) - E) / 2)
    if s1_q2_min != 149:
        raise ValueError(f"q'=2 S1 lower bound regression: {s1_q2_min}")

    # q'=4 at the audited extremal O=d=186.
    q4 = 4
    O = D
    q4_sum = q4 * D // 4
    cap = q4 * O // 8
    if q4_sum != 186 or cap != 93:
        raise ValueError("q'=4 extremal projection arithmetic regression")
    n1 = n2 = 93
    if n1 + n2 != q4_sum or n1 > cap or n2 > cap:
        raise ValueError("q'=4 extremal equality regression")
    R1 = q4 * O - 8 * n1
    R2 = q4 * O - 8 * n2
    if (R1, R2) != (0, 0):
        raise ValueError(f"extremal projection ramification not zero: {(R1, R2)}")
    if R1 + R2 != 2 * q4 * (O - D):
        raise ValueError("ramification remainder identity regression")

    cert, cert_actual = canonical_without(cert_path, "canonical_sha256_without_this_field")
    if cert_actual != CERT_CANONICAL or cert.get("canonical_sha256_without_this_field") != CERT_CANONICAL:
        raise ValueError(f"new certificate canonical mismatch: {cert_actual}")
    ex = cert["exact_sharpening"]
    if ex["qprime_2"] != {"n1_plus_n2": 93, "necessary_even_O_min": 188, "S1_min": 149, "O_186_possible": False}:
        raise ValueError("certificate q'=2 payload mismatch")
    q4c = ex["qprime_4_extremal_O_186"]
    expected_q4 = {
        "n1": 93,
        "n2": 93,
        "R1": 0,
        "R2": 0,
        "projection1_etale": True,
        "projection2_etale": True,
        "full_V4_monodromy_required": True,
    }
    if q4c != expected_q4:
        raise ValueError("certificate q'=4 extremal payload mismatch")
    boundary = cert["evidence_boundary"]
    if boundary["carrier_full_V4_monodromy_evaluated"] is not False or boundary["current_evidence_excludes_multibranch_carrier"] is not False:
        raise ValueError("nonexclusion firewall moved")

    print("STAGE32_POST1473_MULTIBRANCH_PRODUCT_COVER_MONODROMY_EXTREMAL_DIAGNOSTIC=PASS")
    print(f"QPRIME2_MIN_EVEN_O={min(allowed_q2)}")
    print(f"QPRIME2_MIN_S1={s1_q2_min}")
    print("O186_REQUIRES_QPRIME4_FULL_V4=true")
    print("O186_PROJECTIONS=93,93")
    print("O186_PROJECTION_RAMIFICATION=0,0")
    print(f"CERT_CANONICAL={CERT_CANONICAL}")


if __name__ == "__main__":
    main()
