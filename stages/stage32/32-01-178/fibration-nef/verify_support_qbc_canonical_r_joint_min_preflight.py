#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "run_hpadj22_support_qbc_local_row_b.py"
SOURCE_BLOB = "37e72735125c232e534d92c6e24c7afc0a0f4f24"
CANON = HERE / "verify_support_qbc_canonical_joint_min_preflight.py"
CANON_BLOB = "4296a18f9fb1b59f963206ff28af73a4e9cf7ef0"
INF = 10**30


def req(v: bool, m: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + m)


def blob(p: Path) -> str:
    raw = p.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load(p: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, p)
    req(spec is not None and spec.loader is not None, "cannot load " + str(p))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def canonical_r_joint_q_lower(canon, b: int, c: int, t: int, support: int, r: int) -> int:
    """Exact canonical qBC minimum with retained required-x4 parity r.

    In the exact H histogram,
      r = (x0+x8+x10) mod 2.
    Once x0,x1,x9 are fixed, x8+x10=c-t+x1+x9 is fixed, so r is
    decided before minimizing the remaining two-coordinate quadratic term.
    """
    b,c,t,support,r = map(int, (b,c,t,support,r))
    if not (0 <= support <= 7 and r in (0,1)) or ((t-c)&1):
        return INF

    best = INF
    for x0 in range(min(c,t)+1):
        for x1 in range(x0, min(b,t-x0)+1):
            rem = t-x0-x1
            for x9 in range(max(0,rem-c), min(b-x1,rem)+1):
                x5 = b-x1-x9
                x6 = rem-x9
                pair_total = c-t+x1+x9
                if min(x5,x6,pair_total) < 0:
                    continue
                if ((x0 + pair_total) & 1) != r:
                    continue

                base_support = sum(int(v>0) for v in (x0,x1,x5,x6,x9))
                pair_support = support-base_support
                if not (0 <= pair_support <= 2):
                    continue

                if x0 < x1:
                    pair_q = canon.min_pair_positive(pair_total,pair_support)
                else:
                    first_lower = x5 + int(x6>x9)
                    pair_q = canon.min_pair_positive_with_first_lower(
                        pair_total,pair_support,first_lower
                    )
                if pair_q >= INF:
                    continue
                q = x0*x0+x1*x1+x5*x5+x6*x6+x9*x9+pair_q
                best = min(best,q)
    return best


def bounded_formula_regression(canon) -> dict[str,int]:
    out = {
        "states":0,
        "canonical_finite":0,
        "r_finite":0,
        "r_infeasible_canonical_finite":0,
        "strict_finite":0,
        "equal_finite":0,
        "max_strict_gain":0,
        "weakening":0,
    }
    for b in range(9):
        for c in range(9):
            for t in range(b+c+1):
                if ((t-c)&1):
                    continue
                for support in range(8):
                    old = canon.canonical_joint_q_lower(b,c,t,support)
                    for r in (0,1):
                        out["states"] += 1
                        new = canonical_r_joint_q_lower(canon,b,c,t,support,r)
                        if old < INF:
                            out["canonical_finite"] += 1
                        if new < INF:
                            out["r_finite"] += 1
                        if old < INF and new >= INF:
                            out["r_infeasible_canonical_finite"] += 1
                        if old < INF and new < INF:
                            if new < old:
                                out["weakening"] += 1
                            elif new > old:
                                out["strict_finite"] += 1
                                out["max_strict_gain"] = max(out["max_strict_gain"],new-old)
                            else:
                                out["equal_finite"] += 1
    return out


def bounded_literal_regression(canon) -> dict[str,int]:
    literal: dict[tuple[int,int,int,int,int],int] = {}
    for xs in product(range(4),repeat=7):
        x0,x1,x5,x6,x8,x9,x10 = xs
        if x0>x1:
            continue
        if x0==x1 and (x5,x6)>(x8,x9):
            continue
        if (x1+x8+x9+x10)&1:
            continue
        b=x1+x5+x9
        c=x0+x6+x8+x10
        t=x0+x1+x6+x9
        support=sum(int(v>0) for v in xs)
        r=(x0+x8+x10)&1
        q=sum(v*v for v in xs)
        key=(b,c,t,support,r)
        literal[key]=min(literal.get(key,INF),q)

    mismatches=strict=max_gain=0
    for key, exact in literal.items():
        got=canonical_r_joint_q_lower(canon,*key)
        mismatches += int(got != exact)
        old=canon.canonical_joint_q_lower(*key[:4])
        if got > old:
            strict += 1
            max_gain=max(max_gain,got-old)
    return {
        "literal_keys":len(literal),
        "formula_mismatches":mismatches,
        "strict_vs_canonical_without_r":strict,
        "max_strict_gain":max_gain,
    }


def active_scan(canon) -> dict[str,object]:
    rows=[]
    crossings=[]
    b=36
    for c in (83,85,89):
        row={
            "c":c,"states":0,"canonical_finite":0,"r_finite":0,
            "r_infeasible_canonical_finite":0,"strict_finite":0,
            "max_strict_gain":0,
            "strict_with_canonical_floor_at_most_4992":0,
            "crosses_qbc_cap_4992":0,
        }
        for t in range(b+c+1):
            if ((t-c)&1):
                continue
            for support in range(8):
                old=canon.canonical_joint_q_lower(b,c,t,support)
                for r in (0,1):
                    row["states"] += 1
                    new=canonical_r_joint_q_lower(canon,b,c,t,support,r)
                    if old < INF:
                        row["canonical_finite"] += 1
                    if new < INF:
                        row["r_finite"] += 1
                    if old < INF and new >= INF:
                        row["r_infeasible_canonical_finite"] += 1
                    if old < INF and new < INF and new > old:
                        row["strict_finite"] += 1
                        row["max_strict_gain"]=max(row["max_strict_gain"],new-old)
                        if old <= 4992:
                            row["strict_with_canonical_floor_at_most_4992"] += 1
                    if old <= 4992 and new > 4992:
                        row["crosses_qbc_cap_4992"] += 1
                        crossings.append({
                            "c":c,"t":t,"support":support,"r":r,
                            "canonical_floor_without_r":old,
                            "canonical_r_floor":None if new>=INF else new,
                            "r_infeasible":new>=INF,
                            "gain_if_finite":None if new>=INF else new-old,
                        })
        rows.append(row)
    return {"rows":rows,"qbc_cap_crossing_states":crossings}


def main() -> None:
    req(SOURCE.is_file() and blob(SOURCE)==SOURCE_BLOB,"support worker blob drift")
    req(CANON.is_file() and blob(CANON)==CANON_BLOB,"canonical joint verifier blob drift")
    source=load(SOURCE,"canonical_r_source")
    canon=load(CANON,"canonical_r_parent")

    formula=bounded_formula_regression(canon)
    req(formula == {
        "states":5904,
        "canonical_finite":2256,
        "r_finite":1859,
        "r_infeasible_canonical_finite":397,
        "strict_finite":396,
        "equal_finite":1463,
        "max_strict_gain":30,
        "weakening":0,
    }, f"bounded formula regression drift {formula}")

    literal=bounded_literal_regression(canon)
    req(literal == {
        "literal_keys":1064,
        "formula_mismatches":0,
        "strict_vs_canonical_without_r":145,
        "max_strict_gain":4,
    }, f"literal regression drift {literal}")

    witness=(36,83,35,3)
    separate=source.aggregate_q_lower(*witness)
    relaxed=load(HERE/"verify_support_qbc_joint_min_preflight.py","canonical_r_relaxed").joint_q_lower(*witness)
    base=canon.canonical_joint_q_lower(*witness)
    r0=canonical_r_joint_q_lower(canon,*witness,0)
    r1=canonical_r_joint_q_lower(canon,*witness,1)
    req((separate,relaxed,base,r0,r1)==(4753,4825,4825,4825,8115),
        f"active r witness drift {(separate,relaxed,base,r0,r1)}")

    panel=active_scan(canon)
    req(panel["rows"] == [
        {"c":83,"states":960,"canonical_finite":586,"r_finite":562,
         "r_infeasible_canonical_finite":24,"strict_finite":202,
         "max_strict_gain":3290,"strict_with_canonical_floor_at_most_4992":187,
         "crosses_qbc_cap_4992":16},
        {"c":85,"states":976,"canonical_finite":596,"r_finite":571,
         "r_infeasible_canonical_finite":25,"strict_finite":207,
         "max_strict_gain":3430,"strict_with_canonical_floor_at_most_4992":188,
         "crosses_qbc_cap_4992":12},
        {"c":89,"states":1008,"canonical_finite":616,"r_finite":589,
         "r_infeasible_canonical_finite":27,"strict_finite":216,
         "max_strict_gain":3710,"strict_with_canonical_floor_at_most_4992":180,
         "crosses_qbc_cap_4992":4},
    ], f"active panel r summary drift {panel['rows']}")
    req(len(panel["qbc_cap_crossing_states"])==32,
        "active panel r qBC-cap crossing count drift")

    out={
        "schema":"STAGE32_32_01_178_SUPPORT_QBC_CANONICAL_R_JOINT_MIN_PREFLIGHT_V1",
        "status":"EXACT_CANONICAL_R_H_MIN_STRICTLY_DOMINATES_CANONICAL_JOINT__ZERO_MAIN_CREDIT",
        "source_locks":{
            "support_qbc_worker_blob_sha1":SOURCE_BLOB,
            "canonical_joint_min_verifier_blob_sha1":CANON_BLOB,
        },
        "claim":{
            "fixed_data":"(b,c,t,H-support,r)",
            "r_semantics":"r=(x0+x8+x10) mod 2, the exact qBC-histogram required-x4 parity",
            "exact_minimum":"minimum qBC over retained canonical H tuples with fixed r",
            "dominance":"canonical_r_joint_q_lower >= canonical_joint_q_lower pointwise",
            "safety":"the retained qBC histogram is already split by this exact r, so the r-conditioned minimum is same-population and loses no valid tuple",
            "actual_weighted_v48_gain_claimed":False,
        },
        "bounded_formula_regression":formula,
        "bounded_literal_enumeration":literal,
        "active_structural_witness":{
            "b":36,"c":83,"t":35,"support":3,
            "separate_floor":separate,
            "relaxed_joint_floor":relaxed,
            "canonical_floor_without_r":base,
            "canonical_r0_floor":r0,
            "canonical_r1_floor":r1,
            "r1_gain_vs_canonical":r1-base,
        },
        "active_three_cell_structural_scan":panel,
        "next_gate":"use canonical_r_joint_q_lower per exact retained histogram parity r in the same full-support+Picard successor replay",
        "firewalls":{
            "main_credit":False,
            "full178_numerical_census_changed":False,
            "effectivity_credit":False,
            "receiver_credit":False,
            "route_credit":False,
            "theorem_credit":False,
            "endpoint_credit":False,
            "stage32_closed":False,
            "merge_authorized":False,
        },
    }
    print("SUPPORT_QBC_CANONICAL_R_JOINT_MIN_PREFLIGHT="+json.dumps(out,sort_keys=True))


if __name__=="__main__":
    main()
