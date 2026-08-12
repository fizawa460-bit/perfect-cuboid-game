from __future__ import annotations

from math import log


def naive_x_height_upper(d: int, k: int, Z: int) -> float:
    return log(2 * d * k * Z * Z)


def petit_log_threshold(d: int, alpha: float) -> float:
    if not (0 < alpha < 1 / 120):
        raise ValueError("Petit range requires 0 < alpha < 1/120")
    return (1 / 8 + alpha) * log(d)


def formal_scale_countermodel(B: int) -> dict[str, object]:
    # This is deliberately only a countermodel to the certified SIZE IMPLICATION,
    # not a claim that the formal block contains a physical Stage15 point.
    d, k, kappa, W = 2, 2, 1, 2
    Z = max(2, B // 4)
    return {
        "d": d,
        "k": k,
        "kappa": kappa,
        "Z": Z,
        "W": W,
        "physical_product_inequality": k * Z * W <= 2 * B,
        "small_kappa_inequality": kappa * kappa < Z * W,
        "naive_x_height_upper": naive_x_height_upper(d, k, Z),
        "petit_threshold_alpha_1_over_240": petit_log_threshold(d, 1 / 240),
    }


if __name__ == "__main__":
    print(formal_scale_countermodel(10**6))
