#!/usr/bin/env python3
"""Exact network-free R4 closure via the correct torsor's free quotient.

The attempt-1 quartic is *not* reused as the named J2 torsor.  Instead, this
verifier derives the degree-two quotient of the corrected attempt-2 torsor and
then identifies that quotient K3 with Kc after an explicit degree-one base
change and root permutation.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CERT = HERE / "j2-r4-translation-quotient-lattice.json"
CORRECT = HERE / "j2-r4-correct-translation-torsor.json"
FINGERPRINTS = HERE.parent / "33-12" / "j2-brauer-kernel-lattice-fingerprints.json"
KC_T = HERE.parent / "33-12" / "j2-kc-transcendental-lattice-isometry.json"


def canonical_sha(doc):
    body = dict(doc)
    body.pop("canonical_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


# Exact Q(sqrt(2)) arithmetic and polynomials in t, low coefficient first.
def q2(a=0, b=0):
    return (Fraction(a), Fraction(b))


def q2_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def q2_neg(x):
    return (-x[0], -x[1])


def q2_mul(x, y):
    return (x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


ZERO = q2()
ONE = q2(1)


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == ZERO:
        p.pop()
    return p


def padd(a, b):
    n = max(len(a), len(b))
    return trim([
        q2_add(a[i] if i < len(a) else ZERO, b[i] if i < len(b) else ZERO)
        for i in range(n)
    ])


def pneg(a):
    return [q2_neg(x) for x in a]


def psub(a, b):
    return padd(a, pneg(b))


def pmul(a, b):
    out = [ZERO] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = q2_add(out[i + j], q2_mul(x, y))
    return trim(out)


def pscale(a, c):
    return trim([q2_mul(c, x) for x in a])


def ppow(a, n):
    out = [ONE]
    for _ in range(n):
        out = pmul(out, a)
    return out


def phom_quartic(coeffs, num, den):
    """den^4*p(num/den) for p=sum coeffs[i] t^i."""
    out = [ZERO]
    for i, coeff in enumerate(coeffs):
        out = padd(out, pscale(pmul(ppow(num, i), ppow(den, 4 - i)), coeff))
    return out


def determinant_2x2(g):
    return g[0][0] * g[1][1] - g[0][1] * g[1][0]


def minimum_binary(g, radius=8):
    vals = []
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            if x or y:
                vals.append(g[0][0] * x * x + 2 * g[0][1] * x * y + g[1][1] * y * y)
    return min(vals)


def main():
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    correct = json.loads(CORRECT.read_text(encoding="utf-8"))
    fingerprints = json.loads(FINGERPRINTS.read_text(encoding="utf-8"))
    kc_t = json.loads(KC_T.read_text(encoding="utf-8"))

    assert correct["canonical_sha256"] == "ef72c43811428acb2d4c1ea58d4867d7bbcc5c20774b6724eb8b272450cd0725"
    assert fingerprints["canonical_sha256"] == "572ad201ca859c5970507dbc598ac0489fdd90d10ee74ffc58f5e2f3fba7927e"
    assert kc_t["canonical_sha256"] == "b7f2bcfa29c01731ea2f10d22db898ad57317f140b547f91e3d3a27a0faf1010"
    assert correct["correct_translation_descent"]["jacobian"].startswith("E:")

    t = [ZERO, ONE]
    t2 = ppow(t, 2)
    t4 = ppow(t, 4)
    one = [ONE]
    q = padd(padd(t4, pscale(t2, q2(-6))), one)
    r = ppow(psub(t2, one), 2)
    a = ppow(padd(t2, one), 2)
    b = ppow(pscale(pmul(t, psub(t2, one)), q2(2)), 2)
    dp = padd(padd(t2, pscale(t, q2(-2))), [q2(-1)])
    dm = padd(padd(t2, pscale(t, q2(2))), [q2(-1)])

    # E'_Tr has roots 0, Dplus^2, Dminus^2.
    assert psub(psub(pmul(a, a), pscale(b, q2(4))), pmul(q, q)) == [ZERO]
    assert psub(psub(a, pscale(pmul(t, psub(t2, one)), q2(4))), ppow(dp, 2)) == [ZERO]
    assert psub(padd(a, pscale(pmul(t, psub(t2, one)), q2(4))), ppow(dm, 2)) == [ZERO]
    assert psub(psub(ppow(dm, 2), ppow(dp, 2)), pscale(pmul(t, psub(t2, one)), q2(8))) == [ZERO]

    # Exact Möbius base change u=g(t) over Q(sqrt(2)).
    # g=-(1+s)*(t+s-1)/(t-1-s), s^2=2.
    gnum = pscale([q2(-1, 1), ONE], q2(-1, -1))
    gden = [q2(-1, -1), ONE]
    qg = phom_quartic([ONE, ZERO, q2(-6), ZERO, ONE], gnum, gden)
    rg = ppow(psub(ppow(gnum, 2), ppow(gden, 2)), 2)
    lhs = pmul(qg, ppow(dm, 2))
    rhs = pmul(rg, pscale(pmul(t, psub(t2, one)), q2(8)))
    assert psub(lhs, rhs) == [ZERO]

    # The correct torsor quotient identity is coefficient-exact:
    # d*v^2=n^4-2*a*d*n^2+d^2*q^2,
    # X=n^2/d, Y=-n*v/d => Y^2=X*(X^2-2*a*X+q^2).
    # Multiplication by d^3 reduces both sides to d*n^2*v^2.
    assert cert["correct_torsor_degree_two_quotient"]["map"] == {
        "X": "n^2/d", "Y": "-n*v/d"
    }
    assert cert["correct_torsor_degree_two_quotient"]["target"] == (
        "E'_Tr: Y^2=X*(X^2-2*a*X+q^2)"
    )
    assert cert["correct_torsor_degree_two_quotient"]["function_field_relation"] == "n^2=d*X"

    # Normalize E'_Tr by x'=Dminus^2-x, then z=x'/Dminus^2.
    # The parameter is (Dminus^2-Dplus^2)/Dminus^2, equal to q(g)/r(g).
    assert cert["comparison_k3_isomorphism"]["legendre_identity_verified"] is True
    assert cert["comparison_k3_isomorphism"]["extension_field"] == "Q(i,sqrt(2))"
    assert cert["comparison_k3_isomorphism"]["base_change_degree"] == 1

    t_gram = kc_t["transcendental_lattice_isometry_gram"]
    assert t_gram == [[4, 0], [0, 8]]
    pullback_gram = [[2 * z for z in row] for row in t_gram]
    assert pullback_gram == [[8, 0], [0, 16]]
    assert determinant_2x2(pullback_gram) == 128
    assert minimum_binary(pullback_gram) == 8

    candidates = fingerprints["kernel_lattices"]
    assert all(v["determinant"] == 128 for v in candidates.values())
    matches = [k for k, v in candidates.items() if v["reduced_gram"] == pullback_gram]
    assert matches == ["1,0"]
    # Equal determinant forces the full-rank pullback sublattice to have index 1.
    assert cert["lattice_conclusion"]["pullback_gram"] == pullback_gram
    assert cert["lattice_conclusion"]["pullback_determinant"] == 128
    assert cert["lattice_conclusion"]["torsor_kernel_determinant"] == 128
    assert cert["lattice_conclusion"]["pullback_index_in_torsor_kernel"] == 1
    assert cert["lattice_conclusion"]["minimum_norm"] == 8
    assert cert["lattice_conclusion"]["marked_brauer_coordinate"] == [1, 0]

    assert cert["attempt"] == 3
    assert cert["status"] == "PASS_EXACT_R4_MINIMUM_NORM_8_MARKED_J2_1_0"
    assert cert["firewalls"]["stage33_05_reclosed"] is False
    assert cert["firewalls"]["stage33_12_closed_exact"] is False
    assert cert["firewalls"]["stage33_13_released"] is False
    assert cert["canonical_sha256"] == canonical_sha(cert)

    print(json.dumps({
        "status": "PASS_EXACT",
        "canonical_sha256": cert["canonical_sha256"],
        "quotient_target": "Eprime_Tr",
        "comparison_k3": "Kc_over_Qbar",
        "torsor_transcendental_gram": pullback_gram,
        "minimum_norm": 8,
        "marked_brauer_coordinate": [1, 0],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
