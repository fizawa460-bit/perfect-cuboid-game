#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import pathlib
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from resumable_prefix_engine import run_resumable_dfs


LABELS = [0, 1, 2, 3]


def upper_for_prefix(prefix: list[int]) -> int:
    # Small deterministic tree with varying width by depth/value.
    remaining = max(0, 5 - sum(prefix))
    return min(3, remaining)


def feasible(prefix: list[int]) -> bool:
    # Exact deterministic pruning, deliberately nontrivial across depths.
    return sum(prefix) <= 5 and (len(prefix) < 3 or (prefix[0] + prefix[-1]) % 3 != 2)


def canonical(prefix: list[int]) -> bool:
    # Prefix-local canonicalization surrogate: keep a lexicographic chamber.
    return len(prefix) < 2 or prefix[0] <= prefix[1] + 1


def digest(terminals: list[tuple[int, ...]]) -> str:
    h = hashlib.sha256()
    for terminal in terminals:
        h.update(json.dumps(list(terminal), separators=(",", ":")).encode() + b"\n")
    return h.hexdigest()


class ResumablePrefixEngineTest(unittest.TestCase):
    def one_shot(self):
        return run_resumable_dfs(
            labels=LABELS,
            fixed_prefix=[],
            root_lo=0,
            root_hi=3,
            node_limit=1_000_000,
            upper_for_prefix=upper_for_prefix,
            feasible=feasible,
            canonical=canonical,
            capture_terminals=True,
        )

    def segmented(self, budget: int):
        state = None
        terminals: list[tuple[int, ...]] = []
        calls = 0
        incomplete_children = []
        while True:
            out = run_resumable_dfs(
                labels=LABELS,
                fixed_prefix=[],
                root_lo=0,
                root_hi=3,
                node_limit=budget,
                upper_for_prefix=upper_for_prefix,
                feasible=feasible,
                canonical=canonical,
                continuation=state,
                capture_terminals=True,
            )
            calls += 1
            terminals.extend(out.terminals)
            incomplete_children.append(0 if out.complete else 1)
            if out.complete:
                return terminals, calls, incomplete_children
            self.assertIsNotNone(out.continuation)
            state = out.continuation

    def test_segmented_terminal_stream_matches_one_shot(self):
        expected = self.one_shot()
        self.assertTrue(expected.complete)
        for budget in (1, 2, 3, 5, 7, 11):
            terminals, calls, _ = self.segmented(budget)
            self.assertGreater(calls, 1)
            self.assertEqual(terminals, list(expected.terminals))
            self.assertEqual(digest(terminals), expected.terminal_stream_sha256)

    def test_incomplete_call_has_at_most_one_child(self):
        terminals, calls, children = self.segmented(3)
        self.assertGreater(calls, 2)
        self.assertTrue(terminals)
        self.assertTrue(all(v in (0, 1) for v in children))
        self.assertEqual(max(children), 1)

    def test_resume_state_is_deterministic(self):
        first = run_resumable_dfs(
            labels=LABELS,
            fixed_prefix=[],
            root_lo=0,
            root_hi=3,
            node_limit=5,
            upper_for_prefix=upper_for_prefix,
            feasible=feasible,
            canonical=canonical,
            capture_terminals=True,
        )
        second = run_resumable_dfs(
            labels=LABELS,
            fixed_prefix=[],
            root_lo=0,
            root_hi=3,
            node_limit=5,
            upper_for_prefix=upper_for_prefix,
            feasible=feasible,
            canonical=canonical,
            capture_terminals=True,
        )
        self.assertFalse(first.complete)
        self.assertEqual(first.continuation, second.continuation)
        self.assertEqual(first.terminals, second.terminals)

    def test_fixed_prefix_resume_matches_one_shot(self):
        fixed = [1]
        expected = run_resumable_dfs(
            labels=LABELS,
            fixed_prefix=fixed,
            root_lo=0,
            root_hi=3,
            node_limit=1_000_000,
            upper_for_prefix=upper_for_prefix,
            feasible=feasible,
            canonical=canonical,
            capture_terminals=True,
        )
        state = None
        terminals: list[tuple[int, ...]] = []
        while True:
            out = run_resumable_dfs(
                labels=LABELS,
                fixed_prefix=fixed,
                root_lo=0,
                root_hi=3,
                node_limit=2,
                upper_for_prefix=upper_for_prefix,
                feasible=feasible,
                canonical=canonical,
                continuation=state,
                capture_terminals=True,
            )
            terminals.extend(out.terminals)
            if out.complete:
                break
            state = out.continuation
        self.assertEqual(terminals, list(expected.terminals))


if __name__ == "__main__":
    unittest.main()
