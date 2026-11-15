"""checks13 / bands13.py -- bands12 (cone-free bands, Lemma G) on degree 5, resumable and parallel.

Uses the analysis of checks12/bands12.py unchanged (its definitions are executed, not its main part).
Maps: all degree-5 maps whose branch type is the representative of its octahedral orbit of types
(the 7 types 002222, 011222, 020222, 021122, 021212, 111122, 111212; 612 maps).
For a rotation h of B, the triangulation tau of h o p is the same as that of p. h permutes the octahedron's
faces and vertices and keeps antipodal pairs, so all band numbers are invariant. Every orbit of maps meets
these types, so the distribution over the 612 maps is the distribution up to rotation.
Option --also-degree4: the same run on all 680 degree-4 maps (bands12 used every 4th map).
usage (from the repository root): python3 -I .../wall/checks13/bands13.py [--workers 10] [--also-degree4]
"""
import sys, os, io, contextlib, json, argparse, time
sys.dont_write_bytecode = True
from collections import Counter
from concurrent.futures import ProcessPoolExecutor, as_completed
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_k] = "1"
HERE = os.path.dirname(os.path.abspath(__file__))
B12 = os.path.join(HERE, "..", "checks12", "bands12.py")
F02 = os.path.join(HERE, "..", "..", "f02")
REPS5 = {"002222", "011222", "020222", "021122", "021212", "111122", "111212"}


def defs():
    src = open(B12, encoding="utf-8").read().split("\nstride = ")[0]
    G = {"__name__": "bands12_defs", "__file__": B12}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(src, "bands12_defs", "exec"), G)
    return G


_G = {}


def items(deg):
    G = _G.setdefault("G", defs())
    data = json.load(open(os.path.join(F02, "maps%d.json" % deg)))
    C9 = G["C9"]; mp = C9.mp
    cv = lambda s: mp.mpc(*[mp.mpf(x) for x in C9._split(s)])
    keep = [(i, C9.Map([cv(c) for c in d["P"]], [cv(c) for c in d["Q"]], "deg%d_%04d" % (deg, i)))
            for i, d in enumerate(data) if deg != 5 or d["datum"] in REPS5]
    return keep, data


def job(args):
    deg, ids, out = args
    G = _G.setdefault("G", defs())
    if ("M", deg) not in _G: _G[("M", deg)] = dict(items(deg)[0])
    M = _G[("M", deg)]
    rows = []
    for i in ids:
        with contextlib.redirect_stdout(io.StringIO()):
            r = G["analyse"](M[i].P, M[i].Q, M[i].n)
        r["index"] = i; rows.append(r)
    tmp = out + ".tmp"
    with open(tmp, "w") as f: json.dump(rows, f)
    os.replace(tmp, out)


def summary(name, rows):
    g = sum(r["good"] for r in rows); lg = sum(r["comp"] == r["compG"] for r in rows)
    s = dict(name=name, maps=len(rows), checks_ok=g, lemmaG=lg,
             comp=dict(sorted(Counter(r["comp"] for r in rows).items())),
             T0_share_max=max(r["T0"] / (8.0 * r["n"]) for r in rows),
             largest_T0_region=dict(sorted(Counter(r["largest"] for r in rows).items())),
             depth=dict(sorted(Counter(r["depth"] for r in rows).items())),
             band_width=dict(sorted(Counter(r["cross"] for r in rows if r["comp"] >= 2).items())))
    print(json.dumps(s), flush=True)
    return s, g == len(rows) and lg == len(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=10)
    ap.add_argument("--chunk", type=int, default=8)
    ap.add_argument("--also-degree4", action="store_true")
    ap.add_argument("--out", default=os.path.join(HERE, "bandchunks"))
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    degs = [5] + ([4] if a.also_degree4 else [])
    res, ok = [], True
    for deg in degs:
        keep, data = items(deg)
        ids = [i for i, _ in keep]
        chunks = [ids[k:k + a.chunk] for k in range(0, len(ids), a.chunk)]
        paths = [os.path.join(a.out, "b%d_%04d.json" % (deg, c)) for c in range(len(chunks))]
        todo = [(deg, ch, p) for ch, p in zip(chunks, paths) if not os.path.exists(p)]
        print("degree %d: %d maps, %d chunks, to do %d" % (deg, len(ids), len(chunks), len(todo)), flush=True)
        t0 = time.time(); done = len(chunks) - len(todo)
        if todo:
            with ProcessPoolExecutor(max_workers=a.workers) as ex:
                for fut in as_completed([ex.submit(job, t) for t in todo]):
                    fut.result(); done += 1
                    if done % 10 == 0: print("  %d/%d %.0fs" % (done, len(chunks), time.time() - t0), flush=True)
        rows = []
        for p in paths:
            with open(p) as f: rows += json.load(f)
        for r in rows: r["datum"] = data[r["index"]]["datum"]
        name = "degree 5 (7 orbit-representative types)" if deg == 5 else "degree 4 (all maps)"
        s, k = summary(name, rows); ok &= k
        s["by_type"] = {t: summary("  type " + t, [r for r in rows if r["datum"] == t])[0]
                        for t in sorted({r["datum"] for r in rows})} if deg == 5 else None
        res.append(s)
    json.dump(res, open(os.path.join(HERE, "bands13.json"), "w"), indent=1)
    print("PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()
