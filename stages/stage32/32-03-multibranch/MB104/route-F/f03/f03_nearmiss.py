"""F-03 follow-up: near misses for the recorded T (c >= 4) of one f03 run.
For each recorded T (rebuilt exactly from its first 3 coincident pairs), every point of O(p1) is mapped and its
chordal distance to every point of O(q) is computed; the script reports how many recorded coincidences are
reproduced (< 1e-40) and the smallest distance among the other pairs (a value < 1e-15 would be a missed
coincidence or a true near miss, i.e. c could be larger than recorded).
usage: F03_DPS=90 python -I f03_nearmiss.py tagfile.jsonl steps c1 c2 [workers]
"""
import json, os, sys
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import f03_isogeny_pairs as F
mp = F.mp


def init(steps, c1, c2): F.winit(steps, c1, c2); F.W.pop("H")


def check(co):
    X1 = [p for p, _ in F.W["O1"]]; X2 = [p for p, _ in F.W["O2"]]
    T = F.mob3([X1[a] for a, _ in co[:3]], [X2[b] for _, b in co[:3]])
    hit = 0; far = mp.mpf(1); maxco = mp.mpf(0)
    s = set(map(tuple, co))
    for a, x in enumerate(X1):
        y = F.mob(T, x)
        for b, w in enumerate(X2):
            d = F.chord(y, w)
            if (a, b) in s:
                hit += d < F.EPS; maxco = max(maxco, d)
            elif d < far: far = d
    return hit == len(co), float(maxco), float(far)


if __name__ == "__main__":
    path, steps, c1, c2 = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
    workers = int(sys.argv[5]) if len(sys.argv) > 5 else 8
    T = {}
    for line in open(path):
        for rec in json.loads(line)["recs"]: T[tuple(map(tuple, rec["co"]))] = rec["co"]
    with Pool(workers, initializer=init, initargs=(steps, c1, c2)) as pool:
        res = pool.map(check, list(T.values()), chunksize=200)
    print(json.dumps(dict(file=os.path.basename(path), dps=mp.mp.dps, T=len(res),
                          all_coincidences_reproduced=all(r[0] for r in res),
                          max_coincident_chordal=max(r[1] for r in res),
                          min_other_chordal=min(r[2] for r in res),
                          T_with_other_below_1e_15=sum(1 for r in res if r[2] < 1e-15))))
