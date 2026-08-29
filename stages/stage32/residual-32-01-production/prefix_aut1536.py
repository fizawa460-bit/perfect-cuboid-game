#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Sequence

from pairing_prefix_engine import close_permutation_group

EXPECTED_AUT_GROUP_ORDER = 1536


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


@dataclass(frozen=True)
class PrefixAutCheck:
    depth: int
    assigned_known_indices_1based: tuple[int, ...]
    stabilizer_size: int
    actions_on_prefix: tuple[tuple[int, ...], ...]

    def canonical(self, values: Sequence[int]) -> bool:
        base = tuple(int(v) for v in values)
        assert len(base) == self.depth
        return all(base <= tuple(base[i] for i in action) for action in self.actions_on_prefix)


class PrefixAut1536CanonicalAugmentation:
    """Exact, conservative prefix canonical augmentation from retained Aut(S).

    The retained permutations act on the 140 known curve labels.  The cost
    probe only assigns a selected 64-coordinate primitive basis with separate
    exceptional/curve mass budgets, so we deliberately use only Aut elements
    preserving the entire selected 64-set and its two budget classes setwise.
    At depth k we further restrict to elements preserving the assigned prefix
    label-set setwise.  Such an element induces a genuine permutation of the
    k assigned values, so lexicographic orbit minimization is exact and needs
    no guessed values for unassigned coordinates.
    """

    def __init__(
        self,
        permutations_1based: Sequence[Sequence[int]],
        selected_known_indices_1based: Sequence[int],
        exceptional_coordinate_count: int,
        assignment_order: Sequence[int],
        aut_certificate_sha256: str,
    ) -> None:
        selected = tuple(int(v) for v in selected_known_indices_1based)
        assert len(selected) == 64 and len(set(selected)) == 64
        ecount = int(exceptional_coordinate_count)
        assert 0 < ecount < len(selected)
        order = tuple(int(v) for v in assignment_order)
        assert len(set(order)) == len(order)
        assert all(0 <= i < 64 for i in order)

        group = close_permutation_group(permutations_1based)
        if len(group) != EXPECTED_AUT_GROUP_ORDER:
            raise ValueError(f"retained Aut group order regression: {len(group)}")
        n = len(group[0])
        if max(selected) > n:
            raise ValueError("selected known index exceeds retained Aut permutation degree")

        selected0 = {v - 1 for v in selected}
        exceptional0 = {selected[i] - 1 for i in range(ecount)}
        curve0 = selected0 - exceptional0
        compatible = tuple(
            g for g in group
            if {g[i] for i in selected0} == selected0
            and {g[i] for i in exceptional0} == exceptional0
            and {g[i] for i in curve0} == curve0
        )
        if not compatible:
            raise ValueError("identity missing from selected-coordinate-compatible Aut subgroup")

        checks: list[PrefixAutCheck] = []
        for depth in range(1, len(order) + 1):
            positions = order[:depth]
            labels = tuple(selected[pos] - 1 for pos in positions)
            label_set = set(labels)
            label_to_prefix = {label: i for i, label in enumerate(labels)}
            actions = set()
            stabilizer_size = 0
            for g in compatible:
                if {g[label] for label in label_set} != label_set:
                    continue
                stabilizer_size += 1
                # y'_target = y_{g^{-1}(target)}.  Record source prefix index
                # for each target slot.
                inv = [0] * n
                for src, target in enumerate(g):
                    inv[target] = src
                action = tuple(label_to_prefix[inv[target]] for target in labels)
                actions.add(action)
            if not actions:
                raise ValueError(f"prefix stabilizer vanished at depth {depth}")
            checks.append(
                PrefixAutCheck(
                    depth=depth,
                    assigned_known_indices_1based=tuple(v + 1 for v in labels),
                    stabilizer_size=stabilizer_size,
                    actions_on_prefix=tuple(sorted(actions)),
                )
            )

        self.group_order = len(group)
        self.compatible_subgroup_size = len(compatible)
        self.permutation_degree = n
        self.order = order
        self.checks = tuple(checks)
        self.aut_certificate_sha256 = str(aut_certificate_sha256)
        self.selected_known_indices_1based = selected
        self.exceptional_coordinate_count = ecount

    def canonical(self, values: Sequence[int]) -> bool:
        if not values:
            return True
        return self.checks[len(values) - 1].canonical(values)

    def certificate(self) -> dict:
        payload = {
            "mode": "EXACT_AUT1536_SELECTED64_BUDGET_CLASS_COMPATIBLE_PREFIX_STABILIZER_LEX_MIN",
            "retained_aut_certificate_sha256": self.aut_certificate_sha256,
            "full_aut_group_order": self.group_order,
            "permutation_degree": self.permutation_degree,
            "selected_coordinate_compatible_subgroup_size": self.compatible_subgroup_size,
            "exceptional_coordinate_count": self.exceptional_coordinate_count,
            "assignment_order": list(self.order),
            "checks": [
                {
                    "depth": c.depth,
                    "assigned_known_indices_1based": list(c.assigned_known_indices_1based),
                    "stabilizer_size": c.stabilizer_size,
                    "distinct_prefix_actions": len(c.actions_on_prefix),
                    "actions_sha256": csha([list(a) for a in c.actions_on_prefix]),
                }
                for c in self.checks
            ],
        }
        payload["canonical_sha256_without_this_field"] = csha(payload)
        return payload
