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
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGES = HERE.parents[1]
EX1 = STAGES / "stage32-ex1"
CERT = EX1 / "ex1-05af-cellular-pullback-smith-certificate.json"
AUDITED_HEAD = "e3c4a04d5010e6dca9428722e334890e2614297a"
COMPACT_REPO_PATH = "stages/stage32-ex1/verify_ex1_05af_s0_integral_ns_pullback_saturation.py"
EXPECTED_CERT_CANONICAL = "988a360ddeb7e22e0aa1923044b8e473d50f10e9dd82d84565266ed292d98984"
EXPECTED_COMPACT_BLOB_SHA1 = "8591e5e25743b32b6768022052ae59746269d17e"


def git_blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def load_compact():
    raw = subprocess.check_output(["git", "show", f"{AUDITED_HEAD}:{COMPACT_REPO_PATH}"])
    assert git_blob_sha1(raw) == EXPECTED_COMPACT_BLOB_SHA1
    with tempfile.NamedTemporaryFile(suffix=".py") as f:
        f.write(raw); f.flush()
        spec = importlib.util.spec_from_file_location("stage32_ex1_compact_audited_mod2", f.name)
        assert spec and spec.loader
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
        return mod


def load_ll():
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    x = dict(cert); claimed = x.pop("canonical_sha256_without_this_field")
    assert claimed == EXPECTED_CERT_CANONICAL
    raw = json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
    assert hashlib.sha256(raw).hexdigest() == claimed
    p = cert["matrix_payload"]
    decoded = zlib.decompress(base64.b85decode(p["encoded"].encode()))
    assert hashlib.sha256(decoded).hexdigest() == p["uncompressed_sha256"]
    return json.loads(decoded.decode())["Lleft"]


def main():
    compact = load_compact()
    LL = load_ll()

    # Actual Smith coordinate 0 is the 26th saturation coordinate modulo 2.
    coeff = [LL[25][j] % 2 for j in range(102)]
    support = [j for j, a in enumerate(coeff) if a]
    assert coeff[0] == 0 and coeff[101] == 0
    assert support == [1 + 10 * 4 + 4]

    ji_formulas = []
    source_F_columns = set()
    for ji, JI in enumerate(compact.JINVS):
        col = [JI[k][4] % 2 for k in range(10)]
        nz = [k for k, a in enumerate(col) if a]
        assert len(nz) == 1
        k = nz[0]
        source_F_columns.add(k)
        ji_formulas.append({
            "ji_index": ji,
            "B44_mod2_equals": f"F[4,{k}] mod 2",
            "source_F_column": k,
        })

    total_F = 0
    unique_F_mod2 = set()
    row4_counts = Counter()
    fixed_entry_values = [[set() for _ in range(10)] for _ in range(10)]
    tracked_counts = {k: Counter() for k in sorted(source_F_columns)}

    for r in compact.RES3:
        opts = [compact.gopts(n, "i" if j == compact.SELECTED[r] else "id") for j, n in enumerate(compact.NORMS)]
        for t in compact.lifts[r]:
            for gp in itertools.product(*opts):
                F, ok = compact.build(t, gp)
                assert ok
                total_F += 1
                fm = tuple(tuple(v % 2 for v in row) for row in F)
                unique_F_mod2.add(fm)
                row4 = fm[4]
                row4_counts[row4] += 1
                for a in range(10):
                    for b in range(10):
                        fixed_entry_values[a][b].add(fm[a][b])
                for k in tracked_counts:
                    tracked_counts[k][row4[k]] += 1

    assert total_F == 6144
    for k in source_F_columns:
        assert tracked_counts[k] == Counter({1: 6144})

    fixed_ones = []
    fixed_zeros = []
    variable = []
    for a in range(10):
        for b in range(10):
            vals = sorted(fixed_entry_values[a][b])
            if vals == [1]: fixed_ones.append([a,b])
            elif vals == [0]: fixed_zeros.append([a,b])
            else: variable.append([a,b])

    out = {
        "schema": "STAGE32_32_01_178_SMITH_MOD2_OBSERVABLE_PREFLIGHT_V1",
        "source": {
            "arsenal_weapon": "S32-PW10",
            "source_pr": 1728,
            "hostile_review": 5147627146,
            "audited_exact_head": AUDITED_HEAD,
            "compact_builder_blob_sha1": EXPECTED_COMPACT_BLOB_SHA1,
            "smith_certificate_canonical": EXPECTED_CERT_CANONICAL,
        },
        "smith_coordinate_0": {
            "formula_in_assembly_coordinates": "B[4,4] mod 2",
            "endpoint_coefficients": [0,0],
            "ji_formulas": ji_formulas,
            "required_F_entries": [[4,k] for k in sorted(source_F_columns)],
        },
        "old_legal_F_replay": {
            "F_count": total_F,
            "unique_F_mod2_count": len(unique_F_mod2),
            "unique_row4_mod2_count": len(row4_counts),
            "row4_mod2_distribution": [[list(k),v] for k,v in sorted(row4_counts.items())],
            "tracked_entry_distributions": {f"F[4,{k}]": dict(v) for k,v in tracked_counts.items()},
            "fixed_one_entry_count": len(fixed_ones),
            "fixed_one_entries": fixed_ones,
            "fixed_zero_entry_count": len(fixed_zeros),
            "variable_entry_count": len(variable),
        },
        "interpretation": {
            "old_v6_obstruction_detected_by_one_bit": True,
            "one_bit": "B[4,4] mod 2 = 1",
            "equivalently_on_old_legal_assemblies": "F[4,9]=1 mod2 for JI0/JI1 and F[4,0]=1 mod2 for JI2/JI3",
            "current_full178_semantic_adapter_established": False,
            "required_next_bridge": "Identify a current FULL178 carrier/correspondence H1 action F in the same audited cellular basis, or prove an invariant replacement for this one-bit condition.",
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
