#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[6]
CERT_PATH = HERE / "FORMAL-INFINITE-FAMILY-PICARD-CERTIFICATE.json"


def require(cond, msg):
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def git_blob_sha1(path):
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def check_source_locks(cert):
    for lock in cert["source_locks"]:
        path = ROOT / lock["path"]
        require(path.is_file(), f"missing source lock {lock['path']}")
        got = git_blob_sha1(path)
        require(got == lock["blob_sha1"], f"source-lock mismatch {lock['path']}: {got}")


def check_common(cert):
    pic = cert["picard_interface"]
    require(pic["support_size"] == 14, "support size")
    require(pic["H_squared"] == 16, "H^2")
    require(pic["H_dot_E_i"] == 0, "H.E")
    require(pic["E_i_squared"] == -2, "E^2")
    require(pic["E_i_dot_E_j_i_ne_j"] == 0, "E_i.E_j")

    common = cert["common_contact_skeleton"]
    require(common["N"] == 14, "N=14")
    require(common["R"] == "28k", "R")
    require(common["R8"] == "28k", "R8")
    require(common["M"] == "28k", "M")
    require(common["r_odd"] == "28k", "r_odd")


def picard_square(a, k):
    return 16 * a * a - 28 * k * k


def replay_f0():
    # Infinite arithmetic progression k=4l+3; finite replay checks the exact symbolic identities.
    for l in range(0, 201):
        k = 4 * l + 3
        g = 0
        d = 28 * k - 4
        require(d % 16 == 0, f"F0 degree divisibility l={l}")
        a = d // 16
        require(a == 7 * l + 5 == (7 * k - 1) // 4, f"F0 H coefficient l={l}")

        # H.D=d; supported E_i.D=2k by the diagonal H/E intersection interface.
        require(16 * a == d, f"F0 H.D l={l}")
        supported_E = 2 * k
        require(supported_E > 0, f"F0 supported E l={l}")

        sq = picard_square(a, k)
        require(sq == 21 * k * k - 14 * k + 1, f"F0 square in k l={l}")
        require(sq == 336 * l * l + 448 * l + 148, f"F0 square in l l={l}")

        numer = sq + d + 2  # MB102: D^2+d=2g-2+2Delta, g=0.
        require(numer % 2 == 0, f"F0 Delta parity l={l}")
        delta = numer // 2
        require(delta == (21 * k * k + 14 * k - 1) // 2, f"F0 Delta k l={l}")
        require(delta == 168 * l * l + 280 * l + 115, f"F0 Delta l l={l}")
        require(delta >= 0, f"F0 Delta nonnegative l={l}")
        require(sq + d == 2 * g - 2 + 2 * delta, f"F0 adjunction l={l}")

        M = 28 * k
        r_odd = 28 * k
        require(-d + M + 4 * g - 4 == 0, f"F0 GFU equality l={l}")
        require(r_odd == d + 4, f"F0 Beauville equality l={l}")

        # P6 support has rank-3 block node counts [3,3,2,2,2,2].
        fiber = [(d - 2 * k * n) // 2 for n in (3, 3, 2, 2, 2, 2)]
        require(fiber == [11 * k - 2, 11 * k - 2, 12 * k - 2, 12 * k - 2, 12 * k - 2, 12 * k - 2], f"F0 rank3 fibers l={l}")
        require(all(x >= 0 for x in fiber), f"F0 rank3 nef l={l}")


def replay_f1(span):
    require(span in (5, 6), "F1 span")
    counts = (0, 0, 0, 5, 5, 4) if span == 5 else (3, 3, 2, 2, 2, 2)
    expected = (lambda k: [14*k, 14*k, 14*k, 9*k, 9*k, 10*k]) if span == 5 else (lambda k: [11*k, 11*k, 12*k, 12*k, 12*k, 12*k])

    for l in range(1, 201):
        k = 4 * l
        g = 1
        d = 28 * k
        require(d % 16 == 0, f"F1-P{span} degree divisibility l={l}")
        a = d // 16
        require(a == 7 * l == 7 * k // 4, f"F1-P{span} H coefficient l={l}")
        require(16 * a == d, f"F1-P{span} H.D l={l}")

        sq = picard_square(a, k)
        require(sq == 21 * k * k == 336 * l * l, f"F1-P{span} square l={l}")
        numer = sq + d  # MB102: D^2+d=2Delta for g=1.
        require(numer % 2 == 0, f"F1-P{span} Delta parity l={l}")
        delta = numer // 2
        require(delta == (21 * k * k + 28 * k) // 2, f"F1-P{span} Delta k l={l}")
        require(delta == 168 * l * l + 56 * l, f"F1-P{span} Delta l l={l}")
        require(delta >= 0, f"F1-P{span} Delta nonnegative l={l}")
        require(sq + d == 2 * g - 2 + 2 * delta, f"F1-P{span} adjunction l={l}")

        M = 28 * k
        r_odd = 28 * k
        require(-d + M + 4 * g - 4 == 0, f"F1-P{span} GFU equality l={l}")
        require(r_odd == d, f"F1-P{span} Beauville equality l={l}")

        fiber = [(d - 2 * k * n) // 2 for n in counts]
        require(fiber == expected(k), f"F1-P{span} rank3 fibers l={l}")
        require(all(x >= 0 for x in fiber), f"F1-P{span} rank3 nef l={l}")


def check_certificate_contract(cert):
    require(cert["schema"] == "STAGE32_MB104_FORMAL_INFINITE_PICARD_REALIZABILITY_V1", "schema")
    require(cert["status"] == "RETAINED_EXPLICIT_PICARD_SUBSEQUENCES_MB104_INCOMPLETE", "status")

    delta = cert["delta_adapter"]
    require(delta["previous_packet_Delta_total_zero_carried_over"] is False, "Delta=0 not carried over")
    require(delta["Delta_off_may_absorb_required_defect_under_MB102_contract"] is True, "Delta_off interface")
    require(delta["actual_singular_curve_realizing_required_delta_claimed"] is False, "no actual singular curve claim")

    route = cert["route_consequence"]
    require(route["integral_picard_class_realizability_on_infinite_subsequences"] is True, "Picard subsequences")
    require(route["picard_integrality_obstruction_closes_hard_sectors"] is False, "Picard obstruction firewall")
    require(route["effectivity_obstruction_tested"] is False, "effectivity untested")
    require(route["irreducible_carrier_existence_tested"] is False, "irreducibility untested")
    require(route["normalization_genus_realized_by_actual_curve"] is False, "no actual low-genus curve")
    require(route["direct_R8_alpha_lt_quarter_route_remains_frozen"] is True, "R8 freeze")
    require(route["MB104_complete"] is False, "MB104 incomplete")

    fw = cert["credit_firewall"]
    for key, value in fw.items():
        require(value is False, f"credit firewall {key}")


def main():
    cert = json.loads(CERT_PATH.read_text())
    check_source_locks(cert)
    check_common(cert)
    check_certificate_contract(cert)
    replay_f0()
    replay_f1(5)
    replay_f1(6)
    print("PASS: hard-sector formal skeleton survives integral Picard-class realizability on infinite arithmetic subsequences; effectivity/actual-carrier existence remains open")


if __name__ == "__main__":
    main()
