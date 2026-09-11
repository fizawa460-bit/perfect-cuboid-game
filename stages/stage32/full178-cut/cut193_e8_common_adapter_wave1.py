#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

from sympy import Matrix
from z3 import Int, SolverFor, Sum, get_version_string, sat, unknown, unsat

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EX5_HANDOFF = ROOT / "stages/stage32-ex5/cut-handoff"
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
sys.path.insert(0, str(EX5_HANDOFF))
sys.path.insert(0, str(RESIDUAL))

import e8_terminal_population_adapter as e8

SCHEMA = "STAGE32_CUT193_E8_COMMON_ADAPTER_WAVE1_SHARD_V1"
PACKS = [[33, 36, 37, 40, 41, 44], [34, 35, 38, 39, 42, 43]]
NORMAL_COUNT = 92
NORMAL_MASS = 112
TARGET_D = 8
TARGET_E = 8
DEFAULT_PRIMES = [2, 3, 5, 7, 11, 13, 17, 31, 127]
MAIN_STATE = ROOT / "stages/stage32/MAIN-STATE.json"
PREFLIGHT = HERE / "CUT193-e8-common-adapter-wave1-preflight.json"
EX5_PREFLIGHT = EX5_HANDOFF / "e8-terminal-population-preflight.json"
EX5_ADAPTER = EX5_HANDOFF / "e8_terminal_population_adapter.py"
EX5_VERIFY = EX5_HANDOFF / "verify_e8_terminal_population_adapter.py"
CUT102_REFERENCE = HERE / "cut102_finite_ring_direct_completion_v2.py"
LOCKS = {
    EX5_PREFLIGHT: "b28539d9d0eafddc181d3bbf6d668261f2ff081e",
    EX5_ADAPTER: "6026d2c8b4a2eb69c453a2bd38c5923f46d6d74f",
    EX5_VERIFY: "8fe802444ca8c92a80058555eaf431f0c1a52c76",
    CUT102_REFERENCE: "fbdd1e65b509526d5198743208bff79bd2488673",
}
MAIN_CANONICAL = "4c143ad944a3506f0c39acdd5cc697276576aa5d0c7293c433d10834f9f462f3"
PREFLIGHT_CANONICAL = "ce2f1eba5e5fe5cb71e3ad822096086c00ecae76ea86cadf02941b5741fccbca"
MAIN_TERMINALS = 65396964990500233636101
MAIN_STRATA = 17128


def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise RuntimeError(msg)


def source_and_authority_preflight() -> dict:
    for path, expected in LOCKS.items():
        req(blob(path) == expected, f"source-lock drift: {path.relative_to(ROOT)}")
    subprocess.run([sys.executable, str(EX5_VERIFY)], cwd=ROOT, check=True)
    pf = json.loads(PREFLIGHT.read_text())
    qpf = dict(pf); claimed_pf = qpf.pop("canonical_sha256_without_this_field", None)
    req(pf["schema"] == "STAGE32_CUT193_E8_COMMON_ADAPTER_WAVE1_PREFLIGHT_V1" and claimed_pf == PREFLIGHT_CANONICAL and csha(qpf) == PREFLIGHT_CANONICAL, "CUT193 preflight canonical/schema drift")
    main = json.loads(MAIN_STATE.read_text())
    claimed = main.get("canonical_sha256_without_this_field")
    body = dict(main); body.pop("canonical_sha256_without_this_field", None)
    req(claimed == MAIN_CANONICAL and csha(body) == MAIN_CANONICAL, "MAIN V12 canonical drift")
    req(main.get("schema") == "STAGE32_MAIN_COMPACT_STATE_V12_CUT191_AUDITED_CONSUMED", "MAIN V12 schema drift")
    f = main["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == MAIN_STRATA, "MAIN strata drift")
    req(f["authoritative_remaining_terminals"] == MAIN_TERMINALS, "MAIN terminals drift")
    req(f["n356_main_pruning_credit"] is True and f["cut191_main_pruning_credit"] is True, "N356/CUT191 authority not consumed")
    req(f["cut191_incremental_rejected_terminals"] == 113, "CUT191 width drift")
    return main


def left_kernel_mod_p(P: Matrix, prime: int) -> tuple[list[list[int]], int]:
    a = [[int(P[col, row]) % prime for col in range(P.rows)] for row in range(P.cols)]
    nrows, ncols = len(a), len(a[0])
    pivots: list[int] = []
    r = 0
    for c in range(ncols):
        pivot = next((i for i in range(r, nrows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, prime)
        a[r] = [(v * inv) % prime for v in a[r]]
        for i in range(nrows):
            if i == r or not a[i][c]:
                continue
            q = a[i][c]
            a[i] = [(x - q * y) % prime for x, y in zip(a[i], a[r])]
        pivots.append(c); r += 1
        if r == nrows:
            break
    pset = set(pivots)
    basis = []
    for f in (c for c in range(ncols) if c not in pset):
        v = [0] * ncols; v[f] = 1
        for i, pc in enumerate(pivots):
            v[pc] = (-a[i][f]) % prime
        req(not any(sum(v[i] * int(P[i, j]) for i in range(P.rows)) % prime for j in range(P.cols)), f"left-kernel replay failed mod {prime}")
        basis.append(v)
    return basis, len(pivots)


def row_sum(m: Matrix, labels: list[int]) -> Matrix:
    out = Matrix.zeros(1, m.cols)
    for label in labels:
        out += m.row(label - 1)
    return out


def load_picard_interface():
    g = e8.load_geometry()
    d18 = e8.d18
    bundle = d18.load_retained(d18.RETAINED, "s32cut193_bundle")
    marking = d18.load_retained(d18.MARKING, "s32cut193_marking")
    adapter = d18.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = Matrix(adapter.pairing_matrix)
    coords = Matrix(adapter.class_coordinates_in_retained_basis)
    gram = Matrix(bundle["picard_gram_64x64"])
    req(P.shape == (140,64) and coords.shape == (140,64) and gram.shape == (64,64), "Picard matrix shape drift")
    full = coords * gram * coords.T
    blocks = []
    fibre_coeffs = []
    for pack in PACKS:
        seen, factor_blocks, funcs = [], [], []
        for boundary in pack:
            inc = [j for j in range(93,141) if int(full[boundary-1,j-1]) == 1]
            req(len(inc) == 8, f"incidence regression boundary {boundary}")
            seen.extend(inc); factor_blocks.append(inc)
            funcs.append(2*P.row(boundary-1) + row_sum(P,inc))
        req(sorted(seen) == list(range(93,141)) and all(f == funcs[0] for f in funcs[1:]), "fibre partition regression")
        blocks.append(factor_blocks); fibre_coeffs.append(funcs[0])
    req(19*(fibre_coeffs[0]+fibre_coeffs[1]) == row_sum(P,list(range(1,93))) + 5*row_sum(P,list(range(93,141))), "degree-sum functional regression")
    return P, blocks, g


def make_solver(P: Matrix, blocks, prime: int, timeout_ms: int):
    kernel, rank = left_kernel_mod_p(P, prime)
    y = [Int(f"y_{prime}_{i+1}") for i in range(140)]
    s = SolverFor("QF_LIA"); s.set(timeout=timeout_ms)
    for i in range(NORMAL_COUNT):
        s.add(y[i] >= 0, y[i] <= NORMAL_MASS)
    for i in range(NORMAL_COUNT,140):
        s.add(y[i] >= 0, y[i] <= TARGET_E)
    s.add(Sum(y[:NORMAL_COUNT]) == NORMAL_MASS, Sum(y[NORMAL_COUNT:]) == TARGET_E)
    fibre = []
    for pack, factor_blocks in zip(PACKS, blocks):
        vals = [2*y[b-1] + Sum([y[j-1] for j in block]) for b,block in zip(pack,factor_blocks)]
        for v in vals[1:]: s.add(v == vals[0])
        fibre.append(vals[0])
    n1,n2 = fibre
    s.add(n1+n2 == TARGET_D, n1>=0, n1<=TARGET_D, n2>=0, n2<=TARGET_D)
    for label in range(93,141): s.add(y[label-1] <= TARGET_D//2)
    for b1 in blocks[0]:
        a = Sum([y[j-1] for j in b1])
        for b2 in blocks[1]: s.add(a + Sum([y[j-1] for j in b2]) <= TARGET_D)
    for h in kernel:
        terms = [int(h[i])*y[i] for i in range(140) if h[i] % prime]
        s.add(Sum(terms) % prime == 0)
    return s,y,{"prime":prime,"rank_mod_p":rank,"left_kernel_dimension":len(kernel)}


def check_with_fixed(s, y, fixed: dict[int,int]):
    s.push()
    for label,value in fixed.items(): s.add(y[label-1] == int(value))
    r = s.check()
    reason = s.reason_unknown() if r == unknown else None
    s.pop()
    return str(r), reason


def classify_block(block_index: int, P: Matrix, blocks, g, solvers: dict[int,tuple], primes: list[int]) -> dict:
    sig = e8.block_signature(block_index)
    req(sig["current_main_audited_prefix_survivor"] is True, f"block {block_index} lost N220/N355 survival")
    sums = [int(v) for v in sig["n355_known_group_sums"]]
    req(max(sums) <= 4, "N355 survivor group cap drift")
    n356_lhs = sums[1] - sums[2]
    req(n356_lhs <= 4 <= 16, f"N356 bridge failed on block {block_index}")
    req(block_index != 0, "CUT193 wave overlaps consumed CUT191 block0")
    fixed_terminal = {int(k):int(v) for k,v in sig["fixed_exceptional_pairings"].items()}

    whole_attempts = []
    for prime in primes:
        s,y,_ = solvers[prime]
        result,reason = check_with_fixed(s,y,fixed_terminal)
        whole_attempts.append({"prime":prime,"result":result,**({"reason_unknown":reason} if reason else {})})
        if result == "unsat":
            return {"block_index":block_index,"terminal_rank_range":sig["terminal_rank_range"],"terminal_count":113,"n355_group_sums":sums,"n356_lhs_b_minus_c":n356_lhs,"method":"WHOLE_BLOCK_FINITE_RING_UNSAT","whole_block_obstruction_prime":prime,"whole_block_attempts":whole_attempts,"modular_feasible_parent_count":None,"closed_candidate":True,"candidate_pruned_terminals":113}

    parent_records = list(e8.iter_parent_population(block_index,g))
    parent_count = len(parent_records)
    if parent_count == 0:
        return {"block_index":block_index,"terminal_rank_range":sig["terminal_rank_range"],"terminal_count":113,"n355_group_sums":sums,"n356_lhs_b_minus_c":n356_lhs,"method":"HNF_PARENT_POPULATION_EMPTY","whole_block_attempts":whole_attempts,"modular_feasible_parent_count":0,"closed_candidate":True,"candidate_pruned_terminals":113}

    unresolved = set(range(parent_count))
    obstruction_prime: dict[int,int] = {}
    unknown_checks = 0
    for prime in primes:
        s,y,_ = solvers[prime]
        for ordinal in list(unresolved):
            rec = parent_records[ordinal]
            fixed = {int(label):int(value) for label,value in zip(g.exceptional_labels,rec["selected_exceptional_pairings"])}
            result,_reason = check_with_fixed(s,y,fixed)
            if result == "unsat":
                obstruction_prime[ordinal] = prime; unresolved.remove(ordinal)
            elif result == "unknown":
                unknown_checks += 1
    oh = hashlib.sha256()
    hist = {str(p):0 for p in primes}
    for ordinal in sorted(obstruction_prime):
        p = obstruction_prime[ordinal]; hist[str(p)] += 1; oh.update(f"{ordinal}:{p}\n".encode())
    rh = hashlib.sha256()
    for ordinal in sorted(unresolved): rh.update(f"{ordinal}\n".encode())
    closed = not unresolved
    return {"block_index":block_index,"terminal_rank_range":sig["terminal_rank_range"],"terminal_count":113,"n355_group_sums":sums,"n356_lhs_b_minus_c":n356_lhs,"method":"ALL_HNF_PARENTS_FINITE_RING_UNSAT" if closed else "FINITE_RING_NONCLOSING_RESIDUAL_PARENTS","whole_block_attempts":whole_attempts,"modular_feasible_parent_count":parent_count,"finite_ring_obstructed_parent_count":len(obstruction_prime),"residual_parent_count":len(unresolved),"obstruction_prime_histogram":hist,"obstruction_assignment_sha256":oh.hexdigest(),"residual_parent_ordinal_sha256":rh.hexdigest(),"unknown_check_count":unknown_checks,"closed_candidate":closed,"candidate_pruned_terminals":113 if closed else 0}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--survivor-offset-start", type=int, required=True)
    ap.add_argument("--survivor-offset-count", type=int, required=True)
    ap.add_argument("--primes", default=",".join(map(str,DEFAULT_PRIMES)))
    ap.add_argument("--timeout-ms", type=int, default=750)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    req(args.survivor_offset_start >= 1 and args.survivor_offset_count > 0, "wave must start after consumed CUT191 survivor offset0")
    primes = [int(v) for v in args.primes.split(",") if v.strip()]
    req(primes and all(p>=2 for p in primes), "prime list empty")
    source_and_authority_preflight()
    survivors = e8.current_main_survivor_block_indices()
    start=args.survivor_offset_start; end=start+args.survivor_offset_count
    req(end <= 256, "CUT193 wave1 is bounded to survivor offsets 1..255")
    block_indices = survivors[start:end]
    req(len(block_indices)==args.survivor_offset_count and all(i!=0 for i in block_indices), "disjoint wave identity drift")
    P,blocks,g = load_picard_interface()
    solvers = {p: make_solver(P,blocks,p,args.timeout_ms) for p in primes}
    recs = [classify_block(i,P,blocks,g,solvers,primes) for i in block_indices]
    closed = [r["block_index"] for r in recs if r["closed_candidate"]]
    methods: dict[str,int] = {}
    for r in recs: methods[r["method"]] = methods.get(r["method"],0)+1
    bh=hashlib.sha256(); ch=hashlib.sha256()
    for i in block_indices: bh.update(f"{i}\n".encode())
    for i in closed: ch.update(f"{i}\n".encode())
    body={"schema":SCHEMA,"stage":"32","surface":"full178-cut","node":"CUT193","status":"WAVE1_SHARD_CANDIDATE_NEEDS_AGGREGATE_AND_HOSTILE_AUDIT","z3_version":get_version_string(),"source":{"main_parent_exact_head":"6d63d798adb50dd4efc5f0d5abc553b3dfa23060","main_parent_external_reaudit_review":5178420739,"main_state_canonical":MAIN_CANONICAL,"ex5_producer_exact_head":"fd00531181228c9f367a49eb61ddc3af6ab84ab3","ex5_producer_ci_run":34598945799,"ex5_wave_artifact_id":10263148684,"ex5_wave_artifact_digest":"sha256:df48610fbf8d6cd11640f8f3feb534256b307e6ea803688267a33cb972cfba7f"},"target":{"row_id":"g1-d008","g":1,"d":8,"e":8,"survivor_offset_range":[start,end-1],"block_indices":block_indices,"block_index_stream_sha256":bh.hexdigest(),"block_count":len(block_indices),"terminal_count":113*len(block_indices),"cut191_block0_disjoint":True,"n356_preserved_all_wave_blocks":True},"method":{"primes":primes,"per_check_timeout_ms":args.timeout_ms,"whole_block_relaxation_first":True,"parent_level_relaxation_after_hnf":True,"necessity":"every exact integral Picard64 completion must survive the source-locked HNF parent population and every finite-ring column-image relaxation; UNSAT is monotone, SAT/UNKNOWN grants no pruning credit"},"result":{"candidate_closed_block_indices":closed,"candidate_closed_block_count":len(closed),"candidate_closed_block_stream_sha256":ch.hexdigest(),"candidate_pruned_terminals":113*len(closed),"method_counts":methods,"blocks":recs},"credit":{"stage32_main_pruning_credit":False,"full178_complete":False,"theorem_credit":False,"endpoint_credit":False,"merge_authorized":False},"firewalls":{"sat_or_unknown_promoted_to_unsat":False,"cut191_double_counted":False,"n356_double_counted":False,"main_authority_mutated":False,"perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False}}
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(body,sort_keys=True,indent=2)+"\n")
    print(json.dumps({"status":body["status"],"offsets":[start,end-1],"blocks":len(block_indices),"closed":len(closed),"candidate_pruned_terminals":113*len(closed),"canonical":body["canonical_sha256_without_this_field"]},sort_keys=True))

if __name__ == "__main__":
    main()
