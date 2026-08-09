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
    """Reduce one physical integral face and record whether shared is S or X."""
    g = math.gcd(shared, other)
    shared0 = shared // g
    other0 = other // g
    if math.gcd(shared0, other0) != 1:
        raise ArithmeticError(("primitive gcd", shared, other, shared0, other0))

    if shared0 % 2 == 1 and other0 % 2 == 0:
        shared_role = "S"
        S, X = shared0, other0
    elif shared0 % 2 == 0 and other0 % 2 == 1:
        shared_role = "X"
        S, X = other0, shared0
    else:
        raise ArithmeticError(("primitive-face-parity", shared, other, shared0, other0))

    H2 = S * S + X * X
    H = math.isqrt(H2)
    if H * H != H2:
        raise ArithmeticError((shared, other, S, X, H2))

    m2_num = H + S
    n2_num = H - S
    if m2_num % 2 or n2_num % 2:
        raise ArithmeticError(("euclid-half-integrality", S, X, H))
    m = math.isqrt(m2_num // 2)
    n = math.isqrt(n2_num // 2)
    if m * m != m2_num // 2 or n * n != n2_num // 2 or 2 * m * n != X or not (m > n > 0):
        raise ArithmeticError(("euclid-recovery", S, X, H, m, n))

    if shared_role == "S":
        shared_ratio = Fraction(X, S)
    else:
        shared_ratio = Fraction(S, X)
    if shared_ratio != Fraction(other, shared):
        raise ArithmeticError(("physical-ratio dictionary", shared, other, shared_role, S, X))

    return {
        "g": g,
        "shared0": shared0,
        "other0": other0,
        "shared_role": shared_role,
        "S": S,
        "X": X,
        "H": H,
        "m": m,
        "n": n,
        "other_over_shared": shared_ratio,
    }


def p7_shared_column(face):
    """Return the s5 moving-factor column carrying p=7 for the primitive shared leg."""
    if face["shared0"] % P != 0:
        return "good"
    m, n = face["m"], face["n"]
    if face["shared_role"] == "S":
        minus = (m - n) % P == 0
        plus = (m + n) % P == 0
        if minus == plus:
            raise ArithmeticError(("S-column root", face))
        return "m-n" if minus else "m+n"
    mzero = m % P == 0
    nzero = n % P == 0
    if mzero == nzero:
        raise ArithmeticError(("X-column root", face))
    return "m" if mzero else "n"


def s5_row_kind(face, column):
    if column == "good":
        return "good-prime"
    if face["shared_role"] == "S":
        return "S-row"
    return "X-row"


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
    return {"ambient": ambient, "missing_third_face_qr0_pass": passed, "forced": True}


def s5_row_audit():
    if legendre(-1, P) != -1:
        raise ArithmeticError("p=7 must be 3 mod 4")
    # s5d: unselected X row is chi(d2)=+1 OR chi(-d2)=+1.
    for d2 in range(1, P):
        if not (legendre(d2, P) == 1 or legendre(-d2, P) == 1):
            raise ArithmeticError(("unselected-X-not-automatic", d2))
    # s5c/14-4an: selected X/13 requires chi(-1)=+1.
    if legendre(-1, P) == 1:
        raise ArithmeticError("selected X unexpectedly possible")
    return {
        "minus_one_legendre": -1,
        "selected_S_label": "12",
        "selected_S_compressed_condition": "chi_7(a3)=+1",
        "unselected_S_condition": "chi_7(d3)=+1",
        "selected_X_label": "13",
        "selected_X_possible": False,
        "unselected_X_row_automatic": True,
    }


def main():
    rows = load_rows()
    by_direction_shared = defaultdict(Counter)
    by_direction_bad_face_count = defaultdict(Counter)
    by_direction_role_pair = defaultdict(Counter)
    by_direction_p7_packet = defaultdict(Counter)
    by_direction_row_packet = defaultdict(Counter)
    by_direction_shared_parity = defaultdict(Counter)
    valuation_packets = defaultdict(Counter)

    for row in rows:
        direction, e, x, y = object_view(row)
        if not x < y:
            raise ArithmeticError(("nonshared order", row, x, y))

        f1 = primitive_face(e, x)
        f2 = primitive_face(e, y)
        t1 = f1["other_over_shared"]
        t2 = f2["other_over_shared"]
        if direction == "a":
            ok = Fraction(1, 1) < t1 < t2
        elif direction == "b":
            ok = t1 < Fraction(1, 1) < t2
        else:
            ok = t1 < t2 < Fraction(1, 1)
        if not ok:
            raise ArithmeticError(("canonical chamber dictionary", row, t1, t2))

        col1 = p7_shared_column(f1)
        col2 = p7_shared_column(f2)
        row1 = s5_row_kind(f1, col1)
        row2 = s5_row_kind(f2, col2)
        bad_count = int(col1 != "good") + int(col2 != "good")
        shared7 = e % P == 0

        # If 7|physical shared edge but it disappeared from both primitive shared
        # legs, then 7 would divide e,x,y, contradicting primitive cuboid gcd=1.
        if shared7 != (bad_count >= 1):
            raise ArithmeticError(("shared7 <-> primitive shared-column incidence", row, f1, f2, col1, col2))

        vp_e, vp_x, vp_y = v_p(e, P), v_p(x, P), v_p(y, P)
        expected_bad = int(vp_e > vp_x) + int(vp_e > vp_y)
        if expected_bad != bad_count:
            raise ArithmeticError(("valuation role mismatch", row, vp_e, vp_x, vp_y, bad_count))

        by_direction_shared[direction]["yes" if shared7 else "no"] += 1
        by_direction_bad_face_count[direction][str(bad_count)] += 1
        by_direction_role_pair[direction][f"{f1['shared_role']}|{f2['shared_role']}"] += 1
        by_direction_shared_parity[direction]["odd" if e % 2 else "even"] += 1
        if shared7:
            by_direction_p7_packet[direction][f"{col1}|{col2}"] += 1
            by_direction_row_packet[direction][f"{row1}|{row2}"] += 1
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
        "classification": "P7_SHARED_EDGE_TO_EXISTING_S5_LOCAL_ROW_TRANSLATION",
        "source_rows": len(rows),
        "exact_dictionary": {
            "physical_pair": "e=shared edge; integral faces (e,x),(e,y); x<y",
            "primitive_face_reduction": "g_i=gcd(e,other_i); shared_i=e/g_i; other_i=other_i/g_i",
            "shared_leg_role": "shared_i is S if odd, X if even in the primitive Pythagorean face",
            "direction_a": "1 < x/e < y/e",
            "direction_b": "x/e < 1 < y/e",
            "direction_c": "x/e < y/e < 1",
            "p7_event": "7|e iff at least one primitive shared_i remains divisible by 7",
            "if_shared_role_S": "7 lies in m_i-n_i or m_i+n_i column (S=(m-n)(m+n))",
            "if_shared_role_X": "7 lies in m_i or n_i column (X=2mn)",
            "s5_receiver": "S role -> s5c/s5d S-row; X role -> s5c/s5d X-row",
        },
        "diag4_shared7_counts": {q: dict(by_direction_shared[q]) for q in DIRECTIONS},
        "primitive_shared_p7_bad_face_count_by_direction": {q: dict(sorted(by_direction_bad_face_count[q].items())) for q in DIRECTIONS},
        "primitive_shared_leg_role_pair_by_direction": {q: dict(sorted(by_direction_role_pair[q].items())) for q in DIRECTIONS},
        "physical_shared_edge_parity_by_direction": {q: dict(sorted(by_direction_shared_parity[q].items())) for q in DIRECTIONS},
        "p7_moving_factor_packet_by_direction": {q: dict(sorted(by_direction_p7_packet[q].items())) for q in DIRECTIONS},
        "p7_s5_row_packet_by_direction": {q: dict(sorted(by_direction_row_packet[q].items())) for q in DIRECTIONS},
        "p7_valuation_packet_by_direction": {q: dict(sorted(valuation_packets[q].items())) for q in DIRECTIONS},
        "finite_field_missing_face": ff,
        "s5_local_rows_at_p7": s5,
        "decision": {
            "P7_SHARED_EVENT_ALGEBRAIZED_TO_EXISTING_S5_MOVING_FACTOR_COLUMNS": True,
            "P7_SHARED_EVENT_CAN_HIT_S_OR_X_ROW_AFTER_PRIMITIVE_FACE_REDUCTION": True,
            "P7_X_ROW_IS_LOCALLY_ASYMMETRIC_TO_S_ROW": True,
            "P7_MISSING_THIRD_FACE_QR0_IS_INDEPENDENT_FILTER": False,
            "STAGE13_LAMBDA7_NULL_REUSED": False,
            "ASYMPTOTIC_DIRECTION_CLAIM": False,
            "NEXT_RECEIVING_TEST": "in the 14-4 two-face matching count, split each chamber by the ordered p7 row packet (good/S/X on the two primitive face orientations), insert the already-proved s5c/s5d local weights, and test whether the chamber p7 rate vector is explained by row-packet mixture or requires a residual local-archimedean correlation",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
