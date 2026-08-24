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
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_decomp

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
            "User-Agent": "perfect-cuboid-stage33/1.3",
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
    # K has independent rows. Pick pivot columns giving an invertible square minor.
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
Acc = sp.Matrix(raw["picard_cc_matrix"])
Act = sp.Matrix(raw["picard_ct_matrix"])
if Acc.shape != (64, 64) or Act.shape != (64, 64):
    raise SystemExit("unexpected Picard action shape")

I72 = sp.eye(72)
I64 = sp.eye(64)
if Pcc * Pcc != I72 or Pct * Pct != I72 or Pcc * Pct != Pct * Pcc:
    raise SystemExit("boundary actions do not realize V4")
if Acc * Acc != I64 or Act * Act != I64 or Acc * Act != Act * Acc:
    raise SystemExit("Picard actions do not realize V4")
if Pcc * M != M * Acc:
    raise SystemExit("cc equivariance failure for Div_D -> Pic")
if Pct * M != M * Act:
    raise SystemExit("ct equivariance failure for Div_D -> Pic")

Ucc, unit_pivots = basis_action_on_row_lattice(K, Pcc)
Uct, unit_pivots2 = basis_action_on_row_lattice(K, Pct)
if unit_pivots != unit_pivots2:
    raise SystemExit("unit pivot choices unexpectedly differ")
I14 = sp.eye(14)
if Ucc * Ucc != I14 or Uct * Uct != I14 or Ucc * Uct != Uct * Ucc:
    raise SystemExit("unit-lattice action does not realize V4")
unit_mult = joint_eigenspace_multiplicities(Ucc, Uct)

# Exact quotient-coordinate adapter for Pic(Ubar)=Z^64/row(M).
D, S, T = smith_normal_decomp(M, domain=ZZ)
if D != S * M * T:
    raise SystemExit("Smith decomposition identity failed")
rank = M.rank()
diag = [abs(int(D[i, i])) for i in range(rank)]
if [d for d in diag if d != 1] != [2, 2]:
    raise SystemExit(f"unexpected Pic(Ubar) torsion invariants: {diag}")
Tinv = T.inv()
if any(sp.Rational(Tinv[i, j]).q != 1 for i in range(64) for j in range(64)):
    raise SystemExit("Smith right transform inverse nonintegral")
Acc_snf = Tinv * Acc * T
Act_snf = Tinv * Act * T
if any(sp.Rational(x).q != 1 for x in list(Acc_snf) + list(Act_snf)):
    raise SystemExit("quotient-coordinate action nonintegral")

torsion_indices = [i for i, d in enumerate(diag) if d == 2]
free_indices = list(range(rank, 64))
q_indices = torsion_indices + free_indices
if len(torsion_indices) != 2 or len(free_indices) != 6:
    raise SystemExit("unexpected quotient generator count")


def quotient_action(A_snf):
    rows = []
    for src_pos, src in enumerate(q_indices):
        r = []
        # target torsion coordinates are reduced mod 2
        for tgt in torsion_indices:
            r.append(int(A_snf[src, tgt]) % 2)
        # target free coordinates are integral
        free_part = [int(A_snf[src, tgt]) for tgt in free_indices]
        if src_pos < 2 and any(free_part):
            raise SystemExit("torsion quotient generator maps to nonzero free part")
        r.extend(free_part)
        rows.append(r)
    return rows

Qcc = quotient_action(Acc_snf)
Qct = quotient_action(Act_snf)

# The odd-primary absolute-character inventory depends only on U_D away from 2.
# Since V4 has order 4, its Q-representation splits into the four sign characters.
# Each multiplicity m_chi corresponds parametrically to m_chi copies of
# H^1(Q, (Q/Z)_{odd}(chi)); no claim is made here that the 2-primary extension
# data have already been computed.
odd_inventory = {
    key: {
        "multiplicity": mult,
        "family": f"H^1(Q,(Q/Z)_odd({key}))^{mult}" if mult else "0",
    }
    for key, mult in unit_mult.items()
}

certificate = {
    "schema": "STAGE33_03_UPIC_V4_INTEGRAL_ACTION_V1",
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
    },
    "exact_checks": {
        "boundary_v4_relations": True,
        "picard_v4_relations": True,
        "differential_cc_equivariant": True,
        "differential_ct_equivariant": True,
        "unit_action_integral": True,
        "unit_v4_relations": True,
        "pic_u_smith_adapter_exact": True,
    },
    "unit_basis_pivot_columns_1based": [x + 1 for x in unit_pivots],
    "unit_cc_matrix": int_rows(Ucc),
    "unit_ct_matrix": int_rows(Uct),
    "unit_v4_rational_character_multiplicities": unit_mult,
    "odd_primary_absolute_character_inventory": odd_inventory,
    "pic_u_quotient_generator_order": ["torsion_2_a", "torsion_2_b", "free_1", "free_2", "free_3", "free_4", "free_5", "free_6"],
    "pic_u_cc_action_mixed_matrix": Qcc,
    "pic_u_ct_action_mixed_matrix": Qct,
    "finite_v4_hypercohomology_completed": False,
    "two_primary_absolute_extension_completed": False,
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
    "pic_u_torsion": [2, 2],
    "pic_u_free_rank": 6,
    "certificate_sha256": certificate["canonical_sha256"],
}, indent=2, sort_keys=True))
