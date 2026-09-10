#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import json
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGES = HERE.parents[1]
CERT = STAGES / "stage32-ex1" / "ex1-05af-cellular-pullback-smith-certificate.json"

EXPECTED_CERT_CANONICAL = "988a360ddeb7e22e0aa1923044b8e473d50f10e9dd82d84565266ed292d98984"
EXPECTED_SMITH = [1] * 25 + [2, 2, 2, 4, 4]
MODS = [2, 2, 2, 4, 4]


def canonical_without_field(obj: dict) -> str:
    x = dict(obj)
    claimed = x.pop("canonical_sha256_without_this_field")
    raw = json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
    got = hashlib.sha256(raw).hexdigest()
    assert got == claimed
    return claimed


def decode_payload(cert: dict) -> dict:
    p = cert["matrix_payload"]
    raw = zlib.decompress(base64.b85decode(p["encoded"].encode()))
    assert len(raw) == p["uncompressed_bytes"]
    assert hashlib.sha256(raw).hexdigest() == p["uncompressed_sha256"]
    return json.loads(raw.decode())


def add_group(x, y):
    return tuple((a + b) % m for a, b, m in zip(x, y, MODS))


def cyclic_multiples(g):
    out = {(0, 0, 0, 0, 0)}
    cur = (0, 0, 0, 0, 0)
    while True:
        cur = add_group(cur, g)
        if cur in out:
            return out
        out.add(cur)


def subgroup_generated(gens):
    H = {(0, 0, 0, 0, 0)}
    for g in gens:
        cyc = cyclic_multiples(g)
        H = {add_group(h, c) for h in H for c in cyc}
    return H


def coord_generator(LL, j):
    return tuple(LL[25 + i][j] % MODS[i] for i in range(5))


def additive_row_col(C, m):
    # C[a][b] = u[a] + v[b] mod m iff all mixed second differences vanish.
    c00 = C[0][0] % m
    for a in range(10):
        for b in range(10):
            if (C[a][b] - C[a][0] - C[0][b] + c00) % m:
                return False
    return True


def main():
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    claimed = canonical_without_field(cert)
    assert claimed == EXPECTED_CERT_CANONICAL
    assert cert["smith"]["invariant_factors"] == EXPECTED_SMITH
    payload = decode_payload(cert)
    LL = payload["Lleft"]
    assert len(LL) == 30 and all(len(row) == 102 for row in LL)

    endpoint_gens = [coord_generator(LL, 0), coord_generator(LL, 101)]
    middle_gens = [coord_generator(LL, j) for j in range(1, 101)]
    all_gens = endpoint_gens + middle_gens

    endpoint_image = subgroup_generated(endpoint_gens)
    middle_image = subgroup_generated(middle_gens)
    total_image = subgroup_generated(all_gens)

    rows = []
    for i, mod in enumerate(MODS):
        coeff = [LL[25 + i][j] % mod for j in range(102)]
        B = [[coeff[1 + 10 * a + b] for b in range(10)] for a in range(10)]
        nz = [(a, b, B[a][b]) for a in range(10) for b in range(10) if B[a][b] % mod]
        rows.append({
            "smith_coordinate": i,
            "modulus": mod,
            "endpoint_coefficients": [coeff[0], coeff[101]],
            "middle_nonzero_count": len(nz),
            "middle_support": nz,
            "middle_coefficient_values": sorted({v for _, _, v in nz}),
            "middle_matrix_additive_row_plus_column": additive_row_col(B, mod),
            "middle_matrix_constant": len({B[a][b] % mod for a in range(10) for b in range(10)}) == 1,
        })

    out = {
        "schema": "STAGE32_32_01_178_SMITH_PROJECTION_PREFLIGHT_V1",
        "source": {
            "arsenal_weapon": "S32-PW10",
            "source_pr": 1728,
            "hostile_review": 5147627146,
            "audited_exact_head": "e3c4a04d5010e6dca9428722e334890e2614297a",
            "cellular_pullback_certificate_canonical": claimed,
        },
        "map": {
            "assembly_vector_shape": 102,
            "semantic_shape": "[n1] + vec(B_10x10) + [n2]",
            "smith_moduli": MODS,
            "cokernel_order": 128,
            "endpoint_only_image_order": len(endpoint_image),
            "middle_B_only_image_order": len(middle_image),
            "full_linear_image_order": len(total_image),
            "middle_B_alone_surjects_to_full_cokernel": len(middle_image) == 128,
            "endpoint_data_alone_determine_class": all(not any(g) for g in middle_gens),
        },
        "coordinate_rows": rows,
        "current_full178_adapter_status": {
            "exact_current_terminal_to_102d_assembly_adapter_found": False,
            "exact_current_terminal_to_5d_smith_adapter_found": False,
            "coarse_g_d_e_sufficient": False,
            "reason": "The audited source class depends on the H1xH1 correspondence block B. This preflight only determines how the certified Smith map sees that block; it does not identify a current FULL178 carrier with a source-compatible B.",
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
