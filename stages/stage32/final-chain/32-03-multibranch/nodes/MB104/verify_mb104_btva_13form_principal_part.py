#!/usr/bin/env python3
import json
from pathlib import Path

CERT = Path(__file__).with_name("BTVA-13FORM-PRINCIPAL-PART-CERTIFICATE.json")


def require(cond, msg):
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def parse_gauss(s):
    table = {
        "0": (0, 0), "1": (1, 0), "-1": (-1, 0),
        "2": (2, 0), "-2": (-2, 0),
        "i": (0, 1), "-i": (0, -1),
        "2i": (0, 2), "-2i": (0, -2),
    }
    require(s in table, f"unsupported Gaussian integer {s}")
    return table[s]


def gadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def gsub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def gmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def gneg(x):
    return (-x[0], -x[1])


def det3(rows):
    a, b, c = rows
    minor0 = gsub(gmul(b[1], c[2]), gmul(b[2], c[1]))
    minor1 = gsub(gmul(b[0], c[2]), gmul(b[2], c[0]))
    minor2 = gsub(gmul(b[0], c[1]), gmul(b[1], c[0]))
    term0 = gmul(a[0], minor0)
    term1 = gmul(a[1], minor1)
    term2 = gmul(a[2], minor2)
    return gadd(gsub(term0, term1), term2)


def rank3(rows):
    n = len(rows)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if det3([rows[i], rows[j], rows[k]]) != (0, 0):
                    return 3
    return 0


def unit_inv(x):
    require(x != (0, 0), "zero projective pivot")
    norm = x[0] * x[0] + x[1] * x[1]
    require(norm == 1, f"non-unit node coordinate pivot {x}")
    return (x[0], -x[1])


def canon(point):
    for x in point:
        if x != (0, 0):
            inv = unit_inv(x)
            return tuple(gmul(y, inv) for y in point)
    raise SystemExit("FAIL: zero projective point")


Z = (0, 0)
ONE = (1, 0)
I = (0, 1)
MI = (0, -1)


def signed(unit, sign):
    return unit if sign == 1 else gneg(unit)


def all_48_nodes():
    out = set()
    for s1 in (1, -1):
        for s2 in (1, -1):
            for s3 in (1, -1):
                out.add(canon((ONE, Z, Z, Z, signed(ONE, s1), signed(ONE, s2), signed(ONE, s3))))
                out.add(canon((Z, ONE, Z, signed(ONE, s1), Z, signed(ONE, s2), signed(ONE, s3))))
                out.add(canon((Z, Z, ONE, signed(ONE, s1), signed(ONE, s2), Z, signed(ONE, s3))))
                out.add(canon((ONE, signed(I, s1), Z, signed(I, s2), signed(ONE, s3), Z, Z)))
                out.add(canon((Z, ONE, signed(I, s1), Z, signed(I, s2), signed(ONE, s3), Z)))
                out.add(canon((signed(I, s1), Z, ONE, signed(ONE, s2), Z, signed(I, s3), Z)))
    return out


def apply_generator(p, idx):
    a1, a2, a3, b1, b2, b3, c = p
    if idx == 0:
        q = (a2, a1, a3, b2, b1, b3, c)
    elif idx == 1:
        q = (a3, a2, a1, b3, b2, b1, c)
    elif idx == 2:
        q = (gmul(I, c), a2, a3, b1, gmul(I, b3), gmul(MI, b2), gmul(MI, a1))
    elif idx == 3:
        q = (gneg(a1), a2, a3, b1, b2, b3, c)
    elif idx == 4:
        q = (a1, gneg(a2), a3, b1, b2, b3, c)
    elif idx == 5:
        q = (a1, a2, gneg(a3), b1, b2, b3, c)
    elif idx == 6:
        q = (a1, a2, a3, gneg(b1), b2, b3, c)
    elif idx == 7:
        q = (a1, a2, a3, b1, gneg(b2), b3, c)
    elif idx == 8:
        q = (a1, a2, a3, b1, b2, gneg(b3), c)
    else:
        raise AssertionError(idx)
    return canon(q)


def orbit_from_R1():
    r1 = canon((ONE, Z, Z, Z, ONE, ONE, ONE))
    seen = {r1}
    todo = [r1]
    while todo:
        p = todo.pop()
        for idx in range(9):
            q = apply_generator(p, idx)
            if q not in seen:
                seen.add(q)
                todo.append(q)
    return seen


def main():
    cert = json.loads(CERT.read_text())
    require(cert["schema"] == "STAGE32_MB104_BTVA_13FORM_PRINCIPAL_PART_V1", "schema")
    require(cert["status"] == "RETAINED_BRANCH_SENSITIVE_LOCAL_RESULT_MB104_INCOMPLETE", "status")
    require(cert["space"]["dimension"] == 13, "13-form dimension")
    require(cert["space"]["local_A1_obstruction_dimension"] == 3, "A1 obstruction dimension")

    r1 = [[parse_gauss(x) for x in row] for row in cert["R1"]["rows_du2_dudv_dv2"]]
    r2 = [[parse_gauss(x) for x in row] for row in cert["R2"]["rows_du2_dudv_dv2"]]
    require(len(r1) == 13 and len(r2) == 13, "13 rows per representative")
    require(rank3(r1) == cert["R1"]["rank"] == 3, "R1 maximal principal-part rank")
    require(rank3(r2) == cert["R2"]["rank"] == 3, "R2 maximal principal-part rank")

    eval_rows = [
        [(1, 0), (0, 0), (0, 0)],
        [(1, 0), (1, 0), (1, 0)],
        [(1, 0), (-1, 0), (1, 0)],
    ]
    require(det3(eval_rows) != (0, 0), "three distinct landing directions saturate quadratic principal part")
    require(cert["local_A1_lemma"]["distinct_landing_condition_saturation"] == 3, "saturation contract")

    nodes = all_48_nodes()
    orbit = orbit_from_R1()
    require(len(nodes) == 48, "explicit 48-node list")
    require(len(orbit) == 48, "Stoll-generator R1 orbit size")
    require(orbit == nodes, "Stoll-generator orbit equals explicit 48-node set")
    require(cert["all_nodes"]["R1_orbit_size_under_fixed_generators"] == 48, "certificate orbit size")
    require(cert["all_nodes"]["single_geometric_orbit_verified"] is True, "single orbit flag")
    require(cert["all_nodes"]["principal_part_rank_at_every_node"] == 3, "all-node rank contract")

    consequence = cert["branch_multiplicity_consequence"]
    require(consequence["counts_R8_with_multiplicity"] is False, "no multiplicity overclaim")
    require(consequence["order_two_portfolio_alone_can_bound_R8_linearly"] is False, "order-two firewall")
    require(consequence["higher_order_or_repeated_branch_charging_required"] is True, "next-input firewall")

    fw = cert["credit_firewall"]
    for key in [
        "MB104_complete", "absolute_R8_bound_proved", "finite_degree_window_proved",
        "finite_picard_enumeration_released", "r29_lg2_mb_discharged", "receiver_credit",
        "effectivity_credit", "final_milestone_credit", "theorem_credit", "endpoint_credit",
        "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim", "merge_authorized",
    ]:
        require(fw[key] is False, f"credit firewall {key}")

    print("PASS: BTVA 13-form A1 principal part is rank 3; order-two landing conditions saturate after three directions per node")


if __name__ == "__main__":
    main()
