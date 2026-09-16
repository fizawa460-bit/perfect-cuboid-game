#!/usr/bin/env python3
from __future__ import annotations

import bisect
import hashlib
import importlib.util
import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PARENT = ROOT / "stages/stage32-ex5/hpadj-20_ex5/derive_two_tier_qa_predomain_picard_lp_bound.py"
PARENT_BLOB = "837d647cfcbc96bbe384e564f449cd7042a46d48"
MAX_PILOT_D = 16


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_parent():
    req(PARENT.is_file() and git_blob(PARENT) == PARENT_BLOB, "HPADJ20 parent blob drift")
    spec = importlib.util.spec_from_file_location("hpadj20_locked_for_hpadj21_bounded", PARENT)
    req(spec is not None and spec.loader is not None, "cannot load HPADJ20 parent")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def full_profiles(H: int, counter, h19):
    out = [[[] for _ in range(4)] for __ in range(H + 1)]
    classes_gt2 = tuples_above_second = 0
    for a in range(H + 1):
        hist = [defaultdict(int) for _ in range(4)]
        for x2 in range(a + 1):
            for x3 in range(a - x2 + 1):
                x7 = a - x2 - x3
                s = int(x2 > 0) + int(x3 > 0) + int(x7 > 0)
                q = x2*x2 + x3*x3 + x7*x7
                hist[s][q] += 1
        for s in range(4):
            expected = int(counter.triple_free_count(a, s))
            req(sum(hist[s].values()) == expected, f"A histogram multiplicity drift {(a,s)}")
            if not expected:
                continue
            keys = sorted(hist[s])
            req(keys[0] == int(h19.qa_min_for_mass_support(a, s)), f"A q minimum drift {(a,s)}")
            out[a][s] = [(int(q), int(hist[s][q])) for q in keys]
            if len(keys) > 2:
                classes_gt2 += 1
                tuples_above_second += sum(int(hist[s][q]) for q in keys[2:])
    return out, classes_gt2, tuples_above_second


def exact_pilot_cells(p15, p14, counter, pilot_rows):
    rejected = p15.load_certificate(p14)
    H = max(d // 2 for _, _, d in pilot_rows)
    BC = counter.build_bc_exact_parity(H)
    cells = {}
    for row_id, g, d in pilot_rows:
        h = d // 2
        legacy = 8 if g == 0 else 4
        K = counter.ceil_div(d - 16*g + 16, 4)
        A = [[counter.triple_free_count(a, sa) for sa in range(4)] for a in range(h + 1)]
        diffs = {interval: defaultdict(int) for interval in p15.PLANNED}
        for b in range(h + 1):
            diff = diffs[p15.shard_for_b(b)]
            for c in range(h + 1):
                bcv = BC[b][c]
                if not any(any(pair) for pair in bcv):
                    continue
                c3 = counter.component3(d, b, c)
                if c3 < 0:
                    continue
                for a in range(h + 1):
                    avec = A[a]
                    if not any(avec):
                        continue
                    M = a + b + c
                    ca = counter.component_a(d, a)
                    if ca < 0:
                        continue
                    srem = min(16, d) + ca + c3
                    scount = [0 for _ in range(11)]
                    for sbc, pair in enumerate(bcv):
                        left = int(pair[0]) + int(pair[1])
                        if not left:
                            continue
                        for sa, right in enumerate(avec):
                            if right:
                                scount[sbc + sa] += left * int(right)
                    for support, count in enumerate(scount):
                        if not count:
                            continue
                        qneed = K - support
                        if qneed > 0 and srem < qneed:
                            continue
                        lower = max(legacy, K, d - 4*g + 4, M, M + max(0, qneed))
                        upper = min((19*d)//5, 3*d, 3*d - (b-c))
                        if lower > upper:
                            continue
                        excluded = set()
                        e_n358 = 3*d - (b-c)
                        if b <= h - 5 and support + srem == K and e_n358 - M >= srem:
                            excluded.add(e_n358)
                        if g == 1 and d == 8:
                            excluded.add(8)
                        lo = lower if lower % 2 == 0 else lower + 1
                        hi = upper if upper % 2 == 0 else upper - 1
                        if lo > hi:
                            continue
                        diff[lo] += count
                        diff[hi + 2] -= count
                        for ex in excluded:
                            if lo <= ex <= hi and ex % 2 == 0:
                                diff[ex] -= count
                                diff[ex + 2] += count
        for interval in p15.PLANNED:
            diff = diffs[interval]
            caps = {}
            running = 0
            if diff:
                for e in range(min(diff), max(diff) + 1, 2):
                    running += diff.get(e, 0)
                    if running:
                        B = 19*d - 5*e + 1
                        req(B > 0 and B % 2 == 1, f"normal block drift {(g,d,interval,e,B)}")
                        caps[e] = running
            P = sum(n * (19*d - 5*e + 1) for e, n in caps.items())
            key = (interval, int(g), int(d))
            R = int(rejected[key])
            req(0 <= R <= P, f"pilot rejected mass exceeds pre mass {key}")
            cells[key] = {"pre_mass": P, "post_mass": P-R, "rejected_mass": R, "pre_e_term_caps": {e: n*(19*d-5*e+1) for e,n in caps.items()}}
    req(len(cells) == len(pilot_rows) * len(p15.PLANNED), "pilot exact-cell coverage")
    return cells, BC


def full_survivors(h16, profiles, h, g, b, c):
    caps = [[], []]
    xr = h16.a0_interval(h, g, b, c)
    if xr is not None:
        left, right = xr
        for x4 in range(left, right + 1):
            room = -h16.f0(h, g, b, c, x4)
            req(room >= 0, "full-hist q interval construction regression")
            caps[x4 & 1].append(room // 138)
    caps[0].sort(); caps[1].sort()
    out = [[None for _ in range(4)] for __ in range(h + 1)]
    for a in range(h + 1):
        for s in range(4):
            tiers = profiles[a][s]
            if not tiers:
                continue
            grouped = defaultdict(int)
            for q, mult in tiers:
                surv = tuple(len(caps[r]) - bisect.bisect_left(caps[r], q) for r in (0,1))
                grouped[surv] += mult
            out[a][s] = {"tiers": [(k[0], k[1], v) for k,v in sorted(grouped.items())]}
    return out


def main() -> None:
    h20 = load_parent(); h19 = h20.load_parent(); h18 = h19.load_parent(); h17 = h18.load_parent(); h16 = h17.load_parent()
    p15 = h16.load_module(h16.PARENT, h16.PARENT_BLOB, "hpadj15_locked_for_hpadj21_bounded")
    p14 = p15.load_parent(); counter = p14.load_counter()
    manifest = counter.load_locked_json(p14.MANIFEST, p14.LOCKS["manifest_blob"], p14.LOCKS["manifest_canonical"], "FULL178 manifest")
    rows = counter.manifest_rows(manifest)
    pilot_rows = [(row_id, int(g), int(d)) for row_id,g,d in rows if int(d) <= MAX_PILOT_D]
    req(pilot_rows, "no pilot rows")
    cells, BC = exact_pilot_cells(p15, p14, counter, pilot_rows)
    H = max(d//2 for _,_,d in pilot_rows)
    two_profiles, _, _, _ = h20.build_two_tier_profiles(H, counter, h19)
    profiles, classes_gt2, tuples_above_second = full_profiles(H, counter, h19)
    req(classes_gt2 > 0 and tuples_above_second > 0, "pilot lacks genuine >2-bin qA classes")

    strict = []
    tested = 0
    for row_id, g, d in pilot_rows:
        h = d//2; legacy = 8 if g == 0 else 4; K = counter.ceil_div(d - 16*g + 16, 4)
        A = [[sum(mult for _,mult in profiles[a][sa]) for sa in range(4)] for a in range(h+1)]
        two_caps = {interval: defaultdict(int) for interval in p15.PLANNED}
        exact_caps = {interval: defaultdict(int) for interval in p15.PLANNED}
        for b in range(h+1):
            interval = p15.shard_for_b(b)
            for c in range(h+1):
                bcv = BC[b][c]
                if not any(any(pair) for pair in bcv): continue
                c3 = counter.component3(d,b,c)
                if c3 < 0: continue
                two_surv, _ = h20.survivor_profiles(h16,h19,two_profiles,h,g,b,c)
                exact_surv = full_survivors(h16,profiles,h,g,b,c)
                for a in range(h+1):
                    if not any(A[a]): continue
                    M=a+b+c; ca=counter.component_a(d,a)
                    if ca < 0: continue
                    srem=min(16,d)+ca+c3
                    for sbc,pair in enumerate(bcv):
                        for r in (0,1):
                            left=int(pair[r])
                            if not left: continue
                            for sa,right in enumerate(A[a]):
                                if not right: continue
                                ti=two_surv[a][sa]; fi=exact_surv[a][sa]
                                req(ti is not None and fi is not None, "missing q profile")
                                support=sbc+sa; qneed=K-support
                                if qneed>0 and srem<qneed: continue
                                lower=max(legacy,K,d-4*g+4,M,M+max(0,qneed)); upper=min((19*d)//5,3*d,3*d-(b-c))
                                if lower>upper: continue
                                excluded=set(); e_n358=3*d-(b-c)
                                if b<=h-5 and support+srem==K and e_n358-M>=srem: excluded.add(e_n358)
                                if g==1 and d==8: excluded.add(8)
                                lo=lower if lower%2==0 else lower+1; hi=upper if upper%2==0 else upper-1
                                for e in range(lo,hi+1,2):
                                    if e in excluded: continue
                                    B=19*d-5*e+1
                                    for s0,s1,mult in ti["tiers"]:
                                        two_caps[interval][((s0 if r==0 else s1),B)] += left*int(mult)*B
                                    for s0,s1,mult in fi["tiers"]:
                                        exact_caps[interval][((s0 if r==0 else s1),B)] += left*int(mult)*B
        for interval in p15.PLANNED:
            key=(interval,g,d); info=cells[key]; P=int(info["pre_mass"]); Mpost=int(info["post_mass"])
            req(sum(two_caps[interval].values())==P, f"two-tier pre-mass mismatch {key}")
            req(sum(exact_caps[interval].values())==P, f"full-hist pre-mass mismatch {key}")
            tobj,_,_,_=h18.optimize_cell_exact_predomain(two_caps[interval],Mpost)
            fobj,_,_,_=h18.optimize_cell_exact_predomain(exact_caps[interval],Mpost)
            req(fobj<=tobj, f"full histogram weakened HPADJ20 {key}")
            tested += 1
            if fobj<tobj:
                diff=tobj-fobj
                strict.append({"row_id":row_id,"g":g,"d":d,"b_interval":list(interval),"pre_mass":P,"post_mass":Mpost,"hpadj20_num":tobj.numerator,"hpadj20_den":tobj.denominator,"full_hist_num":fobj.numerator,"full_hist_den":fobj.denominator,"hpadj20_floor":tobj.numerator//tobj.denominator,"full_hist_floor":fobj.numerator//fobj.denominator,"improvement_num":diff.numerator,"improvement_den":diff.denominator})

    out={"schema":"STAGE32EX5_HPADJ21_BOUNDED_EXACT_FULL_QA_STRICTNESS_PILOT_V1","route_id":"HPADJ-21_ex5","status":"STRICT_WITNESS_FOUND" if strict else "NO_STRICT_WITNESS_IN_BOUNDED_PILOT","source":{"hpadj20_parent_blob_sha1":PARENT_BLOB,"max_pilot_d":MAX_PILOT_D,"pilot_row_count":len(pilot_rows),"pilot_rows":[[r,g,d] for r,g,d in pilot_rows]},"full_histogram":{"classes_with_more_than_two_qA_bins":classes_gt2,"tuples_above_second_qA_level":tuples_above_second,"population_preserved_exactly":True},"lp_check":{"tested_exact_cells":tested,"no_weaker_exact_cells":tested,"strict_exact_cell_count":len(strict),"strict_witnesses":strict[:16]},"semantics":{"same_pre_domain_population_as_hpadj20":True,"same_post_mass_constraint_as_hpadj20":True,"same_picard_character_as_hpadj20":True,"bounded_pilot_is_not_full178_numeric_replay":True,"strict_global_numeric_bound_claimed":False,"additive_subtraction_used":False,"statistical_independence_assumed":False,"main_consumption_performed":False},"firewalls":{"stage32_main_pruning_credit":False,"current_main_incremental_credit":False,"full178_complete":False,"effectivity_credit":False,"receiver_credit":False,"theorem_credit":False,"endpoint_credit":False,"perfect_cuboid_credit":False,"heavy_run_armed":False,"merge_authorized":False}}
    out["canonical_sha256_without_this_field"]=canonical(out)
    print(json.dumps(out,sort_keys=True,separators=(",",":")))


if __name__ == "__main__": main()
