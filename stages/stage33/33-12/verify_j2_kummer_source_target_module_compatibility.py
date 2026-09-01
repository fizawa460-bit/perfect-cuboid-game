#!/usr/bin/env python3
"""Verify the compact J2 source-target compatibility audit and gauge conventions."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
CERT = HERE / "j2-kummer-source-target-module-compatibility-audit.json"
CERTIFIER = HERE / "certify_j2_kummer_source_target_module_compatibility.py"
PIC = S33 / "33-07" / "retained-picard-base-sparse.json"
PROPER = S33 / "33-07" / "proper-brauer2-from-discriminant.json"
TARGET = HERE / "full-surface-pic2-kummer-target.json"

PIC_SHA = "e41df3f84760b941440035a388baac88602126c80140139ddf9c187bedf0bb49"
PROPER_SHA = "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"
TARGET_SHA = "384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890"
NP = 64
NB = 14


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj


def xor(a: list[int], b: list[int]) -> list[int]:
    return [x ^ y for x, y in zip(a, b)]


def rowmul(v: list[int], m: list[list[int]]) -> list[int]:
    return [sum(v[i] * m[i][j] for i in range(len(v))) & 1 for j in range(len(m[0]))]


def expand_sparse(obj: dict) -> list[list[int]]:
    out = []
    for row in obj["matrix_64x64_sparse_rows_1based"]:
        dense = [0] * NP
        for column, value in row:
            dense[column - 1] = int(value) & 1
        out.append(dense)
    assert len(out) == NP
    return out


cert = json.loads(CERT.read_text(encoding="utf-8"))
body = dict(cert)
claimed = body.pop("canonical_sha256")
assert claimed == csha(body)
assert cert["status"] == "FAIL_EXACT_LOCKED_J2_SOURCE_TARGET_MODULE_COMPATIBILITY"
assert cert["locked_named_j2"]["locked_75D_target_reachable_from_locked_source"] is False
assert cert["consequence"]["named_source_target_relation_rank_credit_after_this_audit"] == 0
assert cert["consequence"]["old_relation_may_be_used_as_kummer_matrix_relation"] is False
assert cert["diagnostic"]["sources_for_which_locked_target_is_not_reachable"] == 23
assert 6 in cert["diagnostic"]["incompatible_source_masks_decimal"]

# Recompute the whole all-extension audit through the independent certifier and
# require byte-for-byte semantic equality, apart from formatting.
spec = importlib.util.spec_from_file_location("compat_certifier", CERTIFIER)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)
recomputed = module.recompute()
assert recomputed == cert

# Independent row-action gauge sanity.  For every elementary section change
# Psi=e_{a,p}, the induced split-extension blocks
#   Phi_g = Psi P_g + B_g Psi
# must satisfy the V4 block relations.  On every retained invariant source,
# its defect must equal the Picard coboundary w(P_g-I), hence project to zero.
pic = locked(PIC, PIC_SHA)
proper = locked(PROPER, PROPER_SHA)
target = locked(TARGET, TARGET_SHA)
Pc = expand_sparse(pic["objects"]["cc"])
Pt = expand_sparse(pic["objects"]["ct"])
Bc = proper["proper_Br2_cc_action_f2"]
Bt = proper["proper_Br2_ct_action_f2"]
I = [[int(i == j) for j in range(NP)] for i in range(NP)]
Nc = [xor(row, eye) for row, eye in zip(Pc, I)]
Nt = [xor(row, eye) for row, eye in zip(Pt, I)]
retained = target["proper_invariant_domain"]["basis_rows_original_proper_br2_coordinates_f2"]

checks = 0
for a in range(NB):
    for p in range(NP):
        # Psi has only row a = e_p.  Compute Phi rows directly from Psi P + B Psi.
        phi_c = [[0] * NP for _ in range(NB)]
        phi_t = [[0] * NP for _ in range(NB)]
        for q in range(NP):
            phi_c[a][q] ^= Pc[p][q]
            phi_t[a][q] ^= Pt[p][q]
        for b in range(NB):
            if Bc[b][a]:
                phi_c[b][p] ^= 1
            if Bt[b][a]:
                phi_t[b][p] ^= 1

        # Involution block laws.
        for b in range(NB):
            assert xor(rowmul(phi_c[b], Pc), [sum(Bc[b][k] * phi_c[k][j] for k in range(NB)) & 1 for j in range(NP)]) == [0] * NP
            assert xor(rowmul(phi_t[b], Pt), [sum(Bt[b][k] * phi_t[k][j] for k in range(NB)) & 1 for j in range(NP)]) == [0] * NP
            left = xor(rowmul(phi_c[b], Pt), [sum(Bc[b][k] * phi_t[k][j] for k in range(NB)) & 1 for j in range(NP)])
            right = xor(rowmul(phi_t[b], Pc), [sum(Bt[b][k] * phi_c[k][j] for k in range(NB)) & 1 for j in range(NP)])
            assert left == right

        # Boundary of every invariant source is exactly a Picard coboundary.
        for source in retained:
            w = [source[a] if j == p else 0 for j in range(NP)]
            raw_c = [sum(source[k] * phi_c[k][j] for k in range(NB)) & 1 for j in range(NP)]
            raw_t = [sum(source[k] * phi_t[k][j] for k in range(NB)) & 1 for j in range(NP)]
            assert raw_c == rowmul(w, Nc)
            assert raw_t == rowmul(w, Nt)
        checks += 1

print(json.dumps({
    "success": True,
    "canonical_sha256": claimed,
    "full_recompute_matches": True,
    "elementary_section_change_gauge_checks": checks,
    "gauge_coboundary_sanity": True,
    "locked_J2_relation_compatible": False,
}, sort_keys=True))
