#!/usr/bin/env python3
from __future__ import annotations

import itertools
import pathlib
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from compressed_terminal_family import stratum_terminal_count, terminal_predicate  # noqa: E402
from compressed_terminal_indexer import CompressedTerminalIndexer  # noqa: E402


class CompressedTerminalIndexerTest(unittest.TestCase):
    def test_small_family_is_exact_and_bijective(self) -> None:
        e, d = 2, 1
        indexer = CompressedTerminalIndexer(e=e, d=d)
        expected = []
        normal_budget = 19 * d - 5 * e
        # Exceptional sum<=2 means each exceptional coordinate is individually
        # <=2, so this finite box is exhaustive for the small calibration.
        for exceptional in itertools.product(range(e + 1), repeat=10):
            for x4 in range(normal_budget + 1):
                x = (
                    exceptional[0], exceptional[1], exceptional[2], exceptional[3],
                    x4,
                    exceptional[4], exceptional[5], exceptional[6], exceptional[7],
                    exceptional[8], exceptional[9],
                )
                if terminal_predicate(x, e=e, d=d):
                    expected.append(x)
        self.assertEqual(indexer.terminal_count, len(expected))
        generated = [indexer.unrank(i) for i in range(indexer.terminal_count)]
        self.assertEqual(len(set(generated)), len(generated))
        self.assertEqual(set(generated), set(expected))
        for i, x in enumerate(generated):
            self.assertEqual(indexer.rank(x), i)

    def test_branch_counts_match_locked_symbolic_count(self) -> None:
        for e, d in [
            (0, 1), (1, 1), (2, 1), (3, 1), (8, 3), (31, 10),
            (63, 20), (128, 40), (256, 80), (511, 160), (663, 192), (729, 192),
        ]:
            with self.subTest(e=e, d=d):
                indexer = CompressedTerminalIndexer(e=e, d=d)
                cert = indexer.certificate()
                self.assertEqual(
                    indexer.terminal_count,
                    stratum_terminal_count(e=e, d=d),
                )
                self.assertEqual(
                    int(cert["unequal_exceptional_count"]) + int(cert["equal_exceptional_count"]),
                    int(cert["exceptional_terminal_count"]),
                )

    def test_random_access_roundtrip_at_large_stage32_strata(self) -> None:
        for e, d in [(663, 192), (729, 192)]:
            indexer = CompressedTerminalIndexer(e=e, d=d)
            n = indexer.terminal_count
            ranks = sorted({0, 1, n // 7, n // 2, (6 * n) // 7, n - 2, n - 1})
            for rank in ranks:
                with self.subTest(e=e, d=d, rank=rank):
                    x = indexer.unrank(rank)
                    self.assertTrue(terminal_predicate(x, e=e, d=d))
                    self.assertEqual(indexer.rank(x), rank)


if __name__ == "__main__":
    unittest.main()
