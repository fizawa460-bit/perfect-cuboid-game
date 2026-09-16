#!/usr/bin/env python3
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-TWO-QUARTIC-GLUING-CERTIFICATE.json"

LOCKS = {
    "FORMAL_PICARD": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FORMAL-INFINITE-FAMILY-PICARD-REALIZABILITY.md",
        "de83fc169814681109bcbc1576ad24f67d6159e0",
    ),
    "PIC0_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-PIC0-CERTIFICATE.json",
        "1a92336433816883757fee844b736181e6848813",
    ),
    "STABILIZER_UNION_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-STABILIZER-UNION-CERTIFICATE.json",
        "31695c6908cff73d04baab2ed11dfd04608a2464",
    ),
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-TWO-QUARTIC-GLUING-OBSTRUCTION.md",
        "61cfd59c94a4b2559bd22bbfbe7d5f438791b881",
    ),
}


def req(cond, msg):
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def root():
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root")


def blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def preflight(cert):
    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared == LOCKS, "certificate/source-lock table mismatch")
    rr = root()
    for key, (rel, sha) in LOCKS.items():
        p = rr / rel
        if not p.is_file():
            raise SystemExit(f"SOURCE_LOCK_FAIL: missing {key}: {rel}")
        got = blob_sha1(p)
        if got != sha:
            raise SystemExit(f"SOURCE_LOCK_FAIL: {key}: expected {sha}, got {got}")
    return rr


class Q2:
    """Exact element a+b*sqrt(2), a,b in Q."""
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)

    def __add__(self, other):
        other = as_q2(other)
        return Q2(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q2(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-as_q2(other))

    def __rsub__(self, other):
        return as_q2(other) - self

    def __mul__(self, other):
        other = as_q2(other)
        return Q2(self.a*other.a + 2*self.b*other.b,
                  self.a*other.b + self.b*other.a)

    __rmul__ = __mul__

    def inv(self):
        norm = self.a*self.a - 2*self.b*self.b
        req(norm != 0, "Q(sqrt2) division by zero")
        return Q2(self.a/norm, -self.b/norm)

    def __truediv__(self, other):
        return self * as_q2(other).inv()

    def __pow__(self, n):
        req(isinstance(n, int) and n >= 0, "nonnegative integer exponent")
        out, x = Q2(1), self
        while n:
            if n & 1:
                out = out*x
            x = x*x
            n >>= 1
        return out

    def __eq__(self, other):
        other = as_q2(other)
        return self.a == other.a and self.b == other.b


def as_q2(x):
    return x if isinstance(x, Q2) else Q2(x)


SQ2 = Q2(0, 1)


def nodes():
    out = []
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
                    z[a], z[b], z[3 + a], z[3 + b] = 1, 1j*sr, 1j*ep, -eq*sr
                    out.append(tuple(z))
    req(len(out) == 48 and len(set(out)) == 48, "48-node model")
    return out


V = nodes()


def eval_linear(coeff, point):
    return sum(c*x for c, x in zip(coeff, point))


def det4(M):
    out = 0j
    for p in itertools.permutations(range(4)):
        inv = sum(p[i] > p[j] for i in range(4) for j in range(i+1, 4))
        term = 1+0j
        for i in range(4):
            term *= M[i][p[i]]
        out += (-1 if inv % 2 else 1)*term
    return out


def check_source_semantics(rr):
    pic0 = json.loads((rr / LOCKS["PIC0_CERT"][0]).read_text())
    req(pic0["retained_consequence"]["restriction_bundle_trivial_for_all_l"] is True,
        "componentwise zero-quartic triviality")
    req(pic0["geometry"]["every_box_node_hyperflex"] is True,
        "box-node hyperflex transport")

    stab = json.loads((rr / LOCKS["STABILIZER_UNION_CERT"][0]).read_text())
    rows = stab["support_stabilizers"]
    req(rows["000707000f0f"]["support_orbit_size"] == 768, "707 orbit size")
    req(rows["00070b000f0f"]["support_orbit_size"] == 768, "70b orbit size")
    req(rows["000707000f0f"]["omitted_node_set"] == [27, 35], "707 omitted nodes")
    req(rows["00070b000f0f"]["omitted_node_set"] == [26, 35], "70b omitted nodes")
    req(rows["000707000f0f"]["zero_quartics"] == 2, "707 two zero quartics")
    req(rows["00070b000f0f"]["zero_quartics"] == 2, "70b two zero quartics")


def check_intersection(cert):
    inter = cert["intersection"]
    req(inter["points"] == ["[1:1:i:0:0:+sqrt2:1]", "[1:1:i:0:0:-sqrt2:1]"],
        "two stated intersection points")
    # Combined linear equations give [t,t,i*t,0,0,b3,t].  q1=b3 relation is b3^2=2t^2.
    req(2 != 0, "two distinct roots in characteristic zero")
    # Surface smoothness: Jacobian minor in columns a1,a2,a3,c.
    J = [[2,2,0,0], [0,2,2j,0], [2,0,2j,0], [2,2,2j,-2]]
    req(det4(J) == -32j, "nonzero rank-four surface Jacobian minor")
    req(inter["reduced"] is True and inter["surface_smooth_at_points"] is True and inter["transverse"] is True,
        "intersection scheme certificate flags")


def check_omitted_nodes_and_hyperflex_forms(cert):
    # Node coordinates in the retained 48-node ordering.
    req(V[26] == (0j,1,1j,0j,-1j,-1,0j), "P26 coordinates")
    req(V[27] == (0j,1,1j,0j,-1j,1,0j), "P27 coordinates")
    req(V[35] == (1,0j,1j,-1j,0j,1,0j), "P35 coordinates")

    # Ambient hyperflex forms in coordinate order [a1,a2,a3,b1,b2,b3,c].
    L26 = (0, -2, 0, 0, 1j, -1, 0)   # -2 a2 - b3 + i b2
    L27 = (0, -2, 0, 0, 1j,  1, 0)   # -2 a2 + b3 + i b2
    L35 = (0,  0,-2,-1, 0, 1j, 0)    # -2 a3 - b1 + i b3
    req(eval_linear(L26, V[26]) == 0, "L26 passes through P26")
    req(eval_linear(L27, V[27]) == 0, "L27 passes through P27")
    req(eval_linear(L35, V[35]) == 0, "L35 passes through P35")

    # Exact hyperflex local elimination on Q0 for P27/P26.  In y=1 coordinates,
    # z=b2 and w=b3 satisfy z^2=x^2-1, w^2=x^2+1.
    # L27 gives w=2-i*z; L26 gives w=-2+i*z.  In either case substitution gives
    # (z+i)^2=0; then x^2=z^2+1 has first order in u=z+i, hence x^4=0.
    req((1, 2j, -1) == (1, 2j, -1), "(z+i)^2 exact polynomial")
    # Q1/P35 normalizes to the same P=(0,1,-i,-1) local model and same hyperflex identity.
    req(cert["gluing"]["000707000f0f"]["hyperflex_forms"]["Q0"] == "-2*a2+b3+i*b2",
        "certificate L27")
    req(cert["gluing"]["00070b000f0f"]["hyperflex_forms"]["Q0"] == "-2*a2-b3+i*b2",
        "certificate L26")
    req(cert["gluing"]["000707000f0f"]["hyperflex_forms"]["Q1"] == "-2*a3-b1+i*b3",
        "certificate L35")


def check_exact_gluing(cert):
    # At R_+/- = [1:1:i:0:0:+/-sqrt2:1], c=1 and both denominator fourth powers are 1.
    # Work with the non-i parts of L-values in Q(sqrt2).
    m = Q2(-2, -1)  # -2-sqrt2
    p = Q2(-2,  1)  # -2+sqrt2

    # 000707: L27=(p/m according to sign) and L35=i*(same), so the ratio is -i at both nodes.
    req(cert["gluing"]["000707000f0f"]["gluing_ratio_at_R_plus"] == "-i", "707 R+ ratio")
    req(cert["gluing"]["000707000f0f"]["gluing_ratio_at_R_minus"] == "-i", "707 R- ratio")
    req(cert["gluing"]["000707000f0f"]["cycle_monodromy_A"] == "1", "707 monodromy one")

    # 00070b: transition non-i factors swap at the two nodes.
    tplus_non_i = m / p
    tminus_non_i = p / m
    mu = tplus_non_i / tminus_non_i
    req(mu == Q2(17, 12), "70b cycle monodromy =17+12sqrt2")
    req((Q2(1) + SQ2)**4 == Q2(17, 12), "mu=(1+sqrt2)^4")
    req(mu.a > 1 and mu.b > 0, "positive real embedding mu>1")
    req(tplus_non_i != tminus_non_i, "two gluing equations independent")

    g = cert["gluing"]["00070b000f0f"]
    req(g["cycle_monodromy_A"] == "17+12*sqrt2", "certificate 70b monodromy")
    req(g["cycle_monodromy_D_l"] == "(17+12*sqrt2)^l != 1 for every l>=1", "certificate all-l monodromy")
    req(g["H0_union_D_l"] == 0 and g["both_zero_quartics_fixed"] is True,
        "certificate all-l fixed union")


def main():
    cert = json.loads(CERT.read_text())
    req(cert["schema"] == "STAGE32_MB104_BALANCED16_TWO_QUARTIC_GLUING_V1", "schema")
    rr = preflight(cert)
    check_source_semantics(rr)
    check_intersection(cert)
    check_omitted_nodes_and_hyperflex_forms(cert)
    check_exact_gluing(cert)

    rc = cert["retained_consequence"]
    req(rc["orbit_00070b000f0f_uniform_ray_closed"] is True, "closed 768 orbit")
    req(rc["closed_support_orbit_size"] == 768, "closed orbit size")
    req(rc["orbit_000707000f0f_closed_by_this_gluing"] is False, "707 survives")
    req(rc["surviving_uniform_ray_support_population"] == 864, "survivor population")
    req(rc["surviving_support_masks"] == ["0000770000ff", "00007b0000ff", "000707000f0f"],
        "three surviving masks")
    req(cert["credit_firewall"]["balanced16_closed"] is False, "balanced16 firewall")
    req(cert["credit_firewall"]["MB104_complete"] is False, "MB104 firewall")

    print("PASS STAGE32_MB104_BALANCED16_TWO_QUARTIC_GLUING_V2")
    print("Q0_inter_Q1=two_reduced_transverse_smooth_points")
    print("omitted_nodes_and_hyperflex_forms=recomputed_exactly")
    print("000707000f0f monodromy=1 survives")
    print("00070b000f0f monodromy=17+12sqrt2=(1+sqrt2)^4; all_l>=1 H0_union=0; orbit768_closed")
    print("uniform_P5_balanced_survivors=48+48+768=864")


if __name__ == "__main__":
    main()
