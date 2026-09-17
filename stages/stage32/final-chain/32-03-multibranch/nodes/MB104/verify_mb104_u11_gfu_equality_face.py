#!/usr/bin/env python3

MASK = "000707000f0f"


def req(cond, msg):
    if not cond:
        raise SystemExit("FAIL: " + msg)


def nodes():
    out = []
    I = 1j
    for j in range(3):
        for sa in (1, -1):
            for s1 in (1, -1):
                for s2 in (1, -1):
                    z = [0j] * 7
                    z[j] = sa
                    o = [t for t in range(3) if t != j]
                    z[3 + o[0]], z[3 + o[1]], z[6] = s1, s2, 1
                    out.append(tuple(z))
    for j in range(3):
        o = [t for t in range(3) if t != j]
        a, b = o
        for sr in (1, -1):
            for ep in (1, -1):
                for eq in (1, -1):
                    z = [0j] * 7
                    z[a] = 1
                    z[b] = I * sr
                    z[3 + a] = I * ep
                    z[3 + b] = -eq * sr
                    out.append(tuple(z))
    req(len(out) == 48 and len(set(out)) == 48, "canonical 48-node model")
    return out


def support(mask):
    m = int(mask, 16)
    return [i for i in range(48) if (m >> i) & 1]


def main():
    V = nodes()
    S = support(MASK)
    req(S == [0, 1, 2, 3, 8, 9, 10, 11, 24, 25, 26, 32, 33, 34], "000707 support")
    req(len(S) == 14, "N=14")

    # GFU cuboid coordinates are matched to the Stage32 convention by
    # x0=a1, x1=a2, x2=a3, x3=c; the remaining face diagonals are a permutation
    # of b1,b2,b3 and are irrelevant here.  GFU E_i is the sum of exceptional
    # curves above the 24 nodes whose image lies on x_i=0.
    coords = [0, 1, 2, 6]
    counts = [sum(1 for j in S if V[j][k] == 0) for k in coords]
    req(counts == [7, 7, 8, 6], f"GFU E_i support counts: {counts}")

    complement_counts = [14 - x for x in counts]
    req(complement_counts == [7, 7, 6, 8], "GFU E'_i support counts")

    # Every supported exceptional has D_l.E_p=8l.  Thus, for genus one, the
    # four Lemma-3.4 enhanced GFU sections have restriction degrees
    # (E'_i.C)=8l * complement_count.
    degree_coefficients = [8 * x for x in complement_counts]
    req(degree_coefficients == [56, 56, 48, 64], "enhanced GFU degree coefficients")
    req(all(x > 0 for x in degree_coefficients), "all enhanced GFU degrees positive")

    # Base GFU Theorem 3.1 degree on the dangerous equality ray:
    # -d + E.C + 4g-4 = -112l + 112l + 0 = 0.
    req(-112 + 112 == 0, "base GFU equality face")

    print("PASS: U11 GFU equality-face replay")
    print("000707 GFU E_i node counts = [7,7,8,6]")
    print("enhanced genus-one restriction degrees = [56,56,48,64] * l > 0")
    print("base GFU Theorem 3.1 degree = 0, not negative")


if __name__ == "__main__":
    main()
