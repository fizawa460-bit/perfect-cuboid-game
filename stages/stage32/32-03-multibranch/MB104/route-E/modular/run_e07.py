"""E07 driver (fail-closed): runs modhecke.py for N = 1..8 and checks
 (a) the singular fixed points of G on X(8) are exactly cusps: each nontrivial g in G fixes 8 or 0 of the 24 cusps,
     the pattern is [8,8,8,0,0,0,0], and no g in G is the image of an elliptic element (no interior fixed points);
 (b) N = 1 reproduces E04 (32 twists k=8 genus 0, 96 twists k=4 genus 1);
 (c) N = 2..8: no twist has genus <= 1.
usage: python -I -O run_e07.py   (from this folder)"""
import subprocess, sys, json, os, itertools
here = os.path.dirname(os.path.abspath(__file__))
def mul8(A, B):
    a, b, c, d = A; e, f, g, h = B
    return ((a*e + b*g) % 8, (a*f + b*h) % 8, (c*e + d*g) % 8, (c*f + d*h) % 8)
def proj(A): return min(A, tuple((-x) % 8 for x in A))
SL8 = {(1, 0, 0, 1)}; fr = [(1, 0, 0, 1)]
while fr:
    nf = []
    for x in fr:
        for g in ((0, 7, 1, 0), (1, 1, 0, 1)):
            y = mul8(g, x)
            if y not in SL8: SL8.add(y); nf.append(y)
    fr = nf
G = sorted({proj(x) for x in SL8 if (x[0] % 4, x[1] % 4, x[2] % 4, x[3] % 4) in ((1, 0, 0, 1), (3, 0, 0, 3))})
# cusps of X(8): primitive vectors (x, y) mod 8 up to sign
cusps = sorted({min((x, y), ((-x) % 8, (-y) % 8)) for x in range(8) for y in range(8) if (x % 2 or y % 2)})
def act(A, v):
    a, b, c, d = A; x, y = v; w = ((a*x + b*y) % 8, (c*x + d*y) % 8); return min(w, ((-w[0]) % 8, (-w[1]) % 8))
fix = sorted(sum(1 for v in cusps if act(g, v) == v) for g in G if g != (1, 0, 0, 1))
# images of elliptic elements: conjugates of S (order 2) and S*T (order 3) in PSL2(Z/8)
def conj_class(A):
    out = set()
    for x in SL8:
        xi = (x[3], (-x[1]) % 8, (-x[2]) % 8, x[0])
        out.add(proj(mul8(mul8(x, A), xi)))
    return out
ellip = conj_class((0, 7, 1, 0)) | conj_class(mul8((0, 7, 1, 0), (1, 1, 0, 1))) | conj_class(mul8(mul8((0, 7, 1, 0), (1, 1, 0, 1)), mul8((0, 7, 1, 0), (1, 1, 0, 1))))
ok = (len(cusps) == 24 and fix == [0, 0, 0, 0, 8, 8, 8] and not (set(G) & ellip))
print("cusps:", len(cusps), " cusp fixed-point counts of G minus identity:", fix, " G meets elliptic images:", bool(set(G) & ellip))
import tempfile
tmpdir = tempfile.mkdtemp(prefix="run_e07_")  # private per run, so parallel runs do not collide
for N in range(1, 9):
    outp = os.path.join(tmpdir, f"modhecke_N{N}.json")
    out = subprocess.run([sys.executable, "-I", "-O", os.path.join(here, "modhecke.py"), str(N), outp], capture_output=True, text=True, cwd=here)
    print(out.stdout.strip())
    if out.returncode: print(out.stderr); ok = False; continue
    r = json.load(open(outp))["res"]
    low = [(k, g) for _, k, g, _ in r if g <= 1]
    # index identity mu * k = 192 n for every twist, and the full (k, genus) table
    nidx = {1: 1, 2: 2, 3: 4, 4: 4, 5: 6, 6: 8, 7: 8, 8: 8}[N]
    ok &= all(mu * k == 192 * nidx for _, k, g, mu in r)
    from collections import Counter
    TABLE = {1: {(8, 0): 32, (4, 1): 96, (2, 3): 64}, 2: {(4, 5): 64, (2, 9): 128}, 3: {(8, 3): 32, (4, 9): 96, (2, 21): 64},
             4: {(4, 9): 64, (2, 21): 128}, 5: {(8, 7): 32, (4, 17): 96, (2, 37): 64}, 6: {(4, 25): 64, (2, 49): 128},
             7: {(8, 11): 32, (4, 25): 96, (2, 53): 64}, 8: {(4, 25): 64, (2, 49): 128}}
    ok &= Counter((k, g) for _, k, g, _ in r) == Counter(TABLE[N])
    if N == 1:
        from collections import Counter
        ok &= Counter(low) == Counter({(8, 0): 32, (4, 1): 96})
    else:
        ok &= (len(low) == 0)
print("PASS" if ok else "FAIL")
if not ok: raise SystemExit(1)
