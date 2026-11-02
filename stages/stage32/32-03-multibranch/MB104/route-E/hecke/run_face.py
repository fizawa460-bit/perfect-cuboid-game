"""Run the equality-face classification over the Hecke list and all twists."""
import sys, json
from hecke import *
def genus_from_action(pts_x, pts_y):
    N = len(pts_x); pxy = [pts_x[pts_y[t]] for t in range(N)]
    def ncyc(p):
        seen = [False]*N; c = 0
        for t in range(N):
            if not seen[t]:
                c += 1; u = t
                while not seen[u]: seen[u] = True; u = p[u]
        return c
    two_g_minus_2 = -2*N + (N - ncyc(pts_x)) + (N - ncyc(pts_y)) + (N - ncyc(pxy))
    if two_g_minus_2 % 2: raise SystemExit('FAIL: odd Euler characteristic')
    return two_g_minus_2 // 2 + 1, N
def cosets_of(S):
    lab = {}; out = []
    for c in range(NG):
        k = frozenset(gmul(c, s) for s in S)
        if k not in lab: lab[k] = len(out); out.append(k)
    return lab, out
def orbit_action(S, F, Ia, Xi, Yi):
    lab, cos = cosets_of(S)
    def cl(c): return lab[frozenset(gmul(c, s) for s in S)]
    rep = [min(k) for k in cos]
    start = (cl(0), Ia); idx = {start: 0}; pts = [start]; px = {}; py = {}; i = 0
    while i < len(pts):
        c, I = pts[i]
        for P, e, gi in ((px, EX, Xi), (py, EY, Yi)):
            nc = cl(gmul(e, rep[c])); nI = ideal_times(F, I, gi) if F else None
            k = (nc, nI)
            if k not in idx: idx[k] = len(pts); pts.append(k)
            P[i] = idx[k]
        i += 1
    n = len(pts)
    return [px[t] for t in range(n)], [py[t] for t in range(n)]
PRIMES = [("7a", 7, (3, 1)), ("7b", 7, (3, -1)), ("9", 3, None), ("17a", 17, (5, 2)), ("17b", 17, (5, -2)),
          ("23a", 23, (5, 1)), ("23b", 23, (5, -1)), ("25", 5, None), ("31a", 31, (7, 3)), ("31b", 31, (7, -3)),
          ("41a", 41, (7, 2)), ("41b", 41, (7, -2))]
def run_prime(name, p, gen):
    if gen is None: F = Fq(p); pi = (Fr(p), Fr(0))
    else:
        a0, b0 = gen; pi = (Fr(a0), Fr(b0))
        s = (-a0 * pow(b0, -1, p)) % p          # a0 + b0*sqrt2 = 0 mod p  ->  sqrt2 = -a0/b0
        if (s * s - 2) % p: raise SystemExit('FAIL: sqrt2 mod p')
        F = Fq(p, s)
    a = find_a(pi)
    if a is None: raise SystemExit('FAIL: no element of norm p for ' + name)
    abar = qred(F, a); Ia = left_ideal(F, abar)
    if len(Ia) != 2: raise SystemExit('FAIL: ideal dimension')
    Xi = qred(F, qinv(X)); Yi = qred(F, qinv(Y))
    phi = phi_table(a)
    if not check_phi_lift_independent(a, GAM): raise SystemExit("FAIL: phi depends on the lift (" + name + ")")
    if sorted(phi) != list(range(NG)): raise SystemExit('FAIL: phi not a bijection')
    return F, a, Ia, Xi, Yi, phi
gU, g0U, nG, nG0 = check_G_unique()
print("G unique among normal involution subgroups of order 8:", gU, "(candidates", nG, ");  G0 unique free subgroup of order 4:", g0U, "(candidates", nG0, ")")
if not (gU and g0U): raise SystemExit("FAIL: G/G0 not uniquely determined")
GAM = gamma_elements()
print("sample nontrivial Gamma elements for lift checks:", len(GAM))
if len(GAM) < 3: raise SystemExit("FAIL: could not sample Gamma elements")
results = []
def record(name, n, sigma, S, g, N):
    e = len([s for s in S if s in G0]); results.append(dict(prime=name, n=n, sigma=sigma, S=sorted(S), S_size=len(S), e=e, genus=g, points=N))
# n = 1: graphs of automorphisms
for sigma in range(NG):
    S = [g for g in G if conj(g, sigma) == g]
    px, py = orbit_action(S, None, None, None, None)
    g, N = genus_from_action(px, py); record("graph", 1, sigma, S, g, N)
print("graphs done"); sys.stdout.flush()
for name, p, gen in PRIMES:
    F, a, Ia, Xi, Yi, phi = run_prime(name, p, gen)
    # sanity: Z itself
    pxz, pyz = orbit_action([0], F, Ia, Xi, Yi); gz, Nz = genus_from_action(pxz, pyz)
    n = Nz // NG
    print(name, "N(p)+1 =", n, " g(Z) =", gz, " expected", 1 + 4*n); sys.stdout.flush()
    if gz != 1 + 4*n or n != (p if gen is not None else p*p) + 1: raise SystemExit('FAIL: Hecke curve sanity ' + name)
    done = {}
    for sigma in range(NG):
        S = tuple(g for g in G if conj(phi[g], sigma) == g)
        if S not in done:
            px, py = orbit_action(list(S), F, Ia, Xi, Yi); done[S] = genus_from_action(px, py)
        g, N = done[S]; record(name, n, sigma, S, g, N)
json.dump(results, open("face_results.json", "w"))
from collections import Counter
low = [r for r in results if r["genus"] <= 1]
print("total twists", len(results), " genus<=1:", len(low))
print(Counter((r["prime"], r["n"], r["S_size"], r["e"], r["genus"]) for r in low))

# fail-closed final check (E04): exactly 32 rational + 48 elliptic curves, all graphs; no Hecke curve of genus <= 1
classes = {g: {frozenset(conj(r["sigma"], h) for h in G) for r in low if r["genus"] == g} for g in (0, 1)}
ok = (all(r["prime"] == "graph" for r in low) and len(classes[0]) == 32 and len(classes[1]) == 48
      and all(r["S_size"] == 8 and r["e"] == 4 for r in low if r["genus"] == 0)
      and all(r["S_size"] == 4 and r["e"] == 2 for r in low if r["genus"] == 1)
      and len(G) == 8 and len(G0) == 4)
print("distinct curves: genus 0", len(classes[0]), " genus 1", len(classes[1]))
print("PASS" if ok else "FAIL")
if not ok: raise SystemExit(1)
