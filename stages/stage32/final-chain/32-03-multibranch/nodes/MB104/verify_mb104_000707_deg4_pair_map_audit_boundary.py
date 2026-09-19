#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent

GENUS7_CERT = HERE / "MB104-000707-GENUS7-FIBRATION-CERTIFICATE.json"
GENUS7_VERIFY = HERE / "verify_mb104_000707_genus7_fibration.py"
FULL28_CERT = HERE / "MB104-FULL28-FIBRATION-P-INTERSECTION-AUDIT-CERTIFICATE.json"
FULL28_VERIFY = HERE / "verify_mb104_full28_fibration_p_intersection_audit.py"
RESTR_CERT = HERE / "MB104-000707-DEG4-PAIR-MAP-RESTRICTION-CERTIFICATE.json"
RESTR_NOTE = HERE / "MB104-000707-DEG4-PAIR-MAP-RESTRICTION-REDUCTION-20260920.md"
DISC_CERT = HERE / "MB104-000707-DEG4-PAIR-MAP-DISCRIMINANT-EXCLUSION-CERTIFICATE.json"
DISC_NOTE = HERE / "MB104-000707-DEG4-PAIR-MAP-DISCRIMINANT-EXCLUSION-20260920.md"

EXPECTED_BLOBS = {
    GENUS7_CERT: "f3b158df6b9105d863d8174340ba1adb075a7f1a",
    GENUS7_VERIFY: "fcfa76f662e9575daef87b2da7042159d972a896",
    FULL28_CERT: "798a78d351fa8ec0f3c7d03e865fbdbe6233403e",
    FULL28_VERIFY: "544c85cd468e84671650adaaee84e59d72333243",
    RESTR_CERT: "7b65e7845e0a5028f61afbd85777c541d9eff305",
    RESTR_NOTE: "186173988d6d3d99839d39b7c6b07863e31ba894",
}

def req(ok, msg):
    if not ok:
        raise SystemExit("FAIL: " + msg)

def git_blob(path):
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()

def main():
    # Lock dependencies before interpreting them.
    for path, expected in EXPECTED_BLOBS.items():
        got = git_blob(path)
        req(got == expected, f"blob lock {path.name}: {got} != {expected}")

    g7 = json.loads(GENUS7_CERT.read_text())
    f28 = json.loads(FULL28_CERT.read_text())
    r = json.loads(RESTR_CERT.read_text())
    d = json.loads(DISC_CERT.read_text())
    rn = RESTR_NOTE.read_text()
    dn = DISC_NOTE.read_text()

    req(g7["schema"] == "STAGE32_MB104_000707_GENUS7_FIBRATION_V1", "genus7 schema")
    req(f28["schema"] == "STAGE32_MB104_FULL28_FIBRATION_P_INTERSECTION_AUDIT_V1", "full28 schema")
    req(r["schema"] == "STAGE32_MB104_000707_DEG4_PAIR_MAP_RESTRICTION_V2", "restriction schema")
    req(d["schema"] == "STAGE32_MB104_000707_DEG4_PAIR_MAP_DISCRIMINANT_EXCLUSION_V2", "discriminant schema")

    # Source-complete pair-map numerical adapter.
    req(g7["fiber"]["H_dot"] == 12 and g7["fiber"]["P_dot"] == 36, "G intersections")
    pairs = list(zip(f28["rank3"]["size768_P_dot_G"], g7["rank3_pairings"]))
    req((40, 4) in pairs, "existence of rank3 F with P.F=40 and G.F=4")
    req(f28["rank3"]["half_class_relation"] == "2G=H-sum_B E", "rank3 half-class relation")
    H2 = 16
    HF = H2 // 2
    req(HF == 8, "H.F=8 from half-class relation and H^2=16")

    dat = r["data"]
    req(dat == {
        "H_G": 12, "P_G": 36, "H_F": 8, "P_F": 40, "G_F": 4,
        "pair_map_generic_degree": 4, "P2": 336, "H_P": 112
    }, "restriction data")
    req(r["unexcluded_restriction_degrees"] == [1, 2, 3, 4], "all r remain unexcluded")
    req(all(not v["excluded"] for v in r["restriction_degrees"].values()), "restriction exclusion firewall")
    req(r["common_vertical_correction_required"] is True, "restriction common vertical gate")
    req(r["source_gate"]["stein_factor_common_vertical_audited"] is False, "restriction Stein gate")
    req(all(v is False for v in r["firewalls"].values()), "restriction credit firewalls")

    # Recompute the conditional numerical identities.
    HG, PG, HF, PF, GF, P2, HP = 12, 36, 8, 40, 4, 336, 112
    def q_values(rr):
        qg = 144 // rr - 36 if 144 % rr == 0 else None
        qf = 160 // rr - 40 if 160 % rr == 0 else None
        qh = 768 // rr - 112 if 768 % rr == 0 else None
        q2 = 11520 // (rr*rr) + 336 - 5760 // rr
        return qg, qf, qh, q2

    req(q_values(4)[:2] == (0, 0), "r4 ruling orthogonality")
    req(q_values(3)[2:] == (144, -304), "r3 Q numerics")
    req(1 + (-304 + 144) // 2 == -79, "r3 l=1 conditional pa negative")

    pm = d["pair_map"]
    req(pm["degree"] == GF and pm["H_G"] == HG and pm["P_G"] == PG, "discriminant G adapter")
    req(pm["H_F"] == HF and pm["P_F"] == PF and pm["G_F"] == GF, "discriminant F adapter")
    req(pm["ramification_class"] == "H+2G+2F", "ramification class")
    req(pm["H_dot_ramification"] == H2 + 2*HG + 2*HF == 56, "H.R")

    # C.Q = l^2 P.((40/r)G+(36/r)F-P)
    cq2 = 20*PG + 18*PF - P2
    cq1 = 40*PG + 36*PF - P2
    req(cq2 == 1104 and cq1 == 2544, "C.Q numerics")
    disc2 = 20*HG + 18*HF + 2*(18*GF) + 2*(20*GF)
    disc1 = 40*HG + 36*HF + 2*(36*GF) + 2*(40*GF)
    req(disc2 == 688 and disc1 == 1376, "conditional discriminant degrees")
    req(d["restriction_cases"]["r2"]["two_C_dot_Q_over_l2"] == 2*cq2, "r2 cross intersection")
    req(d["restriction_cases"]["r1"]["two_C_dot_Q_over_l2"] == 2*cq1, "r1 cross intersection")
    req(d["restriction_cases"]["r2"]["conditional_discriminant_degree_over_l"] == disc2, "r2 disc")
    req(d["restriction_cases"]["r1"]["conditional_discriminant_degree_over_l"] == disc1, "r1 disc")
    req(all(not v["excluded"] for v in d["restriction_cases"].values()), "discriminant exclusion firewall")

    c = d["conclusion"]
    req(c["excluded_orbit"] is None and c["excluded_orbit_size"] == 0, "no excluded orbit")
    expected_sizes = {"0000770000ff": 48, "00007b0000ff": 48, "000707000f0f": 768}
    req(c["remaining_orbit_sizes"] == expected_sizes, "remaining orbit sizes")
    req(c["remaining_orbits"] == list(expected_sizes), "remaining orbit order")
    req(c["remaining_support_count"] == sum(expected_sizes.values()) == 864, "remaining support count")
    req(d["common_vertical_correction_required"] is True, "discriminant common vertical gate")
    req(all(v is False for v in d["source_gate"].values()), "discriminant source gates")
    req(all(v is False for v in d["firewalls"].values()), "discriminant credit firewalls")

    req("r=4: OPEN" in rn and "r=3: OPEN" in rn, "restriction note corrected")
    req("No orbit is excluded." in dn, "discriminant note corrected")
    req("size-768 orbit is **not** excluded" in dn, "size768 correction explicit")
    req("excluded PRE-AUDIT" not in dn, "stale pre-audit exclusion removed")

    print("PASS: MB104 000707 degree-4 pair-map audit boundary")
    print("all restriction degrees remain OPEN; excluded orbit count = 0")
    print("remaining balanced support count = 864")
    print("Stein/common-vertical correction remains mandatory; zero mathematical credit")

if __name__ == "__main__":
    main()
