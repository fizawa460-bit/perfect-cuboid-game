"""Cost of the quadruple index: current layout vs. j-invariant keys with split subsets."""
from math import comb
N = {4: 680, 5: 6090, 6: 70158, 7: 858040, 8: 11012925}       # all covers (weighted)
R = {4: 158, 5: 612, 6: 7040, 7: 118568}                       # profile representatives (weighted)
R[8] = None
for a, b in [(4, 4), (5, 5), (5, 6), (6, 6), (6, 7), (7, 7)]:
    nA, nB = 2 * a + 4, 2 * b + 4; jmin = max(nA, nB) - 4
    best = []
    for fa_deg, q_deg in ((a, b), (b, a)) if a != b else ((a, a),):
        nf, nq = 2 * fa_deg + 4, 2 * q_deg + 4
        cur = R[fa_deg] * comb(nf - jmin + 4, 4) * 24 + N[q_deg] * comb(nq, 4) * 6
        need = nf + nq - jmin + 4
        for Fa in range(4, nf + 1):
            Fb = need - Fa
            if Fb < 4 or Fb > nq: continue
            qa, tb = R[fa_deg] * comb(Fa, 4), N[q_deg] * comb(Fb, 4)
            best.append((qa + tb, fa_deg, Fa, Fb, qa, tb, cur))
    c = min(best)
    print(f'({a},{b}): current {c[6]:.2e} (table+lookups)  ->  new {c[0]:.2e} (query side deg {c[1]}: {c[2]} pts, {c[4]:.2e}; other side {c[3]} pts, {c[5]:.2e})  ratio {c[6]/c[0]:.0f}x')
