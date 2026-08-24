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
        if newreq is not None:
            oldhost = urllib.parse.urlsplit(req.full_url).netloc
            newhost = urllib.parse.urlsplit(newurl).netloc
            if oldhost != newhost:
                newreq.remove_header("Authorization")
        return newreq


def download_br0a_artifact() -> bytes:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN required")
    req = urllib.request.Request(
        BR0A_ARTIFACT_URL,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "perfect-cuboid-stage33/1.4",
        },
    )
    opener = urllib.request.build_opener(StripCrossHostAuthRedirect())
    with opener.open(req, timeout=60) as resp:
        raw = resp.read()
    got = hashlib.sha256(raw).hexdigest()
    if got != BR0A_ARTIFACT_SHA256:
        raise SystemExit(f"BR0A artifact digest mismatch: expected {BR0A_ARTIFACT_SHA256}, got {got}")
    return raw


def int_rows(M: sp.Matrix):
    out = []
    for i in range(M.rows):
        row = []
        for j in range(M.cols):
            x = sp.Rational(M[i, j])
            if x.q != 1:
                raise SystemExit("nonintegral exact matrix")
            row.append(int(x))
        out.append(row)
    return out


def perm_matrix(perm_1based):
    n = len(perm_1based)
    P = sp.zeros(n)
    for j, image in enumerate(perm_1based):
        P[j, image - 1] = 1
    return P


def basis_action_on_row_lattice(K: sp.Matrix, P: sp.Matrix):
    # K has independent rows.  Row coefficients transform by right multiplication
    # with the boundary permutation matrix.  Express the transformed rows back in
    # the exact saturated Stage33-02 kernel basis.
    pivots = list(K.rref()[1])
    if len(pivots) != K.rows:
        raise SystemExit("row lattice basis lost rank")
    minor = K[:, pivots]
    if minor.det() == 0:
        raise SystemExit("chosen row-basis minor singular")
    acted = K * P
    A = acted[:, pivots] * minor.inv()
    if any(sp.Rational(A[i, j]).q != 1 for i in range(A.rows) for j in range(A.cols)):
        raise SystemExit("Galois action does not preserve unit lattice integrally")
    A = sp.Matrix([[int(A[i, j]) for j in range(A.cols)] for i in range(A.rows)])
    if A * K != acted:
        raise SystemExit("unit-lattice action reconstruction failed")
    return A, pivots


def joint_eigenspace_multiplicities(A, B):
    n = A.rows
    I = sp.eye(n)
    out = {}
    for ea in (1, -1):
        for eb in (1, -1):
            stacked = (A - ea * I).col_join(B - eb * I)
            dim = n - stacked.rank()
            out[f"cc{ea:+d}_ct{eb:+d}"] = dim
    if sum(out.values()) != n:
        raise SystemExit(f"V4 rational eigenspaces do not sum to rank: {out}")
    return out


def multiplicities_from_traces(rank, tcc, tct, tcct):
    out = {}
    for ea in (1, -1):
        for eb in (1, -1):
            num = rank + ea * tcc + eb * tct + ea * eb * tcct
            if num % 4:
                raise SystemExit(f"nonintegral V4 multiplicity numerator {num}")
            out[f"cc{ea:+d}_ct{eb:+d}"] = num // 4
    if any(v < 0 for v in out.values()) or sum(out.values()) != rank:
        raise SystemExit(f"invalid V4 multiplicities {out}")
    return out


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


def matmul_mod2(A, B):
    if not A or not B:
        return []
    m, k, n = len(A), len(B), len(B[0])
    if len(A[0]) != k:
        raise SystemExit("GF2 matrix shape mismatch")
    BT = list(zip(*B))
    return [[sum((x & 1) * (y & 1) for x, y in zip(A[i], col)) & 1 for col in BT] for i in range(m)]


def nullspace_columns_mod2(rows):
    # Return an n x q matrix whose columns form the right nullspace of rows.
    A = [[int(x) & 1 for x in row] for row in rows]
    m, n = len(A), len(A[0])
    r = 0
    pivots = []
    for c in range(n):
        pivot = next((u for u in range(r, m) if A[u][c]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        for u in range(m):
            if u != r and A[u][c]:
                A[u] = [x ^ y for x, y in zip(A[u], A[r])]
        pivots.append(c)
        r += 1
        if r == m:
            break
    free = [c for c in range(n) if c not in pivots]
    basis = []
    for f in free:
        v = [0] * n
        v[f] = 1
        for rr in range(len(pivots) - 1, -1, -1):
            pc = pivots[rr]
            v[pc] = sum(A[rr][j] * v[j] for j in free) & 1
        basis.append(v)
    return [list(col) for col in zip(*basis)] if basis else [[] for _ in range(n)]


def sub_identity_mod2(A):
    n = len(A)
    return [[(A[i][j] ^ (1 if i == j else 0)) for j in range(n)] for i in range(n)]


def quotient_fixed_dim_mod2(Mrows, A, B=None):
    # I=row(M) is stable.  A quotient class [v] is fixed iff v(A-I) lies in I.
    # Membership in I is detected by a right-nullspace matrix N of I.
    n = len(A)
    rI = rank_mod2(Mrows)
    N = nullspace_columns_mod2(Mrows)  # n x (n-rI)
    C1 = matmul_mod2(sub_identity_mod2(A), N)
    if B is None:
        C = C1
    else:
        C2 = matmul_mod2(sub_identity_mod2(B), N)
        C = [r1 + r2 for r1, r2 in zip(C1, C2)]
    preimage_dim = n - rank_mod2(C)
    qdim = preimage_dim - rI
    if qdim < 0:
        raise SystemExit("negative quotient fixed dimension")
    return qdim


raw_zip = download_br0a_artifact()
with zipfile.ZipFile(io.BytesIO(raw_zip)) as zf:
    names = zf.namelist()
    cert_name = next((n for n in names if n.endswith("br0a-artifact-certificate.json")), None)
    if cert_name is None:
        raise SystemExit(f"BR0A certificate absent from artifact: {names}")
    cert_bytes = zf.read(cert_name)
if hashlib.sha256(cert_bytes).hexdigest() != BR0A_CERTIFICATE_SHA256:
    raise SystemExit("BR0A certificate hash mismatch")
br0a = json.loads(cert_bytes)
raw = json.loads((ROOT / "galois-action-raw.json").read_text(encoding="utf-8"))

M = sp.Matrix(br0a["boundary_to_pic_matrix"])
K = sp.Matrix(br0a["unit_divisor_relation_kernel_basis"])
if M.shape != (72, 64) or K.shape != (14, 72):
    raise SystemExit(f"unexpected audited BR0A shapes M={M.shape}, K={K.shape}")

Pcc = perm_matrix(raw["boundary_perm_cc_1based"])
Pct = perm_matrix(raw["boundary_perm_ct_1based"])
I72 = sp.eye(72)
if Pcc * Pcc != I72 or Pct * Pct != I72 or Pcc * Pct != Pct * Pcc:
    raise SystemExit("boundary actions do not realize V4")

Ucc, unit_pivots = basis_action_on_row_lattice(K, Pcc)
Uct, unit_pivots2 = basis_action_on_row_lattice(K, Pct)
if unit_pivots != unit_pivots2:
    raise SystemExit("unit pivot choices unexpectedly differ")
I14 = sp.eye(14)
if Ucc * Ucc != I14 or Uct * Uct != I14 or Ucc * Uct != Uct * Ucc:
    raise SystemExit("unit-lattice action does not realize V4")
unit_mult = joint_eigenspace_multiplicities(Ucc, Uct)
unit_traces = {
    "id": 14,
    "cc": int(sp.trace(Ucc)),
    "ct": int(sp.trace(Uct)),
    "cct": int(sp.trace(Ucc * Uct)),
}

# Exact rational character of Div_D is the fixed-point count of each permutation.
def perm_trace(perm):
    return sum(1 for j, image in enumerate(perm, start=1) if j == image)

div_traces = {
    "id": 72,
    "cc": perm_trace(raw["boundary_perm_cc_1based"]),
    "ct": perm_trace(raw["boundary_perm_ct_1based"]),
    "cct": perm_trace([
        raw["boundary_perm_ct_1based"][raw["boundary_perm_cc_1based"][j] - 1]
        for j in range(72)
    ]),
}
pic_traces = raw["picard_character_traces"]
if pic_traces["id"] != 64:
    raise SystemExit("bad Picard identity trace")

# Over Q the exact sequence 0->U_D->Div_D->Pic->Pic(Ubar)->0 gives characters
# additively.  This determines the six-dimensional free quotient representation
# without exporting the huge integral Picard matrices.
picu_free_traces = {
    g: int(pic_traces[g]) - int(div_traces[g]) + int(unit_traces[g])
    for g in ("id", "cc", "ct", "cct")
}
if picu_free_traces["id"] != 6:
    raise SystemExit(f"Pic(Ubar)_Q rank mismatch from traces: {picu_free_traces}")
picu_free_mult = multiplicities_from_traces(
    6, picu_free_traces["cc"], picu_free_traces["ct"], picu_free_traces["cct"]
)

# Independent mod-2 equivariance and quotient fixed-space information.  The
# integral equivariance was asserted inside Magma before export; here the compact
# mod-2 matrices permit a second backend to verify the same relation modulo 2.
M2 = [[int(x) & 1 for x in row] for row in br0a["boundary_to_pic_matrix"]]
Acc2 = raw["picard_cc_matrix_mod2"]
Act2 = raw["picard_ct_matrix_mod2"]
Pcc2 = [[int(x) & 1 for x in row] for row in int_rows(Pcc)]
Pct2 = [[int(x) & 1 for x in row] for row in int_rows(Pct)]
if matmul_mod2(Pcc2, M2) != matmul_mod2(M2, Acc2):
    raise SystemExit("independent cc equivariance mod2 failed")
if matmul_mod2(Pct2, M2) != matmul_mod2(M2, Act2):
    raise SystemExit("independent ct equivariance mod2 failed")
I64_2 = [[1 if i == j else 0 for j in range(64)] for i in range(64)]
if matmul_mod2(Acc2, Acc2) != I64_2 or matmul_mod2(Act2, Act2) != I64_2:
    raise SystemExit("Picard mod2 involution relation failed")
if matmul_mod2(Acc2, Act2) != matmul_mod2(Act2, Acc2):
    raise SystemExit("Picard mod2 commutation failed")
rank_M2 = rank_mod2(M2)
if rank_M2 != 56:
    raise SystemExit(f"expected mod2 boundary-image rank 56 from SNF [..,2,2], got {rank_M2}")
picu_mod2_dim = 64 - rank_M2
if picu_mod2_dim != 8:
    raise SystemExit("Pic(Ubar)/2 dimension mismatch")
picu_mod2_fixed = {
    "cc": quotient_fixed_dim_mod2(M2, Acc2),
    "ct": quotient_fixed_dim_mod2(M2, Act2),
    "cc_and_ct": quotient_fixed_dim_mod2(M2, Acc2, Act2),
}

# For every odd prime ell, 4 is invertible in Z_ell, so the rank-14 unit lattice
# splits canonically into the four V4 idempotent isotypic summands after Z_ell
# completion.  The multiplicities below therefore give the exact dimensions of
# the coefficient modules in which absolute-Galois H^1 character/residue terms
# must be computed.  They do NOT by themselves enumerate those global H^1 groups.
odd_primary_isotypic_inventory = {
    key: {
        "unit_rank_multiplicity": mult,
        "absolute_galois_term": "H^1(Q,(U_D tensor Q_ell/Z_ell)_isotypic)",
        "computed_group": False,
    }
    for key, mult in unit_mult.items()
}

certificate = {
    "schema": "STAGE33_03_UPIC_V4_INTEGRAL_ACTION_V2_COMPRESSED_EXPORT",
    "source_locks": {
        "br0a_artifact_id": BR0A_ARTIFACT_ID,
        "br0a_artifact_sha256": BR0A_ARTIFACT_SHA256,
        "br0a_certificate_sha256": BR0A_CERTIFICATE_SHA256,
        "raw_galois_action_sha256": raw["canonical_sha256"],
    },
    "complex": {
        "div_boundary_rank": 72,
        "picard_rank": 64,
        "unit_lattice_rank": 14,
        "pic_u_free_rank": 6,
        "pic_u_torsion": [2, 2],
        "pic_u_mod2_dimension": picu_mod2_dim,
    },
    "exact_checks": {
        "boundary_v4_relations": True,
        "integral_boundary_equivariance_checked_inside_magma": raw["boundary_equivariance_checked_inside_magma"],
        "independent_cc_equivariance_mod2": True,
        "independent_ct_equivariance_mod2": True,
        "picard_mod2_v4_relations": True,
        "unit_action_integral": True,
        "unit_v4_relations": True,
        "rational_character_exact_sequence_checked": True,
        "pic_u_mod2_dimension_matches_free_plus_2torsion": True,
    },
    "boundary_character_traces": div_traces,
    "picard_character_traces": pic_traces,
    "unit_character_traces": unit_traces,
    "pic_u_free_character_traces": picu_free_traces,
    "unit_basis_pivot_columns_1based": [x + 1 for x in unit_pivots],
    "unit_cc_matrix": int_rows(Ucc),
    "unit_ct_matrix": int_rows(Uct),
    "unit_v4_rational_character_multiplicities": unit_mult,
    "pic_u_free_v4_rational_character_multiplicities": picu_free_mult,
    "pic_u_mod2_fixed_dimensions": picu_mod2_fixed,
    "odd_primary_unit_isotypic_inventory": odd_primary_isotypic_inventory,
    "finite_v4_hypercohomology_completed": False,
    "absolute_odd_primary_h1_groups_completed": False,
    "two_primary_absolute_extension_completed": False,
    "pic_u_integral_torsion_action_fully_materialized": False,
    "br0b_all_primary_classes_accounted": False,
    "unit_closed": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
canonical = json.dumps(certificate, sort_keys=True, separators=(",", ":")).encode()
certificate["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
out = json.dumps(certificate, indent=2, sort_keys=True) + "\n"
(ROOT / "upic-v4-action-certificate.json").write_text(out, encoding="utf-8")
print(json.dumps({
    "success": True,
    "unit_v4_character_multiplicities": unit_mult,
    "pic_u_free_v4_character_multiplicities": picu_free_mult,
    "pic_u_mod2_fixed_dimensions": picu_mod2_fixed,
    "certificate_sha256": certificate["canonical_sha256"],
}, indent=2, sort_keys=True))
