#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
CERT = Path(__file__).with_name("MB104-H1-SYMMETRY-OVERLAP-CERTIFICATE.json")

LOCAL_LOCKS = {
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB103/CERTIFICATE.json":
        "9cb1e8acc268491a84f0c0e27f4fd39f6cb39d8b",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-CLASS3-ROADMAP-20260918.md":
        "72b06b65d2b16768c4b6af47f549a9f4f5a0a515",
}

SUPPORT_MASKS = [
    "0000770000ff",
    "00007b0000ff",
    "000707000f0f",
    "00070b000f0f",
]

def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def require(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(f"FAIL: {msg}")

def canon(z):
    for x in z:
        if x != 0:
            s = x
            break
    w = tuple(x / s for x in z)
    return tuple(complex(round(x.real), round(x.imag)) for x in w)

def nodes():
    out = []
    for j in range(3):
        for sa in (1, -1):
            for s1 in (1, -1):
                for s2 in (1, -1):
                    z = [0j] * 7
                    z[j] = sa
                    o = [t for t in range(3) if t != j]
                    z[3 + o[0]] = s1
                    z[3 + o[1]] = s2
                    z[6] = 1
                    out.append(tuple(z))
    for j in range(3):
        o = [t for t in range(3) if t != j]
        a, b = o
        for sr in (1, -1):
            for ep in (1, -1):
                for eq in (1, -1):
                    z = [0j] * 7
                    z[a] = 1
                    z[b] = 1j * sr
                    z[3 + a] = 1j * ep
                    z[3 + b] = -eq * sr
                    out.append(tuple(z))
    require(len(out) == 48, "48 nodes")
    return out

def apply_gen(z, k):
    a1, a2, a3, b1, b2, b3, c = z
    if k == 0:
        return (a2, a1, a3, b2, b1, b3, c)
    if k == 1:
        return (a3, a2, a1, b3, b2, b1, c)
    if k == 2:
        return (1j*c, a2, a3, b1, 1j*b3, -1j*b2, -1j*a1)
    if k == 3:
        return (-a1, a2, a3, b1, b2, b3, c)
    if k == 4:
        return (a1, -a2, a3, b1, b2, b3, c)
    if k == 5:
        return (a1, a2, -a3, b1, b2, b3, c)
    if k == 6:
        return (a1, a2, a3, -b1, b2, b3, c)
    if k == 7:
        return (a1, a2, a3, b1, -b2, b3, c)
    if k == 8:
        return (a1, a2, a3, b1, b2, -b3, c)
    raise ValueError(k)

def compose(p, q):
    return tuple(p[q[i]] for i in range(48))

def generate_group():
    V = nodes()
    canonical = [canon(z) for z in V]
    index = {z: i for i, z in enumerate(canonical)}
    require(len(index) == 48, "canonical node uniqueness")
    gens = []
    for k in range(9):
        p = tuple(index[canon(apply_gen(z, k))] for z in V)
        require(sorted(p) == list(range(48)), f"generator {k} permutation")
        gens.append(p)
    ident = tuple(range(48))
    group = {ident}
    stack = [ident]
    while stack:
        a = stack.pop()
        for g in gens:
            h = compose(g, a)
            if h not in group:
                group.add(h)
                stack.append(h)
    require(len(group) == 1536, "Aut(S) node action order")
    return group

def support_from_mask(mask):
    x = int(mask, 16)
    return frozenset(i for i in range(48) if (x >> i) & 1)

def act_set(p, s):
    return frozenset(p[i] for i in s)

def double_cosets(group, H):
    remaining = set(group)
    out = []
    Hlist = list(H)
    while remaining:
        g = next(iter(remaining))
        dc = set()
        for h1 in Hlist:
            h1g = compose(h1, g)
            for h2 in Hlist:
                dc.add(compose(h1g, h2))
        out.append((g, dc))
        remaining.difference_update(dc)
    return out

def summarize(group, support):
    H = {p for p in group if act_set(p, support) == support}
    dcs = double_cosets(group, H)
    by = defaultdict(lambda: {"double_cosets": 0, "elements": 0, "sizes": []})
    for g, dc in dcs:
        t = len(support.intersection(act_set(g, support)))
        by[t]["double_cosets"] += 1
        by[t]["elements"] += len(dc)
        by[t]["sizes"].append(len(dc))
    outside = [t for t in by if t < len(support)]
    return {
        "support_size": len(support),
        "stabilizer_order": len(H),
        "orbit_size": len(group) // len(H),
        "double_coset_count": len(dcs),
        "outside_overlap_values": sorted(outside),
        "max_outside_overlap": max(outside),
        "min_cross_coefficient": 784 - 32 * max(outside),
        "by_overlap": {
            str(t): {
                "double_cosets": by[t]["double_cosets"],
                "elements": by[t]["elements"],
                "double_coset_size_multiset": {
                    str(k): v for k, v in sorted(Counter(by[t]["sizes"]).items())
                },
            }
            for t in sorted(by, reverse=True)
        },
    }

def main():
    for rel, expected in LOCAL_LOCKS.items():
        path = ROOT / rel
        require(path.is_file(), f"missing local source {rel}")
        require(git_blob_sha1(path) == expected, f"source drift {rel}")

    cert = json.loads(CERT.read_text())
    require(cert["schema"] == "STAGE32_MB104_H1_SYMMETRY_OVERLAP_PREFLIGHT_V1", "schema")
    require(cert["status"] == "H1_SHALLOW_FAIL_PARKED_NO_CREDIT", "status")

    group = generate_group()
    require(cert["group_replay"]["generated_group_order"] == len(group), "group order certificate")

    for mask in SUPPORT_MASKS:
        support = support_from_mask(mask)
        got = summarize(group, support)
        expected = cert["group_replay"]["supports"][mask]
        require(got == expected, f"double-coset replay {mask}")
        require(got["max_outside_overlap"] == 13, f"max overlap {mask}")
        require(got["min_cross_coefficient"] == 368, f"cross coefficient {mask}")

    ic = cert["intersection_contract"]
    require(ic["H2"] == 16 and ic["H_E"] == 0 and ic["E_i2"] == -2, "intersection interface")
    for t in range(15):
        require(49*16 - 32*t == 784 - 32*t, f"intersection formula t={t}")

    local = cert["local_lower_bound_contract"]
    require(local["allowed_h1_inputs_force_positive_quadratic_excess"] is False, "no quadratic excess")
    require(local["quadratic_excess_coefficient_lower_bound"] == 0, "zero quadratic lower-bound coefficient")
    require(local["worst_case_forced_shared_landing_upper_bound_linear"] == "14*(8*l)=112*l", "linear ceiling")

    decision = cert["decision"]
    require(decision["shallow_gate"] == "FAIL", "H1 gate must fail")
    require(decision["roadmap_action"] == "PARK_H1", "H1 parked")
    require(decision["h2_released_as_next_shallow_gate"] is True, "H2 next")
    require(decision["new_adapter_proved"] is False, "no adapter")

    fw = cert["credit_firewall"]
    for key in [
        "mb104_complete", "finite_degree_window_proved", "receiver_credit",
        "theorem_credit", "endpoint_credit", "perfect_cuboid_nonexistence_claim",
        "merge_authorized",
    ]:
        require(fw[key] is False, f"credit firewall {key}")

    print("PASS STAGE32_MB104_H1_SYMMETRY_OVERLAP_PREFLIGHT_V1")
    print("AutS=1536 supports=4 max_nonstabilizer_overlap=13 min_cross_coeff=368")
    print("H1=FAIL_PARKED quadratic_excess_coeff=0 next=H2_adapter_gate no_credit")

if __name__ == "__main__":
    main()
