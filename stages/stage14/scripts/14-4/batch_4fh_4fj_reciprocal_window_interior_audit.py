from __future__ import annotations

from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def check_window_equivalence() -> None:
    # Exact rational test of the two-window -> radial-product equivalence.
    A = 3
    beta0 = 5
    xm, xp = 12, 24
    ym, yp = 20, 40

    n2_lo = Fraction(xm * ym, A * beta0)
    n2_hi = Fraction(xp * yp, A * beta0)

    for n in range(1, 20):
        l1_lo = Fraction(xm, A)
        l1_hi = Fraction(xp, A)
        l2_lo = Fraction(beta0 * n * n, yp)
        l2_hi = Fraction(beta0 * n * n, ym)
        nonempty = max(l1_lo, l2_lo) <= min(l1_hi, l2_hi)
        radial = n * n >= n2_lo and n * n <= n2_hi
        assert nonempty == radial, (n, nonempty, radial)


def check_endpoint_exponent() -> None:
    # theta > nu-mu implies nu-theta < mu.
    cells = [
        (Fraction(1, 24), Fraction(1, 48), Fraction(1, 32)),
        (Fraction(1, 30), Fraction(1, 40), Fraction(1, 60)),
        (Fraction(1, 50), Fraction(1, 50), Fraction(1, 100)),
    ]
    for nu, mu, eps in cells:
        theta = nu - mu + eps
        assert theta > nu - mu
        assert nu - theta < mu


def check_incidence_sandwich() -> None:
    # Finite-fiber existential support and incidence differ by <= max fiber.
    fibers = {
        1: [0, 1, 0],
        2: [0, 0],
        3: [1],
        4: [1, 1, 0, 0],
    }
    accepted = sum(1 for ws in fibers.values() if any(ws))
    incidence = sum(sum(ws) for ws in fibers.values())
    max_fiber = max(len(ws) for ws in fibers.values())
    assert accepted <= incidence <= max_fiber * accepted


def check_boundary_files() -> None:
    checks = {
        "stages/stage14/14-4fh/result.md": [
            "EXACT_RECIPROCAL_L_WINDOW_INTERSECTION_PROVED=true",
            "RECIPROCAL_WINDOW_NONEMPTY_IFF_RADIAL_PRODUCT_WINDOW=true",
        ],
        "stages/stage14/14-4fi/result.md": [
            "THETA_GT_NU_MINUS_MU_KILLS_ENDPOINT_SUPPORT=true",
            "HEAVY_SUPPORT_CANNOT_CONCENTRATE_AT_RECIPROCAL_WINDOW_ENDPOINTS=true",
        ],
        "stages/stage14/14-4fj/result.md": [
            "INTERIOR_EXISTENTIAL_SUPPORT_INCIDENCE_EXPONENT_EQUIVALENT=true",
            "RECEIVER_MATERIALLY_CHANGED=true",
            "NEXT=Stage14-4fk",
        ],
        "stages/stage14/14-4-batch/4fh-4fj-report.md": [
            "BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3",
            "BATCH_STOP_REASON=receiver_change",
            "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
        ],
    }
    for rel, needles in checks.items():
        text = (ROOT / rel).read_text(encoding="utf-8")
        for needle in needles:
            assert needle in text, (rel, needle)


def main() -> None:
    check_window_equivalence()
    check_endpoint_exponent()
    check_incidence_sandwich()
    check_boundary_files()
    print("Stage14-main-batch 4fh-4fj audit: OK")


if __name__ == "__main__":
    main()
