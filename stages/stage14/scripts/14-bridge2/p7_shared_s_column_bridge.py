#!/usr/bin/env python3
from __future__ import annotations

import base64
import bz2
import csv
import io
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / "stages/stage14/data/14-num-alpha11/b500m_objects.csv.bz2.b64"
P = 7
DIRECTIONS = ("a", "b", "c")
EXPECTED_SHARED7_YES = {"a": 758, "b": 879, "c": 476}
EXPECTED_SHARED7_NO = {"a": 616, "b": 492, "c": 274}


def load_rows():
    encoded = "".join(SOURCE.read_text(encoding="ascii").split())
    raw = bz2.decompress(base64.b64decode(encoded)).decode("utf-8")
    rows = [tuple(int(r[k]) for k in ("a", "b", "c", "d", "mask")) for r in csv.DictReader(io.StringIO(raw))]
    if len(rows) != 3495 or len(set(rows)) != 3495:
        raise ArithmeticError(f"B500 source regression failed: rows={len(rows)} unique={len(set(rows))}")
    return rows


def object_view(row):
    a, b, c, d, mask = row
    if mask == 0b011:
        return "a", a, b, c
    if mask == 0b101:
        return "b", b, a, c
    if mask == 0b110:
        return "c", c, a, b
    raise ArithmeticError(f"unexpected mask {mask}")


def v_p(n: int, p: int) -> int:
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def primitive_face(shared: int, other: int):
    g = math.gcd(shared, other)
    S = shared // g
    X = other // g
    H2 = S * S + X * X
    H = math.isqrt(H2)
    if H * H != H2:
        raise ArithmeticError((shared, other, S, X, H2))
    if math.gcd(S, X) != 1 or S % 2 != 1 or X % 2 != 0:
        raise ArithmeticError(("primitive-face-parity", shared, other, S, X, H))

    m2_num = H + S
    n2_num = H - S
    if m2_num % 2 or n2_num % 2:
        raise ArithmeticError(("euclid-half-integrality", S, X, H))
    m = math.isqrt(m2_num // 2)
    n = math.isqrt(n2_num // 2)
    if m * m != m2_num // 2 or n * n != n2_num // 2 or 2 * m * n != X or not (m > n > 0):
        raise ArithmeticError(("euclid-recovery", S, X, H, m, n))
    return {"g": g, "S": S, "X": X, "H": H, "m": m, "n": n}


def root_type(face, p=P):
    m, n, S = face["m"], face["n"], face["S"]
    minus = (m - n) % p == 0
    plus = (m + n) % p == 0
    if minus and plus:
        raise ArithmeticError(("both roots", m, n, p))
    if (S % p == 0) != (minus or plus):
        raise ArithmeticError(("S-root mismatch", m, n, S, p))
    if minus:
        return "m-n"
    if plus:
        return "m+n"
    return "good"


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    z = pow(a, (p - 1) // 2, p)
    return 1 if z == 1 else -1


def finite_field_p7_missing_face_audit():
    qr0 = {x * x % P for x in range(P)}
    ambient = 0
    passed = 0
    for x in range(P):
        x2 = x * x % P
        for y in range(P):
            y2 = y * y % P
            if (x2 + y2) % P not in qr0:
                continue
            for z in range(P):
                z2 = z * z % P
                if (x2 + z2) % P not in qr0:
                    continue
                space = (x2 + y2 + z2) % P
                if space == 0 or space not in qr0:
                    continue
                ambient += 1
                if (y2 + z2) % P in qr0:
                    passed += 1
    if (ambient, passed) != (54, 54):
        raise ArithmeticError((ambient, passed))
    return {"ambient": ambient, "missing_third_face_qr0_pass": passed, "forced": passed == ambient}


def s5_row_audit():
    if legendre(-1, P) != -1:
        raise ArithmeticError("p=7 must be 3 mod 4")
    # s5d unselected X-row is chi(d2)=+1 OR chi(-d2)=+1.
    # For p=7 this is automatic for every unit d2.
    for d2 in range(1, P):
        if not (legendre(d2, P) == 1 or legendre(-d2, P) == 1):
            raise ArithmeticError(("unselected-X-not-automatic", d2))
    # s5c selected X-row requires chi(-1)=+1 after compression, so impossible.
    selected_x_possible = legendre(-1, P) == 1
    if selected_x_possible:
        raise ArithmeticError("selected X row unexpectedly possible")
    return {
        "minus_one_legendre": -1,
        "selected_X_label13_possible": False,
        "unselected_X_row_automatic": True,
        "shared_edge_receiver_row": "S/12 selected or S-unselected; one d3/a3 square bit",
    }


def main():
    rows = load_rows()
    by_direction_shared = defaultdict(Counter)
    by_direction_bad_face_count = defaultdict(Counter)
    root_packets = defaultdict(Counter)
    valuation_packets = defaultdict(Counter)
    chamber_checks = Counter()

    for row in rows:
        direction, e, x, y = object_view(row)
        if e % 2 == 0:
            raise ArithmeticError(("shared edge must be odd", row))
        if not x < y:
            raise ArithmeticError(("nonshared order", row, x, y))

        f1 = primitive_face(e, x)
        f2 = primitive_face(e, y)
        t1 = Fraction(f1["X"], f1["S"])
        t2 = Fraction(f2["X"], f2["S"])
        if t1 != Fraction(x, e) or t2 != Fraction(y, e):
            raise ArithmeticError(("4ab ratio dictionary", row, t1, t2))

        if direction == "a":
            ok = Fraction(1, 1) < t1 < t2
        elif direction == "b":
            ok = t1 < Fraction(1, 1) < t2
        else:
            ok = t1 < t2 < Fraction(1, 1)
        if not ok:
            raise ArithmeticError(("chamber dictionary", row, t1, t2))
        chamber_checks[direction] += 1

        r1 = root_type(f1)
        r2 = root_type(f2)
        bad_count = int(r1 != "good") + int(r2 != "good")
        shared7 = e % P == 0

        # Because the physical cuboid is primitive, 7|e must remain in at least
        # one primitive shared S-column after reducing the two integral faces.
        if shared7 != (bad_count >= 1):
            raise ArithmeticError(("shared7 <-> S-column incidence", row, r1, r2, f1, f2))

        # Equivalent valuation formulation: S_i retains p exactly when the
        # shared-edge valuation exceeds the corresponding nonshared valuation.
        vp_e, vp_x, vp_y = v_p(e, P), v_p(x, P), v_p(y, P)
        expected_bad = int(vp_e > vp_x) + int(vp_e > vp_y)
        if expected_bad != bad_count:
            raise ArithmeticError(("valuation role mismatch", row, vp_e, vp_x, vp_y, bad_count))

        by_direction_shared[direction]["yes" if shared7 else "no"] += 1
        by_direction_bad_face_count[direction][str(bad_count)] += 1
        if shared7:
            root_packets[direction][f"{r1}|{r2}"] += 1
            valuation_packets[direction][f"ve={vp_e};vx={vp_x};vy={vp_y}"] += 1

    for q in DIRECTIONS:
        if by_direction_shared[q]["yes"] != EXPECTED_SHARED7_YES[q]:
            raise ArithmeticError(("diag4 yes regression", q, by_direction_shared[q]))
        if by_direction_shared[q]["no"] != EXPECTED_SHARED7_NO[q]:
            raise ArithmeticError(("diag4 no regression", q, by_direction_shared[q]))

    ff = finite_field_p7_missing_face_audit()
    s5 = s5_row_audit()

    report = {
        "stage": "14-bridge2",
        "classification": "P7_SHARED_EDGE_TO_S_COLUMN_LOCAL_STATE_TRANSLATION",
        "source_rows": len(rows),
        "exact_dictionary": {
            "two_face_pair": "e=shared edge; faces (e,x),(e,y); x<y",
            "primitive_face_i": "S_i=e/gcd(e,other_i), X_i=other_i/gcd(e,other_i)",
            "shared_edge_is_odd": True,
            "shared7_equivalence": "7|e iff 7|S_1*S_2 iff at least one m_i-n_i or m_i+n_i is 0 mod 7",
            "direction_a": "1 < X1/S1 < X2/S2",
            "direction_b": "X1/S1 < 1 < X2/S2",
            "direction_c": "X1/S1 < X2/S2 < 1",
            "s5_factor_columns": "7|S_i means 7 divides exactly one of m_i-n_i or m_i+n_i; it is an S-side linear-column event",
        },
        "diag4_shared7_counts": {q: dict(by_direction_shared[q]) for q in DIRECTIONS},
        "primitive_S_bad_face_count_by_direction": {q: dict(sorted(by_direction_bad_face_count[q].items())) for q in DIRECTIONS},
        "p7_root_packet_by_direction": {q: dict(sorted(root_packets[q].items())) for q in DIRECTIONS},
        "p7_valuation_packet_by_direction": {q: dict(sorted(valuation_packets[q].items())) for q in DIRECTIONS},
        "finite_field_missing_face": ff,
        "s5_local_row": s5,
        "decision": {
            "P7_SHARED_EVENT_ALGEBRAIZED_TO_S_COLUMN_INCIDENCE": True,
            "P7_SHARED_EVENT_IS_X_COLUMN_EVENT": False,
            "P7_MISSING_THIRD_FACE_QR0_IS_INDEPENDENT_FILTER": False,
            "STAGE13_LAMBDA7_NULL_REUSED": False,
            "ASYMPTOTIC_DIRECTION_CLAIM": False,
            "NEXT_RECEIVING_TEST": "split the two-face matching count by kappa_7=# of primitive face S-columns divisible by 7 and determine the chamber-resolved leading local/archimedean density",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
