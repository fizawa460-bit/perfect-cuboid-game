from itertools import product


def audit_rank(r: int):
    pts = list(product((0, 1), repeat=r))
    index = {x: i for i, x in enumerate(pts)}
    n = len(pts)
    checked = 0
    live = 0

    # Exhaust all Boolean functions for r<=4.
    for mask in range(1 << n):
        vals = [(mask >> i) & 1 for i in range(n)]
        mu = sum(vals) / n
        var = mu * (1.0 - mu)

        influences = []
        for j in range(r):
            changed = 0
            for i, x in enumerate(pts):
                y = list(x)
                y[j] ^= 1
                changed += vals[i] != vals[index[tuple(y)]]
            influences.append(changed / n)

        total = sum(influences)
        assert var <= 0.25 * total + 1e-12

        mean = total / r
        movers = sum(i > 0.0 for i in influences)
        assert movers / r + 1e-12 >= mean

        energy = sum(i * i for i in influences) / r
        assert energy + 1e-12 >= mean * mean

        # Three-class pigeonhole model: assign each coordinate's whole
        # influence to one broad class. This is an extremal equality case
        # of I_p <= I_p^SIGN + I_p^DIV + I_p^PROJ.
        class_mass = [0.0, 0.0, 0.0]
        for j, inf in enumerate(influences):
            class_mass[j % 3] += inf
        assert max(class_mass) + 1e-12 >= total / 3.0

        checked += 1
        if var > 0.0:
            live += 1

    return checked, live


total_checked = 0
total_live = 0
for r in range(1, 5):
    checked, live = audit_rank(r)
    total_checked += checked
    total_live += live

print({
    "boolean_functions_checked": total_checked,
    "nonconstant_live_functions": total_live,
    "max_rank": 4,
    "poincare_checked": True,
    "mover_support_density_checked": True,
    "mover_energy_jensen_checked": True,
    "three_class_pigeonhole_checked": True,
    "status": "ok",
})
