from itertools import product


def check_case(assignments, good):
    # assignments is a list of packet labels theta=pi(lambda)
    occ = {}
    for th in assignments:
        occ[th] = occ.get(th, 0) + 1

    m1 = sum(v for th, v in occ.items() if th in good)
    m2 = sum(v * v for th, v in occ.items() if th in good)
    hit = sum(1 for th, v in occ.items() if th in good and v)
    hit_witness = sum(1 for th in assignments if th in good)

    assert m1 == hit_witness
    assert hit <= m1
    max_occ = max(occ.values(), default=0)
    assert m2 <= max_occ * m1
    if m1:
        assert hit * m2 >= m1 * m1
        assert hit * max_occ >= m1


for n in range(1, 7):
    for assignments in product(range(3), repeat=n):
        for mask in range(8):
            good = {i for i in range(3) if mask & (1 << i)}
            check_case(assignments, good)

print('STAGE14_S_BATCH_S7_144_146_AUDIT=PASS')
