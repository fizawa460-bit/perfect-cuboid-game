"""checks13 / qfix13.py -- stricter test: moduli field inside Q (fixed also by complex conjugation).

Input: the galois13 candidates (both invariants in Q(i)).  Complex conjugation sends p to pbar(z) = conj(p(conj z)),
whose critical values are conj(B) = B with I and -I exchanged.  p is fixed by Gal(Qbar/Q) iff it is fixed by
Gal(Qbar/Q(i)) and pbar = p o m for a Moebius m.
Degree 4: every map is in the list, test pbar ~ p directly.
Degree 5: only orbit representatives are stored.  For q = h o p (h one of the 24 rotations), qbar = hbar o pbar, so q is
fixed iff pbar = hbar^{-1} h o p o m for some m.  Distinct maps h o p are counted up to the symmetry group of p.
Usage: python -I qfix13.py G4.jsonl G5.jsonl
"""
import sys, os, json, itertools, random
HERE = os.path.dirname(os.path.abspath(__file__))
F02 = os.path.normpath(os.path.join(HERE, "..", "..", "f02")); sys.path.insert(0, F02); sys.path.insert(0, HERE)
import mpmath as mp
import build_maps as bm
import sym13 as S
mp.mp.dps = 50


def crit(n, P, Q):
    W = [mp.mpc(0)] * (2 * n)
    for i in range(n + 1):
        for j in range(n + 1):
            if i + j - 1 >= 0: W[i + j - 1] += (i - j) * P[i] * Q[j]
    while abs(W[-1]) < mp.mpf(10) ** -25: W.pop()
    assert len(W) - 1 == 2 * n - 2
    return mp.polyroots(list(reversed(W)), maxsteps=300, extraprec=200)


def mobmul(A, B):
    a, b, c, d = A; e, f, g, h = B
    return (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)


def equiv(n, P, Q, T, U, H):
    """is there m with p o m = H o t ?  (p = P/Q, t = T/U)"""
    cp = crit(n, P, Q); ct = crit(n, T, U)
    lp = [S.lab(S.pval(P, Q, c)) for c in cp]; lt = [S.lab(S.hval(H, S.pval(T, U, c))) for c in ct]
    rnd = random.Random(2); test = [mp.mpc(rnd.uniform(-1, 1), rnd.uniform(-1, 1)) for _ in range(3)]
    for tr in itertools.permutations(range(len(cp)), 3):
        if any(lp[tr[k]] != lt[k] for k in range(3)): continue
        M = S.mob3(ct[:3], [cp[k] for k in tr])         # m sends critical points of t to those of p
        ok = True
        for z in test:
            u = S.pval(P, Q, S.ap(M, z)); v = S.hval(H, S.pval(T, U, z))
            if u == mp.inf or v == mp.inf or abs(u - v) > mp.mpf(10) ** -25 * (1 + abs(v)): ok = False; break
        if ok: return True
    return False


def gen(n, P):
    sg = mp.mpf("0.3719")
    return S.G13.subst(n, P, mp.mpc(1), mp.mpc(0), mp.mpc(sg), mp.mpc(1))


def main():
    d4 = json.load(open(os.path.join(F02, "maps4.json")))
    d5 = [json.loads(l) for l in open(os.path.join(F02, "maps5reps.state.jsonl"))]
    ident = (mp.mpc(1), mp.mpc(0), mp.mpc(0), mp.mpc(1))
    for n, gf, data in ((4, sys.argv[1], d4), (5, sys.argv[2], d5)):
        cand = [r for r in map(json.loads, open(gf)) if r["I1_deg"] == 1 and r["I2_deg"] == 1]
        total_fixed = 0; total_maps = 0
        for r in cand:
            rec = data[r["idx"]]
            P = gen(n, [bm.parse_c(x) for x in rec["P"]]); Q = gen(n, [bm.parse_c(x) for x in rec["Q"]])
            # conjugate of the generically moved map is the generic move (real parameter) of the conjugate
            Pb = [mp.conj(c) for c in P]; Qb = [mp.conj(c) for c in Q]
            if n == 4:
                f = equiv(n, P, Q, Pb, Qb, ident)
                total_fixed += f; total_maps += 1
                print(n, r["idx"], r["datum"], "Q-fixed" if f else "not", flush=True)
            else:
                # classes of h o p: h1 ~ h2 iff h2^{-1} h1 o p ~ p
                hs = S.ROTS; classes = []
                for i, (perm, H) in enumerate(hs):
                    for cl in classes:
                        H2 = hs[cl[0]][1]
                        H2i = (H2[3], -H2[1], -H2[2], H2[0])
                        if equiv(n, P, Q, P, Q, mobmul(H2i, H)): cl.append(i); break
                    else: classes.append([i])
                fixed = 0
                for cl in classes:
                    H = hs[cl[0]][1]
                    Hb = tuple(mp.conj(x) for x in H); Hbi = (Hb[3], -Hb[1], -Hb[2], Hb[0])
                    # q = H o p fixed  iff  pbar ~ Hbar^{-1} H o p, i.e. exists m: p o m' ... test  H o p o m = Hbar o pbar
                    G = mobmul((H[3], -H[1], -H[2], H[0]), Hb)          # H^{-1} Hbar
                    if equiv(n, P, Q, Pb, Qb, G): fixed += 1
                total_fixed += fixed; total_maps += len(classes)
                print(n, r["idx"], r["datum"], "maps h o p:", len(classes), "Q-fixed among them:", fixed, flush=True)
        print("degree", n, ": Q(i)-candidates expand to", total_maps, "maps;", total_fixed, "fixed by complex conjugation too",
              flush=True)


if __name__ == "__main__":
    main()
