#!/usr/bin/env python3
"""Stage14-t38: moving canonical-prime elliptic-packet audit."""

from __future__ import annotations

from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T37_DATA = ROOT / "stages/stage14/data/14-t37/common_core_fixed_ell_saving.json"
OUT = ROOT / "stages/stage14/data/14-t38/moving_prime_elliptic_packets.json"

UNITS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def cmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def cbar(z):
    return (z[0], -z[1])


def cnorm(z):
    return z[0] * z[0] + z[1] * z[1]


def gdiv_exact(z, w):
    den = cnorm(w)
    num = cmul(z, cbar(w))
    assert den > 0 and num[0] % den == 0 and num[1] % den == 0
    return (num[0] // den, num[1] // den)


def psi(c, z):
    cz = cmul(c, z)
    return cz[0] * cz[1]


def phi(c, z):
    return psi(c, cmul(z, z))


def unit_associate(target, base):
    for u in UNITS:
        if cmul(u, base) == target:
            return u
    return None


def line_coeffs(c):
    x, y = c
    # Re(c(r+is))=(x r-y s), Im(c(r+is))=(y r+x s).
    return ((x, -y), (y, x))


def det(v, w):
    return v[0] * w[1] - v[1] * w[0]


def audit_state(state):
    A = (state["a"], state["b"])
    P = (state["p"], state["q"])
    U = tuple(state["U"])
    V = tuple(state["V"])
    ell = state["ell"]
    F = state["F"]

    pi = gdiv_exact(A, U)
    assert cnorm(pi) == ell

    if state["branch"] == "invisible":
        assert P == V
        C1 = cmul(U, cbar(V))
        C2 = cmul(U, V)
        rhs = -psi(C1, pi) * psi(C2, pi)
        assert F == rhs

        # The four rational linear factors in the moving slope are distinct.
        # A shared factor between psi(C1,pi) and psi(C2,pi) would force
        # V/bar(V) to be real or purely imaginary, i.e. pq=0 or p^2=q^2,
        # both excluded by the physical primitive non-torsion state.
        lines = line_coeffs(C1) + line_coeffs(C2)
        assert all(det(lines[i], lines[j]) != 0 for i in range(4) for j in range(i + 1, 4))
        return "invisible"

    eta = gdiv_exact(P, V)
    assert cnorm(eta) == ell

    u_same = unit_associate(eta, pi)
    u_opp = unit_associate(eta, cbar(pi))
    assert (u_same is None) != (u_opp is None)

    if u_same is not None:
        # Absorb the unit into V so P=pi*Vt exactly.
        Vt = cmul(u_same, V)
        assert cmul(pi, Vt) == P
        C1 = cmul(U, cbar(Vt))
        C2 = cmul(U, Vt)
        rhs = -(ell * ell) * psi(C1, (1, 0)) * phi(C2, pi)
        assert F == rhs
        # phi(C2,pi) is a product of two nondegenerate rational quadratics.
        assert cnorm(C2) > 0
        return "visible_same"

    Vt = cmul(u_opp, V)
    assert cmul(cbar(pi), Vt) == P
    C1 = cmul(U, cbar(Vt))
    C2 = cmul(U, Vt)
    rhs = -(ell * ell) * psi(C2, (1, 0)) * phi(C1, pi)
    assert F == rhs
    assert cnorm(C1) > 0
    return "visible_opposite"


def main():
    frozen37 = json.loads(T37_DATA.read_text())
    assert frozen37["decision"]["STAGE14_T37"] == (
        "COMPLETE_COMMON_CORE_SPIN_FACTORIZATION_AND_FIXED_ELL_POWER_SAVING"
    )
    assert frozen37["decision"]["FIXED_ELL_NORM_INDEX_POWER_SAVING_PROVED"] is True
    assert frozen37["decision"]["CANONICAL_PRIME_SUM_POWER_SAVING_PROVED"] is False

    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    states = t36["build_frozen_states"]()
    assert len(states) == 1120

    modes = {"visible_same": 0, "visible_opposite": 0, "invisible": 0}
    for state in states:
        modes[audit_state(state)] += 1

    assert modes["visible_same"] + modes["visible_opposite"] == 282
    assert modes["invisible"] == 838

    report = {
        "stage": "14-t38",
        "t37_frozen_reference": {
            "states": 1120,
            "fixed_ell_power_saving": True,
            "fixed_ell_uniform_bound": "(B/ell)^(5/6)*B^o(1)",
        },
        "moving_prime_factorization": {
            "invisible": (
                "for A=pi*U and P=V, F=-Psi_{U*bar(V)}(pi)*Psi_{U*V}(pi), "
                "Psi_c(z)=Re(cz)Im(cz)"
            ),
            "visible_same": (
                "after a Gaussian-unit normalization P=pi*V, "
                "F=-ell^2*Psi_{U*bar(V)}(1)*Phi_{U*V}(pi)"
            ),
            "visible_opposite": (
                "after a Gaussian-unit normalization P=bar(pi)*V, "
                "F=-ell^2*Psi_{U*V}(1)*Phi_{U*bar(V)}(pi)"
            ),
            "Phi": "Phi_c(z)=Re(c*z^2)Im(c*z^2)",
            "Psi": "Psi_c(z)=Re(c*z)Im(c*z)",
            "moving_target_curve": (
                "visible: Y^2=C*Phi_c(pi); invisible: Y^2=C*Psi_c(pi)*Psi_d(pi)"
            ),
            "visible_curve": "smooth genus one; product of two rational quadratics, hence rational 2-torsion",
            "invisible_curve": "smooth genus one on physical non-torsion states; four distinct rational linear branch factors",
        },
        "moving_packet_bound": {
            "per_fixed_descended_packet": "B^o(1) moving Gaussian-prime slopes by the t22 bounded-height mechanism",
            "cofactor_budget": "Y=max(m*delta)<sqrt(B) in the super-sqrt branch",
            "packet_count": "<=Y*B^o(1) from k|epsilon*m and r_2(n),tau(n)=n^o(1)",
            "global_super_sqrt_bound": "B^(1/2+o(1))",
            "large_ell_range": (
                "for every fixed eta>0, ell>=B^(1/2+eta) contributes "
                "O(B^(1/2-eta+o(1)))"
            ),
        },
        "friedlander_iwaniec_boundary": {
            "degree_two_gaussian_spin_theorem_exists": True,
            "prime_spin_bound": "sum_{N(pi)<=x} spin(pi) << x^(76/77)",
            "fixed_sector_and_progression_allowed": True,
            "jacobi_kubota_multiplier": "[wz]=epsilon*[w]*[z]*(z/w)",
            "dirichlet_symbol_bilinear_forms_available": True,
            "stage14_moving_packet_is_single_FI_spin": False,
            "reason": (
                "Stage14 is a quartic squareclass/auxiliary trace in the coordinates of pi; "
                "it is not the Jacobi-Kubota symbol [pi] nor the quadratic eigenvalue lambda(N(pi))"
            ),
        },
        "finite_audit": {
            "moving_factorization_checks": len(states),
            "visible_checks": modes["visible_same"] + modes["visible_opposite"],
            "invisible_distinct_linear_factor_checks": modes["invisible"],
            "mode_counts": modes,
        },
        "decision": {
            "STAGE14_T38": "COMPLETE_MOVING_PRIME_ELLIPTIC_PACKET_BOUND_AND_CRITICAL_STRIP_REDUCTION",
            "CLASSICAL_QI_GAUSSIAN_SPIN_THEOREM_IDENTIFIED": True,
            "GENERAL_DEGREE_GE3_SPIN_THEOREM_NEEDED": False,
            "STAGE14_PACKET_EQUALS_FI_JACOBI_KUBOTA_SPIN": False,
            "MOVING_PRIME_PACKET_FACTORIZATION_EXACT": True,
            "MOVING_PRIME_TARGET_CURVE_GENUS_ONE": True,
            "MOVING_PRIME_PACKET_MULTIPLICITY": "B^o(1)",
            "GLOBAL_SUPER_SQRT_PACKET_BOUND": "B^(1/2+o(1))",
            "LARGE_ELL_AWAY_FROM_SQRT_POWER_SAVING_PROVED": True,
            "CRITICAL_SQRT_ELL_STRIP_REMAINS": True,
            "CANONICAL_PRIME_SUM_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "NEXT": (
                "Stage14-t39 treat the critical ell=B^(1/2+o(1)) strip by converting the Stage14 "
                "quartic square-sieve correlations into a genuine Gaussian Dirichlet-symbol Type-I/II "
                "bilinear form of the Friedlander-Iwaniec kind, or prove the exact obstruction to that transfer"
            ),
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["finite_audit"], indent=2, sort_keys=True))
    print(json.dumps(report["decision"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
