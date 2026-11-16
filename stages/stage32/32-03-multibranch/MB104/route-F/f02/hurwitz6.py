"""Degree-6 slack-0 Hurwitz counts over the 6 points of B (local degrees 1 or 2).

Cycle types 2^k 1^(6-2k), k = n_y in {0,1,2,3}, sum n_y = 10.  The tuple count of
transitive (g_1..g_6), g_j in class k_j, product 1, depends only on the multiset of
k_j (braid invariance), so it is computed once per multiset by a DP over
(prefix product, orbit partition).  Isomorphism classes by Burnside: classes =
(1/FACT) sum_s #{transitive tuples centralised by s}; computed per conjugacy class of s.
Output hurwitz6.json: {datum: [classes, tuples, {"mass_denFACT": tuples}]} for all 6-letter data,
plus "_multisets" with the per-multiset Burnside terms.
"""
import itertools, json, os, sys
from collections import Counter, defaultdict

n = int(sys.argv[1]) if len(sys.argv) > 1 else 6
Sn = list(itertools.permutations(range(n)))
FACT = len(Sn)


def mul(p, q): return tuple(p[q[i]] for i in range(n))


def inv(p):
    r = [0] * n
    for i, x in enumerate(p): r[x] = i
    return tuple(r)


def cyc(p):
    seen = set(); t = []
    for i in range(n):
        if i in seen: continue
        L = 0; j = i
        while j not in seen: seen.add(j); j = p[j]; L += 1
        t.append(L)
    return tuple(sorted(t))


def k_of(p):
    t = cyc(p)
    return sum(1 for L in t if L == 2) if max(t) <= 2 else None


def join(part, p):
    """part: tuple root label per point (canonical: min of block). merge cycles of p."""
    lab = list(part)
    for i in range(n):
        a, b = lab[i], lab[p[i]]
        if a != b:
            lo, hi = min(a, b), max(a, b)
            lab = [lo if x == hi else x for x in lab]
    return tuple(lab)


def count(ks, allowed):
    """transitive tuples with g_j in class ks[j] (restricted to `allowed`), product 1."""
    CL = {k: [p for p in allowed if k_of(p) == k] for k in set(ks)}
    e = tuple(range(n))
    st = {(e, e): 1}
    for k in ks[:-1]:
        nx = defaultdict(int)
        for (pr, part), c in st.items():
            for g in CL[k]:
                nx[(mul(pr, g), join(part, g))] += c
        st = nx
    last = set(CL[ks[-1]]); tot = 0
    for (pr, part), c in st.items():
        g = inv(pr)
        if g in last and len(set(join(part, g))) == 1: tot += c
    return tot


def main():
    reps = {}
    for p in Sn: reps.setdefault(cyc(p), p)
    csize = Counter(cyc(p) for p in Sn)
    multis = [m for m in itertools.combinations_with_replacement(range(n // 2, -1, -1), 6) if sum(m) == 2 * n - 2]
    res = {}
    for m in multis:
        ks = sorted(m, reverse=True)  # put big classes first (fewer DP states early? harmless)
        terms = {}
        for ct, s in reps.items():
            cent = [g for g in Sn if mul(g, s) == mul(s, g)]
            terms[str(ct)] = count(ks, cent)
        tuples = terms[str((1,) * n)]
        burn = sum(csize[tuple(eval(ct))] * v for ct, v in terms.items())
        assert burn % FACT == 0, (m, burn)
        res["".join(map(str, m))] = {"classes": burn // FACT, "tuples": tuples, "mass": tuples / FACT, "terms": terms}
        print(m, res["".join(map(str, m))]["classes"], tuples, flush=True)
    out = {}
    for ns in itertools.product(range(n // 2 + 1), repeat=6):
        if sum(ns) != 2 * n - 2: continue
        key = "".join(map(str, sorted(ns, reverse=True)))
        r = res[key]
        out["".join(map(str, ns))] = [r["classes"], r["tuples"], {"mass": r["mass"]}]
    out["_multisets"] = res
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"hurwitz{n}.check.json" if n != 6 else "hurwitz6.json"), "w") as f:
        json.dump(out, f, indent=0)
    data = [k for k in out if not k.startswith("_")]
    print("data", len(data), "classes", sum(out[k][0] for k in data))


if __name__ == "__main__":
    main()
