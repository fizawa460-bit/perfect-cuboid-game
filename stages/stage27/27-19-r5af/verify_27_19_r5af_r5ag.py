from math import gcd, isqrt
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
R5AF = Path(__file__).with_name("result.md")
R5AG = ROOT / "stages" / "stage27" / "27-19-r5ag" / "result.md"
CONTRACT = Path(__file__).with_name("route-contract.json")


def is_square(n: int) -> bool:
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def stress_data(u: int, v: int):
    delta = 2 * u * v
    m = u * u - 5 * v * v
    r = u * u + 5 * v * v
    n = 2 * delta
    s = delta
    M = m * m + n * n
    K = r * r - s * s
    h = u**4 + 6 * u * u * v * v + 25 * v**4
    p, q = 1, 4
    g = delta * delta * h

    E = 4 * m * n * r * s
    X = 2 * r * s * (m * m - n * n)
    Y = 2 * m * n * (r * r - s * s)
    Gamma = gcd(gcd(abs(E), abs(X)), abs(Y))
    raw_R2 = E * E + X * X + Y * Y
    physical_R2_num = raw_R2 // (Gamma * Gamma)

    U = m * m * r * r + n * n * s * s
    V = m * m * s * s + n * n * r * r
    J = m * m + delta * delta

    return {
        "delta": delta,
        "m": m,
        "n": n,
        "r": r,
        "s": s,
        "M": M,
        "K": K,
        "h": h,
        "p": p,
        "q": q,
        "g": g,
        "E": E,
        "X": X,
        "Y": Y,
        "Gamma": Gamma,
        "raw_R2": raw_R2,
        "physical_R2_num": physical_R2_num,
        "U": U,
        "V": V,
        "J": J,
    }


def F(u: int, v: int) -> int:
    return (
        5 * u**12
        - 34 * u**10 * v**2
        + 195 * u**8 * v**4
        + 3620 * u**6 * v**6
        + 4875 * u**4 * v**8
        - 21250 * u**2 * v**10
        + 78125 * v**12
    )


def verify_stress_family() -> None:
    checked = 0
    exact_two_checked = 0
    space_fail_checked = 0
    combined_congruence_checked = 0

    for v in range(2, 132, 2):
        for u in range(6 * v + 1, 7 * v):
            if u % 2 == 0 or gcd(u, v) != 1 or u % 5 == 0:
                continue
            z = stress_data(u, v)
            delta = z["delta"]
            m, n, r, s = z["m"], z["n"], z["r"], z["s"]

            assert m > n > 0
            assert r > s > 0
            assert gcd(m, n) == 1
            assert gcd(r, s) == 1
            assert gcd(n, s) == delta
            assert z["M"] == z["K"] == z["h"]
            assert r * r - m * m == 5 * delta * delta
            assert z["Gamma"] == 2 * delta
            assert z["raw_R2"] == 4 * z["U"] * z["V"]
            assert z["physical_R2_num"] == z["raw_R2"] // (4 * delta * delta)

            expected_R2 = (
                5
                * (u * u - 4 * u * v + 5 * v * v)
                * (u * u - 2 * u * v + 5 * v * v) ** 2
                * (u * u + 2 * u * v + 5 * v * v) ** 2
                * (u * u + 4 * u * v + 5 * v * v)
            )
            assert z["physical_R2_num"] == expected_R2

            # r5ag exact normalized receiver on the stress family.
            assert z["U"] == z["h"] * z["J"]
            assert z["V"] == delta * delta * z["h"] * (z["p"] + z["q"])
            assert z["Gamma"] ** 2 * z["physical_R2_num"] == (
                4 * delta * delta * z["h"] ** 2 * z["J"] * (z["p"] + z["q"])
            )
            checked += 1

            is_exact_two_congruence = u % 11 == 1 and v % 11 == 4
            is_space_fail_congruence = v % 3 == 0 and u % 3 != 0

            if is_exact_two_congruence:
                assert F(u, v) % 11 == 8
                assert not is_square(z["X"] * z["X"] + z["Y"] * z["Y"])
                exact_two_checked += 1

            if is_space_fail_congruence:
                assert z["J"] % 3 == 1
                assert (5 * z["J"]) % 3 == 2
                assert not is_square(5 * z["J"])
                space_fail_checked += 1

            if is_exact_two_congruence and is_space_fail_congruence:
                assert not is_square(z["X"] * z["X"] + z["Y"] * z["Y"])
                assert not is_square(5 * z["J"])
                combined_congruence_checked += 1

    assert checked > 1000
    assert exact_two_checked > 0
    assert space_fail_checked > 0
    assert combined_congruence_checked > 0

    assert F(1, 4) % 11 == 8
    assert 8 not in {x * x % 11 for x in range(11)}


def verify_text_contract() -> None:
    r5af = R5AF.read_text(encoding="utf-8")
    for marker in [
        "TASK_ID=Stage27-19-r5af",
        "R402A_HEIGHT_BOX_FIXED_TAU_HALFPOWER_SATURATION_PROVED=true",
        "EXACT_PRIMITIVE_SCALE_ON_STRESS_FAMILY=Gamma=2*delta",
        "EXACT_PHYSICAL_HEIGHT_STRESS_GROWTH=R_asymp_v^6",
        "GLOBAL_B_ONE_THIRD_UPPER_PROVED=false",
        "NEXT_DERIVED_ROUTE=27-19-r5ag",
    ]:
        assert marker in r5af, marker

    r5ag = R5AG.read_text(encoding="utf-8")
    for marker in [
        "TASK_ID=Stage27-19-r5ag",
        "EXACT_NORMALIZED_PHYSICAL_HEIGHT_IDENTITY_PROVED=true",
        "EXACT_NORMALIZED_PHYSICAL_HEIGHT_IDENTITY=Gamma^2*R^2=4*delta^2*h^2*J*(p+q)",
        "PRIMITIVE_SCALE_RETAINED=true",
        "R402C_EXPONENT_IMPROVED=false",
        "STRICT_SUB_SQRT_UPPER_PROVED=false",
        "NEXT_DERIVED_ROUTE=27-19-r5ah",
    ]:
        assert marker in r5ag, marker

    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    assert contract["task_id"] == "Stage27-19-r5af"
    assert contract["batch_id"] == "Stage27-19-r5"
    assert contract["batch_routes"] == ["27-19-r5af", "27-19-r5ag"]
    assert contract["proved"]["exact_normalized_physical_height_identity"] is True
    assert contract["not_proved"]["strict_sub_sqrt_upper"] is True


if __name__ == "__main__":
    verify_stress_family()
    verify_text_contract()
    print("Stage27-19-r5af/r5ag verifier: PASS")
