#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CERT = HERE / "GRF-06-ODD-PRIME-AFFINE-COLUMN-IMAGE-KERNEL.json"
GRF01 = HERE / "GRF-01-DESIGN.md"
GRF05 = HERE / "GRF-05-INTEGRAL-FINITE-QUOTIENT-LOWER-BOUND-KERNEL.json"

EXPECTED_BLOBS = {
    GRF01: "7daa489d182e52401df9300acfe9899759515078",
    GRF05: "75e556dee57dff282232a57898924d7e1826a40c",
}
EXPECTED_CERT_CANONICAL = "ecb750ab063adef5a489f14898e6736d6a850d18bdd04a5616bfc3f671a2aaaf"

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

def mat_vec_mod(m: list[list[int]], z: tuple[int, ...], c: list[int], q: int) -> tuple[int, ...]:
    return tuple(
        (c[i] + sum(m[i][j] * z[j] for j in range(len(z)))) % q
        for i in range(len(m))
    )

def image(m: list[list[int]], c: list[int], q: int) -> set[tuple[int, ...]]:
    n = len(m[0]) if m else 0
    req(q > 1, "modulus must exceed 1")
    req(len(c) == len(m), "offset dimension mismatch")
    req(all(len(row) == n for row in m), "ragged matrix")
    return {
        mat_vec_mod(m, z, c, q)
        for z in itertools.product(range(q), repeat=n)
    }

def is_prime(p: int) -> bool:
    if p < 2:
        return False
    d = 2
    while d * d <= p:
        if p % d == 0:
            return False
        d += 1
    return True

def main() -> None:
    for path, expected in EXPECTED_BLOBS.items():
        req(path.is_file(), f"missing source lock: {path.relative_to(ROOT)}")
        req(blob(path) == expected, f"source-lock drift: {path.relative_to(ROOT)}")

    cert = json.loads(CERT.read_text())
    stored = cert.pop("canonical_sha256_without_this_field", None)
    req(stored == EXPECTED_CERT_CANONICAL, "GRF-06 stored canonical drift")
    req(csha(cert) == EXPECTED_CERT_CANONICAL, "GRF-06 canonical drift")
    req(cert["node"] == "GRF-06", "GRF-06 node drift")
    req("ODD_PRIME_COLUMN_IMAGE_EMPTY" in cert["mathematical_kernel"]["empty_rule"], "empty-rule drift")

    design = GRF01.read_text()
    req("**D. Odd-prime CUT layer.**" in design, "GRF-01 step-D design drift")
    req("source-locked semantic adapter" in design, "GRF-01 adapter firewall drift")

    # Exact local-image regression over q=5.
    m = [[2], [3]]
    c = [1, 0]
    q = 5
    req(is_prime(q), "fixture prime regression")
    im = image(m, c, q)
    req((0, 1) in im, "known SAT residue missing")
    req((0, 0) not in im, "known UNSAT residue unexpectedly reachable")

    # Any exact integer lift must reduce into the finite image.
    for z in range(-20, 21):
        target = ((1 + 2 * z) % q, (3 * z) % q)
        req(target in im, f"integer lift escaped image at z={z}")

    # Prime-power strength is real: modulo p can pass while modulo p^2 fails.
    p = 3
    req(is_prime(p), "prime-power fixture prime regression")
    m2 = [[p * p]]
    c2 = [0]
    target = (p,)
    req((target[0] % p,) in image(m2, c2, p), "mod-p relaxation should pass")
    req(target not in image(m2, c2, p * p), "mod-p^2 obstruction should fail")

    fire = cert["credit_firewall"]
    req(not fire["main_pruning_credit"], "unexpected MAIN pruning credit")
    req(not fire["full178_complete"], "unexpected FULL178 completion")
    req(not fire["merge_authorized"], "unexpected merge authorization")
    own = cert["ownership"]
    req(not own["concrete_row_or_stratum_selected"], "MAIN selected concrete target")
    req(not own["cut_population_replayed"], "MAIN replayed CUT population")

    print(
        "GRF-06 PASS: exact odd-prime affine column-image obstruction retained "
        "with prime-power and semantic-adapter firewalls; no concrete FULL178 target or credit."
    )

if __name__ == "__main__":
    main()
