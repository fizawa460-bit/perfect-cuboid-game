#!/usr/bin/env python3
import hashlib
import io
import json
import os
import pathlib
import urllib.parse
import urllib.request
import zipfile

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parent
REPO = "fizawa460-bit/perfect-cuboid-game"
BR0A_ARTIFACT_ID = 9505735040
BR0A_ARTIFACT_URL = f"https://api.github.com/repos/{REPO}/actions/artifacts/{BR0A_ARTIFACT_ID}/zip"
BR0A_ARTIFACT_SHA256 = "75eb5c0753b06ea3bad9902d70fd8b59ed24ce190a64882d93935f5760d1ec87"
BR0A_CERTIFICATE_SHA256 = "2e365c273f2aae44adb7a871c864fa55d19a95336686b13a5eef245175f8bcd1"


class StripCrossHostAuthRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        newreq = super().redirect_request(req, fp, code, msg, headers, newurl)
        if newreq is not None and urllib.parse.urlsplit(req.full_url).netloc != urllib.parse.urlsplit(newurl).netloc:
            newreq.remove_header("Authorization")
        return newreq


def download_br0a():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN required")
    req = urllib.request.Request(
        BR0A_ARTIFACT_URL,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "perfect-cuboid-stage33/1.8",
        },
    )
    opener = urllib.request.build_opener(StripCrossHostAuthRedirect())
    with opener.open(req, timeout=60) as resp:
        raw = resp.read()
    if hashlib.sha256(raw).hexdigest() != BR0A_ARTIFACT_SHA256:
        raise SystemExit("BR0A artifact digest mismatch")
    with zipfile.ZipFile(io.BytesIO(raw)) as zf:
        name = next((n for n in zf.namelist() if n.endswith("br0a-artifact-certificate.json")), None)
        if name is None:
            raise SystemExit("missing BR0A certificate")
        cert_bytes = zf.read(name)
    if hashlib.sha256(cert_bytes).hexdigest() != BR0A_CERTIFICATE_SHA256:
        raise SystemExit("BR0A certificate digest mismatch")
    return json.loads(cert_bytes)


def perm_matrix(perm):
    P = sp.zeros(len(perm))
    for j, image in enumerate(perm):
        P[j, image - 1] = 1
    return P


def basis_action_on_row_lattice(K, P):
    pivots = list(K.rref()[1])
    if len(pivots) != K.rows:
        raise SystemExit("unit lattice lost rank")
    minor = K[:, pivots]
    acted = K * P
    A = acted[:, pivots] * minor.inv()
    if any(sp.Rational(x).q != 1 for x in A):
        raise SystemExit("nonintegral unit action")
    A = sp.Matrix([[int(A[i, j]) for j in range(A.cols)] for i in range(A.rows)])
    if A * K != acted:
        raise SystemExit("unit action reconstruction failed")
    return A


def rank_mod2(rows):
    if not rows:
        return 0
    a = [[int(x) & 1 for x in row] for row in rows]
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        pivot = next((u for u in range(r, m) if a[u][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        for u in range(m):
            if u != r and a[u][c]:
                a[u] = [x ^ y for x, y in zip(a[u], a[r])]
        r += 1
        if r == m:
            break
    return r


def independent_row_indices(rows):
    basis = {}
    out = []
    for idx, row in enumerate(rows):
        x = 0
        for j, bit in enumerate(row):
            if int(bit) & 1:
                x |= 1 << j
        y = x
        while y:
            p = y.bit_length() - 1
            if p in basis:
                y ^= basis[p]
            else:
                basis[p] = y
                out.append(idx)
                break
    return out


def act_edge_vector(v, perm):
    out = [0] * len(v)
    for j, bit in enumerate(v):
        out[perm[j] - 1] = int(bit) & 1
    return out


br0a = download_br0a()
skeleton = json.loads((ROOT / "boundary-residue-skeleton.json").read_text(encoding="utf-8"))
bg = json.loads((ROOT / "boundary-galois.json").read_text(encoding="utf-8"))
cg = json.loads((ROOT / "boundary-cycle-galois.json").read_text(encoding="utf-8"))

K = sp.Matrix(br0a["unit_divisor_relation_kernel_basis"])
if K.shape != (14, 72) or K.rank() != 14:
    raise SystemExit("unexpected audited unit divisor kernel")

Pcc = perm_matrix(bg["boundary_perm_cc_1based"])
Pct = perm_matrix(bg["boundary_perm_ct_1based"])
Ucc = basis_action_on_row_lattice(K, Pcc)
Uct = basis_action_on_row_lattice(K, Pct)
if Ucc != sp.eye(14) or Uct != sp.eye(14):
    raise SystemExit("unit divisor lattice is not pointwise V4 fixed")

edges = [(int(e["side_vertex"]) - 1, int(e["exceptional_vertex"]) - 1)
         for e in skeleton["codim2_crossings"]]
if len(edges) != 144:
    raise SystemExit("unexpected boundary edge count")

# For unit divisor vectors v,w, the parity of the secondary tame residue at a
# transverse crossing D_a cap D_b is det[[v_a,v_b],[w_a,w_b]] mod 2.  This is
# the graph-level Gersten footprint of the 2-symbol {u_v,u_w}.  We use only the
# divisor-level footprint here: no explicit rational-function representative or
# Brauer-class independence credit is inferred from this certificate alone.
pairs = []
patterns = []
for i in range(14):
    vi = [int(K[i, j]) for j in range(72)]
    for j in range(i + 1, 14):
        vj = [int(K[j, k]) for k in range(72)]
        p = [(vi[a] * vj[b] - vj[a] * vi[b]) & 1 for a, b in edges]
        # Exact graph-cycle compatibility at every boundary component.
        vertex_boundary = [0] * 72
        for bit, (a, b) in zip(p, edges):
            if bit:
                vertex_boundary[a] ^= 1
                vertex_boundary[b] ^= 1
        if any(vertex_boundary):
            raise SystemExit(f"unit-symbol secondary residue is not a graph cycle: {i+1},{j+1}")
        pairs.append((i + 1, j + 1))
        patterns.append(p)

if len(patterns) != 91:
    raise SystemExit("expected 91 unit-symbol pairs")
span_rank = rank_mod2(patterns)
independent = independent_row_indices(patterns)
if len(independent) != span_rank:
    raise SystemExit("independent pair extraction mismatch")

cc_perm = cg["edge_action"]["cc_perm_1based"]
ct_perm = cg["edge_action"]["ct_perm_1based"]
if any(act_edge_vector(p, cc_perm) != p for p in patterns):
    raise SystemExit("unit-symbol residue span not fixed by complex conjugation")
if any(act_edge_vector(p, ct_perm) != p for p in patterns):
    raise SystemExit("unit-symbol residue span not fixed by sqrt(2) conjugation")

qfixed = int(cg["f2_joint_fixed_dimension"])
if qfixed != 61 or span_rank > qfixed:
    raise SystemExit("Q-fixed residue dimension regression")

cert = {
    "schema": "STAGE33_04_UNIT_SYMBOL_SECONDARY_RESIDUE_SPAN_V1",
    "source_locks": {
        "br0a_artifact_id": BR0A_ARTIFACT_ID,
        "br0a_artifact_sha256": BR0A_ARTIFACT_SHA256,
        "br0a_certificate_sha256": BR0A_CERTIFICATE_SHA256,
        "unit_kernel_sha256": br0a["unit_divisor_relation_kernel_basis_sha256"],
        "boundary_skeleton_sha256": skeleton["canonical_sha256"],
        "boundary_galois_sha256": bg["canonical_sha256"],
        "cycle_galois_sha256": cg["canonical_sha256"],
        "residue_formula": "secondary parity at D_a cap D_b = v_a*w_b - w_a*v_b mod 2",
    },
    "unit_divisor_lattice_rank": 14,
    "unit_divisor_lattice_pointwise_v4_fixed": True,
    "candidate_symbol_pair_count": 91,
    "all_secondary_residue_patterns_are_graph_cycles": True,
    "all_secondary_residue_patterns_are_v4_fixed": True,
    "unit_symbol_secondary_residue_span_rank_f2": span_rank,
    "qfixed_boundary_cycle_dimension_f2": qfixed,
    "qfixed_complement_after_unit_symbol_span_dimension": qfixed - span_rank,
    "independent_symbol_pairs_1based": [list(pairs[k]) for k in independent],
    "independent_secondary_residue_patterns": [patterns[k] for k in independent],
    "explicit_q_rational_unit_functions_materialized": False,
    "q_defined_brauer_class_independence_certified": False,
    "physical_open_unramified_kernel_complete": False,
    "br0g_discharged": False,
    "next_exact_leaf": "L33-04-MATERIALIZE-14-Q-UNITS-AND-LIFT-44-SYMBOL-RESIDUES",
    "theorem_credit": False,
    "endpoint_credit": False,
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "unit-symbol-residue-span.json").write_text(
    json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps({
    "success": True,
    "unit_rank": 14,
    "symbol_pairs": 91,
    "unit_symbol_secondary_residue_span_rank_f2": span_rank,
    "qfixed_boundary_cycle_dimension_f2": qfixed,
    "qfixed_complement_dimension": qfixed - span_rank,
    "next_exact_leaf": cert["next_exact_leaf"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
