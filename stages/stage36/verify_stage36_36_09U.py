#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"
CERT = ROOT / "stages" / "stage36" / "36-09U" / "qi-antiinvariant-rankjump-descent-preflight.json"
T_CERT = ROOT / "stages" / "stage36" / "36-09T" / "simultaneous-two-quotient-qi-rankjump-preflight.json"
R_CERT = ROOT / "stages" / "stage36" / "36-09R" / "etau-rankjump-receiver-esigmatau-growth-preflight.json"
S_CERT = ROOT / "stages" / "stage36" / "36-09S" / "esigmatau-torsion-growth-exclusion-preflight.json"
O_CERT = ROOT / "stages" / "stage36" / "36-09O" / "physical-square-lift-v4-quotient-preflight.json"
I_CERT = ROOT / "stages" / "stage36" / "36-09I" / "post-w01-breadth-refresh.json"
DESCENT_SOURCE = ROOT / "stages" / "stage36" / "36-09N" / "relative-2isogeny-specialization-source-lock.md"

BASE = "a3c64f5704f3d1fd297e3b95377ba1938d277178"
V54_BLOB = "e94e6dd4ca25dd5da20acf8d97fd54d967048727"
CERT_BLOB = "a1f0c924d267ab4f45aaada6c9bcb3a5f544f284"
T_BLOB = "1191de3e0176aac4ad10bd7b346830279ce12805"
R_BLOB = "b55d042ede01032ff8c8b0d872510a53cb857969"
S_BLOB = "3af506b590c5e4d7499c203651c0bf4ef31ec767"
O_BLOB = "6a2678ebedba40e13277100441361039ee47ca28"
I_BLOB = "f9bf252f3be47f606a3b270961df3b5943fa1909"
DESCENT_BLOB = "a562d7053a6f04deff4473067777b7cfd538ea8a"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def trim(a: list[int]) -> list[int]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a: list[int], b: list[int]) -> list[int]:
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    return trim(out)


def scale(a: list[int], c: int) -> list[int]:
    return trim([c * x for x in a])


def mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def powp(a: list[int], n: int) -> list[int]:
    out = [1]
    for _ in range(n):
        out = mul(out, a)
    return out


def main() -> None:
    assert git("rev-parse", f"{BASE}:stages/stage36/MAIN-STATE.json") == V54_BLOB
    assert blob(CERT) == CERT_BLOB
    assert blob(T_CERT) == T_BLOB
    assert blob(R_CERT) == R_BLOB
    assert blob(S_CERT) == S_BLOB
    assert blob(O_CERT) == O_BLOB
    assert blob(I_CERT) == I_BLOB
    assert blob(DESCENT_SOURCE) == DESCENT_BLOB

    c = json.loads(CERT.read_text())
    t = json.loads(T_CERT.read_text())
    r = json.loads(R_CERT.read_text())
    s36 = json.loads(S_CERT.read_text())
    o = json.loads(O_CERT.read_text())
    i36 = json.loads(I_CERT.read_text())

    assert c["schema"] == "STAGE36_36_09U_QI_ANTIINVARIANT_RANKJUMP_DESCENT_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    assert c["entry_authority"]["36_09T_hostile_audit_review"] == 5124828133
    assert c["entry_authority"]["36_09T_promotion_merge"] == BASE

    # Exact polynomial identities over Z[p]. Coefficients are low-to-high.
    P = [0, 1]
    ONE = [1]
    p2 = powp(P, 2)
    Nm = add(add(p2, scale(P, -2)), [-1])
    Np = add(add(p2, scale(P, 2)), [-1])
    ss = add(p2, ONE)
    C = mul(Nm, Np)
    D = mul(P, add(p2, [-1]))

    assert add(powp(Nm, 2), powp(Np, 2)) == scale(powp(ss, 2), 2)
    assert add(powp(Np, 2), scale(powp(Nm, 2), -1)) == scale(D, 8)
    assert add(powp(C, 2), scale(powp(D, 2), 16)) == powp(ss, 4)

    # Dual 2-isogeny coefficient identity and factorization.
    dual_b = add(scale(powp(ss, 4), 4), scale(powp(C, 2), -4))
    assert dual_b == scale(powp(D, 2), 64)
    root1 = scale(p2, 16)
    root2 = scale(powp(add(p2, [-1]), 2), 4)
    assert add(root1, root2) == scale(powp(ss, 2), 4)
    assert mul(root1, root2) == scale(powp(D, 2), 64)

    # Gaussian fourth-power identity: (p+i)^4 = C + 4 i D.
    def gmul(z1: tuple[list[int], list[int]], z2: tuple[list[int], list[int]]) -> tuple[list[int], list[int]]:
        a, b = z1
        c2, d = z2
        return add(mul(a, c2), scale(mul(b, d), -1)), add(mul(a, d), mul(b, c2))

    z = (P, ONE)
    z2 = gmul(z, z)
    z4 = gmul(z2, z2)
    assert z4[0] == C
    assert z4[1] == scale(D, 4)

    # Audited inputs and the exact Kummer-growth consequence.
    assert r["generic_E_sigma_tau_MW"]["generic_rank"] == 0
    assert r["generic_E_sigma_tau_MW"]["exact_generic_torsion"] == "Z/2 x Z/2"
    assert s36["conclusion"]["E_SIGMA_TAU_TORSION_GROWTH_EXCLUDED"] is True
    assert s36["conclusion"]["retained_fiber_torsion_exact"] == "Z/2 x Z/2"
    assert t["minus_one_twist"]["generic_rank_E_sigma_over_Qi_p"] == 1
    assert t["receiver_rankjump_consequence"]["receiver_forces_E_sigma_rank_over_Qi_at_least"] == 2
    assert t["receiver_rankjump_consequence"]["receiver_forces_genuine_Qi_rank_jump"] is True

    kb = c["generic_kummer_baseline"]
    assert kb["beta_baseline_size"] == 4
    assert kb["generic_exact_alpha_image"] == ["[1]"]
    assert kb["generic_exact_beta_image"] == ["[1]", "[-1]", "[2*D]", "[-2*D]"]
    assert c["receiver_rankjump_dichotomy"]["dichotomy_is_equivalent_to_positive_rank_via_index_formula"] is True
    assert c["receiver_rankjump_dichotomy"]["candidate_set_shrunk"] is False

    assert o["gaussian_bridge_note"]["C2_status"].startswith("UNTESTED_DISTINCT_ROUTE")
    assert i36["candidate_separation_repair"]["C2_new_candidate"] == "GAUSSIAN_NORM_COMPRESSION"
    assert c["gaussian_fourth_power_bridge"]["C2_GAUSSIAN_NORM_COMPRESSION_status"] == "EXACT_GAUSSIAN_FOURTH_POWER_ADAPTER_READY_BUT_NO_PRIME_IDEAL_COMPRESSION_THEOREM_YET"

    st = json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V55_36_09U_BATCHED"
    assert st["status"] == "ACTIVE_BATCHING_SUBSTANTIVE_PR"
    assert st["base_main_sha"] == BASE
    u = st["authority_frontier"]["36-09U"]
    assert u["status"] == "EXACT_ANTIINVARIANT_KUMMER_DICHOTOMY_AND_GAUSSIAN_FOURTH_POWER_BRIDGE_BATCHED_PENDING_AUDIT"
    assert u["certificate_blob_sha"] == CERT_BLOB
    assert u["QI_ANTIINVARIANT_DESCENT_REDUCES_TO_E_SIGMA_TAU_Q_DESCENT"] is True
    assert u["GENERIC_ALPHA_IMAGE"] == ["[1]"]
    assert u["GENERIC_BETA_IMAGE"] == ["[1]", "[-1]", "[2*D]", "[-2*D]"]
    assert u["RECEIVER_FORCES_KUMMER_IMAGE_GROWTH"] is True
    assert u["GAUSSIAN_FOURTH_POWER_BRIDGE"] == "C+4*i*D=(p+i)^4"
    assert u["CANDIDATE_SET_SHRUNK"] is False
    assert u["QI_RANKJUMP_LOCUS_EMPTY"] is False
    assert st["current"]["unit"] == "36-09V"
    assert st["current"]["next_exact_leaf"] == "36-09V_GAUSSIAN_FOURTH_POWER_PRIME_IDEAL_DIRECTIONAL_COMPRESSION_PREFLIGHT"
    assert st["current"]["36_09V_entry_allowed"] is True
    assert st["promotion_gates"]["36_09U_hostile_audit_passed"] is False
    assert st["promotion_gates"]["Gaussian_prime_ideal_compression_proved"] is False
    assert st["promotion_gates"]["receiver_emptiness_proved"] is False
    assert st["claims"]["candidate_set_shrunk"] is False
    assert st["claims"]["perfect_cuboid_nonexistence_claim"] is False

    print("36-09U anti-invariant 2-isogeny Kummer dichotomy and Gaussian fourth-power bridge verified; batched audit deferred; 36-09V unlocked")


if __name__ == "__main__":
    main()
