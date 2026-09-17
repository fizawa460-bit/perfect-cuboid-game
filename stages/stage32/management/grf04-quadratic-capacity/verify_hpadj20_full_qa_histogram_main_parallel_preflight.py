#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARTIFACT = HERE / "HPADJ20-FULL-QA-HISTOGRAM-MAIN-PARALLEL-PREFLIGHT.json"
ARTIFACT_BLOB = "0eb5672dea0712cbf5044d5376e60fe233e767c3"
ARTIFACT_CANON = "0191c14b3fc072a762d1b702408746691cd5fe315ce9f4a0a040b75183bd13a8"
H = 96
PROFILE_SHA256 = "eca7baca3e0efa30baf861c0a911939bd947a9e2360ae18520122037f0b0ba21"

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canon(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

def expected_count(a: int, support: int) -> int:
    if a == 0:
        return 1 if support == 0 else 0
    if support == 0 or support > min(3, a):
        return 0
    return comb(3, support) * comb(a - 1, support - 1)

def main() -> None:
    req(ARTIFACT.is_file(), "missing preflight artifact")
    req(git_blob(ARTIFACT) == ARTIFACT_BLOB, "preflight artifact blob drift")
    art = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    req(art.get("canonical_sha256_without_this_field") == ARTIFACT_CANON,
        "stored preflight canonical drift")
    req(canon(art) == ARTIFACT_CANON, "preflight canonical drift")
    req(art["status"] ==
        "STRUCTURAL_DOMINANCE_PREFLIGHT__NUMERICAL_REPLAY_NOT_RUN__ZERO_MAIN_CREDIT",
        "preflight status")

    profiles = {}
    class_count = gt1 = gt2 = nonminimum = total = minimum = 0
    max_bins = -1
    max_info = None

    for a in range(H + 1):
        hist = [defaultdict(int) for _ in range(4)]
        for x2 in range(a + 1):
            for x3 in range(a - x2 + 1):
                x7 = a - x2 - x3
                support = int(x2 > 0) + int(x3 > 0) + int(x7 > 0)
                qA = x2*x2 + x3*x3 + x7*x7
                hist[support][qA] += 1

        for support in range(4):
            got = sum(hist[support].values())
            exp = expected_count(a, support)
            req(got == exp, f"multiplicity formula drift {(a,support)}: {got} != {exp}")
            if not got:
                continue
            class_count += 1
            keys = sorted(hist[support])
            entries = [[int(q), int(hist[support][q])] for q in keys]
            profiles[f"{a}:{support}"] = entries
            total += got
            minimum += hist[support][keys[0]]
            nonminimum += got - hist[support][keys[0]]
            if len(keys) > 1:
                gt1 += 1
                q1 = keys[1]
                req(all(q >= q1 for q in keys[1:]),
                    f"second-tier lower-bound dominance drift {(a,support)}")
            if len(keys) > 2:
                gt2 += 1
            if len(keys) > max_bins:
                max_bins = len(keys)
                max_info = (a, support, got, keys[0], keys[-1])

    profile_sha = hashlib.sha256(
        json.dumps(profiles, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    req(profile_sha == PROFILE_SHA256, "full histogram profile digest drift")
    req(total == comb(H + 3, 3) == 156849, "ordered triple total drift")
    req(class_count == 286, "nonempty class count drift")
    req(gt1 == 185, "multi-qA class count drift")
    req(gt2 == 182, ">2 qA class count drift")
    req(minimum == 933 and nonminimum == 155916, "minimum/nonminimum tuple count drift")
    req(max_bins == 628 and max_info == (95, 3, 4371, 3009, 8651),
        "maximum histogram class drift")

    c = art["exact_combinatorial_preflight"]
    req(c["ordered_nonnegative_triples_with_0_le_a_le_H"] == total,
        "artifact total mismatch")
    req(c["nonempty_a_support_classes"] == class_count, "artifact class mismatch")
    req(c["classes_with_more_than_one_distinct_qA"] == gt1, "artifact >1 mismatch")
    req(c["classes_with_more_than_two_distinct_qA"] == gt2, "artifact >2 mismatch")
    req(c["minimum_qA_tier_tuple_count"] == minimum, "artifact min tuple mismatch")
    req(c["nonminimum_tuple_count"] == nonminimum, "artifact nonminimum mismatch")
    req(c["full_histogram_profile_sha256"] == profile_sha, "artifact profile hash mismatch")

    dom = art["structural_dominance"]
    req(dom["population_preserved_exactly"] is True, "population firewall")
    req(dom["same_pre_domain_terminal_mass"] is True, "pre-domain mass firewall")
    req(dom["same_post_mass_constraint"] is True, "post-mass firewall")
    req(dom["full_histogram_cell_objective_no_larger_than_hpadj20"] is True,
        "dominance statement missing")
    req(dom["strict_global_improvement_proven"] is False,
        "preflight overclaims strict global improvement")

    fw = art["firewalls"]
    for key in ("stage32_main_pruning_credit", "current_main_incremental_credit",
                "exact_incremental_rejected_identity_set_claimed",
                "statistical_independence_assumed", "additive_subtraction_used",
                "full178_complete", "effectivity_credit", "receiver_credit",
                "theorem_credit", "endpoint_credit", "perfect_cuboid_credit",
                "merge_authorized"):
        req(fw[key] is False, f"firewall {key}")

    print("PASS: exact H=96 qA histogram population/multiplicity preflight")
    print("PASS: 182 classes retain >2 exact qA levels beyond HPADJ20 two-tier compression")
    print("PASS: structural dominance retained with zero MAIN credit and no additive subtraction")

if __name__ == "__main__":
    main()
