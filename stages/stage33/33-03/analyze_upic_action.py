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


def download_br0a_artifact():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN required")
    req = urllib.request.Request(
        BR0A_ARTIFACT_URL,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "perfect-cuboid-stage33/1.5",
        },
    )
    opener = urllib.request.build_opener(StripCrossHostAuthRedirect())
    with opener.open(req, timeout=60) as resp:
        raw = resp.read()
    if hashlib.sha256(raw).hexdigest() != BR0A_ARTIFACT_SHA256:
        raise SystemExit("BR0A artifact digest mismatch")
    return raw


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


def perm_matrix(perm):
    P = sp.zeros(len(perm))
    for j, image in enumerate(perm):
        P[j, image - 1] = 1
    return P


def basis_action_on_row_lattice(K, P):
    pivots = list(K.rref()[1])
    if len(pivots) != K.rows:
        raise SystemExit("unit basis lost rank")
    minor = K[:, pivots]
    acted = K * P
    A = acted[:, pivots] * minor.inv()
    if any(sp.Rational(x).q != 1 for x in A):
        raise SystemExit("unit action not integral")
    A = sp.Matrix([[int(A[i, j]) for j in range(A.cols)] for i in range(A.rows)])
    if A * K != acted:
        raise SystemExit("unit action reconstruction failed")
    return A, pivots


def joint_multiplicities(A, B):
    I = sp.eye(A.rows)
    out = {}
    for ea in (1, -1):
        for eb in (1, -1):
            stacked = (A - ea * I).col_join(B - eb * I)
            out[f"cc{ea:+d}_ct{eb:+d}"] = A.rows - stacked.rank()
    if sum(out.values()) != A.rows:
        raise SystemExit(f"bad joint eigenspace dimensions {out}")
    return out


def mult_from_traces(rank, tcc, tct, tcct):
    out = {}
    for ea in (1, -1):
        for eb in (1, -1):
            num = rank + ea*tcc + eb*tct + ea*eb*tcct
            if num % 4:
                raise SystemExit(f"nonintegral V4 multiplicity {num}/4")
            out[f"cc{ea:+d}_ct{eb:+d}"] = num // 4
    if sum(out.values()) != rank or any(v < 0 for v in out.values()):
        raise SystemExit(f"invalid V4 multiplicities {out}")
    return out


def perm_trace(perm):
    return sum(j == image for j, image in enumerate(perm, 1))


raw_zip = download_br0a_artifact()
with zipfile.ZipFile(io.BytesIO(raw_zip)) as zf:
    cert_name = next((n for n in zf.namelist() if n.endswith("br0a-artifact-certificate.json")), None)
    if cert_name is None:
        raise SystemExit("BR0A certificate absent")
    cert_bytes = zf.read(cert_name)
if hashlib.sha256(cert_bytes).hexdigest() != BR0A_CERTIFICATE_SHA256:
    raise SystemExit("BR0A certificate hash mismatch")
br0a = json.loads(cert_bytes)
raw = json.loads((ROOT / "galois-action-raw.json").read_text(encoding="utf-8"))

# Stage33-02's primitive Picard basis and Magma's internal quotient basis are
# deliberately NOT identified.  The first compressed pilot caught this basis
# mismatch.  Only basis-invariant Picard traces are combined across them here.
# The rank-14 unit lattice lives canonically inside Div_D, so its integral V4
# action is recovered directly from the audited kernel and boundary permutation.
K = sp.Matrix(br0a["unit_divisor_relation_kernel_basis"])
if K.shape != (14, 72) or K.rank() != 14:
    raise SystemExit("bad audited unit kernel")
cc_perm = raw["boundary_perm_cc_1based"]
ct_perm = raw["boundary_perm_ct_1based"]
Pcc, Pct = perm_matrix(cc_perm), perm_matrix(ct_perm)
I72 = sp.eye(72)
if Pcc*Pcc != I72 or Pct*Pct != I72 or Pcc*Pct != Pct*Pcc:
    raise SystemExit("boundary action is not V4")

Ucc, pivots = basis_action_on_row_lattice(K, Pcc)
Uct, pivots2 = basis_action_on_row_lattice(K, Pct)
if pivots != pivots2:
    raise SystemExit("unit pivot mismatch")
I14 = sp.eye(14)
if Ucc*Ucc != I14 or Uct*Uct != I14 or Ucc*Uct != Uct*Ucc:
    raise SystemExit("unit action is not V4")
unit_mult = joint_multiplicities(Ucc, Uct)
unit_traces = {
    "id": 14,
    "cc": int(sp.trace(Ucc)),
    "ct": int(sp.trace(Uct)),
    "cct": int(sp.trace(Ucc*Uct)),
}

div_traces = {
    "id": 72,
    "cc": perm_trace(cc_perm),
    "ct": perm_trace(ct_perm),
    "cct": perm_trace([ct_perm[cc_perm[j]-1] for j in range(72)]),
}
pic_traces = {k: int(v) for k, v in raw["picard_character_traces"].items()}
if pic_traces["id"] != 64:
    raise SystemExit("Picard trace lock failed")

# Over Q, torsion disappears and the exact sequence
# 0 -> U_D -> Div_D -> Pic(Sbar) -> Pic(Ubar) -> 0
# makes the character additive.  Hence the six-dimensional free representation
# of Pic(Ubar) is determined without a change-of-basis matrix.
picu_traces = {
    g: pic_traces[g] - div_traces[g] + unit_traces[g]
    for g in ("id", "cc", "ct", "cct")
}
if picu_traces["id"] != 6:
    raise SystemExit(f"Pic(Ubar)_Q trace rank mismatch {picu_traces}")
picu_mult = mult_from_traces(6, picu_traces["cc"], picu_traces["ct"], picu_traces["cct"])

# For every odd ell, |V4|=4 is invertible over Z_ell, so the unit coefficient
# module splits into the four exact sign-isotypic summands with these ranks.
# This is a coefficient-module inventory only: the corresponding absolute
# Galois H^1 groups are not inferred merely from their ranks.
odd_inventory = {
    key: {
        "unit_rank_multiplicity": mult,
        "coefficient_module": f"(U_D tensor Q_ell/Z_ell)_{key}",
        "absolute_h1_computed": False,
    }
    for key, mult in unit_mult.items()
}

certificate = {
    "schema": "STAGE33_03_UPIC_V4_INTEGRAL_ACTION_V3_BASIS_FIREWALL",
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
    "boundary_character_traces": div_traces,
    "picard_character_traces_basis_invariant": pic_traces,
    "unit_character_traces": unit_traces,
    "pic_u_free_character_traces": picu_traces,
    "unit_basis_pivot_columns_1based": [p+1 for p in pivots],
    "unit_cc_matrix": int_rows(Ucc),
    "unit_ct_matrix": int_rows(Uct),
    "unit_v4_rational_character_multiplicities": unit_mult,
    "pic_u_free_v4_rational_character_multiplicities": picu_mult,
    "odd_primary_unit_isotypic_inventory": odd_inventory,
    "exact_checks": {
        "boundary_v4_relations": True,
        "integral_boundary_equivariance_checked_inside_magma": raw["boundary_equivariance_checked_inside_magma"],
        "unit_action_integral": True,
        "unit_v4_relations": True,
        "rational_character_exact_sequence_checked": True,
        "magma_picard_basis_not_identified_with_stage32_primitive_basis": True,
    },
    "superseded_invalid_cross_basis_mod2_comparison": True,
    "next_exact_leaf": "L33-03-PICU-INTEGRAL-TORSION-ACTION-AND-V4-HYPERCOHOMOLOGY",
    "pic_u_integral_torsion_action_fully_materialized": False,
    "finite_v4_hypercohomology_completed": False,
    "absolute_odd_primary_h1_groups_completed": False,
    "two_primary_absolute_extension_completed": False,
    "br0b_all_primary_classes_accounted": False,
    "unit_closed": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
canonical = json.dumps(certificate, sort_keys=True, separators=(",", ":")).encode()
certificate["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "upic-v4-action-certificate.json").write_text(
    json.dumps(certificate, indent=2, sort_keys=True)+"\n", encoding="utf-8"
)
print(json.dumps({
    "success": True,
    "unit_v4_character_multiplicities": unit_mult,
    "pic_u_free_v4_character_multiplicities": picu_mult,
    "unit_traces": unit_traces,
    "pic_u_free_traces": picu_traces,
    "next_exact_leaf": certificate["next_exact_leaf"],
    "certificate_sha256": certificate["canonical_sha256"],
}, indent=2, sort_keys=True))
