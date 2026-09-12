#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-CHARACTER-PAIR-SQUARE-WALL-CERTIFICATE.json"
LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-CHARACTER-PAIR-SQUARE-WALL.md",
        "657653c56f8e36be505bbca663e60ef3a937a044",
    ),
    "RESIDUAL_CHARACTER_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-RESIDUAL-SHEET-CHARACTER-CERTIFICATE.json",
        "5e12d24f85d1fe27e53edab337bbacc45fb34cdb",
    ),
    "FIBRATION_SOURCE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/STOLL-TESTA-G2-ISOTRIVIAL-FIBRATION-SOURCE-NOTE.md",
        "b71225ac859eef5afefeebd019a97c403ed27655",
    ),
}
ZERO = (0, 0, 0, 0, 0)


def req(c, m):
    if not c:
        raise SystemExit("FAIL: " + m)


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


def clean(p):
    return {m: v for m, v in p.items() if v != 0}


def const(z):
    return {} if z == 0 else {ZERO: complex(z)}


def var(j):
    e = [0] * 5
    e[j] = 1
    return {tuple(e): 1 + 0j}


def add(a, b):
    out = dict(a)
    for m, v in b.items():
        out[m] = out.get(m, 0) + v
    return clean(out)


def neg(a):
    return {m: -v for m, v in a.items()}


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    out = {}
    for ma, va in a.items():
        for mb, vb in b.items():
            m = tuple(x + y for x, y in zip(ma, mb))
            out[m] = out.get(m, 0) + va * vb
    return clean(out)


def scale(z, a):
    return {m: z * v for m, v in a.items() if z * v != 0}


def sq(a):
    return mul(a, a)


def preflight(cert):
    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared == LOCKS, "source-lock table")
    rr = root()
    for k, (rel, sha) in LOCKS.items():
        p = rr / rel
        if not p.is_file():
            raise SystemExit(f"SOURCE_LOCK_FAIL missing {k}")
        got = blob(p)
        if got != sha:
            raise SystemExit(f"SOURCE_LOCK_FAIL {k}: expected {sha}, got {got}")


def main():
    cert = json.loads(CERT.read_text())
    req(cert["schema"] == "STAGE32_MB104_BALANCED16_000707_CHARACTER_PAIR_SQUARE_WALL_V1", "schema")
    preflight(cert)
    rc = json.loads((root() / LOCKS["RESIDUAL_CHARACTER_CERT"][0]).read_text())
    req(rc["scope"]["mask"] == "000707000f0f", "mask")
    req(rc["scope"]["node_type_counts"] == [7, 7, 0], "absent b3 type")
    req(rc["joint_factor_constraint"]["eta_1_equals_eta_2"] is True, "upstream eta equality")

    a1, a2, a3, c, b3 = [var(j) for j in range(5)]
    I = 1j
    R = sub(sub(sub(sq(c), sq(a1)), sq(a2)), sq(a3))
    B = sub(sub(sq(b3), sq(c)), neg(sq(a3)))  # b3^2-c^2+a3^2

    Nt = sub(add(add(c, a1), a3), scale(I, a2))
    Dt = add(sub(add(c, a1), a3), scale(I, a2))
    Nu = sub(sub(add(c, a1), a3), scale(I, a2))
    Du = add(add(add(c, a1), a3), scale(I, a2))

    # (Nt/Dt)/(Nu/Du)=(c+a3)/(c-a3) modulo R.
    lhs = sub(mul(mul(Nt, Du), sub(c, a3)), mul(mul(Dt, Nu), add(c, a3)))
    rhs = scale(2, mul(a3, R))
    req(lhs == rhs, "exact factor-character ratio identity modulo canonical quadric")

    # (c+a3)/(c-a3)=((c+a3)/b3)^2 modulo b3^2=c^2-a3^2.
    lhs2 = sub(mul(add(c, a3), sq(b3)), mul(sub(c, a3), sq(add(c, a3))))
    rhs2 = mul(add(c, a3), B)
    req(lhs2 == rhs2, "exact global-square identity modulo b3 equation")

    ch = cert["characters"]
    req(ch["f_t"] == "(t-i)/(t+i)" and ch["f_u"] == "(u-i)/(u+i)", "character reps")
    req(ch["global_square"] == "f_t/f_u=((c+a3)/b3)^2", "certificate square")
    co = cert["consequence"]
    req(co["eta_1_equals_eta_2_automatic"] is True, "automatic eta equality")
    req(co["joint_character_inequality_route_exhausted"] is True, "route wall")
    req(co["e2_iff_common_eta_zero"] is True and co["e4_iff_common_eta_nonzero"] is True, "case firewall")
    fw = cert["credit_firewall"]
    req(fw["e2_closed"] is False and fw["e4_closed"] is False and fw["orbit_000707_closed"] is False, "no closure")
    req(fw["MB104_complete"] is False and fw["merge_authorized"] is False, "credit/merge firewall")

    print("PASS STAGE32_MB104_BALANCED16_000707_CHARACTER_PAIR_SQUARE_WALL_V1")
    print("f_t/f_u=(c+a3)/(c-a3)=((c+a3)/b3)^2 exactly on the cuboid surface")
    print("eta_1=eta_2 is automatic; only one-factor square/non-square status remains")
    print("firewall: e=2,e=4 and 000707 remain open")


if __name__ == "__main__":
    main()
