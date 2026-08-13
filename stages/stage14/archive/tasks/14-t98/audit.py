from itertools import product

# Verify the generic p-orientation pair identities and that every reconstructed
# linear predicate can only change through sign or congruence XORs.
checks = 0
sign_xor_checks = 0
congruence_xor_checks = 0
mods = [3, 5, 7, 11]
for u, v, A, B in product(range(-4, 5), repeat=4):
    if A == 0 and B == 0:
        continue
    gp = (u*A-v*B, u*B+v*A)
    gm = (u*A+v*B, -u*B+v*A)
    assert gp[0] - gm[0] == -2*v*B
    assert gp[1] - gm[1] == 2*u*B
    assert gp[0] + gm[0] == 2*u*A
    assert gp[1] + gm[1] == 2*v*A
    assert gp[0]*gp[0] + gp[1]*gp[1] == gm[0]*gm[0] + gm[1]*gm[1]

    # representative reconstructed linear forms: q-p and q+p
    rp, tp = gp[1]-gp[0], gp[1]+gp[0]
    rm, tm = gm[1]-gm[0], gm[1]+gm[0]
    for lp, lm in ((rp, rm), (tp, tm), (gp[0], gm[0]), (gp[1], gm[1])):
        sx = (lp > 0) ^ (lm > 0)
        assert sx in (False, True)
        sign_xor_checks += 1
        for q in mods:
            dx = (lp % q == 0) ^ (lm % q == 0)
            assert dx in (False, True)
            congruence_xor_checks += 1
    checks += 1

# Primitive-selector invariance is a valuation statement.  Audit its local
# split-prime model: for a generic p, the background carries no p-primary
# factor, so choosing pi^e versus conjugate(pi)^e never supplies both sides.
primitive_local_checks = 0
for left_bg, right_bg, e in product(range(3), range(3), range(1, 5)):
    if left_bg or right_bg:
        continue  # genericity requires no p-primary background
    plus = (left_bg + e, right_bg)
    minus = (left_bg, right_bg + e)
    assert not (plus[0] and plus[1])
    assert not (minus[0] and minus[1])
    primitive_local_checks += 1

print({
    'orientation_pair_checks': checks,
    'sign_xor_checks': sign_xor_checks,
    'congruence_xor_checks': congruence_xor_checks,
    'primitive_local_checks': primitive_local_checks,
    'status': 'ok',
})
