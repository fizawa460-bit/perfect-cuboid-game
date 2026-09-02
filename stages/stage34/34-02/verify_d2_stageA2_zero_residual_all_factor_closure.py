#!/usr/bin/env python3
import hashlib
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "d2-stageA2-zero-residual-all-factor-closure-assembly-certificate.json"

SOURCES = {
    "two_adic_pattern": ("d2-stageA2-two-adic-pattern-lock.json", "a27621570e79e045a47bc27aec7ecbabb2ebd5f1"),
    "factor_local": ("d2-stageA2-factor-branch-local-lock.json", "4c0afce8f693cab2f6652686bc85f46aba39f802"),
    "factor_support": ("d2-stageA2-factor-branch-support-lock.json", "ff510a1c39b9dc0ffeb8335f4ac65db86795b214"),
    "reconstruction_rank": ("d2-stageA2-reconstruction-rank-lock.json", "dc18cceeed2cce97b9cbb6b9225cf8334ea43cc8"),
    "full_support": ("d2-stageA2-full-support-projective-lock.json", "92dff93b3c8e5af8afbfc7b35e85ed7c578b2208"),
    "rankzero_ab": ("d2-stageA2-rankzero-AB-complete-pullback.json", "463d8e6c651dd315258640ef8a2de29537e3d9e5"),
    "rank1_mw": ("d2-stageA2-rank1-mw-congruence-sieve-certificate.json", "03067245c30f765db16fb1aea16ef25371f53bb0"),
    "genus2_rankzero": ("d2-stageA2-genus2-rankzero-closure-certificate.json", "ed66e62bb73c41d018ebb0a54466649f65cee28f"),
    "genus2_rankle1": ("d2-stageA2-genus2-rankle1-14-closure-certificate.json", "2fc15586127ae19c9bda63eecbe59edfa76e8ea0"),
    "two_orbit": ("d2-stageA2-two-orbit-audit-promotion-certificate.json", "0ae3514825f03d7ebdc31a58ba655f888998c79e"),
    "two_rankzero": ("d2-stageA2-two-rankzero-alternate-audit-promotion-certificate.json", "37b03844347bf3bf66244fb4610c190a3b3e3f25"),
    "candidate_ab": ("d2-stageA2-candidateAB-hostile-reaudit-promotion-certificate.json", "ce4ab24cab327270202674bee1814127d9a1c4c9"),
    "q8039": ("d2-stageA2-pr1486-q8039-hostile-audit-promotion-certificate.json", "1f65181fa158e61d9e35702ce1dbbad272d75a37"),
    "q8413": ("d2-stageA2-pr1489-q8413-hostile-audit-promotion-certificate.json", "90d86e05337cbb772ec25f4ef93659ccfbaab4e3"),
}


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load_locked(name):
    fn, expected = SOURCES[name]
    data = (HERE / fn).read_bytes()
    actual = git_blob_sha(data)
    assert actual == expected, (name, actual, expected)
    return json.loads(data)


def qdict(d):
    return {str(k): int(v) for k, v in d.items()}


def subtract_q(a, b):
    out = dict(qdict(a))
    for k, v in qdict(b).items():
        out[k] = out.get(k, 0) - v
        assert out[k] >= 0
    return {k: v for k, v in out.items() if v or k in out}


def hist(records):
    return dict(Counter(r[0] if isinstance(r, tuple) else r["q"] for r in records))


def assert_q_equal(a, b):
    keys = set(a) | set(b)
    assert {k: int(a.get(k, 0)) for k in keys} == {k: int(b.get(k, 0)) for k in keys}


def main():
    d = {name: load_locked(name) for name in SOURCES}

    # Exact exhaustive over-approximation / monotone pruning chain.
    initial = d["two_adic_pattern"]["branch_upper_bound_before_real_and_Qp_filter"]["total_over_all_fourteen_cases"]
    assert initial == 29952
    assert d["factor_local"]["input_branch_upper_bound"] == initial
    assert d["factor_local"]["survivors"] == 1946
    assert d["factor_support"]["input_survivors"] == 1946
    assert d["factor_support"]["survivors"] == 1214
    assert d["reconstruction_rank"]["input_survivors"] == 1214
    assert d["reconstruction_rank"]["survivors"] == 1024
    assert d["full_support"]["rank_zero_replay"]["input_after_legendre2"] == 1214
    assert d["full_support"]["rank_zero_replay"]["input_after_rank_zero_pruning"] == 1024
    assert d["full_support"]["result"]["after_rankzero"] == 1024
    assert d["full_support"]["result"]["support_projective_survivors"] == 92
    assert d["full_support"]["result"]["d2"] == "20 -> 0"
    assert d["full_support"]["result"]["d2_factor_branches_closed"] is True
    full92_by_q = qdict(d["full_support"]["result"]["d1_survivors_by_q"])
    assert sum(full92_by_q.values()) == 92

    layers = []

    rz = d["rankzero_ab"]
    assert rz["input_d1_factor_branches"] == 92
    assert rz["rank_zero_AB_parent_branches"] == 16
    assert rz["remaining_d1_factor_branches"] == 76
    rz_records = [(r["q"], r["branch_id"]) for r in rz["branches"]]
    assert len(rz_records) == 16
    after_rz = subtract_q(full92_by_q, dict(Counter(q for q, _ in rz_records)))
    assert sum(after_rz.values()) == 76
    layers.append(("rankzero_AB", [bid for _, bid in rz_records]))

    r1 = d["rank1_mw"]
    assert (r1["input_branches"], r1["closed_branches"], r1["remaining_branches"]) == (76, 24, 52)
    r1_records = [(r[0], r[1]) for r in r1["closed"]]
    assert len(r1_records) == 24
    assert_q_equal(dict(Counter(q for q, _ in r1_records)), r1["closed_by_q"])
    after_r1 = subtract_q(after_rz, r1["closed_by_q"])
    assert_q_equal(after_r1, r1["remaining_by_q"])
    layers.append(("rank1_MW", [bid for _, bid in r1_records]))

    g0 = d["genus2_rankzero"]
    assert (g0["input_remaining_branches"], g0["closed_branches"], g0["remaining_branches"]) == (52, 8, 44)
    g0_records = [(r["q"], r["branch_id"]) for r in g0["closed"]]
    assert_q_equal(dict(Counter(q for q, _ in g0_records)), g0["closed_by_q"])
    after_g0 = subtract_q(after_r1, g0["closed_by_q"])
    assert_q_equal(after_g0, g0["remaining_by_q"])
    layers.append(("genus2_rankzero", [bid for _, bid in g0_records]))

    g1 = d["genus2_rankle1"]
    assert (g1["input_remaining_branches"], g1["closed_branches"], g1["remaining_branches"]) == (44, 14, 30)
    g1_records = [(r["q"], r["branch_id"]) for r in g1["closed_records"]]
    assert_q_equal(dict(Counter(q for q, _ in g1_records)), g1["closed_by_q"])
    after_g1 = subtract_q(after_g0, g1["closed_by_q"])
    assert_q_equal(after_g1, g1["remaining_by_q"])
    layers.append(("genus2_rankle1", [bid for _, bid in g1_records]))

    two = d["two_orbit"]
    assert two["baseline"]["authoritative_remaining_branches"] == 30
    assert two["promoted_closures"]["count"] == 4
    assert two["promoted_authoritative_state"]["remaining_branches"] == 26
    assert_q_equal(after_g1, two["baseline"]["authoritative_remaining_by_q"])
    after_two = qdict(two["promoted_authoritative_state"]["remaining_by_q"])
    layers.append(("two_orbit_audit", list(two["promoted_closures"]["all"])))

    alt = d["two_rankzero"]
    assert alt["baseline"]["authoritative_remaining_branches"] == 26
    assert alt["promoted_closures"]["count"] == 4
    assert alt["promoted_authoritative_state"]["remaining_branches"] == 22
    assert_q_equal(after_two, alt["baseline"]["authoritative_remaining_by_q"])
    after_alt = qdict(alt["promoted_authoritative_state"]["remaining_by_q"])
    layers.append(("two_rankzero_audit", list(alt["promoted_closures"]["all"])))

    cab = d["candidate_ab"]
    assert cab["baseline"]["authoritative_remaining_branches"] == 22
    assert_q_equal(after_alt, cab["baseline"]["authoritative_remaining_by_q"])
    a_ids = list(cab["candidate_A"]["direct_representatives"]) + list(cab["candidate_A"]["sign_partners"])
    b_ids = list(cab["candidate_B"]["closed_branch_ids"])
    assert len(a_ids) == 10 and len(b_ids) == 4 and cab["disjointness"]["candidate_sets_disjoint"] is True
    assert cab["disjointness"]["total_promoted_branches"] == 14
    assert cab["candidate_B"]["factor_branch_rational_pointset_empty_claim"] is False
    assert cab["promoted_authoritative_state"]["remaining_branches"] == 8
    after_cab = qdict(cab["promoted_authoritative_state"]["remaining_by_q"])
    layers.append(("candidate_A", a_ids))
    layers.append(("candidate_B_receiver_intersection", b_ids))

    q80 = d["q8039"]
    assert q80["authoritative_before"]["remaining_branches"] == 8
    assert_q_equal(after_cab, q80["authoritative_before"]["by_q"])
    assert q80["promotion"]["closed_branches"] == 4
    assert q80["authoritative_after"]["remaining_branches"] == 4
    after_q80 = qdict(q80["authoritative_after"]["by_q"])
    layers.append(("q80_39_audit", list(q80["promotion"]["closed_branch_ids"])))

    q84 = d["q8413"]
    assert q84["authoritative_before"]["remaining_branches"] == 4
    assert_q_equal(after_q80, q84["authoritative_before"]["by_q"])
    assert q84["promotion"]["closed_branches"] == 4
    assert q84["authoritative_after"]["remaining_branches"] == 0
    assert q84["authoritative_after"]["remaining_sign_orbits"] == 0
    assert sum(q84["authoritative_after"]["by_q"].values()) == 0
    layers.append(("q84_13_audit", list(q84["promotion"]["closed_branch_ids"])))

    # Every one of the 92 post-support d1 branches is discharged exactly once.
    all_ids = []
    layer_counts = {}
    for name, ids in layers:
        assert len(ids) == len(set(ids)), name
        layer_counts[name] = len(ids)
        all_ids.extend(ids)
    assert layer_counts == {
        "rankzero_AB": 16,
        "rank1_MW": 24,
        "genus2_rankzero": 8,
        "genus2_rankle1": 14,
        "two_orbit_audit": 4,
        "two_rankzero_audit": 4,
        "candidate_A": 10,
        "candidate_B_receiver_intersection": 4,
        "q80_39_audit": 4,
        "q84_13_audit": 4,
    }
    assert len(all_ids) == 92
    assert len(set(all_ids)) == 92
    closure_digest = hashlib.sha256(("\n".join(sorted(all_ids)) + "\n").encode()).hexdigest()
    assert closure_digest == "7d43cd93f9329b48fa981857c10b03ad7a9df985af057ff1845001ca4fcefa6f"

    cert = json.loads(CERT.read_text())
    assert cert["schema"] == "STAGE34_02C_D2_STAGEA2_ZERO_RESIDUAL_ALL_FACTOR_CLOSURE_ASSEMBLY_CERTIFICATE_V1"
    assert cert["status"] == "PASS_EXACT_CUMULATIVE_ALL_FACTOR_CLOSURE_ASSEMBLY_PREAUDIT"
    assert cert["coverage_chain"] == [29952, 1946, 1214, 1024, 92, 76, 52, 44, 30, 26, 22, 8, 4, 0]
    assert cert["post_support_d1_closed_unique"] == 92
    assert cert["post_support_d1_closed_ids_sha256"] == closure_digest
    assert cert["promotion_candidate"]["D2_all_factor_branches_closed"] is True
    assert cert["promotion_candidate"]["scope"] == "audited nonzero-free-part R29-EXT-CHANG-C receiver population only"
    assert cert["firewalls"]["hostile_audit_passed"] is False
    assert cert["firewalls"]["direct_cover_rational_points_complete"] is False
    assert cert["firewalls"]["all_multiples_closed"] is False
    assert cert["firewalls"]["R29_EXT_CHANG_C_closed"] is False
    assert cert["firewalls"]["candidateB_factor_branch_rational_pointset_empty_claim"] is False
    print("PASS_EXACT_CUMULATIVE_ALL_FACTOR_CLOSURE_ASSEMBLY_PREAUDIT")


if __name__ == "__main__":
    main()
