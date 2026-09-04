#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT_PATH = HERE / "post1550-b3-v4-torsor-normalizer.json"
CONTROLLER = ROOT / "stages/stage32/controller.json"

EXPECTED_CANONICAL = "1225ca34034f1f1dacb2f3e1f46e7f3d15a6008a5e6b03960109f7bc992b5e95"
EXPECTED_BASE = "bdd707e52ded061014bfbb6158762e8b997e7a38"


def fail(msg: str) -> None:
    raise SystemExit(msg)


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def canonical_sha(doc: dict) -> str:
    body = dict(doc)
    claimed = body.pop("canonical_sha256_without_this_field")
    calc = hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    if claimed != calc:
        fail(f"canonical mismatch: {claimed} != {calc}")
    return calc


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def matmul_mod2(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    n = len(a)
    m = len(b[0])
    k = len(b)
    return [
        [sum(a[i][t] * b[t][j] for t in range(k)) % 2 for j in range(m)]
        for i in range(n)
    ]


def main() -> None:
    cert = load_json(CERT_PATH)
    if cert["schema"] != "STAGE32_POST1550_B3_V4_TORSOR_NORMALIZER_V1":
        fail("certificate schema moved")
    if cert["status"] != "EXACT_AMBIENT_V4_NORMALIZER_PENDING_HOSTILE_AUDIT":
        fail("certificate status moved")
    if canonical_sha(cert) != EXPECTED_CANONICAL:
        fail("certificate canonical moved")
    if cert["base_main_sha"] != EXPECTED_BASE:
        fail("base main moved")

    locked = {}
    for name, lock in cert["source_locks"].items():
        path = ROOT / lock["path"]
        if not path.is_file():
            fail(f"missing source lock: {name}")
        got = blob_sha1(path)
        if got != lock["blob_sha1"]:
            fail(f"source blob drift: {name}: {got}")
        if "canonical_sha256" in lock:
            doc = load_json(path)
            if canonical_sha(doc) != lock["canonical_sha256"]:
                fail(f"source canonical drift: {name}")
            locked[name] = doc
        else:
            locked[name] = path.read_text()

    adapter = locked["retained_v4_plane_adapter"]
    b3src = locked["single_b3_reduction"]
    relative = locked["relative_v4_coupling"]
    boundary = locked["post1550_boundary_note"]
    note = locked["source_note"]

    if adapter["retained_F2_4_adapter"]["ordered_basis"] != cert["retained_basis"]:
        fail("retained basis mismatch")
    if adapter["retained_F2_4_adapter"]["W_basis_vectors"] != cert["v4_character_plane"]["basis_vectors"]:
        fail("W basis mismatch")
    if adapter["retained_F2_4_adapter"]["W_dimension"] != 2:
        fail("W dimension moved")
    if adapter["retained_F2_4_adapter"]["W_equals_kernel_r_mod2"] is not True:
        fail("W=ker(r mod2) anchor moved")

    b3 = b3src["principal_automorphisms"]["b3_mod2_4x4"]
    if b3 != cert["principal_b3"]["matrix_mod2"]:
        fail("b3 matrix mismatch")
    if b3src["retained_basis"] != cert["retained_basis"]:
        fail("b3 source basis does not match W basis")

    # W is exactly the final two coordinate axes. Both off-diagonal 2x2
    # blocks vanish, so stability is convention-independent (row/column).
    if any(b3[i][j] for i in range(2) for j in range(2, 4)):
        fail("b3 mixes W into the first coordinate plane")
    if any(b3[i][j] for i in range(2, 4) for j in range(2)):
        fail("b3 mixes the first coordinate plane into W")
    restriction = [row[2:4] for row in b3[2:4]]
    if restriction != cert["principal_b3"]["restriction_to_W"]:
        fail("b3 restriction to W mismatch")

    B2 = matmul_mod2(restriction, restriction)
    B3 = matmul_mod2(B2, restriction)
    if B3 != [[1, 0], [0, 1]]:
        fail("b3 restriction does not have order dividing 3")
    if restriction == [[1, 0], [0, 1]]:
        fail("b3 restriction unexpectedly identity")
    det = (restriction[0][0] * restriction[1][1] -
           restriction[0][1] * restriction[1][0]) % 2
    if det != 1:
        fail("b3 restriction is not invertible")
    if cert["principal_b3"]["restriction_order"] != 3:
        fail("certificate order moved")
    if cert["principal_b3"]["W_invariant"] is not True:
        fail("certificate W invariance moved")

    rv4 = relative["relative_v4_coupling"]
    if rv4["base_torsor"] != "Z=X(8) -> C0=Z/H, H ~= F2^2, connected finite etale degree 4":
        fail("relative V4 base torsor anchor moved")
    if rv4["character_plane"] != "W=image(H^* -> H^1(C0,F2))":
        fail("relative V4 character plane anchor moved")
    if rv4["W_dimension"] != 2:
        fail("relative V4 dimension moved")

    normalizer = cert["torsor_normalizer"]
    for key in (
        "b3_pullback_preserves_cover_class_up_to_Aut_H",
        "semilinear_lift_exists",
        "same_lift_on_both_factors_normalizes_H_diag",
        "diagonal_b3_lift_to_X_exists",
    ):
        if normalizer[key] is not True:
            fail(f"ambient normalizer theorem flag moved: {key}")
    if normalizer["ambient_relative_v4_torsor"] != "X=(Z x Z)/H_diag":
        fail("ambient relative torsor moved")
    if normalizer["covers"] != "b3 x b3 on C0 x C0":
        fail("ambient lift base action moved")

    # #1550 explicitly requires a semantic bridge beyond an ambient candidate.
    if "ambient candidate without this semantic bridge is insufficient" not in boundary:
        fail("#1550 ambient-vs-carrier firewall moved")
    if "exact quotient-normalizer/lift identity" not in boundary:
        fail("#1550 quotient-normalizer re-entry condition moved")

    decision = cert["decision"]
    if decision["result"] != "PASS_EXACT_AMBIENT_V4_TORSOR_NORMALIZER":
        fail("decision moved")
    if decision["ambient_quotient_normalizer_gate_closed_positive"] is not True:
        fail("ambient normalizer positive gate missing")
    if decision["next_exact_leaf"] != "PROVE_CARRIER_OR_CORRESPONDENCE_INVARIANCE_UNDER_THE_AMBIENT_B3_LIFT":
        fail("next exact leaf moved")
    for key in (
        "intrinsic_carrier_equivariance_proved",
        "correspondence_invariance_proved",
        "actual_T_b3_commutation_proved",
        "actual_T_b3_noncommutation_proved",
        "Q602_excluded",
        "O210_excluded",
        "O212_plus_advance_allowed",
        "controller_change_authorized",
    ):
        if decision[key] is not False:
            fail(f"decision firewall leaked: {key}")

    if any(cert["firewalls"].values()):
        fail("credit firewall leaked")

    for marker in (
        "B3_NORMALIZES_RETAINED_V4_CHARACTER_PLANE=true",
        "DIAGONAL_B3_LIFT_TO_RELATIVE_V4_TORSOR_X=true",
        "PROVE_CARRIER_OR_CORRESPONDENCE_INVARIANCE_UNDER_THE_AMBIENT_B3_LIFT",
        "does **not** by itself prove",
        "The Stage32 controller remains unchanged.",
    ):
        if marker not in note:
            fail(f"source-note marker missing: {marker}")

    ctl = load_json(CONTROLLER)
    if ctl["schema"] != "STAGE32_LOWGENUS_PICARD_CONTROLLER_V247_POST1520_Q602_RETAINED_GEOMETRY_18_TO_18_AUDITED":
        fail("controller schema moved")
    if ctl["stage"] != 32 or ctl["stage32_closed"] is not False:
        fail("controller lifecycle moved")
    fixed = ctl["fixed_target"]
    if (fixed["row_id"], fixed["O"], fixed["qprime"], fixed["Q"]) != ("g1-d186", 210, 4, 602):
        fail("controller fixed target moved")

    print("PASS post1550 ambient b3 V4 torsor normalizer")
    print(f"canonical={EXPECTED_CANONICAL}")
    print("W=span(re1,re2)=ker(r mod2), b3(W)=W, b3|W order=3")
    print("ambient diagonal b3 lift to X=PASS")
    print("carrier/correspondence invariance=UNRESOLVED [T,b3]=UNRESOLVED")
    print("Q602/O210=OPEN O212+=BLOCKED controller=UNCHANGED")


if __name__ == "__main__":
    main()
