#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT = HERE / "post1648ap-factor-pair-birational-conductor-demand.json"
NOTE = HERE / "post1648ap-factor-pair-birational-conductor-demand-source-note.md"
AO = HERE / "post1648ao-special-fibre-hurwitz-budget.json"
AM = HERE / "post1648am-beauville-fibration-picard-source-lock.json"
AN = HERE / "post1648an-a1-strict-transform-delta-feasibility.json"


def canonical_sha(payload: dict) -> str:
    body = dict(payload)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    cert = json.loads(CERT.read_text())
    got = canonical_sha(cert)
    if got != cert["canonical_sha256_without_this_field"]:
        raise SystemExit(f"AP canonical mismatch: {got}")
    note_sha = hashlib.sha256(NOTE.read_bytes()).hexdigest()
    if note_sha != cert["source_locks"]["source_note_sha256"]:
        raise SystemExit(f"AP source note moved: {note_sha}")

    ao = json.loads(AO.read_text())
    am = json.loads(AM.read_text())
    an = json.loads(AN.read_text())
    if ao["canonical_sha256_without_this_field"] != cert["parent"]["ao_canonical_sha256"]:
        raise SystemExit("AO canonical moved")
    if am["canonical_sha256_without_this_field"] != cert["parent"]["am_canonical_sha256"]:
        raise SystemExit("AM canonical moved")
    if an["canonical_sha256_without_this_field"] != cert["parent"]["an_canonical_sha256"]:
        raise SystemExit("AN canonical moved")

    degrees = sorted(int(x) for x in am["retained_picard_replay"]["projection_degrees_unordered"])
    if degrees != [81, 105] or degrees != sorted(cert["factor_pair_quotient"]["carrier_factor_degrees_unordered"]):
        raise SystemExit("factor degrees moved")
    group_order = int(cert["factor_pair_quotient"]["residual_group_order"])
    gdeg = math.gcd(*degrees)
    pair_degree = math.gcd(group_order, gdeg)
    if (group_order, gdeg, pair_degree) != (8, 3, 1):
        raise SystemExit("factor-pair birationality arithmetic moved")
    if not cert["factor_pair_quotient"]["pair_map_birational"] or cert["factor_pair_quotient"]["pair_map_generic_degree"] != 1:
        raise SystemExit("pair-map birational credit moved")

    a, b = degrees
    p_img = (a - 1) * (b - 1)
    g_norm = 1
    delta_img = p_img - g_norm
    C2 = int(cert["v6_strict_transform"]["self_intersection"])
    KC = int(cert["v6_strict_transform"]["canonical_intersection"])
    p_c = 1 + (C2 + KC) // 2
    delta_c = p_c - g_norm
    conductor = p_img - p_c
    if (p_img, delta_img, p_c, delta_c, conductor) != (8320, 8319, 473, 472, 7847):
        raise SystemExit("AP genus/conductor arithmetic moved")
    if cert["image_curve"]["arithmetic_genus"] != p_img or cert["image_curve"]["total_delta_defect"] != delta_img:
        raise SystemExit("image genus certificate moved")
    if cert["v6_strict_transform"]["arithmetic_genus"] != p_c or cert["v6_strict_transform"]["intrinsic_delta_defect"] != delta_c:
        raise SystemExit("V6 strict-transform genus certificate moved")
    if cert["conductor_demand"]["required_additional_conductor_length"] != conductor or cert["conductor_demand"]["delta_defect_difference"] != conductor:
        raise SystemExit("conductor demand moved")
    if any(cert["firewalls"].values()):
        raise SystemExit("AP firewall moved")
    if cert["decision"]["v6_carrier_excluded"]:
        raise SystemExit("AP must not exclude V6")

    print("PASS_STAGE32_POST1648AP_FACTOR_PAIR_BIRATIONAL_CONDUCTOR_DEMAND")
    print(cert["canonical_sha256_without_this_field"])
    print(json.dumps({"pair_degree": pair_degree, "image_pa": p_img, "required_conductor": conductor}, sort_keys=True))


if __name__ == "__main__":
    main()
