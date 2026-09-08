#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import json
import zlib
from collections import Counter
from itertools import product
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

# The independently certified primitive saturation coordinates are c=Lleft*k.
# Because Lleft*Lsat=I, a Kunneth vector k lies in the saturation lattice iff
# Lsat*c=k.  The actual pullback image is Lsat*diag(ds)*Z^30, so its cokernel
# class is exactly c_i mod ds_i; only coordinates 25..29 are nontrivial.
for i in range(30):
    e = [0] * 30
    e[i] = 1
    assert mv(LL, [LS[r][i] for r in range(102)]) == e

counts = [Counter() for _ in range(4)]
by_residue = [Counter() for _ in range(4)]
total_assemblies = 0
checked_classes = 0

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

                # This is the missing load-bearing identity: the former compact
                # OBS/PIVROWS coordinates agree assembly-by-assembly with the
                # actual independently certified cellular Smith cokernel class.
                compact_ob, compact_order = compact.obstruction(F, JI)
                assert actual == compact_ob, (r, j, actual, compact_ob)
                assert compact_order == 2
                assert any(actual)
                assert all((2 * actual[i]) % mods[i] == 0 for i in range(5))

                counts[j][actual] += 1
                by_residue[j][(r, actual)] += 1
                checked_classes += 1

assert total_assemblies == 6144
assert checked_classes == 6144 * 4
expected = {(1, 1, 1, 2, 0): 3072, (1, 1, 1, 0, 2): 3072}
for j in range(4):
    assert dict(counts[j]) == expected
    for r in compact.RES3:
        assert by_residue[j][(r, (1, 1, 1, 2, 0))] == 1024
        assert by_residue[j][(r, (1, 1, 1, 0, 2))] == 1024

print("PASS_EX1_05AF_CELLULAR_SMITH_TO_6144_OBSTRUCTION_BRIDGE")
print("certified_smith_tail", mods, "index", cert["smith"]["index"])
print("assemblies", total_assemblies, "actual_cokernel_classes_checked", checked_classes)
print("compact_coordinates_equal_actual_cellular_cokernel_coordinates", True)
