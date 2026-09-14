#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

AUDITED_MAIN_V22_HEAD = "f8039b4ce479a4b91f2f0547e7049f629e9be5f5"
AUDITED_MAIN_V22_REVIEW = 5188224290
AUDITED_N358_HEAD = "462174f74d6470ec7c64f5b6d078757c7b3372fc"
AUDITED_N358_REVIEW = 5184322011

V22_STATE_BLOB = "80fb35c79854bfdf775dc5b94c331f5f8a535ced"
V22_TERMINALS = 47589703313957134804198
V22_STRATA = 17128

N358_VERIFIER_REL = Path("stages/stage32/32-01-178/nodes/N358/verify_n358_exact_incremental_census.py")
N358_VERIFIER_BLOB = "c07a7e358a6253919194189377d6ed56f95e047a"
N358_RECEIPT_REL = Path("stages/stage32/32-01-178/nodes/N358/HOSTILE-AUDIT-PASS.json")

HPERP_REL = Path("stages/stage32/residual-32-01-production/hperp_integral_adapter.py")
HPERP_BLOB = "fb1eb380ca786e42a6b00c5ef454b0e79fdba771"
PREFIX_REL = Path("stages/stage32/residual-32-01-production/pairing_prefix_engine.py")
PREFIX_BLOB = "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b"
BUNDLE_REL = Path("stages/stage33/33-07/picard_base_rows_retained.py")
BUNDLE_BLOB = "82e4d450a1d852e34f6615440fb88a029c6e54eb"
MARKING_REL = Path("stages/stage33/33-07/stage32_picard_marking_retained.py")
MARKING_BLOB = "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7"

HERE = Path(__file__).resolve().parent
RESULT = HERE / "RESULT.json"
BREADTH = HERE / "BREADTH-AUDIT.json"
RESULT_BLOB = "520b6b0f230e23fb5ea34b80fef591cfa5f9be4b"
RESULT_CANON = "9773c11e87de149b5b56438fd1c86929aa54a971601bf8306855fd0f8a303506"
BREADTH_BLOB = "1b7154b050167aa202c3f6801b25b4d1fab53a8b"
BREADTH_CANON = "23ffb5bcc3dd9691e36b36298453bf62432e169e3ba2d11c0198fc514ed096a5"

EXPECTED_PREFIX_INSTANCES = 19700993066083231249
EXPECTED_TERMINALS = 27104321327305699275487
EXPECTED_G0 = 6263333577918328238904
EXPECTED_G1 = 20840987749387371036583
EXPECTED_ROW_STREAM = "5852e58fdd570e05c057d5fcaf426f6b25fefb1eaf83ae1329657b42289775ae"
TERMINAL_EXCEPTIONAL_LABELS = [95, 99, 103, 102, 97, 94, 101, 93, 98, 96]


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def lock_json(path: Path, blob: str, canonical: str) -> dict:
    req(path.is_file(), f"missing {path}")
    req(git_blob(path) == blob, f"blob drift {path}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == canonical, f"stored canonical drift {path}")
    req(canon(obj) == canonical, f"canonical drift {path}")
    return obj


def head(root: Path) -> str:
    return subprocess.check_output(
        ["git", "-C", str(root), "rev-parse", "HEAD"], text=True
    ).strip()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def load_retained(path: Path, name: str) -> dict:
    mod = load_module(path, name)
    payload = mod.load()
    req(isinstance(payload, dict), f"retained payload not dict: {path}")
    return payload


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def even_interval_normal_sum(d: int, lower: int, upper: int, excluded: set[int]) -> tuple[int, int]:
    lo = lower if lower % 2 == 0 else lower + 1
    hi = upper if upper % 2 == 0 else upper - 1
    if lo > hi:
        return 0, 0
    n = (hi - lo) // 2 + 1
    total_e = n * (lo + hi) // 2
    total = n * (19 * d + 1) - 5 * total_e
    count = n
    for e in sorted(excluded):
        if lo <= e <= hi and e % 2 == 0:
            total -= 19 * d - 5 * e + 1
            count -= 1
    return count, total


def verify_geometry(v22: Path) -> None:
    hpath = v22 / HPERP_REL
    ppath = v22 / PREFIX_REL
    bpath = v22 / BUNDLE_REL
    mpath = v22 / MARKING_REL
    for path, expected in (
        (hpath, HPERP_BLOB),
        (ppath, PREFIX_BLOB),
        (bpath, BUNDLE_BLOB),
        (mpath, MARKING_BLOB),
    ):
        req(path.is_file(), f"missing audited geometry source {path}")
        req(git_blob(path) == expected, f"audited geometry source drift {path}")

    residual = v22 / "stages/stage32/residual-32-01-production"
    sys.path.insert(0, str(residual))
    hmod = load_module(hpath, "stage32_hpadj01_hperp")
    bundle = load_retained(bpath, "stage32_hpadj01_bundle")
    marking = load_retained(mpath, "stage32_hpadj01_marking")

    q, degree, linear, _, _ = hmod._parse_hperp(marking["hperp_text"])
    full = hmod._recover_full_intersection(q, degree, linear)
    for label in range(93, 141):
        i = label - 1
        req(int(degree[i]) == 0, f"exceptional degree nonzero label={label}")
        for other in range(93, 141):
            j = other - 1
            want = -2 if label == other else 0
            req(int(full[i, j]) == want, f"exceptional Gram drift {(label, other)}")

    req(all(93 <= label <= 140 for label in TERMINAL_EXCEPTIONAL_LABELS),
        "terminal exceptional label outside exceptional block")
    req(len(set(TERMINAL_EXCEPTIONAL_LABELS)) == 10, "terminal exceptional labels not distinct")


def census(n358_root: Path) -> dict:
    path = n358_root / N358_VERIFIER_REL
    req(path.is_file(), "audited N358 verifier missing")
    req(git_blob(path) == N358_VERIFIER_BLOB, "audited N358 verifier blob drift")
    receipt = json.loads((n358_root / N358_RECEIPT_REL).read_text(encoding="utf-8"))
    req(receipt.get("status") == "PASS", "N358 audit status drift")
    req(receipt.get("review_id") == AUDITED_N358_REVIEW, "N358 review drift")
    req(receipt.get("audited_exact_head") == AUDITED_N358_HEAD, "N358 audited head drift")

    n358 = load_module(path, "stage32_hpadj01_n358")
    BC = n358.build_bc_exact(n358.HMAX)
    req(n358.n357_count_witness(BC) == n358.EXPECTED_N357_WITNESS,
        "N357 semantic witness replay drift")

    total_prefix_instances = 0
    total_terms = 0
    by_g = {0: 0, 1: 0}
    per_row: list[dict] = []

    for g in (0, 1):
        dmax = 176 if g == 0 else 192
        for d in range(8, dmax + 1, 2):
            h = d // 2
            legacy = 8 if g == 0 else 4
            K = n358.ceil_div(d - 16 * g + 16, 4)
            row_prefix_instances = 0
            row_terms = 0
            A = [[n358.triple_free_count(a, sa) for sa in range(4)] for a in range(h + 1)]

            for b in range(h + 1):
                for c in range(h + 1):
                    bcv = BC[b][c]
                    if not any(bcv):
                        continue
                    c3 = n358.component3(d, b, c)
                    if c3 < 0:
                        continue
                    for a in range(h + 1):
                        avec = A[a]
                        if not any(avec):
                            continue

                        # For group sizes 3,3,4, Cauchy gives
                        # sum(y_i^2) >= a^2/3+b^2/3+c^2/4.
                        # Combined with 8 sum(y_i^2) <= d^2+32, violation is:
                        if 8 * a * a + 8 * b * b + 6 * c * c <= 3 * d * d + 96:
                            continue

                        M = a + b + c
                        ca = n358.component_a(d, a)
                        if ca < 0:
                            continue
                        srem = min(16, d) + ca + c3

                        scount = [0] * 11
                        for sbc, left in enumerate(bcv):
                            if not left:
                                continue
                            for sa, right in enumerate(avec):
                                if right:
                                    scount[sbc + sa] += left * right

                        for support, count in enumerate(scount):
                            if not count:
                                continue
                            qneed = K - support
                            if qneed > 0 and srem < qneed:
                                continue

                            lower = max(
                                legacy,
                                K,
                                d - 4 * g + 4,
                                M,
                                M + max(0, qneed),
                            )
                            upper = min(
                                (19 * d) // 5,
                                3 * d,
                                3 * d - (b - c),
                            )
                            if lower > upper:
                                continue

                            excluded: set[int] = set()

                            # Remove the exact already-consumed N358 incremental slice.
                            e_n358 = 3 * d - (b - c)
                            if (
                                b <= h - 5
                                and support + srem == K
                                and e_n358 - M >= srem
                            ):
                                excluded.add(e_n358)

                            # V22 consumed CUT191/193/194/195/196/197/198 are all
                            # within g1-d008/e8. Drop that entire stratum rather
                            # than depend on individual CUT closed-block sets.
                            if g == 1 and d == 8:
                                excluded.add(8)

                            ne, normal_sum = even_interval_normal_sum(
                                d, lower, upper, excluded
                            )
                            if ne <= 0:
                                continue
                            row_prefix_instances += count * ne
                            row_terms += count * normal_sum

            req(row_terms > 0, f"HPADJ lower-bound row unexpectedly empty {(g,d)}")
            total_prefix_instances += row_prefix_instances
            total_terms += row_terms
            by_g[g] += row_terms
            per_row.append({
                "g": g,
                "d": d,
                "candidate_hodge_endpoint_terms": row_terms,
            })

    stream = hashlib.sha256()
    for rec in sorted(per_row, key=lambda r: (r["g"], r["d"])):
        stream.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")

    req(len(per_row) == 178, "FULL178 row count drift")
    req(total_prefix_instances == EXPECTED_PREFIX_INSTANCES, "prefix-instance census drift")
    req(total_terms == EXPECTED_TERMINALS, "terminal census drift")
    req(by_g[0] == EXPECTED_G0 and by_g[1] == EXPECTED_G1, "genus subtotal drift")
    req(stream.hexdigest() == EXPECTED_ROW_STREAM, "per-row stream drift")

    return {
        "affected_rows": len(per_row),
        "exceptional_prefix_stratum_instances": total_prefix_instances,
        "candidate_endpoint_rejected_terminals_lower_bound": total_terms,
        "genus0_candidate_rejected_terminals": by_g[0],
        "genus1_candidate_rejected_terminals": by_g[1],
        "per_row_stream_sha256": stream.hexdigest(),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--audited-main-v22-root", type=Path, required=True)
    ap.add_argument("--audited-n358-root", type=Path, required=True)
    args = ap.parse_args()

    v22 = args.audited_main_v22_root.resolve()
    n358 = args.audited_n358_root.resolve()
    req(head(v22) == AUDITED_MAIN_V22_HEAD, "audited V22 exact head drift")
    req(head(n358) == AUDITED_N358_HEAD, "audited N358 exact head drift")

    state_path = v22 / "stages/stage32/MAIN-STATE.json"
    req(git_blob(state_path) == V22_STATE_BLOB, "V22 MAIN-STATE blob drift")
    state = json.loads(state_path.read_text(encoding="utf-8"))
    frontier = state["current_exact_frontier"]
    req(frontier["authoritative_remaining_strata"] == V22_STRATA, "V22 stratum authority drift")
    req(frontier["authoritative_remaining_terminals"] == V22_TERMINALS, "V22 terminal authority drift")
    req(frontier["full178_numerical_census_complete"] is False, "V22 FULL178 unexpectedly complete")

    result = lock_json(RESULT, RESULT_BLOB, RESULT_CANON)
    breadth = lock_json(BREADTH, BREADTH_BLOB, BREADTH_CANON)
    req(breadth["cycle"]["exhaustive_view_audit"] is True, "breadth audit missing")
    req(breadth["cycle"]["blind_rediscovery"] is True, "blind rediscovery missing")

    verify_geometry(v22)
    got = census(n358)

    retained = result["current_v22_intersection_lower_bound"]
    for key, value in got.items():
        req(retained[key] == value, f"retained result drift {key}")
    req(retained["candidate_endpoint_rejected_terminals_lower_bound"] < V22_TERMINALS,
        "candidate lower bound exceeds current authority")
    req(result["composition_firewall"]["main_authority_mutated"] is False,
        "research leaf mutated MAIN authority")
    for key in (
        "main_pruning_credit", "full178_complete", "effectivity_final_credit",
        "receiver_credit", "theorem_credit", "endpoint_credit", "stage32_closed",
        "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
        "merge_authorized",
    ):
        req(result["firewalls"][key] is False, f"firewall opened {key}")

    print(json.dumps({
        "verdict": "PASS_HPADJ01_CURRENT_V22_ENDPOINT_LOWER_BOUND",
        "audited_main_v22_review": AUDITED_MAIN_V22_REVIEW,
        "audited_n358_review": AUDITED_N358_REVIEW,
        "current_v22_terminals": V22_TERMINALS,
        "candidate_endpoint_rejected_terminals_lower_bound": EXPECTED_TERMINALS,
        "candidate_endpoint_remaining_upper_bound_if_adapter_promoted": V22_TERMINALS - EXPECTED_TERMINALS,
        "affected_rows": 178,
        "main_pruning_credit": False,
        "endpoint_credit": False,
        "merge_authorized": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
