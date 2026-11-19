# E25 check: for every n, a slack-0 cover profile (r, s, s, r, 0, 0) over (0, inf, 1, -1, i, -i)
# realised by dihedral involutions (s1, s2, s2, s1, id, id); and the label counts needed for
# topological type-(1,3) pairs between degrees n and n+1 (E25 section 3).
import sys
def compose(p, q):  # (p*q)(x) = p(q(x))
    return tuple(p[q[x]] for x in range(len(q)))
def refl(n, c):     # x -> c - x mod n
    return tuple((c - x) % n for x in range(n))
def ntrans(p):
    return sum(1 for x in range(len(p)) if p[x] != x) // 2
def transitive(gens, n):
    seen = {0}; st = [0]
    while st:
        x = st.pop()
        for g in gens:
            if g[x] not in seen: seen.add(g[x]); st.append(g[x])
    return len(seen) == n
N = int(sys.argv[1]) if len(sys.argv) > 1 else 40
ok = True
for n in range(1, N + 1):
    s1, s2 = refl(n, 0), refl(n, 1)
    e = tuple(range(n))
    tup = [s1, s2, s2, s1, e, e]
    prod = e
    for g in tup: prod = compose(prod, g)
    assert all(compose(g, g) == e for g in tup)
    t = [ntrans(g) for g in tup]
    good = prod == e and transitive(tup, n) and sum(t) == 2 * n - 2
    # odd points per label: e={0,inf}, b={1,-1}, a={i,-i}; n_chi = 2n - 2 t_chi
    nl = (2 * n - 2 * (t[0] + t[1]), 2 * n - 2 * (t[2] + t[3]), 2 * n - 2 * (t[4] + t[5]))
    ok &= good and sum(nl) == 2 * n + 4
    if n <= 8 or n == N: print(n, 'profile', t, 'odd per label (e,b,a)', nl, 'ok' if good else 'FAIL')
# type (1,3): degree n -> n+1 counts change by (0, 0, +2): e and b unchanged, a gains 2
for n in range(1, N):
    t = lambda m: [ntrans(refl(m, 0)), ntrans(refl(m, 1))]
    a1 = sum(t(n)); a2 = sum(t(n + 1))
    nl1 = (2*n - 2*a1, 2*n - 2*a1, 2*n); nl2 = (2*(n+1) - 2*a2, 2*(n+1) - 2*a2, 2*(n+1))
    ok &= (nl2[0] - nl1[0], nl2[1] - nl1[1], nl2[2] - nl1[2]) == (0, 0, 2)
print('PASS' if ok else 'FAIL')
