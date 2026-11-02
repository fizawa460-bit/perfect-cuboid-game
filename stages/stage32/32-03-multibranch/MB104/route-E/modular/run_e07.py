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
print("cusps:", len(cusps), " cusp fixed-point counts of G\{1}:", fix, " G meets elliptic images:", bool(set(G) & ellip))
for N in range(1, 9):
    out = subprocess.run([sys.executable, "-I", os.path.join(here, "modhecke.py"), str(N)], capture_output=True, text=True, cwd=here)
    print(out.stdout.strip())
    if out.returncode: print(out.stderr); ok = False; continue
    import tempfile
    r = json.load(open(os.path.join(tempfile.gettempdir(), f"modhecke_N{N}.json")))["res"]
    low = [(k, g) for _, k, g, _ in r if g <= 1]
    if N == 1:
        from collections import Counter
        ok &= Counter(low) == Counter({(8, 0): 32, (4, 1): 96})
    else:
        ok &= (len(low) == 0)
print("PASS" if ok else "FAIL")
if not ok: raise SystemExit(1)
