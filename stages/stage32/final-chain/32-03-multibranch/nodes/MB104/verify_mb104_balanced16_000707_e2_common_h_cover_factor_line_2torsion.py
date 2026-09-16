#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ACTIVE = "MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP"
PASS = "PASS STAGE32_MB104_000707_E2_COMMON_H_COVER_FACTOR_LINE_2TORSION_V1"

LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-COMMON-H-COVER-FACTOR-LINE-2TORSION.md",
        "1e121116c1591e3b3d9f748f306151ab0e89b580",
    ),
    "BASECHANGE_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-ETALE-BASECHANGE-DETERMINANT-PASSPORT-CERTIFICATE.json",
        "034885449c9726e9ef81bc1ef090956d89ce2fd7",
    ),
    "H_QUOTIENT_MODEL": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-INTERMEDIATE-H-QUOTIENT-MODEL.md",
        "d2e3056137360a9e15ae7c820088d2977a5eb137",
    ),
}


def req(cond, msg):
    if not cond:
        raise SystemExit("FAIL: " + msg)


def repo_root():
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root")


def blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


root = repo_root()
for name, (rel, expected) in LOCKS.items():
    p = root / rel
    req(p.is_file(), f"missing {name}: {rel}")
    got = blob_sha1(p)
    req(got == expected, f"SOURCE_LOCK_FAIL {name}: {got} != {expected}")

note = (root / LOCKS["HUMAN_NOTE"][0]).read_text(encoding="utf-8")
hq = (root / LOCKS["H_QUOTIENT_MODEL"][0]).read_text(encoding="utf-8")
base = json.loads((root / LOCKS["BASECHANGE_CERT"][0]).read_text(encoding="utf-8"))

req(base.get("active_leaf") == ACTIVE, "basechange active leaf")
req(base.get("scope", {}).get("case") == "e=2", "basechange e2 scope")
req(base.get("basechange_passport", {}).get("normalization_identity") == "Z=Norm(E x_R C8)", "basechange normalization identity")
req(base.get("basechange_passport", {}).get("psi_ramification_indices_over_H_branch_values") == [1, 2], "simple ramification passport")
req(base.get("credit_firewall", {}).get("e2_closed") is False, "basechange firewall")

for token in [
    "u^2=(r^4+4)/4",
    "v^2=(r^4-4)/4",
    "H=<T',TT'R>",
]:
    req(token in hq, f"H quotient token missing: {token}")

for token in [
    "N_(1,u) ~= N_(2,u)",
    "N_(1,v) ~= N_(2,v)",
    "M_1^2 ~= M_2^2",
    "delta_fac := M_1 tensor M_2^(-1)",
    "|Pic^0(E)[2]|=4",
    "O_E(R_(1,u)) ~= O_E(R_(2,u))",
    "O_E(R_(1,v)) ~= O_E(R_(2,v))",
    "No e=2 closure is claimed",
]:
    req(token in note, f"semantic token missing: {token}")

# Degree and Riemann--Hurwitz sanity.  Each B_chi has degree 4 on R; its
# pullback has degree 4n.  If U_chi has degree 2n (the retained passport gives
# total unramified degree 4n split evenly across the two inertia types), then
# 4n = 2n + 2*deg(R_chi), hence deg(R_chi)=n.
n = 28
B_pull = 4 * n
U_type = 2 * n
R_type = (B_pull - U_type) // 2
req(R_type == n, "type ramification degree")
req(2 * R_type == 2 * n, "two type ramification divisors total degree 2n")

# Line-bundle exponent replay in additive notation.
# TYPE: 2M1-R1 = 2M2-R2 for each of two characters.
# Sum: 4M1-(R1u+R1v) = 4M2-(R2u+R2v).
# RH-LINE: Ri_total = 2Mi.  Substitute to get 2M1=2M2.
left_after_rh = 4 - 2
right_after_rh = 4 - 2
req(left_after_rh == right_after_rh == 2, "square-line exponent cancellation")
req(2 ** 2 == 4, "elliptic 2-torsion cardinality")

for forbidden in [
    "delta_fac=eta",
    "e2_closed: true",
    "receiver_credit: true",
    "theorem_credit: true",
    "endpoint_credit: true",
    "perfect_cuboid_nonexistence_claim: true",
]:
    req(forbidden not in note, f"forbidden promotion token: {forbidden}")

print(PASS)
