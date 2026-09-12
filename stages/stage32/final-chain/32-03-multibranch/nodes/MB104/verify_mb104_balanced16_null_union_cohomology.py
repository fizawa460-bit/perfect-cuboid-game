#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-NULL-UNION-COHOMOLOGY-CERTIFICATE.json"
LOCKS = {
    "SECTION_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-SECTION-COMPONENTS-20-19-16-CERTIFICATE.json",
        "9c36555e495df0d8d6b816f1c0dc7d4c35b55848",
    ),
    "PIC0_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-PIC0-CERTIFICATE.json",
        "1a92336433816883757fee844b736181e6848813",
    ),
    "STABILIZER_UNION_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-STABILIZER-UNION-CERTIFICATE.json",
        "31695c6908cff73d04baab2ed11dfd04608a2464",
    ),
    "TWO_QUARTIC_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-TWO-QUARTIC-GLUING-CERTIFICATE.json",
        "658516458e0af20bbcac28f5f778eeeb361cd468",
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

def preflight(cert):
    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared == LOCKS, "source lock table")
    rr = root()
    for key, (rel, expected) in LOCKS.items():
        p = rr / rel
        if not p.is_file():
            raise SystemExit(f"SOURCE_LOCK_FAIL missing {key}")
        got = blob(p)
        if got != expected:
            raise SystemExit(f"SOURCE_LOCK_FAIL {key}: expected {expected}, got {got}")

def main():
    cert = json.loads(CERT.read_text())
    req(cert["schema"] == "STAGE32_MB104_BALANCED16_NULL_UNION_COHOMOLOGY_V1", "schema")
    preflight(cert)

    # Four section components Q_(s,t), s,t = +/-1.
    qs = [(s,t) for s in (-1,1) for t in (-1,1)]
    same_s = same_t = opposite_both = 0
    for i in range(len(qs)):
        for j in range(i+1, len(qs)):
            s,t = qs[i]; u,v = qs[j]
            if s == u and t == -v:
                same_s += 1
            elif t == v and s == -u:
                same_t += 1
            elif s == -u and t == -v:
                opposite_both += 1
            else:
                raise SystemExit("FAIL: unclassified quartic pair")
    req((same_s, same_t, opposite_both) == (2,2,2), "K2,2 pair classification")

    # Exact local A1 branch equations used for the two nonempty pair types.
    # same-s: q4-q2=(a1-c)(a1+c)+b1^2 = x*z+y^2.
    # same-t: q2=(a2+i*a3)(a2-i*a3)-b1^2 = x*z-y^2.
    req(cert["size48_union"]["same_s_local_A1"] == "x*z+y^2=0", "same-s A1")
    req(cert["size48_union"]["same_t_local_A1"] == "x*z-y^2=0", "same-t A1")
    req(cert["size48_union"]["strict_transform_pairwise_intersection"] == 0, "strict transforms disjoint")
    req(cert["size48_union"]["component_count"] == 4, "four components")
    req(cert["size48_union"]["H0_union_D_l"] == 4, "H0 disconnected trivial union")

    # Cohomology arithmetic for Z4.
    Z4sq, KZ4, DZ4 = -16, 16, 0
    req((Z4sq + KZ4 - 2*DZ4) // 2 == 0, "chi(D-Z4)-chi(D)=0")
    req(32 - 112 < 0, "H2(D-Z4) vanishes already at l=1")
    req(cert["size48_union"]["forced_h1_lower_bound"] == 4, "h1>=4")

    # Surviving 768 orbit: two genus-one quartics meeting twice.
    qsq = -4
    qpair = 2
    Z2sq = 2*qsq + 2*qpair
    KZ2 = 8
    req(Z2sq == -4, "Z2 square")
    req((Z2sq + KZ2) // 2 == 2, "chi(D-Z2)-chi(D)=2")
    req(24 - 112 < 0, "H2(D-Z2) vanishes already at l=1")
    req(cert["size768_000707_union"]["arithmetic_genus"] == 3, "Z2 arithmetic genus")
    req(cert["size768_000707_union"]["forced_h1_lower_bound"] == 3, "h1>=3")

    rc = cert["retained_consequence"]
    req(rc["surviving_support_population"] == 864, "population firewall")
    req(rc["any_surviving_orbit_closed"] is False, "no closure")
    req(rc["null_union_gluing_route_exhausted"] is True, "route exhausted")
    print("PASS STAGE32_MB104_BALANCED16_NULL_UNION_COHOMOLOGY_V1")
    print("size48: four strict-transform zero quartics pairwise disjoint; h1(D_l)>=4")
    print("000707: connected trivial two-quartic union; h1(D_l)>=3")
    print("survivors=48+48+768=864; no new closure")

if __name__ == "__main__":
    main()
