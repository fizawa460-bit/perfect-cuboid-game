"""32R-72 v2 candidate members.  For every finished e_<i>_<t>.out with CANDIDATES, one member job per candidate point
q = (s0 : u : v) of D' (multiplicity >= THR): member G_q = s0 F1 + u F2 + v F3 of the same random basis as in the net
job (same seed, same code), residual after removing the fixed part D, then the fast genus tail (v2).
Candidate points of degree k >= 2 are taken over F_p(ww), minpoly of degree k (conjugate members have equal genus).
usage (from stoll/): python n16/mkcand.py [maxdeg] -> n16/m_<i>_<t>_<k>.sing, n16/mjobs.txt"""
import json, re, sys, glob, os
NL = chr(10); P = 10009
MAXDEG = int(sys.argv[1]) if len(sys.argv) > 1 else 99
plan = json.load(open("n16/plan.json"))
FAST = open("gfast/tail_fast_v2.sing").read()
TAIL = open("n16/net_tail_c.sing").read().split(NL)
BASIS = NL.join(l for l in TAIL if l.startswith(("ideal SS", "ideal NFL", "system(\"random\"", "int ii;", "list FL;", "ideal FI;")))


def polyterms(s):
    """parse a Singular poly in s0,u,v with integer coefficients -> dict {(e_s0, e_u, e_v): c mod p}"""
    s = s.replace(" ", ""); out = {}
    for sg, body in re.findall(r"([+-]?)([^+-]+)", s):
        c = 1; e = [0, 0, 0]
        for f in body.split("*"):
            m = re.fullmatch(r"(s0|u|v)(?:\^(\d+))?", f)
            if m: e[["s0", "u", "v"].index(m.group(1))] += int(m.group(2) or 1)
            else: c *= int(f)
        if sg == "-": c = -c
        out[tuple(e)] = (out.get(tuple(e), 0) + c) % P
    return out


def kernel(rows):
    """1-dim kernel of a 2x3 matrix mod p"""
    import itertools
    a, b = rows
    k = [(a[1] * b[2] - a[2] * b[1]) % P, (a[2] * b[0] - a[0] * b[2]) % P, (a[0] * b[1] - a[1] * b[0]) % P]
    assert any(k); return k


def cands(txt):
    blk = txt.split("CANDIDATES", 1)[1]
    cur = None
    for line in blk.split(NL):
        m = re.match(r"\s*cand (\d+)\s+deg (\d+) :\s*(.*)", line)
        if m:
            if cur: yield cur
            cur = [int(m.group(1)), int(m.group(2)), []]; line = m.group(3)
        if cur is None: continue
        g = re.match(r"\s*_\[(\d+)\]=(.*)", line)
        if g: cur[2].append(g.group(2).strip())
        elif line.strip() and not line.startswith("time"): cur[2][-1] += line.strip()
    if cur: yield cur


def cands5(txt):
    for cn, dg, gens in cands(txt):
        yield cn, dg, gens[0], (gens[1] if len(gens) > 1 else ""), len(gens) != 2


jobs = []; skipped = []; bad = []; BADG = []
SHAPE = {}
if os.path.exists("n16/shape.txt"):
    for line in open("n16/shape.txt"):
        if line.startswith("SHAPE "):
            _, key, ch, fu, gs = line.strip().split(" ", 4)
            SHAPE[key] = (ch, fu, gs.replace(" ", ""))
for f in sorted(glob.glob("n16/e_*_*.out")) + sorted(glob.glob("n16/le_*_*.out")):
    txt = open(f).read()
    if "CANDIDATES" not in txt or "NO-CANDIDATES" in txt or "D-RECONSTRUCTED" not in txt: continue
    LE, i, t = re.match(r"n16/(l?)e_(\d+)_(\d+)\.out", f.replace(os.sep, "/")).groups()
    src = open(f"n16/e_{i}_{t}.sing").read(); k = src.index("int HH = ")
    hdr = src[k:src.index(NL, k)]
    pre = src[:k] + hdr + NL
    ti = int(t); ti = 2 if (ti >= 2 and ti == plan[i].get("third")) else ti
    D = plan[i]["decs"][ti][1]
    cids = sorted(int(x) for x in D if int(x) <= 92)
    dc = ("intersect(" + ",".join(f"G{x}" for x in cids) + ")") if len(cids) > 1 else (f"G{cids[0]}" if cids else "ideal(1)")
    HH = int(re.search(r"int HH = (\d+)", hdr).group(1))
    if HH != 3: continue
    for cn, dg, gens in cands(txt):
        key = f"{LE}{i}_{t}_{cn}"
        g1, g2 = gens[0], (gens[1] if len(gens) > 1 else "")
        if key in SHAPE:
            ch, fu, gs = SHAPE[key]
            mp = fu.replace("u", "ww"); gw = gs.replace("u", "ww")
            coef = {"v": [f"({gw})", "ww", "1"], "u": [f"({gw})", "1", "ww"], "s0": [None]}[ch]
            if coef[0] is None: bad.append((f, cn, "chart s0")); continue
            if dg > MAXDEG: skipped.append((f, cn, dg)); continue
            body_coef = coef
        elif len(gens) != 2:
            bad.append((f, cn, "3 generators")); BADG.append((key, dg, gens)); continue
        else:
            body_coef = None
        if dg > MAXDEG: skipped.append((f, cn, dg)); continue
        if body_coef is not None:
            coef = body_coef
        elif dg == 1:
            p1, p2 = polyterms(g1), polyterms(g2)
            rows = [[p.get((1, 0, 0), 0), p.get((0, 1, 0), 0), p.get((0, 0, 1), 0)] for p in (p1, p2)]
            if any(sum(e) != 1 for p in (p1, p2) for e in p): bad.append((f, cn, "nonlinear")); continue
            s0, u, v = kernel(rows); coef = [str(s0), str(u), str(v)]; mp = None
        else:
            p1, p2 = polyterms(g1), polyterms(g2)
            # shape: _[1] = f(u, v) homogeneous of degree dg (no s0), _[2] = s0 + a u + b v; chart v = 1, u = ww
            if any(e[0] for e in p1) or any(sum(e) != dg for e in p1) or p1.get((0, dg, 0), 0) == 0:
                bad.append((f, cn, "shape1")); BADG.append((key, dg, gens)); continue
            if p2.get((1, 0, 0), 0) != 1 or any(sum(e) != 1 for e in p2): bad.append((f, cn, "shape2")); BADG.append((key, dg, gens)); continue
            a, b = p2.get((0, 1, 0), 0), p2.get((0, 0, 1), 0)
            mp = "+".join(f"({c})*ww^{e[1]}" for e, c in p1.items())
            coef = [f"(-({a})*ww-({b}))", "ww", "1"]
        body = pre + BASIS + NL + f"ideal Dc = std({dc});" + NL
        body += f"poly NN = {coef[0]} * FL[1] + {coef[1]} * FL[2] + {coef[2]} * FL[3];" + NL
        body += 'ideal B = std(S + ideal(NN)); def LL = sat(B, Dc); ideal Bp; if (typeof(LL) == "list") { Bp = std(LL[1]); } else { Bp = std(LL); } kill LL;' + NL
        body += f'"net candidate {cn} degree {dg}; residual dim", dim(Bp), " degree", mult(Bp), " expected 16";' + NL
        body += 'if (mult(Bp) < 16) { "MEMBER-REDUCIBLE (contains a D-curve)"; quit; }' + NL
        body += 'if (dim(Bp) != 2) { "MEMBER-NOT-CURVE"; quit; }' + NL + FAST
        if mp:
            body = re.sub(r"ring (\w+) = 10009,(\([^)]*\)),dp;", lambda mm: f"ring {mm.group(1)} = (10009,ww),{mm.group(2)},dp; minpoly = {mp};", body)
        nm = f"m{LE}_{i}_{t}_{cn}"; open(f"n16/{nm}.sing", "w", newline=NL).write(body); jobs.append((dg, nm))
jobs.sort()
open("n16/mjobs.txt", "w", newline=NL).write(NL.join(n for _, n in jobs) + NL)
from collections import Counter
print("jobs", len(jobs), sorted(Counter(d for d, _ in jobs).items()))
print("skipped (degree >", MAXDEG, ")", len(skipped), sorted(Counter(d for *_, d in skipped).items()))
print("bad", len(bad), bad[:10])
# pre-pass for the remaining candidates: chart v = 1 (else u = 1), lex basis {s0 - g(u), f(u)} (shape position)
sp = ['LIB "primdec.lib";', 'ring Q = 10009,(s0,u,v),dp;', 'ring L = 10009,(s0,u),lp;', 'setring Q; ideal P; ideal P1; int ok;']
for key, dg, gens in BADG:
    sp.append(f'setring Q; P = {",".join(gens)}; P = std(P);')
    sp.append('if (reduce(v, std(radical(P))) != 0) { setring L; ideal PL = std(imap(Q, P) + ideal(0)); kill PL; setring Q; P1 = subst(P, v, 1); string ch = "v"; }')
    sp.append('else { P1 = subst(P, u, 1); P1 = subst(P1, v, u); string ch = "u"; }')
    sp.append(f'setring L; ideal PL = std(imap(Q, P1)); if (size(PL) == 2 && deg(PL[1]) == {dg} && PL[2] - s0 == reduce(PL[2] - s0, ideal(s0)) && leadmonom(PL[2]) == s0) {{ "SHAPE {key}", ch, string(PL[1]), string(s0 - PL[2]); }} else {{ "NOSHAPE {key}", PL; }} kill PL; kill ch;')
sp.append("quit;")
open("n16/shape.sing", "w", newline=NL).write(NL.join(sp) + NL)
print("shape pre-pass candidates", len(BADG))
