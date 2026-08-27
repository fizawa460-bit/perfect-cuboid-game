#!/usr/bin/env python3
"""Extract one Q-defined coordinate-swap Picard action without Smith form.

The public calculator is only asked for one 64x64 integral Picard action and
its boundary permutation.  No Smith transformation or discriminant reduction
is performed remotely.  The two modes are the Testa--Stoll automorphism
indices 1 and 2:

  swap12: a1<->a2 and b1<->b2
  swap13: a1<->a3 and b1<->b3.
"""
import ast
import hashlib
import json
import pathlib
import re
import sys

from stoll_cuboid_source import load_pinned_source, run_magma

MODES = {"swap12": 1, "swap13": 2}
if len(sys.argv) != 2 or sys.argv[1] not in MODES:
    raise SystemExit("usage: extract_picard_coordinate_swap_rows.py swap12|swap13")
mode = sys.argv[1]
idx = MODES[mode]
HERE = pathlib.Path(__file__).resolve().parent
full, core, blob, source_attempt = load_pinned_source()
a = full.index("// The automorphism group (see Proposition 4)")
b = full.index("// Automorphisms + Galois on Pic/2*Pic", a)
block = full[a:b]
block = "\n".join(
    line for line in block.splitlines()
    if not line.startswith("AutS :=") and not line.startswith('printf "#Aut(S) =')
) + "\n"
extra = f'''\nidx := {idx};\nG := action[idx];\nI64 := IdentityMatrix(Integers(),64);\nassert G*pmPic*Transpose(G) eq pmPic;\nassert G^2 eq I64;\nassert G*ccPic eq ccPic*G and G*ctPic eq ctPic*G;\nsidep := perms[idx][1..24];\npointp := [perms[idx][#Cs+j]-#Cs : j in [1..#pts]];\nassert Seqset(sidep) eq {{1..24}};\nassert Seqset(pointp) eq {{1..48}};\nprintf "STAGE33_07_SWAP_BEGIN\\n";\nprintf "SIDE_PERM=%o\\n",sidep;\nprintf "POINT_PERM=%o\\n",pointp;\nfor r in [1..64] do printf "G_ROW_%o=%o\\n",r,[G[r,c]:c in [1..64]]; end for;\nprintf "STAGE33_07_SWAP_END\\n";\n'''
code = "SetColumns(0);\nquick := true;\n" + core + "\n" + block + extra
stdout, attempt = run_magma(
    code, 240, f"Stage33-07 Picard {mode} action rows Magma",
    user_agent="perfect-cuboid-stage33/3.4",
)
(HERE / f"picard-action-{mode}-magma-stdout.txt").write_text(stdout, encoding="utf-8")
if "STAGE33_07_SWAP_END" not in stdout or any(
    x in stdout for x in ("Runtime error", "Internal error", "Assertion failed")
):
    print(stdout)
    raise SystemExit(f"Picard {mode} action row extraction failed")

def grab(name):
    m = re.search(rf"^{re.escape(name)}=(.+)$", stdout, re.M)
    if not m:
        raise SystemExit(f"missing {mode} output {name}")
    return ast.literal_eval(m.group(1))

rows = []
for r in range(1, 65):
    row = grab(f"G_ROW_{r}")
    if len(row) != 64:
        raise SystemExit("action row length regression")
    rows.append([int(x) for x in row])
sidep = [int(x) for x in grab("SIDE_PERM")]
pointp = [int(x) for x in grab("POINT_PERM")]
if sorted(sidep) != list(range(1,25)) or sorted(pointp) != list(range(1,49)):
    raise SystemExit("boundary permutation regression")
out = {
    "schema": "STAGE33_07_PICARD_COORDINATE_SWAP_ROWS_V1",
    "action": mode,
    "upstream_automorphism_index_1based": idx,
    "upstream_git_blob_sha1": blob,
    "source_fetch_attempt": source_attempt,
    "submitted_code_sha256": hashlib.sha256(code.encode()).hexdigest(),
    "magma_request_attempt": attempt,
    "picard_action_64x64": rows,
    "boundary_side_permutation_1based": sidep,
    "boundary_exceptional_permutation_1based": pointp,
    "smith_form_used": False,
    "stage33_progress": "6/11",
    "stage33_08_released": False,
}
can = json.dumps(out, sort_keys=True, separators=(",", ":")).encode()
out["canonical_sha256"] = hashlib.sha256(can).hexdigest()
(HERE / f"picard-action-{mode}.json").write_text(
    json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps({
    "success": True,
    "action": mode,
    "rank": 64,
    "smith_form_used": False,
    "certificate_sha256": out["canonical_sha256"],
}, indent=2, sort_keys=True))
