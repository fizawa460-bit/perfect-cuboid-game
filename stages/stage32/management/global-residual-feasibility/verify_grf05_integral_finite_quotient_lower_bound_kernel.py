#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CERT = HERE / "GRF-05-INTEGRAL-FINITE-QUOTIENT-LOWER-BOUND-KERNEL.json"
GRF04 = HERE / "GRF-04-RATIONAL-QUADRATIC-LOWER-BOUND-KERNEL.json"
CARD = ROOT / "docs/arsenal/cards/provisional/S32-PW04.md"
SOURCE = ROOT / "stages/stage32/residual-32-01-production/direct_picard_integral_coset_bound.py"

EXPECTED_BLOBS = {
    GRF04: "f7c1073edbf895f498fd9923e59eedf5a4e981c8",
    CARD: "c7912f776853bb273797de68d1e683857b7347f9",
    SOURCE: "9276a75e00970851f1d27b043492257ca5c1d3f1",
}
EXPECTED_CERT_CANONICAL = "b468fdcd24a481a63df03ccf56823f4386d7ab51ffacc9202a24a69488b85ca7"


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise RuntimeError(msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def inverse(a: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(a)
    req(n > 0 and all(len(row) == n for row in a), "inverse requires square matrix")
    aug = [
        list(row) + [Fraction(int(i == j), 1) for j in range(n)]
        for i, row in enumerate(a)
    ]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col] != 0), None)
        req(pivot is not None, "singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        p = aug[col][col]
        aug[col] = [v / p for v in aug[col]]
        for r in range(n):
            if r == col:
                continue
            f = aug[r][col]
            if f:
                aug[r] = [aug[r][j] - f * aug[col][j] for j in range(2 * n)]
    return [row[n:] for row in aug]


def det(a: list[list[Fraction]]) -> Fraction:
    n = len(a)
    req(n > 0 and all(len(row) == n for row in a), "det requires square matrix")
    m = [list(row) for row in a]
    out = Fraction(1)
    sign = 1
    for col in range(n):
        pivot = next((r for r in range(col, n) if m[r][col] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            m[col], m[pivot] = m[pivot], m[col]
            sign *= -1
        p = m[col][col]
        out *= p
        for r in range(col + 1, n):
            f = m[r][col] / p
            for j in range(col, n):
                m[r][j] -= f * m[col][j]
    return out * sign


def is_spd(a: list[list[Fraction]]) -> bool:
    n = len(a)
    if n == 0 or any(len(row) != n for row in a):
        return False
    if any(a[i][j] != a[j][i] for i in range(n) for j in range(n)):
        return False
    return all(det([row[:k] for row in a[:k]]) > 0 for k in range(1, n + 1))


def dist_to_z(x: Fraction) -> Fraction:
    floor_x = x.numerator // x.denominator
    r = x - floor_x
    return min(r, 1 - r)


def coordinate_lb(shift: list[Fraction], b_inv: list[list[Fraction]]) -> Fraction:
    req(len(shift) == len(b_inv), "shift/B inverse dimension mismatch")
    candidates = []
    for i, value in enumerate(shift):
        diagonal = b_inv[i][i]
        req(diagonal > 0, "inverse diagonal must be positive")
        candidates.append(dist_to_z(value) ** 2 / diagonal)
    return max(candidates, default=Fraction(0))


def quad(b: list[list[Fraction]], y: list[Fraction]) -> Fraction:
    return sum(
        y[i] * b[i][j] * y[j]
        for i in range(len(y))
        for j in range(len(y))
    )


def affine_shift(
    linear: list[list[Fraction]],
    constant: list[Fraction],
    u: tuple[int, ...],
) -> list[Fraction]:
    return [
        constant[i] + sum(linear[i][j] * u[j] for j in range(len(u)))
        for i in range(len(constant))
    ]


def main() -> None:
    for path, expected in EXPECTED_BLOBS.items():
        req(path.is_file(), f"missing source lock: {path.relative_to(ROOT)}")
        req(blob(path) == expected, f"source-lock drift: {path.relative_to(ROOT)}")

    cert = json.loads(CERT.read_text())
    stored = cert.pop("canonical_sha256_without_this_field", None)
    req(stored == EXPECTED_CERT_CANONICAL, "GRF-05 stored canonical drift")
    req(csha(cert) == EXPECTED_CERT_CANONICAL, "GRF-05 canonical drift")
    req(
        cert["status"]
        == "EXACT_SYMBOLIC_INTEGRAL_FINITE_QUOTIENT_LOWER_BOUND_KERNEL_NO_CONCRETE_178_TARGET_NO_CREDIT",
        "GRF-05 status drift",
    )

    card = CARD.read_text()
    req("FINITE_LATTICE_QUOTIENT_BOUND" in card, "S32-PW04 role drift")
    req("blob_sha=9276a75e00970851f1d27b043492257ca5c1d3f1" in card, "S32-PW04 source snapshot drift")
    req("classwise lower bound without a closest-vector search" in card, "S32-PW04 theorem snapshot drift")

    source = SOURCE.read_text()
    req(
        "safe_class_lower_bound" in source
        and "max_i dist(v*_i,Z)^2/(B^-1)_ii <= delta" in source,
        "source coordinate-Cauchy proof drift",
    )
    req("closest_vector_search_run" in source, "source no-CVP boundary drift")

    # Generic exact regression.  This deliberately does not reuse the source's
    # 61-dimensional specialization, its Smith diagonal, generator orders, or
    # reachable-class count.
    b = [
        [Fraction(2), Fraction(1)],
        [Fraction(1), Fraction(2)],
    ]
    req(is_spd(b), "fixture B is not SPD")
    b_inv = inverse(b)
    req(
        b_inv
        == [
            [Fraction(2, 3), Fraction(-1, 3)],
            [Fraction(-1, 3), Fraction(2, 3)],
        ],
        "exact inverse regression",
    )

    linear = [
        [Fraction(1, 2), Fraction(1, 3)],
        [Fraction(1, 3), Fraction(1, 6)],
    ]
    constant = [Fraction(1, 6), Fraction(0)]
    q = 6

    class_lb: dict[tuple[int, int], Fraction] = {}
    for u in itertools.product(range(q), repeat=2):
        shift = affine_shift(linear, constant, u)
        lb = coordinate_lb(shift, b_inv)
        class_lb[u] = lb

        # Exact regression against implementation/sign mistakes.  The theorem
        # itself is the coordinate Cauchy inequality source-locked above.
        for z in itertools.product(range(-3, 4), repeat=2):
            y = [Fraction(z[i]) - shift[i] for i in range(2)]
            loss = quad(b, y)
            req(loss >= lb, f"coordinate lower bound failed at u={u}, z={z}")

    # Rational affine shifts with denominator dividing q factor through u mod q.
    for u in itertools.product(range(-6, 7), repeat=2):
        reduced = (u[0] % q, u[1] % q)
        shift = affine_shift(linear, constant, u)
        req(
            coordinate_lb(shift, b_inv) == class_lb[reduced],
            f"finite quotient regression failed at u={u}",
        )

    # The bound is intentionally not claimed to solve CVP exactly.
    shift0 = affine_shift(linear, constant, (0, 0))
    lb0 = coordinate_lb(shift0, b_inv)
    exact_box_min = min(
        quad(b, [Fraction(z[i]) - shift0[i] for i in range(2)])
        for z in itertools.product(range(-3, 4), repeat=2)
    )
    req(lb0 == Fraction(1, 24), "fixture lower-bound regression")
    req(exact_box_min == Fraction(1, 18), "fixture integral minimum regression")
    req(lb0 < exact_box_min, "fixture must witness lower bound != exact CVP loss")

    # Safe GRF-04 composition: rho+lambda is a lower bound on every integral
    # objective; strict cap separation is the only emptiness direction.
    rho = Fraction(5, 7)
    cap = rho + lb0 - Fraction(1, 1000)
    req(rho + lb0 > cap, "strict combined-bound fixture drift")
    nonempty_unknown_cap = rho + exact_box_min
    req(
        rho + lb0 <= nonempty_unknown_cap,
        "non-emptiness firewall fixture drift",
    )

    imported = cert["source_specialization_not_imported"]
    req(not any(imported[k] for k in (
        "fixed_dimension_61",
        "smith_diagonal_1_2_2",
        "generator_orders_20_20_40",
        "reachable_class_count_640",
        "prior_slice_count_2018569",
    )), "source specialization leaked into generic MAIN kernel")

    fire = cert["credit_firewall"]
    req(not fire["main_pruning_credit"], "unexpected MAIN pruning credit")
    req(not fire["full178_complete"], "unexpected FULL178 completion")
    req(not fire["merge_authorized"], "unexpected merge authorization")
    req(not cert["ownership"]["concrete_row_or_stratum_selected"], "MAIN selected concrete 178 target")

    print(
        "GRF-05 PASS: exact finite-quotient coordinate lower bound is valid under "
        "an explicit integral-lattice adapter; no concrete FULL178 target or credit."
    )


if __name__ == "__main__":
    main()
