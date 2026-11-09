#!/usr/bin/env python3
"""Check the scalar identities, separately from the modular polynomial checker."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
N = 393648362324456806647414264130928641711553162973261279756877858799612593368832


def main():
    with (HERE / "rank31_trace382.txt").open() as f:
        assert f.readline().strip() == "ROW382-31-CHAIN-1"
        f.readline()
        assert int(f.readline()) == N and int(f.readline()) == 8
        adds = negs = 0
        for name in ["H", "D+", "D-", "D5a", "D5b", "D7", "D14", "D15a"]:
            assert f.readline().split()[0] == name
            expr = [tuple(int(i == j) for j in range(9)) for i in range(9)]
            for _ in expr:
                f.readline()
            for _ in range(int(f.readline())):
                op, i, *rest = f.readline().split(maxsplit=4)
                i = int(i)
                assert 0 <= i < len(expr)
                if op == "N":
                    assert not rest
                    expr.append(tuple(-v for v in expr[i]))
                    negs += 1
                else:
                    assert op == "A" and len(rest) == 3
                    j = int(rest[0])
                    assert 0 <= j < len(expr)
                    expr.append(tuple(a + b for a, b in zip(expr[i], expr[j])))
                    adds += 1
            a, q = map(int, f.readline().split())
            assert 0 < a < 9 and 0 <= q < len(expr)
            assert expr[q] == tuple(N if k == 0 else int(k == a) for k in range(9))
        assert not f.read() and adds == 4473
        print(json.dumps({"scalar": str(N), "additions": adds, "negations": negs, "full_terminal_identities": 8}))


if __name__ == "__main__":
    main()
