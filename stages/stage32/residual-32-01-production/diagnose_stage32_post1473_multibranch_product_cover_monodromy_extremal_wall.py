#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

D = 186
E = 266
UPSTREAM_CANONICAL = "250f987a4aa298362ce0c8b4a0993d762434e0cece3236a85f08280d5587b078"
WITNESS_CANONICAL = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
ALL140_CANONICAL = "4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3"
TANGENT_CANONICAL = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"
NOTE_BLOB_SHA1 = "c6430ca94a4897f9f50104ab76a4eaae60df4268"
CERT_CANONICAL = "1d7086f7ebd2a826f42d0f8d67fef075a64b5af214c92e681c4a8b36e9b03c0f"
DP_STATE_COUNT = 216095
DP_STATES_SHA256 = "315a6f45625584fa3fa9e91fa69ad34bb682c34dc746eddb59f12b113b46d5bf"


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


def partitions(n: int, lo: int = 1):
    if n == 0:
        yield ()
        return
    for first in range(lo, n + 1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def local_states(m: int) -> set[tuple[int, int, int]]:
    if m == 0:
        return {(0, 0, 0)}
    return {
        (len(p), sum(x & 1 for x in p), sum(x == 1 for x in p))
        for p in partitions(m)
    }


def replay_partition_states(exceptional: list[int]) -> set[tuple[int, int, int]]:
    states = {(0, 0, 0)}
    for m in exceptional:
        local = local_states(m)
        states = {
            (B + b, O + o, S1 + s1)
            for B, O, S1 in states
            for b, o, s1 in local
        }
    return states


def main() -> None:
    repo = Path(__file__).resolve().parents[3]
    here = Path(__file__).resolve().parent

    upstream_path = here / "post1473-specific-class-multibranch-beauville-odd-branch-wall.json"
    note_path = here / "post1473-specific-class-multibranch-product-cover-monodromy-extremal-wall.md"
    cert_path = here / "post1473-specific-class-multibranch-product-cover-monodromy-extremal-wall.json"
    witness_path = repo / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
    tangent_path = repo / "stages/stage33/33-07/exceptional-p1-tangent-coordinates.json"

    upstream, upstream_actual = canonical_without(upstream_path, "canonical_sha256_without_this_field")
    if upstream_actual != UPSTREAM_CANONICAL or upstream.get("canonical_sha256_without_this_field") != UPSTREAM_CANONICAL:
        raise ValueError(f"audited upstream canonical moved: {upstream_actual}")

    if git_blob_sha1(note_path) != NOTE_BLOB_SHA1:
        raise ValueError("source note blob moved")

    witness, witness_actual = canonical_without(witness_path, "canonical_sha256_without_this_field")
    if witness_actual != WITNESS_CANONICAL or witness.get("canonical_sha256_without_this_field") != WITNESS_CANONICAL:
        raise ValueError(f"V6 witness canonical moved: {witness_actual}")
    all140 = [int(x) for x in witness["witness"]["all140_pairings"]]
    if len(all140) != 140 or csha(all140) != ALL140_CANONICAL:
        raise ValueError("V6 all140 pairing lock moved")
    exceptional = all140[92:]
    if len(exceptional) != 48 or sum(exceptional) != E:
        raise ValueError("V6 exceptional vector regression")

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

    # Reuse the exact finite-partition layer only as a nonexclusion check for the sharpened threshold.
    states = replay_partition_states(exceptional)
    if len(states) != DP_STATE_COUNT or csha(sorted(states)) != DP_STATES_SHA256:
        raise ValueError("exact branch-partition state space moved")
    min_s1_ge188 = min(S1 for _B, O, S1 in states if O >= 188)
    if min_s1_ge188 != 149 or (188, 188, 149) not in states:
        raise ValueError("sharpened q'=2 coarse boundary unexpectedly excluded")
    if (186, 186, 146) not in states:
        raise ValueError("audited q'=4 coarse extremal state disappeared")

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
    q2c = cert["exact_sharpening"]["qprime_2"]
    if q2c["necessary_even_O_min"] != 188 or q2c["S1_min"] != 149 or q2c["coarse_extremal_reachable_state"] != {"B":188,"O":188,"S1":149}:
        raise ValueError("certificate q'=2 payload mismatch")
    q4c = cert["exact_sharpening"]["qprime_4_extremal_O_186"]
    if (q4c["n1"], q4c["n2"], q4c["R1"], q4c["R2"]) != (93,93,0,0):
        raise ValueError("certificate q'=4 arithmetic payload mismatch")
    if q4c["projection1_etale"] is not True or q4c["projection2_etale"] is not True or q4c["full_V4_monodromy_required"] is not True:
        raise ValueError("certificate q'=4 geometry payload mismatch")
    boundary = cert["evidence_boundary"]
    if boundary["carrier_full_V4_monodromy_evaluated"] is not False or boundary["current_evidence_excludes_multibranch_carrier"] is not False:
        raise ValueError("nonexclusion firewall moved")

    print("STAGE32_POST1473_MULTIBRANCH_PRODUCT_COVER_MONODROMY_EXTREMAL_DIAGNOSTIC=PASS")
    print(f"QPRIME2_MIN_EVEN_O={min(allowed_q2)}")
    print(f"QPRIME2_MIN_S1={s1_q2_min}")
    print(f"QPRIME2_COARSE_MIN_S1={min_s1_ge188}")
    print("QPRIME2_COARSE_EXTREMAL_188_188_149=true")
    print("O186_REQUIRES_QPRIME4_FULL_V4=true")
    print("O186_PROJECTIONS=93,93")
    print("O186_PROJECTION_RAMIFICATION=0,0")
    print(f"CERT_CANONICAL={CERT_CANONICAL}")


if __name__ == "__main__":
    main()
