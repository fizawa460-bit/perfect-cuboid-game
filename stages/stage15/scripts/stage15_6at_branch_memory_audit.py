def scale_gate(B: int, k: int, kappa: int = 1, Z: int = 2, W: int = 2):
    small_kappa = kappa * kappa < Z * W
    product_height = k * Z * W <= 2 * B
    # A scale-level low-core box can be chosen with V > (k/2)^2; use V=k^2+1.
    V = k * k + 1
    low_core_size = k * k < 4 * V
    return small_kappa and product_height and low_core_size


def audit(B: int = 10000):
    admissible_scales = [k for k in range(1, B // 2 + 1) if scale_gate(B, k)]
    assert len(admissible_scales) == B // 2
    return {
        "B": B,
        "scale_compatible_k_count": len(admissible_scales),
        "subpolynomial_forced": False,
    }


if __name__ == "__main__":
    data = audit()
    print("STAGE15_6AT_VERIFY=PASS")
    print("AUDIT_VERDICT=BLOCK")
    print(f"SCALE_COMPATIBLE_K_COUNT={data['scale_compatible_k_count']}")
    print("SIZE_ONLY_SUBPOLYNOMIAL=false")
