#!/usr/bin/env python3
from __future__ import annotations

import base64
import contextlib
import hashlib
import importlib.util
import io
import itertools
import json
import subprocess
import tempfile
import zlib
from collections import Counter
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGES = HERE.parents[1]
EX1 = STAGES / "stage32-ex1"
CERT = EX1 / "ex1-05af-cellular-pullback-smith-certificate.json"

AUDITED_HEAD = "e3c4a04d5010e6dca9428722e334890e2614297a"
COMPACT_REPO_PATH = "stages/stage32-ex1/verify_ex1_05af_s0_integral_ns_pullback_saturation.py"
EXPECTED_CERT_CANONICAL = "988a360ddeb7e22e0aa1923044b8e473d50f10e9dd82d84565266ed292d98984"
EXPECTED_COMPACT_BLOB_SHA1 = "8591e5e25743b32b6768022052ae59746269d17e"
MODS = [2, 2, 2, 4, 4]


def canonical_without_field(obj: dict) -> str:
    x = dict(obj)
    claimed = x.pop("canonical_sha256_without_this_field")
    raw = json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
    assert hashlib.sha256(raw).hexdigest() == claimed
    return claimed


def decode_payload(cert: dict) -> dict:
    p = cert["matrix_payload"]
    raw = zlib.decompress(base64.b85decode(p["encoded"].encode()))
    assert len(raw) == p["uncompressed_bytes"]
    assert hashlib.sha256(raw).hexdigest() == p["uncompressed_sha256"]
    return json.loads(raw.decode())


def git_blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def load_compact():
    raw = subprocess.check_output(["git", "show", f"{AUDITED_HEAD}:{COMPACT_REPO_PATH}"])
    assert git_blob_sha1(raw) == EXPECTED_COMPACT_BLOB_SHA1
    with tempfile.NamedTemporaryFile(suffix=".py") as f:
        f.write(raw)
        f.flush()
        spec = importlib.util.spec_from_file_location("stage32_ex1_compact_audited", f.name)
        assert spec and spec.loader
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
        return mod


def mv(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def element_order(x):
    order = 1
    for a, m in zip(x, MODS):
        if a:
            o = m // gcd(a, m)
            order = order * o // gcd(order, o)
    return order


def main():
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    assert canonical_without_field(cert) == EXPECTED_CERT_CANONICAL
    payload = decode_payload(cert)
    LS, LL = payload["Lsat"], payload["Lleft"]
    compact = load_compact()
    assert compact.MODS == MODS

    per_coordinate_nonzero = [0] * 5
    class_counts = Counter()
    order_counts = Counter()
    by_ji = [Counter() for _ in range(4)]
    total = 0

    for r in compact.RES3:
        opts = [
            compact.gopts(n, "i" if j == compact.SELECTED[r] else "id")
            for j, n in enumerate(compact.NORMS)
        ]
        assert [len(x) for x in opts] == [2, 4, 2]
        for t in compact.lifts[r]:
            for gp in itertools.product(*opts):
                F, ok = compact.build(t, gp)
                assert ok
                for ji, JI in enumerate(compact.JINVS):
                    B = compact.mm(F, JI)
                    k = [81] + [B[a][b] for a in range(10) for b in range(10)] + [105]
                    c = mv(LL, k)
                    assert mv(LS, c) == k
                    actual = tuple(c[25 + i] % MODS[i] for i in range(5))
                    assert any(actual)
                    assert element_order(actual) == 2
                    total += 1
                    class_counts[actual] += 1
                    by_ji[ji][actual] += 1
                    order_counts[2] += 1
                    for i, a in enumerate(actual):
                        if a:
                            per_coordinate_nonzero[i] += 1

    assert total == 24576

    detector_subsets = []
    minimal_size = None
    for size in range(1, 6):
        for subset in itertools.combinations(range(5), size):
            misses = sum(n for cls, n in class_counts.items() if not any(cls[i] for i in subset))
            if misses == 0:
                detector_subsets.append(list(subset))
                if minimal_size is None:
                    minimal_size = size
        if minimal_size is not None:
            break

    out = {
        "schema": "STAGE32_32_01_178_SMITH_MINIMAL_DETECTOR_PREFLIGHT_V1",
        "source": {
            "arsenal_weapon": "S32-PW10",
            "source_pr": 1728,
            "hostile_review": 5147627146,
            "audited_exact_head": AUDITED_HEAD,
            "smith_certificate_canonical": EXPECTED_CERT_CANONICAL,
            "compact_assembly_builder_path": COMPACT_REPO_PATH,
            "compact_assembly_builder_blob_sha1": EXPECTED_COMPACT_BLOB_SHA1,
            "compact_builder_loaded_by": "git show from audited exact head",
        },
        "exact_replay": {
            "classes_checked": total,
            "distinct_actual_smith_classes": len(class_counts),
            "actual_class_distribution": [[list(k), v] for k, v in sorted(class_counts.items())],
            "order_distribution": dict(order_counts),
            "per_coordinate_nonzero_counts": per_coordinate_nonzero,
            "minimal_detector_coordinate_count": minimal_size,
            "minimal_detector_coordinate_subsets": detector_subsets,
            "per_ji_distinct_classes": [len(x) for x in by_ji],
        },
        "interpretation": {
            "purpose": "Find the smallest certified Smith-coordinate observable sufficient to detect every old legal V6 assembly, so a future current-FULL178 adapter need not reconstruct all five cokernel coordinates if a smaller observable suffices.",
            "current_full178_bridge_established": False,
            "old_v6_uniformity_is_not_current_full178_uniformity": True,
        },
        "credit": {
            "main_pruning_credit": False,
            "full178_completion": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_claim": False,
        },
    }
    raw = json.dumps(out, sort_keys=True, separators=(",", ":")).encode()
    out["canonical_sha256_without_this_field"] = hashlib.sha256(raw).hexdigest()
    print(json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
