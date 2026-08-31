#!/usr/bin/env python3
from __future__ import annotations

import pathlib
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from aut_equivariant_pairing_adapter import (  # noqa: E402
    AutEquivariantPrefixCanonicalAugmentation,
    EquivariantPrefixMembershipOracle,
)
from compressed_terminal_family import (  # noqa: E402
    build_exceptional_count_table,
    stratum_terminal_count,
    terminal_predicate,
)
from hperp_integral_adapter import HperpIntegralPairingAdapter  # noqa: E402
from pairing_prefix_engine import RETAINED_BUNDLE_SHA256  # noqa: E402
from run_full178_prefix_work_unit import (  # noqa: E402
    KNOWN_LABEL_ORDER,
    load_module_payload,
    run_partition,
)

ROOT = HERE.parents[2]
RETAINED = ROOT / "stages" / "stage33" / "33-07" / "picard_base_rows_retained.py"
MARKING = ROOT / "stages" / "stage33" / "33-07" / "stage32_picard_marking_retained.py"


class CompressedTerminalFamilyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        bundle = load_module_payload(RETAINED, "stage32_compressed_family_picard")
        assert bundle["canonical_sha256"] == RETAINED_BUNDLE_SHA256
        marking = load_module_payload(MARKING, "stage32_compressed_family_marking")
        adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
        cls.oracle = EquivariantPrefixMembershipOracle(adapter, KNOWN_LABEL_ORDER)
        cls.aut = AutEquivariantPrefixCanonicalAugmentation(
            marking["aut_action"]["permutations_1based"],
            KNOWN_LABEL_ORDER,
            marking["aut_action"]["canonical_sha256_without_this_field"],
        )

    def test_certificate_structure_reduces_to_documented_constraints(self) -> None:
        self.assertEqual([c.modulus for c in self.oracle.checks], [1] * 10 + [2])
        self.assertEqual(
            self.oracle.checks[-1].coefficients,
            ((0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1),),
        )
        identity = lambda n: tuple(range(n))
        swap01 = lambda n: (1, 0) + tuple(range(2, n))
        for depth, check in enumerate(self.aut.checks, start=1):
            actions = set(check.actions_on_prefix)
            if depth == 1:
                self.assertEqual(actions, {identity(depth)})
            elif 2 <= depth <= 5:
                self.assertEqual(actions, {identity(depth), swap01(depth)})
            elif 6 <= depth <= 9:
                self.assertEqual(actions, {identity(depth)})
            elif depth == 10:
                self.assertEqual(
                    actions,
                    {
                        identity(10),
                        (1, 0, 2, 3, 4, 8, 9, 7, 5, 6),
                    },
                )
            else:
                self.assertEqual(actions, {identity(depth)})

    def test_symbolic_counts_match_current_exact_dfs(self) -> None:
        cases = [(1, 0), (1, 3), (2, 4), (2, 7), (3, 8), (3, 11)]
        for d, e in cases:
            with self.subTest(d=d, e=e):
                exact = run_partition(
                    self.oracle,
                    self.aut,
                    list(KNOWN_LABEL_ORDER),
                    e=e,
                    d=d,
                    node_limit=50_000_000,
                    prefix=[],
                    next_min=None,
                    next_max=None,
                )
                self.assertTrue(exact["complete"], exact)
                self.assertEqual(exact["terminal_count"], stratum_terminal_count(e=e, d=d))

    def test_terminal_predicate_matches_every_exact_prefix_filter_on_small_box(self) -> None:
        e, d = 2, 1
        vals = [0] * 11
        seen = 0

        def rec(depth: int) -> None:
            nonlocal seen
            if depth == 11:
                expected = True
                for k in range(1, 12):
                    prefix = vals[:k]
                    if not self.oracle.feasible(prefix) or not self.aut.canonical(prefix):
                        expected = False
                        break
                exceptional_sum = sum(vals[i] for i in range(11) if i != 4)
                budget_ok = exceptional_sum <= e and vals[4] <= 19 * d - 5 * e
                expected = expected and budget_ok
                self.assertEqual(terminal_predicate(vals, e=e, d=d), expected, tuple(vals))
                seen += 1
                return
            for v in range(3):
                vals[depth] = v
                rec(depth + 1)

        rec(0)
        self.assertEqual(seen, 3 ** 11)

    def test_precompute_reaches_full_stage32_e_ceiling(self) -> None:
        table = build_exceptional_count_table(729)
        self.assertEqual(table.max_e, 729)
        self.assertEqual(len(table.counts), 730)
        self.assertTrue(all(a <= b for a, b in zip(table.counts, table.counts[1:])))


if __name__ == "__main__":
    unittest.main()
