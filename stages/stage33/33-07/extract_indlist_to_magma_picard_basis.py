#!/usr/bin/env python3
"""Extract the exact marked basis bridge from INDLIST to Magma's Picard basis.

The pinned Testa--Stoll source defines
  MatqPic = Matrix([qPic(Big.j) : j in [1..140]])
and proves that the 64 known classes indexed by `indlist` map isomorphically
onto Pic.  Thus the corresponding 64 rows are the literal change-of-basis
matrix from the marked INDLIST basis used by the retained Stage32 geometry to
the Magma-chosen Picard basis used by the historical Stage33 q256 endpoint.

Only this 64x64 integer bridge is emitted. No automorphism, Smith form, Brauer
module or Gersten computation is performed in this leaf.
"""
from __future__ import annotations

import ast
import hashlib
import json
import re
from pathlib import Path

from stoll_cuboid_source import load_pinned_source, run_magma

HERE = Path(__file__).resolve().parent
OUT = HERE / "indlist-to-magma-picard-basis.json"
SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
INDLIST = [
    1,2,3,4,5,6,7,9,10,11,12,13,14,15,17,18,19,20,21,22,23,
    25,26,27,29,33,34,35,37,38,41,45,49,53,69,
    93,94,95,96,97,98,99,101,102,103,104,105,106,107,
    109,110,111,113,117,118,119,120,121,125,126,127,129,133,135,
]


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def grab(stdout: str, name: str) -> list[int]:
    m = re.search(rf"^{re.escape(name)}=(.+)$", stdout, re.M)
    if not m:
        raise SystemExit(f"missing marked Picard bridge output {name}")
    row = ast.literal_eval(m.group(1))
    if not isinstance(row, list) or len(row) != 64:
        raise SystemExit(f"bad marked Picard bridge row {name}")
    return [int(x) for x in row]


text, core, blob, source_attempt = load_pinned_source()
if blob != SOURCE_BLOB:
    raise SystemExit("pinned upstream blob moved")
# The retained helper stops immediately before the automorphism block, after
# qPic, MatqPic, indlist, pmPic and the primitive-surjectivity assertion exist.
extra = r'''
assert #indlist eq 64;
assert qPic(sub<Big | [Big.j : j in indlist]>) eq Pic;
printf "STAGE33_07_MARKED_PICARD_BRIDGE_BEGIN\n";
for r in [1..64] do
  printf "B_ROW_%o=%o\n", r, Eltseq(qPic(Big.indlist[r]));
end for;
printf "STAGE33_07_MARKED_PICARD_BRIDGE_END\n";
'''
code = "SetColumns(0);\nquick := true;\n" + core + "\n" + extra
stdout, attempt = run_magma(
    code, 180, "Stage33-07 marked INDLIST-to-Magma Picard basis",
    user_agent="perfect-cuboid-stage33/3.2-marked-picard-bridge",
)
if "STAGE33_07_MARKED_PICARD_BRIDGE_END" not in stdout or any(
    x in stdout for x in ("Runtime error", "Internal error", "User error", "Assertion failed")
):
    print(stdout)
    raise SystemExit("marked Picard basis bridge extraction failed")
B = [grab(stdout, f"B_ROW_{r}") for r in range(1, 65)]

out = {
    "schema": "STAGE33_07_INDLIST_TO_MAGMA_PICARD_BASIS_V1",
    "source": {
        "repository": "MichaelStollBayreuth/Verification",
        "commit": "51233ed5ef2bf228fac9416c66db9adc0ebcaadd",
        "path": "Cuboids/cuboids.magma",
        "git_blob_sha1": blob,
        "submitted_code_sha256": hashlib.sha256(code.encode()).hexdigest(),
    },
    "basis_from": "upstream primitive INDLIST known-class basis",
    "basis_to": "Magma Basis(Pic) chosen by pinned upstream quotient",
    "indlist_1based": INDLIST,
    "indlist_to_magma_picard_matrix_64x64": B,
    "upstream_asserts_indlist_maps_onto_pic": True,
    "execution": {
        "source_fetch_attempt": source_attempt,
        "magma_request_attempt": attempt,
        "remote_cas_role": "emit the exact upstream quotient-basis coordinates of 64 already-defined marked classes",
        "automorphism_computed": False,
        "smith_form_computed": False,
        "gersten_data_computed": False,
    },
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
out["canonical_sha256"] = csha(out)
OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "row_count": 64,
    "certificate_sha256": out["canonical_sha256"],
}, indent=2, sort_keys=True))
