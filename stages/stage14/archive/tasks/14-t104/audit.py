#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

# Regression locks: only merged theorem sources are consumed.
locks = {
    "stages/stage14/14-t103/frozen-boundary.txt": [
        "COMMON_ELEMENTARY_BOUNDARY_SKELETON_ACROSS_PRIMES_PROVED=true",
        "COMMON_ELEMENTARY_BOUNDARY_FULL_COEFFICIENTS_ACROSS_PRIMES_PROVED=false",
        "COMMON_ELEMENTARY_BOUNDARY_PRIME_AVERAGE_EXPONENT_ZERO=true",
    ],
    "stages/stage14/14-t101/result.md": [
        "CENTERED_L2_ENERGY_EQUALS_RHO_ONE_MINUS_RHO=true",
    ],
    "stages/stage14/14-tH27/result.md": [
        "CERTIFIED_BOUNDARY_SAVING_EXPONENT=0",
        "NEXT_H_NEEDED=false",
    ],
    "stages/stage14/14-Work-bjX22/result.md": [
        "COMMON_FINITE_LABEL_FREEZING_PRINCIPLE_PROVED=true",
        "TH28_NEEDED=false",
    ],
}
for rel, needles in locks.items():
    text = (ROOT / rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)


def boundary_vector(action: int, nstates: int = 8):
    # Deterministic toy full-boundary function. Equal action labels give
    # literally equal Boolean state functions; different labels may collide,
    # which only makes the action partition coarser than necessary.
    return tuple(((action + 1) * (x + 2) + x * x) % 5 in (0, 1) for x in range(nstates))


def audit_assignment(actions):
    r = len(actions)
    assert r > 0
    vectors = {a: boundary_vector(a) for a in set(actions)}
    rho_action = {
        a: Fraction(sum(vectors[a]), len(vectors[a]))
        for a in vectors
    }
    rho_p = [rho_action[a] for a in actions]
    rho_bar = sum(rho_p, Fraction(0, 1)) / r

    image = sorted(set(actions))
    K = len(image)
    assert K <= r

    W = {}
    for a in image:
        W[a] = sum(
            (rho_p[i] for i, aa in enumerate(actions) if aa == a),
            Fraction(0, 1),
        ) / r

    assert sum(W.values(), Fraction(0, 1)) == rho_bar
    a_star = max(image, key=lambda a: W[a])
    assert W[a_star] >= rho_bar / K

    n_star = sum(a == a_star for a in actions)
    frac = Fraction(n_star, r)
    rho_star = rho_action[a_star]
    assert W[a_star] == frac * rho_star
    assert frac >= W[a_star]
    assert rho_star >= W[a_star]

    # Same action means same full boundary function and same state density.
    for i, a in enumerate(actions):
        if a == a_star:
            assert boundary_vector(a) == vectors[a_star]
            assert rho_p[i] == rho_star

    # Exact Bernoulli centered energy identity for the frozen full boundary.
    vals = vectors[a_star]
    centered_energy = sum(
        (Fraction(int(v), 1) - rho_star) ** 2 for v in vals
    ) / len(vals)
    assert centered_energy == rho_star * (1 - rho_star)
    return K, W[a_star], frac, rho_star


cases = [
    [0],
    [0, 1],
    [0, 1, 2, 3],              # singleton action cells are allowed
    [0, 0, 1, 2, 2],
    [3, 3, 3, 1, 1, 0, 2],
    [0, 1, 0, 1, 2, 2, 3, 3],
]
results = [audit_assignment(c) for c in cases]

boundary = (ROOT / "stages/stage14/14-t104/frozen-boundary.txt").read_text()
for needle in [
    "FULL_PRIME_ACTION_FREEZE_PROVED=true",
    "COMMON_ELEMENTARY_BOUNDARY_FULL_COEFFICIENTS_ON_EXPONENT_ZERO_PRIME_SUBFAMILY_PROVED=true",
    "FIXED_ACTION_PRIME_FRACTION_EXPONENT_ZERO=true",
    "FIXED_FULL_BOUNDARY_STATE_DENSITY_EXPONENT_ZERO=true",
    "PRIME_ACTION_VARIATION_DISCHARGED_AS_LOCALIZATION=true",
    "TH28_NEEDED=false",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "NEXT=Stage14-t105",
]:
    assert needle in boundary, needle

print({
    "stage": "14-t104",
    "cases_checked": len(cases),
    "max_action_image": max(k for k, *_ in results),
    "action_pigeonhole_checked": True,
    "exact_mass_factorization_checked": True,
    "same_action_same_boundary_checked": True,
    "centered_energy_identity_checked": True,
    "status": "ok",
})
