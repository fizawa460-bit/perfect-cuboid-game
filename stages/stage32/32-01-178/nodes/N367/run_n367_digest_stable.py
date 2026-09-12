#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
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


def output_path() -> Path:
    req("--output" in sys.argv, "--output missing")
    i = sys.argv.index("--output")
    req(i + 1 < len(sys.argv), "--output value missing")
    return Path(sys.argv[i + 1])


def main() -> None:
    req(blob(GENERATOR) == EXPECTED_GENERATOR_BLOB, "N367 generator blob drift")
    spec = importlib.util.spec_from_file_location("n367_generator_stable", GENERATOR)
    req(spec is not None and spec.loader is not None, "cannot import N367 generator")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["n367_generator_stable"] = mod
    spec.loader.exec_module(mod)

    replay_meta = {}

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
        current = sorted(unresolved)
        req(1 <= len(current) <= 12,
            f"finite-ring replay unresolved set outside bounded exact-probe gate: {len(current)}")
        replay_meta.update({
            "source_cut196_residual_count": mod.EXPECTED_RESIDUAL_COUNT,
            "source_cut196_residual_parent_ordinal_sha256": mod.EXPECTED_RESIDUAL_STREAM,
            "independent_replay_unresolved_count": len(current),
            "independent_replay_unresolved_ordinals": current,
            "independent_replay_unresolved_sha256": stream_digest(current),
            "source_digest_reproduced_exactly": stream_digest(current) == mod.EXPECTED_RESIDUAL_STREAM,
            "semantics": "CUT196 source residuals are route-selection only; every parent proved finite-ring UNSAT in this exact-head replay is safely excluded by a necessary condition, and every unresolved parent is sent to exact selected64 solve"
        })
        print(json.dumps(replay_meta, sort_keys=True))
        return current

    mod.residual_ordinals = stable_residual_ordinals
    mod.main()

    out = output_path()
    body = json.loads(out.read_text())
    body["schema"] = "STAGE32_32_01_178_N367_BLOCK1155_INDEPENDENT_FINITE_RING_RESIDUAL_WITNESS_RESULT_V1"
    body["route_replay"] = replay_meta
    if body.get("witness") is not None:
        body["status"] = "SAT_CURRENT_V15_WITNESS_CANDIDATE"
    elif any(a.get("exact_result") == "unknown" for a in body.get("attempts", [])):
        body["status"] = "UNKNOWN_REMAINS_IN_INDEPENDENT_RESIDUAL_PROBE"
    else:
        body["status"] = "NO_SAT_IN_INDEPENDENT_RESIDUAL_PROBE"
    body.pop("canonical_sha256_without_this_field", None)
    body["canonical_sha256_without_this_field"] = mod.csha(body)
    out.write_text(json.dumps(body, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"final_status": body["status"], "exact_parent_ordinals": body["target"]["parent_ordinals"], "canonical": body["canonical_sha256_without_this_field"]}, sort_keys=True))


if __name__ == "__main__":
    main()
