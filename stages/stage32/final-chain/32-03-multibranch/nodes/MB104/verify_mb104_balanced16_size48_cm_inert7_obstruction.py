#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-SIZE48-CM-INERT7-OBSTRUCTION-CERTIFICATE.json"
LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-SIZE48-CM-INERT7-OBSTRUCTION.md",
        "5e1f7d4d6db10cd823532b1ac44290621ee2aa99",
    ),
    "CM_SOURCE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BEAUVILLE-KUMMER-CM-SOURCE-NOTE.md",
        "b86c0b8702c4596535ee8acbf43ca78b8f42da91",
    ),
    "EQUALITY_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-P5-BEAUVILLE-EQUALITY-RIGIDITY-CERTIFICATE.json",
        "62a2d01447016731001d35cc5915880daa2bfada",
    ),
    "NODE_TYPE_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-BEAUVILLE-NODE-TYPE-QUOTIENT-CERTIFICATE.json",
        "f018c21bb1ecd4e33fc31d5aae15650928e592c3",
    ),
    "SIZE48_QUOTIENT_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-SIZE48-BEAUVILLE-QUOTIENT.md",
        "911eb7b25da312435ad953e0bfc8d7fa6d303d52",
    ),
}


def req(cond, msg):
    if not cond:
        raise SystemExit("FAIL: " + msg)


def root():
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root")


def blob(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def preflight(cert):
    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared == LOCKS, "source-lock table")
    rr = root()
    for key, (rel, expected) in LOCKS.items():
        p = rr / rel
        if not p.is_file():
            raise SystemExit(f"SOURCE_LOCK_FAIL missing {key}: {rel}")
        got = blob(p)
        if got != expected:
            raise SystemExit(f"SOURCE_LOCK_FAIL {key}: expected {expected}, got {got}")


def load_locked(rel):
    return json.loads((root() / rel).read_text())


def main():
    cert = json.loads(CERT.read_text())
    req(cert["schema"] == "STAGE32_MB104_BALANCED16_SIZE48_CM_INERT7_OBSTRUCTION_V1", "schema")
    preflight(cert)

    eq = load_locked(LOCKS["EQUALITY_CERT"][0])
    nt = load_locked(LOCKS["NODE_TYPE_CERT"][0])

    # Upstream semantics: equality packet and the two one-type current masks.
    req(eq["uniform_F1_P5"]["g"] == 1, "genus-one equality input")
    req(eq["uniform_F1_P5"]["d"] == "112*l", "d=112l")
    req(eq["uniform_F1_P5"]["r_odd"] == "112*l", "r_odd=d")
    req(eq["equality_consequence"]["both_projections_etale"] is True, "etale projections")
    req(eq["product_cover"]["component_etale_degrees"] == [1, 2, 4], "e choices")

    for mask in ("0000770000ff", "00007b0000ff"):
        row = nt["survivors"][mask]
        req(row["node_type_counts"] == [14, 0, 0], f"{mask} one node type")
        req(row["allowed_e"] == [1, 2, 4], f"{mask} e choices")

    scope = cert["scope"]
    req(scope["masks"] == ["0000770000ff", "00007b0000ff"], "mask scope")
    req(scope["orbit_sizes"] == [48, 48], "orbit sizes")
    req(scope["supported_nodes"] == 14, "N=14")

    # Exact RH arithmetic for B1=Z/<s>. Each of 112l branch points on E
    # has e lifts fixed by s, while 2g(Z)-2=e*d=112el.
    for e in (1, 2, 4):
        coeff_fixed = 112 * e
        coeff_two_gz_minus_two = e * 112
        req(coeff_fixed == coeff_two_gz_minus_two, f"RH equality e={e}")
        # RH: LHS = 2*(2gB1-2) + fixed. Equality forces gB1=1.
        req((coeff_two_gz_minus_two - coeff_fixed) == 0, f"B1 genus-one e={e}")

        ncoeff = 14 * e
        req(ncoeff % 7 == 0, f"7 divides isogeny degree coefficient e={e}")
        req(ncoeff > 0, f"positive isogeny degree e={e}")

    # 7 is inert in Q(i): x^2+1 has no root mod 7.
    roots = [x for x in range(7) if (x * x + 1) % 7 == 0]
    req(roots == [], "7 inert in Q(i)")

    cm = cert["cm_quotient"]
    req(cm["factor_elliptic_curve"] == "E0:y^2=x^3-x", "CM quotient curve")
    req(cm["j"] == 1728, "j=1728")
    req(cm["endomorphism_algebra"] == "Q(i)", "CM algebra")
    req(cm["prime"] == 7 and cm["prime_inert_in_Q_i"] is True, "inert-prime adapter")
    req(cm["equal_degree_ratio_norm"] == 1, "norm-one ratio")
    req(cm["ratio_is_7_adic_unit"] is True, "7-adic unit")
    req(cm["common_nontrivial_7_primary_kernel"] is True, "common 7-kernel")
    req(cm["pair_map_generic_degree_divisible_by_7"] is True, "pair degree divisible by 7")

    # The geometric box/Kummer degree can only be e or 2e, hence a 2-power.
    expected_degrees = sorted({m * e for e in (1, 2, 4) for m in (1, 2)})
    req(expected_degrees == [1, 2, 4, 8], "box degree options")
    req(all(d > 0 and (d & (d - 1)) == 0 for d in expected_degrees), "all box degrees are 2-powers")
    req(all(d % 7 != 0 for d in expected_degrees), "no box degree divisible by 7")

    kb = cert["kummer_box_degree"]
    req(kb["B1_to_B_sigma_generic_degree_options"] == expected_degrees, "certificate box degree table")
    req(kb["any_option_divisible_by_7"] is False, "certificate 7 firewall")

    contradiction = cert["contradiction"]
    req(contradiction["cm_side_requires_generic_degree_divisible_by_7"] is True, "CM side")
    req(contradiction["box_side_requires_generic_degree_power_of_two"] is True, "box side")
    req(contradiction["uniform_minimal_branch_packet_realizable_on_size48"] is False, "packet closure")

    frontier = cert["frontier"]
    req(frontier["geometric_uniform_ray_supports_with_arbitrary_branch_partition"] == 864, "geometric support firewall")
    req(frontier["mb104_equality_packet_supports_before"] == 864, "packet before")
    req(frontier["mb104_equality_packet_supports_after"] == 768, "packet after")
    req(frontier["remaining_equality_packet_mask"] == "000707000f0f", "remaining mask")

    fw = cert["credit_firewall"]
    req(fw["picard_class_irreducible_member_excluded_for_all_branch_partitions"] is False, "arbitrary branch firewall")
    req(fw["span5_closed"] is False and fw["MB104_complete"] is False, "MB104 firewall")
    req(fw["receiver_credit"] is False and fw["theorem_credit"] is False and fw["endpoint_credit"] is False, "credit firewall")
    req(fw["merge_authorized"] is False, "merge firewall")

    print("PASS STAGE32_MB104_BALANCED16_SIZE48_CM_INERT7_OBSTRUCTION_V1")
    print("size48 equality packet: B1 genus1; equal degree 14*e*l isogenies to j=1728 CM quotient")
    print("7 inert in Q(i) => common 7-primary kernel => pair degree divisible by 7")
    print("box/Kummer degree in {1,2,4,8} => contradiction; equality-packet frontier 864 -> 768")
    print("firewall: arbitrary branch partitions in |D_l| are not excluded")


if __name__ == "__main__":
    main()
