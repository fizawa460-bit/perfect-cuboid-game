#!/usr/bin/env python3
import collections
import hashlib
import io
import json
import os
import pathlib
import urllib.parse
import urllib.request
import zipfile

import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_decomp

ROOT = pathlib.Path(__file__).resolve().parent
REPO = "fizawa460-bit/perfect-cuboid-game"
ARTIFACT_ID = 9505735040
ARTIFACT_URL = f"https://api.github.com/repos/{REPO}/actions/artifacts/{ARTIFACT_ID}/zip"
ARTIFACT_SHA256 = "75eb5c0753b06ea3bad9902d70fd8b59ed24ce190a64882d93935f5760d1ec87"
CERTIFICATE_SHA256 = "2e365c273f2aae44adb7a871c864fa55d19a95336686b13a5eef245175f8bcd1"


class StripCrossHostAuthRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        newreq = super().redirect_request(req, fp, code, msg, headers, newurl)
        if newreq is not None:
            oldhost = urllib.parse.urlsplit(req.full_url).netloc
            newhost = urllib.parse.urlsplit(newurl).netloc
            if oldhost != newhost:
                newreq.remove_header("Authorization")
        return newreq


def download_artifact():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN required")
    req = urllib.request.Request(
        ARTIFACT_URL,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "perfect-cuboid-stage33/1.3",
        },
    )
    opener = urllib.request.build_opener(StripCrossHostAuthRedirect())
    with opener.open(req, timeout=60) as resp:
        raw = resp.read()
    got = hashlib.sha256(raw).hexdigest()
    if got != ARTIFACT_SHA256:
        raise SystemExit(f"artifact digest mismatch: {got}")
    return raw


def rank_mod2(rows):
    a = [[int(x) & 1 for x in row] for row in rows]
    if not a:
        return 0
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


def int_rows(M):
    out = []
    for i in range(M.rows):
        row = []
        for j in range(M.cols):
            q = sp.Rational(M[i, j])
            if q.q != 1:
                raise SystemExit("nonintegral exact matrix")
            row.append(int(q))
        out.append(row)
    return out


raw_zip = download_artifact()
with zipfile.ZipFile(io.BytesIO(raw_zip)) as zf:
    cert_name = next((n for n in zf.namelist() if n.endswith("br0a-artifact-certificate.json")), None)
    if cert_name is None:
        raise SystemExit("missing BR0A certificate")
    cert_bytes = zf.read(cert_name)
if hashlib.sha256(cert_bytes).hexdigest() != CERTIFICATE_SHA256:
    raise SystemExit("BR0A certificate hash mismatch")
cert = json.loads(cert_bytes)
P = sp.Matrix(cert["boundary_intersection_matrix"])
if P.shape != (72, 72) or P != P.T:
    raise SystemExit("bad audited boundary intersection matrix")

labels = []
for family in ("A1", "A2", "A3"):
    labels.extend([f"SIDE_{family}_{j:03d}" for j in range(1, 9)])
labels.extend([f"EXC_{j:03d}" for j in range(1, 49)])
if len(labels) != 72 or len(set(labels)) != 72:
    raise SystemExit("stable boundary labels failed")
upstream_indices = list(range(1, 25)) + list(range(93, 141))

# Exact resolved-boundary block shape.
for i in range(24):
    if int(P[i, i]) != -4:
        raise SystemExit(f"side self-intersection mismatch at {i}")
for i in range(24, 72):
    if int(P[i, i]) != -2:
        raise SystemExit(f"exceptional self-intersection mismatch at {i}")
for i in range(24):
    for j in range(24):
        if i != j and int(P[i, j]) != 0:
            raise SystemExit(f"nonzero side-side resolved intersection {i},{j}: {P[i,j]}")
for i in range(24, 72):
    for j in range(24, 72):
        if i != j and int(P[i, j]) != 0:
            raise SystemExit(f"nonzero exceptional-exceptional intersection {i},{j}: {P[i,j]}")
for i in range(24):
    for j in range(24, 72):
        if int(P[i, j]) not in (0, 1):
            raise SystemExit(f"non-SNC side-exceptional multiplicity {i},{j}: {P[i,j]}")

edges = []
for i in range(24):
    for j in range(24, 72):
        if int(P[i, j]) == 1:
            edges.append((i, j))
E = len(edges)
V = 72

# Union-find connected components.
parent = list(range(V))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[rb] = ra

for a, b in edges:
    union(a, b)
components = collections.defaultdict(list)
for v in range(V):
    components[find(v)].append(v)
component_lists = sorted((sorted(vs) for vs in components.values()), key=lambda x: (x[0], len(x)))
c = len(component_lists)
cycle_rank_formula = E - V + c
if cycle_rank_formula < 0:
    raise SystemExit("negative graph cycle rank")

# Oriented integral incidence: side -> exceptional.
B = sp.zeros(V, E)
for k, (a, b) in enumerate(edges):
    B[a, k] = -1
    B[b, k] = 1
rank_Q = B.rank()
if rank_Q != V - c:
    raise SystemExit(f"incidence rank mismatch {rank_Q} != {V-c}")
rank_F2 = rank_mod2(int_rows(B))
if rank_F2 != V - c:
    raise SystemExit(f"mod2 incidence rank mismatch {rank_F2} != {V-c}")

# Exact saturated integral cycle lattice ker(B).
D, S, T = smith_normal_decomp(B, domain=ZZ)
if D != S * B * T:
    raise SystemExit("incidence Smith identity failed")
cycle_rank = E - rank_Q
if cycle_rank != cycle_rank_formula:
    raise SystemExit("cycle rank mismatch")
Kcycle = T[:, rank_Q:].T
if Kcycle.shape != (cycle_rank, E):
    raise SystemExit("cycle lattice shape mismatch")
if Kcycle * B.T != sp.zeros(cycle_rank, V):
    raise SystemExit("integral cycle basis does not annihilate incidence")
if Kcycle.rank() != cycle_rank:
    raise SystemExit("integral cycle basis lost rank")

side_degrees = [sum(1 for a, _ in edges if a == i) for i in range(24)]
exc_degrees = [sum(1 for _, b in edges if b == j) for j in range(24, 72)]
edge_records = [
    {
        "edge_id": f"X_{k+1:04d}",
        "side_id": labels[a],
        "exceptional_id": labels[b],
        "side_vertex": a + 1,
        "exceptional_vertex": b + 1,
    }
    for k, (a, b) in enumerate(edges)
]

# On a smooth surface, two distinct curves have nonnegative local intersection
# multiplicities. The exact zero side-side block therefore rules out two side
# strict transforms sharing an exceptional crossing. Combined with each
# side-exceptional total intersection equal to 1, every listed edge is a unique
# transverse codimension-two point and no triple boundary point occurs.
certificate = {
    "schema": "STAGE33_04_PHYSICAL_BOUNDARY_SNC_RESIDUE_SKELETON_V1",
    "source_lock": {
        "br0a_artifact_id": ARTIFACT_ID,
        "br0a_artifact_sha256": ARTIFACT_SHA256,
        "br0a_certificate_sha256": CERTIFICATE_SHA256,
        "boundary_intersection_matrix_sha256": cert["boundary_intersection_matrix_sha256"],
    },
    "component_inventory": [
        {
            "vertex": i + 1,
            "stable_id": labels[i],
            "kind": "side_conic" if i < 24 else "exceptional_curve",
            "upstream_index_1based": upstream_indices[i],
            "self_intersection": int(P[i, i]),
        }
        for i in range(72)
    ],
    "component_count": V,
    "side_component_count": 24,
    "exceptional_component_count": 48,
    "codim2_crossing_count": E,
    "connected_component_count": c,
    "connected_components_vertex_ids": [[x + 1 for x in vs] for vs in component_lists],
    "dual_graph_cycle_rank": cycle_rank,
    "integral_incidence_rank": rank_Q,
    "mod2_incidence_rank": rank_F2,
    "side_degree_multiset": sorted(side_degrees),
    "exceptional_degree_multiset": sorted(exc_degrees),
    "side_degree_histogram": dict(sorted(collections.Counter(side_degrees).items())),
    "exceptional_degree_histogram": dict(sorted(collections.Counter(exc_degrees).items())),
    "codim2_crossings": edge_records,
    "integral_cycle_basis": int_rows(Kcycle),
    "exact_checks": {
        "all_72_components_present": True,
        "side_side_offdiagonal_zero": True,
        "exceptional_exceptional_offdiagonal_zero": True,
        "side_exceptional_entries_binary": True,
        "resolved_boundary_bipartite": True,
        "unique_crossing_per_nonzero_pair": True,
        "triple_boundary_crossings_excluded_by_zero_side_side_intersection": True,
        "all_crossings_transverse": True,
        "integral_cycle_lattice_saturated": True,
        "prime_by_prime_graph_compatibility_rank_locked": True,
    },
    "gersten_boundary_cycle_module": f"(Q/Z)^{cycle_rank}",
    "gersten_prime_primary_cycle_dimension": cycle_rank,
    "galois_action_on_cycle_module_attached": False,
    "multiquadratic_pullback_accounted": False,
    "physical_open_unramified_kernel_complete": False,
    "br0g_discharged": False,
    "unit_closed": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
canonical = json.dumps(certificate, sort_keys=True, separators=(",", ":")).encode()
certificate["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
out = json.dumps(certificate, indent=2, sort_keys=True) + "\n"
(ROOT / "boundary-residue-skeleton.json").write_text(out, encoding="utf-8")
print(json.dumps({
    "success": True,
    "vertices": V,
    "edges": E,
    "components": c,
    "cycle_rank": cycle_rank,
    "side_degree_histogram": certificate["side_degree_histogram"],
    "exceptional_degree_histogram": certificate["exceptional_degree_histogram"],
    "certificate_sha256": certificate["canonical_sha256"],
}, indent=2, sort_keys=True))
