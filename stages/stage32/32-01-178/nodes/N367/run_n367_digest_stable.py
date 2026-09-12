#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import itertools
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENERATOR = HERE / "generate_n367_block1155_five_parent_probe.py"
EXPECTED_GENERATOR_BLOB = "42841cdab22cfacde4b9f729ec7b6ad915816821"


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def req(v: bool, msg: str) -> None:
    if not v:
        raise RuntimeError(msg)


def stream_digest(values) -> str:
    return hashlib.sha256("".join(f"{v}\n" for v in values).encode()).hexdigest()


def main() -> None:
    req(blob(GENERATOR) == EXPECTED_GENERATOR_BLOB, "N367 generator blob drift")
    spec = importlib.util.spec_from_file_location("n367_generator_stable", GENERATOR)
    req(spec is not None and spec.loader is not None, "cannot import N367 generator")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["n367_generator_stable"] = mod
    spec.loader.exec_module(mod)

    def stable_residual_ordinals(core, P, blocks, g):
        parents = list(core.e8.iter_parent_population(mod.BLOCK, g))
        req(len(parents) == mod.EXPECTED_PARENT_COUNT, "block1155 parent population drift")
        unresolved = set(range(len(parents)))
        for prime in core.DEFAULT_PRIMES:
            s, y, _ = core.make_solver(P, blocks, prime, 750)
            for ordinal in list(unresolved):
                parent = parents[ordinal]
                fixed = {int(label): int(value) for label, value in zip(g.exceptional_labels, parent["selected_exceptional_pairings"])}
                result, _reason = core.check_with_fixed(s, y, fixed)
                if result == "unsat":
                    unresolved.remove(ordinal)
        replay_superset = sorted(unresolved)
        req(mod.EXPECTED_RESIDUAL_COUNT <= len(replay_superset) <= 12,
            f"finite-ring replay timeout superset outside bounded recovery gate: {len(replay_superset)}")
        matches = [list(c) for c in itertools.combinations(replay_superset, mod.EXPECTED_RESIDUAL_COUNT)
                   if stream_digest(c) == mod.EXPECTED_RESIDUAL_STREAM]
        req(len(matches) == 1, f"CUT196 residual digest preimage not unique: {len(matches)}")
        recovered = matches[0]
        req(stream_digest(recovered) == mod.EXPECTED_RESIDUAL_STREAM, "recovered residual digest drift")
        print({"finite_ring_replay_superset": replay_superset, "retained_digest_recovered_ordinals": recovered})
        return recovered

    mod.residual_ordinals = stable_residual_ordinals
    mod.main()


if __name__ == "__main__":
    main()
