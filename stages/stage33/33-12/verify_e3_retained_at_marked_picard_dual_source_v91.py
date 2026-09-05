#!/usr/bin/env python3
"""Locally replay the retained V91 marked Picard-dual source binding."""
from __future__ import annotations

import base64
import hashlib
import json
import runpy
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
LEGACY = STAGE / "33-07"
MARKED = STAGE / "33-09"
CERT = HERE / "e3-retained-at-marked-picard-dual-source-v91.json"
V89 = HERE / "e3-proper14-dual-to-discriminant-quotient-bridge-v89.json"
COMPACT = LEGACY / "picard-discriminant-compact.json"
ENDPOINT = LEGACY / "retained-q256-geometric-sign-endpoint.json"
OLD_BASE = LEGACY / "picard_base_rows_retained.py"
OLD_SIGNS = LEGACY / "picard_coordinate_sign_rows_retained.py"
BRIDGE = MARKED / "marked-picard-basis-bridge-certified.json"
PRODUCER = HERE / "materialize_e3_retained_at_marked_picard_dual_source_v91.py"

CERT_SHA = "729f296c1495d9ba600b085a6e9a5a0b53f8968a7997af4774fa11dc2d0215e9"
V89_SHA = "26bf699fd92e261e1ae40066ad0fd5aece9cb896f28a385367786de1d0460639"
COMPACT_SHA = "4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0"
ENDPOINT_SHA = "19d59e89b87d49681ae8b1b165085d529bef64b40c2d5ab6fe692a6b899fb061"
BRIDGE_SHA = "039e3792e950ac5bf94adf6538c229640da231000a5e1b159a80e2323a812a92"
OLD_BASE_SHA = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
OLD_SIGN_SHA = "5cd64ca89ee9f3ec76d275bc4082349764ac8a5cb4647a9bb9a4eaf267b76ab9"
MODS = [2] * 4 + [4] * 6 + [8] * 4
TARGET = [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path: Path, expected: str) -> dict:
    x = json.loads(path.read_text(encoding="utf-8"))
    body = dict(x)
    claimed = body.pop("canonical_sha256", None)
    if claimed != expected or csha(body) != expected:
        raise SystemExit(f"canonical lock moved: {path}")
    return x


def mm(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    if not A or not B or len(A[0]) != len(B):
        raise SystemExit("matrix product shape mismatch")
    out = [[0] * len(B[0]) for _ in range(len(A))]
    nz = [[(j, int(x)) for j, x in enumerate(row) if x] for row in B]
    for i, row in enumerate(A):
        for k, a in enumerate(row):
            if a:
                for j, b in nz[k]:
                    out[i][j] += int(a) * b
    return out


def transpose(A: list[list[int]]) -> list[list[int]]:
    return [list(r) for r in zip(*A)]


def induced(R: list[list[int]], C: list[list[int]], G: list[list[int]]) -> list[list[int]]:
    raw = mm(mm(R, transpose(G)), C)
    return [[int(x) % MODS[j] for j, x in enumerate(row)] for row in raw]


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


cert = load_locked(CERT, CERT_SHA)
v89 = load_locked(V89, V89_SHA)
compact = load_locked(COMPACT, COMPACT_SHA)
endpoint = load_locked(ENDPOINT, ENDPOINT_SHA)
bridge = load_locked(BRIDGE, BRIDGE_SHA)

if cert["schema"] != "stage33.e3.retained_at_marked_picard_dual_source.v91":
    raise SystemExit("V91 schema moved")
if cert["source_locks"]["v89_canonical_sha256"] != V89_SHA:
    raise SystemExit("V91->V89 lock moved")
if cert["source_locks"]["picard_discriminant_compact_sha256"] != COMPACT_SHA:
    raise SystemExit("V91 compact discriminant lock moved")
if cert["source_locks"]["retained_q256_endpoint_sha256"] != ENDPOINT_SHA:
    raise SystemExit("V91 q256 endpoint lock moved")
if cert["source_locks"]["stage33_09_marked_picard_bridge_sha256"] != BRIDGE_SHA:
    raise SystemExit("V91 marked bridge lock moved")
if cert["historical_common_smith_replay"]["discriminant_moduli"] != MODS:
    raise SystemExit("V91 discriminant moduli moved")
if compact["discriminant_moduli"] != MODS or endpoint["discriminant_moduli"] != MODS:
    raise SystemExit("retained discriminant moduli moved")

# Decode the nonexpiring compact replay payload and verify its own digest.
t = cert["marked_picard_dual_transport"]
if t["payload_codec"] != "base85(zlib(canonical-json))":
    raise SystemExit("V91 payload codec moved")
raw = zlib.decompress(base64.b85decode(t["payload_b85_zlib"].encode()))
if hashlib.sha256(raw).hexdigest() != t["payload_uncompressed_sha256"]:
    raise SystemExit("V91 retained transport payload hash regression")
payload = json.loads(raw)
R = payload["historical_R_mod8_14x64"]
C = payload["historical_C_mod8_64x14"]
b8 = payload["b8"]
Rm = payload["marked_R_mod8_14x64"]
Cm = payload["marked_C_mod8_64x14"]
if len(R) != 14 or any(len(r) != 64 for r in R):
    raise SystemExit("historical R shape moved")
if len(C) != 64 or any(len(r) != 14 for r in C):
    raise SystemExit("historical C shape moved")
if len(Rm) != 14 or any(len(r) != 64 for r in Rm):
    raise SystemExit("marked R shape moved")
if len(Cm) != 64 or any(len(r) != 14 for r in Cm):
    raise SystemExit("marked C shape moved")
I14 = [[int(i == j) for j in range(14)] for i in range(14)]
if [[x % 8 for x in row] for row in mm(R, C)] != I14:
    raise SystemExit("historical retained Smith R*C regression")
if [[x % 8 for x in row] for row in mm(Rm, Cm)] != I14:
    raise SystemExit("marked retained Smith R*C regression")
if b8 != compact["discriminant_bilinear_numerator_over_8_reduced"]:
    raise SystemExit("retained Smith B8 differs from compact discriminant authority")

# Replay the historical mixed basis against independently retained q256 actions.
old = runpy.run_path(str(OLD_BASE))["load"]()
signs = runpy.run_path(str(OLD_SIGNS))["load"]()
if old["canonical_sha256"] != OLD_BASE_SHA or signs["canonical_sha256"] != OLD_SIGN_SHA:
    raise SystemExit("retained historical Picard sources moved")
old_cc = [[int(x) for x in row] for row in old["picard_action_cc_64x64"]]
old_ct = [[int(x) for x in row] for row in old["picard_action_ct_64x64"]]
order = list(signs["coordinate_order"])
if order != ["a1", "a2", "a3", "b1", "b2", "b3", "c"]:
    raise SystemExit("historical sign order moved")
old_signs = [
    [[int(x) for x in row] for row in signs["picard_actions_64x64"][name]]
    for name in order
]
if induced(R, C, old_cc) != endpoint["cc_action_mixed_moduli"]:
    raise SystemExit("local V91 replay failed cc")
if induced(R, C, old_ct) != endpoint["ct_action_mixed_moduli"]:
    raise SystemExit("local V91 replay failed ct")
if [induced(R, C, G) for G in old_signs] != endpoint["sign_actions_mixed_moduli"]:
    raise SystemExit("local V91 replay failed seven signs")

# Replay the marked-basis transport with the exact Stage33-09 bridge.
b = bridge["basis_bridge"]
if b["from"] != "upstream primitive INDLIST known-class basis" or b["to"] != "historical retained Magma Basis(Pic)":
    raise SystemExit("Stage33-09 bridge orientation moved")
B = [[int(x) for x in row] for row in b["matrix_64x64"]]
Binv = [[int(x) for x in row] for row in b["inverse_64x64"]]
I64 = [[int(i == j) for j in range(64)] for i in range(64)]
if mm(B, Binv) != I64 or mm(Binv, B) != I64:
    raise SystemExit("Stage33-09 marked bridge inverse regression")
want_Rm = [[x % 8 for x in row] for row in mm(R, transpose(B))]
want_Cm = [[x % 8 for x in row] for row in mm(transpose(Binv), C)]
if Rm != want_Rm or Cm != want_Cm:
    raise SystemExit("V91 marked dual transport matrix orientation regression")

# Recompute the exact e3 target source binding and its inverse roundtrip.
if v89["e3_transport"]["retained_at_mod2_quotient_coordinate_f2"] != TARGET:
    raise SystemExit("V89 target moved")
old_target = [sum(TARGET[i] * R[i][j] for i in range(14)) % 8 for j in range(64)]
marked_target = [sum(TARGET[i] * Rm[i][j] for i in range(14)) % 8 for j in range(64)]
source = cert["e3_source_binding"]
if source["historical_picard_dual_numerator_mod8_64"] != old_target:
    raise SystemExit("V91 historical e3 target numerator regression")
if source["marked_indlist_picard_dual_numerator_mod8_64"] != marked_target:
    raise SystemExit("V91 marked e3 target numerator regression")
decoded = mm([marked_target], Cm)[0]
decoded = [int(decoded[j]) % MODS[j] for j in range(14)]
if decoded != TARGET:
    raise SystemExit("V91 marked e3 target mixed-coordinate roundtrip failed")
if source["retained_at_mod2_quotient_support_one_based"] != [1, 8, 10]:
    raise SystemExit("V91 retained support moved")
if not source["source_bound_to_actual_140_class_marking"]:
    raise SystemExit("V91 marked source binding flag moved")
if source["object_type"] != "marked Picard dual-lattice/discriminant class, not an integral Picard divisor":
    raise SystemExit("V91 object-type firewall moved")

# Lock the one-time evidence acquisition without putting remote CAS in hot CI.
evidence = cert["retained_evidence"]
if evidence != {
    "artifact_id": 9966920497,
    "artifact_name": "stage33-v91-marked-picard-dual-source",
    "artifact_zip_sha256": "471ff4b840717c673beb54a9aaf5ae93db98469247f7546e3d6f4d0e66b8252d",
    "full_remote_certificate_canonical_sha256": "20256a3ca66589a09226f223c3e1ea954c1f3cda819542e3b9ad924a3677cd47",
    "producer_git_blob_sha1": "ef5106a2f19e84c91e5ac52989e0d71cfb812ce2",
    "producer_job_id": 101284099329,
    "producer_run_id": 33957769427,
}:
    raise SystemExit("V91 retained acquisition evidence moved")
if git_blob_sha1(PRODUCER) != evidence["producer_git_blob_sha1"]:
    raise SystemExit("V91 producer blob differs from retained acquisition lock")
if cert["source_locks"]["historical_common_smith_submitted_code_sha256"] != "fc06b21f6c54f102e5dd7e510be1b5dc92c1a4b9750e6445cdeb70637c31eefa":
    raise SystemExit("historical common-Smith submitted-code lock moved")

cons = cert["exact_consequence"]
if not cons["retained_support_1_8_10_source_bound_to_marked_picard_dual_class"]:
    raise SystemExit("V91 source-binding consequence moved")
if not cons["all_14_retained_mixed_smith_generators_source_bound_to_marked_picard_dual_basis"]:
    raise SystemExit("V91 all-generator source-binding consequence moved")
for key in (
    "literal_picard_divisor_materialized",
    "literal_kummer_function_materialized",
    "literal_cech_seed_materialized",
    "complete_residue_audit_materialized",
    "genuine_full_surface_h2_mu2_lift_for_e3",
):
    if cons[key]:
        raise SystemExit(f"V91 credit firewall violated: {key}")
f = cert["credit_firewall"]
if f["stage33_progress"] != "6/11":
    raise SystemExit("Stage33 progress moved")
for key in (
    "stage33_12_closed_exact",
    "stage33_13_released",
    "receiver_credit",
    "theorem_credit",
    "endpoint_credit",
    "merge_allowed",
):
    if f[key]:
        raise SystemExit(f"V91 credit firewall violated: {key}")

print(json.dumps({
    "success": True,
    "marker": "V91_E3_RETAINED_AT_MARKED_PICARD_DUAL_SOURCE_BINDING_COMPLETE",
    "certificate_sha256": CERT_SHA,
    "full_remote_certificate_sha256": evidence["full_remote_certificate_canonical_sha256"],
    "producer_run_id": evidence["producer_run_id"],
    "retained_support_one_based": [1, 8, 10],
    "marked_dual_numerator_mod8_64": marked_target,
    "literal_picard_divisor_materialized": False,
    "next_exact_leaf": cert["next_exact_leaf"],
}, sort_keys=True))
