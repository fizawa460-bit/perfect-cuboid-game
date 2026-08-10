#!/usr/bin/env python3
"""Stage14-t39: FI Dirichlet-symbol transfer / obstruction audit."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
T38_DATA = ROOT / "stages/stage14/data/14-t38/moving_prime_elliptic_packets.json"
OUT = ROOT / "stages/stage14/data/14-t39/fi_transfer_obstruction.json"

INTERNAL_PRIMES = (5, 13, 17, 29, 37, 41)
EXTERNAL_PRIMES = (13, 17, 29, 37, 41)
BOX = range(-6, 7)


def cmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def cnorm(z):
    return z[0] * z[0] + z[1] * z[1]


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def primary_prime_rep(p: int):
    candidates = []
    for u in range(-p, p + 1):
        for v in range(-p, p + 1):
            if u * u + v * v != p:
                continue
            if u % 2 == 0 or v % 2 != 0:
                continue
            if (u + v - 1) % 4 != 0:
                continue
            candidates.append((u, v))
    assert candidates
    # Fix one deterministic primary associate/conjugate choice.
    candidates.sort(key=lambda z: (z[1] < 0, abs(z[1]), z[0], z[1]))
    w = candidates[0]
    assert cnorm(w) == p
    assert w[0] % 2 != 0 and w[1] % 2 == 0 and (w[0] + w[1] - 1) % 4 == 0
    return w


def xi(w, z):
    q = cnorm(w)
    wz = cmul(w, z)
    return legendre(wz[0], q)


def minus_i(z):
    x, y = z
    return (y, -x)


def psi(c, z):
    cz = cmul(c, z)
    return cz[0] * cz[1]


def phi(c, z):
    return psi(c, cmul(z, z))


def natural_modulus_audit():
    psi_checks = 0
    phi_checks = 0
    unit_sign_checks = 0
    rotation_checks = 0
    reps = {}

    for q in INTERNAL_PRIMES:
        w = primary_prime_rep(q)
        reps[str(q)] = list(w)
        sign = xi(w, (0, -1))  # xi_w(-i)
        expected_sign = 1 if q % 8 == 1 else -1
        assert q % 8 in (1, 5)
        assert sign == expected_sign
        unit_sign_checks += 1

        u, v = w
        assert u % q != 0 and v % q != 0
        # FI denominator w sees Re(wz)=u*x-v*y, not the fixed x or y coordinate.
        assert v % q != 0  # determinant against x-axis
        assert u % q != 0  # determinant against y-axis
        rotation_checks += 1

        for x in BOX:
            for y in BOX:
                if x == 0 and y == 0:
                    continue
                z = (x, y)
                xiz = xi(w, z)

                lhs_psi = legendre(psi(w, z), q)
                rhs_psi = sign * (xiz ** 2)
                assert lhs_psi == rhs_psi
                psi_checks += 1

                lhs_phi = legendre(phi(w, z), q)
                rhs_phi = sign * (xiz ** 4)
                assert lhs_phi == rhs_phi
                phi_checks += 1

    assert psi_checks == 1008
    assert phi_checks == 1008
    assert unit_sign_checks == 6
    assert rotation_checks == 6
    return {
        "primary_representatives": reps,
        "psi_natural_modulus_identities": psi_checks,
        "phi_natural_modulus_identities": phi_checks,
        "unit_sign_checks": unit_sign_checks,
        "coordinate_rotation_mismatch_checks": rotation_checks,
    }


def external_nonmultiplicativity_audit():
    phi_witnesses = {
        13: ((1, 5), (1, 5)),
        17: ((1, 2), (1, 4)),
        29: ((1, 2), (1, 6)),
        37: ((1, 2), (1, 2)),
        41: ((1, 2), (1, 4)),
    }
    psi_witnesses = {
        13: ((1, 1), (1, 2)),
        17: ((1, 1), (1, 2)),
        29: ((1, 1), (1, 4)),
        37: ((1, 1), (1, 2)),
        41: ((1, 1), (1, 2)),
    }

    phi_rows = {}
    psi_rows = {}
    for lam in EXTERNAL_PRIMES:
        z1, z2 = phi_witnesses[lam]
        z12 = cmul(z1, z2)
        a1 = legendre(phi((1, 0), z1), lam)
        a2 = legendre(phi((1, 0), z2), lam)
        a12 = legendre(phi((1, 0), z12), lam)
        assert 0 not in (a1, a2, a12)
        assert a12 != a1 * a2
        phi_rows[str(lam)] = {
            "z1": list(z1), "z2": list(z2), "z1z2": list(z12),
            "A_z1": a1, "A_z2": a2, "A_z1z2": a12,
        }

        z1, z2 = psi_witnesses[lam]
        z12 = cmul(z1, z2)
        a1 = legendre(psi((1, 0), z1), lam)
        a2 = legendre(psi((1, 0), z2), lam)
        a12 = legendre(psi((1, 0), z12), lam)
        assert 0 not in (a1, a2, a12)
        assert a12 != a1 * a2
        psi_rows[str(lam)] = {
            "z1": list(z1), "z2": list(z2), "z1z2": list(z12),
            "A_z1": a1, "A_z2": a2, "A_z1z2": a12,
        }

    assert len(phi_rows) == 5 and len(psi_rows) == 5
    return {
        "phi_nonmultiplicativity_witnesses": phi_rows,
        "psi_nonmultiplicativity_witnesses": psi_rows,
    }


def exponent_audit():
    trivial = Fraction(2, 1)
    fi = Fraction(23, 12)
    saving = trivial - fi
    assert saving == Fraction(1, 12)
    return {
        "balanced_trivial_exponent_X": str(trivial),
        "balanced_FI_prop_21_3_exponent_X": str(fi),
        "formal_balanced_saving_X": str(saving),
        "formal_balanced_saving_if_X_equals_sqrtB": "B^(-1/24)",
    }


def main():
    frozen38 = json.loads(T38_DATA.read_text())
    assert frozen38["decision"]["STAGE14_T38"] == (
        "COMPLETE_MOVING_PRIME_ELLIPTIC_PACKET_BOUND_AND_CRITICAL_STRIP_REDUCTION"
    )
    assert frozen38["decision"]["CRITICAL_SQRT_ELL_STRIP_REMAINS"] is True
    assert frozen38["decision"]["STAGE14_PACKET_EQUALS_FI_JACOBI_KUBOTA_SPIN"] is False

    natural = natural_modulus_audit()
    external = external_nonmultiplicativity_audit()
    exponents = exponent_audit()

    report = {
        "stage": "14-t39",
        "t38_frozen_reference": {
            "moving_factorization_checks": 1120,
            "critical_sqrt_ell_strip_remains": True,
            "global_super_sqrt_packet_bound": "B^(1/2+o(1))",
        },
        "fi_primary_source_interface": {
            "dirichlet_symbol": "xi_w(z)=(z/w)=Jacobi(Re(w*z),N(w)) for primary primitive w",
            "reciprocity": "(z/w)=(w/z) for primary primitive w,z",
            "bilinear_form": "Q(M,N)=sum_w^* sum_z alpha_w beta_z (z/w)",
            "proposition_21_3": "Q(M,N)<<(M+N)^(1/12)*(M*N)^(11/12+epsilon)",
            "jacobi_kubota_multiplier": "[wz]=epsilon*[w]*[z]*(z/w)",
        },
        "natural_modulus": natural,
        "external_auxiliary": external,
        "balanced_exponents": exponents,
        "transfer_dichotomy": {
            "internal_modulus": (
                "using the Stage14 Gaussian coefficient as the FI denominator makes "
                "chi_Nw(Psi_w(z)) and chi_Nw(Phi_w(z)) constant-or-zero in z"
            ),
            "external_modulus": (
                "keeping an independent split auxiliary prime preserves a nontrivial quartic trace, "
                "but that trace is nonmultiplicative in the moving Gaussian variable"
            ),
            "root_rotation": (
                "FI sees Re(varpi*z)=u*x-v*y; converting fixed Stage14 coordinate factors requires "
                "a varpi-dependent rotation and destroys separated bilinear coefficients"
            ),
            "surviving_object": (
                "T=sum_varpi sum_pi sum_gamma a_varpi b_pi c_gamma "
                "chi_{N(varpi)}(P_gamma(pi))"
            ),
        },
        "decision": {
            "STAGE14_T39": "COMPLETE_FI_TRANSFER_AUDIT_AND_EXTERNAL_AUXILIARY_TRILINEAR_BOUNDARY",
            "FI_DIRICHLET_SYMBOL_DEFINITION_MATCHED": True,
            "FI_PROPOSITION_21_3_BALANCED_POWER_SAVING_AVAILABLE": True,
            "NATURAL_MODULUS_PSI_TRACE": "CONSTANT_OR_ZERO",
            "NATURAL_MODULUS_PHI_TRACE": "CONSTANT_OR_ZERO",
            "EXTERNAL_AUXILIARY_PSI_TRACE_MULTIPLICATIVE": False,
            "EXTERNAL_AUXILIARY_PHI_TRACE_MULTIPLICATIVE": False,
            "AUXILIARY_ROOT_ROTATION_PRESERVES_SEPARATED_COEFFICIENTS": False,
            "DIRECT_TWO_VARIABLE_FI_TRANSFER_VALID": False,
            "EXTERNAL_AUXILIARY_THIRD_VARIABLE_ESSENTIAL": True,
            "CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED": False,
            "CANONICAL_PRIME_SUM_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "NEXT": (
                "Stage14-t40 build an external-auxiliary trilinear dispersion inequality for "
                "T=sum_varpi,sum_pi,sum_gamma chi_{N(varpi)}(P_gamma(pi)); after one Cauchy/differencing "
                "step, test whether the surviving cross-kernel becomes a genuine Gaussian Dirichlet symbol "
                "to which FI Proposition 21.3 or a quadratic-Hecke large sieve applies"
            ),
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "natural_modulus": natural,
        "external_auxiliary": external,
        "balanced_exponents": exponents,
    }, indent=2, sort_keys=True))
    print(json.dumps(report["decision"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
