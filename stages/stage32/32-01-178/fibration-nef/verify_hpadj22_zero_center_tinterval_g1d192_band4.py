#!/usr/bin/env python3
from __future__ import annotations

import argparse
import bisect
import hashlib
import importlib.util
import json
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
DIRECT_REL = Path("stages/stage32/management/hpadj22-fast-global/benchmark_direct_count.py")
DIRECT_BLOB = "e965ab0a6ea51938006882ca2110016f48b3768e"
FAST = HERE / "verify_fibration_nef_lowmass_parity_separable_picard_min.py"
FAST_BLOB = "a4f7b35e52d01d36614c7f46a592fdb7cb54518b"

ROW_INDEX = 22
ROW_ID = "g1-d192"
BAND = 4
CURRENT_GLOBAL = 138652739800650593494
ONE_PERCENT = CURRENT_GLOBAL // 100


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, "cannot load " + str(path))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def nearest_t_distance(*, d: int, b: int, c: int, x4: int) -> int:
    # Every retained H tuple has
    #   t=x0+x1+x6+x9,
    #   b+c=t+x5+x8+x10 >= t,
    # and retained parity x1+x8+x9+x10 == 0 gives t == c (mod 2).
    # Minimize |d/2-2*x4-t| over the deliberately enlarged parity interval;
    # enlarging the actual t-set can only lower the penalty, hence is safe.
    parity = c & 1
    lo = parity
    hi = b + c
    if (hi & 1) != parity:
        hi -= 1
    req(lo <= hi, f"empty parity interval {(b,c)}")
    y = d // 2 - 2 * x4
    if y < lo:
        return lo - y
    if y > hi:
        return y - hi
    return (y - parity) & 1


def qcut(*, g: int, d: int, b: int, c: int, x4: int, a_parity: int) -> int:
    z = nearest_t_distance(d=d, b=b, c=c, x4=x4)
    p0 = (b + c) & 1
    p1 = int(a_parity) & 1
    # q/2 + z^2/12 + p0/2 + p1/10 <= d^2/16+d+2-2g.
    # Multiply by 120 and solve exactly for integral q.
    rhs120 = (15 * d * d) // 2 + 120 * d + 240 - 240 * g
    num = rhs120 - 10 * z * z - 60 * p0 - 12 * p1
    return num // 60


def caps_ge(sorted_caps: list[int], qa: int) -> int:
    return len(sorted_caps) - bisect.bisect_left(sorted_caps, int(qa))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", type=Path, required=True)
    ap.add_argument("--source-root", type=Path, required=True)
    args = ap.parse_args()

    direct_path = args.repo_root / DIRECT_REL
    req(direct_path.is_file() and blob(direct_path) == DIRECT_BLOB, "direct-count source drift")
    req(FAST.is_file() and blob(FAST) == FAST_BLOB, "zero-center parity source drift")
    direct = load(direct_path, "stage32_178_tinterval_direct")
    fast = load(FAST, "stage32_178_tinterval_fast")
    cert = fast.load_certificate()
    req(int(cert["membership_modulus"]) == 2, "Picard modulus drift")

    old = direct.load_old(args.source_root)
    ctx = old.source_context()
    bc,bnd,h21,h18,h16,p15,p14,counter,rows,rejected,profiles,classes_gt2,tuples_above_second = ctx

    row_id,g0,d0 = rows[ROW_INDEX]
    g,d = int(g0),int(d0)
    req((row_id,g,d) == (ROW_ID,1,192), "target row drift")
    req(d % 2 == 0, "target degree parity drift")
    h = d // 2
    K = counter.ceil_div(d - 16*g + 16, 4)
    tq = (d*d + 16*d + (32 if g == 0 else 0)) // 8
    req(tq == 4992, "target q threshold drift")

    b0,b1 = old.PLANNED[BAND]
    joint = bc.build_joint_bc_shard(old.HMAX,b0,b1)

    # Independent current-row replay with the exact current HPADJ22 direct counter.
    baseline = direct.direct_count(old, ctx, joint, BAND, ROW_INDEX)
    baseline_current = int(baseline["hpadj22_exact_survivors"])

    ca = [counter.component_a(d,a) for a in range(h+1)]
    row_aprof = {}
    row_qas = set()
    for a in range(h+1):
        if ca[a] < 0:
            continue
        for sa in range(4):
            tiers = profiles[a][sa]
            if tiers:
                tt = tuple((int(q),int(v)) for q,v in tiers)
                row_aprof[(a,sa)] = tt
                row_qas.update(q for q,_ in tt)

    current = refined = 0
    strict_bc = 0
    bc_records = []

    for b in range(b0,min(b1,h)+1):
        for c in range(h+1):
            jbc = joint[b][c]
            active = []
            for sbc in range(8):
                for r in (0,1):
                    hist = jbc[sbc][r]
                    if not hist:
                        continue
                    qs=[]; pref=[]; tot=0
                    for q,v in sorted((int(q),int(v)) for q,v in hist.items() if int(v)):
                        qs.append(q); tot += v; pref.append(tot)
                    if tot:
                        active.append((sbc,r,qs,pref))
            if not active:
                continue

            c3 = counter.component3(d,b,c)
            if c3 < 0:
                continue

            caps = bnd.x4_caps(h16,h,g,b,c)
            xr = h16.a0_interval(h,g,b,c)
            if xr is None:
                continue

            # For each A parity and required x4 parity, group actual x4 values by
            # the new q-cut and retain their individual current x4 qA capacities.
            groups = {
                ap: {0: defaultdict(list), 1: defaultdict(list)}
                for ap in (0,1)
            }
            for x4 in range(int(xr[0]), int(xr[1])+1):
                room = -int(h16.f0(h,g,b,c,x4))
                req(room >= 0, f"negative current x4 room {(b,c,x4)}")
                cap = room // 138
                r = x4 & 1
                for ap in (0,1):
                    cut = qcut(g=g,d=d,b=b,c=c,x4=x4,a_parity=ap)
                    req(cut <= tq, f"new cut weakened current threshold {(b,c,x4,ap,cut)}")
                    groups[ap][r][cut].append(cap)
            for ap in (0,1):
                for r in (0,1):
                    for cut in list(groups[ap][r]):
                        groups[ap][r][cut].sort()

            bc_cur = bc_ref = 0
            for a in range(h+1):
                if ca[a] < 0:
                    continue
                srem = min(16,d) + ca[a] + c3
                ec = {}
                for support in range(11):
                    es = bnd.eligible_e(counter,d,g,h,a,b,c,support,srem,K)
                    if es:
                        req(all((int(e)&1)==0 for e in es),
                            f"odd eligible e {(a,b,c,support)}")
                        ec[support] = len(es)
                if not ec:
                    continue

                ap = a & 1
                for sbc,r,qs,pref in active:
                    for sa in range(4):
                        tiers = row_aprof.get((a,sa))
                        ne = ec.get(sbc+sa)
                        if tiers is None or ne is None:
                            continue
                        for qa,va in tiers:
                            qa=int(qa); va=int(va)
                            cur_x4 = int(bnd.survivor_count(caps,r,qa))
                            if not cur_x4:
                                continue
                            # Cross-check our grouped actual-x4 capacities against
                            # the current HPADJ22 parity-cap adapter.
                            grouped_x4 = sum(
                                caps_ge(caplist,qa)
                                for caplist in groups[ap][r].values()
                            )
                            req(grouped_x4 == cur_x4,
                                f"x4 grouping/current adapter mismatch {(a,b,c,r,qa,grouped_x4,cur_x4)}")

                            cur_h = direct.ple(qs,pref,tq-qa)
                            cur = cur_h * cur_x4
                            ref = 0
                            for cut, caplist in groups[ap][r].items():
                                n4 = caps_ge(caplist,qa)
                                if n4:
                                    ref += n4 * direct.ple(qs,pref,int(cut)-qa)
                            req(ref <= cur, f"refined count weakened {(a,b,c,sbc,r,sa,qa)}")
                            w = va * int(ne)
                            bc_cur += cur * w
                            bc_ref += ref * w

            current += bc_cur
            refined += bc_ref
            if bc_ref < bc_cur:
                strict_bc += 1
                bc_records.append({
                    "b":b,"c":c,
                    "current":str(bc_cur),
                    "refined":str(bc_ref),
                    "reduction":str(bc_cur-bc_ref),
                })

    req(current == baseline_current,
        f"same-population row-band identity drift {current} != {baseline_current}")
    reduction = current - refined
    candidate = CURRENT_GLOBAL - reduction
    out = {
        "schema":"STAGE32_32_01_178_HPADJ22_ZERO_CENTER_TINTERVAL_G1D192_BAND4_V1",
        "status":"EXACT_CURRENT_HPADJ22_ROW_BAND_REFINEMENT__ZERO_MAIN_CREDIT",
        "target":{"row_index":ROW_INDEX,"row_id":ROW_ID,"g":g,"d":d,
                  "band_position":BAND,"b_interval":[b0,b1]},
        "result":{
            "current_row_band_survivors":str(current),
            "refined_row_band_survivors":str(refined),
            "exact_reduction":str(reduction),
            "current_global_upper_bound":str(CURRENT_GLOBAL),
            "candidate_global_upper_bound_if_promoted":str(candidate),
            "global_reduction_fraction":reduction/CURRENT_GLOBAL,
            "one_percent_threshold":str(ONE_PERCENT),
            "one_percent_reached_by_this_single_row_band":reduction >= ONE_PERCENT,
            "strict_bc_cells":strict_bc,
        },
        "mathematics":{
            "actual_H_identity":"b+c=t+x5+x8+x10, hence 0<=t<=b+c",
            "actual_H_parity":"t == c (mod 2)",
            "safe_t_relaxation":"all integers t in [0,b+c] with parity c",
            "z_lower_bound":"min |d/2-2*x4-t| over safe_t_relaxation",
            "picard_minimum_lower_bound":"((b+c) mod2)/2 + (a mod2)/10",
            "necessary_inequality":"qexc/2 + z_min^2/12 + parity_min <= d^2/16+d+2-2g",
            "general_caps_and_exact_t_deliberately_ignored":True,
            "therefore_zero_loss_but_weaker_than_full_zero_center":True,
        },
        "validation":{
            "current_row_band_replayed_by_current_direct_counter":True,
            "our_current_count_matches_direct_counter":True,
            "grouped_x4_capacities_match_current_adapter_for_every_used_qA":True,
            "source_picard_certificate_loaded":True,
        },
        "strict_cells":bc_records,
        "semantics":{
            "same_population_as_current_hpadj22":True,
            "direct_replacement_not_additive_subtraction":True,
            "all_non_target_current_hpadj22_survivors_unchanged":True,
            "main_consumption_performed":False,
        },
        "firewalls":{
            "main_credit_changed":False,"full178_complete":False,
            "hostile_audit_required_before_promotion":True,
            "theorem_credit_changed":False,"endpoint_credit_changed":False,
            "merge":False,
        },
    }
    print("HPADJ22_ZERO_CENTER_TINTERVAL_G1D192_BAND4="+json.dumps({
        "current":str(current),"refined":str(refined),"reduction":str(reduction),
        "global_fraction":reduction/CURRENT_GLOBAL,
        "one_percent":reduction>=ONE_PERCENT,
        "candidate_global":str(candidate),"strict_bc":strict_bc,
    },sort_keys=True))
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
