# A1-12-ex independent Sage/eclib certification.
# Database lookup is disabled for the Mordell-Weil computation.

proof.all(True)

E = EllipticCurve(QQ, [0,1,0,95,703])
P = E(3,32)

assert E.discriminant() == -249036800
assert E.rank(proof=True, use_database=False, algorithm='mwrank_lib') == 1
assert E.rank_bound(algorithm='pari') == 1
G = E.gens(proof=True, use_database=False, algorithm='mwrank_lib', sat_bound=10000)
assert E.gens_certain() is True
assert len(G) == 1
assert G[0] == P or G[0] == -P
assert E.torsion_subgroup().order() == 1

print('SAGE_MW_RANK=1')
print('SAGE_RANK_BOUND=1')
print('SAGE_GENS_CERTAIN=true')
print('SAGE_GENERATOR=', G[0])
print('SAGE_TORSION_ORDER=1')

expected = {
    7:   (9,  {0,1,2,8}),
    23:  (29, {0,1,2,28}),
    37:  (10, {0,1,2,9}),
    257: (22, {0,1,2,21}),
    263: (34, {0,1,2,33}),
    863: (21, {0,1,2,20}),
}

for p,(want_order,want_allowed) in expected.items():
    Ep = E.change_ring(GF(p))
    Pp = Ep(3,32)
    N = Pp.order()
    assert N == want_order
    allowed = set()
    for n in range(N):
        R = n*Pp
        if R[2] == 0:
            allowed.add(n)  # O: pole retained
            continue
        xx,yy = R[0],R[1]
        if xx == GF(p)(3) and yy == GF(p)(32):
            allowed.add(n)  # P: pole retained
            continue
        if xx == GF(p)(3):
            assert yy == GF(p)(-32)
            zz = GF(p)(2)
        else:
            zz = -(yy+GF(p)(32))/(xx-GF(p)(3))
        if (zz+2).is_square() and (zz-2).is_square():
            allowed.add(n)
    assert allowed == want_allowed
    print('SAGE_FP', p, 'ORDER', N, 'ALLOWED', sorted(allowed))

print('A1-12-ex Sage/eclib certification: PASS')
