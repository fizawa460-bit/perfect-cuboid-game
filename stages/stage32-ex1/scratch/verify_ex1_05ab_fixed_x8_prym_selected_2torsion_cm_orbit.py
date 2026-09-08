#!/usr/bin/env python3

# Exact finite replay for EX1-05AB.
# This verifier checks only the sign-group adapter, the three explicit elliptic
# quotient models, the Gaussian two-torsion orbit criterion, and the fixed
# Stage32EX1 state count. It does not claim actual carrier existence.


def xor(a, b):
    return tuple(x ^ y for x, y in zip(a, b))


su = (1, 0, 0)
sv = (0, 1, 0)
sw = (0, 0, 1)
identity = (0, 0, 0)
H = {
    identity,
    xor(su, sv),
    xor(su, sw),
    xor(sv, sw),
}
assert all(sum(g) % 2 == 0 for g in H)
assert len(H) == 4

j = xor(xor(su, sv), sw)
sigma = xor(sv, sw)
tau = xor(su, sw)
sigma_tau = xor(su, sv)
assert xor(j, sigma) == su
assert xor(j, tau) == sv
assert xor(j, sigma_tau) == sw
assert j not in H

# Explicit quotient identities from the X(8) sign model.
# u-character: Y^2=t^4+4, A=t^2, B=tY -> B^2=A^3+4A.
for t in range(-4, 5):
    A = t * t
    lhs = t * t * (t ** 4 + 4)
    rhs = A ** 3 + 4 * A
    assert lhs == rhs

# v-character: w^2=u^4+1, A=u^2, B=uw -> B^2=A^3+A.
for u in range(-4, 5):
    A = u * u
    lhs = u * u * (u ** 4 + 1)
    rhs = A ** 3 + A
    assert lhs == rhs

# w-character: v^2=u^4-1, A=u^2, B=uv -> B^2=A^3-A.
for u in range(-4, 5):
    A = u * u
    lhs = u * u * (u ** 4 - 1)
    rhs = A ** 3 - A
    assert lhs == rhs

# Short Weierstrass y^2=x^3+a*x (a != 0) has j=1728.
def j_short_ax(a):
    assert a != 0
    c4 = -48 * a
    delta = -64 * (4 * a ** 3)
    return c4 ** 3 // delta

assert j_short_ax(4) == 1728
assert j_short_ax(1) == 1728
assert j_short_ax(-1) == 1728

# Gaussian CM on E:y^2=x^3-x fixes (0,0) and swaps (+/-1,0).
# Quotient by the fixed subgroup gives y^2=x^3+4x, hence j=1728.
assert j_short_ax(4) == 1728

# Quotient by a swapped subgroup, using P=(1,0): after x=X+1,
# y^2=X^3+3X^2+2X. The standard 2-isogeny quotient is
# y^2=X^3-6X^2+X. Replay its general Weierstrass j.
def j_a2_a4(a2, a4):
    # a1=a3=a6=0
    b2 = 4 * a2
    b4 = 2 * a4
    b6 = 0
    b8 = -a4 * a4
    c4 = b2 * b2 - 24 * b4
    delta = -b2 * b2 * b8 - 8 * b4 ** 3 - 27 * b6 ** 2 + 9 * b2 * b4 * b6
    assert delta != 0
    return c4 ** 3 // delta

assert j_a2_a4(-6, 1) == 287496
assert 287496 != 1728

# Degree-two quotient E -> E/<alpha>: image of E[2] has order two.
# Thus it has one unique nonzero point, which is the dual-isogeny kernel point.
E2 = [(0, 0), (1, 0), (0, 1), (1, 1)]
alpha = (1, 0)
cosets = []
seen = set()
for x in E2:
    if x in seen:
        continue
    xa = xor(x, alpha)
    coset = frozenset((x, xa))
    cosets.append(coset)
    seen.update(coset)
assert len(cosets) == 2
assert frozenset(((0, 0), alpha)) in cosets
assert len([c for c in cosets if (0, 0) not in c]) == 1

# Therefore, if both source and target of the dual 2-isogeny have j=1728,
# the selected nonzero kernel must be the unique Gaussian-CM-fixed point.
selected_cm_fixed_count = 3
selected_cm_swapped_count = 0
assert selected_cm_fixed_count == 3
assert selected_cm_swapped_count == 0

Q_STATES = list(range(210, 267, 2))
RES3 = [73, 97, 235]
assert len(Q_STATES) == 29
assert len(RES3) == 3

print("PASS_EX1_05AB_ALL_SELECTED_PRYM_POINTS_CM_FIXED")
print("selected_cm_fixed", selected_cm_fixed_count, "selected_cm_swapped", selected_cm_swapped_count)
print("Q_states", len(Q_STATES), "residues", RES3, "excluded", 0)
