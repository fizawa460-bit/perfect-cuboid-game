def base_discriminant_j1728() -> int:
    # y^2 = x^3 - x, short Weierstrass discriminant -16(4a^3+27b^2)
    a = -1
    b = 0
    return -16 * (4 * a**3 + 27 * b**2)


def sixth_power_free(n: int) -> bool:
    n = abs(n)
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e >= 6:
            return False
        p += 1 if p == 2 else 2
    return True


def audit():
    delta = base_discriminant_j1728()
    assert delta == 64
    assert sixth_power_free(delta) is False
    return {
        "delta": delta,
        "nara_direct": False,
        "covering_height_adapter": False,
        "global_twist_count": False,
    }


if __name__ == "__main__":
    data = audit()
    print("STAGE15_6AS_VERIFY=PASS")
    print("AUDIT_VERDICT=BLOCK")
    print(f"BASE_DISCRIMINANT={data['delta']}")
    print("NARA_DIRECTLY_APPLICABLE=false")
