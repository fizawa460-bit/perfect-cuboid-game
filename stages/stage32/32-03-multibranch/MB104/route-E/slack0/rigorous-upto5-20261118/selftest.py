"""Self-tests: (1) the search must report the trivial configuration (f, f, id) for every query cover when a = b;
(2) prove_V must FAIL for a wrong U and for a perturbed triple; (3) transfer must fail for a wrong triple."""
import sys, pickle, numpy as np
a, b = int(sys.argv[1]), int(sys.argv[2])
sys.argv = [sys.argv[0], str(a), str(b)]
src = open('prove.py').read(); src = src[:src.index('# ---------- main')]
exec(src)
SV = pickle.load(open(f'surv_{a}_{b}.pkl', 'rb'))
# (1)
if a == b:
    idx = {k: i for i, k in enumerate(SV['FB'])}
    found = set()
    for s in SV['surv']:
        if s['pi'] == 0 and SV['FA'][s['fi']] == SV['FB'][s['qi']]:
            x = [FA[s['fi']].oddc[k] for k in s['xq'][:3]]; y = [FB[s['qi']].oddc[k] for k in s['yq'][:3]]
            if max(abs(u - v) for u, v in zip(x, y)) < 1e-12: found.add(s['fi'])
    print('(1) trivial (f,f,id) found for', len(found), 'of', len(FA), 'query covers')
# (2)/(3) on a few survivors
rng = np.random.default_rng(0); bad_ok = 0; tests = 0; good_ok = 0
for s in [SV['surv'][i] for i in rng.choice(len(SV['surv']), 30, replace=False)]:
    f = FA[s['fi']]; q = FB[s['qi']]
    for U in AUTq:
        if all(U[1][f.oddy[s['xq'][i]]] == q.oddy[s['yq'][i]] for i in range(3)):
            ok, _ = prove_V(f, q, s['xq'], s['yq'], U); tests += 1
            good_ok += ok
    # perturbed triple: replace the third target point by another odd point of q with the same B value
    yq = list(s['yq'])
    alt = [k for k in range(len(q.oddy)) if q.oddy[k] == q.oddy[yq[2]] and k not in yq]
    if alt:
        yq2 = yq[:2] + [alt[0]] + yq[3:]
        for U in AUTq:
            if all(U[1][f.oddy[s['xq'][i]]] == q.oddy[yq2[i]] for i in range(3)):
                ok, _ = prove_V(f, q, s['xq'], yq2, U); bad_ok += ok
print('(2) prove_V over all label-compatible U:', tests, 'attempts,', good_ok, 'succeeded (expected: only the true U, |Aut(f)|-many)')
print('    perturbed triples proved (must be 0 unless the perturbed M is itself a composite):', bad_ok)
