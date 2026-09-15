#!/usr/bin/env python3
"""Fail-closed exact Picard/2 descent check; stdout is deliberately bounded."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-E2-PICARD-DESCENT-PARITY-CERTIFICATE.json"
PASS = "PASS STAGE32_MB104_000707_E2_PICARD_DESCENT_PARITY_V1"

LOCKS = {
    "PICARD_BASE_RETAINED": ("stages/stage33/33-07/picard_base_rows_retained.py", "82e4d450a1d852e34f6615440fb88a029c6e54eb"),
    "PICARD_MARKING_RETAINED": ("stages/stage33/33-07/stage32_picard_marking_retained.py", "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7"),
    "INTEGRAL_ADAPTER": ("stages/stage32/residual-32-01-production/hperp_integral_adapter.py", "fb1eb380ca786e42a6b00c5ef454b0e79fdba771"),
    "DIRECT_BRIDGE": ("stages/stage32/residual-32-01-production/direct_picard_slice_bridge.py", "be48bd94304d0217727c5c3368761d347cb22eaa"),
    "NODE_MODEL": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_balanced16_two_quartic_gluing.py", "20b49289677b5f7b6f5370107b286ac977fe6a11"),
    "ORBIT_CERT": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-NODE-ORBIT-TABLE-CERTIFICATE.json", "02c5c5b52ed18cc2850a01bab05c6dfac85a59f9"),
    "SATURATION_CERT": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-BOUNDARY-FIBER-SATURATION-CERTIFICATE.json", "fcdfeaddbe0da190c2210ad271d26f611956f32a"),
    "PASSPORT_CERT": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-ETALE-BASECHANGE-DETERMINANT-PASSPORT-CERTIFICATE.json", "034885449c9726e9ef81bc1ef090956d89ce2fd7"),
}


def req(ok, msg):
    if not ok:
        raise SystemExit("FAIL: " + msg)


def root():
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root")


def blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def raw_sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"module spec {name}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def rref_bits(rows, width, companions=None):
    a = [sum((int(v) & 1) << j for j, v in enumerate(row)) for row in rows]
    c = list(companions) if companions is not None else [0] * len(a)
    pivots, rank = [], 0
    for col in range(width):
        pivot = next((i for i in range(rank, len(a)) if (a[i] >> col) & 1), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        c[rank], c[pivot] = c[pivot], c[rank]
        for i in range(len(a)):
            if i != rank and ((a[i] >> col) & 1):
                a[i] ^= a[rank]
                c[i] ^= c[rank]
        pivots.append(col)
        rank += 1
    return a[:rank], c[:rank], pivots


def nullspace(rows, width):
    rr, _, pivots = rref_bits(rows, width)
    out = []
    for free in (j for j in range(width) if j not in pivots):
        v = 1 << free
        for i in range(len(pivots) - 1, -1, -1):
            if (rr[i] & v).bit_count() & 1:
                v |= 1 << pivots[i]
        out.append([(v >> j) & 1 for j in range(width)])
    return out


def dot(a, b):
    return sum(int(x) * int(y) for x, y in zip(a, b)) & 1


def main():
    rr = root()
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared == LOCKS, "certificate/source-lock table mismatch")
    for key, (rel, expected) in LOCKS.items():
        p = rr / rel
        req(p.is_file(), f"SOURCE_LOCK_FAIL missing {key}")
        req(blob_sha1(p) == expected, f"SOURCE_LOCK_FAIL {key}")

    retained_base = load_module(rr / LOCKS["PICARD_BASE_RETAINED"][0], "mb104_picard_base").load()
    retained_marking = load_module(rr / LOCKS["PICARD_MARKING_RETAINED"][0], "mb104_picard_marking").load()
    residual = rr / "stages/stage32/residual-32-01-production"
    sys.path.insert(0, str(residual))
    from hperp_integral_adapter import HperpIntegralPairingAdapter
    from direct_picard_slice_bridge import DirectPicardSliceBridge

    adapter = HperpIntegralPairingAdapter.from_retained(retained_marking, retained_base)
    bridge = DirectPicardSliceBridge.from_retained(retained_marking, retained_base)
    coords = adapter.class_coordinates_in_retained_basis
    node_model = load_module(rr / LOCKS["NODE_MODEL"][0], "mb104_node_model")
    absent_nodes = [i for i, point in enumerate(node_model.V) if point[5] == 0]
    orbit = json.loads((rr / LOCKS["ORBIT_CERT"][0]).read_text())
    support_nodes = orbit["exact_residual_orbits"]["support_nodes"]
    req(absent_nodes == list(range(16, 24)) + list(range(40, 48)), "absent-node derivation")
    req(support_nodes == [0,1,2,3,8,9,10,11,24,25,26,32,33,34], "support-node lock")

    # all140 labels 93..140 are E_0..E_47; coordinates are integral in the
    # saturated retained Picard basis, so reduction here is exact in Pic/2Pic.
    absent = [[int(coords[92+i, j]) & 1 for j in range(64)] for i in absent_nodes]
    support = [[int(coords[92+i, j]) & 1 for j in range(64)] for i in support_nodes]
    hyperplane = [int(v) & 1 for v in bridge.hyperplane_coordinates]
    absent_rr, _, _ = rref_bits(absent, 64)
    annihilator = nullspace(absent, 64)
    raw, dual_bits = [], []
    for w in annihilator:
        raw.append([dot(w, hyperplane)] + [dot(w, e) for e in support])
        dual_bits.append(sum((v & 1) << j for j, v in enumerate(w)))
    eq_bits, witnesses, pivots = rref_bits(raw, 15, dual_bits)
    equations = [[(bits >> j) & 1 for j in range(15)] for bits in eq_bits]

    # Two saturation relations from the exact residual orbit table and two
    # determinant-passport relations; column zero is l.
    existing = [
        [0] + [int(i in {0,1,2,3,24,25,26}) for i in support_nodes],
        [0] + [int(i in {8,9,10,11,32,33,34}) for i in support_nodes],
        [0] + [int(i in {0,1,2,3}) for i in support_nodes],
        [0] + [int(i in {8,9,10,11}) for i in support_nodes],
    ]
    existing_rr, _, _ = rref_bits(existing, 15)
    combined_rr, _, _ = rref_bits(existing + equations, 15)

    expected_equations = [[0] + [int(k == j) for k in range(14)] for j in range(14)]
    req(equations == expected_equations and pivots == list(range(1, 15)), "canonical equations")
    req(all(row[0] == 0 for row in raw), "H must vanish in quotient")
    for j, bits in enumerate(witnesses):
        w = [(bits >> k) & 1 for k in range(64)]
        req(all(dot(w, a) == 0 for a in absent), f"witness {j} absent annihilation")
        req(dot(w, hyperplane) == 0, f"witness {j} H annihilation")
        req([dot(w, e) for e in support] == [int(k == j) for k in range(14)], f"witness {j} delta pairing")

    result = {
        "picard_mod2_dimension": 64,
        "absent_span_rank": len(absent_rr),
        "quotient_dimension": 64-len(absent_rr),
        "membership_equation_rank": len(equations),
        "equation_rows_l_then_support": equations,
        "obstruction_witness_hex": [f"{w:016x}" for w in witnesses],
        "existing_parity_rank": len(existing_rr),
        "combined_rank": len(combined_rr),
        "new_independent_rank": len(combined_rr)-len(existing_rr),
        "remaining_affine_dimension": 14-len(equations),
        "remaining_parity_classes": 1 << (14-len(equations)),
        "e2_closed": False,
    }
    req(result == cert["exact_result"], "certificate exact-result mismatch")
    hashes = cert["retained_hashes"]
    req(raw_sha256(rr / LOCKS["PICARD_BASE_RETAINED"][0]) == hashes["picard_base_raw_sha256"], "base raw sha256")
    req(raw_sha256(rr / LOCKS["PICARD_MARKING_RETAINED"][0]) == hashes["marking_raw_sha256"], "marking raw sha256")
    req(retained_base["canonical_sha256"] == hashes["picard_base_canonical_sha256"], "base canonical hash")
    req(retained_marking["canonical_sha256"] == hashes["marking_canonical_sha256"], "marking canonical hash")
    req(adapter.certificate["canonical_sha256_without_this_field"] == hashes["adapter_canonical_sha256"], "adapter hash")
    req(bridge.certificate["canonical_sha256_without_this_field"] == hashes["bridge_canonical_sha256"], "bridge hash")
    req(cert["stdout_policy"]["raw_picard64_payload_printed"] is False, "stdout firewall")
    req(all(cert["credit_firewall"][k] is False for k in cert["credit_firewall"]), "credit firewall")
    print(PASS)
    print("pic2_dim=64 absent_rank=15 quotient_dim=49 equations=14 existing_rank=4 new_rank=10 affine_dim=0 parity_classes=1 e2_closed=false")


if __name__ == "__main__":
    main()
