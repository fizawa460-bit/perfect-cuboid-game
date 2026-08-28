#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass
from typing import Iterable, Sequence

import sympy
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form

from pairing_prefix_engine import INDLIST, close_permutation_group

KNOWN_CURVE_COUNT = 140
PICARD_RANK = 64
NORMAL_LABEL_MAX = 92
EXPECTED_AUT_GROUP_ORDER = 1536


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def matrix_list(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def _to_int(value: object) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return int(value)
    if isinstance(value, str):
        try:
            q = sympy.Rational(value)
        except Exception:
            return None
        if q.q == 1:
            return int(q)
    return None


def _coerce_rectangular(obj: list) -> Matrix | None:
    if not obj or not all(isinstance(r, list) for r in obj):
        return None
    widths = {len(r) for r in obj}
    if len(widths) != 1:
        return None
    rows = len(obj)
    cols = next(iter(widths))
    if (rows, cols) not in (
        (KNOWN_CURVE_COUNT, PICARD_RANK),
        (PICARD_RANK, KNOWN_CURVE_COUNT),
        (KNOWN_CURVE_COUNT, KNOWN_CURVE_COUNT),
    ):
        return None
    vals: list[list[int]] = []
    for row in obj:
        out: list[int] = []
        for value in row:
            iv = _to_int(value)
            if iv is None:
                return None
            out.append(iv)
        vals.append(out)
    return Matrix(vals)


def _dict_label_matrix(obj: dict) -> Matrix | None:
    expected = {str(i) for i in range(1, KNOWN_CURVE_COUNT + 1)}
    if set(obj) != expected:
        return None
    rows: list[list[int]] = []
    for i in range(1, KNOWN_CURVE_COUNT + 1):
        row = obj[str(i)]
        if not isinstance(row, list) or len(row) != PICARD_RANK:
            return None
        vals: list[int] = []
        for value in row:
            iv = _to_int(value)
            if iv is None:
                return None
            vals.append(iv)
        rows.append(vals)
    return Matrix(rows)


def _pairing_matrix_candidates(obj: object, path: str = "$") -> Iterable[tuple[str, str, Matrix]]:
    if isinstance(obj, dict):
        keyed = _dict_label_matrix(obj)
        if keyed is not None:
            yield path, "LABEL_DICT_140x64", keyed
        for key, value in obj.items():
            yield from _pairing_matrix_candidates(value, f"{path}.{key}")
        return
    if not isinstance(obj, list) or not obj:
        return

    raw = _coerce_rectangular(obj)
    if raw is not None:
        if raw.shape == (KNOWN_CURVE_COUNT, PICARD_RANK):
            yield path, "ARRAY_140x64", raw
        elif raw.shape == (PICARD_RANK, KNOWN_CURVE_COUNT):
            yield path, "ARRAY_64x140_TRANSPOSED", raw.T
        elif raw.shape == (KNOWN_CURVE_COUNT, KNOWN_CURVE_COUNT):
            cols = [i - 1 for i in INDLIST]
            yield path, "FULL_INTERSECTION_140x140_BASIS_COLUMNS", raw[:, cols]

    for i, value in enumerate(obj):
        if isinstance(value, (dict, list)):
            yield from _pairing_matrix_candidates(value, f"{path}[{i}]")


def _propagate_full_pairing_from_basis_gram(marking: dict, gram: Matrix) -> tuple[Matrix, dict]:
    """Reconstruct the 140x140 intersection pairing by exact Aut invariance.

    Stoll's source defines the 140 classes as 92 known curves followed by 48
    exceptional divisors and the retained Aut permutations act on exactly this
    ordered set.  The retained primitive-basis Gram supplies <a,b> for all
    a,b in INDLIST.  Since every retained Aut element is an exact Picard
    isometry, <g(a),g(b)>=<a,b>.  We propagate these 4096 values through the
    full 1536-element group and fail closed unless every ordered pair is covered
    with no conflicting value.
    """
    aut_payload = marking.get("aut_action")
    if not isinstance(aut_payload, dict):
        raise ValueError("retained marking missing aut_action")
    generators = aut_payload.get("permutations_1based")
    if not isinstance(generators, list) or not generators:
        raise ValueError("retained marking missing Aut permutations")
    group = close_permutation_group(generators)
    if len(group) != EXPECTED_AUT_GROUP_ORDER:
        raise ValueError(f"retained Aut group order regression: {len(group)}")
    if any(len(g) != KNOWN_CURVE_COUNT for g in group):
        raise ValueError("retained Aut permutation degree regression")

    basis = [i - 1 for i in INDLIST]
    known: dict[tuple[int, int], int] = {}
    conflicts: list[dict] = []
    for bi, a in enumerate(basis):
        for bj, b in enumerate(basis):
            value = int(gram[bi, bj])
            for g in group:
                key = (g[a], g[b])
                prior = known.get(key)
                if prior is not None and prior != value:
                    conflicts.append({
                        "pair_1based": [key[0] + 1, key[1] + 1],
                        "prior": prior,
                        "new": value,
                        "basis_pair_1based": [a + 1, b + 1],
                    })
                    if len(conflicts) >= 8:
                        break
                else:
                    known[key] = value
            if conflicts:
                break
        if conflicts:
            break
    if conflicts:
        raise ValueError(f"Aut orbit propagation conflict: {conflicts}")

    expected = KNOWN_CURVE_COUNT * KNOWN_CURVE_COUNT
    if len(known) != expected:
        uncovered = [
            [i + 1, j + 1]
            for i in range(KNOWN_CURVE_COUNT)
            for j in range(KNOWN_CURVE_COUNT)
            if (i, j) not in known
        ]
        raise ValueError(
            "Aut orbit propagation incomplete: "
            f"covered={len(known)}/{expected}; uncovered_sample={uncovered[:40]}"
        )

    full = Matrix(
        KNOWN_CURVE_COUNT,
        KNOWN_CURVE_COUNT,
        lambda i, j: known[(i, j)],
    )
    if full != full.T:
        raise ValueError("reconstructed all140 pairing is not symmetric")
    basis_sub = full.extract(basis, basis)
    if basis_sub != gram:
        raise ValueError("reconstructed basis Gram regression")

    # Avoid a second expensive symbolic rank computation: the exact retained
    # 64x64 Gram is nonsingular, so full rank is at least 64; all 140 columns
    # pair through the same Picard rank-64 lattice by construction.  The
    # adapter only consumes the 140x64 basis-column image below.
    pairing = full[:, basis]
    cert = {
        "mode": "AUT_ORBIT_PROPAGATION_FROM_RETAINED_BASIS_GRAM",
        "full_aut_group_order": len(group),
        "seed_basis_pair_count": PICARD_RANK * PICARD_RANK,
        "covered_ordered_pair_count": len(known),
        "expected_ordered_pair_count": expected,
        "coverage_complete": True,
        "conflict_count": 0,
        "full_pairing_sha256": csha(matrix_list(full)),
        "pairing_to_basis_sha256": csha(matrix_list(pairing)),
        "basis_gram_regression_exact": True,
    }
    cert["canonical_sha256_without_this_field"] = csha(cert)
    return pairing, cert


@dataclass(frozen=True)
class AutEquivariantPairingAdapter:
    pairing_matrix: Matrix
    discovery_paths: tuple[str, ...]
    discovery_modes: tuple[str, ...]
    certificate: dict

    @classmethod
    def from_retained(cls, marking: dict, bundle: dict) -> "AutEquivariantPairingAdapter":
        gram = Matrix(bundle["picard_gram_64x64"])
        if gram.shape != (PICARD_RANK, PICARD_RANK) or gram != gram.T:
            raise ValueError("retained Picard Gram regression")

        valid: dict[str, dict[str, set[str]]] = {}
        matrices: dict[str, Matrix] = {}
        for path, source_mode, candidate in _pairing_matrix_candidates(marking):
            for algebra_mode in ("DIRECT_PAIRING_MATRIX", "CURVE_COORDINATES_TIMES_GRAM"):
                m = candidate if algebra_mode == "DIRECT_PAIRING_MATRIX" else candidate * gram
                ok = True
                for basis_pos, known_label in enumerate(INDLIST):
                    expected = [int(gram[basis_pos, j]) for j in range(PICARD_RANK)]
                    got = [int(m[known_label - 1, j]) for j in range(PICARD_RANK)]
                    if got != expected:
                        ok = False
                        break
                if not ok:
                    continue
                digest = csha(matrix_list(m))
                matrices[digest] = m
                entry = valid.setdefault(digest, {"paths": set(), "modes": set()})
                entry["paths"].add(path)
                entry["modes"].add(f"{source_mode}:{algebra_mode}")

        propagation_certificate = None
        if not valid:
            propagated, propagation_certificate = _propagate_full_pairing_from_basis_gram(marking, gram)
            digest = csha(matrix_list(propagated))
            matrices[digest] = propagated
            valid[digest] = {
                "paths": {"$.aut_action.permutations_1based + retained.picard_gram_64x64"},
                "modes": {"AUT_ORBIT_PROPAGATION_FROM_RETAINED_BASIS_GRAM"},
            }

        if len(valid) != 1:
            summary = {
                k: {"paths": sorted(v["paths"]), "modes": sorted(v["modes"])}
                for k, v in valid.items()
            }
            raise ValueError(f"expected one exact all-140 pairing matrix, found {len(valid)}: {summary}")

        digest = next(iter(valid))
        meta = valid[digest]
        pairing = matrices[digest]
        for basis_pos, known_label in enumerate(INDLIST):
            expected = [int(gram[basis_pos, j]) for j in range(PICARD_RANK)]
            got = [int(pairing[known_label - 1, j]) for j in range(PICARD_RANK)]
            if got != expected:
                raise ValueError(f"basis-row regression failed for known label {known_label}")

        cert = {
            "mode": "EXACT_RETAINED_ALL140_PAIRINGS_TO_PICARD64",
            "known_curve_count": KNOWN_CURVE_COUNT,
            "picard_rank": PICARD_RANK,
            "basis_known_indices_1based": list(INDLIST),
            "discovery_paths": sorted(meta["paths"]),
            "discovery_modes": sorted(meta["modes"]),
            "pairing_matrix_sha256": digest,
            "basis_row_regression_count": len(INDLIST),
            "basis_row_regression_exact": True,
            "orbit_propagation_certificate": propagation_certificate,
        }
        cert["canonical_sha256_without_this_field"] = csha(cert)
        return cls(
            pairing_matrix=pairing,
            discovery_paths=tuple(sorted(meta["paths"])),
            discovery_modes=tuple(sorted(meta["modes"])),
            certificate=cert,
        )


@dataclass(frozen=True)
class EquivariantMembershipCheck:
    depth: int
    known_labels_1based: tuple[int, ...]
    modulus: int
    coefficients: tuple[tuple[int, ...], ...]
    image_index: int
    hnf_sha256: str

    def feasible(self, values: Sequence[int]) -> bool:
        if len(values) != self.depth:
            raise ValueError("prefix length mismatch")
        if self.modulus == 1:
            return True
        for row in self.coefficients:
            if sum(a * int(v) for a, v in zip(row, values)) % self.modulus:
                return False
        return True


class EquivariantPrefixMembershipOracle:
    def __init__(self, adapter: AutEquivariantPairingAdapter, known_labels_1based: Sequence[int]):
        labels = tuple(int(v) for v in known_labels_1based)
        if len(set(labels)) != len(labels) or any(v < 1 or v > KNOWN_CURVE_COUNT for v in labels):
            raise ValueError("known labels must be distinct and in 1..140")
        self.adapter = adapter
        self.labels = labels
        self.checks = tuple(self._build_check(k) for k in range(1, len(labels) + 1))

    def _build_check(self, depth: int) -> EquivariantMembershipCheck:
        labels = self.labels[:depth]
        A = self.adapter.pairing_matrix[[v - 1 for v in labels], :]
        hnf = hermite_normal_form(A)
        if hnf.shape != (depth, depth) or hnf.det() == 0:
            raise ValueError(f"pairing-prefix row rank regression at depth {depth}: {hnf.shape}")
        inv = hnf.inv()
        modulus = 1
        for value in inv:
            modulus = math.lcm(modulus, int(sympy.denom(value)))
        inv_int = inv * modulus
        if any(sympy.denom(v) != 1 for v in inv_int):
            raise ValueError("HNF inverse integer scaling regression")
        inv_int = Matrix([[int(inv_int[i, j]) for j in range(depth)] for i in range(depth)])
        coeff_rows = tuple(
            tuple(int(inv_int[i, j]) % modulus for j in range(depth))
            for i in range(depth)
            if modulus != 1 and any(int(inv_int[i, j]) % modulus for j in range(depth))
        )
        return EquivariantMembershipCheck(
            depth=depth,
            known_labels_1based=labels,
            modulus=modulus,
            coefficients=coeff_rows,
            image_index=abs(int(hnf.det())),
            hnf_sha256=csha(matrix_list(hnf)),
        )

    def feasible(self, values: Sequence[int]) -> bool:
        if not values:
            return True
        return self.checks[len(values) - 1].feasible(values)

    def certificate(self) -> dict:
        return {
            "mode": "EXACT_HNF_INTEGER_IMAGE_OF_ALL140_PAIRING_ROWS",
            "known_labels_1based": list(self.labels),
            "checks": [
                {
                    "depth": c.depth,
                    "known_labels_1based": list(c.known_labels_1based),
                    "modulus": c.modulus,
                    "active_congruence_rows": len(c.coefficients),
                    "image_index": c.image_index,
                    "hnf_sha256": c.hnf_sha256,
                }
                for c in self.checks
            ],
        }


@dataclass(frozen=True)
class EquivariantAutCheck:
    depth: int
    known_labels_1based: tuple[int, ...]
    stabilizer_size: int
    actions_on_prefix: tuple[tuple[int, ...], ...]

    def canonical(self, values: Sequence[int]) -> bool:
        base = tuple(int(v) for v in values)
        return all(base <= tuple(base[i] for i in action) for action in self.actions_on_prefix)


class AutEquivariantPrefixCanonicalAugmentation:
    def __init__(
        self,
        permutations_1based: Sequence[Sequence[int]],
        known_labels_1based: Sequence[int],
        aut_certificate_sha256: str,
    ) -> None:
        labels = tuple(int(v) for v in known_labels_1based)
        group = close_permutation_group(permutations_1based)
        if len(group) != EXPECTED_AUT_GROUP_ORDER:
            raise ValueError(f"retained Aut group order regression: {len(group)}")
        if len(group[0]) != KNOWN_CURVE_COUNT:
            raise ValueError("retained Aut permutation degree regression")

        normal = set(range(NORMAL_LABEL_MAX))
        exceptional = set(range(NORMAL_LABEL_MAX, KNOWN_CURVE_COUNT))
        budget_group = tuple(
            g for g in group
            if {g[i] for i in normal} == normal and {g[i] for i in exceptional} == exceptional
        )
        if not budget_group:
            raise ValueError("identity missing from global budget-class-preserving subgroup")

        checks: list[EquivariantAutCheck] = []
        n = KNOWN_CURVE_COUNT
        for depth in range(1, len(labels) + 1):
            prefix = tuple(v - 1 for v in labels[:depth])
            prefix_set = set(prefix)
            label_to_pos = {label: i for i, label in enumerate(prefix)}
            actions: set[tuple[int, ...]] = set()
            stabilizer_size = 0
            for g in budget_group:
                if {g[label] for label in prefix_set} != prefix_set:
                    continue
                stabilizer_size += 1
                inv = [0] * n
                for src, target in enumerate(g):
                    inv[target] = src
                actions.add(tuple(label_to_pos[inv[target]] for target in prefix))
            if not actions:
                raise ValueError(f"prefix stabilizer vanished at depth {depth}")
            checks.append(
                EquivariantAutCheck(
                    depth=depth,
                    known_labels_1based=tuple(v + 1 for v in prefix),
                    stabilizer_size=stabilizer_size,
                    actions_on_prefix=tuple(sorted(actions)),
                )
            )

        self.group_order = len(group)
        self.global_budget_subgroup_size = len(budget_group)
        self.labels = labels
        self.checks = tuple(checks)
        self.aut_certificate_sha256 = str(aut_certificate_sha256)

    def canonical(self, values: Sequence[int]) -> bool:
        if not values:
            return True
        return self.checks[len(values) - 1].canonical(values)

    def certificate(self) -> dict:
        payload = {
            "mode": "EXACT_AUT1536_ALL140_GLOBAL_BUDGET_CLASS_PREFIX_STABILIZER_LEX_MIN",
            "retained_aut_certificate_sha256": self.aut_certificate_sha256,
            "full_aut_group_order": self.group_order,
            "global_budget_class_preserving_subgroup_size": self.global_budget_subgroup_size,
            "known_labels_1based": list(self.labels),
            "checks": [
                {
                    "depth": c.depth,
                    "known_labels_1based": list(c.known_labels_1based),
                    "stabilizer_size": c.stabilizer_size,
                    "distinct_prefix_actions": len(c.actions_on_prefix),
                    "actions_sha256": csha([list(a) for a in c.actions_on_prefix]),
                }
                for c in self.checks
            ],
        }
        payload["canonical_sha256_without_this_field"] = csha(payload)
        return payload
