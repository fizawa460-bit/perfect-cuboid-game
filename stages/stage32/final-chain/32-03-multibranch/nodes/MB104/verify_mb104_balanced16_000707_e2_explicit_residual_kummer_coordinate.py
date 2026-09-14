#!/usr/bin/env python3
import hashlib, json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ACTIVE = "MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP"
LOCKS = {
    "SOURCE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FREITAG-SALVATI-MANNI-RESIDUAL-KUMMER-COORDINATE-SOURCE-NOTE.md",
        "a49f5b28b456dd88436c030e857cf771e5a1ba2f",
    ),
    "PROOF": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-EXPLICIT-RESIDUAL-KUMMER-COORDINATE.md",
        "5017d7c137f6d4994a34cb1edac28aadcd832a2a",
    ),
    "CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-EXPLICIT-RESIDUAL-KUMMER-COORDINATE-CERTIFICATE.json",
        "38bdf0155a6965093b17976974ea6514ab212774",
    ),
    "AMBIENT_WRAPPER": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_balanced16_000707_e2_ambient_kummer_conductor_chain.py",
        "c4671b94b54ce12b45032365df606debb5bee90f",
    ),
    "AMBIENT_CHARACTER": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-AMBIENT-CHARACTER-FUNCTION.md",
        "2bdb46e79be8a745880622c9c0643eb13ef20b26",
    ),
    "SQRT_BASECHANGE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-SQRT-FACTOR-BASECHANGE-SEMANTICS.md",
        "9d688ee48fd0df8d7ad4e2c6abc146fa2728ba7e",
    ),
    "STATE": (
        "stages/stage32/final-chain/32-03-multibranch/STATE.json",
        "b4e34e9e6db30de02adbf88c0f635027fbd04550",
    ),
    "PRIORITY": (
        "stages/stage32/final-chain/32-03-multibranch/PRIORITY-OVERRIDE-20260912.json",
        "73cc0979adffe0b17fccfe9705d3e1b86e0f04dd",
    ),
}

def req(cond, msg):
    if not cond:
        raise SystemExit("FAIL: " + msg)

def root():
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root")

def blob(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()

def main():
    r = root()
    for key, (rel, want) in LOCKS.items():
        p = r / rel
        req(p.is_file(), f"missing {key}")
        req(blob(p) == want, f"source lock {key}")

    cp = subprocess.run(
        [sys.executable, str(r / LOCKS["AMBIENT_WRAPPER"][0])],
        cwd=r, capture_output=True, text=True
    )
    req(cp.returncode == 0, "ambient wrapper replay")
    req("PASS STAGE32_MB104_000707_E2_AMBIENT_KUMMER_CONDUCTOR_CHAIN_V1" in cp.stdout,
        "ambient wrapper token")

    cert = json.loads((r / LOCKS["CERT"][0]).read_text())
    state = json.loads((r / LOCKS["STATE"][0]).read_text())
    pri = json.loads((r / LOCKS["PRIORITY"][0]).read_text())
    proof = (r / LOCKS["PROOF"][0]).read_text()
    src = (r / LOCKS["SOURCE"][0]).read_text()

    req(cert["active_leaf"] == ACTIVE, "certificate leaf")
    req(state["next_obligation"]["active_leaf"] == ACTIVE, "STATE leaf")
    req(pri["next_execution_leaf"] == ACTIVE, "priority leaf")

    ch_e = (-1, 1, 1)
    ch_c = (1, 1, -1)
    ch_d = (1, 1, -1)
    ch_r0 = tuple(a*b for a,b in zip(ch_e, ch_d))
    req(ch_r0 == (-1, 1, -1), "r0 character")
    def eval_char(word):
        return ch_r0[0]**word[0] * ch_r0[1]**word[1] * ch_r0[2]**word[2]
    req(eval_char((0,1,0)) == 1, "T' must fix r0")
    req(eval_char((1,1,1)) == 1, "TT'R must fix r0")
    req(eval_char((1,0,0)) == -1, "T must negate r0")
    req(ch_c == ch_d, "c/d must be G-invariant")

    ex = cert["exact_result"]
    req(ex["H"] == "<T',TT'R>", "H")
    req(ex["residual_generator"] == "T H", "residual generator")
    req(ex["residual_equation"] == "r0^2=2*f_t", "Kummer equation")
    req(ex["H_invariant"] is True, "H invariance")
    req(ex["generates_kR_over_kS"] is True, "quadratic generator")

    for token in [
        "f_t=(t-i)/(t+i)=X/Y",
        "r0^2=2*X/Y=2*f_t",
        "k(R)=k(S)(r0)",
        "T H : r0 -> -r0",
    ]:
        req(token in proof, f"proof token {token}")
    req("conductor preimage evaluation still missing" in proof.lower(), "proof missing-datum status")
    req("e^2 = 2*c*d" in src, "theta identity source")
    req("T  : (+,-,+,+,+)" in src, "T action source")
    req("T' : (+,+,-,+,+)" in src, "T' action source")
    req("R  : (+,+,+,-,-)" in src, "R action source")

    missing = cert["remaining_missing_datum"]
    req(missing["abstract_residual_cover_equation_missing"] is False, "abstract cover resolved")
    req(missing["conductor_preimage_to_R_evaluation_missing"] is True, "preimage evaluation remains")
    req(missing["relative_r0_sign_at_conductor_pairs_missing"] is True, "relative sign remains")
    req(missing["weighted_cut_upper_bound_proved"] is False, "no cut upper bound")

    fw = cert["credit_firewall"]
    for key in [
        "e2_closed","e4_closed","mask_000707_closed","mb104_complete",
        "finite_degree_window_proved","receiver_credit","effectivity_credit",
        "theorem_credit","endpoint_credit","perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim","heavy_compute_authorized","merge_authorized"
    ]:
        req(fw[key] is False, f"firewall {key}")

    print("PASS STAGE32_MB104_000707_E2_EXPLICIT_RESIDUAL_KUMMER_COORDINATE_V1")
    print("retained: k(R)=k(S)(r0), r0^2=2*f_t, residual deck r0->-r0")
    print("open: conductor-preimage r0 evaluation; e=2/e=4/000707; credit 0")

if __name__ == "__main__":
    main()
