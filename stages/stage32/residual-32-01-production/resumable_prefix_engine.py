#!/usr/bin/env python3
from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass
from typing import Callable


STATE_SCHEMA = "STAGE32_RESUMABLE_DFS_STATE_V1"


@dataclass(frozen=True)
class ResumableResult:
    complete: bool
    nodes: int
    membership_prunes: int
    symmetry_prunes: int
    terminal_count: int
    terminal_stream_sha256: str
    continuation: dict | None
    terminals: tuple[tuple[int, ...], ...]


def _frame(depth: int, lo: int, hi: int) -> dict:
    return {"depth": int(depth), "next_value": int(lo), "hi": int(hi)}


def _validate_state(state: dict, *, labels_len: int, fixed_prefix: list[int]) -> None:
    assert state["schema"] == STATE_SCHEMA
    values = [int(v) for v in state["values"]]
    stack = state["stack"]
    assert values[: len(fixed_prefix)] == fixed_prefix
    assert stack
    assert int(stack[0]["depth"]) == len(fixed_prefix)
    assert int(stack[-1]["depth"]) == len(values)
    assert all(0 <= int(f["depth"]) < labels_len for f in stack)
    assert all(int(f["next_value"]) <= int(f["hi"]) + 1 for f in stack)
    for left, right in zip(stack, stack[1:]):
        assert int(right["depth"]) == int(left["depth"]) + 1


def run_resumable_dfs(
    *,
    labels: list[int],
    fixed_prefix: list[int],
    root_lo: int,
    root_hi: int,
    node_limit: int,
    upper_for_prefix: Callable[[list[int]], int],
    feasible: Callable[[list[int]], bool],
    canonical: Callable[[list[int]], bool],
    continuation: dict | None = None,
    capture_terminals: bool = False,
) -> ResumableResult:
    """Run the same lexicographic DFS as the Stage32 prefix engine, but suspend
    by serializing its exact traversal cursor instead of bisecting the search
    region into multiple children.

    A non-complete call therefore emits exactly one continuation. Repeated calls
    preserve the same terminal order as a single unlimited call. No continuation
    is interpreted as UNSAT; it means only that this exact DFS segment completed.
    """
    assert node_limit >= 0
    labels_len = len(labels)
    assert len(fixed_prefix) < labels_len

    if continuation is None:
        values = [int(v) for v in fixed_prefix]
        stack = [_frame(len(fixed_prefix), int(root_lo), int(root_hi))]
    else:
        state = copy.deepcopy(continuation)
        _validate_state(state, labels_len=labels_len, fixed_prefix=fixed_prefix)
        values = [int(v) for v in state["values"]]
        stack = [
            {
                "depth": int(f["depth"]),
                "next_value": int(f["next_value"]),
                "hi": int(f["hi"]),
            }
            for f in state["stack"]
        ]

    nodes = membership = symmetry = terminals = 0
    terminal_hash = hashlib.sha256()
    captured: list[tuple[int, ...]] = []

    while stack:
        top = stack[-1]
        depth = int(top["depth"])
        assert depth == len(values)

        if int(top["next_value"]) > int(top["hi"]):
            stack.pop()
            if depth > len(fixed_prefix):
                values.pop()
            continue

        if nodes >= node_limit:
            state = {
                "schema": STATE_SCHEMA,
                "values": list(values),
                "stack": copy.deepcopy(stack),
            }
            _validate_state(state, labels_len=labels_len, fixed_prefix=fixed_prefix)
            return ResumableResult(
                complete=False,
                nodes=nodes,
                membership_prunes=membership,
                symmetry_prunes=symmetry,
                terminal_count=terminals,
                terminal_stream_sha256=terminal_hash.hexdigest(),
                continuation=state,
                terminals=tuple(captured),
            )

        value = int(top["next_value"])
        top["next_value"] = value + 1
        nodes += 1
        values.append(value)

        if not feasible(values):
            membership += 1
            values.pop()
            continue
        if not canonical(values):
            symmetry += 1
            values.pop()
            continue

        if len(values) == labels_len:
            terminals += 1
            encoded = json.dumps(values, separators=(",", ":")).encode() + b"\n"
            terminal_hash.update(encoded)
            if capture_terminals:
                captured.append(tuple(values))
            values.pop()
            continue

        upper = int(upper_for_prefix(values))
        assert upper >= 0
        stack.append(_frame(len(values), 0, upper))

    return ResumableResult(
        complete=True,
        nodes=nodes,
        membership_prunes=membership,
        symmetry_prunes=symmetry,
        terminal_count=terminals,
        terminal_stream_sha256=terminal_hash.hexdigest(),
        continuation=None,
        terminals=tuple(captured),
    )
