#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARENT = HERE / "verify_hpadj22_e192_zero_center_single_witness.py"
PARENT_BLOB = "5e54175ac7ef5983d639f1657f7878142d3bd5dc"

EXPECTED_H_TUPLES = 7620382
EXPECTED_H_HIST_BINS = 87604
EXPECTED_H_HIST_SHA256 = "0cbf8d0aed4c3223da556a8e0a378992b39ec119954cf57747682fce374a881a"
EXPECTED_CURRENT = 310555670331
EXPECTED_REFINED = 241616252951
EXPECTED_REDUCTION = 68939417380
EXPECTED_CANDIDATE = 138652739731711176114


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def positive_A_hist(a: int) -> Counter[int]:
    out: Counter[int] = Counter()
    for x2 in range(1, a - 1):
        for x3 in range(1, a - x2):
            x7 = a - x2 - x3
            if x7 > 0:
                out[x2*x2 + x3*x3 + x7*x7] += 1
    return out


def unequal_support7_hist(*, b: int, c: int) -> tuple[Counter[tuple[int,int,int]], int]:
    """
    Exact coordinate replay of the current HPADJ22 unequal x0<x1 branch,
    restricted to supportH=7.  Support 7 forces all seven H coordinates
    x0,x1,x5,x6,x8,x9,x10 to be positive.
    """
    out: Counter[tuple[int,int,int]] = Counter()
    total = 0
    for x0 in range(1, c):
        for x1 in range(x0 + 1, b):
            rem_b = b - x1
            rem_c = c - x0
            if rem_b < 2 or rem_c < 3:
                continue
            for x5 in range(1, rem_b):
                x9 = rem_b - x5
                required_cpar = (x9 & 1) ^ (x1 & 1)
                qbase = x0*x0 + x1*x1 + x5*x5 + x9*x9
                r = (x0 ^ x1 ^ x9) & 1
                tbase = x0 + x1 + x9
                for x6 in range(1, rem_c - 1):
                    rem2 = rem_c - x6
                    # Current producer requires (x8+x10) parity =
                    # x9 parity XOR x1 parity.  Since x8+x10=rem2,
                    # this test is independent of the split.
                    if (rem2 & 1) != required_cpar:
                        continue
                    for x8 in range(1, rem2):
                        x10 = rem2 - x8
                        qbc = qbase + x6*x6 + x8*x8 + x10*x10
                        t = tbase + x6
                        out[(t, qbc, r)] += 1
                        total += 1
    return out, total


def hist_sha(hist: Counter[tuple[int,int,int]]) -> str:
    h = hashlib.sha256()
    for (t, qbc, r), mult in sorted(hist.items()):
        rec = {"t": int(t), "qBC": int(qbc), "r": int(r), "multiplicity": int(mult)}
        h.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode())
        h.update(b"\n")
    return h.hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", type=Path, required=True)
    ap.add_argument("--source-root", type=Path, required=True)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    req(PARENT.is_file() and blob(PARENT) == PARENT_BLOB, "single-witness parent drift")
    p = load_module(PARENT, "stage32_178_hpadj22_allh_parent")

    direct_path = args.repo_root / p.DIRECT_REL
    req(direct_path.is_file() and blob(direct_path) == p.DIRECT_BLOB, "current direct-count source drift")
    direct = load_module(direct_path, "stage32_178_hpadj22_allh_direct")
    old = direct.load_old(args.source_root)

    bc = old.load_bchunk()
    bnd = bc.load_bound()
    h21 = bnd.load_module(bnd.H21, bnd.H21_BLOB, "stage32_178_allh_h21")
    h20 = h21.load_parent()
    h19 = h20.load_parent()
    h18 = h19.load_parent()
    h17 = h18.load_parent()
    h16 = h17.load_parent()
    p15 = h16.load_module(h16.PARENT, h16.PARENT_BLOB, "stage32_178_allh_h15")
    p14 = p15.load_parent()
    counter = p14.load_counter()
    manifest = counter.load_locked_json(
        p14.MANIFEST, p14.LOCKS["manifest_blob"], p14.LOCKS["manifest_canonical"], "FULL178 manifest"
    )
    rows = counter.manifest_rows(manifest)
    row_id, g0, d0 = rows[p.ROW_INDEX]
    req((row_id, int(g0), int(d0)) == ("g1-d192", 1, 192), "target row identity drift")

    W = dict(p.W)
    g, d = W["g"], W["d"]
    a, b, c, e = W["a"], W["b"], W["c"], W["e"]
    h = d // 2
    req((a,b,c,e) == (45,45,60,192), "target aggregate drift")

    ah = positive_A_hist(a)
    req(sum(ah.values()) == counter.triple_free_count(a, 3) == 946, "A support3 population drift")

    hh, htotal = unequal_support7_hist(b=b, c=c)
    req(htotal == EXPECTED_H_TUPLES, f"H tuple population drift {htotal}")
    req(len(hh) == EXPECTED_H_HIST_BINS, f"H histogram bin drift {len(hh)}")
    req(hist_sha(hh) == EXPECTED_H_HIST_SHA256, "H histogram stream drift")
    req(all((t & 1) == 0 for (t,_q,_r) in hh), "H t parity drift")

    # The explicit coordinate loops above are a direct injection into the
    # producer's unequal branch.  Recheck all aggregate/source invariants
    # used by that branch.
    support = 10
    K = counter.ceil_div(d - 16*g + 16, 4)
    ca = counter.component_a(d, a)
    c3 = counter.component3(d, b, c)
    srem = min(16, d) + ca + c3
    es = bnd.eligible_e(counter, d, g, h, a, b, c, support, srem, K)
    req(e in es, "e192 left current HPADJ22 eligible set")
    req(tuple(old.PLANNED[p.BAND]) == (36,47), "target band drift")

    # Current HPADJ22 caps qBC at 4993 only after 4992.  Since qA>=0 and
    # the d=192 survival threshold is exactly 4992, overflow qBC can never
    # survive.  Therefore exact qBC<=4992-qA is equivalent to the producer's
    # qcap-based survival test on this subset.
    threshold8 = d*d + 16*d
    threshold_q = threshold8 // 8
    req(threshold_q == 4992 and bc.QCAP == 4992 and bc.OVERFLOW == 4993, "qBC threshold/cap drift")

    fast = load_module(p.FAST, "stage32_178_hpadj22_allh_fast")
    cert = fast.load_certificate()
    for t in sorted({t for (t,_q,_r) in hh}):
        parity = fast.parity_witness((a,b,c,t,0,e,d))
        req(parity == (1,1,0,0,0), f"Picard parity drift t={t}: {parity}")
        req(fast.membership_ok(cert, (a,b,c,t,0,e,d) + parity), f"Picard membership drift t={t}")

    caps = bnd.x4_caps(h16, h, g, b, c)
    xr = h16.a0_interval(h, g, b, c)
    req(xr is not None, "target x4 interval disappeared")

    # Exact A-prefix counts keyed by qA.  This counts ordered positive
    # (x2,x3,x7) triples, exactly matching supportA=3 in current full_profiles.
    max_q = max(max(ah), threshold_q)
    apref = [0] * (max_q + 1)
    for q, mult in ah.items():
        apref[int(q)] += int(mult)
    for i in range(1, len(apref)):
        apref[i] += apref[i-1]

    def acount(limit: int) -> int:
        if limit < 0:
            return 0
        return apref[min(int(limit), len(apref)-1)]

    cap_by_x4: dict[int,int] = {}
    for x4 in range(xr[0], xr[1] + 1):
        room = -int(h16.f0(h, g, b, c, x4))
        req(room >= 0, "x4 interval room drift")
        cap_by_x4[x4] = room // 138

    # Cross-check the current producer's x4 survivor adapter for every qA
    # class and both required parities used by this family.
    for qA in ah:
        for r in (0,1):
            exact = sum(
                1 for x4 in range(xr[0], xr[1] + 1)
                if (x4 & 1) == r and int(qA) <= cap_by_x4[x4]
            )
            req(exact == int(bnd.survivor_count(caps, r, int(qA))),
                f"x4 survivor adapter drift qA={qA} r={r}")

    genus_budget = Fraction(d*d,16) + d + 2 - 2*g
    minpen = Fraction(3,5)
    current = 0
    refined = 0
    rejected_by_x4: Counter[int] = Counter()
    rejected_by_t: Counter[int] = Counter()

    for (t, qbc, r), hmult in hh.items():
        hmult = int(hmult)
        for x4 in range(xr[0] + ((r - xr[0]) & 1), xr[1] + 1, 2):
            current_limit = min(cap_by_x4[x4], threshold_q - int(qbc))
            cur_a = acount(current_limit)
            if cur_a == 0:
                continue
            cur = hmult * cur_a
            current += cur

            static_rho = Fraction((d//2 - 2*x4 - int(t))**2, 12)
            exact_cut = 2 * (genus_budget - static_rho - minpen)
            cut_floor = exact_cut.numerator // exact_cut.denominator
            refined_limit = min(current_limit, cut_floor - int(qbc))
            ref_a = acount(refined_limit)
            ref = hmult * ref_a
            refined += ref
            delta = cur - ref
            if delta:
                rejected_by_x4[x4] += delta
                rejected_by_t[int(t)] += delta

    reduction = current - refined
    req(current == EXPECTED_CURRENT, f"current all-H family drift {current}")
    req(refined == EXPECTED_REFINED, f"refined all-H family drift {refined}")
    req(reduction == EXPECTED_REDUCTION, f"all-H strict reduction drift {reduction}")
    req(sum(rejected_by_x4.values()) == reduction, "x4 reduction accounting drift")
    req(sum(rejected_by_t.values()) == reduction, "t reduction accounting drift")

    candidate = p.OLD_GLOBAL - reduction
    req(candidate == EXPECTED_CANDIDATE, "candidate global bound drift")

    out = {
        "schema": "STAGE32_32_01_178_HPADJ22_E192_ZERO_CENTER_ALL_UNEQUAL_SUPPORT7_FAMILY_V1",
        "status": "EXACT_CURRENT_HPADJ22_ALL_UNEQUAL_SUPPORT7_FAMILY_STRICT_REFINEMENT__ZERO_MAIN_CREDIT__HOSTILE_AUDIT_REQUIRED",
        "source_locks": {
            "single_witness_parent_blob_sha1": PARENT_BLOB,
            "current_direct_count_blob_sha1": p.DIRECT_BLOB,
            "hpadj22_source_head": p.HPADJ22_SOURCE_HEAD,
            "historical_hpadj22_worker_blob_sha1": direct.OLD_BLOB,
            "zero_center_picard_source_blob_sha1": p.FAST_BLOB,
        },
        "target": {
            "row_index": p.ROW_INDEX, "row_id": row_id, "band_position": p.BAND,
            "b_interval": [36,47], "a": a, "b": b, "c": c, "e": e,
            "A_support": 3, "H_support": 7, "canonical_H_branch": "x0<x1",
        },
        "family": {
            "A_support3_ordered_triples": sum(ah.values()),
            "H_unequal_support7_tuples": htotal,
            "H_histogram_bins": len(hh),
            "H_histogram_stream_sha256": EXPECTED_H_HIST_SHA256,
            "current_hpadj22_survivors": current,
            "zero_center_survivors": refined,
            "exact_survivor_reduction": reduction,
            "rejected_by_x4": {str(k): int(v) for k,v in sorted(rejected_by_x4.items())},
            "rejected_by_t": {str(k): int(v) for k,v in sorted(rejected_by_t.items())},
        },
        "result": {
            "current_v45_global_upper_bound": str(p.OLD_GLOBAL),
            "certified_strict_reduction_lower_bound": reduction,
            "candidate_global_upper_bound_if_promoted": str(candidate),
        },
        "semantics": {
            "same_current_hpadj22_population": True,
            "canonical_unequal_H_coordinates_replayed_exactly": True,
            "all_A_support3_ordered_triples_replayed_exactly": True,
            "hpadj22_qcap_survival_equivalence_proved_on_subset": True,
            "current_x4_survivor_adapter_crosschecked": True,
            "zero_center_picard_condition_replayed_for_every_t": True,
            "no_additive_cross_route_subtraction": True,
            "candidate_is_direct_same_population_upper_bound_refinement": True,
            "all_nonfamily_current_hpadj22_survivors_left_unchanged": True,
            "main_bound_replacement_performed": False,
            "hostile_audit_required_before_consumption": True,
        },
        "firewalls": {
            "main_credit_changed": False, "full178_complete": False,
            "theorem_credit_changed": False, "effectivity_credit_changed": False,
            "receiver_credit_changed": False, "endpoint_credit_changed": False,
            "stage32_closed": False, "merge": False,
        },
    }
    out["canonical_sha256_without_this_field"] = canon(out)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(out, sort_keys=True, separators=(",", ":")) + "\n")
    print("HPADJ22_E192_ZERO_CENTER_ALL_UNEQUAL_SUPPORT7=" + json.dumps({
        "current_family": current, "refined_family": refined, "reduction": reduction,
        "old_global": str(p.OLD_GLOBAL), "candidate_global": str(candidate),
        "canonical": out["canonical_sha256_without_this_field"],
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
