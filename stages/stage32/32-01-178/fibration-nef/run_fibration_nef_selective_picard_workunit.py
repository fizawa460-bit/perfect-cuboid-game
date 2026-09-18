#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json, os, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORKUNIT = HERE / "verify_fibration_nef_selective_picard_workunit_preflight.py"
WORKUNIT_BLOB = "0ee1c21df1b765e91937587903e873f83ec06729"
PLAN = HERE / "verify_fibration_nef_selective_workunit_plan_certificate.py"
PLAN_BLOB = "37745be7877f32a1804a350d8ebbeedc893d4a5b"
SELECTED_X4 = (0, 24, 48, 72, 96)
WORKUNIT_SIZE = 256
SCHEMA = "STAGE32_32_01_178_SELECTIVE_PICARD_WORKUNIT_RECEIPT_V1"

def req(v, m):
    if not v: raise SystemExit("FAIL: " + m)

def git_blob(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None: raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec); sys.modules[name] = mod; spec.loader.exec_module(mod)
    return mod

def csha(v):
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def stream_sha(records):
    h = hashlib.sha256()
    for r in records:
        h.update(json.dumps(r, sort_keys=True, separators=(",", ":")).encode()); h.update(b"\n")
    return h.hexdigest()

def atomic_write(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, sort_keys=True); f.write("\n"); f.flush(); os.fsync(f.fileno())
        os.replace(tmp, path)
    except BaseException:
        try: os.unlink(tmp)
        except FileNotFoundError: pass
        raise

def load_runtime():
    req(WORKUNIT.is_file() and git_blob(WORKUNIT) == WORKUNIT_BLOB, "workunit producer drift")
    req(PLAN.is_file() and git_blob(PLAN) == PLAN_BLOB, "plan certificate producer drift")
    wu = load_module(WORKUNIT, "s32_178_runtime_wu")
    req(int(wu.WORKUNIT_SIZE) == WORKUNIT_SIZE, "workunit size drift")
    req(wu.SELECTIVE.is_file() and wu.git_blob(wu.SELECTIVE) == wu.SELECTIVE_BLOB, "selective carrier drift")
    sel = wu.load_module(wu.SELECTIVE, "s32_178_runtime_sel")
    req(sel.STATIC_FIRST.is_file() and sel.git_blob(sel.STATIC_FIRST) == sel.STATIC_FIRST_BLOB, "static-first drift")
    sf = sel.load_module(sel.STATIC_FIRST, "s32_178_runtime_sf")
    for name, (path, expected) in sf.LOCKS.items():
        req(path.is_file() and sf.git_blob(path) == expected, f"static-first source drift {name}")
    depth2 = sf.load_module(sf.DEPTH2, "s32_178_runtime_d2")
    complete = sf.load_module(sf.COMPLETE, "s32_178_runtime_complete")
    req(depth2.DEPTH1.is_file() and depth2.git_blob(depth2.DEPTH1) == depth2.DEPTH1_BLOB, "depth1 drift")
    depth1 = depth2.load_module(depth2.DEPTH1, "s32_178_runtime_d1")
    for name, (path, expected) in depth1.LOCKS.items():
        req(path.is_file() and depth1.git_blob(path) == expected, f"depth1 source drift {name}")
    weighted = depth1.load_module(depth1.WEIGHTED, "s32_178_runtime_weighted")
    qthr = depth1.load_module(depth1.QTHRESH, "s32_178_runtime_qthr")
    weighted.lock_sources_before_import()
    for name, (path, expected) in qthr.SOURCE_LOCKS.items():
        req(path.is_file() and qthr.git_blob(path) == expected, f"qthreshold source drift {name}")
    sigmod = qthr.load_module(qthr.SIGNATURE, "s32_178_runtime_sig")
    existential = qthr.load_module(qthr.EXISTENTIAL, "s32_178_runtime_exist")
    req(existential.PREFIX.is_file() and existential.git_blob(existential.PREFIX) == existential.PREFIX_BLOB, "prefix drift")
    prefix = existential.load_module(existential.PREFIX, "s32_178_runtime_prefix")
    req(prefix.LEAF.is_file() and prefix.git_blob(prefix.LEAF) == prefix.LEAF_BLOB, "leaf drift")
    leaf = prefix.load_module(prefix.LEAF, "s32_178_runtime_leaf"); prefix.lock_leaf_and_dependencies(leaf)
    cert = leaf.load_picard_certificate()
    bnb = leaf.load_module(leaf.BNB, "s32_178_runtime_bnb"); bnb.lock_extra_sources()
    vf = bnb.load_module(bnb.RECOVERABILITY, "s32_178_runtime_vf"); vf.lock_sources()
    kernel = bnb.build_kernel(vf)
    req(complete.UNEQUAL.is_file() and complete.git_blob(complete.UNEQUAL) == complete.UNEQUAL_BLOB, "unequal producer drift")
    unequal = complete.load_module(complete.UNEQUAL, "s32_178_runtime_uneq")
    g, d, e = 1, 192, 32
    qcap = (d*d)//8 + 2*d + 4 - 4*g
    req(qcap == 4992, "qcap drift")
    limit = weighted.effective_mass_cap(e, qcap); req(limit == e, "mass cap drift")
    uh, _ = unequal.unequal_static_minq(limit, qcap)
    eh = complete.equal_static_minq(limit, qcap); hmin = complete.merge_static_minq(uh, eh)
    static_keys = []
    for a in range(limit + 1):
        qa = unequal.a_min_q_closed(a)
        if qa > qcap: continue
        for (b,c,t), qh in hmin.items():
            if a+b+c <= e and qa+qh <= qcap: static_keys.append((a,b,c,t,qa+qh))
    return locals()

def unit_for(rt, x4, ordinal):
    req(x4 in SELECTED_X4, f"x4={x4} outside retained selected-slice plan")
    req(ordinal >= 0, "negative unit ordinal")
    rows, _ = rt["sel"].survivor_rows(
        sf=rt["sf"], depth2=rt["depth2"], depth1=rt["depth1"], sigmod=rt["sigmod"],
        prefix=rt["prefix"], bnb=rt["bnb"], kernel=rt["kernel"], cert=rt["cert"],
        static_keys=rt["static_keys"], g=rt["g"], d=rt["d"], e=rt["e"], x4_values=(x4,))
    req(len(rows) == 1 and rows[0][0] == x4, "single-slice reconstruction drift")
    _, survivors, thresholds = rows[0]; ordered = tuple(sorted(survivors))
    req(len(ordered) == len(set(ordered)), "duplicate survivor key")
    start = ordinal * WORKUNIT_SIZE; req(start < len(ordered), "unit ordinal out of range")
    stop = min(start + WORKUNIT_SIZE, len(ordered)); chunk = ordered[start:stop]
    records = [{"row_id":"g1-d192","e":rt["e"],"x4":x4,"a":a,"b":b,"c":c,"t":t} for a,b,c,t in chunk]
    ident = {"workunit_id":f"g1-d192-e032-x4-{x4:04d}-u{ordinal:04d}","x4":x4,
             "start_index":start,"stop_index_exclusive":stop,"static_key_count":len(chunk),
             "static_key_stream_sha256":stream_sha(records)}
    return ident, chunk, thresholds

def execute(rt, ident, chunk, thresholds):
    a_cache, h_cache, evidence = {}, {}, []
    env_total = exact_total = no_picard = zero_mass = nodes = 0
    x4, qcap = int(ident["x4"]), rt["qcap"]
    for a,b,c,t in chunk:
        env_thr = int(thresholds[(a,b,c,t)])
        problem = rt["sigmod"].signature_problem(rt["bnb"], rt["kernel"], g=rt["g"], d=rt["d"], e=rt["e"], sig=(a,b,c,t,x4,0))
        req(not problem.get("structurally_infeasible"), "survivor became structurally infeasible")
        minimum, witness, stats = rt["qthr"].picard_min_penalty(
            rt["prefix"], rt["leaf"], rt["bnb"], rt["kernel"], problem, rt["cert"],
            static_values=(a,b,c,t,x4,rt["e"],rt["d"]))
        _cut, exact_thr = rt["qthr"].qexc_threshold(g=rt["g"], d=rt["d"], t=t, x4=x4, min_penalty=minimum)
        aq = a_cache.setdefault(a, rt["sel"].a_poly_for_key(a, qcap))
        hk = (b,c,t); hq = h_cache.setdefault(hk, rt["sel"].h_poly_for_key(b,c,t,qcap))
        req(aq and hq, "selective polynomial missing key")
        env_mass = rt["sel"].cumulative_product(aq, hq, min(qcap, env_thr))
        if exact_thr is None:
            exact_mass = 0; no_picard += 1
        else:
            exact_thr = int(exact_thr); req(exact_thr <= env_thr, "exact threshold exceeds envelope")
            exact_mass = rt["sel"].cumulative_product(aq, hq, min(qcap, exact_thr))
        req(exact_mass <= env_mass, "exact mass enlarged envelope")
        if exact_mass == 0: zero_mass += 1
        env_total += env_mass; exact_total += exact_mass; nodes += int(stats.visited_nodes)
        evidence.append({"static_key":[a,b,c,t],"depth2_envelope_threshold":env_thr,
                         "exact_picard_threshold":exact_thr,
                         "exact_picard_minimum":None if minimum is None else str(minimum),
                         "exact_picard_witness":None if witness is None else list(witness),
                         "exact_picard_minimum_nodes":int(stats.visited_nodes),
                         "depth2_envelope_weighted_mass":str(env_mass),
                         "exact_picard_weighted_mass":str(exact_mass)})
    req(len(evidence) == ident["static_key_count"], "executed key count mismatch")
    receipt = {"schema":SCHEMA,"role":"COMPLETE_EXACT_WORKUNIT_RECEIPT__NO_MAIN_CREDIT",
      "workunit_identity":ident,
      "source_locks":{"worker_blob_sha1":git_blob(Path(__file__)),"workunit_preflight_blob_sha1":WORKUNIT_BLOB,
                      "workunit_plan_certificate_producer_blob_sha1":PLAN_BLOB,
                      "selective_weighted_survivor_blob_sha1":rt["wu"].SELECTIVE_BLOB},
      "execution_semantics":{"row_id":"g1-d192","g":rt["g"],"d":rt["d"],"e":rt["e"],"absolute_qcap":qcap,"x4":x4,
                             "exact_picard_minimum_per_static_key":True,"selective_A_H_polynomials":True,
                             "unknown_count":0,"completed_key_count":len(evidence),
                             "atomic_receipt_written_only_after_complete_unit":True},
      "result":{"depth2_envelope_weighted_mass":str(env_total),"exact_picard_weighted_mass":str(exact_total),
                "exact_picard_tightening":str(env_total-exact_total),
                "no_picard_feasible_residual_static_keys":no_picard,
                "zero_exact_weighted_mass_static_keys":zero_mass,
                "aggregate_exact_picard_minimum_nodes":nodes,
                "key_evidence_stream_sha256":stream_sha(evidence),
                "key_evidence_rows_included":True,"key_evidence_rows":evidence},
      "firewalls":{"selected_slice_only":True,"full_row_census_claimed":False,"full178_census_claimed":False,
                   "main_credit_changed":False,"theorem_credit_changed":False,"endpoint_credit_changed":False,"merge":False}}
    receipt["canonical_sha256_without_this_field"] = csha(receipt)
    return receipt

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--x4", type=int, required=True); p.add_argument("--unit-ordinal", type=int, required=True)
    p.add_argument("--output", type=Path); p.add_argument("--identity-only", action="store_true")
    a = p.parse_args(); rt = load_runtime(); ident, chunk, thresholds = unit_for(rt, a.x4, a.unit_ordinal)
    if a.identity_only:
        print(json.dumps(ident, indent=2, sort_keys=True)); return
    receipt = execute(rt, ident, chunk, thresholds)
    if a.output: atomic_write(a.output, receipt)
    print("SELECTIVE_PICARD_WORKUNIT_RECEIPT_SUMMARY=" + json.dumps({
        "workunit_id":ident["workunit_id"],"static_key_count":ident["static_key_count"],
        "exact_picard_weighted_mass":receipt["result"]["exact_picard_weighted_mass"],
        "tightening":receipt["result"]["exact_picard_tightening"],
        "receipt_sha256":receipt["canonical_sha256_without_this_field"]}, sort_keys=True))
    print(json.dumps(receipt, indent=2, sort_keys=True))

if __name__ == "__main__": main()
