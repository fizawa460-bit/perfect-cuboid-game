from itertools import combinations
from math import gcd

LINES = {
    "Lx": (1, 0, 0),
    "Ly": (0, 1, 0),
    "Lz": (0, 0, 1),
    "Lxy": (1, 1, 0),
    "Lxz": (1, 0, 1),
    "Lyz": (0, 1, 1),
    "Ls": (1, 1, 1),
}


def normalize_projective(v):
    g = 0
    for a in v:
        g = gcd(g, abs(a))
    if g:
        v = tuple(a // g for a in v)
    for a in v:
        if a:
            if a < 0:
                v = tuple(-b for b in v)
            break
    return v


def cross(a, b):
    return normalize_projective((
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    ))


def vanishes(line, point):
    return sum(a * b for a, b in zip(line, point)) == 0


def main():
    points = {}
    for n1, n2 in combinations(LINES, 2):
        p = cross(LINES[n1], LINES[n2])
        points[p] = tuple(sorted(n for n, l in LINES.items() if vanishes(l, p)))

    assert len(points) == 9
    multiplicities = sorted(len(v) for v in points.values())
    assert multiplicities == [2, 2, 2, 3, 3, 3, 3, 3, 3]

    triples = {p: inc for p, inc in points.items() if len(inc) == 3}
    doubles = {p: inc for p, inc in points.items() if len(inc) == 2}
    assert len(triples) == 6
    assert len(doubles) == 3

    # Bipartite incidence graph: seven line vertices plus nine point vertices.
    V = len(LINES) + len(points)
    E = sum(len(inc) for inc in points.values())
    assert V == 16
    assert E == 24

    # Connectivity by BFS on line/point bipartite graph.
    adj = {}
    for n in LINES:
        adj[("L", n)] = set()
    for p, inc in points.items():
        pv = ("P", p)
        adj[pv] = set()
        for n in inc:
            lv = ("L", n)
            adj[pv].add(lv)
            adj[lv].add(pv)

    start = next(iter(adj))
    seen = {start}
    stack = [start]
    while stack:
        v = stack.pop()
        for w in adj[v]:
            if w not in seen:
                seen.add(w)
                stack.append(w)
    assert len(seen) == V

    b1 = E - V + 1
    assert b1 == 9

    print("TRIPLE_POINTS=6")
    print("DOUBLE_POINTS=3")
    print("INCIDENCE_GRAPH_VERTICES=16")
    print("INCIDENCE_GRAPH_EDGES=24")
    print("INCIDENCE_GRAPH_CONNECTED=true")
    print("B1_GAMMA=9")


if __name__ == "__main__":
    main()
