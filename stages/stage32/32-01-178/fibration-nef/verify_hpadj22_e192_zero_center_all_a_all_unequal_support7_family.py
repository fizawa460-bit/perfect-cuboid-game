#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARENT = HERE / "verify_hpadj22_e192_zero_center_single_witness.py"
PARENT_BLOB = "5e54175ac7ef5983d639f1657f7878142d3bd5dc"

EXPECTED_H_TUPLES = 7620382
EXPECTED_H_HIST_BINS = 87604
EXPECTED_H_HIST_SHA256 = "0cbf8d0aed4c3223da556a8e0a378992b39ec119954cf57747682fce374a881a"
EXPECTED_A_MIN = 3
EXPECTED_A_MAX = 49
EXPECTED_A_TUPLES = 18424
EXPECTED_A_EVEN_TUPLES = 8924
EXPECTED_A_ODD_TUPLES = 9500
EXPECTED_CURRENT = 6306457460585
EXPECTED_REFINED = 4985608973274
EXPECTED_REDUCTION = 1320848487311
EXPECTED_CANDIDATE = 138652738479802106183
EXPECTED_BY_A_SHA256 = "a238f1ab8c89c3066e8ce4aa2b1e3187d166e321f2920c928c1fc50976cf09f1"


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
    out: Counter[tuple[int,int,int]] = Counter()
    total = 0
    # Exact coordinate replay of current HPADJ22 build_joint_bc_shard's
    # canonical unequal x0<x1 branch, restricted to supportH=7.
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


def prefix(counter: Counter[int], cutoff: int) -> list[int]:
    out = [0] * (cutoff + 1)
    for q, mult in counter.items():
        if int(q) <= cutoff:
            out[int(q)] += int(mult)
    for i in range(1, len(out)):
        out[i] += out[i-1]
    return out


def prefix_count(pref: list[int], limit: int) -> int:
    if limit < 0:
        return 0
    return pref[min(int(limit), len(pref)-1)]


def eval_limit_hist(ah: Counter[int], limits: Counter[int], cutoff: int) -> int:
    pref = prefix(ah, cutoff)
    return sum(int(mult) * prefix_count(pref, int(limit)) for limit, mult in limits.items())


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", type=Path, required=True)
    ap.add_argument("--source-root", type=Path, required=True)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    req(PARENT.is_file() and blob(PARENT) == PARENT_BLOB, "single-witness parent drift")
    p = load_module(PARENT, "stage32_178_hpadj22_alla_parent")

    direct_path = args.repo_root / p.DIRECT_REL
    req(direct_path.is_file() and blob(direct_path) == p.DIRECT_BLOB, "current direct-count source drift")
    direct = load_module(direct_path, "stage32_178_hpadj22_alla_direct")
    old = direct.load_old(args.source_root)

    bc = old.load_bchunk()
    bnd = bc.load_bound()
    h21 = bnd.load_module(bnd.H21, bnd.H21_BLOB, "stage32_178_alla_h21")
    h20 = h21.load_parent()
    h19 = h20.load_parent()
    h18 = h19.load_parent()
    h17 = h18.load_parent()
    h16 = h17.load_parent()
    p15 = h16.load_module(h16.PARENT, h16.PARENT_BLOB, "stage32_178_alla_h15")
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
    b, c, e = W["b"], W["c"], W["e"]
    h = d // 2
    req((b,c,e) == (45,60,192), "target b/c/e drift")
    req(tuple(old.PLANNED[p.BAND]) == (36,47), "target band drift")

    hh, htotal = unequal_support7_hist(b=b, c=c)
    req(htotal == EXPECTED_H_TUPLES, f"H tuple population drift {htotal}")
    req(len(hh) == EXPECTED_H_HIST_BINS, f"H histogram bin drift {len(hh)}")
    req(hist_sha(hh) == EXPECTED_H_HIST_SHA256, "H histogram stream drift")
    req(all((t & 1) == 0 for (t,_q,_r) in hh), "H t parity drift")

    threshold8 = d*d + 16*d
    threshold_q = threshold8 // 8
    req(threshold_q == 4992 and bc.QCAP == 4992 and bc.OVERFLOW == 4993, "qBC threshold/cap drift")

    # For supportA=3, supportH=7 and this fixed (b,c,e), current HPADJ22
    # admits e=192 exactly for a=3..49.  Check it through the producer
    # rather than relying only on the closed arithmetic.
    by_a_hist: dict[int,Counter[int]] = {}
    even_hist: Counter[int] = Counter()
    odd_hist: Counter[int] = Counter()
    total_a_tuples = 0
    for a in range(EXPECTED_A_MIN, EXPECTED_A_MAX + 1):
        ah = positive_A_hist(a)
        req(sum(ah.values()) == counter.triple_free_count(a, 3), f"A support3 population drift a={a}")
        ca = counter.component_a(d, a)
        c3 = counter.component3(d, b, c)
        srem = min(16, d) + ca + c3
        es = bnd.eligible_e(counter, d, g, h, a, b, c, 10, srem, counter.ceil_div(d-16*g+16,4))
        req(e in es, f"e192 left current HPADJ22 eligible set a={a}")

        # Exact residual-simplex reduction for this range.
        R = e - a - b - c
        req(R == 87-a and R >= 38, f"remaining residual mass drift a={a}")
        known = (b+c, a, 0, 0, 0, 0)
        caps = tuple(min(R, d-known[i]) for i in range(5))
        sum_lo = max(0, R - (d-known[5]))
        req(caps == (R,R,R,R,R), f"residual caps not simplex a={a}: {caps}")
        req(sum_lo == 0, f"residual sum_lo drift a={a}: {sum_lo}")

        by_a_hist[a] = ah
        (odd_hist if (a & 1) else even_hist).update(ah)
        total_a_tuples += sum(ah.values())

    req(total_a_tuples == EXPECTED_A_TUPLES, f"aggregate A tuple drift {total_a_tuples}")
    req(sum(even_hist.values()) == EXPECTED_A_EVEN_TUPLES, "even-a tuple drift")
    req(sum(odd_hist.values()) == EXPECTED_A_ODD_TUPLES, "odd-a tuple drift")

    # Picard parity is exact over the whole family: H parity forces t even,
    # b=45 is odd, so r0=(b+t)%2=1; r1=a%2.  The exact zero-center
    # residual penalties are therefore 1/2 for even a and 3/5 for odd a.
    fast = load_module(p.FAST, "stage32_178_hpadj22_alla_fast")
    cert = fast.load_certificate()
    t_values = sorted({t for (t,_q,_r) in hh})
    for a in range(EXPECTED_A_MIN, EXPECTED_A_MAX + 1):
        R = 87-a
        for t in t_values:
            parity = fast.parity_witness((a,b,c,t,0,e,d))
            expected = (1, a&1, 0, 0, 0)
            req(parity == expected, f"Picard parity drift a={a} t={t}: {parity}")
            req(sum(expected) <= R, f"minimal parity exceeds residual mass a={a}")
            req(fast.membership_ok(cert, (a,b,c,t,0,e,d) + expected),
                f"Picard membership drift a={a} t={t}")

    caps_x4 = bnd.x4_caps(h16, h, g, b, c)
    xr = h16.a0_interval(h, g, b, c)
    req(xr is not None, "target x4 interval disappeared")
    cap_by_x4: dict[int,int] = {}
    for x4 in range(xr[0], xr[1] + 1):
        room = -int(h16.f0(h, g, b, c, x4))
        req(room >= 0, "x4 interval room drift")
        cap_by_x4[x4] = room // 138

    all_qA = set(even_hist) | set(odd_hist)
    for qA in all_qA:
        for r in (0,1):
            exact = sum(
                1 for x4 in range(xr[0], xr[1] + 1)
                if (x4 & 1) == r and int(qA) <= cap_by_x4[x4]
            )
            req(exact == int(bnd.survivor_count(caps_x4, r, int(qA))),
                f"x4 survivor adapter drift qA={qA} r={r}")

    # Compress the H/x4 side to exact qA-limit histograms.  These are shared
    # by all a values; only the zero-center parity penalty differs by a parity.
    current_limits: Counter[int] = Counter()
    refined_even_limits: Counter[int] = Counter()
    refined_odd_limits: Counter[int] = Counter()

    # genus_budget = d^2/16+d+2-2g = 2496.  With
    # z=d/2-2*x4-t, exact_cut=2*(2496-z^2/12-minpen).
    # even a: minpen=1/2 => floor((29946-z^2)/6)
    # odd  a: minpen=3/5 => floor((149724-5*z^2)/30)
    req(d*d//16 + d + 2 - 2*g == 2496, "genus budget drift")
    for (t, qbc, r), hmult in hh.items():
        hmult = int(hmult)
        start = xr[0] + ((r - xr[0]) & 1)
        for x4 in range(start, xr[1] + 1, 2):
            cur_limit = min(cap_by_x4[x4], threshold_q - int(qbc))
            if cur_limit < 0:
                continue
            current_limits[cur_limit] += hmult
            z = d//2 - 2*x4 - int(t)
            z2 = z*z
            cut_even = (29946 - z2) // 6
            cut_odd = (149724 - 5*z2) // 30
            refined_even_limits[min(cur_limit, cut_even-int(qbc))] += hmult
            refined_odd_limits[min(cur_limit, cut_odd-int(qbc))] += hmult

    by_a = []
    current = 0
    refined = 0
    stream = hashlib.sha256()
    for a in range(EXPECTED_A_MIN, EXPECTED_A_MAX + 1):
        ah = by_a_hist[a]
        cur = eval_limit_hist(ah, current_limits, threshold_q)
        ref_limits = refined_odd_limits if (a & 1) else refined_even_limits
        ref = eval_limit_hist(ah, ref_limits, threshold_q)
        req(0 <= ref <= cur, f"zero-center refinement weakened family a={a}")
        rec = {
            "a": a,
            "A_support3_ordered_triples": sum(ah.values()),
            "current": cur,
            "refined": ref,
            "reduction": cur-ref,
        }
        by_a.append(rec)
        stream.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode())
        stream.update(b"\n")
        current += cur
        refined += ref

    req(stream.hexdigest() == EXPECTED_BY_A_SHA256, "per-a result stream drift")
    reduction = current - refined
    req(current == EXPECTED_CURRENT, f"current all-a family drift {current}")
    req(refined == EXPECTED_REFINED, f"refined all-a family drift {refined}")
    req(reduction == EXPECTED_REDUCTION, f"all-a strict reduction drift {reduction}")
    req(0 < current < p.OLD_GLOBAL, "family current count outside locked global bound")

    candidate = p.OLD_GLOBAL - reduction
    req(candidate == EXPECTED_CANDIDATE, "candidate global bound drift")

    out = {
        "schema": "STAGE32_32_01_178_HPADJ22_E192_ZERO_CENTER_ALL_A_ALL_UNEQUAL_SUPPORT7_FAMILY_V1",
        "status": "EXACT_CURRENT_HPADJ22_ALL_A_ALL_UNEQUAL_SUPPORT7_FAMILY_STRICT_REFINEMENT__ZERO_MAIN_CREDIT__HOSTILE_AUDIT_REQUIRED",
        "source_locks": {
            "single_witness_parent_blob_sha1": PARENT_BLOB,
            "current_direct_count_blob_sha1": p.DIRECT_BLOB,
            "hpadj22_source_head": p.HPADJ22_SOURCE_HEAD,
            "historical_hpadj22_worker_blob_sha1": direct.OLD_BLOB,
            "zero_center_picard_source_blob_sha1": p.FAST_BLOB,
        },
        "target": {
            "row_index": p.ROW_INDEX, "row_id": row_id, "band_position": p.BAND,
            "b_interval": [36,47], "a_interval": [EXPECTED_A_MIN,EXPECTED_A_MAX],
            "b": b, "c": c, "e": e, "A_support": 3, "H_support": 7,
            "canonical_H_branch": "x0<x1",
        },
        "family": {
            "A_support3_ordered_triples_all_a": total_a_tuples,
            "A_even_a_ordered_triples": sum(even_hist.values()),
            "A_odd_a_ordered_triples": sum(odd_hist.values()),
            "H_unequal_support7_tuples": htotal,
            "H_histogram_bins": len(hh),
            "H_histogram_stream_sha256": EXPECTED_H_HIST_SHA256,
            "per_a_stream_sha256": EXPECTED_BY_A_SHA256,
            "current_hpadj22_survivors": current,
            "zero_center_survivors": refined,
            "exact_survivor_reduction": reduction,
            "by_a": by_a,
        },
        "result": {
            "current_v45_global_upper_bound": str(p.OLD_GLOBAL),
            "certified_strict_reduction_lower_bound": reduction,
            "candidate_global_upper_bound_if_promoted": str(candidate),
        },
        "semantics": {
            "same_current_hpadj22_population": True,
            "all_a_values_are_disjoint_aggregate_families": True,
            "canonical_unequal_H_coordinates_replayed_exactly": True,
            "all_A_support3_ordered_triples_replayed_exactly": True,
            "e192_current_eligibility_replayed_for_every_a": True,
            "residual_simplex_caps_proved_for_every_a": True,
            "zero_center_picard_closed_form_replayed_for_every_a_and_t": True,
            "hpadj22_qcap_survival_equivalence_proved_on_subset": True,
            "current_x4_survivor_adapter_crosschecked": True,
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
    print("HPADJ22_E192_ZERO_CENTER_ALL_A_ALL_UNEQUAL_SUPPORT7=" + json.dumps({
        "current_family": current, "refined_family": refined, "reduction": reduction,
        "old_global": str(p.OLD_GLOBAL), "candidate_global": str(candidate),
        "canonical": out["canonical_sha256_without_this_field"],
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
