#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import json
import zlib
from collections import Counter
from itertools import product
from math import gcd
from pathlib import Path

import verify_ex1_05af_s0_integral_ns_pullback_saturation as compact

HERE = Path(__file__).resolve().parent
CERT = HERE / "ex1-05af-cellular-pullback-smith-certificate.json"


def mv(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def decode_payload(cert):
    p = cert["matrix_payload"]
    raw = zlib.decompress(base64.b85decode(p["encoded"].encode()))
    assert len(raw) == p["uncompressed_bytes"]
    assert hashlib.sha256(raw).hexdigest() == p["uncompressed_sha256"]
    return json.loads(raw.decode())


def element_order(x, mods):
    order = 1
    for a, m in zip(x, mods):
        if a:
            o = m // gcd(a, m)
            order = order * o // gcd(order, o)
    return order


cert = json.loads(CERT.read_text(encoding="utf-8"))
claimed = cert.pop("canonical_sha256_without_this_field")
raw = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
assert hashlib.sha256(raw).hexdigest() == claimed
cert["canonical_sha256_without_this_field"] = claimed

payload = decode_payload(cert)
LS = payload["Lsat"]
LL = payload["Lleft"]
ds = cert["smith"]["invariant_factors"]
mods = ds[-5:]

assert ds == [1] * 25 + [2, 2, 2, 4, 4]
assert mods == compact.MODS
assert len(LS) == 102 and len(LS[0]) == 30
assert len(LL) == 30 and len(LL[0]) == 102

# Independently certified primitive saturation coordinates are c=Lleft*k.
# Lleft*Lsat=I.  An assembly Kunneth vector k is first checked to lie in the
# certified saturation lattice by Lsat*c=k.  Since the actual pullback image is
# Lsat*diag(ds)*Z^30, its actual cokernel class is c_i mod ds_i.  Only the last
# five coordinates are nontrivial.
for i in range(30):
    e = [0] * 30
    e[i] = 1
    assert mv(LL, [LS[r][i] for r in range(102)]) == e

actual_counts = [Counter() for _ in range(4)]
actual_orders = [Counter() for _ in range(4)]
by_residue = [Counter() for _ in range(4)]
legacy_disagreement = [Counter() for _ in range(4)]
total_assemblies = 0
checked_classes = 0
zero_actual_classes = 0

for r in compact.RES3:
    opts = [
        compact.gopts(n, "i" if j == compact.SELECTED[r] else "id")
        for j, n in enumerate(compact.NORMS)
    ]
    assert [len(x) for x in opts] == [2, 4, 2]
    gaussian_choices = list(product(*opts))
    assert len(gaussian_choices) == 16

    for t in compact.lifts[r]:
        for gp in gaussian_choices:
            F, ok = compact.build(t, gp)
            assert ok
            total_assemblies += 1
            for j, JI in enumerate(compact.JINVS):
                B = compact.mm(F, JI)
                k = [81] + [B[a][b] for a in range(10) for b in range(10)] + [105]
                assert len(k) == 102

                c = mv(LL, k)
                assert mv(LS, c) == k, (r, j, "assembly_not_in_certified_saturation")
                actual = tuple(c[25 + i] % mods[i] for i in range(5))
                order = element_order(actual, mods)

                # Load-bearing test: use only the actual independently certified
                # cellular Smith cokernel coordinates.  The historical compact
                # OBS/PIVROWS coordinates are retained below only as diagnostic
                # provenance and are not required to agree coordinatewise.
                if not any(actual):
                    zero_actual_classes += 1
                assert any(actual), (r, j, "zero_actual_cellular_cokernel_class")
                assert order == 2, (r, j, actual, order)

                legacy, _legacy_order = compact.obstruction(F, JI)
                if actual != legacy:
                    legacy_disagreement[j][(actual, legacy)] += 1

                actual_counts[j][actual] += 1
                actual_orders[j][order] += 1
                by_residue[j][(r, actual)] += 1
                checked_classes += 1

assert total_assemblies == 6144
assert checked_classes == 6144 * 4
assert zero_actual_classes == 0
for j in range(4):
    assert sum(actual_counts[j].values()) == 6144
    assert dict(actual_orders[j]) == {2: 6144}
    for r in compact.RES3:
        assert sum(n for (rr, _actual), n in by_residue[j].items() if rr == r) == 2048

print("PASS_EX1_05AF_ACTUAL_CELLULAR_COKERNEL_ALL_6144_NONZERO")
print("certified_smith_tail", mods, "index", cert["smith"]["index"])
print("assemblies", total_assemblies, "actual_cokernel_classes_checked", checked_classes)
print("zero_actual_classes", zero_actual_classes)
for j in range(4):
    print("JI", j, "actual_distribution", dict(actual_counts[j]))
    print("JI", j, "actual_orders", dict(actual_orders[j]))
    print("JI", j, "legacy_coordinate_disagreement_pairs", len(legacy_disagreement[j]))
