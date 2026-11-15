"""checks13 / census13.py -- census9 (problem-window census) extended to bidegrees (a, 5), resumable and parallel.

Same search and analysis as checks9/census9.py (imported unchanged). Two changes:
 1. Octahedral reduction of the first map p. For a rotation h of B, (p, q o T) and (h o p, h o q o T) give the same
    record type (m1, m2, h, |Omega|, delta, genus, bdeg): h permutes the labels a/b/e on both maps in the same way,
    so label-matched stays label-matched. The second list Qs (all maps of degree b) is closed under q -> h o q.
    So p only needs to run over maps whose branch type is the chosen representative of its rotation orbit of types.
    Every rotation orbit of maps meets these types. For degree 1 and 2 (generated maps without a datum) all maps are kept.
    Counts of records are therefore counts for the representative p only. They are NOT comparable with census9
    counts; the problem-window count (0 or not) is.
 2. Chunks of p are run in a process pool. Every finished chunk is saved to OUT/chunk_a_b_XXXX.json, and existing
    chunks are skipped on restart.
usage (from the repository root): python3 -I .../wall/checks13/census13.py --bideg 4,5 [--workers 10] [--chunk 4]
"""
import sys, os, json, argparse, time, itertools, importlib.util
sys.dont_write_bytecode = True
from collections import Counter
from concurrent.futures import ProcessPoolExecutor, as_completed

HERE = os.path.dirname(os.path.abspath(__file__))
F02 = os.path.join(HERE, "..", "..", "f02")
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_k] = "1"


def load_c9():
    spec = importlib.util.spec_from_file_location("census9", os.path.join(HERE, "..", "checks9", "census9.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


C9 = load_c9()


def rep_types(types):
    """one representative branch type (min string) per rotation orbit; digit order = BV order of census9"""
    reps = set()
    for t in types:
        orb = []
        for r in C9.ROT:                      # r[i] = index of the image of BV[i]
            u = [0] * 6
            for i in range(6): u[r[i]] = int(t[i])
            orb.append("".join(map(str, u)))
        reps.add(min(orb))
    return reps


def p_list(a):
    maps = C9.load_maps(a, F02)
    if a <= 2: return maps, None
    data = json.load(open(os.path.join(F02, "maps%d.json" % a)))
    types = [m["datum"] for m in data]
    reps = rep_types(set(types))
    keep = [m for m, t in zip(maps, types) if t in reps]
    return keep, sorted(reps)


_Q = {}


def run_chunk(args):
    a, b, idx, out, first, keep = args
    if b not in _Q: _Q[b] = C9.load_maps(b, F02)
    if ("P", a) not in _Q: _Q[("P", a)] = p_list(a)[0]
    P = _Q[("P", a)]
    sub = [P[i] for i in idx]
    t0 = time.time()
    recs = C9.search(sub, _Q[b], a, b, first, False, keep)
    rows = [{k: (v if k not in ("M", "p", "q") else None) for k, v in r.items()} for r in recs]
    for row, r in zip(rows, recs):
        row["p"] = r["p"].name; row["q"] = r["q"].name; row.pop("M")
    tmp = out + ".tmp"
    with open(tmp, "w") as f: json.dump(dict(idx=idx, seconds=time.time() - t0, recs=rows), f)
    os.replace(tmp, out)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bideg", required=True)
    ap.add_argument("--workers", type=int, default=10)
    ap.add_argument("--chunk", type=int, default=4)
    ap.add_argument("--first", type=int, default=6)
    ap.add_argument("--keep", type=int, default=3)
    ap.add_argument("--out", default=os.path.join(HERE, "chunks"))
    args = ap.parse_args()
    a, b = map(int, args.bideg.split(","))
    os.makedirs(args.out, exist_ok=True)
    P, reps = p_list(a)
    idx = list(range(len(P)))
    chunks = [idx[i:i + args.chunk] for i in range(0, len(idx), args.chunk)]
    jobs = []
    for c, ids in enumerate(chunks):
        out = os.path.join(args.out, "chunk_%d_%d_%04d.json" % (a, b, c))
        if not os.path.exists(out): jobs.append((a, b, ids, out, args.first, args.keep))
    print("bidegree %d,%d: p maps %d (rep types %s), chunks %d, to do %d" % (a, b, len(P), reps, len(chunks), len(jobs)), flush=True)
    t0 = time.time(); done = len(chunks) - len(jobs)
    if jobs:
        with ProcessPoolExecutor(max_workers=args.workers) as ex:
            for fut in as_completed([ex.submit(run_chunk, j) for j in jobs]):
                fut.result(); done += 1
                if done % 5 == 0 or done == len(chunks):
                    print("  chunks %d/%d  %.0fs" % (done, len(chunks), time.time() - t0), flush=True)
    recs = []
    for c in range(len(chunks)):
        with open(os.path.join(args.out, "chunk_%d_%d_%04d.json" % (a, b, c))) as f: recs += json.load(f)["recs"]
    cnt = Counter((r["m1"], r["m2"], r["h"], r["omega"], r["delta"], r["genus"], r["bdeg"]) for r in recs)
    window = [r for r in recs if (r["m1"], r["m2"]) != (0, 0) and r["omega"] <= 4]
    mixed = [r for r in recs if (r["m1"], r["m2"]) != (0, 0)]
    u = [r["thmU"] for r in recs if r["thmU"] is not None]
    bez = all(r["NH"] <= a + b for r in mixed)
    comp = all(r["m1"] % r["bdeg"] == 0 and r["m2"] % r["bdeg"] == 0 for r in recs)
    ok = bez and all(u) and comp
    mixed_omega = sorted({r["omega"] for r in mixed})
    res = dict(bidegree=[a, b], p_maps=len(P), p_rep_types=reps, q_maps=len(C9.load_maps(b, F02)),
               search=dict(first=args.first, keep=args.keep), distinct_T=len(recs),
               key="(m1, m2, h, |Omega|, delta, genus, degree onto image)",
               counts=sorted([list(k) + [v] for k, v in cnt.items()]),
               problem_window_mixed=len(window), window_records=[{k: r[k] for k in ("p", "q", "m1", "m2", "h", "omega")} for r in window],
               mixed_records_min_omega=(mixed_omega[0] if mixed_omega else None),
               typeU_records=len(u), typeU_all_octahedral=all(u),
               bezout_NH_le_a_plus_b_on_mixed=bez, composite_degree_divides_m1_m2=comp,
               max_NH_mixed=max([r["NH"] for r in mixed], default=None),
               crit_overlaps_mixed=dict(crit_crit=sum(r["cc"] for r in mixed), crit_O=sum(r["co"] for r in mixed),
                                        O_crit=sum(r["oc"] for r in mixed)),
               worst_coincidence=max([r["worst"] for r in recs], default=0.0),
               smallest_gap=min([r["gap"] for r in recs], default=1.0), seconds_this_run=round(time.time() - t0, 1))
    print(json.dumps(res), flush=True)
    with open(os.path.join(HERE, "census13_%d_%d.json" % (a, b)), "w") as f: json.dump(res, f, indent=1)
    print("PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()
