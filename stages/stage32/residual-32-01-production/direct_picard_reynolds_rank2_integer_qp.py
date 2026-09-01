#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass

from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_decomp

from direct_picard_orbit_sum_qp_bound import DirectPicardOrbitSumQPBound
from direct_picard_reynolds_lattice_diagnostic import (
    EXPECTED_FIXED_RANK,
    GROUP_ORDER,
    PICARD_RANK,
    exact_column_lattice_basis_lowrank,
)
from direct_picard_reynolds_rank2_integral_projection_bound import (
    build_reynolds_numerator,
)
from hperp_integral_adapter import HperpIntegralPairingAdapter


EXPECTED_INTEGER_FREE_RANK = 2
EXPECTED_PROJECTED_SLICE_SMITH = (1, 2, 2)
EXPECTED_DISTINCT_FIXED_HALFSPACE_COUNT = 12
EXPECTED_RANK2_HESSIAN_DET = 1310720
OBJECTIVE_DENOMINATOR = GROUP_ORDER * GROUP_ORDER


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def matrix_int_list(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def dot(a: tuple[int, ...], b: tuple[int, ...]) -> int:
    return sum(x * y for x, y in zip(a, b))


def mat_vec(m: tuple[tuple[int, ...], ...], v: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(dot(row, v) for row in m)


def quad(m: tuple[tuple[int, ...], ...], v: tuple[int, ...]) -> int:
    return dot(v, mat_vec(m, v))


def ceil_div(a: int, b: int) -> int:
    if b <= 0:
        raise ValueError("ceil_div requires positive denominator")
    return -((-a) // b)


def integer_nonnegative_interval(a: int, b: int, c: int) -> tuple[int, int] | None:
    """Exact integer n interval where a*n^2+b*n+c >= 0 for a<0.

    Concavity makes the integer solution set contiguous. We locate one exact
    nonnegative central integer, then find both sign changes by exponential
    bracketing and integer binary search. No floating-point root arithmetic is
    used.
    """
    if a >= 0:
        raise ValueError("expected a strictly concave quadratic")

    den = -2 * a
    floor_vertex = b // den
    central = (floor_vertex, floor_vertex + 1)

    def p(n: int) -> int:
        return a * n * n + b * n + c

    seed = max(central, key=p)
    if p(seed) < 0:
        return None

    step = 1
    left_bad = seed - step
    while p(left_bad) >= 0:
        step *= 2
        left_bad = seed - step
    left_good = seed
    while left_good - left_bad > 1:
        mid = (left_bad + left_good) // 2
        if p(mid) >= 0:
            left_good = mid
        else:
            left_bad = mid

    step = 1
    right_bad = seed + step
    while p(right_bad) >= 0:
        step *= 2
        right_bad = seed + step
    right_good = seed
    while right_bad - right_good > 1:
        mid = (right_good + right_bad) // 2
        if p(mid) >= 0:
            right_good = mid
        else:
            right_bad = mid

    return left_good, right_good


def _interval_selftest() -> None:
    tests = [
        (-1, 0, 0),
        (-1, 0, 9),
        (-3, 7, 11),
        (-8, -13, 29),
        (-5, 100, -123),
    ]
    for a, b, c in tests:
        got = integer_nonnegative_interval(a, b, c)
        brute = [n for n in range(-200, 201) if a * n * n + b * n + c >= 0]
        expected = None if not brute else (min(brute), max(brute))
        if got != expected:
            raise ValueError(
                f"integer concave interval selftest failed: {(a,b,c)} got={got} expected={expected}"
            )


@dataclass(frozen=True)
class ReynoldsRank2IntegerQP:
    orbit_qp: DirectPicardOrbitSumQPBound
    smith_diagonal_signed: tuple[int, int, int]
    smith_left: tuple[tuple[int, ...], ...]
    smith_right: tuple[tuple[int, ...], ...]
    kernel_columns: tuple[tuple[int, ...], tuple[int, ...]]
    hessian: tuple[tuple[int, ...], ...]
    fixed_halfspace_rows: tuple[tuple[int, ...], ...]
    kernel_h0: tuple[int, ...]
    kernel_h1: tuple[int, ...]
    objective_uu: int
    objective_uv_twice: int
    objective_vv: int
    halfspace_u: tuple[int, ...]
    halfspace_v: tuple[int, ...]
    certificate: dict

    @property
    def bound(self):
        return self.orbit_qp.bound

    @property
    def bridge(self):
        return self.orbit_qp.bound.bridge

    def affine_origin(self, d: int, e: int, a: int) -> tuple[int, ...] | None:
        t = (int(d), int(e), int(a))
        st = tuple(
            sum(self.smith_left[i][j] * t[j] for j in range(3))
            for i in range(3)
        )
        y = []
        for value, diag in zip(st, self.smith_diagonal_signed):
            if value % diag:
                return None
            y.append(value // diag)
        return tuple(
            sum(self.smith_right[row][j] * y[j] for j in range(3))
            for row in range(EXPECTED_FIXED_RANK)
        )

    def can_reach_selfsq(
        self, d: int, e: int, a: int, lower: int
    ) -> tuple[bool, str, int, tuple[int, int] | None]:
        """Exact decision for the projected integral rank-2 relaxation.

        Returns (survives, reason, checked_u_count, witness_uv). If False, the
        original integral Picard slice is impossible because every integral x
        projects to one of these p and x^2 <= p^2. If True, this is only a
        surviving necessary condition; anti-fixed lift/integrality remains.
        """
        z0 = self.affine_origin(d, e, a)
        if z0 is None:
            return False, "PROJECTED_SLICE_NOT_IN_INTEGER_IMAGE", 0, None

        k0, k1 = self.kernel_columns
        dlin = 2 * dot(z0, self.kernel_h0)
        elin = 2 * dot(z0, self.kernel_h1)
        fconst = quad(self.hessian, z0) - int(lower) * OBJECTIVE_DENOMINATOR

        # q(u,v) = A u^2 + B uv + C v^2 + D u + E v + F.
        A = self.objective_uu
        B = self.objective_uv_twice
        C = self.objective_vv
        D = dlin
        E = elin
        F = fconst
        if not (A < 0 and C < 0 and 4 * A * C - B * B > 0):
            raise ValueError("rank2 objective lost strict concavity")

        # For fixed u, q>=0 has a real v iff its v-discriminant is >=0.
        # This discriminant is itself a strictly concave integral quadratic in u.
        delta2 = B * B - 4 * C * A
        delta1 = 2 * B * E - 4 * C * D
        delta0 = E * E - 4 * C * F
        urange = integer_nonnegative_interval(delta2, delta1, delta0)
        if urange is None:
            return False, "PROJECTED_CONTINUOUS_SELF_INTERSECTION_TOO_LOW", 0, None

        gammas = tuple(dot(row, z0) for row in self.fixed_halfspace_rows)
        u_lo, u_hi = urange
        # Visit the discriminant vertex first so surviving slices usually exit
        # quickly, while negative decisions still exhaust the exact finite set.
        center_den = -2 * delta2
        center_floor = delta1 // center_den
        center = min(max(center_floor, u_lo), u_hi)
        checked = 0

        def try_u(u: int) -> tuple[bool, tuple[int, int] | None]:
            nonlocal checked
            checked += 1
            v_lo: int | None = None
            v_hi: int | None = None
            for alpha, beta, gamma in zip(
                self.halfspace_u, self.halfspace_v, gammas
            ):
                s = alpha * u + gamma
                if beta > 0:
                    bound = ceil_div(-s, beta)
                    v_lo = bound if v_lo is None else max(v_lo, bound)
                elif beta < 0:
                    bound = (s // (-beta))
                    v_hi = bound if v_hi is None else min(v_hi, bound)
                elif s < 0:
                    return False, None
                if v_lo is not None and v_hi is not None and v_lo > v_hi:
                    return False, None

            linear_v = B * u + E
            const_v = A * u * u + D * u + F
            vertex_den = -2 * C
            vf = linear_v // vertex_den
            candidates = {vf, vf + 1}
            if v_lo is not None:
                candidates.add(v_lo)
            if v_hi is not None:
                candidates.add(v_hi)

            for v in tuple(candidates):
                if v_lo is not None and v < v_lo:
                    v = v_lo
                if v_hi is not None and v > v_hi:
                    v = v_hi
                if v_lo is not None and v_hi is not None and v_lo > v_hi:
                    continue
                q = C * v * v + linear_v * v + const_v
                if q >= 0:
                    return True, (u, v)
            return False, None

        ok, witness = try_u(center)
        if ok:
            return True, "PROJECTED_RANK2_INTEGER_QP_SURVIVES", checked, witness
        step = 1
        while center - step >= u_lo or center + step <= u_hi:
            if center - step >= u_lo:
                ok, witness = try_u(center - step)
                if ok:
                    return True, "PROJECTED_RANK2_INTEGER_QP_SURVIVES", checked, witness
            if center + step <= u_hi:
                ok, witness = try_u(center + step)
                if ok:
                    return True, "PROJECTED_RANK2_INTEGER_QP_SURVIVES", checked, witness
            step += 1

        return False, "PROJECTED_RANK2_INTEGER_QP_EXHAUSTED", checked, None

    @classmethod
    def from_retained(cls, marking: dict, bundle: dict) -> "ReynoldsRank2IntegerQP":
        _interval_selftest()
        orbit_qp = DirectPicardOrbitSumQPBound.from_retained(marking, bundle)
        adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
        bridge = orbit_qp.bound.bridge
        gram = Matrix(bundle["picard_gram_64x64"])
        phi = Matrix([
            list(bridge.degree_functional),
            list(bridge.exceptional_mass_functional),
            list(bridge.first_normal_half_functional),
        ])
        if int(phi.rank()) != 3:
            raise ValueError("slice functional rank regression")

        N, subgroup, action_hashes_sha = build_reynolds_numerator(
            marking, adapter, gram, phi
        )
        Bmat, module_stats = exact_column_lattice_basis_lowrank(
            N, EXPECTED_FIXED_RANK
        )
        if Bmat.shape != (PICARD_RANK, EXPECTED_FIXED_RANK):
            raise ValueError(f"fixed image basis shape regression: {Bmat.shape}")

        phi_B = phi * Bmat
        if any(int(v) % GROUP_ORDER for v in phi_B):
            raise ValueError("phi(B) divisibility regression")
        Psi = phi_B.applyfunc(lambda v: int(v) // GROUP_ORDER)
        Dmat, Smat, Tmat = smith_normal_decomp(Psi, domain=ZZ)
        if Smat * Psi * Tmat != Dmat:
            raise ValueError("projected slice Smith decomposition regression")
        if abs(int(Smat.det())) != 1 or abs(int(Tmat.det())) != 1:
            raise ValueError("projected Smith transforms are not unimodular")
        signed_diag = tuple(int(Dmat[i, i]) for i in range(3))
        abs_diag = tuple(abs(v) for v in signed_diag)
        if abs_diag != EXPECTED_PROJECTED_SLICE_SMITH:
            raise ValueError(f"projected Smith regression: {abs_diag}")

        kernel = Tmat[:, 3:]
        if kernel.shape != (EXPECTED_FIXED_RANK, EXPECTED_INTEGER_FREE_RANK):
            raise ValueError(f"integer kernel shape regression: {kernel.shape}")
        if Psi * kernel != Matrix.zeros(3, EXPECTED_INTEGER_FREE_RANK):
            raise ValueError("integer kernel regression")

        Hmat = Bmat.T * gram * Bmat
        reduced = kernel.T * Hmat * kernel
        if reduced.shape != (2, 2) or reduced != reduced.T:
            raise ValueError("rank2 Hessian shape/symmetry regression")
        if int(reduced.det()) != EXPECTED_RANK2_HESSIAN_DET:
            raise ValueError(f"rank2 Hessian determinant regression: {reduced.det()}")
        if not (int(reduced[0, 0]) < 0 and int(reduced.det()) > 0):
            raise ValueError("rank2 Hessian is not negative definite")

        pairing_B = adapter.pairing_matrix * Bmat
        distinct_rows = tuple(sorted({
            tuple(int(pairing_B[i, j]) for j in range(EXPECTED_FIXED_RANK))
            for i in range(pairing_B.rows)
        }))
        if len(distinct_rows) != EXPECTED_DISTINCT_FIXED_HALFSPACE_COUNT:
            raise ValueError(
                f"fixed halfspace regression: {len(distinct_rows)} != "
                f"{EXPECTED_DISTINCT_FIXED_HALFSPACE_COUNT}"
            )

        # Recheck that each of the 14 actual stabilizer orbits is constant,
        # while allowing distinct orbits to induce the same fixed halfspace.
        unvisited = set(range(140))
        orbit_sizes = []
        while unvisited:
            seed = min(unvisited)
            orbit = tuple(sorted({g[seed] for g in subgroup}))
            base = tuple(int(pairing_B[seed, j]) for j in range(EXPECTED_FIXED_RANK))
            if any(
                tuple(int(pairing_B[i, j]) for j in range(EXPECTED_FIXED_RANK)) != base
                for i in orbit
            ):
                raise ValueError("fixed pairing row not constant on stabilizer orbit")
            orbit_sizes.append(len(orbit))
            unvisited.difference_update(orbit)
        if len(orbit_sizes) != 14:
            raise ValueError(f"stabilizer orbit count regression: {len(orbit_sizes)}")

        H = tuple(tuple(int(Hmat[i, j]) for j in range(5)) for i in range(5))
        S = tuple(tuple(int(Smat[i, j]) for j in range(3)) for i in range(3))
        T = tuple(tuple(int(Tmat[i, j]) for j in range(5)) for i in range(5))
        k0 = tuple(int(kernel[i, 0]) for i in range(5))
        k1 = tuple(int(kernel[i, 1]) for i in range(5))
        hk0 = mat_vec(H, k0)
        hk1 = mat_vec(H, k1)
        obj_uu = dot(k0, hk0)
        obj_uv2 = 2 * dot(k0, hk1)
        obj_vv = dot(k1, hk1)
        half_u = tuple(dot(row, k0) for row in distinct_rows)
        half_v = tuple(dot(row, k1) for row in distinct_rows)

        cert = {
            "schema": "STAGE32_RESIDUAL32_01_REYNOLDS_RANK2_EXACT_INTEGER_QP_MODEL_V1",
            "mode": "EXACT_2D_INTEGER_CONCAVE_QP_DECISION_ON_PROJECTED_INTEGRAL_PICARD_LATTICE",
            "slice_stabilizer_group_order": GROUP_ORDER,
            "fixed_rank": EXPECTED_FIXED_RANK,
            "slice_rank": 3,
            "integer_free_rank": EXPECTED_INTEGER_FREE_RANK,
            "projected_slice_smith_abs": list(abs_diag),
            "projected_slice_smith_signed": list(signed_diag),
            "smith_left_sha256": csha(matrix_int_list(Smat)),
            "smith_right_sha256": csha(matrix_int_list(Tmat)),
            "fixed_image_basis_sha256": csha(matrix_int_list(Bmat)),
            "fixed_image_column_module_stats": module_stats,
            "reynolds_numerator_sha256": csha(matrix_int_list(N)),
            "action_hashes_sha256": action_hashes_sha,
            "objective_denominator": OBJECTIVE_DENOMINATOR,
            "rank2_hessian": matrix_int_list(reduced),
            "rank2_hessian_det": int(reduced.det()),
            "rank2_hessian_negative_definite": True,
            "stabilizer_orbit_count": len(orbit_sizes),
            "stabilizer_orbit_sizes": sorted(orbit_sizes),
            "distinct_fixed_halfspace_count": len(distinct_rows),
            "distinct_fixed_halfspace_rows": [list(row) for row in distinct_rows],
            "algorithm": {
                "slice_affine_lattice": "Smith exact z=z0+K(u,v), u,v in Z",
                "threshold_region": "exact q(u,v)>=0 ellipse from x^2<=p^2 and p^2 threshold",
                "u_envelope": "exact integer interval from v-discriminant using exponential bracket plus integer binary search",
                "v_feasibility": "exact integer interval from all 12 fixed halfspaces",
                "fixed_u_objective": "strictly concave integer quadratic; test nearest integer(s) to exact rational vertex clamped to feasible interval",
                "floating_point_used": False,
                "false_result_exhausts_all_integer_u_in_threshold_ellipse": True,
            },
            "safe_semantics": {
                "projected_integrality_exact": True,
                "all140_nonnegative_original_implies_fixed_halfspaces": True,
                "original_self_square_le_projected_self_square": True,
                "false_decision_prunes_original_integral_slice": True,
                "true_decision_is_only_necessary_condition": True,
                "anti_fixed_lift_not_solved": True,
            },
            "numerical_row_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        }
        cert["canonical_sha256_without_this_field"] = csha(cert)

        return cls(
            orbit_qp=orbit_qp,
            smith_diagonal_signed=signed_diag,
            smith_left=S,
            smith_right=T,
            kernel_columns=(k0, k1),
            hessian=H,
            fixed_halfspace_rows=distinct_rows,
            kernel_h0=hk0,
            kernel_h1=hk1,
            objective_uu=obj_uu,
            objective_uv_twice=obj_uv2,
            objective_vv=obj_vv,
            halfspace_u=half_u,
            halfspace_v=half_v,
            certificate=cert,
        )
