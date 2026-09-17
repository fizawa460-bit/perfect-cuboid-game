#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CERT = HERE / "GRF-07-COPRIME-CRT-LOCAL-SYSTEM-COMPOSITION-KERNEL.json"
GRF01 = HERE / "GRF-01-DESIGN.md"
GRF03 = HERE / "GRF-03-NORM-LADDER-RESIDUE-COLLAPSE.json"
GRF06 = HERE / "GRF-06-ODD-PRIME-AFFINE-COLUMN-IMAGE-KERNEL.json"

EXPECTED_BLOBS = {
    GRF01: "7daa489d182e52401df9300acfe9899759515078",
    GRF03: "d6777200cadb6809dc3b46374c8f714cb6ebd6cd",
    GRF06: "fec2271a241c76750d904fb08de48aa068339218",
}
EXPECTED_CERT_CANONICAL = "b799bbd899f3953d9b98191609f6f989f47780738bd1579eb146b2b9083b4beb"

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

def pairwise_coprime(moduli: list[int]) -> bool:
    return all(math.gcd(moduli[i], moduli[j]) == 1
               for i in range(len(moduli)) for j in range(i))

def crt_scalar(residues: tuple[int, ...], moduli: list[int]) -> int:
    req(len(residues) == len(moduli), "CRT arity mismatch")
    req(pairwise_coprime(moduli), "CRT requires pairwise-coprime moduli")
    q = math.prod(moduli)
    out = 0
    for a, m in zip(residues, moduli):
        qi = q // m
        inv = pow(qi, -1, m)
        out = (out + (a % m) * qi * inv) % q
    return out

def crt_vector(local_vectors: tuple[tuple[int, ...], ...], moduli: list[int]) -> tuple[int, ...]:
    req(local_vectors, "need at least one local vector")
    n = len(local_vectors[0])
    req(all(len(v) == n for v in local_vectors), "CRT vector dimension mismatch")
    return tuple(
        crt_scalar(tuple(v[j] for v in local_vectors), moduli)
        for j in range(n)
    )

def reduce_vector(v: tuple[int, ...], q: int) -> tuple[int, ...]:
    return tuple(x % q for x in v)

def main() -> None:
    for path, expected in EXPECTED_BLOBS.items():
        req(path.is_file(), f"missing source lock: {path.relative_to(ROOT)}")
        req(blob(path) == expected, f"source-lock drift: {path.relative_to(ROOT)}")

    cert = json.loads(CERT.read_text())
    stored = cert.pop("canonical_sha256_without_this_field", None)
    req(stored == EXPECTED_CERT_CANONICAL, "GRF-07 stored canonical drift")
    req(csha(cert) == EXPECTED_CERT_CANONICAL, "GRF-07 canonical drift")
    req(cert["node"] == "GRF-07", "GRF-07 node drift")
    req("probabilistic independence" in cert["mathematical_kernel"]["scope"], "independence firewall drift")

    design = GRF01.read_text()
    req("Keep odd primes separate from the 2-adic core unless CRT combination materially simplifies" in design,
        "GRF-01 CRT routing drift")

    # Three pairwise-coprime local systems on the same two integer variables.
    moduli = [8, 3, 5]
    req(pairwise_coprime(moduli), "fixture moduli are not pairwise coprime")
    q = math.prod(moduli)

    def local_set(m: int) -> set[tuple[int, int]]:
        return {
            (x, y)
            for x, y in itertools.product(range(m), repeat=2)
            if (2 * x + y - 1) % m == 0
        }

    locals_ = [local_set(m) for m in moduli]
    req(all(locals_), "fixture local set unexpectedly empty")
    global_by_crt = {
        crt_vector(combo, moduli)
        for combo in itertools.product(*locals_)
    }
    global_direct = {
        (x, y)
        for x, y in itertools.product(range(q), repeat=2)
        if (2 * x + y - 1) % q == 0
    }
    req(global_by_crt == global_direct, "CRT admissible-product regression")
    req(len(global_direct) == math.prod(len(s) for s in locals_), "CRT cardinality-product regression")

    # Every reconstructed class reduces back to the chosen local classes.
    for combo in itertools.islice(itertools.product(*locals_), 0, 100):
        v = crt_vector(combo, moduli)
        for local_v, m in zip(combo, moduli):
            req(reduce_vector(v, m) == local_v, "CRT roundtrip regression")

    # One empty local necessary-condition set forces global emptiness.
    empty_locals = [locals_[0], set(), locals_[2]]
    req(math.prod(len(s) for s in empty_locals) == 0, "empty local product regression")
    reconstructed = {
        crt_vector(combo, moduli)
        for combo in itertools.product(*empty_locals)
    }
    req(not reconstructed, "empty local system did not force empty global set")

    # Noncoprime moduli must fail closed.
    req(not pairwise_coprime([4, 6]), "noncoprime fixture regression")
    try:
        crt_scalar((1, 1), [4, 6])
    except RuntimeError:
        pass
    else:
        raise RuntimeError("noncoprime CRT did not fail closed")

    fire = cert["credit_firewall"]
    req(not fire["multiply_local_savings"], "local savings were multiplied")
    req(not fire["assume_statistical_independence"], "statistical independence was assumed")
    req(not fire["main_pruning_credit"], "unexpected MAIN pruning credit")
    req(not fire["merge_authorized"], "unexpected merge authorization")

    print(
        "GRF-07 PASS: exact coprime-modulus CRT composition retained for one common "
        "source-locked variable system; no independence, concrete population, or credit."
    )

if __name__ == "__main__":
    main()
