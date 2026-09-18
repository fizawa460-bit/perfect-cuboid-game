#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
H = 10

CURRENT_LOCKS = {
    "compressed_terminal_family": (
        "stages/stage32/residual-32-01-production/compressed_terminal_family.py",
        "90ff82ed312dcc0cb32cf207935945f550e29170",
    ),
    "pairing_prefix_engine": (
        "stages/stage32/residual-32-01-production/pairing_prefix_engine.py",
        "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    ),
}

HISTORICAL_LOCKS = {
    "td02_grf04_integer_lattice_kernel": {
        "source_branch": "stage32-01-178-topdown-grf02-hpadj08",
        "path": "stages/stage32/32-01-178/topdown-02/verify_td02_grf04_integer_lattice_kernel.py",
        "git_blob_sha1": "d51a8edbfc4fb2c8e46dc9ea788ca43a7587f054",
    },
    "td02_grf04_bounded": {
        "source_branch": "stage32-01-178-topdown-grf02-hpadj08",
        "path": "stages/stage32/32-01-178/topdown-02/verify_td02_grf04_bounded.py",
        "git_blob_sha1": "8dc7b6255b31a79aa7f51141f1ac5a5b8137efc0",
    },
    "bc2_18_mod8_checkpoint": {
        "source_branch": "stage32ex5-hpadj09-successor-20260915",
        "path": "stages/stage32-ex5/breadth-cycle-2/bc2-18-n354-survivor-selected-exceptional-mod8-checkpoint.json",
        "git_blob_sha1": "0e269d5ec6da24b9b887b6dd40f4b4f33242e154",
    },
    "hpadj09_mod8_verifier": {
        "source_branch": "stage32ex5-hpadj09-successor-20260915",
        "path": "stages/stage32-ex5/hpadj-09_ex5/verify_hpadj09_mod8_quotient.py",
        "git_blob_sha1": "feea2b9cb89638d36816fd63ac27dc49b6259cfa",
    },
    "hpadj09_result": {
        "source_branch": "stage32ex5-hpadj09-successor-20260915",
        "path": "stages/stage32-ex5/hpadj-09_ex5/RESULT.json",
        "git_blob_sha1": "e545ccdbd30e6ecc786df6fbb55ee22a3cbfc4fc",
    },
}

PICARD = {
    "modulus": 8,
    "free_selected_exceptional_generators": 19,
    "normal_quotient_index": 748288838313422294120286634350736906063837462003712,
    "normal_plus_free_quotient_index": 46768052394588893382517914646921056628989841375232,
    "fixed_image_size": 2,
    "mu_universal_upper_bound": 8,
}

EXPECTED = {
    "bc_assignment_count": 78945,
    "bc_full_state_count": 18294,
    "bc_full_stream_sha256": "f3de8e9a04389781f9bf97c503604adc1470eff2fbef57aa4994ccbeb60b5c22",
    "bc_k8_base_state_count": 3800,
    "bc_k8_stream_sha256": "015e5e5fbe710b03757b1a7f3d6a0638bce1176ca4060d6340add57e1896d037",
    "a_assignment_count": 286,
    "a_full_state_count": 66,
    "a_full_stream_sha256": "ab58f7bb7e952832ceac47efddf66d395735ab81a1a1dc6f18a0ade34956c2bd",
}


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def counter_hash(c: Counter) -> str:
    h = hashlib.sha256()
    for key, mult in sorted(c.items()):
        h.update((json.dumps([*key, mult], separators=(",", ":")) + "\n").encode())
    return h.hexdigest()


def mapping_hash(m: dict) -> str:
    h = hashlib.sha256()
    for key, value in sorted(m.items()):
        payload = [*key, [list(pair) for pair in value]]
        h.update((json.dumps(payload, separators=(",", ":")) + "\n").encode())
    return h.hexdigest()


def direct_bc() -> Counter:
    out = Counter()
    for x0 in range(H + 1):
        for x1 in range(H + 1):
            for x5 in range(H + 1):
                for x6 in range(H + 1):
                    for x8 in range(H + 1):
                        for x9 in range(H + 1):
                            for x10 in range(H + 1):
                                b = x1 + x5 + x9
                                c = x0 + x8 + x6 + x10
                                if b > H or c > H:
                                    continue
                                if x0 > x1:
                                    continue
                                if x0 == x1 and (x5, x6) > (x8, x9):
                                    continue
                                if (x1 + x8 + x9 + x10) & 1:
                                    continue
                                vals = (x0, x1, x5, x6, x8, x9, x10)
                                support = sum(v > 0 for v in vals)
                                t = x0 + x1 + x6 + x9
                                r = (x0 + x8 + x10) & 1
                                q = sum(v * v for v in vals)
                                out[(b, c, support, t, r, q)] += 1
    return out


def compact_bc() -> Counter:
    B = [[[defaultdict(int) for _ in range(2)] for __ in range(3)] for ___ in range(H + 1)]
    C = [[[defaultdict(int) for _ in range(2)] for __ in range(4)] for ___ in range(H + 1)]
    for m in range(H + 1):
        for x9 in range(m + 1):
            x5 = m - x9
            B[m][int(x5 > 0) + int(x9 > 0)][x9 & 1][(x5*x5 + x9*x9, x9)] += 1
        for x8 in range(m + 1):
            for x10 in range(m - x8 + 1):
                x6 = m - x8 - x10
                C[m][int(x6 > 0) + int(x8 > 0) + int(x10 > 0)][(x8 + x10) & 1][
                    (x6*x6 + x8*x8 + x10*x10, x6)
                ] += 1

    out = Counter()

    for x0 in range(H + 1):
        extra = int(x0 > 0) + 1
        for x1 in range(x0 + 1, H + 1):
            parity = x1 & 1
            q01 = x0*x0 + x1*x1
            for g2 in range(H - x1 + 1):
                b = x1 + g2
                for g3 in range(H - x0 + 1):
                    c = x0 + g3
                    for sb in range(3):
                        for pb in (0, 1):
                            left = B[g2][sb][pb]
                            if not left:
                                continue
                            for sc in range(4):
                                cpar = pb ^ parity
                                right = C[g3][sc][cpar]
                                if not right:
                                    continue
                                support = sb + sc + extra
                                r = (x0 & 1) ^ cpar
                                for (ql, x9), vl in left.items():
                                    for (qr, x6), vr in right.items():
                                        t = x0 + x1 + x6 + x9
                                        out[(b, c, support, t, r, q01 + ql + qr)] += vl * vr

    for x0 in range(H + 1):
        cap = H - x0
        for x5 in range(cap + 1):
            for x8 in range(x5 + 1, cap + 1):
                for x9 in range(cap - x5 + 1):
                    b = x0 + x5 + x9
                    for x6 in range(cap - x8 + 1):
                        for x10 in range(cap - x8 - x6 + 1):
                            c = x0 + x8 + x6 + x10
                            if (x0 + x8 + x9 + x10) & 1:
                                continue
                            vals = (x0, x0, x5, x6, x8, x9, x10)
                            support = sum(v > 0 for v in vals)
                            t = 2*x0 + x6 + x9
                            r = (x0 + x8 + x10) & 1
                            q = sum(v*v for v in vals)
                            out[(b, c, support, t, r, q)] += 1

    for x0 in range(H + 1):
        cap = H - x0
        for x5 in range(cap + 1):
            x8 = x5
            for x6 in range(cap - x8 + 1):
                for x9 in range(x6, cap - x5 + 1):
                    b = x0 + x5 + x9
                    for x10 in range(cap - x8 - x6 + 1):
                        c = x0 + x8 + x6 + x10
                        if (x0 + x8 + x9 + x10) & 1:
                            continue
                        vals = (x0, x0, x5, x6, x8, x9, x10)
                        support = sum(v > 0 for v in vals)
                        t = 2*x0 + x6 + x9
                        r = (x0 + x8 + x10) & 1
                        q = sum(v*v for v in vals)
                        out[(b, c, support, t, r, q)] += 1
    return out


def direct_a() -> Counter:
    out = Counter()
    for a in range(H + 1):
        for x2 in range(a + 1):
            for x3 in range(a - x2 + 1):
                x7 = a - x2 - x3
                support = sum(v > 0 for v in (x2, x3, x7))
                q = x2*x2 + x3*x3 + x7*x7
                out[(a, support, q)] += 1
    return out


def dp_a() -> Counter:
    dp = Counter({(0, 0, 0): 1})
    for _ in range(3):
        nxt = Counter()
        for (a, support, q), mult in dp.items():
            for x in range(H - a + 1):
                nxt[(a + x, support + int(x > 0), q + x*x)] += mult
        dp = nxt
    return dp


def k8_tiers(bc: Counter) -> dict:
    grouped = defaultdict(list)
    for (b, c, support, t, r, q), mult in bc.items():
        grouped[(b, c, support, t, r)].append((q, mult))
    return {key: tuple(sorted(values)[:8]) for key, values in grouped.items()}


def main() -> None:
    for name, (rel, expected) in CURRENT_LOCKS.items():
        path = ROOT / rel
        req(path.is_file(), f"missing current source {name}")
        req(git_blob(path) == expected, f"current source drift {name}")

    direct = direct_bc()
    compact = compact_bc()
    req(direct == compact, "BC direct/compact multiplicity mismatch")
    req(sum(direct.values()) == EXPECTED["bc_assignment_count"], "BC assignment count drift")
    req(len(direct) == EXPECTED["bc_full_state_count"], "BC full-state count drift")
    req(counter_hash(direct) == EXPECTED["bc_full_stream_sha256"], "BC full stream drift")

    kd = k8_tiers(direct)
    kc = k8_tiers(compact)
    req(kd == kc, "K=8 qBC tier mismatch")
    req(len(kd) == EXPECTED["bc_k8_base_state_count"], "K=8 base-state count drift")
    req(mapping_hash(kd) == EXPECTED["bc_k8_stream_sha256"], "K=8 tier stream drift")

    ad = direct_a()
    ac = dp_a()
    req(ad == ac, "A direct/DP full qA histogram mismatch")
    req(sum(ad.values()) == EXPECTED["a_assignment_count"], "A assignment count drift")
    req(len(ad) == EXPECTED["a_full_state_count"], "A state count drift")
    req(counter_hash(ad) == EXPECTED["a_full_stream_sha256"], "A stream drift")

    qn = PICARD["normal_quotient_index"]
    qf = PICARD["normal_plus_free_quotient_index"]
    req(qn == 2**169, "normal quotient is not 2^169")
    req(qf == 2**165, "normal+free quotient is not 2^165")
    req(qn % qf == 0 and qn // qf == 16, "Picard free-exceptional image is not 16 states")
    req(PICARD["mu_universal_upper_bound"] == 8, "mu bound regression")

    result = {
        "schema": "STAGE32_BR201_SOURCE_LOCK_COMPACT_PRODUCER_REGRESSION_V1",
        "status": "PASS_ZERO_CREDIT",
        "domain": {"H": H, "identity_materialization": False},
        "source_locks": {
            "current_branch_required_blobs": {
                k: {"path": rel, "git_blob_sha1": sha}
                for k, (rel, sha) in CURRENT_LOCKS.items()
            },
            "historical_source_only": HISTORICAL_LOCKS,
        },
        "bc_regression": {
            "key": ["b", "c", "BC_support", "t", "r", "qBC"],
            "direct_assignment_count": sum(direct.values()),
            "full_state_count": len(direct),
            "direct_equals_compact": True,
            "full_stream_sha256": counter_hash(direct),
            "K8_base_state_count": len(kd),
            "K8_direct_equals_compact": True,
            "K8_stream_sha256": mapping_hash(kd),
        },
        "a_regression": {
            "key": ["a", "A_support", "qA"],
            "direct_assignment_count": sum(ad.values()),
            "full_state_count": len(ad),
            "direct_equals_dp": True,
            "full_qA_stream_sha256": counter_hash(ad),
        },
        "picard_mu_interface": {
            **PICARD,
            "reachable_state_count": qn // qf,
            "additional_bits_above_existing_picard_parity": 4,
            "interface": "sigma=sigma_A+sigma_BC in H; require mu[sigma] <= residual exceptional mass",
            "claim_scope": "source-locked finite interface only; BR203 computes the exact statewise mu table",
        },
        "classification": "REGRESSION_EQUIVALENT_SOURCE_SEMANTICS",
        "credit": {
            "stage32_main": False,
            "theorem": False,
            "effectivity": False,
            "receiver": False,
            "endpoint": False,
            "perfect_cuboid": False,
            "merge": False,
        },
        "next": "BR202_P1_K8_FULL_QA_INTEGRATION",
    }
    out = HERE / "BR201-SOURCE-LOCK-COMPACT-PRODUCER-REGRESSION.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
